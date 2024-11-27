from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import patch
from django.urls import reverse


class FloorListViewTest(APITestCase):
    @patch('realty.domain.floor.selectors.FloorRepository.get_all_floors')
    def test_get_floor_list(self, mock_get_all_floors):
        mock_get_all_floors.return_value = [
            {'id': 1, 'floor_number': 1, 'section_id': 1},
            {'id': 2, 'floor_number': 2, 'section_id': 2},
            {'id': 3, 'floor_number': 3, 'section_id': 3},
            {'id': 4, 'floor_number': 4, 'section_id': 4},
            {'id': 5, 'floor_number': 5, 'section_id': 5},
            {'id': 6, 'floor_number': 6, 'section_id': 6},
        ]

        url = reverse('floor-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.json()['results']), 5)
        self.assertEqual(response.json()['results'][0]['floor_number'], 1)


class FloorDetailViewTest(APITestCase):
    @patch('realty.domain.floor.selectors.FloorRepository.get_floor_by_id')
    def test_get_floor_detail_success(self, mock_get_floor_by_id):
        mock_get_floor_by_id.return_value = {'id': 1, 'floor_number': 1, 'section_id': 1}

        url = reverse('floor-detail', args=[1])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['floor_number'], 1)

    @patch('realty.domain.floor.selectors.FloorRepository.get_floor_by_id')
    def test_get_floor_detail_fail(self, mock_get_floor_by_id):
        mock_get_floor_by_id.side_effect = ValueError('Floor not found')

        url = reverse('floor-detail', args=[99])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json()['error'], 'Floor not found')