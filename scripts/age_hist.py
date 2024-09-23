from utils import load_data, plot_histogram

def main():
    # load data
    df = load_data('data/social-media.csv')

    # Plot the histogram of ages
    plot_histogram(df, 'Age', bins=10, xlabel='Edad', ylabel='Frecuencia', title='Distribución de Edades de los Usuarios', figure_num=4)
