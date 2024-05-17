import numpy as np

def scalar_product(vector1, vector2):
    return np.dot(vector1, vector2)


from concurrent.futures import ThreadPoolExecutor

def cascade_dot_product(vectors):
    # Создаем список для хранения результатов
    results = []
    
    # Используем ThreadPoolExecutor для параллельного выполнения задач
    with ThreadPoolExecutor() as executor:
        # Генерируем пары векторов для скалярного произведения
        pairs = [(vectors[i], vectors[j]) for i in range(len(vectors)) for j in range(i+1, len(vectors))]
        
        # Выполняем скалярное произведение в парах и собираем результаты
        futures = [executor.submit(scalar_product, pair[0], pair[1]) for pair in pairs]
        for future in futures:
            results.append(future.result())
    
    return results

# Пример использования
if __name__ == "__main__":
    vectors = [
        np.array([1, 2, 3]),
        np.array([4, 5, 6]),
        np.array([7, 8, 9])
    ]
    
    products = cascade_dot_product(vectors)
    print("Скалярные произведения:", products)
