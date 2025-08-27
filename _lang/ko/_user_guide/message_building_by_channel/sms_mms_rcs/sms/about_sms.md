---
nav_title: "SMS 정보"
article_title: SMS 정보
page_order: 1
description: "이 참조 문서에서는 SMS 채널의 일반적인 사용 사례와 SMS를 시작하고 실행하는 데 필요한 요구 사항을 다룹니다."
page_type: reference
alias: /about_sms/
channel:
  - SMS
search_rank: 2
---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"}SMS 소개

> 이 문서에서는 SMS 통합에 도움이 되고 고객과 효과적이고 전략적으로 커뮤니케이션할 수 있도록 참고할 수 있는 몇 가지 일반적인 사용 사례, 요구 사항 및 알아야 할 용어를 공유합니다.![텍스트가 포함된 SMS 메시지 "Braze에 오신 것을 환영합니다! 여러분과 함께하게 되어 기쁩니다. 시작하려면 설명서를 확인하세요. https://www.braze.com/문서/ 도움을 원하시면 HELP를 입력하고 중지를 원하시면 STOP을 입력하세요."]({% image_buster /assets/img/sms/sms_about.png %}){: style="float:right;max-width:30%;margin-left:15px;margin-top:10px;border: 0;"}

<br>
단문 메시지 서비스라고도 하는 SMS는 휴대폰으로 문자 메시지를 보내는 데 사용됩니다. 현재 전 세계적으로 매일 230억 건 이상의 문자 메시지가 전송되고 있으며, SMS는 사용자와 고객에게 가장 직접적으로 다가갈 수 있는 수단입니다. 이러한 광범위한 사용과 입증된 가치 덕분에 SMS는 모든 규모의 비즈니스에 효과적인 마케팅 도구로 자리 잡았습니다. 
<br><br>
## 잠재적 사용 사례

| 사용 사례 | 설명 |
|---|---|
| 일반 마케팅 | SMS 메시지는 고객에게 예정된 거래, 판매 호재, 현재 또는 예상되는 제품을 직접적이고 유연하며 효율적으로 전달할 수 있는 방법입니다. |
| 리마인더 | SMS 메시지는 서비스 예약을 설정한 사용자에게 알림을 보내는 데 효과적일 수 있습니다. 예를 들어, 병원 예약 전날 고객에게 예약을 상기시키는 SMS 메시지를 보내면 예약을 놓치는 일이 최소화되어 판매자와 고객 모두 시간과 비용을 절약할 수 있습니다. |
| 트랜잭션 메시지 | SMS 메시지는 주문 확인 및 배송 정보와 같은 거래 알림을 전송하는 효율적인 방법으로, 필요한 모든 정보를 한 곳에서 편리하게 확인할 수 있습니다. 트랜잭션 메시지를 보낼 때 준수해야 하는 법적 가이드라인이 있다는 점에 유의하세요. 이러한 가이드라인에 대해 잘 모르는 경우 내부 법무팀에 문의하세요.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 요구 사항

SMS를 보내기 전에 몇 가지 필요한 사항이 있습니다. 자세한 내용은 다음 차트를 참조하세요.

|요구 사항 | 설명 | 획득 |
|---|---|---|
| 전용 전화번호(단축 코드 또는 긴 코드) | 단일 브랜드 또는 호스트에게만 제공되는 전용 전화번호입니다. | Braze에서 이러한 번호 획득을 대행합니다. [짧은 코드와 긴 코드에]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/) 대해 자세히 알아보세요.|
| 전화번호가 있는 사용자 목록 | 메시지 전송을 시작하려면 먼저 계정에 사용자를 추가해야 합니다. 또한 오디언스의 대략적인 규모를 파악해야 합니다.  | 사용자는 처음에 백엔드를 통해 Braze에 추가됩니다. 업로드하려면 이 목록을 저희에게 전달해 주셔야 합니다. 전화번호는 국가 지역 번호와 함께 10자리 숫자로 형식화해야 합니다. [사용자 전화번호]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/)에 대해 자세히 알아보세요. |
| [SMS 키워드 및 응답]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/) | 모든 기본 키워드에 귀속된 응답이 있어야 메시징을 시작할 수 있습니다 | 온보딩 과정에서 이러한 목록을 작성하여 Braze 담당자 또는 온보딩 매니저에게 보내야 합니다. [SMS 키워드 템플릿]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#short-code-application) 보기. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 알아두어야 할 용어

전체 용어 목록을 보려면 [알아야 할 SMS 약관]({{site.baseurl}}/sms_terms_to_know/)을 참조하세요.

