---
nav_title: MMS 캠페인 만들기
article_title: MMS 캠페인 만들기
page_order: 2
description: "이 참고 문서에서는 MMS 메시지 작성, 전송 및 미리 보기와 관련된 단계를 다룹니다."
page_type: reference
alias: /create_mms_message/
tool:
  - Campaigns
channel:
  - MMS
search_rank: 1  
---

# MMS 캠페인 만들기

> 이 문서에는 SMS 작성기의 일부인 MMS 작성에 관한 정보가 포함되어 있습니다. SMS/MMS 작성기에 대한 자세한 내용은 [SMS 작성기를]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/create/) 참조하세요.

## MMS 전송 기본 사항

### 구독 그룹 선택하기

타겟팅할 MMS 사용 휴대폰 번호로 구독 그룹을 지정해야 합니다(짧은 코드 또는 긴 코드 가능).

### 메시지 본문 입력

미디어 라이브러리에서 PNG, JPEG, GIF 및 VCF 이미지 유형을 입력하거나 URL을 지정합니다. 하나의 이미지만 지원됩니다.

### MMS 전송 이해하기

MMS는 문자 전용 SMS와 다른 요금으로 청구되며, 모든 이동통신사가 MMS를 수락하는 것은 아닙니다. 이러한 경우 Twilio는 MMS를 사용자가 클릭할 수 있는 이미지 링크로 자동 변환합니다.

### 연락처 카드 사용

연락처 카드(vCard 또는 가상 연락처 파일(vcf)이라고도 함)는 비즈니스 및 연락처 정보를 전송하기 위한 표준화된 파일 형식으로, 주소록이나 연락처 목록으로 쉽게 가져올 수 있습니다. 이러한 카드는 [프로그래밍 방식으로](https://www.twilio.com/blog/send-vcard-twilio-sms) 생성하여 Braze 미디어 라이브러리에 업로드하거나 구축된 [연락처 카드 생성기를]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/) 통해 만들 수 있습니다.

## MMS 메시지 작성하기

MMS 메시지를 작성하려면 MMS 전송을 위해 구독 그룹을 구성해야 합니다. 구독 그룹을 선택할 때 MMS 태그가 표시되면 이를 알 수 있습니다. MMS 사용 구독 그룹을 선택하면 이미지를 업로드하거나 이미지 URL을 참조하거나 연락처 카드를 포함할 수 있습니다.

'작성하기' 탭을 클릭하여 메시지를 작성합니다.]({% image_buster /assets/img/sms/mms_composer.png %}){: style="max-width:80%;"}

### 이미지 사양

| **이미지 사양** | **권장 속성** |
|--------------------------|----------------------------|
| 크기                     | 최대 600KB        |
| 파일 형식               | PNG, JPEG, GIF             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## MMS 메시지 미리보기

Braze는 메시지 작성기의 **미리보기** 패널에서 업로드한 이미지의 미리 보기를 제공합니다. 

{% alert note %}
SMS/MMS 자산의 주문은 커스텀할 수 없습니다. 주문은 이 메시지를 수신하는 휴대폰에 따라 달라집니다.
{% endalert %}

"집에서...헬스장에 갈 준비가 되셨나요?" 메시징의 예입니다. 미리보기에는 텍스트로 전송된 메시지와 이미지가 표시됩니다.]({% image_buster /assets/img/sms/mms_preview.png %})
