from fastapi import Request
from fastapi.responses import JSONResponse
from app.exception.dbexception import DatabaseConnectionException

async def db_exception_handler(request: Request, exc: DatabaseConnectionException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.name,
            "message": exc.message
        }
    )