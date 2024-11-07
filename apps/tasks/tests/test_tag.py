from django.test import TestCase
from rest_framework.response import Response
from rest_framework.utils import json

from apps.tasks.models.tag import Tag


class TagsListTestCase(TestCase):
    def test_get_empty_list_of_tags(self):
        response = self.client.get('/api/tags/')

        self.assertEqual(response.status_code, 204)
        self.assertIsInstance(response.data, list)
        self.assertEqual(Tag.objects.count(), 0)

    def test_get_tags(self):
        tags = [
            Tag(name='Backend'),
            Tag(name='Frontend'),
            Tag(name='DevOPS'),
            Tag(name='Design'),
            Tag(name='Testing'),
            Tag(name='Data Science'),
            Tag(name='Data Analytics'),
            Tag(name='machine Learning'),
        ]
        Tag.objects.bulk_create(tags)

        response = self.client.get('/api/tags/')

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, Response)

        self.assertIsInstance(response.data, list)
        for tag in response.data:
            self.assertIsInstance(tag, dict)
            self.assertIn('name', tag)
            self.assertIsInstance(tag['name'], str)
            self.assertRegex(tag['name'], r'^[a-zA-Z ]{4,20}$')


class CreateTagTestCase(TestCase):
    def test_create_valid_tag(self):
        data = {"name": "Test Tag"}

        response = self.client.post('/api/tags/', data)

        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(Tag.objects.count(), 1)
        self.assertEqual(Tag.objects.get(name='Test Tag').name, 'Test Tag')

    def test_create_invalid_tag(self):
        data = {"name": "QA"}

        response = self.client.post('/api/tags/', data)

        self.assertEqual(response.status_code, 400)

    def test_create_tag_without_data(self):
        data = {}
        response = self.client.post('/api/tags/', data)

        self.assertEqual(response.status_code, 400)


class GetTagObjectTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(id=1, name='Test Tag')

    def test_get_tag_by_id(self):
        response = self.client.get('/api/tags/1/')

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, dict)
        self.assertIn('name', response.data)
        self.assertEqual(response.data['name'], 'Test Tag')

    def test_get_tag_by_undefined_id(self):
        response = self.client.get('/api/tags/99/')

        self.assertEqual(response.status_code, 404)

    def test_get_tag_by_invalid_url_param(self):
        response = self.client.get('/api/tags/Test_Tag/')

        self.assertEqual(response.status_code, 404)


class UpdateTagTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(id=1, name='Test Tag')

    def test_update_tag_with_valid_name(self):
        new_tag_name = {"name": "TEST TAG"}
        response = self.client.put(
            '/api/tags/1/',
            data=json.dumps(new_tag_name),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(response.data['name'], new_tag_name['name'])

    def test_update_tag_with_invalid_name(self):
        bad_tag_name = {"name": "SUPER LONG TEST TAG NAME"}
        response = self.client.put(
            '/api/tags/1/',
            data=json.dumps(bad_tag_name),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 400)

    def test_update_tag_without_data(self):
        response = self.client.put(
            '/api/tags/1/',
            data=json.dumps({}),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 400)


class DeleteTagTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(id=1, name='Test Tag')

    def test_delete_tag(self):
        response = self.client.delete('/api/tags/1/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Tag.objects.count(), 0)
        self.assertEqual(response.data, {
            "message": "Tag 1 deleted."
        })


class TagsTestCase(TestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertContains(response, "Welcome")
