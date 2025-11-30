class APIError(Exception):
    def __init__(self, message, code=400):
        super().__init__(message)
        self.code = code

    @staticmethod
    def from_response(response):
        msg = response.get('error', "unknown error")
        code = response.get("code", 500)
        return APIError(msg, code=code)


# symulujemy odpowiedz z serwera
response = {"error": "Brak tokena JWT", "code": 401}
raise APIError.from_response(response)
# Traceback (most recent call last):
#   File "/Users/radoslawjaniak/PycharmProjects/BootCamp-11-10-2025A/day_8_30_11_2025/kl19a.py", line 15, in <module>
#     raise APIError.from_response(response)
# APIError: Brak tokena JWT
