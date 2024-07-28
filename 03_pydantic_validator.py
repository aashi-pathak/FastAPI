from pydantic import BaseModel, field_validator, model_validator

class CreateUser(BaseModel):
    email: str
    password: str
    confirm_password: str

    @field_validator("email")
    def validate_email(cls, value):
        if "admin" in value:
            raise ValueError("This email is not allowed")
        return value
    
    @model_validator(mode="after")
    def validate_password(self):
        password = self.password
        confirm_password = self.confirm_password

        if password!=confirm_password :
            raise ValueError("two passqords shoulrd match")
        return self
        
    
CreateUser(email="abcd@gmail.com", password="ahdg", confirm_password="ahdg")

