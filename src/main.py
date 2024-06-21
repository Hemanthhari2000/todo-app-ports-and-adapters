if __name__ == "__main__":
    import uvicorn

    from entrypoints.api.main import app

    uvicorn.run("entrypoints.api.main:app", host="0.0.0.0", port=8000, reload=True)
