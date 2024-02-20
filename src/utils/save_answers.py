import asyncio


async def save_answers(answers, user_id) -> None:
  with open("../db/" + "user_" + str(user_id) + ".txt", "w") as fp:
    for answer in answers:
      fp.write(answer[0] + " -> " + answer[1] + "\n")
    fp.close()
  mutex = 1