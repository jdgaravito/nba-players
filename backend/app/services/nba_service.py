from typing import Optional
import httpx

async def fetch_all_players() -> dict:
    '''This function fetches and return all the data from the url asyncrounously''' 
    url = "https://mach-eight.uc.r.appspot.com"
    async with httpx.AsyncClient() as client:
        resp: httpx.Response = await client.get(url)
        
        #Test if the Fetch operation was succesfully done
        assert resp.status_code == 200
        
        
    data = resp.json()
    return data['values']