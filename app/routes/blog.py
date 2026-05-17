from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Blog
from app.schemas import BlogBase

router = APIRouter()


# GET BLOGS
@router.get("/get")
def get_blogs(db: Session = Depends(get_db)):

    blogs = db.query(Blog).all()

    return blogs


# ADD BLOG
@router.post("/add")
def add_blog(blog: BlogBase, db: Session = Depends(get_db)):

    new_blog = Blog(
        title=blog.title,
        subject=blog.subject,
        img=blog.img,
        des=blog.des
    )

    db.add(new_blog)

    db.commit()

    db.refresh(new_blog)

    return {
        "message": "Blog Added Successfully"
    }


# DELETE BLOG
@router.delete("/delete/{id}")
def delete_blog(id: int, db: Session = Depends(get_db)):

    blog = db.query(Blog).filter(Blog.id == id).first()

    if blog:

        db.delete(blog)

        db.commit()

        return {
            "message": "Blog Deleted Successfully"
        }

    return {
        "message": "Blog Not Found"
    }