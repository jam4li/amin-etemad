from rest_framework import views, status
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _

from utils.response import ApiResponse

from apps.products.models import Product
from apps.products.serializers.user_serializers import ProductSerializer
from apps.products.decorators import auth_required


class ProductsAPIView(views.APIView):
    def get(self, request, pk=None):
        if pk:
            product_obj = Product.objects.get(id=pk)

            serializer = ProductSerializer(
                product_obj,
                context={"request": request},
            )

        else:
            products_list = Product.objects.all()

            serializer = ProductSerializer(
                products_list,
                many=True,
                context={"request": request},
            )

        success_response = ApiResponse(
            success=True,
            code=200,
            data=serializer.data,
            message='Data retrieved successfully'
        )

        return Response(
            success_response,
            status=status.HTTP_200_OK,
        )

    @auth_required
    def post(self, request):
        serializer = ProductSerializer(
            data=request.data,
            context={'request': request},
        )

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            success_response = ApiResponse(
                success=True,
                code=201,
                data=serializer.data,
                message='Product has been created successfully.'
            )

            return Response(
                success_response,
                status=status.HTTP_201_CREATED,
            )

        fail_response = ApiResponse(
            success=False,
            code=400,
            error={
                'code': 'bad_request',
                'detail': 'Failed to create product.',
            }
        )

        return Response(
            fail_response,
            status=status.HTTP_400_BAD_REQUEST,
        )

    @auth_required
    def put(self, request, pk):
        product = Product.objects.get(id=pk)

        serializer = ProductSerializer(
            product,
            data=request.data,
        )

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            success_response = ApiResponse(
                success=True,
                code=200,
                data=serializer.data,
                message='Product has been updated successfully.'
            )

            return Response(
                success_response,
                status=status.HTTP_200_OK,
            )

        fail_response = ApiResponse(
            success=False,
            code=400,
            error={
                'code': 'bad_request',
                'detail': 'Failed to update product.',
            }
        )

        return Response(
            fail_response,
            status=status.HTTP_400_BAD_REQUEST,
        )

    @auth_required
    def delete(self, request, pk):
        try:
            product = Product.objects.get(id=pk)

            product.delete()

            success_response = ApiResponse(
                success=True,
                code=204,
                data={},
                message='Product has been deleted successfully.'
            )

            return Response(
                success_response,
                status=status.HTTP_204_NO_CONTENT,
            )

        except Product.DoesNotExist:
            fail_response = ApiResponse(
                success=False,
                code=404,
                error={
                    'code': 'product_not_found',
                    'detail': 'Product not found in the database',
                }
            )

            return Response(
                fail_response,
                status=status.HTTP_404_NOT_FOUND,
            )
