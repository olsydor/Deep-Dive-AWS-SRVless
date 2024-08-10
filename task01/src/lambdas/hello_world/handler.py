from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('HelloWorld-handler')

class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
        # Можна додати валідацію вхідних даних, якщо необхідно
        pass
        
    def handle_request(self, event, context):
        """
        Описуємо вхідний event тут
        """
        # Реалізуємо бізнес-логіку, яка формує потрібну відповідь
        response = {
            "statusCode": 200,
            "message": "Hello from Lambda"
        }
        return response
    

HANDLER = HelloWorld()

def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
