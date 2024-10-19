class YearException(Exception):
    code: int

    def __init__(self, message: str, code: int = 400):
        super().__init__(message)
        self.code = code
