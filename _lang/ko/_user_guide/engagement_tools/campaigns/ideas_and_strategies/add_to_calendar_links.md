---
nav_title: 캘린더에 추가 링크
article_title: 캘린더에 추가 링크
page_order: 1
page_type: tutorial
description: "이 기사는 이메일 캠페인에 캘린더 추가 링크를 포함하는 방법을 설명합니다."
channel: email

---

# 캘린더에 추가 링크

> 이벤트, 세일 또는 약속을 홍보할 때 이메일에 "캘린더에 추가" 링크를 추가하여 사용자가 이벤트를 쉽게 캘린더에 저장할 수 있도록 도울 수 있습니다.

그렇게 하려면 이메일을 작성하고 링크를 삽입할 위치를 결정하세요. 그런 다음 Google 캘린더용 옵션 하나와 다른 캘린더(iCal 또는 Outlook과 같은)용 옵션 하나를 추가합니다. 예를 들어, "Google 캘린더에 추가" 및 "iCal 또는 Outlook에 추가".

![대시보드에서 링크를 추가할 때 링크 대화 상자. The "Link Info" tab is selected and the text is set to "Add to Google Calendar".]({% image_buster /assets/img_archive/calendar_1.png %}){: style="max-width:50%"}

## URL 형식

다음 URL을 링크에 추가하고 자리 표시자를 교체하세요. 이 두 URL의 유일한 차이점은 Google 캘린더에 `&format=gcal` 추가 매개변수가 필요하다는 것입니다.

{% tabs %}
{% tab Google 캘린더 %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION&format=gcal
```

{% endtab %}
{% tab iCal 또는 Outlook %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION
```

{% endtab %}
{% endtabs %}

다음을 교체하십시오:

- `EVENT_SUBJECT`: 행사의 제목
- `EVENT_LOCATION`: 행사의 위치
- `START_TIME`: 이벤트의 시작 시간은 ISO 8601 형식(YYYY-MM-DDTHH:MM:SSZ)으로 UTC입니다
- `END_TIME`: 이벤트 종료 시간의 ISO 8601 형식(YYYY-MM-DDTHH:MM:SSZ), UTC 기준
- `EVENT_DESCRIPTION`: 이벤트 설명

공백을 `%20` HTML 이스케이프 코드로 바꾸세요. 예를 들어, "Meet Braze"라는 제목은 "Meet%20Braze"가 됩니다.

다음은 "Google 캘린더에 추가" URL의 예입니다:

```
https://ics.agical.io/?subject=Meet%20Braze&location=114%20Sansome%20Street&dtstart=2021-06-24T15:00:00Z&dtend=2021-06-24T16:00:00Z&description=Braze%20Party&format=gcal
```

### 추가 매개변수

다음 매개변수는 선택 사항이며 이벤트의 추가 측면을 정의하는 데 사용할 수 있습니다.

- **주최자 이름:** `&organizer=name`
- **이벤트와 관련된 URL 첨부:** `&attach=http://www.example.com/`
- **기간:** `duration=30M`, 이벤트 종료 시간 (dtend)의 대안으로 1H 또는 30M과 같은 기간을 지정합니다.
- **알람 시간, 분 단위:** `&reminder=15`
- **하루 종일 이벤트:** `&allday=1`
- **UID:** 선택적 매개변수로 이벤트의 고유 식별자를 하드코딩하여 일부 캘린더 앱이 시간이 지남에 따라 이벤트를 업데이트할 수 있도록 합니다. 문자열 @ics.agical.io 은(는) 값에 자동으로 추가됩니다.

다음과 같은 반복 이벤트에 대한 추가 매개변수를 추가할 수 있습니다:
- **주간 이벤트:** `&recur=weekly`
- **월간 이벤트:** `&recur=monthly`
- **반복 종료:** `&recuruntil=END_DATE`, 여기서 `END_DATE`는 반복이 종료되는 날짜와 시간을 UTC 기준 ISO 8601 형식(YYYY-MM-DDTHH:MM:SSZ)으로 나타낸 것입니다.

## 링크 동작

사용자가 링크를 클릭하면 캘린더는 URL의 UTC 타임스탬프를 사용자의 캘린더에 설정된 시간대로 자동 변환합니다.

예를 들어, "Google 캘린더에 추가" 링크를 열고 캘린더가 CST로 설정된 경우, 이벤트 시간은 UTC 3시가 CST(오전 10시)에서 무엇인지에 따라 미리 채워집니다.

### 구글 캘린더

클릭하면 Google 캘린더가 새 탭 또는 창에서 열리며, 초대장에 이벤트 세부 정보가 미리 채워져 있고 사용자가 저장할 준비가 됩니다. 이것은 모바일과 데스크탑 모두에서 발생합니다.

![Google Calendar dialog to add an event with the event's details added and ready to save.]({% image_buster /assets/img_archive/calendar_2.png %}){: style="max-width:75%"}

### iCal 또는 Outlook

데스크탑에서 클릭하면 ICS 파일이 다운로드됩니다. 사용자는 ICS 파일을 열어 iCal 또는 Outlook을 열고 사용자가 이벤트를 캘린더에 추가하도록 요청해야 합니다.

![iCal calendar with a dialog for adding a new event, which prompts the user to select a calendar and confirm.]({% image_buster /assets/img_archive/calendar_3.png %}){: style="max-width:75%"}

![iCal calendar with the event added.]({% image_buster /assets/img_archive/calendar_4.png %}){: style="max-width:81%"}

모바일에서 사용자는 링크를 길게 눌러 캘린더에 추가하라는 메시지가 표시됩니다.

![iOS pop-up when you press and hold on a calendar link, which includes a button to "Add to Calendar".]({% image_buster /assets/img_archive/calendar_5.png %}){: style="max-width:50%"}

자세한 내용은 다음을 참조하십시오:
* [Google 캘린더에 이벤트 만들기](https://developers.google.com/calendar/api/guides/create-events)
* [이메일 메시지에 캘린더 추가 링크 만들기](https://support.microsoft.com/en-us/office/create-an-add-to-calendar-link-in-an-email-message-34f8ea28-322a-4867-b423-2998f9634e59)


