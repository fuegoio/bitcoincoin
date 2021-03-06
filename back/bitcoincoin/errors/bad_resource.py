class BadResourceError(Exception):
    def __init__(self, resource, resource_type):
        Exception.__init__(self)
        self.resource = resource
        self.resource_type = resource_type

    def get_dict(self):
        return {'error': '{} is not a valid {}'.format(self.resource, self.resource_type)}


class BadIdError(BadResourceError):
    def __init__(self, resource):
        BadResourceError.__init__(self, resource, 'id')


class BadQuantityError(BadResourceError):
    def __init__(self, resource):
        BadResourceError.__init__(self, resource, 'quantity')


class BadCurrencyValueError(BadResourceError):
    def __init__(self, resource):
        BadResourceError.__init__(self, resource, 'currency value')


class BadBoolError(BadResourceError):
    def __init__(self, resource):
        BadResourceError.__init__(self, resource, 'boolean')


class BadCurrencyProviderError(BadResourceError):
    def __init__(self, resource):
        BadResourceError.__init__(self, resource, 'currency provider')


class EmptyStringError(BadResourceError):
    def __init__(self, resource):
        BadResourceError.__init__(self, resource, 'string')


class BadFromDatetimeError(BadResourceError):
    def __init__(self, resource):
        BadResourceError.__init__(self, resource, 'from_date')


class BadToDatetimeError(BadResourceError):
    def __init__(self, resource):
        BadResourceError.__init__(self, resource, 'to_date')


class BadLimitError(BadResourceError):
    def __init__(self, resource):
        BadResourceError.__init__(self, resource, 'limit')
