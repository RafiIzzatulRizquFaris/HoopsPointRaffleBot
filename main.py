import json

import pandas as pd
from requests import Session


def login_func(email, password, id_card):
    with Session() as s:
        login_data = {"username": email, "password": password, "grant_type": "password"}
        response = s.post("https://www.hoopspoint.com/token", login_data)
        json_login = json.loads(str(response.content))
        token = json_login['access_token']
        user_id = json.loads(str(json_login['user']))['Id']
        submit_data = {
            "IdProductOption": 21628,
            "IdRaffle": 76,
            "IdUser": user_id,
            "Identification": id_card,
            "Options": "<div>Size: 8</div>",
        }
        s.post("https://www.hoopspoint.com/api/raffle", submit_data, headers={"authorization": "Bearer " + token})


df = pd.read_excel(r'/Users/rafiizzatulrizqufaris/Downloads/testeratmos.xls', sheet_name='Sheet3')

for x in df.values:
    login_func(x[3], "Hendrajwr121718", x[1])
