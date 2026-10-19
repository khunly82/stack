from pydantic import BaseModel, EmailStr, Field


class MyPatchRequestDto(BaseModel):
    email: EmailStr | None = Field(default=None)
    score: int | None = Field(default=None)
    comment: str|None = Field(default=None, max_length=1000)