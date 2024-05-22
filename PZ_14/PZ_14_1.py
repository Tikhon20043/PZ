#В исходном текстовом файле(radio_stations.txt) найти все домены из URL-адресов
#(например, в URL-адресе http://stream.hoster.by:8081/pilotfm/audio/icecast.audio
#домен выделен полужирным).

import re
def extract_domains(file_path):
    domains = set()  # Создаем множество для хранения уникальных доменных имен
    with open(file_path, 'r', encoding='utf-8') as file:  # Открываем файл для чтения в кодировке UTF-8
        for line in file:  # Читаем файл построчно
            urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
            # Используем регулярное выражение для извлечения URL-адресов из строки
            for url in urls:  # Для каждого извлеченного URL-адреса
                domain = re.search(r'://([^/]+)', url)
                # Используем регулярное выражение для извлечения доменного имени из URL-адреса
                if domain:  # Если доменное имя найдено
                    domains.add(domain.group(1))  # Добавляем его во множество уникальных доменных имен
    return domains  # Возвращаем множество уникальных доменных имен

# Пример использования
file_path = 'radio_stations.txt'  # Путь к файлу с URL-адресами радиостанций
extracted_domains = extract_domains(file_path)  # Вызываем функцию для извлечения доменных имен

for domain in extracted_domains:  # Для каждого уникального доменного имени
    print(domain)  # Выводим его на экран