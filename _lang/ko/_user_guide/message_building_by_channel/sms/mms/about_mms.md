---
nav_title: "MMS에 대하여"
article_title: MMS에 대하여
page_order: 0
description: "이 참조 기사에서는 MMS 메시지가 무엇인지와 MMS 채널의 일반적인 사용 사례를 다룹니다."
page_type: reference
channel:
  - MMS
search_rank: 2  
---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"}MMS 메시지에 대하여

> MMS, 또한 멀티미디어 메시지 서비스로 알려진, 멀티미디어 자산(JPEG, GIF, PNG)을 포함하는 메시지를 휴대폰으로 보내는 데 사용됩니다.<br><br>SMS와 마찬가지로, MMS는 다른 채널에서는 할 수 없는 방식으로 고객과 즉시 소통할 수 있는 높은 긴급도의 메시징 채널입니다. 그러나 MMS는 텍스트만 포함된 SMS에 미디어를 추가할 수 있는 기능을 제공하여 SMS의 기능을 확장합니다.

## 잠재적 사용 사례

| 사용 사례 | 설명 |
| --- | --- |
| 프로모션 | 높은 가시성의 SMS 캠페인으로 사용자에게 도달하고, MMS의 미디어 측면을 활용하여 구매자에게 제공하는 내용을 유혹하세요. | 
| 재참여 캠페인 | 모든 다른 채널이 고객을 다시 데려오는 데 실패할 때 SMS 수신에 동의한 고객을 다시 참여시키십시오. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## MMS에 대해 알아보세요

### MMS 사용 가능

대부분의 미국 및 캐나다 통신사는 고객의 휴대폰에서 멀티미디어 자산을 수신하고 표시하는 것을 지원합니다. 국제 통신사를 위해 Braze는 지원되는 미국 또는 캐나다 기반 전화번호에서 보낸 MMS 메시지를 자동으로 변환하며, MMS를 지원하지 않는 목적지로만 전송합니다. 이 메시지의 경우, Braze는 첨부된 미디어를 메시지 본문에 추가된 짧은 URL로 대체하여 파일에 링크합니다.

### 구독 그룹

[구독 그룹][1]은 특정 유형의 메시징 목적으로 사용되는 발신 전화번호(짧은 코드, 긴 코드 및 영문 발신자 ID)의 모음입니다. 귀하의 구독 그룹에는 MMS를 사용할 수 있는 전화번호가 필요합니다. 귀하의 Braze 계정 매니저와 이 기능 활성화에 대해 상의하십시오.

### MMS 메시지 한도 및 처리량

MMS의 경우 메시지 제한은 1MB입니다(여기에는 멀티미디어 자산 및 메시지 본문 크기가 포함됩니다). 안전을 위해 Braze는 메시지 본문을 포함하면서 멀티미디어 자산의 용량을 600KB를 넘지 않는 것을 권장합니다.

MMS 처리량은 긴 코드를 통해 초당 세그먼트 하나입니다.

### 인바운드 MMS

사용자가 미디어 항목이 포함된 인바운드 메시지를 보낼 때 Braze는 커런츠와 Liquid를 통해 Liquid 태그 {%raw%}`{{sms.${inbound_media_url}}}`{%endraw%}에 미디어 항목의 URL을 노출합니다.

### 허용된 파일 형식

Braze는 JPEG, GIF, PNG 및 VCF 파일을 허용하며 MMS 메시지에 단일 멀티미디어 자산을 첨부할 수 있습니다.


[사진]: {% image_buster /assets/img/sms/MMS.png %}
[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement
