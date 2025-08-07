---
nav_title: 알 수 없는 전화번호 처리
article_title: 알 수 없는 SMS 전화번호 처리
page_order: 4
description: "이 참고 문서에서는 Braze가 신규 사용자의 알 수 없는 SMS 전화번호를 처리하는 방법에 대해 설명합니다."
page_type: reference
channel:
  - SMS
  
---

# 알 수 없는 전화번호 처리 - 신규 사용자

> Braze에서 SMS를 실행한 후 알 수 없는 사용자로부터 메시지를 받는 경우가 있을 수 있습니다. 다음 단계에서는 미확인 사용자 및 번호가 처리되는 방법에 대해 설명합니다.

{% alert important %}
현재 네이티브가 아닌 SMS 클라이언트를 사용 중이신가요? 그렇다면 알 수 없는 전화번호 처리 관련 [비네이티브 SMS 설명서]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/)를 참조하세요.
{% endalert %}

## 알 수 없는 번호에 대한 옵트인/아웃 및 사용자 지정 키워드 워크플로

Braze는 세 가지 방법 중 하나로 알 수 없는 번호에 자동으로 주소를 지정합니다.

1. 옵트인 키워드가 문자 메시지로 전송되는 경우:
  * Braze는 익명 프로필을 생성합니다.
  * 시스템에서 전화 속성을 설정합니다.
  * Braze에서 수신한 옵트인 키워드에 따라 사용자를 해당 구독 그룹에 구독합니다.<br><br>
2. 옵트아웃 키워드가 문자 메시지로 전송되는 경우:
  * Braze는 익명 프로필을 생성합니다.
  * 시스템에서 전화 속성을 설정합니다.
  * Braze가 수신한 옵트아웃 키워드에 따라 해당 구독 그룹에서 사용자를 구독 취소합니다.<br><br>
3. 다른 사용자 지정 키워드가 텍스트인 경우:
  * Braze는 문자 메시지를 무시하고 아무 조치도 취하지 않습니다.

[ualink]: {{site.baseurl}}/api/objects_filters/user_alias_object/
[telink]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[uaolink]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[e.164]: https://en.wikipedia.org/wiki/E.164