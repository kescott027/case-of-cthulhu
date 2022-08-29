#!/usr/bin/python3
import playsound
import playsounds

from fastapi import FastAPI
app = FastAPI()


@app.get("/thud")
def thud(count=None):
    if not count:
        playsounds.play_bang()
    else:
        playsounds.multi_bang(int(count))
    return {'200 OK'}


@app.get("/growl")
def growl():
    playsounds.growl()
    return {'200 OK'}


@app.get("/creepy")
def creepy():
    playsounds.creepy()
    return {'200 OK'}