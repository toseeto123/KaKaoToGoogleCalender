from pprint import pprint
from Google import Create_Service, convert_to_RFC_datetime

CLIENT_SECRET_FILE='credentials.json'
API_NAME='calendar'
API_VERSION='v3'
SCOPES=['https://www.googleapis.com/auth/calendar']

service=Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

# 캘린더 id는 구글캘린더 내부에서 직접적으로 확인도 가능함.
calendar_id='72ac6aa0bd79505df40eb6cda729f6796b37b0059b984174518c7c9fbc951204@group.calendar.google.com'

# create an event
colors = service.colors().get().execute()
pprint(colors)