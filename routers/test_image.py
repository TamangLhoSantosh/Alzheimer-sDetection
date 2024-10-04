from fastapi import APIRouter, Depends, status, File, UploadFile
from sqlalchemy.orm import Session
from repository import test_image
import schemas, database, oauth2


router = APIRouter(
    prefix="/hospital/{hospital_id}/patient/{patient_id}/test_image",
    tags=["Test Images"],
)
get_db = database.get_db


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
async def upload_test_image(
    hospital_id: int,
    patient_id: int,
    image: UploadFile,
    db: Session = Depends(get_db),
    current_user: schemas.UserShow = Depends(oauth2.get_current_user),
):
    return await test_image.create(db, image, patient_id)


@router.get("/", response_model=list[schemas.TestImage])
def show_test_images(
    hospital_id: int,
    patient_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.UserShow = Depends(oauth2.get_current_user),
):
    return test_image.get_test_images(db, patient_id)


@router.get("/{id}", response_model=schemas.TestImage)
def show_test_image(
    hospital_id: int,
    patient_id: int,
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.UserShow = Depends(oauth2.get_current_user),
):
    return test_image.show(db, id)
