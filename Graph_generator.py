import matplotlib.pyplot as plt
import pandas as pd

####################### DATASETS ###############################
# Load csv files
wine = pd.read_csv('Datasets/white-wine-quality.csv')
fps = pd.read_csv('Datasets/fps-in-video-games.csv')
# fps_small = pd.read_csv('Datasets/fps-in-video-games_small.csv')

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

# for white wine:
acidity = wine[['V1', 'V2', 'V3']]
sulfur = wine[['V7', 'V6']]
sugar = wine['V4']
result = wine['Class']
split1 = wine[['V11', 'V1', 'V9']]
split2 = wine[['V2', 'V3', 'V5', 'V8', 'V10']]
total_split1 = wine[['V7', 'V6', 'V4']]
total_split2 = wine[['V11', 'V1', 'V9']]
total_split3 = wine[['V2', 'V3', 'V5', 'V8', 'V10']]

# for FPS
fps_values = fps['FPS']
cpu_frequency = fps['CpuFrequency']
game_name = fps["GameName"].tolist()

# ------------------------------------------------
gpu_memory_size = fps['GpuMemorySize'].tolist()

# set missing values to 0
for i in range(0, len(gpu_memory_size)):
    if gpu_memory_size[i] == "?":
        gpu_memory_size[i] = 0

gpu_memory_size = list(map(int, gpu_memory_size))


# -------------------------------------------------


# #################### METHODS ########################################


def plot_table_wine(table, plot_name, file_name):
    for n in table:
        plt.hist(table[n], 100, histtype='step', label=labels[n])

    plt.title(plot_name)
    plt.legend()
    plt.savefig(file_name)
    # plt.show()
    plt.close()


def plot_column_wine(column, plot_name, file_name):
    plt.hist(column, 100, label=labels[column.name])

    plt.title(plot_name)
    plt.legend()
    plt.savefig(file_name)
    # plt.show()
    plt.close()


def plot_column_fps(column, bins, plot_name, file_name):
    plt.hist(column, bins)
    plt.title(plot_name)
    plt.xticks(rotation=30)
    # plt.legend()
    plt.savefig(file_name)
    # plt.show()
    plt.close()


def plot_column_fps_nominal(column, plot_name, file_name):
    plt.figure(figsize=(20, 5), constrained_layout=True)
    plt.hist(column, 30)
    plt.title(plot_name)
    plt.xticks(rotation=60)
    plt.savefig(file_name)
    # plt.show()
    plt.close()


############## HISTOGRAMS ############################################

# -------------- WHITE WINE QUALITY ----------------------------------
# plot_table_wine(wine, 'White Wine', 'Graphs/WineTotal.png')
# plot_table_wine(sulfur, 'White Wine Sulfur', 'Graphs/Sulfur.png')
# plot_column_wine(result, 'Quality', 'Graphs/Quality.png')
# plot_column_wine(sugar, 'Sugar', 'Graphs/sugar.png')
# plot_table_wine(split1, 'Split1', 'Graphs/split1.png')
# plot_table_wine(split2, 'Split2', 'Graphs/split2.png')
# plot_table_wine(total_split1, '', 'Graphs/total_split1.png')
# plot_table_wine(total_split2, '', 'Graphs/total_split2.png')
# plot_table_wine(total_split3, '', 'Graphs/total_split3.png')


# ------------- PC GAME FPS --------------------------------------
# plot_column_fps(fps_values, 50, "FPS", "Graphs/fps.png")
# plot_column_fps(cpu_frequency, 30, "CPU frequency", "Graphs/cpu")
# plot_column_fps(gpu_memory_size, 20, "GPU memory size", "Graphs/gpu.png")
# plot_column_fps_nominal(game_name, "Game Name", "Graphs/games.png")
