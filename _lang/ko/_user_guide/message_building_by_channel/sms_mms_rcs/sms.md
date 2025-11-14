---
nav_title: "SMS"
article_title: SMS에 대하여
page_order: 13
description: "이 참조 문서는 SMS 채널의 일반적인 사용 사례와 SMS를 시작하는 데 필요한 요구 사항을 다룹니다."
page_type: reference
alias: /about_sms/
channel:
  - SMS
search_rank: 2
---

# [![Braze Learning 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"}SMS에 대하여

> 이 문서는 SMS 통합을 지원하고 고객과 효과적이고 전략적으로 소통할 수 있도록 돕는 일반적인 사용 사례, 요구 사항 및 알아야 할 용어를 공유합니다.\!["Braze에 오신 것을 환영합니다!"라는 텍스트가 포함된 SMS 메시지 여러분을 모시게 되어 기쁩니다. 시작하려면 문서를 확인하세요. https://www.braze.com/docs/ 도움을 원하시면 HELP를 입력하고 중지를 원하시면 STOP을 입력하세요."]({% image_buster /assets/img/sms/sms_about.png %}){: style="float:right;max-width:30%;margin-left:15px;margin-top:10px;border: 0;"}

<br>
SMS는 단문 메시지 서비스로도 알려져 있으며, 모바일 전화로 텍스트 메시지를 보내는 데 사용됩니다. 현재 전 세계에서 매일 230억 개 이상의 텍스트 메시지가 전송되고 있으며, SMS는 사용자와 고객에게 도달하는 가장 직접적인 방법입니다. 이러한 광범위한 사용과 입증된 가치는 SMS를 모든 규모의 비즈니스에 효과적인 마케팅 도구로 만들었습니다. 
<br><br>
## 잠재적 사용 사례

| 사용 사례 | 설명 |
|---|---|
| 일반 마케팅 | SMS 메시지는 고객에게 다가오는 거래, 유리한 세일 및 현재 또는 예상되는 제품을 직접적이고 유연하며 효율적으로 전달하는 방법입니다. |
| 알림 | SMS 메시지는 서비스 예약을 한 사용자에게 알리는 데 효과적일 수 있습니다. 예를 들어, 고객에게 의사 예약 하루 전에 SMS 메시지를 보내면 예약 누락을 최소화하는 데 도움이 되어 여러분과 고객 모두의 시간과 비용을 절약할 수 있습니다. |
| 거래 메시지 | SMS 메시지는 주문 확인 및 배송 정보와 같은 거래 알림을 전송하는 효율적인 방법으로, 필요한 모든 정보를 한 곳에서 제공합니다. 법적 지침이 존재하며, 거래 메시지를 보낼 때 준수해야 합니다. 이 지침이 확실하지 않은 경우, 내부 법무팀에 문의하십시오.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 요구 사항

SMS를 보내기 시작하기 전에 필요한 몇 가지 사항이 있습니다. 다음 차트를 참조하여 자세히 알아보십시오.

|요구 사항 | 설명 | 획득 |
|---|---|---|
| 전용 전화번호(단축 코드 또는 일반 코드) | 단일 브랜드 또는 호스트에 독점적으로 제공되는 전용 전화번호입니다. | Braze가 이러한 번호를 획득해 드립니다. [단축 및 일반 코드]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/)에 대해 자세히 알아보십시오.|
| 전화번호가 있는 사용자 목록 | 메시지를 보내기 시작하기 전에 사용자를 계정에 추가해야 합니다. 또한, 청중의 대략적인 규모를 알아야 합니다.  | 사용자는 처음에 Braze의 백엔드를 통해 추가됩니다. 이 목록을 저희에게 전달하여 업로드해야 합니다. 전화번호는 10자리 숫자와 국가 지역 코드로 형식이 지정되어야 합니다. [사용자 전화번호]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/)에 대해 자세히 알아보십시오. |
| [SMS 키워드 및 응답]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/) | 모든 기본 키워드는 메시지를 시작하기 전에 이에 대한 응답이 있어야 합니다. | 이들을 나열하고 온보딩 과정 중에 Braze 담당자 또는 온보딩 관리자에게 보내야 합니다. [SMS 키워드 템플릿]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#short-code-application)을(를) 확인하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 알아야 할 용어

전체 용어 목록은 SMS [알아야 할 용어]({{site.baseurl}}/sms_terms_to_know/)를 방문하세요.

