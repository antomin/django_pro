from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Book, Review


class BookTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(username='reviewuser', email='reviewuser@mail.com',
                                                         password='reviewuserpass123')
        self.book = Book.objects.create(title='Harry Potter', author='JK Rowling', price='25.00')
        self.review = Review.objects.create(book=self.book, author=self.user, review='Oh!!! Greate!')

    def test_book_listing(self):
        self.assertEqual(self.book.title, 'Harry Potter')
        self.assertEqual(self.book.author, 'JK Rowling')
        self.assertEqual(self.book.price, '25.00')

    def test_book_list(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/12345')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Harry Potter')
        self.assertContains(response, 'Oh!!! Greate!')
        self.assertTemplateUsed(response, 'books/book_detail.html')
