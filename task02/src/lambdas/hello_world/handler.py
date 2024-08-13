import json
from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('HelloWorld-handler')

class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
        """
        Валідація запиту, перевірка, чи шлях відповідає /hello.
        """
        path = event.get('path')
        method = event.get('httpMethod')

        if path == '/hello' and method == 'GET':
            return {
                "is_valid": True
            }
        else:
            return {
                "is_valid": False,
                "path": path,
                "method": method
            }
        
    def handle_request(self, event, context):
        """
        Основна логіка обробки запиту Lambda.
        Повертає відповідь з кодом 200 для /hello і кодом 400 для інших шляхів.
        """
        validation_result = self.validate_request(event)

        if validation_result["is_valid"]:
            response = {
                "statusCode": 200,
                "body": json.dumps({
                    "message": "Hello from Lambda"
                })
            }
        else:
            response = {
                "statusCode": 400,
                "body": json.dumps({
                    "message": f"Bad request syntax or unsupported method. Request path: {validation_result['path']}. HTTP method: {validation_result['method']}"
                })
            }

        return response
    
    def lambda_handler(self, event, context):
        """
        Цей метод викликається безпосередньо, коли запускається Lambda-функція.
        """
        return self.handle_request(event, context)

HANDLER = HelloWorld()

def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
