import jwt
import requests, time
#from . import config


def gbal(id):
  payload: dict = {
    "uid": id,
    "timeIssued": round(time.time() * 1000)
  }
  token = jwt.encode(payload, config["ecokey"])
  resp = requests.get("http://192.241.218.152:3000/getbal/" + token.decode("utf-8"))
  respcontent = resp.json()
  return respcontent["balance"]

def sbal(id, amount):
  time.sleep(0.4)
  payload = {
    "uid": id,
    "amount": amount,
    "timeIssued": int(round(time.time() * 1000))
  }
  token = jwt.encode(payload, config["ecokey"])
  resp = requests.get("http://192.241.218.152:3000/setbal/" + token.decode("utf-8"))
  print(resp)

def award(id, amount):
  sbal(id, (gbal(id) + amount))