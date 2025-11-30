class APIError(Exception):
    def __init__(self, message, code=400):
        super().__init__(message)
        self.code = code

    @staticmethod
    def from_response(response):
        msg = response.get('error', "unknown error")
        code = response.get("code", 500)
        return APIError(msg, code=code)
