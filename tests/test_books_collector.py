import pytest

from main import BooksCollector
from data import COLLECTOR_LIST
from data import COLLECTOR_ADULT_LIST


class TestBooksCollector:

    def test_add_new_book_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': ''}

    def test_add_new_book_len_name_more_40_book_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Длинное название книги про пушистых кошек')
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_name_in_books_genre_and_genre_in_genre_book_added(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Комедии')
        assert collector.get_books_genre() == {name: 'Комедии'}

    @pytest.mark.parametrize('name, genre', COLLECTOR_LIST)
    def test_get_book_genre_name_in_books_genre_book_returned(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize('name, genre', COLLECTOR_LIST)
    def test_get_books_with_specific_genre_books_genre_in_genre_books_with_specific_genre_returned(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre)[0] == name

    @pytest.mark.parametrize('name, genre',
                             [
                                 ('Звёздные войны', 'Фантастика'),
                                 ('Тупой и ещё тупее', 'Комедии')
                             ])
    def test_get_books_for_children_books_not_in_genre_age_rating_books_returned(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_for_children()[0] == name

    @pytest.mark.parametrize('name, genre', COLLECTOR_ADULT_LIST)
    def test_get_books_for_children_books_in_genre_age_rating_books_not_returned(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert len(collector.get_books_for_children()) == 0

    def test_add_book_in_favorites_name_in_books_genre_book_added(self):
        collector = BooksCollector()
        name = 'Преступление и наказание'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books()[0] == name

    def test_delete_book_from_favorites_name_in_favorites_book_deleted(self):
        collector = BooksCollector()
        name = 'Преступление и наказание'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_add_book_book_returned(self):
        collector = BooksCollector()
        name = 'Преступление и наказание'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() == [name]
        