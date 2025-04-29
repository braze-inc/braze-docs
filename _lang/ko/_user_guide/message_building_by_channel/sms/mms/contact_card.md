---
nav_title: 연락처 카드
article_title: 연락처 카드
page_order: 3
description: "이 참조 문서에서는 MMS 및 SMS 메시지에 포함할 연락처 카드를 만드는 방법에 대해 설명합니다."
page_type: reference
channel:
  - MMS
  
---

# 연락처 카드 

> 연락처 카드(vCard 또는 가상 연락처 파일(VCF)이라고도 함)는 주소록이나 연락처로 쉽게 가져올 수 있는 비즈니스 및 연락처 정보를 전송하기 위한 표준화된 파일 형식입니다. 

연락처 카드는 [프로그래밍 방식으로](https://www.twilio.com/blog/send-vcard-twilio-sms) 생성하여 Braze [미디어 라이브러리에]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#media-library) 업로드하거나 내장된 연락처 카드 생성기를 통해 만들 수 있습니다. 이 카드에는 회사 이름, 전화번호, 주소, 이메일 및 작은 사진과 같은 공통 속성을 할당할 수 있습니다. 연락처 카드 만들기를 시작하려면 먼저 Braze에서 MMS를 사용하도록 설정되어 있는지 확인하세요.

## 연락처 카드 생성기

<script src="https://fast.wistia.com/embed/medias/7m77mdfr4y.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_7m77mdfr4y videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/7m77mdfr4y/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>

### 1단계: 이름 지정

연락처 카드는 SMS 및 MMS 작성기에서 만들 수 있습니다. 시작하려면 **연락처 카드 생성기** 탭을 선택하세요.

다음으로 회사 이름 또는 별명을 입력하라는 메시지가 표시됩니다. 이것은 사용자가 카드를 저장할 때 볼 이름입니다. 20자 제한이 적용되어 사용자가 연락처 및 메시징 앱에서 회사 이름 또는 별칭 전체를 볼 수 있습니다. 

![]({% image_buster /assets/img/sms/contact_card1.png %}){: style="max-width:60%" }

### 2단계: 전화번호 할당

사용 가능한 드롭다운 옵션에서 구독 그룹과 원하는 전화번호를 선택합니다. 이 번호는 연락처 카드에 나열되며 저장 후 휴대폰에서 문자를 보낼 수 있습니다.

영숫자 코드는 양방향 메시징과 호환되지 않으며 연락처 카드에는 지원되지 않는다는 점에 유의하세요.

### 3단계: 선택적 필드

![]({% image_buster /assets/img/sms/contact_card2.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

#### 연락처 카드 연락처 사진 업로드

연락처 카드의 썸네일 연락처 사진(선택 사항)을 업로드할 수 있습니다. 240 x 240 px JPEG 또는 PNG 이미지를 권장합니다. 업로드된 모든 고해상도 이미지는 메시지의 전달 가능성을 보장하기 위해 240 x 240픽셀로 크기가 조정됩니다. 5MB보다 큰 MMS 메시지는 실패할 수 있습니다.

#### 자세한 정보 추가

기타 필드에는 이름, 부제목, 주소 및 사용자가 사용할 수 있는 기타 연락처 정보를 입력할 수 있습니다. 

### 4단계: 연락처 카드 저장

모든 필수 필드를 입력한 후, **연락처 카드 생성**을 클릭하면 자동으로 캠페인 또는 캔버스에 첨부됩니다. 여기에서 메시지를 추가하고, 연락처 카드를 테스트하고, 캠페인 또는 캔버스를 시작할 수 있습니다.

연락처 카드는 [미디어 라이브러리에]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#media-library) 저장되어 향후 캠페인과 캔버스에서 쉽게 재사용할 수 있습니다.

## 기존 연락처 카드 추가

기존 연락처 카드를 추가하려면 캠페인 또는 캔버스를 만들고 원하는 구독 그룹을 선택합니다. 다음으로, 메시지 작성기 창에 **미디어 추가** 옵션이 나타납니다. 여기에서 기존 연락처 카드 파일을 업로드하거나 미디어 라이브러리를 통해 파일을 찾을 수 있습니다.
