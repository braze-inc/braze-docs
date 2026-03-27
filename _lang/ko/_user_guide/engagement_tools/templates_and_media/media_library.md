---
nav_title: 미디어 라이브러리
article_title: 미디어 라이브러리
page_order: 0
page_type: reference
description: "이 참조 문서에서는 미디어 라이브러리에 대해 다룹니다. 여기서 단일 중앙 집중식 위치에서 자산을 관리하는 방법, AI를 활용한 이미지 생성, 메시지 작성기 내 미디어 접근 방법을 배울 수 있습니다."
tool: Media

---

# 미디어 라이브러리

> 미디어 라이브러리를 통해 자산을 단일 중앙 위치에서 관리할 수 있습니다. 

## 미디어 라이브러리 대 CDN

CDN(Content Delivery Network) 대신 미디어 라이브러리를 사용하면 인앱 메시지에 대해 더 나은 캐싱과 성능을 제공합니다. 인앱 메시지에 포함된 모든 미디어 라이브러리 자산은 더 빠른 표시를 위해 미리 캐시되며 오프라인에서도 표시할 수 있습니다. 또한 미디어 라이브러리는 Braze 작성기와 통합되어 마케터가 이미지 URL을 복사하여 붙여넣는 대신 이미지를 선택하거나 태그할 수 있습니다.

## 미디어 라이브러리 접근

미디어 라이브러리에서 자산 유형, 크기, 치수, URL, 라이브러리에 추가된 날짜 및 기타 정보를 볼 수 있습니다. Braze 미디어 라이브러리에 액세스하려면 **템플릿** > **미디어 라이브러리**로 이동합니다. 여기에서 다음을 수행할 수 있습니다:

* 한 번에 여러 이미지를 업로드
* 가상 연락처 파일(.vcf) 업로드
* WhatsApp 메시지에 사용할 동영상 파일 업로드
* 이미지가 담긴 폴더를 업로드(최대 50개 이미지)
* [AI를 사용하여 이미지를 생성](#generate-ai)하고 미디어 라이브러리에 저장
* 기존 이미지를 잘라서 메시지에 적합한 비율로 만들기
* 태그 또는 Teams를 추가하여 이미지를 더 잘 정리
* 미디어 라이브러리 그리드에서 태그 또는 Teams로 검색
* 이미지나 폴더를 드래그 앤 드롭하여 업로드
* 이미지 삭제

![미디어 라이브러리 페이지에는 파일을 드래그 앤 드롭하거나 업로드할 수 있는 "라이브러리에 업로드" 섹션이 포함되어 있습니다. 미디어 라이브러리에는 업로드된 콘텐츠 목록도 있습니다.]({% image_buster /assets/img_archive/media_library_main.png %})

나중에 Braze에서 메시지를 작성할 때 미디어 라이브러리에서 이미지를 불러올 수 있습니다.

![메시지 작성기에 따라 미디어 라이브러리에 접근하는 두 가지 일반적인 방법. 하나는 제목이 "이미지 및 GIF"인 이메일 드래그 앤 드롭 편집기와 "미디어 라이브러리에서 추가" 버튼을 보여줍니다. 다른 화면에는 '미디어'라는 제목과 '이미지 추가' 버튼이 있는 푸시 알림 및 인앱 메시지 같은 표준 편집기들이 표시됩니다.]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} 미디어 라이브러리에 대한 자세한 내용은 [템플릿 및 미디어 FAQ]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs)를 참조하세요. {% endalert %}

## 이미지 사양

미디어 라이브러리에 업로드되는 모든 이미지는 5&nbsp;MB 미만이어야 합니다. 지원되는 파일 형식은 PNG, JPEG, GIF, SVG 및 WebP입니다. 메시징 채널별 특정 이미지 권장 사항은 다음 섹션을 참조하세요.

{% alert important %}
매우 길쭉한 형태(예: 3000 x 2 픽셀)의 GIF나 300프레임 이상의 GIF는 총 파일 크기가 작더라도 업로드에 실패할 수 있습니다.
{% endalert %}

### 콘텐츠 카드

{% multi_lang_include image_specs.md variable_name='content cards' %}

