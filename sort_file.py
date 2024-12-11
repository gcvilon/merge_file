def merge_files(file_list, output_file):
    files_info = []

    for filepath in file_list:  # Используем заданный список файлов
        try:
            with open(filepath, 'r', encoding='UTF-8') as file:
                lines = file.read().splitlines()  # Считываем строки без '\n'
                files_info.append({
                    'filename': filepath,  # Имя файла
                    'lines': lines,        # Содержимое строк
                    'line_count': len(lines)  # Количество строк
                })
        except FileNotFoundError:
            print(f"Файл {filepath} не найден.")
        except Exception as e:
            print(f"Ошибка при обработке файла {filepath}: {e}")

    files_info.sort(key=lambda x: x['line_count'])

    try:
        with open(output_file, 'w', encoding='UTF-8') as outfile:
            for file_info in files_info:
                outfile.write(file_info['filename'] + '\n')  # Имя файла
                outfile.write(str(file_info['line_count']) + '\n')  # Количество строк
                outfile.write('\n'.join(file_info['lines']) + '\n')  # Содержимое файла
    except Exception as e:
        print(f"Ошибка при записи в файл {output_file}: {e}")

file_list = ['1.txt', '2.txt', '3.txt']  # Укажите список файлов в папке
merge_files(file_list, 'result.txt')
