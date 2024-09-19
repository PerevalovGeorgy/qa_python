# qa_python
1. тест test_add_new_book_add_two_books - написан для примера, проверяет работу функции add_new_book
2. тест test_set_book_genre_add_genre - проверяет работу функции set_book_genre, устанавливает и проверяет жанр
3. тест test_get_book_genre_get_genre - проверяет работу функции get_book_genre, проверяет жанр
4. тест test_get_books_with_specific_genre_get_amount_books_with_specific_genre - проверяет работу функции get_books_with_specific_genre, проверяет что в коллекции книг есть нужное количество книг определенного жанра
5. тест test_get_books_genre_get_dictionary_of_books - проверяет работу функуии get_books_genre, сверяет созданную коллекцию с эталоной коллекцией
6. тест test_get_books_for_children_add_one_book_for_children - проверяет работу функции get_books_for_children, проверяет наличие одной книги доступного жанра
7. тест test_get_books_for_children_add_unresolved_book_for_children - проверяет работу функции get_books_for_children, проверяет наличие  книги запрещенного жанра
8. тест test_add_book_in_favorites_add_one_book_in_favorites - проверяет работу функции add_book_in_favorites, проверяет наличие книги в списке любимых
9. тест test_delete_book_from_favorites_delete_one_book_from_favorites - проверяет работу функции delete_book_from_favorites, проверяет наличие книги в списке любимых после удаления
10. тест test_get_list_of_favorites_books_get_amount_of_favorites_books - проверяет работу функции get_list_of_favorites_books, сверяет количество любимых книг
11. отрицательный тест test_add_book_in_favorites_add_same_book_in_favorites -  проверяет работу функции add_book_in_favorites, проверяет возможность повторного добавления книги в список любимых
12. тест test_genre_presence_in_list_genre - проверяет список имеющихся жанров