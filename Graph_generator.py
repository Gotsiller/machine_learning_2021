
import matplotlib.pyplot as plt
import pandas as pd

####################### DATASETS ###############################


def load_white_wine() -> tuple[pd.DataFrame, dict]:
    wine = pd.read_csv('data/white_wine.csv')
    labels = {'V1': 'fixed acidity',
              'V2': 'volatile acidity',
              'V3': 'citric acid',
              'V4': 'residual sugar',
              'V5': 'chlorides',
              'V6': 'free sulfur dioxide',
              'V7': 'total sulfur dioxide',
              'V8': 'density',
              'V9': 'pH',
              'V10': 'sulphates',
              'V11': 'alcohol',
              'Class': 'quality'}
    return wine, labels

def load_internet_usage() -> pd.DataFrame:
    netuse = pd.read_csv('data/internet_usage.csv')

    # exchange columns of "Actual Time" and "who"
    netuse = netuse.rename(columns = {'Actual Time': 'who', 'who': 'Actual Time'})
    return netuse


def remove_missing_values(column: pd.Series, symbol: str) -> pd.Series:
    return column.drop(column.index[column == symbol])


def prepare_income_data(income_raw: pd.Series) -> tuple[list, list]:
    conversion = {'Under_$10': 0,
                  '$10-19': 1,
                  '$20-29': 2,
                  '$30-39': 3,
                  '$40-49': 4,
                  '$50-74': 5,
                  '$75-99': 6,
                  'Over_$100': 7}

    income = []
    for value in income_raw:
        income.append(conversion[value])

    return income, ['Under_$10', '$10-19', '$20-29', '$30-39', '$40-49', '$50-74', '$75-99', 'Over_$100']


def plot_table_wine(table, labels, plot_name, file_name):
    for n in table:
        plt.hist(table[n], 100, histtype='step', label=labels[n])

    plt.title(plot_name)
    plt.legend()
    plt.savefig(file_name)
    plt.close()


def plot_column_wine(column, labels, plot_name, file_name):
    plt.hist(column, 100, label=labels[column.name])

    plt.title(plot_name)
    plt.legend()
    plt.savefig(file_name)
    # plt.show()
    plt.close()


def plot_column_netuse(column, bins, plot_name, file_name):
    plt.hist(column, bins)
    plt.title(plot_name)
    plt.xticks(rotation=30)
    # plt.legend()
    plt.savefig(file_name)
    # plt.show()
    plt.close()



def plot_column_netuse_nominal(column, labels: list, plot_name, file_name):
    # plt.figure(figsize=(10, 5), constrained_layout=True)
    plt.hist(column, len(labels))
    plt.title(plot_name)
    plt.xticks(rotation=20, ticks=[x for x in range(0, 8)], labels=labels)
    plt.savefig(file_name)
    # plt.show()
    plt.close()


if __name__ == '__main__':
    # -------------- WHITE WINE QUALITY ----------------------------------
    # wine, labels = load_white_wine()
    # plot_table_wine(wine, labels, 'White Wine', 'Graphs/WineTotal.png')
    # plot_column_wine(wine['Class'], labels, 'Quality', 'Graphs/Quality.png')
    # plot_table_wine(wine[['V7', 'V6', 'V4']], labels, '', 'Graphs/total_split1.png')
    # plot_table_wine(wine[['V11', 'V1', 'V9']], labels, '', 'Graphs/total_split2.png')
    # plot_table_wine(wine[['V2', 'V3', 'V5', 'V8', 'V10']], labels, '', 'Graphs/total_split3.png')

    # ---------------- INTERNET USAGE -----------------------------------
    netuse = load_internet_usage()
    plot_column_netuse(netuse['Actual Time'], 100, 'Internet Usage Time', 'Graphs/ActualTime.png')

    age_column = remove_missing_values(netuse['Age'], 'Not_Say').astype(int)
    plot_column_netuse(age_column, 50, 'Age of Users', 'Graphs/Age.png')

    income_column, income_labels = prepare_income_data(remove_missing_values(netuse['Household_Income'], 'Not_Say'))
    plot_column_netuse_nominal(income_column, income_labels, 'Household Income', 'Graphs/income.png')
