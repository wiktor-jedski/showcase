from typing import List
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from django.contrib.staticfiles import finders
from io import StringIO


def programming_languages_analysis(*args: List[str]):
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

    # find number of months per language
    months_per_language = dataset.groupby(['Programming Language']).agg('count')\
        .sort_values('Query Count', ascending=False)['Month']

    # change Month column type to datetime
    dataset['Month'] = pd.to_datetime(dataset['Month'])

    # plots
    counts = []
    if not args:
        args = ['java', 'python']
    for arg in args:
        counts.append(dataset[dataset['Programming Language'] == arg])

    colors = list(mcolors.TABLEAU_COLORS.values())
    fig1 = plt.figure()
    for i in range(len(counts)):
        plt.plot(counts[i]['Month'].values, counts[i]['Query Count'].values,
                 color=colors[i], label=args[i])
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
                 color=colors[i], label=args[i])
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
               'months_per_language': months_per_language, 'plot_raw': plot_raw, 'plot_rolling': plot_rolling}
    return context
