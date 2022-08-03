from typing import Optional

from pydantic import BaseModel, EmailStr, Field

class ApplicantSchema(BaseModel):
	fullname: str = Field(...)
	email: EmailStr = Field(...)
	degree_of_study: str = Field(...)
	year: int = Field(..., gt=0, lt=9)
	gpa: float = Field(..., le=4.0)

	class Config:
		schema_extra = {
			"example": {
				"fullname": "John Doe",
				"email": "jdoe@wit.edu",
				"degree_of_study": "Computer Science",
				"year": 5,
				"gpa": "3.5",
			}
	}

class UpdateApplicantModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    degree_of_studey: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@wit.edu",
                "course_of_study": "Computer Science and Applied Mathemeatics",
                "year": 5,
                "gpa": "3.8",
            }
        }

def ResponseModel(data, message):
	return {
		"data": [data],
		"code": 200,
		"message": message,
	}


def ErrorResponseModel(error, code, message):
	return {"error": error, "code": code, "message": message}
