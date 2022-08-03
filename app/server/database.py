import motor.motor_asyncio

from decouple import config

from bson.objectid import ObjectId

conn_str = config("MONGO_DB")

client = motor.motor_asyncio.AsyncIOMotorClient(conn_str)
database = client.applicants

applicant_collection = database.get_collection("applicant_collection")

def applicant_helper(applicant) -> dict:
	return {
		"id": str(applicant["_id"]),
		"fullname": applicant["fullname"],
		"email": applicant["email"],
		"degree_of_study": applicant["degree_of_study"],
		"year": applicant["year"],
		"GPA": applicant["gpa"],
	}


# Retrieve all applicants in the database
async def retrieve_applicants():
    applicants = []
    async for applicant in applicant_collection.find():
        applicants.append(applicant_helper(student))
    return applicants


# Add a new applicant into to the database
async def add_applicant(applicant_data: dict) -> dict:
    applicant = await applicant_collection.insert_one(applicant_data)
    new_applicant = await applicant_collection.find_one({"_id": applicant.inserted_id})
    return applicant_helper(new_applicant)


# Retrieve an applicant with a matching ID
async def retrieve_applicant(id: str) -> dict:
    applicant = await applicant_collection.find_one({"_id": ObjectId(id)})
    if applicant:
        return applicant_helper(applicant)


# Update an applicant with a matching ID
async def update_applicant(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    applicant = await applicant_collection.find_one({"_id": ObjectId(id)})
    if applicant:
        updated_applicant = await applicant_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_applicant:
            return True
        return False


# Delete an applicant from the database
async def delete_applicant(id: str):
    applicant = await applicant_collection.find_one({"_id": ObjectId(id)})
    if applicant:
        await applicant_collection.delete_one({"_id": ObjectId(id)})
        return True

