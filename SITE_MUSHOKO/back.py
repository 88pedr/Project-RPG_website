from SITE_MUSHOKO import fastapi as fp

test = fp.FastAPI()

@test.get("/")
def caralho():
    return {"message": "caralho"}