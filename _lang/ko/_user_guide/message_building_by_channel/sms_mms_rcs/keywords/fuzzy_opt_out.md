---
nav_title: 퍼지 옵트아웃
article_title: 퍼지 옵트아웃
description: "이 참조 문서에서는 수신 메시지가 수신 거부 키워드와 일치하지 않을 때를 인식하려고 시도하는 설정인 퍼지 수신 거부를 구성하는 방법을 다룹니다."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
page_order: 1

---

# 퍼지 옵트아웃

![인바운드 퍼지 옵트아웃에 대한 응답으로 아웃바운드 옵트아웃 메시지를 표시하는 iOS 메시지 채팅 "Please stopppp".]({% image_buster /assets/img/sms/fuzzy1.jpg %}){: style="float:right;max-width:30%;margin-left:15px;"}

> Braze로 SMS, MMS, RCS를 전송하는 사용자는 정의된 관련 법률, 규정 및 업계 표준을 준수해야 합니다. 법률에 따르면 사용자가 "STOP"이라고 문자를 보내면 해당 메시징 프로그램과 관련된 모든 후속 메시징이 중단됩니다. Braze는 이러한 메시지를 자동으로 처리하고 사용자의 구독을 취소합니다.<br><br>퍼지 옵트아웃은 수신 메시지가 [옵트아웃 키워드]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/)와 일치하지 않지만, 옵트아웃 의도를 나타내는 경우를 인식하려고 시도합니다. 퍼지 옵트아웃이 활성화되어 있고 인바운드 키워드 응답이 '퍼지'로 간주되면 Braze는 사용자에게 옵트아웃을 안내하는 응답 메시지로 자동 응답합니다.

현재는 [로컬 언어]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#multi-language-support)로 영어를 사용하여 생성된 옵트아웃 키워드만 지원됩니다.

## 모호한 것으로 간주되는 것은 무엇입니까?

인바운드 응답이 '모호한' 것으로 간주되는 기준은 다음과 같습니다.
- QWERTY 키보드에서 문자 하나를 왼쪽 또는 오른쪽의 문자로 바꾸면 일치하는 옵트아웃 키워드가 생성됩니다.
- 메시지의 하위 문자열이 옵트아웃 키워드와 일치합니다.

예를 들어, "Stpo" 또는 "Please stopppp"는 모호한 것으로 간주되며, 모호한 옵트아웃 응답이 전송됩니다. 사용자가 옵트아웃 키워드로 응답하면 구독 취소 이벤트가 트리거됩니다.

## 퍼지 옵트아웃 구성

퍼지 옵트 아웃을 구성하려면 구독 그룹 키워드 관리 페이지로 이동하십시오.

1. **대상** > 구독으로 이동하여 **구독** 그룹을 선택합니다. **SMS/MMS/RCS** 구독 그룹을 선택합니다.

{:start="2"}
2\. **글로벌 키워드에서** **옵트아웃** 카테고리를 찾아 연필 아이콘을 선택합니다.
3\. **퍼지 옵트 아웃**을 켜서 활성화합니다.
4\. 희미한 옵트아웃 응답을 원하는 대로 수정하십시오. 

![]({% image_buster /assets/img/sms/fuzzy2.png %}){: style="max-width:70%;"}


