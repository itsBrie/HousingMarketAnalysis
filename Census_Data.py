import requests;
import pandas as pd;
import os;

api_key="xxx"
base_url="https://api.census.gov/data/{year}/acs/acs5?"
param=("get=NAME,B01001_001E,B01001_002E,B01001_026E,B02001_002E,B02001_003E,"
       "B02001_004E,B02001_005E,B02001_006E,B02001_007E,B02001_008E,B19013_001E"
       "&for=place:*&in=state:48"
       "&key={api_key}")

start_year=2019
end_year=2023