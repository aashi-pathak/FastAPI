from fastapi import FastAPI, Depends, HTTPException, status

# blogs = {
#     "1": "ahdsh",
#     "2": "hjdvbjsb",
#     "3": "jdgjsb"
# }

# users = {
#     "8": "abc",
#     "9": "def"
# }

# app = FastAPI(title = "Dependency Injection")


# def get_object_or_404(model: dict, id: str):
#     obj = model.get(id)
#     if not obj:
#         raise HTTPException("Blog with if {id} does not exist", status_code=status.HTTP_404_NOT_FOUND)
#     return obj

# class GetObjectOr404:
#     def __init__(self, model) -> None:
#         self.model = model

#     def __call__(self, id: str):
#         obj = self.model.get(id)
#         if not obj:
#             raise HTTPException("Blog with if {id} does not exist", status_code=status.HTTP_404_NOT_FOUND)
#         return obj

# blog_dependency = GetObjectOr404(blogs)
# @app.get("/blog/{id}")
# def get_blogs(blog_name: str = Depends(blog_dependency)):
#     return blog_name

# user_dependency = GetObjectOr404(users)
# @app.get("/user/{id}")
# def get_blogs(user_name: str = Depends(user_dependency)):
#     return user_name

development_db = ["DB for developemnt"]

def get_db_session():
    return development_db

app = FastAPI()

@app.post("/items")
def add_item(item: str, db = Depends(get_db_session)):
    db.append(item)
    print(db)
    return {"message": f"added item {item}"}

