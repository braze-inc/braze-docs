---
nav_title: "MMS"
article_title: MMS에 대하여
page_order: 15
description: "이 참조 문서는 MMS 메시지가 무엇인지와 MMS 채널의 일반적인 사용 사례를 다룹니다."
page_type: reference
alias: /about_mms/
channel:
  - MMS
search_rank: 2  
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"}MMS 메시지에 대하여

> MMS는 멀티미디어 메시지 서비스(Multimedia Message Service)로, 멀티미디어 자산(JPEG, GIF, PNG)을 포함한 메시지를 휴대폰으로 전송하는 데 사용됩니다.<br><br>SMS와 마찬가지로 MMS는 고객과 즉시 소통할 수 있는 긴급 메시징 채널로, 다른 채널로는 할 수 없는 방식입니다. 그러나 MMS는 SMS의 기능을 확장하여 텍스트 전용 SMS에 미디어를 추가할 수 있는 기능을 제공합니다.

## 잠재적 사용 사례

| 사용 사례 | 설명 |
| --- | --- |
| 프로모션 | 높은 가시성을 가진 SMS 캠페인으로 사용자에게 도달하되, MMS의 미디어 측면을 활용하여 제공하는 내용을 매력적으로 만드세요. | 
| 재참여 캠페인 | 모든 다른 채널이 고객을 다시 불러오는 데 실패할 때 SMS 수신에 동의한 고객을 재참여시키세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## MMS 알아보기

### MMS 가용성

대부분의 미국 및 캐나다 통신사는 고객의 휴대폰에서 멀티미디어 자산을 수신하고 표시하는 것을 지원합니다. 국제 통신사의 경우, Braze는 지원되는 미국 또는 캐나다 기반 전화번호에서 전송된 MMS 메시지를 자동으로 변환하며, MMS를 지원하지 않는 목적지로만 전송됩니다. 이러한 메시지의 경우, Braze는 첨부된 미디어를 파일에 링크된 짧은 URL로 대체하여 메시지 본문에 추가합니다.

### 구독 그룹

[구독 그룹]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement)은 특정 유형의 메시징 목적을 위해 사용되는 발신 전화번호(단문 코드, 장문 코드 및 알파벳 발신자 ID)의 모음입니다. 귀하의 구독 그룹은 MMS가 활성화된 전화번호가 필요합니다. 이 기능을 활성화하려면 Braze 계정 관리자와 상담하십시오.

### MMS 메시지 한도 및 처리량

통신사는 궁극적으로 MMS 전송의 성공을 결정하는 자체 파일 크기 한도를 부과합니다. 이 한도는 지리 및 통신사에 따라 다를 수 있으므로, 안전을 위해 Braze는 멀티미디어 자산의 크기가 메시지 본문을 포함하여 600 KB를 초과하지 않도록 권장합니다. 또한 귀하의 미디어가 사용자 통신사에서 전달될 수 있는지 확인하기 위해 테스트할 것을 권장합니다.

MMS 처리량은 장기 코드로 초당 한 세그먼트입니다.

#### 통신사 파일 크기 한도

| 파일 크기 | 통신사 처리 |
| --- | --- |
| 300 KB | 모든 통신사는 이 크기의 MMS 메시지를 안정적으로 처리해야 합니다. |
| 600 KB | 이는 대부분의 통신사에서 MMS의 표준 최대 파일 크기로 간주됩니다. |
| 1 MB |  대부분의 미국 및 캐나다 통신사는 이 크기의 MMS 메시지를 처리할 수 있지만, 통신사에 따라 다를 수 있습니다. 일부 통신사는 이보다 더 큰 파일 크기를 허용할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### 수신 MMS

사용자가 미디어 항목을 포함하는 수신 메시지를 보낼 때, Braze는 Currents와 Liquid를 통해 미디어 항목의 URL을 Liquid 태그 {%raw%}`{{sms.${inbound_media_url}}}`{%endraw%}로 노출합니다.

### 허용된 파일 형식

Braze는 JPEG, GIF, PNG 및 VCF 파일을 허용하며 MMS 메시지에 단일 멀티미디어 자산을 첨부할 수 있습니다.


