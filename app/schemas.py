from pydantic import BaseModel

class BlogBase(BaseModel):

    title: str
    subject: str
    img: str
    des: str


class BlogResponse(BlogBase):

    id: int

    class Config:
        from_attributes = True