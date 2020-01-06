class BadResource(Exception):
    def __init__(self, resource, resource_type):
        Exception.__init__(self)
        self.resource = resource
        self.resource_type = resource_type

    def get_dict(self):
        return {'error': '{} is not a valid {}'.format(self.resource, self.resource_type)}


class BadUser(BadResource):
    def __init__(self, resource):
        BadResource.__init__(self, resource, 'user')
