## JournalEntryMS
Journal Entry Prompt Generator Microservice. 
Written in Python 3.10.
Uses [FastAPI](https://fastapi.tiangolo.com/tutorial/) and [Hypercorn]() to generate GET API for randomized entry prompts. 

Deployed on [Railway](https://docs.railway.app/): https://journalpromptms-production.up.railway.app/ 
- More information on the API [here](https://journalpromptms-production.up.railway.app/docs)
  
### ✨ How to use ✨

- Save locally and make changes in 'main.py'. Commit and Push back into a GitHub repository and deploy on Railway.
- In Railway, you will need to generate a URL for the API to appear in.

To send request: 
- Send GET request to https://journalpromptms-production.up.railway.app/
- Receive JSON response


UML:
![UML](https://onedrive.live.com/embed?resid=57F9C83EDD214436%2133793&authkey=%21ACzr7GotibNeGvc&width=1100&height=618)
