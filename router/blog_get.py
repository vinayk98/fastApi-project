from fastapi import APIRouter, status, Response
from enum import Enum
from typing import Optional

from fastapi.params import Depends

from router.blog_post import required_functionality

#with this router we mention common prefix and tags for all the routes in this router
router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)

class blogType(str, Enum):
    short = "short"
    long = "long"
    story = "story"

@router.get("/type/{type}", summary="Get blogs by type", description="This API endpoint retrieves blogs based on their type.")
def blog_type(type: blogType):
    return {"message": f"Blog type is {type}"}

@router.get("/{id}/comments/{comment_id}", tags=["comments"])
def get_comment_from_blog(id:int, comment_id:int, valid:bool = True, username:Optional[str] = None):
    """
    This API endpoint retrieves a specific comment from a blog post based on the provided blog ID and comment ID.
    It also accepts optional query parameters for validation and username.
    - **id**: The ID of the blog post.
    - **comment_id**: The ID of the comment to retrieve.
    - **valid**: Optional query parameter to indicate if the comment is valid (default is True).
    - **username**: Optional query parameter to specify the username associated with the comment."""
    return {"blog_id": id, "comment_id": comment_id, "valid": valid, "username": username}

@router.get("/all", 
tags=["blogs"], 
summary="Get all blogs", 
description="This API endpoint retrieves all blogs with optional pagination parameters.",
response_description="The response includes a message indicating the current page and page size for the retrieved blogs."
)
def get_all_blogs(page: int = 1, page_size: Optional[int] = None, req_parameter: dict = Depends(required_functionality)):
    return {"message": f"All blogs - Page: {page} and Page Size: {page_size}", "req_parameter": req_parameter}

@router.get("/{id}",status_code = status.HTTP_200_OK, summary="Get a blog by ID", description="This API endpoint retrieves a specific blog by its ID. If the blog ID is greater than 5, it returns a 404 error indicating that the blog was not found.")
def blog(id: int, response: Response):
    if(id > 5):
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Blog not found!"}
    else:
        return {"blog_id": id}
