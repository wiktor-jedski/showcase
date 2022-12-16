from typing import List, Dict
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from django.contrib.staticfiles import finders
from io import StringIO


def programming_languages_analysis(choices: List[str] = None) -> Dict:
    """
    Takes a list of programming languages names.
    Returns an analysis of usage of given names in StackOverflow.
    """
    # loading the file
    result = finders.find('data/QueryResults.csv')
    dataset = pd.read_csv(result)

    # initial data exploration
    head = dataset.head()
    tail = dataset.tail()
    shape = dataset.shape
    data_types = dataset.dtypes
    column_names = dataset.columns
    entry_count = []
    for i in range(len(column_names)):
        entry_count.append(dataset.iloc[:, i].count())
    is_duplicated = dataset.duplicated().any()
    is_na = dataset.isna().any()

    # change column names
    dataset.columns = ['Month', 'Programming Language', 'Query Count']

    # find number of posts per language
    posts_per_language = dataset.groupby(['Programming Language']).agg('sum')\
        .sort_values('Query Count', ascending=False)
    posts_per_language = posts_per_language.reset_index()

    # find number of months per language
    months_per_language = dataset.groupby(['Programming Language']).agg('count')\
        .sort_values('Query Count', ascending=False)['Month']
    months_per_language = pd.DataFrame({'Programming Language': months_per_language.index,
                                        'Count': months_per_language.values})

    # change Month column type to datetime
    dataset['Month'] = pd.to_datetime(dataset['Month'])

    # plots
    counts = []
    if not choices:
        choices = ['java', 'python']
    for arg in choices:
        counts.append(dataset[dataset['Programming Language'] == arg])

    colors = list(mcolors.TABLEAU_COLORS.values())
    colors.extend([mcolors.CSS4_COLORS['lime'], mcolors.CSS4_COLORS['navy'],
                   mcolors.CSS4_COLORS['tan'], mcolors.CSS4_COLORS['pink']])
    fig1 = plt.figure()
    for i in range(len(counts)):
        plt.plot(counts[i]['Month'].values, counts[i]['Query Count'].values,
                 color=colors[i], label=choices[i])
    plt.xlabel('Month')
    plt.ylabel('Number of queries')
    plt.title('StackOverflow Threads')
    plt.legend()

    imgdata = StringIO()
    fig1.savefig(imgdata, format='svg')
    imgdata.seek(0)
    plot_raw = imgdata.getvalue()

    fig2 = plt.figure()
    for i in range(len(counts)):
        plt.plot(counts[i]['Month'].values, counts[i]['Query Count'].rolling(6).mean(),
                 color=colors[i], label=choices[i])
    plt.xlabel('Month')
    plt.ylabel('Number of queries')
    plt.title('StackOverflow Threads (with 6 months rolling mean)')
    plt.legend()

    imgdata = StringIO()
    fig2.savefig(imgdata, format='svg')
    imgdata.seek(0)
    plot_rolling = imgdata.getvalue()

    context = {'head': head, 'tail': tail, 'shape': shape, 'column_names': column_names, 'entry_count': entry_count,
               'is_na': is_na, 'is_duplicated': is_duplicated, 'posts_per_language': posts_per_language,
               'months_per_language': months_per_language, 'plot_raw': plot_raw, 'plot_rolling': plot_rolling,
               'data_types': data_types}
    return context
