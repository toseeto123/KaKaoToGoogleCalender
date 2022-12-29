# eventId : 일정을 조회한 후 얻은 id 값을 말합니다.
# 먼저 수정할 일정을 가져옵니다.
# 방법 1 : get 함수를 통해서 가져오기
# eventId = 'fraof7dh0g0ene8kdcfl3hg4p4_20200213T000000Z'
# event = service.events().get(calendarId='primary', eventId=eventId).execute()
# 방법 2 : list 함수에서 반환된 일정 사용하기
event = events_result.get('items')[0]
event_id = event.get('id')

# 원하는 일정의 속성 값을 변경합니다.
event['summary'] = "(수정된)" + event['summary']

# 일정 수정 요청하기
updated_event = service.events().update(calendarId='primary', eventId=event_id, body=event).execute()

updated_event
# 제목이 "(수정된)itsplay의 OpenAPI 수업"로 바뀌었습니다.