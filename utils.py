from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import json

def k_means_algorithm(data):
    try:
        # ---- Ajustar el módelo de datos y asignar las etiquetas ---- #
        k = 3
        kmeans = KMeans(n_clusters=k, n_init=10)
        kmeans.fit(data)
        labels = kmeans.labels_
        data['Cluster'] = labels
        centroids = kmeans.cluster_centers_

        # ---- Obtener los centroides y asignar nombres a las columnas (CONCEPTUAL) ---- #
        decimales = 0
        centroids_df = pd.DataFrame(centroids, columns = data.columns[:-1])
        centroids_df['Cluster'] = range(k)
        centroids_df = centroids_df.round(decimales)

        data_sorted = data.sort_values(by = "Cluster")

        print(f"\nCentroides (Tipo de dato => {type(centroids_df)})")
        print(centroids_df)
        print("\nDatos con etiquetas de cluster:")
        print(data_sorted)
        
        return data, kmeans, labels
    except Exception as error:
        print(f'Se ha generado un error realizando el algoritmo k-meant -> {error}')

def create_chart(data, kmeans, labels):
    try:
        # ---- Graficar los puntos en el conjunto de datos ---- #
        plt.scatter(data['X'], data['Y'], c=labels, cmap='viridis', edgecolors='k')

        # ---- Graficar los centroides con una 'x' en rojo ---- #
        plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='x', s=200, linewidths=3, color='r')

        # ---- Configurar el título y etiquetas de los ejes ---- #
        plt.title('K-Means Clustering')
        plt.xlabel('X1')
        plt.ylabel('X2')

        # ---- Mostrar los gráficos ---- #
        plt.show()
    except Exception as error:
        print(f'Se ha generado un error creando la gráfica con Matplotlib -> {error}')

def create_interactive_chart(data, kmeans, labels):
    try:
        # Agregar las etiquetas de cluster al DataFrame original
        data['Cluster'] = labels

        # Crear el gráfico interactivo con plotly express
        fig = px.scatter(data, x='X', y='Y', color='Cluster', hover_data=['X', 'Y'], title='K-Means Clustering')

        # Agregar los centroides al gráfico
        fig.add_scatter(x=kmeans.cluster_centers_[:, 0], y=kmeans.cluster_centers_[:, 1],
                        mode='markers', marker=dict(color='red', symbol='x', size=12))

        # Mostrar el gráfico
        fig.show()
    except Exception as error:
        print(f'Error creando el gráfico interactivo -> {error}')

def convert_json(kmeans, data):
    # Crear un diccionario con la información
    resultado_dict = {
        'centroides': kmeans.cluster_centers_.tolist(),
        'datos_con_clusters': data.to_dict(orient='records')
    }

    # Convertir el diccionario a formato JSON
    resultado_json = json.dumps(resultado_dict, indent=2)
    return resultado_json