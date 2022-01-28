from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

MONGO_URL = "mongodb+srv://violet:pro@cluster0.2gvyp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
mongo_client = MongoClient(MONGO_URL)
db = mongo_client.violet

usersdb = db.users

async def is_served_user(user_id: int) -> bool:
    user = await usersdb.find_one({"user_id": user_id})
    if not user:
        return False
    return True


async def get_served_users() -> list:
    users = usersdb.find({"user_id": {"$gt": 0}})
    if not users:
        return []
    users_list = []
    for user in await users.to_list(length=1000000000):
        users_list.append(user)
    return users_list


async def add_served_user(user_id: int):
    is_served = await is_served_user(user_id)
    if is_served:
        return
    return await usersdb.insert_one({"user_id": user_id})