import pytest


class TestBooksCollector:
    def test_add_new_book(self, collector):
        collector.add_new_book('Убить пересмешника')
        assert 'Убить пересмешника' in collector.books_genre

    def test_set_book_genre(self, collector):
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        assert collector.books_genre['1984'] == 'Фантастика'

    def test_set_genre_for_nonexistent_book(self, collector):
        collector.set_book_genre('Звездные войны', 'Фантастика')
        assert 'Звездные войны' not in collector.books_genre

    def test_get_book_genre(self, collector):
        collector.add_new_book('Вишнёвый сад')
        collector.set_book_genre('Вишнёвый сад', 'Комедии')
        genre = collector.get_book_genre('Вишнёвый сад')
        assert genre == 'Комедии'

    def test_get_books_genre(self, collector):
        collector.add_new_book('Долгая прогулка')
        collector.set_book_genre('Долгая прогулка', 'Фантастика')
        result = collector.get_books_genre()
        assert result is collector.books_genre

    def test_get_books_with_specific_genre_found(self, collector):
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        result = collector.get_books_with_specific_genre('Фантастика')
        assert '1984' in result

    def test_get_books_with_specific_genre_no_matches(self, collector):
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        result = collector.get_books_with_specific_genre('Детективы')
        assert result == []

    def test_get_books_for_children_no_books(self, collector):
        result = collector.get_books_for_children()
        assert result == []

    def test_get_books_for_children_with_books(self, collector):
        collector.add_new_book('Мой сосед Тоторо')
        collector.set_book_genre('Мой сосед Тоторо', 'Мультфильмы')
        result = collector.get_books_for_children()
        assert 'Мой сосед Тоторо' in result

    def test_get_books_for_children_excludes_age_rated(self, collector):
        horror_book = 'Дракула'
        collector.add_new_book(horror_book)
        collector.set_book_genre(horror_book, 'Ужасы')
        books_for_children = collector.get_books_for_children()
        assert horror_book not in books_for_children

    @pytest.mark.parametrize("book_name", [
        'Убить пересмешника',
        'Остров проклятых'
    ])
    def test_add_to_favorites(self, collector, book_name):
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)

        assert book_name in collector.favorites

    def test_get_list_of_favorites_books_have_books(self, collector):
        books = ['Мастер и Маргарита', 'Преступление и наказание', 'Убить пересмешника']
        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)
        favorites = collector.get_list_of_favorites_books()
        assert favorites == books

    @pytest.mark.parametrize("book_name", [
        'Убить пересмешника',
        'Остров проклятых'
    ])
    def test_delete_from_favorites(self, collector, book_name):
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        favorites = collector.get_list_of_favorites_books()
        assert book_name not in favorites

    def test_add_duplicate_in_favorites(self, collector):
        book_name = 'Властелин колец'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.add_book_in_favorites(book_name)
        favorites = collector.get_list_of_favorites_books()
        assert favorites.count(book_name) == 1
