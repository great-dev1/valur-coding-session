from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class MultiplicationTests(APITestCase):
  def setUp(self):
    self.url = reverse('multiply')

  def test_multiply_positive_numbers(self):
    """Test multiplication of two positive numbers"""
    data = {'number1': 5.0, 'number2': 3.0}
    response = self.client.post(self.url, data, format='json')
    
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['result'], 15.0)
    self.assertEqual(response.data['numbers'], data)

  def test_multiply_negative_numbers(self):
    """Test multiplication with negative numbers"""
    data = {'number1': -2.0, 'number2': 4.0}
    response = self.client.post(self.url, data, format='json')
    
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['result'], -8.0)

  def test_invalid_input(self):
    """Test with invalid input (non-numeric values)"""
    data = {'number1': 'invalid', 'number2': 3.0}
    response = self.client.post(self.url, data, format='json')
    
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)