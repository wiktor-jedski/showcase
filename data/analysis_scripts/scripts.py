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


def google_analysis() -> Dict:
    """
    Returns a dictionary of variables to show the results of analysis of Bitcoin prices and unemployment.
    """
    # finding files
    tesla = finders.find('data/TESLA Search Trend vs Price.csv')
    btc_search = finders.find('data/Bitcoin Search Trend.csv')
    btc_price = finders.find('data/Daily Bitcoin Price.csv')
    unemployment = finders.find('data/UE Benefits Search vs UE Rate 2004-19.csv')
    unemployment_covid = finders.find('data/UE Benefits Search vs UE Rate 2004-20.csv')

    # reading files
    df_tesla = pd.read_csv(tesla)
    df_btc_search = pd.read_csv(btc_search)
    df_btc_price = pd.read_csv(btc_price)
    df_unemployment = pd.read_csv(unemployment)
    df_benefits = pd.read_csv(unemployment_covid)

    # data exploration
    tesla_min = df_tesla.TSLA_WEB_SEARCH.min()
    tesla_max = df_tesla.TSLA_WEB_SEARCH.max()
    tesla_head = df_tesla.head()
    tesla_tail = df_tesla.tail()
    ue_description = df_unemployment.describe()
    ue_description.insert(0, 'Statistic', ue_description.index)
    ue_head = df_unemployment.head()
    ue_tail = df_unemployment.tail()
    btc_search_head = df_btc_search.head()
    btc_search_tail = df_btc_search.tail()
    btc_search_min = df_btc_search.BTC_NEWS_SEARCH.min()
    btc_search_max = df_btc_search.BTC_NEWS_SEARCH.max()
    btc_price_description = df_btc_price.describe()
    btc_price_description.insert(0, 'Statistic', btc_price_description.index)
    btc_price_head = df_btc_price.head()
    btc_price_tail = df_btc_price.tail()

    # missing values check
    tesla_missing = df_tesla.isna().values.any()
    ue_missing = df_unemployment.isna().values.any()
    btc_search_missing = df_btc_search.isna().values.any()
    btc_price_missing = df_btc_price.isna().values.any()
    btc_price_missing_count = df_btc_price.isna().values.sum()
    btc_missing_row = df_btc_price[df_btc_price.CLOSE.isna()].values

    # duplicate check
    tesla_duplicate = df_tesla.duplicated().values.any()
    ue_duplicate = df_unemployment.duplicated().values.any()
    btc_search_duplicate = df_btc_search.duplicated().values.any()
    btc_price_duplicate = df_btc_price.duplicated().values.any()

    # data type check
    tesla_dtypes = df_tesla.dtypes
    ue_dtypes = df_unemployment.dtypes
    btc_search_dtypes = df_btc_search.dtypes
    btc_price_dtypes = df_btc_price.dtypes

    # change date/month column types to datetime
    df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
    df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
    df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE)
    df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)

    # drop nan values
    df_btc_price = df_btc_price.dropna()

    context = {'df_tesla': df_tesla, 'tesla_min': tesla_min, 'tesla_max': tesla_max, 'tesla_head': tesla_head,
               'tesla_tail': tesla_tail, 'df_unemployment': df_unemployment, 'ue_description': ue_description,
               'ue_head': ue_head, 'ue_tail': ue_tail, 'df_btc_search': df_btc_search, 'btc_search_min': btc_search_min,
               'btc_search_head': btc_search_head, 'btc_search_tail': btc_search_tail, 'btc_search_max': btc_search_max,
               'df_btc_price': df_btc_price, 'btc_price_description': btc_price_description,
               'btc_price_head': btc_price_head, 'btc_price_tail': btc_price_tail,
               'tesla_missing': tesla_missing, 'tesla_duplicate': tesla_duplicate, 'ue_missing': ue_missing,
               'ue_duplicate': ue_duplicate, 'btc_search_missing': btc_search_missing,
               'btc_search_duplicate': btc_search_duplicate, 'btc_price_missing': btc_price_missing,
               'btc_price_duplicate': btc_price_duplicate, 'btc_price_missing_count': btc_price_missing_count,
               'btc_missing_row': btc_missing_row, 'tesla_dtypes': tesla_dtypes, 'ue_dtypes': ue_dtypes,
               'btc_search_dtypes': btc_search_dtypes, 'btc_price_dtypes': btc_price_dtypes}
    return context
