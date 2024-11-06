from rest_framework import viewsets
from core.publisher.application.use_cases.create_publisher import CreatePublisherInput, CreatePublisherUseCase
from core.publisher.application.use_cases.list_publisher import ListPublisherUseCase
from core.publisher.infra.publisher_django_app.repository import DjangoORMPublisherRepository
from core.publisher.infra.publisher_django_app.serializers import CreatePublisherRequestSerializer, CreatePublisherResponseSerializer, ListPublisherResponseSerializer
from rest_framework.response import Response
from rest_framework import status

class PublisherViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = CreatePublisherRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        request_input = CreatePublisherInput(**serializer.validated_data)
        use_case = CreatePublisherUseCase(repository=DjangoORMPublisherRepository())

        output = use_case.execute(request_input)
        return Response(
            status=status.HTTP_201_CREATED, 
            data=CreatePublisherResponseSerializer(output).data
            )
    def list(self):
        use_case = ListPublisherUseCase(repository=DjangoORMPublisherRepository())
        output = use_case.execute()
        return Response(
            status=status.HTTP_200_OK,
            data=ListPublisherResponseSerializer(output, many=True).data
        )