### 이메일

{% multi_lang_include image_specs.md variable_name="email"  %}

### 인앱 메시지

{% multi_lang_include image_specs.md variable_name="in-app messages"  %}

자세한 내용은 [인앱 메시지 크리에이티브 세부 정보]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/)를 참조하세요.

### 푸시

{% multi_lang_include image_specs.md variable_name="push notifications"  %}

#### 권장 메시지 길이

최상의 결과를 위해 푸시 메시지를 작성할 때 다음 메시지 길이 가이드라인을 참조하세요. 이미지 유무, 알림 상태(iOS), 사용자 기기의 표시 설정, 기기 크기에 따라 다소 차이가 있을 수 있습니다.

| 메시지 유형 | 권장 길이 (텍스트만) | 권장 길이 (리치) |
| --- | --- | --- |
| iOS 잠금 화면 | 160자 | 130자 |
| iOS 알림 센터 | 160자 | 130자 |
| iOS 배너 알림 | 80자 | 65자 |
| Android 잠금 화면 | 49자 | N/A |
| Android 알림 서랍 | 597자 | N/A |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

iOS 글자 수에 대한 자세한 내용은 [iOS 글자 수 가이드라인]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count)을 참조하세요.

#### 웹 푸시

{% tabs %}
{% tab 이미지 %}

| 브라우저 | 권장 아이콘 크기 |
| --- | --- |
| Chrome | 192 x 192 px 이상 |
| Firefox | 192 x 192 px 이상 |
| Safari | 192 x 192 px 이상 (macOS 13+ Safari 16에서 캠페인별 설정 가능) |
| Opera | 192 x 192 px 이상 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

| 브라우저 | 플랫폼 | 큰 이미지 크기 |
| --- | --- | --- |
| Chrome | Android | 2:1 종횡비 |
| Firefox | Android | N/A |
| Chrome | Windows | 2:1 종횡비 |
| Edge | Windows | 2:1 종횡비 |
| Firefox | Windows | N/A |
| Opera | Windows | 2:1 종횡비 |
| Chrome | macOS | N/A |
| Safari | macOS | N/A |
| Firefox | macOS | N/A |
| Opera | macOS | N/A |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab 텍스트 %}

| 브라우저 | 플랫폼 | 최대 제목 길이 | 최대 본문 길이 |
| --- | --- | --- | --- |
| Chrome | Android | 35 | 50 |
| Firefox | Android | 35 | 50 |
| Chrome | Windows | 50 | 120 |
| Edge | Windows | 50 | 120 |
| Firefox | Windows | 54 | 200 |
| Opera | Windows | 50 | 120 |
| Chrome | macOS | 35 | 50 |
| Safari | macOS | 38 | 84 |
| Firefox | macOS | 38 | 42 |
| Opera | macOS | 38 | 42 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% endtabs %}

#### 푸시 알림 예시

{% tabs %}
{% tab iOS %}

![텍스트에 "Hi! This is an iOS Push with an image"라고 표시되고 이모지가 있는 iOS 푸시 알림. 텍스트 옆에 작은 이미지가 있습니다.]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![이전 메시지와 동일한 텍스트가 포함된 하드 푸시 iOS 푸시 알림으로, 텍스트 앞에 확장된 이미지가 표시됩니다.]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Android %}

![메시지 텍스트 아래에 큰 이미지가 있는 Android 푸시 알림.]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
큰 이미지 알림은 최소 600 x 300 픽셀 이미지를 사용할 때 가장 잘 표시됩니다.
{% endalert %}

{% endtab %}
{% endtabs %}

### 동영상

미디어 라이브러리에 업로드된 동영상은 WhatsApp 메시지에서만 사용할 수 있습니다. 자세한 내용은 [WhatsApp 메시지 생성]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#outbound-messages)을 참조하세요.

## BrazeAI<sup>TM</sup>로 이미지 생성 {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
이 기능을 사용하기 전에 [데이터가 OpenAI에 어떻게 사용되고 전송되는지]({{site.baseurl}}/user_guide/brazeai/generative_ai/images/#ai-policy) 검토하세요.
{% endalert %}