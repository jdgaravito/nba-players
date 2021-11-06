# FastAPI Imports
from fastapi import FastAPI, Depends
from fastapi import Body, Path

#App Module imports
from app.services import nba_service
from app.models.player_model import Player

app = FastAPI()

#Our database
db = []



@app.on_event("startup")
async def startup():
    '''Initial setup of the backend.'''
    data = await nba_service.fetch_all_players()
    db[:] = data
    
    



@app.get("/")
async def get_all_players():
    response = db
    return response



@app.post("/new-player")
def create_a_player(player: Player = Body(...)):
    print(player.dict())
    return player
