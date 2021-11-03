import json
from channels.generic.websocket import WebsocketConsumer

class LocConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        if message == 'biblioteca':
            self.send(text_data=json.dumps({
                'message': 'Servidor: Te recomendamos estos super libros!!!'
            }))
