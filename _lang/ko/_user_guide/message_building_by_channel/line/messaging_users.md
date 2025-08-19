---
nav_title: 사용자 메시징
article_title: LINE 사용자 메시지 보내기
page_order: 2
description: "이 참고 문서에서는 템플릿 캠페인과 캔버스를 사용하여 사용자와 채팅하는 방법에 대해 설명합니다."
page_type: reference
channel:
 - LINE
alias: /line/messaging_users/
---

# LINE 사용자에게 메시지 보내기

> LINE은 양방향 커뮤니케이션 채널입니다. 템플릿 캠페인과 캔버스를 사용하여 사용자에게 메시지를 보내는 것을 넘어 사용자와의 대화에 참여할 수 있습니다. 이 기사에서는 수신 메시지 및 인식되지 않은 응답에 대한 트리거 단어를 설정하는 방법과 같은 사용자 메시징의 세부 사항을 다룹니다.

LINE 트리거 단어를 사용하는 등 LINE을 통해 사용자와 대화할 수 있는 방법은 다양합니다. 클릭 유도 문안(CTA)을 사용하여 LINE 메시지에 대한 사용자 참여를 유도할 수도 있습니다.

## 동작 기반 트리거

트리거 단어가 포함된 인바운드 LINE 메시지(사용자가 보낸 메시지)를 수신하면 캠페인과 캔버스를 생성하여 시작, 분기, 여정 중간에 변경할 수 있습니다. 사용자가 보낼 것으로 예상되는 내용과 일치하는 트리거 단어를 선택해야 합니다.

### 캠페인

실행 기반 전달 캠페인을 예약할 때 트리거 단어를 설정하세요.

![Action-based trigger of "Send this campaign to users who sent inbound LINE to subscription group where the message body is" and a blank field.]({% image_buster /assets/img/line/trigger_word_campaign.png %})

### 캔버스

캔버스의 [작업 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths) 내에 트리거 단어를 설정하세요.

![Action path with a trigger of "Send this campaign to users who sent inbound LINE to subscription group where the message body is" and a blank field.]({% image_buster /assets/img/line/trigger_word_canvas.png %})

### 요구 사항

캠페인이나 캔버스를 구축할 때 트리거 단어의 각 글자는 대문자로 표기해야 하지만, Braze는 인바운드 트리거 단어를 대문자로 표기하지 않아도 됩니다. 예를 들어 트리거 단어가 "JOIN2023"인 경우, "jOin2023"의 인바운드 메시지는 여전히 캔버스 또는 캠페인을 트리거합니다.

트리거 단어를 지정하지 않으면 *모든* 인바운드 LINE 메시지에 대해 캠페인 또는 캔버스가 실행됩니다. 여기에는 활성 캠페인과 캔버스에서 일치하는 문구가 있는 메시지가 포함되며, 이 경우 사용자는 두 개의 LINE 메시지를 받게 됩니다.

## 인식할 수 없는 응답

대화형 캔버스에서 인식되지 않는 응답에 대한 트리거 옵션을 포함해야 합니다. 이렇게 하면 사용자에게 사용 가능한 프롬프트(또는 트리거 단어)를 알려주고 채널에 대한 기대치를 설정할 수 있습니다.

### 인식되지 않는 응답에 대한 트리거 만들기

사용자 지정 필터 문구에 대한 작업 그룹을 만든 후, **LINE 메시지 보내기** 작업 경로에 다른 작업 그룹을 추가하고 **메시지 본문 위치는** 체크하지 마세요. 이것은 "else" 절과 유사하게 인식되지 않은 모든 사용자 응답을 포착합니다.

이 메시지의 경우 이 채널은 사람이 모니터링하고 있지 않음을 알리는 LINE 메시지를 보내고, 필요한 경우 지원 채널로 안내해야 합니다.

