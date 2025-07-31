from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_book(self):
        collector = BooksCollector()
        collector.add_new_book('Убить пересмешника')
        assert collector.books_genre['Убить пересмешника'] == ''


    @pytest.mark.parametrize('books, genre', [('Дракула', 'Ужасы'),
                                              ('Двенадцать стульев', 'Комедии')])


    def test_get_list_of_favorites_books_have_books(self, books, genre):
        collector = BooksCollector()
        collector.add_new_book(books)
        collector.set_book_genre(books, genre)
        collector.add_book_in_favorites(books)
        assert books in collector.get_list_of_favorites_books()


    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        assert collector.get_book_genre('1984') == 'Фантастика'


    def test_set_book_genre_invalid(self):
        collector = BooksCollector()
        collector.add_new_book('Двенадцать стульев')
        collector.set_book_genre('Двенадцать стульев', 'Ужасы')
        assert collector.get_book_genre('Двенадцать стульев') == ''


    def test_get_books_for_children_list_is_not_empty(self):
        collector = BooksCollector()
        collector.add_new_book('Мой сосед Тоторо')
        collector.set_book_genre('Мой сосед Тоторо', 'Мультфильмы')
        assert 'Мой сосед Тоторо' in collector.get_books_for_children()

    def test_get_books_for_children_list_is_empty(self):
        collector = BooksCollector()
        collector.add_new_book('Дракула')
        collector.set_book_genre('Дракула', 'Ужасы')
        assert 'Дракула' not in collector.get_books_for_children()

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Убить пересмешника')
        collector.add_book_in_favorites('Убить пересмешника')
        assert 'Убить пересмешника' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Убить пересмешника')
        collector.add_book_in_favorites('Убить пересмешника')
        collector.delete_book_from_favorites('Убить пересмешника')
        assert 'Убить пересмешника' not in collector.get_list_of_favorites_books()


    def test_add_duplicate_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Убить пересмешника', genre='Криминал')
        collector.add_book_in_favorites('Убить пересмешника')
        collector.add_book_in_favorites('Убить пересмешника')
        assert collector.get_list_of_favorites_books().count('Убить пересмешника') == 1


    def test_adding_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Убить пересмешника')
        assert collector.get_book_genre('Убить пересмешника') == ''


    def test_books_with_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Остров проклятых')
        assert collector.get_books_with_specific_genre('') == []


    def test_get_books_for_children_no_books(self):
        collector = BooksCollector()
        assert collector.get_books_for_children() == []