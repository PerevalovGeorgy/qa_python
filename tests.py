from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        #исправлен вызов метода с get_books_rating на get_books_genre = проверен метод add_new_book
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_genre_add_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', 'Детективы')

        assert collector.get_book_genre('Книга 1') == 'Детективы'

    def test_get_book_genre_get_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', 'Детективы')

        assert collector.get_book_genre('Книга 1') == 'Детективы'

    def test_get_books_with_specific_genre_get_amount_books_with_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', 'Детективы')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 2', 'Детективы')
        collector.add_new_book('Книга 3')
        collector.set_book_genre('Книга 3', 'Фантастика')

        assert len(collector.get_books_with_specific_genre('Детективы')) == 2

    def test_get_books_genre_get_dictionary_of_books(self):
        collector = BooksCollector()

        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', 'Детективы')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 2', 'Детективы')
        collector.add_new_book('Книга 3')
        collector.set_book_genre('Книга 3', 'Фантастика')

        etalon = {'Книга 1': 'Детективы',
                  'Книга 2': 'Детективы',
                  'Книга 3': 'Фантастика'}

        assert collector.get_books_genre() == etalon

    def test_get_books_for_children_add_one_book_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('Книга 3')
        collector.set_book_genre('Книга 3', 'Фантастика')

        assert len(collector.get_books_for_children()) == 1

    def test_get_books_for_children_add_unresolved_book_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', 'Детективы')

        assert len(collector.get_books_for_children()) == 0

    def test_add_book_in_favorites_add_one_book_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Книга 1')
        # убрал строку с добавлением жанра, действительно можно и без нее

        collector.add_book_in_favorites('Книга 1')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_delete_one_book_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', 'Детективы')

        collector.add_book_in_favorites('Книга 1')
        collector.delete_book_from_favorites('Книга 1')

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_get_amount_of_favorites_books(self):
        collector = BooksCollector()

        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', 'Детективы')

        collector.add_book_in_favorites('Книга 1')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_add_same_book_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', 'Детективы')

        collector.add_book_in_favorites('Книга 1')
        collector.add_book_in_favorites('Книга 1')

        assert len(collector.get_list_of_favorites_books()) == 1

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_genre_presence_in_list_genre(self, genre):
        collector = BooksCollector()
        assert genre in collector.genre

