import unittest
from app import create_app

class AgeCheckerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_check_age_under(self):
        res = self.app.post("/check-age", json={"birth_date": "2010-01-01"})
        self.assertEqual(res.status_code, 200)
        self.assertFalse(res.get_json()["legal"])

    def test_check_age_over(self):
        res = self.app.post("/check-age", json={"birth_date": "1990-01-01"})
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.get_json()["legal"])

    def test_requests_endpoint(self):
        self.app.post("/check-age", json={"birth_date": "1990-01-01"})
        self.app.post("/check-age", json={"birth_date": "2010-01-01"})

        res = self.app.get("/requests")
        self.assertEqual(res.status_code, 200)

        data = res.get_json()
        self.assertIn("total_requests", data)
        self.assertGreaterEqual(data["total_requests"], 2)
   
    def test_index_page(self):
        res = self.app.get("/")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Check if Your Age is Legal", res.data)

    def test_health_check(self):
        res = self.app.get("/health")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_data(as_text=True), "OK")

    def test_metrics_endpoint(self):
        res = self.app.get("/metrics")
        self.assertEqual(res.status_code, 200)
        self.assertIn("total_requests", res.get_data(as_text=True))
