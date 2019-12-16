class NotFoundError(Exception):
    def __init__(self, resource, resource_id):
        Exception.__init__(self)
        self.resource = resource
        self.resource_id = resource_id

    def get_dict(self):
        return {'error': f"{self.resource} {self.resource_id} not found"}


class CurrencyNotFoundError(NotFoundError):
    def __init__(self, resource_id):
        NotFoundError.__init__(self, "Currency", resource_id)
