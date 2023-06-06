import requests
from bs4 import BeautifulSoup
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import ScrapedData
from app.serializers import ScrapedDataSerializer


class ScrapingView(APIView):
    def get(self, request):
        response = requests.get('https://www.brightermonday.co.ke/jobs')

        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find('h1').text
        content = soup.find('p').text

        scraped_data = ScrapedData.objects.create(title=title, content=content)

        serializer = ScrapedDataSerializer(scraped_data)

        return Response(serializer.data)


class JobViewSet(viewsets.ModelViewSet):
    queryset = ScrapedData.objects.all()
    serializer_class = ScrapedDataSerializer
