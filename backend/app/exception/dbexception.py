class DatabaseConnectionException(Exception):
    def __init__(self, message: str = "Database connection failed"):
        self.name = "DatabaseConnectionError"
        self.message = message
        self.status_code = 500