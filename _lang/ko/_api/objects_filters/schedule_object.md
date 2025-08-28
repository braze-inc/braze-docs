---
nav_title: "스케줄 객체"
article_title: API 스케줄 객체
page_order: 12
page_type: reference
description: "이 참조 문서에서는 Braze에서 사용되는 다양한 스케줄링 객체를 나열하고 설명합니다."

---

# 스케줄 객체

> 캠페인 및 캔버스 일정 생성 엔드포인트의 매개변수는 전송 엔드포인트의 매개변수를 반영하고 `schedule` 매개변수를 추가하여 타겟 사용자가 메시지를 수신할 시기를 지정할 수 있습니다. `schedule` 객체에 `time` 매개변수만 포함하면 모든 사용자에게 해당 시간에 메시지가 전송됩니다.

`in_local_time`을 `true`로 설정하면 모든 시간대에서 시간 매개변수가 지나간 경우 오류 응답이 표시됩니다. `at_optimal_time` 을 true로 설정하면 사용자가 제공한 시간과 관계없이 지정된 날짜에 최적의 시간에 메시지를 받게 됩니다. 현지 시간 또는 최적 시간 전송을 사용하는 경우 시간 매개변수 값에 시간대 지정자를 제공하지 마세요(예: `"2015-02-20T13:14:47-05:00"` 대신 `"2015-02-20T13:14:47"` 사용).

응답에는 나중에 예약한 메시지를 취소하거나 업데이트해야 할 경우를 대비하여 저장해야 하는 `schedule_id`가 제공됩니다.

## 개체 본문

필요에 따라 이 개체를 삽입하여 메시지를 예약하세요.

```json
"schedule": {
  "time": (required, datetime as ISO 8601 string) time to send the message in UTC,
  "in_local_time": (optional, bool),
  "at_optimal_time": (optional, bool),
}
```

## ID 응답 예약

작성한 예약 메시지에 대한 `schedule_id`가 전송됩니다.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "schedule_id" : (required, string) identifier for the scheduled message that was created
}
```

서버 간 호출에 API를 사용하는 경우 방화벽 뒤에 있는 경우 적절한 API URL을 허용 목록에 추가해야 할 수 있습니다.

메시지 예약 엔드포인트 응답에는 메시지 발송을 다시 참조할 수 있도록 메시지의 `dispatch_id` 링크가 포함됩니다. `dispatch_id` 은 메시지 발송의 ID(Braze에서 보낸 각 '전송'에 대한 고유 ID)입니다.

