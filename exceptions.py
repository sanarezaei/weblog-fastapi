from fastapi import HTTPException, status

NotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
)

class UserNotFound(HTTPException):
    def __init__(self) -> None:
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = "User not found"
        

class UserAlreadyExists(HTTPException):
    def __init__(self):
        self.status_code = 400
        self.detail = "user already exists!"
