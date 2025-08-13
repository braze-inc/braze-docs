---
nav_title: 창의적인 세부 사항
article_title: 창의적인 세부 사항
page_order: 3.5
layout: dev_guide
guide_top_header: "창의적인 세부 사항"
guide_top_text: "창의적인 인앱 메시지를 작성하기 전에 몇 가지 지침을 알아두어야 합니다. 모든 인앱 메시지 템플릿은 최신 기기에서 다양한 길이의 텍스트와 크기의 이미지를 표시하도록 설계되었습니다. 모든 휴대폰, 태블릿 및 컴퓨터에서 메시지가 잘 표시되도록 하려면 이러한 지침을 따르고 항상 <a href='/docs/user_guide/message_building_by_channel/in-app_messages/testing/'>메시지</a>를 테스트하는 것이 좋습니다."
description: "이 랜딩 허브는 세 가지 유형의 인앱 메시지, 모달, 슬라이드업 및 전체 화면에 대한 디자인 및 콘텐츠 요구 사항을 다룹니다."

channel:
  - in-app messages
tools:
  - Media

guide_featured_title: "메시지 유형별 사양"

guide_featured_list:
- name: Modal
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/modal/
  image: /assets/img/braze_icons/layout-alt-01.svg
- name: 슬라이드업
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup/
  image: /assets/img/braze_icons/arrow-circle-broken-up.svg
- name: "전체 화면"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/
  image: /assets/img/braze_icons/expand-05.svg

---

## 콘텐츠 지침

### 텍스트

인앱 메시지 본문 또는 헤더의 경우, 짧고 간결하게 유지하는 것이 좋습니다. 헤더는 한두 줄, 본문은 최대 세 줄로 작성하세요. 세 줄 후에는 메시지가 세로로 스크롤해야 할 가능성이 있으며, 사용자가 모든 콘텐츠와 상호작용하지 않을 수 있습니다. 스크롤을 트리거하는 임계값은 최종사용자의 기기 크기, 커스텀 스타일 또는 메시지 내 이미지의 존재 여부에 따라 달라질 수 있지만, 일반적으로 세 줄이 안전합니다.

최신 세대의 인앱 메시지(Generation 3)를 사용 중이라면, 글꼴이 iOS 및 Android의 운영 체제 기본 Sans Serif로 기본 설정된다는 것을 알 수 있습니다. 웹 인앱 메시지는 기본값으로 헬베티카를 사용합니다.

### 이미지

우리의 이미지 가이드라인은 텍스트 가이드라인보다 더 체계적입니다. 모든 모델과 크기의 전화기, 태블릿, 컴퓨터에서 메시지가 의도한 대로 아름답게 표시되도록 하기 위함입니다.

일반적으로 Braze는 16:10 화면에 맞는 이미지를 사용할 것을 권장합니다.

- **모든 이미지는 5MB 미만이어야 합니다.**
- PNG, JPEG 및 GIF 파일 형식만 허용합니다.
- 이미지를 [미디어 라이브러리]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/)에 호스팅하여 Braze SDK가 오프라인 메시지 표시를 위해 CDN에서 에셋을 다운로드할 수 있도록 권장합니다.
- 전체 화면 메시지의 경우 [이미지 안전 영역]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/#image-safe-zone)에 대한 지침을 따르십시오.

{% alert tip %} 자신감을 가지고 자산을 만드세요! Braze 인앱 메시지 이미지 템플릿과 안전 영역 오버레이는 모든 크기의 기기와 잘 어울리도록 설계되었습니다. [디자인 템플릿 ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %} 다운로드

{% tabs %}{% tab 전체 화면 %}

![앱 화면을 차지하는 전체 화면 인앱 메시지. 전체 화면 메시지에는 큰 이미지, 헤더, 메시지 본문 및 두 개의 버튼이 포함됩니다.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

| 레이아웃 | 애셋 크기 | 참고 |
|--- | --- | --- |
| 이미지 + 텍스트 | 6:5 종횡비<br>고해상도 1200 x 1000 픽셀<br> 최소 600 x 500 픽셀 | 크로핑은 모든 면에서 발생할 수 있지만, 이미지는 항상 뷰포트의 상위 50%를 채웁니다 |
| 이미지만 | 3:5 종횡비<br>고해상도 1200 x 2000 픽셀<br> 최소 600 x 1000 픽셀 | 키가 큰 기기에서는 왼쪽과 오른쪽 가장자리에서 잘림 현상이 발생할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[전체 화면에 대한 추가 세부정보]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen)


{% endtab %}
{% tab 모달 %}

![앱 및 웹사이트의 중앙에 대화 상자로 표시되는 모달 인앱 메시지. 모달에는 이미지, 헤더, 메시지 본문 및 두 개의 버튼이 포함되어 있습니다.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

| 레이아웃 | 애셋 크기 | 참고 |
|--- | --- | ------ |
| 이미지 + 텍스트 | 29:10 종횡비<br>고해상도 1450 x 500 픽셀<br> 최소 600 x 205 픽셀 | 긴 이미지는 축소되어 가로로 가운데에 배치됩니다. 넓은 이미지는 왼쪽과 오른쪽 가장자리가 잘립니다. |
| 이미지만 | 거의 모든 종횡비<br>고해상도 최대 1200 x 2000 픽셀<br> 최소 600 x 600 픽셀 | 메시지는 대부분의 가로 세로 비율에 맞게 이미지 크기를 조정합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[추가 세부 사항]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/modal)

{% endtab %}
{% tab 슬라이드업 %}

![앱 화면 하단에서 슬라이드업 인앱 메시지가 나타납니다. 슬라이드업에는 아이콘 이미지와 간단한 메시지가 포함됩니다.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

| 레이아웃 | 애셋 크기 | 참고 |
|--- | --- | --- |
| 이미지 + 텍스트 | 1:1 화면비<br>고해상도 150 x 150 픽셀<br> 최소 50 x 50 픽셀 | 다양한 가로 세로 비율의 이미지가 잘리지 않고 정사각형 이미지 컨테이너에 들어갑니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[슬라이드업 추가 세부 사항]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup)

{% endtab %}
{% endtabs %}

### GIF 및 비디오

Braze currently supports GIFs for Web (included), [Android]({{site.baseurl}}/developer_guide/in_app_messages/gifs/?sdktab=android), and iOS (included) in-app messaging, given that it has been enabled during the desired platform integration. 인앱 메시지의 비디오에 대한 자세한 내용은 [맞춤 설명서]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#video)를 참조하세요.

## 추가 고려 사항

Braze 인앱 메시지는 글로벌 및 개별 크리에이티브 사양을 모두 가지고 있습니다. For more information about fully customizing in-app messages, go to our [Customization]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/) page.

<br>
