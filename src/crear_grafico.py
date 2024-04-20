import matplotlib.pyplot as plt

def plot_metrics(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        cache_type = lines[0].split(":")[1].strip()
        policy = lines[1].split(":")[1].strip()
        hits = int(lines[2].split(":")[1])
        misses = int(lines[3].split(":")[1])

        # Crear el gráfico de barras
        plt.figure(figsize=(8, 6))
        categories = ['Hits', 'Misses']
        values = [hits, misses]
        plt.bar(categories, values, color=['green', 'red'])
        plt.title(f"Métricas para {cache_type} con política {policy}")
        plt.xlabel('Tipo de Métrica')
        plt.ylabel('Cantidad')
        plt.savefig(f"{filename.split('.')[0]}.png")  # Guardar el gráfico como imagen
        plt.show()

if __name__ == "__main__":
    plot_metrics("classic_LRU_metrics.txt")
    plot_metrics("classic_MRU_metrics.txt")
    plot_metrics("replicated_LRU_metrics.txt")
    plot_metrics("replicated_MRU_metrics.txt")
    plot_metrics("partitioned_LRU_metrics.txt")
    plot_metrics("partitioned_MRU_metrics.txt")
