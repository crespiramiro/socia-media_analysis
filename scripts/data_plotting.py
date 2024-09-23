from utils import load_data, plot_scatter

def main():
    # Cargar los datos
    df = load_data('data/social-media.csv')

    # Graficar la relación entre Edad y Duración de Uso
    plot_scatter(df['Age'], df['UsageDuration'], xlabel='Edad', ylabel='Duración de Uso', title='Relación entre Edad y Uso de Redes Sociales', figure_num=1)
