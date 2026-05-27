from pydantic import BaseModel, Field


class OrganizationCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)


class OrganizationRead(BaseModel):
    id: str
    name: str
