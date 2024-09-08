import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"


TOKEN = "vjsdnvsjnieicevnjnvja"
USER_NAME ="makena"
GRAPH_ID = "zi"


user_params = {
    "token" : TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService" : "yes",
    "notMinor": "yes",

}
# response=  requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
graphs_params ={
    "id" : GRAPH_ID,
    "name": "cycling Graph",
    "unit" :"Km",
    "type" : "float",
    "color": "momiji"
}
header ={
    "X-USER-TOKEN" : TOKEN
}

# response= requests.post(url=graph_endpoint,json=graphs_params, headers=header)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now()
print(today)
pixel_request_params = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "How many kilometers did you cycle today? ",

}
response = requests.post(url=pixel_creation_endpoint,json=pixel_request_params,headers=header)
print(response.text)
