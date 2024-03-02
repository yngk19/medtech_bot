import asyncio


async def GetDoctor() -> list:
  with open("/app/db/doctors.txt", "r") as fp:
    doctors = fp.readlines()
    fp.close()
    return doctors
  mutex = 1