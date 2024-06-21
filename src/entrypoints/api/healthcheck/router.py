from fastapi import APIRouter, status

router = APIRouter()


@router.get("")
def health_check():
    return {"status": status.HTTP_200_OK, "message": "Healthy"}
