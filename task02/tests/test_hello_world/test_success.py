from tests.test_hello_world import HelloWorldLambdaTestCase

class TestHelloWorldLambda(HelloWorldLambdaTestCase):

    def test_success(self):
        # Simulate a GET request to the /hello path
        event = {
            "path": "/hello",
            "httpMethod": "GET"
        }
        response = self.HANDLER.handle_request(event, dict())
        
        # Verify that the statusCode is 200
        self.assertEqual(response['statusCode'], 200)
        # Verify that the message is "Hello from Lambda"
        self.assertEqual(response['message'], "Hello from Lambda")

    def test_bad_request(self):
        # Simulate a GET request to an incorrect path
        event = {
            "path": "/wrong_path",
            "httpMethod": "GET"
        }
        response = self.HANDLER.handle_request(event, dict())

        # Verify that the statusCode is 400
        self.assertEqual(response['statusCode'], 400)
        # Verify that the error message is correctly formatted
        expected_message = "Bad request syntax or unsupported method. Request path: /wrong_path. HTTP method: GET"
        self.assertEqual(response['message'], expected_message)
        
        # Simulate a POST request to the /hello path (unsupported method)
        event = {
            "path": "/hello",
            "httpMethod": "POST"
        }
        response = self.HANDLER.handle_request(event, dict())

        # Verify that the statusCode is 400
        self.assertEqual(response['statusCode'], 400)
        # Verify that the error message is correctly formatted
        expected_message = "Bad request syntax or unsupported method. Request path: /hello. HTTP method: POST"
        self.assertEqual(response['message'], expected_message)
