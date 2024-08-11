from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('HelloWorld-handler')

class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
        # Валідація вхідних даних, якщо необхідно
        pass
        
    def handle_request(self, event, context):
        """
        Основна логіка обробки запиту Lambda.
        Повертає просто значення 200, як очікується в тесті.
        """
        return 200
    
    def lambda_handler(self, event, context):
        """
        Цей метод викликається безпосередньо, коли запускається Lambda-функція.
        """
        return self.handle_request(event, context)

HANDLER = HelloWorld()

def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
