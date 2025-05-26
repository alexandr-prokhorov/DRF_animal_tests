from rest_framework.test import APITestCase
from rest_framework import status

from sections.models import Section
from sections.tests.utils import get_admin_user, get_member_user


class SectionTestCase(APITestCase):

    def setUp(self):
        self.user = get_admin_user()
        response = self.client.post('/users/token/', {"email": "tester@test1.com", "password": "qwerty"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.test_section = Section.objects.create(
            title="Test Section",
            description="Test Description",
        )

    def test_01_section_create(self):
        data = {
            "title": "Test Section Create",
            "description": "Test Description Create",
        }
        response = self.client.post('/section/create/', data=data)
        print(response.status_code)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get('title'), "Test Section Create")
        self.assertEqual(response.json().get('description'), "Test Description Create")

    def test_02_section_detail(self):
        response = self.client.get('/section/3/', {"email": "tester@test1.com", "password": "qwerty"})
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), "Test Section")
        self.assertEqual(response.json().get('description'), "Test Description")

    def test_03_section_update(self):
        data = {
            "title": "Test Section Update Put",
            "description": "Test Description Update Put",
        }
        response = self.client.put('/section/4/update/', data=data)
        # метод ниже используется для того чтобы не подсчитывать id
        # response = self.client.put(f'/section/{self.test_section.id}/update/', data=data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), "Test Section Update Put")
        self.assertEqual(response.json().get('description'), "Test Description Update Put")

    def test_04_section_delete(self):
        response = self.client.delete('/section/5/delete/')
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_05_section_list(self):
        response = self.client.get('/section/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.json().get('results'),
        #                  [{'id': 6, 'title': 'Test Section', 'section_content_title': []}])
        self.assertEqual(response.json()['results'][0]['title'], "Test Section")
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_06_section_create_forbidden(self):
        self.user = get_member_user()
        response = self.client.post('/users/token/', {"email": self.user.email, "password": "qwerty"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        data = {
            "title": "Test Section Create",
            "description": "Test Description Create",
        }
        response = self.client.post('/section/create/', data=data)
        print(response.status_code, status.HTTP_403_FORBIDDEN)
        print(response.json().get("detail"), "У вас недостаточно прав для выполнения данного действия.")
