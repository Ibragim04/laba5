import pickle

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

def count_word_occurrences(file_name, word):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()
            occurrences = text.lower().count(word.lower())
            return occurrences
    except FileNotFoundError:
        print("Файл не найден.")
        return -1

def write_to_text_file(matrix_objects, file_name):
    try:
        with open(file_name + ".txt", 'w') as file:
            for matrix in matrix_objects:
                file.write(f"{matrix.rows} {matrix.columns}\n")
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")

def read_from_text_file(file_name):
    matrices = []
    try:
        with open(file_name + ".txt", 'r') as file:
            for line in file:
                rows, columns = map(int, line.split())
                matrices.append(Matrix(rows, columns))
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
    return matrices

def write_to_binary_file(matrix_objects, file_name):
    try:
        with open(file_name + ".bin", 'wb') as file:
            pickle.dump(matrix_objects, file)
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")

def read_from_binary_file(file_name):
    matrices = []
    try:
        with open(file_name + ".bin", 'rb') as file:
            matrices = pickle.load(file)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
    return matrices

class BookCatalog:
    def __init__(self, file_name):
        self.file_name = file_name
        self.catalog = []

    def load_catalog(self):
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    if line.strip():
                        book_info = line.strip().split()
                        self.catalog.append({'ID': book_info[0], 'Author': book_info[1], 'Title': book_info[2], 'Pages': int(book_info[3])})
        except FileNotFoundError:
            print("Файл с каталогом не найден.")

    def save_catalog(self):
        try:
            with open(self.file_name, 'w') as file:
                for book in self.catalog:
                    file.write(f"{book['ID']} {book['Author']} {book['Title']} {book['Pages']}\n")
        except Exception as e:
            print(f"Ошибка при сохранении каталога: {e}")

    def add_book(self, book_id, author, title, pages):
        self.catalog.append({'ID': book_id, 'Author': author, 'Title': title, 'Pages': pages})

    def view_catalog(self):
        for book in self.catalog:
            print(book)

    def delete_book(self, book_id):
        self.catalog = [book for book in self.catalog if book['ID'] != book_id]

    def search_book(self, keyword):
        results = [book for book in self.catalog if keyword.lower() in book['Title'].lower()]
        return results

    def edit_book(self, book_id, new_author=None, new_title=None, new_pages=None):
        for book in self.catalog:
            if book['ID'] == book_id:
                if new_author:
                    book['Author'] = new_author
                if new_title:
                    book['Title'] = new_title
                if new_pages:
                    book['Pages'] = new_pages

    def add_record(self, book_id, author, title, pages):
        self.add_book(book_id, author, title, pages)
        self.save_catalog()

    def delete_record(self, book_id):
        self.delete_book(book_id)
        self.save_catalog()

    def edit_record(self, book_id, new_author=None, new_title=None, new_pages=None):
        self.edit_book(book_id, new_author, new_title, new_pages)
        self.save_catalog()

# Пример использования:

# Подсчёт количества вхождений слова в текстовом файле
file_name = "example.txt"
word = "example"
print(f"Количество вхождений слова '{word}' в файле: {count_word_occurrences(file_name, word)}")

# Работа с объектами Matrix
matrices = [Matrix(2, 2), Matrix(3, 3), Matrix(4, 4)]

write_to_text_file(matrices, "matrices_text")
matrices_from_text = read_from_text_file("matrices_text")

write_to_binary_file(matrices, "matrices_binary")
matrices_from_binary = read_from_binary_file("matrices_binary")

# Манипуляции с каталогом книг
catalog = BookCatalog("book_catalog.txt")
catalog.load_catalog()
catalog.view_catalog()

# Добавление новой записи
catalog.add_record("0003", "J.K. Rowling", "Harry Potter", 400)
catalog.view_catalog()

# Удаление записи
catalog.delete_record("0002")
catalog.view_catalog()

# Поиск записи
results = catalog.search_book("dubrovsky")
print("Результаты поиска:")
for book in results:
    print(book)

# Редактирование записи
catalog.edit_record("0001", new_author="Alexander Pushkin")
catalog.view_catalog()
