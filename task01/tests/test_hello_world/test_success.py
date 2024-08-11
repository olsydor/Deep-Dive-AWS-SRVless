from tests.test_hello_world import HelloWorldLambdaTestCase

class TestSuccess(HelloWorldLambdaTestCase):

    def test_success(self):
        # Виконання запиту до функції
        response = self.HANDLER.handle_request(dict(), dict())
        
        # Перевірка значення statusCode у повернутому словнику
        self.assertEqual(response['statusCode'], 200)
        # Перевірка значення message у повернутому словнику
        self.assertEqual(response['message'], "Hello from Lambda")
