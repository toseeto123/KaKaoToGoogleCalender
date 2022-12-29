from google_auth_oauthlib.flow import InstalledAppFlow

# 구글 클라우드 콘솔에서 다운받은 OAuth 2.0 클라이언트 파일경로
creds_filename = 'credentials.json'

# 사용 권한 지정
# https://www.googleapis.com/auth/calendar	               캘린더 읽기/쓰기 권한
# https://www.googleapis.com/auth/calendar.readonly	       캘린더 읽기 권한
SCOPES = ['https://www.googleapis.com/auth/calendar']

# 파일에 담긴 인증 정보로 구글 서버에 인증하기
# 새 창이 열리면서 구글 로그인 및 정보 제공 동의 후 최종 인증이 완료됩니다.
flow = InstalledAppFlow.from_client_secrets_file(creds_filename, SCOPES)
creds = flow.run_local_server(port=0)

import datetime

# 구글 캘린더 API 서비스 객체 생성

from googleapiclient.discovery import build

today = datetime.date.today().isoformat()
service = build('calendar', 'v3', credentials=creds)


event = {
        'summary': 'namsu의 캘린더 api 실습2', # 일정 제목
        'location': '서울특별시 종로구 하이미디어', # 일정 장소
        'description': 'itsplay와 OpenAPI 실행중.', # 일정 설명
        'start': { # 시작 날짜
            'dateTime': '2022-12-27T12:00:00', 
            'timeZone': 'Asia/Seoul',
        },
        'end': { # 종료 날짜
            'dateTime': '2022-12-27T15:00:00', 
            'timeZone': 'Asia/Seoul',
        },
    }

# calendarId : 캘린더 ID. primary이 기본 값입니다.
event = service.events().insert(calendarId='primary', body=event).execute()
print('Event created: %s' % (event.get('htmlLink')))