from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum
from datetime import datetime

class Language(str, Enum):
    PY = "python"
    JAVA = "java"
    GO = "go"

class Comment(BaseModel):
    text: Optional[str] = None

class Blog(BaseModel):
    title: str
    description: Optional[str] = None
    is_active: bool
    language: Language = Language.PY
    created_at: datetime = Field(default_factory=datetime.now)
    comments: Optional[list[Comment]]

first_blog = Blog(title="My title", is_active=True, comments=[{"text":"My first comment"}])
print(first_blog)

