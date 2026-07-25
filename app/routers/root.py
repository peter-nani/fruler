from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def home():
    return {
        "application": "Campus Management System",
        "version": "1.0.0",
        "status": "running",
    }


@router.get("/health")
def health():
    return {
        "status": "healthy",
    }