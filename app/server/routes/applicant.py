from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    	add_applicant,
    	delete_applicant,
    	retrieve_applicant,
    	retrieve_applicants,
    	update_applicant,
)
from app.server.models.applicant import (
    	ErrorResponseModel,
    	ResponseModel,
    	ApplicantSchema,
	UpdateApplicantModel,
)

router = APIRouter()

@router.post("/", response_description="Applicant data added to database")
async def add_applicant_data(applicant: ApplicantSchema = Body(...)):
	applicant = jsonable_encoder(applicant)
	new_applicant = await add_applicant(applicant)
	return ResponseModel(new_applicant, "Applicant added successfully.")

@router.post("/", response_description="Applicants retrieved")
async def get_applicants():
	applicant = await retrieve_applicants()
	if applicants:
		return ResponseModel(applicants, "Applicants data retrieved successfully")
	return ResponseModel(applicants, "Empty")

@router.get("/{id}", response_description="Applicant data retrieved")
async def get_applicant_data(id):
	applicant = await retrieve_applicant(id)
	if applicant:
		return ResponseModel(applicant, "Applicant data retrieved successfully")
	return ErrorResponseModel("Error!", 404, "Applicant not found.")

@router.put("/{id}")
async def update_applicant_data(id: str, req: UpdateApplicantModel = Body(...)):
    	req = {k: v for k, v in req.dict().items() if v is not None}
    	updated_applicant = await update_applicant(id, req)
    	if updated_applicant:
        	return ResponseModel(
            		"Applicant with ID: {} name update is successful".format(id),
            		"Applicant name updated successfully",
        	)
    	return ErrorResponseModel(
        	"An error occurred",
        	404,
        	"There was an error updating the applicant data.",
    	)
@router.delete("/{id}", response_description="Applicant data deleted from the database")
async def delete_applicant_data(id: str):
    	deleted_applicant = await delete_applicant(id)
    	if deleted_applicant:
        	return ResponseModel(
            		"Applicant with ID: {} removed".format(id), "Applicant deleted successfully"
        	)
    	return ErrorResponseModel(
        	"An error occurred", 404, "Applicant with id {0} doesn't exist".format(id)
    	)


