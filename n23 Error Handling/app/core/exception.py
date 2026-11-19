from fastapi import FastAPI, HTTPException, Request,status 
from fastapi.responses import JSONResponse
from fastapi.exceptions import ResponseValidationError
from rich.panel import Panel
from rich import print 

class FastShipError(Exception):
    """Base exception for all exceptions we raise in our FastShip API."""
    status = status.HTTP_400_BAD_REQUEST


class EntityNotFound(FastShipError):
    """Entity not found in database."""
    status = status.HTTP_404_NOT_FOUND


class ClientNotAuthorized(FastShipError):
    """Client is not authorized to perform the action."""
    status = status.HTTP_401_UNAUTHORIZED


class InValidToken(FastShipError):
    """Token is invalid"""
    status = status.HTTP_401_UNAUTHORIZED




def get_handler(status_code: int,detail: str):
    def handler(request: Request, exception: InValidToken):

        print(Panel(f"Handled : {exception.__class__.__name__}"))
        raise HTTPException(
            detail=detail,
            status_code=status_code,
        )
    return handler
def response_validation_error_handler(
        request: Request,
        exception: ResponseValidationError,
    ):
        print(Panel(f"Handled : {exception.__class__.__name__}"))
        raise HTTPException(
            detail={"detail": "Response has validation errors"},
            status_code=500,
        )

def add_exception_handlers(app: FastAPI):

    for subclass in FastShipError.__subclasses__():
        app.add_exception_handler(
            subclass,
            get_handler(
                subclass.status,
                subclass.__doc__
            )
        )

    app.add_exception_handler(
        ResponseValidationError,
        response_validation_error_handler,
    )

    @app.exception_handler(AttributeError)
    def internal_server_error_handler(
        request: Request,
        exception: Exception,
    ):
        print(Panel(f"Handled : {exception.__class__.__name__}"))
        return JSONResponse(
            content={"detail": "Something went wrong"},
            status_code=500,
            headers={"X-Error": str(exception)},
        )