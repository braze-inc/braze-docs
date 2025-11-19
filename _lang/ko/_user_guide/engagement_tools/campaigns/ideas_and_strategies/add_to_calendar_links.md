---
nav_title: 캘린더에 추가 링크
article_title: 캘린더에 추가 링크
page_order: 1
page_type: tutorial
description: "이 문서에서는 이메일 캠페인에 캘린더에 추가 링크를 포함하는 방법에 대해 설명합니다."
channel: email

---

# 캘린더에 추가 링크

> 이벤트, 세일 또는 약속을 홍보할 때 이메일에 '캘린더에 추가' 링크를 추가하여 사용자가 이벤트를 캘린더에 쉽게 저장할 수 있도록 도울 수 있습니다.

이렇게 하려면 이메일 초안을 작성하고 링크를 넣을 위치를 결정합니다. 그런 다음 두 가지 옵션을 추가합니다. 하나는 Google 캘린더용, 다른 캘린더(예: iCal 또는 Outlook)용입니다. 예를 들어, 'Google 캘린더에 추가' 및 'iCal 또는 Outlook에 추가'를 클릭합니다.

대시보드에 링크를 추가할 때 링크 대화상자. '링크 정보' 탭이 선택되고 텍스트가 'Google 캘린더에 추가'로 설정됩니다.]({% image_buster /assets/img_archive/calendar_1.png %}){: style="max-width:50%"}

## URL 형식

입력 안내를 대체하여 링크에 다음 URL을 추가합니다. 이 두 URL의 유일한 차이점은 Google 캘린더에 추가 매개변수가 필요하다는 것입니다: `&format=gcal`.

{% tabs %}
{% tab Google Calendar %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION&format=gcal
```

{% endtab %}
{% tab iCal or Outlook %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION
```

{% endtab %}
{% endtabs %}

다음을 교체합니다:

- `EVENT_SUBJECT`: 이벤트 제목
- `EVENT_LOCATION`: 이벤트 위치
- `START_TIME`: 이벤트의 시작 시간은 ISO 8601 형식(YYYY-MM-DDTHH:MM:SSZ)으로 UTC로 표시합니다.
- `END_TIME`: 이벤트 종료 시간은 ISO 8601 형식(YYYY-MM-DDTHH:MM:SSZ)의 UTC로 표시됩니다.
- `EVENT_DESCRIPTION`: 이벤트 설명

모든 공백을 HTML 이스케이프 코드 `%20` 로 바꿉니다. 예를 들어 "Meet Braze"의 제목은 "Meet%20Braze"가 됩니다.

다음은 'Google 캘린더에 추가' URL의 예입니다:

```
https://ics.agical.io/?subject=Meet%20Braze&location=114%20Sansome%20Street&dtstart=2021-06-24T15:00:00Z&dtend=2021-06-24T16:00:00Z&description=Braze%20Party&format=gcal
```

### 추가 매개 변수

다음 매개변수는 선택 사항이며 이벤트의 추가 측면을 정의하는 데 사용할 수 있습니다.

- **주최자 이름:** `&organizer=name`
- **이벤트와 관련된 URL을 첨부합니다:** `&attach=http://www.example.com/`
- **기간:** `duration=30M` 이벤트 종료 시간(dtend)의 대안으로 1H 또는 30M과 같은 기간을 지정합니다.
- **알림 알람 시간, 분 단위:** `&reminder=15`
- **종일 이벤트:** `&allday=1`
- **UID:** 이벤트의 고유 식별자를 하드코딩하여 일부 캘린더 앱이 시간이 지남에 따라 이벤트를 업데이트할 수 있도록 하는 선택적 매개변수입니다. ics.agical.io 문자열이 값에 자동으로 추가됩니다.

반복 이벤트에 대한 추가 매개변수를 추가할 수도 있습니다:
- **주간 이벤트:** `&recur=weekly`
- **월간 이벤트:** `&recur=monthly`
- **반복 종료:** `&recuruntil=END_DATE` 여기서 `END_DATE` 은 반복이 끝나는 날짜와 시간(ISO 8601 형식(YYYY-MM-DDTHH:MM:SSZ)을 UTC로 표시합니다.

## 링크 동작

사용자가 링크를 클릭하면 캘린더는 URL의 UTC 타임스탬프를 자동으로 변환하여 캘린더에 설정된 사용자의 표준 시간대를 반영합니다.

예를 들어 'Google 캘린더에 추가' 예제 링크를 열고 캘린더가 CST로 설정되어 있는 경우, 이벤트의 시간은 UTC 기준 오후 3시(오전 10시)에 맞춰 미리 채워집니다.

### 구글 캘린더

클릭하면 초대장에 미리 입력되어 있고 사용자가 저장할 수 있는 이벤트 세부 정보가 있는 새 탭 또는 창에서 Google 캘린더가 열립니다. 이는 모바일과 데스크톱 모두에서 발생합니다.

이벤트 세부 정보가 추가되고 저장할 준비가 된 이벤트를 추가하려면 Google 캘린더 대화 상자를 클릭합니다.]({% image_buster /assets/img_archive/calendar_2.png %}){: style="max-width:75%"}

### iCal 또는 Outlook

데스크톱에서 클릭하면 ICS 파일이 다운로드됩니다. 그런 다음 사용자가 ICS 파일을 열면 iCal 또는 Outlook이 열리고 사용자에게 캘린더에 이벤트를 추가하라는 메시지가 표시됩니다.

새 이벤트를 추가할 수 있는 대화 상자가 있는 iCal 캘린더에서 사용자에게 캘린더를 선택하고 확인하라는 메시지를 표시합니다.]({% image_buster /assets/img_archive/calendar_3.png %}){: style="max-width:75%"}

이벤트가 추가된 iCal 캘린더.]({% image_buster /assets/img_archive/calendar_4.png %}){: style="max-width:81%"}

모바일에서는 사용자가 링크를 길게 누르면 캘린더에 추가할지 묻는 메시지가 표시됩니다.

iOS에서는 캘린더 링크를 길게 누르면 '캘린더에 추가' 버튼이 포함된 팝업이 나타납니다.]({% image_buster /assets/img_archive/calendar_5.png %}){: style="max-width:50%"}

자세한 내용은 다음을 참조하세요:
* [Google 캘린더용 이벤트 만들기](https://developers.google.com/calendar/api/guides/create-events)
* [이메일 메시징에 캘린더에 추가 링크 만들기](https://support.microsoft.com/en-us/office/create-an-add-to-calendar-link-in-an-email-message-34f8ea28-322a-4867-b423-2998f9634e59)


