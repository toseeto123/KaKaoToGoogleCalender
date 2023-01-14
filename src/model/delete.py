from pprint import pprint
from Google import Create_Service, convert_to_RFC_datetime

CLIENT_SECRET_FILE= '../../credentials.json'
API_NAME='calendar'
API_VERSION='v3'
SCOPES=['https://www.googleapis.com/auth/calendar']

service=Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

#insert 구간
#필요없는 조정 adjustment일수있음. 왜냐면 시간조정용 이니깐..
calendar_id='8d762569ee30e088994ea3a39d894a289a99bdb4792c960ff6b9c220cfeb5dbe@group.calendar.google.com'

### event 가 등록되어있는 id 값 list 에서 id:값에 표시되어있는거 가져오면됨
eventId='glca3eo7762nj6n6fre428p27k'

# ##delete 구간
service.events().delete(calendarId=calendar_id,eventId=eventId).execute()
