from django.http import JsonResponse

class CommandResponse:
    def __init__(self, successful, data):
        self.successful = successful
        self.data = data

    def json(self):
        _type = '1' if self.successful else '0' 
        return {'type':  'ciao', 'data': self.data }

    def jsonResponse(self):
        return JsonResponse(self.json())