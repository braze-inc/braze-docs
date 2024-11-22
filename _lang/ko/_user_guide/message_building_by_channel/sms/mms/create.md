---
nav_title: MMS 캠페인 만들기
article_title: MMS 캠페인 만들기
page_order: 2
description: "이 참고 문서에서는 MMS 메시지 작성, 전송 및 미리 보기와 관련된 단계를 설명합니다."
page_type: reference
tool:
  - Campaigns
channel:
  - MMS
search_rank: 1  
---

# MMS 캠페인 만들기

> 이 문서에는 SMS 작성기의 일부인 MMS 작성과 관련된 정보가 포함되어 있습니다. SMS/MMS 작성기에 대한 자세한 내용은 [SMS 작성기를]({{site.baseurl}}/user_guide/message_building_by_channel/sms/create/) 참조하세요.

## MMS 전송 기본 사항

### 구독 그룹 선택

타겟팅할 MMS 사용 전화 번호로 구독 그룹을 지정해야 합니다(짧은 코드 또는 긴 코드 가능).

### 메시지 본문 입력

미디어 라이브러리에서 PNG, JPEG, GIF 및 VCF 이미지 유형을 입력하거나 URL을 지정합니다. 하나의 이미지만 지원됩니다.

### MMS 전송에 대한 이해

MMS는 문자 전용 SMS와 다른 요금으로 청구되며, 모든 이동통신사가 MMS를 허용하는 것은 아닙니다. 이러한 경우 Twilio는 자동으로 MMS를 사용자가 클릭할 수 있는 이미지 링크로 변환합니다.

### 연락처 카드 사용

연락처 카드(vCard 또는 가상 연락처 파일(vcf)이라고도 함)는 비즈니스 및 연락처 정보를 전송하기 위한 표준화된 파일 형식으로 주소록이나 연락처 목록으로 쉽게 가져올 수 있습니다. 이러한 카드는 [프로그래밍 방식으로](https://www.twilio.com/blog/send-vcard-twilio-sms) 생성하여 Braze 미디어 라이브러리에 업로드하거나 내장된 [연락처 카드 생성기를]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/contact_card/) 통해 만들 수 있습니다.

## MMS 메시지 만들기

MMS 메시지를 작성하려면 MMS 전송을 위해 구독 그룹을 구성해야 합니다. 이는 구독 그룹을 선택할 때 MMS 태그가 표시되는 것으로 알 수 있습니다. MMS 지원 구독 그룹을 선택하면 이미지를 업로드하거나 이미지 URL을 참조하거나 연락처 카드를 포함할 수 있습니다.

!['작성' 탭에서 메시지를 작성할 수 있습니다.]({% image_buster /assets/img/sms/mms_composer.png %})

### 이미지 사양

| **이미지 사양** | **권장 속성** |
|--------------------------|----------------------------|
| 크기                     | 최대 600KB        |
| 파일 유형               | PNG, JPEG, GIF             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## MMS 메시지 미리보기

Braze는 메시지 작성기의 **미리보기** 패널에서 업로드한 이미지의 미리보기를 제공합니다. 

{% alert note %}
SMS/MMS 자산의 순서는 사용자 지정할 수 없습니다. 주문은 이 메시지를 수신하는 휴대폰에 따라 달라집니다.
{% endalert %}

!["다음 여행을 준비하세요!!!" 메시지의 예입니다. 미리보기에는 문자로 전송된 메시지와 이미지가 표시됩니다.]({% image_buster /assets/img/sms/mms_preview.png %})
