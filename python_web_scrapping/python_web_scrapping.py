from Google import Create_Service
import pandas as pd

CLIENT_SECRET_FILE = "client_secret_GoogleCloudDemo.json"
API_NAME = "youtube"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/youtube"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
