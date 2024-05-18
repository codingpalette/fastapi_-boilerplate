from fastapi import FastAPI
from typing import Optional
from routes import v1
from db.database import Base, engine
import uvicorn

description = """
<div>
    -------------------------------<br>
    <a href="/docs">[ 기본api ]</a><br>
    <a href="/api/v1/docs">[ v1_api ]</a><br>
    -------------------------------
</div>
"""

def create_app():
    Base.metadata.create_all(bind=engine)
    app = FastAPI(title="기본 api", description=description, docs_url="/docs", redoc_url=None, swagger_ui_parameters={"defaultModelsExpandDepth": -1})
    v1_app = FastAPI(title="v1 api", description=description, docs_url="/docs", redoc_url=None, swagger_ui_parameters={"defaultModelsExpandDepth": -1})

    @app.get("/")
    def read_root():
        return {"Hello": "World"}

    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Optional[str] = None):
        return {"item_id": item_id, "q": q}

    # v1 api
    v1_app.include_router(v1.router)
    app.mount("/api/v1", v1_app)

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True, workers=4)
