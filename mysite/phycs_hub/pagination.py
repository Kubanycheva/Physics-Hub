from rest_framework import pagination
from .models import Material


class MaterialPagination(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 50