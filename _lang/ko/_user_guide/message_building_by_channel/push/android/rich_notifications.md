---
nav_title: "리치 알림 만들기"
article_title: "Android용 리치 푸시 알림 만들기"
page_order: 3
page_layout: tutorial
description: "이 튜토리얼에서는 Braze 캠페인에 대한 Android 리치 알림을 설정하는 방법을 다룹니다."
platform: Android
channel:
  - Push
tool:
  - Campaigns
  
---

# Android용 리치 푸시 알림 만들기

> 리치 알림을 사용하면 단순한 복사 외에 추가 콘텐츠를 추가하여 푸시 알림을 더욱 커스텀할 수 있습니다. Android 알림에는 한동안 "확장된 알림 이미지"라고 하는 이미지가 푸시 알림에 포함되어 있었습니다.

## 전제 조건

Android용 리치 푸시 알림을 만들기 전에 다음 세부 사항을 참고하세요:

- 빠른 푸시 캠페인을 만들 때는 Android 리치 알림을 사용할 수 없습니다.
- Android 확장 알림 이미지는 2:1 비율이어야 하지만 크기 제한은 없습니다.
- Android에서는 표준 알림 보기에 별도의 이미지를 설정할 수도 있습니다. 권장되는 이미지 크기는 다음과 같습니다: 
  - **Small:** 512x256
  - **중간:** 1024x512 
  - **Large:** 2048x1024
- 현재 Android 리치 알림은 JPEG 및 PNG 이미지 형식을 포함한 정적 이미지만 허용합니다. GIF 및 기타 이미지 형식은 아직 지원되지 않습니다.
- 푸시 알림에 실행 버튼을 추가하면 표시할 수 있는 이미지 영역에 영향을 줄 수 있습니다. 대시보드 프리뷰와 라이브 기기로 테스트하여 결과가 예상대로 나오는지 확인하세요.
- 이미지를 렌더링하려면 Braze 소프트웨어 개발 키트를 인에이블먼트해야 합니다.

{% alert note %}
Braze는 리치 푸시 설정 방법에 대한 지침을 제공하지만, 실제 리치 푸시 알림의 렌더링은 기기의 종횡비, Android 버전, OEM별 제약 조건 등과 같은 외부 요인에 따라 달라질 수 있습니다. 여러 Android 기기로 보내기 테스트를 수행하여 리치 푸시 알림이 의도한 대로 표시되는지 확인하는 것이 좋습니다.
{% endalert %}

## Android 리치 알림 설정하기

### 1단계: 푸시 캠페인 만들기

다음 단계에 따라 [캠페인을 만들어]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message) Android용 푸시 알림을 작성합니다. 리치 콘텐츠가 포함되지 않은 푸시 알림을 설정할 때도 동일한 작성기를 사용하게 됩니다.

### 2단계: 캡션 추가

알림의 이미지 앞에 표시할 **요약 텍스트/이미지 캡션을** 추가합니다.

이미지를 추가하거나 이미지 URL을 입력할 수 있는 확장된 알림 이미지 섹션입니다.]({% image_buster /assets/img_archive/android_rich_summarytext.png %})

### 3단계: 미디어 추가

메시지 작성기의 **확장된 알림 이미지** 필드에 이미지를 추가합니다. 이미지는 대시보드를 통해 직접 업로드하거나 다른 곳에서 호스팅되는 콘텐츠 URL을 지정하여 업로드할 수 있습니다.

지원되는 이미지에 대한 자세한 내용은 [이미지 사양을]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push) 확인하세요.

사용자에게 "안녕하세요"라는 제목과 "로열티 프로그램에 가입해 주셔서 감사합니다!"라는 문구가 포함된 iOS용 푸시 알림이 전송됩니다.]({% image_buster /assets/img_archive/android_rich_image.png %})

### 4단계: 캠페인 계속 만들기

리치 알림 콘텐츠가 대시보드에 업로드된 후에는 [캠페인을]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/) 계속 [예약할]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/) 수 있습니다.

