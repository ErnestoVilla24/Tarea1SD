def save_metrics(cache_type, policy, hits, misses):
    filename = f"{cache_type}_{policy}_metrics.txt"
    with open(filename, "w") as file:
        file.write(f"Tipo de caché: {cache_type}\n")
        file.write(f"Política de reemplazo: {policy}\n")
        file.write(f"Número de aciertos: {hits}\n")
        file.write(f"Número de fallos: {misses}\n")
        file.write("\n")
