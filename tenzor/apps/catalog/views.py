from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Category, Goods
from .serializers import CategorySerializer, GoodsSerializer
from itertools import chain
from collections import defaultdict


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 1000


class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.none()
    serializer_class = GoodsSerializer
    pagination_class = StandardResultsSetPagination

    permission_classes = (AllowAny,)

    def get_queryset(self):
        print('we are here', self.request.query_params)
        complete_field = self.request.query_params.get('input', -1)
        category_id = self.request.query_params.get('category', -1)
        goods_dict = defaultdict(int)
        chain_query = []
        result_query = []
        query_start,query_regexp = [], []
        if complete_field == -1:
            if category_id == -1:
                return Goods.objects.all()
            return Goods.objects.filter(category=category_id)
        if category_id == -1:
            print('no category')
            query_start = Goods.objects.filter(name__istartswith=complete_field)
            query_regexp = Goods.objects.filter(name__iregex=r'^(.)+' + complete_field)
        else:
            print('yes category')
            query_start = Goods.objects.filter(category_id=category_id, name__istartswith=complete_field)
            query_regexp = Goods.objects.filter(category_id=category_id, name__iregex=r'^(.)+' + complete_field)
        chain_query = list(chain(query_start, query_regexp))
        for item in chain_query:
            if not goods_dict[item]:
                result_query.append(item)
            goods_dict[item] += 1
        print(result_query)
        return result_query


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = (AllowAny,)
