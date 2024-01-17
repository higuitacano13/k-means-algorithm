import utils
import pandas as pd

if __name__ == '__main__':
    try:
        csv_path = './csv_files/coordenadas_espacio_bidimensional.csv'
        data = pd.read_csv(csv_path)
        data, kmeans, labels = utils.k_means_algorithm(data)
        utils.convert_json(kmeans, data)
        # utils.create_interactive_chart(data, kmeans, labels)

    except Exception as error:
        print(f'Se ha generado un error en el método main -> {error}')

