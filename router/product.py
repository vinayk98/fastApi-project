from typing import List, Optional

from fastapi import APIRouter, Cookie, Depends, Form, Header
from fastapi.responses import HTMLResponse, PlainTextResponse, Response
from sqlalchemy.orm import Session

from db.database import get_db

router = APIRouter(
    prefix="/product",
    tags=["product"]
)
products = ["laptop", "mobile", "tablet"]

@router.post("/new")
def create_product(product_name: str = Form(...)):
    products.append(product_name)
    return products

@router.get("/all")
def get_all_products(db: Session = Depends(get_db)):
    data = " ".join(products)
    response = Response(content=data, media_type="text/plain")
    response.set_cookie(key="test_cookie", value="test_value")
    return response

@router.get("/withHeader")
def get_all_products(response: Response, 
                     custom_header: Optional[List[str]] = Header(None),
                     test_cookie: Optional[str] = Cookie(None)
                     ):
    if custom_header:
        response.headers["custom_response_header"] = ", ".join(custom_header) if custom_header else "No custom header provided"
    return {
        "data": products,
        "custom_header": custom_header,
        "my_cookie": test_cookie
    }

@router.get("/{id}", responses={
    200: {
        "content": {"text/html": {
          "example": "<div>product</div>"
        }},
        "description": "Return the product details in HTML format",
    },
    404: {
        "content": {"text/plain": {
            "example": "Product not found"
        }},
        "description": "A clear message indicating that the requested product was not found",
    },
})

def get_product(id: int, db: Session = Depends(get_db)):
    if id < 0 or id >= len(products):
        out = "Product not found"
        return PlainTextResponse(content=out, media_type="text/plain", status_code=404)
    else:
        product = products[id]
        out = f"""
    <head>
    <style>
    .product {{
        width: 300px;
        height: 200px;
        border: 1px solid #ccc;
        border-radius: 5px;
        background-color: #f9f9f9;
        text-align: center;
        padding: 20px;     
        }}
    </style>
    </head>     
    <div class="product">
       {product}
    </div>
    """
    return HTMLResponse(content=out, media_type="text/html")
    