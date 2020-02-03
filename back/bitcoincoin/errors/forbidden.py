class ForbiddenError(Exception):
    def __init__(self, required_status):
        Exception.__init__(self)
        self.required_status = required_status

    def get_dict(self):
        return {'error': f"The requested resource is forbidden : it requires a {self.required_status} status"}


class ForbiddenAdminError(NotFoundError):
    def __init__(self, required_status):
        ForbiddenError.__init__(self, "admin")
