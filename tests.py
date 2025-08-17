import pytest

class TestBooksCollector:
    def test_add_new_book(self, collector):
        collector.add_new_book('Убить пересмешника')
        assert 'Убить пересмешника' in collector.books_genre
        assert collector.books_genre['Убить пересмешника'] == ''

    def test_set_book_genre(self, collector):
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        assert collector.books_genre['1984'] == 'Фантастика'

    def test_set_genre_for_nonexistent_book(self, collector):
        collector.set_book_genre('Звездные войны', 'Фантастика')
        assert 'Звездные войны' not in collector.books_genre

    def test_get_book_genre(self, collector):
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Преступление и наказание', 'Драма')
        genre = collector.get_book_genre('Преступление и наказание')
        assert genre == 'Драма'
        genre_none = collector.get_book_genre('Звездная война')
        assert genre_none is None

    def test_get_books_genre(self, collector):
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Роман')

        collector.add_new_book('Отцы и дети')
        collector.set_book_genre('Отцы и дети', 'Роман')

        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита', 'Фантастика')

        books_in_romance = collector.get_books_genre('Роман')

        assert 'Война и мир' in books_in_romance
        assert 'Отцы и дети' in books_in_romance
        assert 'Мастер и Маргарита' not in books_in_romance

        empty_list = collector.get_books_genre('Научная фантастика')
        assert empty_list == []

    def test_get_books_with_specific_genre_found(self, collector):
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')

        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Преступление и наказание', 'Драма')

        result = collector.get_books_with_specific_genre('Фантастика')
        assert '1984' in result
        assert 'Преступление и наказание' not in result

    def test_get_books_with_specific_genre_no_matches(self, collector):
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')

        result = collector.get_books_with_specific_genre('Драма')
        assert result == []

    def test_get_books_for_children_no_books(self, collector):
        result = collector.get_books_for_children()
        assert result == []

    def test_get_books_for_children_with_books(self, collector):
        collector.add_new_book('Мой сосед Тоторо')
        result = collector.get_books_for_children()
        assert 'Мой сосед Тоторо' in result

...     def test_get_books_for_children_excludes_age_rated(self, collector):
...         horror_book = 'Дракула'
...
...         if horror_book not in collector.books_genre:
...             collector.add_new_book(horror_book)
...             collector.set_book_genre(horror_book, 'Ужасы')
...
...         crime_book = 'Преступление и наказание'
...         if crime_book not in collector.books_genre:
...             collector.add_new_book(crime_book)
...             collector.set_book_genre(crime_book, 'Драма')
...
...         books_for_children = [
...            name for name, genre in collector.books_genre.items()
...            if genre not in ['Ужасы', 'Детективы']
...         ]
...         assert horror_book not in books_for_children
...         assert crime_book not in books_for_children
...
...    @pytest.mark.parametrize("book_name", [
...        'Убить пересмешника',
...        'Остров проклятых'
...    ])
...    def test_add_to_favorites(self, collector, book_name):
...
...         collector.add_new_book(book_name)
...         collector.add_book_in_favorites(book_name)
...
...         favorites = collector.get_list_of_favorites_books()
...
...         assert book_name in favorites
...
...    def test_get_list_of_favorites_books_have_books(self, collector):
...         books = ['Мастер и Маргарита', 'Преступление и наказание', 'Убить пересмешника']
...         for book in books:
...             сollector.add_new_book(book)
...             collector.add_book_in_favorites(book)
...         favorites = collector.get_list_of_favorites_books()
...         for book in books:
...             assert book in favorites
...
...
...    @pytest.mark.parametrize("book_name", [
...        'Убить пересмешника',
...        'Остров проклятых'
...    ])
...    def test_delete_from_favorites(self, collector, book_name):
...        collector.add_new_book(book_name)
...        collector.add_book_in_favorites(book_name)
...        collector.delete_book_from_favorites(book_name)
...        favorites = collector.get_list_of_favorites_books()
...        assert book_name not in favorites
...
...    def test_add_duplicate_in_favorites(self, collector):
...        book_name = 'Властелин колец'
...        collector.add_new_book(book_name)
...        collector.add_book_in_favorites(book_name)
...        collector.add_book_in_favorites(book_name)
...        favorites = collector.get_list_of_favorites_books()
