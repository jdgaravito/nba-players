#python imports
from uuid import uuid4 as uuid
# FastAPI Imports
from fastapi import FastAPI, Depends
from fastapi import Body, Path, status
from fastapi.exceptions import HTTPException

#App Module imports
from app.services import nba_service
from app.models.player_model import Player

#Setting up the backend with fastAPI and their OpenAPI tags
app = FastAPI(
title="NBA Players Heights API",
description="This is a small API that search in a DB of players and look for their heights",
version="1.0",
openapi_tags=[{
    "name": "players",
    "description": "Player API Routes"
}]
)

#Setting our database
db = []



@app.on_event("startup")
async def startup():
    '''Initial setup of the backend app'''
    data = await nba_service.fetch_all_players()
    
    #str types conversion to int/float
    data = await nba_service.convert_type(data)
    
    #Id generation for each player
    data = await nba_service.generate_id(data)
    #populate the db
    db[:] = data
    


# Basic routes

@app.get("/", status_code=status.HTTP_200_OK, tags=["players"])
async def get_all_players():
    response = db
    return response


@app.post("/new-player", status_code=status.HTTP_201_CREATED, tags=["players"])
def create_a_player(player: Player = Body(...)):
    '''Function that gets a body and add it to player list'''
    player.id = str(uuid())
    db.append(player.dict())
    return db[-1]


@app.get("/{player_id}", status_code=status.HTTP_200_OK, tags=["players"])
def get_player(player_id: str):
    '''Function that looks for a player based on player ID'''
    for player in db:
        if player["id"] == player_id:
            return player
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@app.delete("/{player_id}", status_code=status.HTTP_200_OK, tags=["players"])
def delete_player(player_id: str):
    for index, player in enumerate(db):
        if player["id"] == player_id:
            db.pop(index)
            return {"message":"Player has been deleted successfully"}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@app.put("/{player_id}", status_code=status.HTTP_200_OK, tags=["players"])
def edit_player(player_id: str, player: Player = Body(...)):
    for index, player in enumerate(db):
        if player['id'] == player_id:
            db[index]["first_name"] = player.first_name
            db[index]["last_name"] = player.last_name
            db[index]["h_in"] = player.h_in
            db[index]["h_meters"] = player.h_meters
            return {"message": "Player has been updated successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)    


@app.get("/search-pair/{player_height}", status_code=status.HTTP_200_OK, tags=["players"])
def calc_pairs(player_height: int = Path(..., lt=200)):
    index_pairs = []
    map_pair = {} 
    
    for index, player in enumerate(db):
        if player_height - player['h_in'] in map_pair:
            # index2 = map_pair[player_height - player['h_in']]
            # index_pairs.append({index, index2})
           print(map_pair)
               
        if player['h_in'] in map_pair:
            map_pair[db[index]['h_in']] = index
            
        else:
            pass
        
        # if player['h_in'] in map_pair:
        #    map_pair[db[index]['h_in']] += 1
        # else:       
        #    map_pair[db[index]['h_in']] = 1



        
    return index_pairs


@app.get("/search-pair-n2/{player_height}", status_code=status.HTTP_200_OK, tags=["players"])
def calc_pairs(player_height: int = Path(..., lt=200)):   
    index_pairs = []
    for index, player in enumerate(db):
        for index2 in range(index + 1, len(db)):
                if db[index]['h_in'] + db[index2]['h_in'] <= player_height and db[index] != db[index2]:
                    index_pairs.append({index, index2})               
    return index_pairs

                    #print(db[index]['first_name'], " ", db[index]['last_name'], "  -  ", db[index2]['first_name'], " ", db[index2]['last_name'])
                   
                   
        
       
       


    