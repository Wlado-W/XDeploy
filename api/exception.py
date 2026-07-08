class XUIError(Exception):
    """Базовая ошибка API 3X-UI"""

class AuthenticationError(XUIError):
    """Ошибка авторизации"""

class RequestError(XUIError):
    """Ошибка выполнения запроса"""        