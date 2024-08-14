import json
from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('HelloWorld-handler')

class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
        """
        Валідація запиту, перевірка, чи шлях відповідає /hello.
        """
        path = event.get('rawPath')
        method = event.get('requestContext', {}).get('http', {}).get('method')

        _LOG.debug(f"Received path: {path}, method: {method}")

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
        """
        validation_result = self.validate_request(event)

        if validation_result["is_valid"]:
            return {
                "statusCode": 200,
                "message": "Hello from Lambda"
            }
        else:
            path = validation_result['path'] or 'Unknown'
            method = validation_result['method'] or 'Unknown'
            return {
                "statusCode": 400,
                "message": f"Bad request syntax or unsupported method. Request path: {path}. HTTP method: {method}"
            }
    
    def lambda_handler(self, event, context):
        """
        Цей метод викликається безпосередньо, коли запускається Lambda-функція.
        """
        _LOG.debug(f"Incoming event: {json.dumps(event)}")

        return self.handle_request(event, context)

HANDLER = HelloWorld()

def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)