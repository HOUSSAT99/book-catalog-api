from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book_data = {
            "title": "Test Book",
            "author": "Zakaria",
            "isbn": "1234567890123",
            "published_date": "2023-01-01"
        }
        self.book = Book.objects.create(**self.book_data)

    def test_create_book(self):
        response = self.client.post('/api/books/', {
            "title": "New Book",
            "author": "Author Name",
            "isbn": "9999999999999",
            "published_date": "2022-05-05"
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_book(self):
        response = self.client.get(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book_data['title'])

    def test_delete_book(self):
        response = self.client.delete(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

