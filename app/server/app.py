from fastapi import FastAPI

from app.server.routes.applicant import router as ApplicantRouter

app = FastAPI()

app.include_router(ApplicantRouter, tags=["Applicant"], prefix="/applicant")

@app.get("/", tags=["Root"])
async def read_root():
	return {"message": "Welcome!"}
