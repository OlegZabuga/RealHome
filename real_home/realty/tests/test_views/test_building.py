from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import patch
from django.urls import reverse


class BuildingListViewTest(APITestCase):
    @patch('realty.domain.building.selectors.BuildingRepository.get_all_buildings')
    def test_get_buildings_list(self, mock_get_all_buildings):
        mock_get_all_buildings.return_value = [
            {'id': 1, 'num': 1, 'on_street': 'Kirova', 'project_id': 1, 'image_url': 'image1.jpg'},
            {'id': 2, 'num': 2, 'on_street': 'Kirova', 'project_id': 2, 'image_url': 'image2.jpg'},
            {'id': 3, 'num': 3, 'on_street': 'Kirova', 'project_id': 3, 'image_url': 'image3.jpg'},
            {'id': 4, 'num': 4, 'on_street': 'Kirova', 'project_id': 4, 'image_url': 'image4.jpg'},
        ]

        url = reverse('building-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.json()['results']), 3)
        self.assertEqual(response.json()['results'][0]['num'], 1)


class BuildingDetailViewTest(APITestCase):
    @patch('realty.domain.building.selectors.BuildingRepository.get_building_by_id')
    def test_get_building_detail_success(self, mock_get_building_by_id):
        mock_get_building_by_id.return_value = {
            'id': 1, 'num': 1, 'on_street': 'Kirova', 'project_id': 1, 'image_url': 'image1.jpg'
        }
        url = reverse('building-detail', args=[1])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['num'], 1)

    @patch('realty.domain.building.selectors.BuildingRepository.get_building_by_id')
    def test_get_building_detail_fail(self, mock_get_building_by_id):
        mock_get_building_by_id.side_effect = ValueError('Building not found')

        url = reverse('building-detail', args=[99])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json()['error'], 'Building not found')
