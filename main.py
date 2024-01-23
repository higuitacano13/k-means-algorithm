import utils
import pandas as pd

def select_file():
    try:

        print('Selecciona el archivo CSV con el que desea realizar la operación:\n1- Coordenadas de Espacio Bidimensional. \n2- Clasificación Genética \n3- Segmentación Clientes \n4- Vendedores')
        option_selected = int(input('Selección -> '))
        csv_path = ''

        if option_selected == 1:
            csv_path = './csv_files/coordenadas_espacio_bidimensional.csv'
            return csv_path, option_selected
        elif option_selected == 2:
            csv_path = './csv_files/csv_genes.csv'
            return csv_path, option_selected
        elif option_selected == 3:
            csv_path = './csv_files/segmentacion_clientes.csv'
            return csv_path, option_selected
        elif option_selected == 4:
            csv_path = './csv_files/ventas.csv'
            return csv_path, option_selected
        else:
            raise Exception('La opción seleccionada no es válida, por favor intente de nuevo!')
        
    except Exception as error:
        print(f'Se ha generado un error en el método select_file -> {error}')
    
def action_result(option_selected):
    try:

        if option_selected == 1:
            chart_selection = input('\nEl contenido del archivo es posible graficarlo, ¿Desea ver gráficarlo? \nY/N: ')
            if chart_selection.upper() == 'Y':
                print('Seleccione el tipo de gráfica: \n1- Gráfica Matplotlib \n2- Gráfica Web')
                type_chart = int(input('Selección -> '))
                if type_chart == 1:
                    utils.create_chart(data, kmeans, labels)
                elif type_chart == 2:
                    utils.create_interactive_chart(data, kmeans, labels)
                else:
                    raise Exception('La opción seleccionada no es válida, por favor intente de nuevo!')
            else:
                resultadoJson = utils.convert_json(kmeans, data)
                print(f'\nResultado Json: \n {resultadoJson}')
        else:
            resultadoJson = utils.convert_json(kmeans, data)
            print(f'\nResultado Json: \n {resultadoJson}')

    except Exception as error:
        print(f'Se ha generado un error en el método action_result -> {error}')

if __name__ == '__main__':
    try:
        print('*****' * 20)
        print('Bienvenido al ejercicio de agrupamiento utilizando el algoritmo K-Means')
        path, option_selected = select_file()  
        if path and option_selected is not None:
            data = pd.read_csv(path)
            data, kmeans, labels = utils.k_means_algorithm(data)
            action_result(option_selected)

    except Exception as error:
        print(f'Se ha generado un error en el método main -> {error}')

