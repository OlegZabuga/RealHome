from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import patch
from django.urls import reverse


class ApartmentListViewTest(APITestCase):
    @patch('realty.domain.apartment.selectors.ApartmentRepository.get_all_apartments')
    def test_get_apartment_list(self, mock_get_all_apartments):
        mock_get_all_apartments.return_value = [
            {'id': 1, 'num': 1, 'on_sale': True, 'type_id': 1, 'floor_id': 1, 'section_id': 1, 'building_id': 1,
             'image_url': 'image1.jpg'},
            {'id': 2, 'num': 2, 'on_sale': True, 'type_id': 2, 'floor_id': 2, 'section_id': 2, 'building_id': 2,
             'image_url': 'image2.jpg'},
            {'id': 3, 'num': 3, 'on_sale': True, 'type_id': 3, 'floor_id': 3, 'section_id': 3, 'building_id': 3,
             'image_url': 'image3.jpg'},
            {'id': 4, 'num': 4, 'on_sale': True, 'type_id': 4, 'floor_id': 4, 'section_id': 4, 'building_id': 4,
             'image_url': 'image4.jpg'},
        ]

        url = reverse('apartment-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.json()['results']), 3)
        self.assertEqual(response.json()['results'][0]['num'], 1)


class ApartmentDetailViewTest(APITestCase):
    @patch('realty.domain.apartment.selectors.ApartmentRepository.get_apartment_by_id')
    def test_get_apartment_detail_success(self, mock_get_apartment_by_id):
        mock_get_apartment_by_id.return_value = {
            'id': 1, 'num': 1,
            'on_sale': True, 'type_id': 1,
            'floor_id': 1, 'section_id': 1,
            'building_id': 1, 'image_url': 'image1.jpg'
        }

        url = reverse('apartment-detail', args=[1])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['num'], 1)

    @patch('realty.domain.apartment.selectors.ApartmentRepository.get_apartment_by_id')
    def test_get_apartment_detail_fail(self, mock_get_apartment_by_id):
        mock_get_apartment_by_id.side_effect = ValueError('Apartment not found')

        url = reverse('apartment-detail', args=[99])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json()['error'], 'Apartment not found')
