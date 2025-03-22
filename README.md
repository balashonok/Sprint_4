Класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector.

Тест test_add_new_book_book_added 
добавляет книгу и проверяет что книга добавлена в словарь и для неё задан пустой жанр.

Тест test_add_new_book_len_name_more_40_book_not_added
добавляет книгу с длиной имени более 40 символов и проверяет что книга не добавлена

Тест test_set_book_genre_name_in_books_genre_and_genre_in_genre_book_added
добавляет книги жанр, проверяет что жанр добавлен.

Тест test_get_book_genre_name_in_books_genre_book_returned
проверяет получение жанра книги по её имени.

Тест test_get_books_with_specific_genre_books_genre_in_genre_books_with_specific_genre_returned
проверяет получение имени книги по жанру.

Тест test_get_books_for_children_books_not_in_genre_age_rating_books_returned
проверяет получение книги подходящей для детей.

Тест test_get_books_for_children_books_in_genre_age_rating_books_not_returned
проверяет, что книга с жанром, входящим в возрастной рейтинг, не добавлена в список книг подходящих детям.

Тест test_add_book_in_favorites_name_in_books_genre_book_added
проверяет добавление книги в Избранное.

Тест test_delete_book_from_favorites_name_in_favorites_book_deleted
проверяет удаление книги из Избранного.
