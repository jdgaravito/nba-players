from uuid import uuid4 as uuid
from typing import Optional
import httpx

async def fetch_all_players() -> dict:
    '''This function fetches and return all the data from the url asyncrounously''' 
    url = "https://mach-eight.uc.r.appspot.com"
    async with httpx.AsyncClient() as client:
        resp: httpx.Response = await client.get(url)
        
        #Test if the Fetch operation was succesfully done
        assert resp.status_code == 200
        
    fetched_data = resp.json()
    data= fetched_data['values']
    return data

async def convert_type(data) ->dict:
   
    # Type conversion of dictionary values
    for dicts in data:
        for key in dicts:
            if key == 'h_in':
                dicts['h_in'] = int(dicts['h_in'])
            elif key == 'h_meters':
                dicts['h_meters'] = float(dicts['h_meters'])
    
    return data

async def generate_id(data) ->dict:
    for dicts in data:
        dicts['id'] = str(uuid())

    return data                

