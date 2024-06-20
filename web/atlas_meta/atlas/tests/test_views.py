import datetime

from rest_framework.test import APIClient, APITestCase

from .factories import MetaDataFactory
from ..models import MetaData


class TestMetaData(APITestCase):
    client = None

    def setUp(self):
        self.client = APIClient()

    def test_non_existing(self):
        data = {
            "id": "hoi",
        }

        response = self.client.put(
            "/metadata/{}/".format(data["id"]), data, format="json"
        )
        self.assertEqual(response.status_code, 404)

    def test_update_shouldnt_update_fields(self):
        m = MetaDataFactory.create(
            id="hoi",
            title="hoihoi",
            update_frequency="4 x per week",
        )

        data = {
            "id": "hoi",
            "title": "haihai",
            "update_frequency": "5 x per week",
        }

        response = self.client.put(
            "/metadata/{}/".format(data["id"]), data, format="json"
        )
        self.assertEqual(response.status_code, 200)

        model = MetaData.objects.get(id=m.id)
        self.assertEqual(model.update_frequency, "4 x per week")
        self.assertEqual(model.title, "hoihoi")

    def test_get(self):
        MetaDataFactory.create(id="hoi")

        num_models = MetaData.objects.exclude(title__isnull=True).count()

        response = self.client.get("/metadata/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), num_models)
