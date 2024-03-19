import asyncio


async def SaveAnswers(answers, user_id):
  s = ''
  with open("/home/yusuf/Desktop/medbot/db/" + "user_" + str(user_id) + ".txt", "w") as fp:
    for answer in answers:
      fp.write(answer[0] + " -> " + answer[1] + "\n")
      s += answer[0] + " -> " + answer[1] + "\n"
    fp.close()
  mutex = 1
  return s