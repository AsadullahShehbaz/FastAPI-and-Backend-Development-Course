from fastapi import FastAPI, HTTPException, Request, Response,status 
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import JSONResponse
from rich.panel import Panel
from rich import print
from sqlalchemy import JSON 


class AsadullahAIShipError(Exception):
    """Base exception for all exceptions we raise in our AsadullahAIShip API."""
    status = status.HTTP_400_BAD_REQUEST

class EntityNotFound(AsadullahAIShipError):
    """Entity not found in database"""
    status = status.HTTP_404_NOT_FOUND

class ClientNotAuthorized(AsadullahAIShipError):
    """Client is not authorized to perform the action"""
    status=status.HTTP_401_UNAUTHORIZED


class ClientNotVerified(AsadullahAIShipError):
    """Client is not verified"""

    pass


class NothingToUpdate(AsadullahAIShipError):
    """No data provided to update"""
    pass 

class BadCredentials(AsadullahAIShipError):
    """User email or password is incorrect"""

    pass


class InvalidToken(AsadullahAIShipError):
    """Access token is invalid or expired"""

    status=status.HTTP_401_UNAUTHORIZED


class DeliveryPartnerNotAvailable(AsadullahAIShipError):
    """Delivery partner/s do not service the destination"""

    pass


class DeliveryPartnerCapacityExceeded(AsadullahAIShipError):
    """Delivery partner has reached their max handling capacity"""

    pass

def get_handler(status: int,detail: str): 
    def handler(request: Request,exception: Exception):

        print(Panel(f"Handled {exception.__class__.__name__}"))
        raise HTTPException(
            status_code=status,
            detail=detail 
        )
    return handler

def response_validation_error_handler(request: Request,exception: ResponseValidationError):
        print(Panel(f"Handled {exception.__class__.__name__}"))
        return JSONResponse(
            status_code=500,
            content="Response has validation error",
            headers={
                "X-Error":f"{exception.__class__.__name__}",
            }
        )


def internel_server_error_handler(request: Request,exception: Exception):
        print(Panel(f"Handled {exception.__class__.__name__}"))
        return JSONResponse(
            status_code=500,
            content={"detail":"Something went wrong"},
            headers={
                "X-Error":f"{exception.__class__.__name__}",
            }
        )



def add_exception_handler(app: FastAPI):
    # Register handlers for custom exception

    for subclass in AsadullahAIShipError.__subclasses__():
        app.add_exception_handler(
            subclass,
            get_handler(
                status = subclass.status,
                detail=subclass.__doc__
            )
        )
    app.add_exception_handler(ResponseValidationError,response_validation_error_handler)
    app.add_exception_handler(status.HTTP_500_INTERNAL_SERVER_ERROR,internel_server_error_handler)
    
 