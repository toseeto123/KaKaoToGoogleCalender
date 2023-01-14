from pprint import pprint
from Google import Create_Service, convert_to_RFC_datetime
import datetime

CLIENT_SECRET_FILE= '../../credentials.json'
API_NAME='calendar'
API_VERSION='v3'
SCOPES=['https://www.googleapis.com/auth/calendar']

service=Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

# 캘린더 id는 구글캘린더 내부에서 직접적으로 확인도 가능함.

calendar_id='8d762569ee30e088994ea3a39d894a289a99bdb4792c960ff6b9c220cfeb5dbe@group.calendar.google.com'
today = datetime.date.today().isoformat()
time_min = today + 'T00:00:00+09:00'
time_max = today + 'T23:59:59+09:00'
max_results = 5
is_single_events = True
orderby = 'startTime'

events_result = service.events().list(
        calendarId=calendar_id,
        timeMin=time_min,
        timeMax=time_max,
        maxResults=250,
        singleEvents=is_single_events,
        orderBy=orderby,
).execute()

pprint(events_result)

