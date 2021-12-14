from sqlmodel import SQLModel, Field
from typing import Optional


class OrganizationBase(SQLModel):
    name: str
    address1: Optional[int] = None
    address2: Optional[int] = None
    city: Optional[int] = None


class Organization(OrganizationBase, table=True):
    id: int = Field(default=None, primary_key=True)


class OrganizationCreate(OrganizationBase):
    pass
