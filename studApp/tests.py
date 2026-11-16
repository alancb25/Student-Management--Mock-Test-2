from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class AllStudentListViewTests(APITestCase):
    def test_student_list_requires_token_authentication(self):
        response = self.client.get('/studentlist')
        self.assertEqual(response.status_code, 401)

        user = User.objects.create_user(username='student-list-user', password='test-password')
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

        response = self.client.get('/studentlist')
        self.assertEqual(response.status_code, 200)
