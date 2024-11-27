from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import patch
from django.urls import reverse


class ProjectListViewTest(APITestCase):
    @patch('realty.domain.project.selectors.ProjectRepository.get_all_projects')
    def test_get_project_list(self, mock_get_all_projects):
        mock_get_all_projects.return_value = [
            {'id': 1, 'name': 'first', 'description': 'first', 'amount_floors': 9, 'rating': 'A', 'image_url': 'image1.jpg'},
            {'id': 2, 'name': 'second', 'description': 'second', 'amount_floors': 9, 'rating': 'A', 'image_url': 'image2.jpg'},
            {'id': 3, 'name': 'third', 'description': 'third', 'amount_floors': 9, 'rating': 'A', 'image_url': 'image3.jpg'},
            {'id': 4, 'name': 'fourth', 'description': 'fourth', 'amount_floors': 9, 'rating': 'A', 'image_url': 'image4.jpg'},
        ]

        url = reverse('project-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.json()['results']), 3)
        self.assertEqual(response.json()['results'][0]['name'], 'first')


class ProjectDetailViewTest(APITestCase):
    @patch('realty.domain.project.selectors.ProjectRepository.get_project_by_id')
    def test_get_project_detail_success(self, mock_get_project_by_id):
        mock_get_project_by_id.return_value = {
            'id': 1, 'name': 'first', 'description': 'first', 'amount_floors': 9, 'rating': 'A', 'image_url': 'image1.jpg'
        }

        url = reverse('project-detail', args=[1])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'first')

    @patch('realty.domain.project.selectors.ProjectRepository.get_project_by_id')
    def test_get_project_detail_fail(self, mock_get_project_by_id):
        mock_get_project_by_id.side_effect = ValueError('Project not found')

        url = reverse('project-detail', args=[99])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json()['error'], 'Project not found')