---
nav_title: 수신 동의 및 수신 거부 키워드
article_title: SMS 수신 동의/수신 거부 키워드
page_order: 0
description: "이 참조 문서에서는 Braze가 SMS 메시징을 위한 기본 수신 동의 및 수신 거부 키워드를 처리하는 방법을 다룹니다."
page_type: reference
alias: /optin_optout/
tool:
  - Dashboard

channel:
  - SMS
---

# 수신 동의 및 수신 거부 키워드

> 규정에 따라 모든 수신 동의, 수신 거부 및 도움/정보 키워드 응답에 대한 응답이 필요합니다. Braze는 다음 _정확한, 단어, 대소문자 구분 없음_ 메시지를 자동으로 처리하며, 모든 수신 요청에 대해 사용자와 관련된 전화번호의 [구독 그룹 상태]({{site.baseurl}}/sms_rcs_subscription_groups/)를 자동으로 업데이트합니다.

## 키워드 개요

Braze는 다음 키워드를 자동으로 처리하고 모든 수신 요청에 대해 전화번호의 구독 그룹 상태를 업데이트합니다. 이 기본 키워드 및 응답은 사용자 정의할 수도 있습니다. 

| 유형 | 키워드 | 변경 |
\|-|-------|---|
|수신 동의| `START`<br> `YES`<br> `UNSTOP` | 이러한 `Opt-In` 키워드 중 하나가 포함된 모든 수신 요청은 구독 그룹 상태 변경을 `subscribed`으로 초래합니다. 또한, 해당 구독 그룹과 관련된 발신자 풀은 이제 해당 고객에게 SMS, MMS 또는 RCS 메시지를 보낼 수 있습니다(발신자가 지원하는 메시징 유형에 따라 다름). <br><br>사용자는 정의한 수신 동의 자동 응답을 받게 됩니다.  |
|수신 거부| `STOP`<br> `STOPALL`<br> `UNSUBSCRIBE`<br> `CANCEL`<br> `END`<br> `QUIT` | 이러한 `Opt-Out` 키워드 중 하나가 포함된 모든 수신 요청은 구독 그룹 상태 변경을 `unsubscribed`으로 초래합니다. 또한, 해당 구독 그룹과 관련된 번호 풀은 더 이상 해당 고객에게 메시지를 보낼 수 없습니다.<br><br>사용자는 정의한 수신 거부 자동 응답을 받게 됩니다. |
| 도움 | `HELP`<br> `INFO` | 사용자는 정의된 도움말 자동 응답을 받게 됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

오직 **정확한, 단어 하나의 메시지**만 처리됩니다 (대소문자 구분 없음). `STOP PLEASE`와 같은 키워드는 [퍼지 선택 해제]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/fuzzy_opt_out/)가 활성화되지 않는 한 무시됩니다.

수신자가 `HELP` 또는 `INFO` 키워드를 사용하면 자동으로 응답이 트리거됩니다. 이 자동 응답 메시지의 기본 응답은 [온보딩]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process) 및 전화번호 조달 기간 동안 설정됩니다. 초기 온보딩 기간 이후에도 이러한 응답을 계속 업데이트할 수 있습니다.

{% alert tip %}
선택 해제 처리 확장에 관심이 있으신가요? [퍼지 선택 해제]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/fuzzy_opt_out/)를 시도해 보세요. 이는 수신 메시지가 선택 해제 키워드와 일치하지 않지만 선택 해제 의도를 나타낼 때 인식하려고 시도하는 기능입니다.
{% endalert %}

