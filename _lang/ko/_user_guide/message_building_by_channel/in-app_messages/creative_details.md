---
nav_title: 크리에이티브 세부 정보
article_title: 크리에이티브 디테일
page_order: 3.5
layout: dev_guide
guide_top_header: "크리에이티브 디테일"
guide_top_text: "인앱 메시지로 창의력을 발휘하기 전에 몇 가지 가이드라인을 숙지해야 합니다. 모든 인앱 메시지 템플릿은 최신 기기에서 다양한 길이의 텍스트와 이미지 크기를 표시하도록 설계되었습니다. 모든 휴대폰, 태블릿, 컴퓨터에서 메시징이 잘 표시되도록 하려면 다음 가이드라인을 따르고 시작하기 전에 항상 <a href='/docs/user_guide/message_building_by_channel/in-app_messages/testing/'>메시지를 테스트하는</a> 것이 좋습니다."
description: "이 랜딩 허브에서는 모달, 슬라이드업, 전체 화면의 세 가지 인앱 메시지 유형에 대한 디자인 및 콘텐츠 요구 사항을 다룹니다."

channel:
  - in-app messages
tools:
  - Media

guide_featured_title: "메시지 유형별 사양"

guide_featured_list:
- name: 모달
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/modal/
  image: /assets/img/braze_icons/layout-alt-01.svg
- name: 슬라이드업
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup/
  image: /assets/img/braze_icons/arrow-circle-broken-up.svg
- name: "전체 화면"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/
  image: /assets/img/braze_icons/expand-05.svg

---

## 콘텐츠 가이드라인

### 텍스트

인앱 메시지 본문 또는 헤더의 경우 헤더는 1~2줄, 본문은 최대 3줄로 짧고 간결하게 작성하는 것이 좋습니다. 세 줄이 지나면 메시지가 세로로 스크롤되어야 하며 사용자가 모든 콘텐츠에 참여하지 않을 수 있습니다. 스크롤을 트리거하는 임계값은 최종 사용자의 기기 크기, 커스텀 스타일 또는 메시지 내 이미지 유무에 따라 달라질 수 있지만 일반적으로 세 줄이면 안전합니다.

최신 세대의 인앱 메시지(3세대)를 사용하는 경우 글꼴이 iOS 및 Android용 운영 체제 기본값인 산세리프체로 기본 설정되어 있음을 알 수 있습니다. 웹 인앱 메시지는 기본값이 헬베티카로 설정됩니다.

### 이미지

이미지에 대한 가이드라인은 모든 기종과 크기의 휴대폰, 태블릿, 컴퓨터에서 메시징이 의도한 대로 아름답게 표시되도록 하기 위해 텍스트에 대한 가이드라인보다 더 체계적으로 구성되어 있습니다.

일반적으로 Braze는 16:10 화면에 맞는 이미지를 사용할 것을 권장합니다.

- **모든 이미지는 5MB 미만이어야 합니다.**
- PNG, JPEG, GIF 파일 형식만 허용됩니다.
- [미디어 라이브러리에]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) 이미지를 호스팅하여 오프라인 메시지 표시를 위해 Braze SDK가 CDN에서 자산을 다운로드할 수 있도록 하는 것이 좋습니다.
- 전체 화면 메시징의 경우 [이미지 안전 영역에]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/#image-safe-zone) 대한 가이드라인을 따르세요.

{% alert tip %} 자신 있게 자산을 생성하세요! 인앱 메시지 이미지 템플릿과 안전 영역 오버레이는 모든 크기의 기기에 잘 어울리도록 디자인되었습니다. [디자인 템플릿 ZIP 다운로드]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

{% tabs %}{% tab Fullscreen %}

앱 화면을 가득 채우는 전체화면 인앱 메시지. 전체 화면 메시지에는 큰 이미지, 헤더, 메시지 본문 및 두 개의 버튼이 포함됩니다.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

| 레이아웃 | 자산 규모 | 참고 |
|--- | --- | --- |
| 이미지 + 텍스트 | 6:5 종횡비<br>고해상도 1200 x 1000 픽셀<br> 최소 600 x 500 픽셀 | 모든 면에서 자르기가 발생할 수 있지만 이미지는 항상 뷰포트의 상단 50%를 채웁니다. |
| 이미지 전용 | 3:5 종횡비<br>고해상도 1200 x 2000 픽셀<br> 최소 600 x 1000 픽셀 | 키가 큰 기기의 경우 왼쪽과 오른쪽 가장자리에서 잘림 현상이 발생할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[전체 화면에 대한 자세한 내용]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen)


{% endtab %}
{% tab Modal %}

앱과 웹사이트 중앙에 대화 상자로 표시되는 모달 인앱 메시지. 모달에는 이미지, 헤더, 메시지 본문 및 두 개의 버튼이 포함됩니다.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

| 레이아웃 | 자산 규모 | 참고 |
|--- | --- | ------ |
| 이미지 + 텍스트 | 29:10 종횡비<br>고해상도 1450 x 500 픽셀<br> 최소 600 x 205 픽셀 | 세로 이미지의 크기가 축소되고 가로 중앙에 배치됩니다. 와이드 이미지는 왼쪽과 오른쪽 가장자리에서 잘립니다. |
| 이미지 전용 | 거의 모든 종횡비 지원<br>최대 1200 x 2000 픽셀의 고해상도<br> 최소 600 x 600 픽셀 | 메시징은 대부분의 종횡비 이미지에 맞게 크기가 조정됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[모달에 대한 자세한 내용]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/modal)

{% endtab %}
{% tab Slideup %}

앱 화면 하단에서 슬라이드업 인앱 메시지가 표시됩니다. 슬라이드업에는 아이콘 이미지와 간단한 메시지가 포함됩니다.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

| 레이아웃 | 자산 규모 | 참고 |
|--- | --- | --- |
| 이미지 + 텍스트 | 1:1 종횡비<br>고해상도 150 x 150 픽셀<br> 최소 50 x 50 픽셀 | 다양한 종횡비의 이미지를 잘리지 않고 정사각형 이미지 컨테이너에 넣을 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[슬라이드업에 대한 자세한 내용]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup)

{% endtab %}
{% endtabs %}

### GIF 및 동영상

현재 Braze는 원하는 플랫폼 통합 과정에서 인에이블먼트된 웹(포함), [Android]({{site.baseurl}}/developer_guide/in_app_messages/gifs/?sdktab=android) 및 iOS(포함) 인앱 메시징용 GIF를 지원합니다. 인앱 메시지 내 동영상에 대한 자세한 내용은 [커스텀 설명서를]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#video) 참조하세요.

## 추가 고려 사항

Braze 인앱 메시지는 글로벌 및 개별 크리에이티브 사양을 모두 갖추고 있습니다. 인앱 메시지를 완전히 커스텀하는 방법에 대한 자세한 내용은 [커스터마이징]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/) 페이지를 참조하세요.

<br>
