---
nav_title: 통합
article_title: Roku용 인앱 메시지 통합 가이드
platform: Roku
page_order: 2
description: "이 참조 가이드에서는 Roku용 인앱 메시지를 통합하는 방법과 관련 코드 고려사항을 다룹니다."
channel:
  - in-app messages
---

# 인앱 메시지 통합

> 이 구현 가이드에서는 인앱 메시지 코드 고려사항과 함께 제공되는 코드 스니펫을 다룹니다. 샘플 통합 코드를 제공하지만, 원하는 UI 내에서 트리거된 메시지를 처리하고 표시하는 로직을 추가해야 합니다. 

코드는 앱에 고유한 것이므로 사용 사례와 관련이 없는 경우 나열된 모든 상황을 처리할 필요는 없습니다. 예를 들어 인앱 메시지 지연 표시를 사용하지 않는다면 해당 로직과 엣지 케이스를 구현할 필요가 없습니다.

## SDK 요구 사항 {#supported-sdk-versions}

인앱 메시지는 지원되는 최소 SDK 버전을 실행하는 Roku 기기로만 전송됩니다.

{% sdk_min_versions roku:0.1.2 %}

## 인앱 메시지 설정

인앱 메시지를 처리하려면 `BrazeTask.BrazeInAppMessage` 에서 옵저버를 추가할 수 있습니다:

```brightscript
m.BrazeTask.observeField("BrazeInAppMessage", "onInAppMessageReceived")
```

그런 다음, 핸들러 내에서 캠페인이 트리거하는 최상위 인앱 메시지에 액세스할 수 있습니다.

```brightscript
sub onInAppMessageReceived()
  in_app_message = m.BrazeTask.BrazeInAppMessage
  ...
end sub
```

## 인앱 메시지 필드

다음은 인앱 메시지를 처리하는 데 필요한 필드 목록입니다:

| 필드 | 설명 |
| ------ | ----------- |
| `buttons` | 버튼 목록(빈 목록일 수 있음). |
| `click_action` | `"URI"` 또는 `"NONE"`. 이 필드를 사용하여 인앱 메시지를 클릭할 때 URI 링크로 열 것인지 아니면 메시지를 닫을 것인지 표시합니다. 버튼이 없는 경우, 인앱 메시지가 표시될 때 사용자가 '확인'을 클릭하면 이 작업이 수행됩니다. |
| `dismiss_type` | `"AUTO_DISMISS"` 또는 `"SWIPE"`. 이 필드를 사용하여 인앱 메시지를 자동으로 해제할지 아니면 밀어서 해제할지 표합니다. |
| `display_delay` | 인앱 메시지를 표시할 때까지 기다리는 시간(초). |
| `duration` | `dismiss_type`이 `"AUTO_DISMISS"`로 설정된 경우 메시지가 표시되는 기간(밀리초). |
| `extras` | 키-값 쌍. |
| `header` | 헤더 텍스트입니다. |
| `id` | 노출 횟수 또는 클릭을 기록하는 데 사용되는 ID. |
| `image_url` | 인앱 메시지 이미지 URL. |
| `message` | 메시지 본문 텍스트. |
| `uri` | URI 사용자는 `click_action`에 따라 전송됩니다. 이 필드는 `click_action` 가 `"URI"` 일 때 반드시 포함되어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
버튼이 포함된 인앱 메시지의 경우 버튼 텍스트를 추가하기 전에 클릭 동작이 추가되면 `click_action` 메시지도 최종 페이로드에 포함됩니다.
{% endalert %}

### 스타일링 필드
대시보드에서 사용할 수 있는 다양한 스타일 필드도 있습니다.

| 필드 | 설명 |
| ------ | ----------- |
| `bg_color` | 배경색. |
| `close_button_color` | 닫기 버튼 색상. |
| `frame_color` | 배경 화면 오버레이의 색상입니다. |
| `header_text_color` | 헤더 텍스트 색상. |
| `message_text_color` | 메시지 텍스트 색상. |
| `text_align` | 'START', 'CENTER' 또는 'END'. 선택한 텍스트 정렬. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

또는 인앱 메시지를 구현하고 표준 팔레트를 사용하여 Roku 애플리케이션 내에서 스타일을 지정할 수 있습니다:

### 버튼 필드

| 필드 | 설명 |
| ------ | ----------- |
| `click_action` | `"URI"` 또는 `"NONE"`. 이 필드를 사용하여 인앱 메시지를 클릭할 때 URI 링크로 열 것인지 아니면 메시지를 닫을 것인지 표시합니다. |
| `id` | 버튼 자체의 ID 값입니다. |
| `text` | 버튼에 표시할 텍스트입니다. |
| `uri` | URI 사용자는 `click_action`에 따라 전송됩니다. 이 필드는 `click_action` 가 `"URI"` 일 때 반드시 포함되어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 상호 작용 처리하기

캠페인의 분석을 처리하기 위해 특정 함수가 호출되는지 확인해야 합니다.

##### 메시지가 표시되는 경우

메시지가 표시되거나 확인되면 노출 횟수를 기록합니다.
```brightscript
LogInAppMessageImpression(in_app_message.id, brazetask)
```

##### 사용자가 메시지를 클릭하는 경우
사용자가 메시지를 클릭하면 클릭을 기록한 다음, `in_app_message.click_action`을 처리합니다.
```brightscript
LogInAppMessageClick(in_app_message.id, brazetask)
```

##### 사용자가 버튼을 클릭하는 경우
사용자가 버튼을 클릭하면 버튼 클릭을 기록한 다음, `inappmessage.buttons[selected].click_action`을 처리합니다.

```brightscript
LogInAppMessageButtonClick(inappmessage.id, inappmessage.buttons[selected].id, brazetask)
```

##### 인앱 메시지 처리 후
인앱 메시지를 처리한 후에는 해당 필드를 지워야 합니다.
```brightscript
m.BrazeTask.BrazeInAppMessage = invalid
```
