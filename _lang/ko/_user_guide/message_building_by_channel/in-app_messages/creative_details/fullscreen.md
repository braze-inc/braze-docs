---
nav_title: "전체 화면"
article_title: 전체 화면 인앱 메시지
description: "이 참조 문서에서는 전체 화면 인앱 메시지의 메시지 및 디자인 요구 사항을 다룹니다."
page_type: reference
page_order: 0
channel:
  - in-app messages
tool:
  - Media

---

# 전체 화면 인앱 메시지

> 전체 화면 메시지는 디바이스의 전체 화면을 차지합니다! 이 메시지 유형은 필수 앱 업데이트와 같이 사용자의 주의가 정말 필요한 경우에 유용합니다.

{% tabs %}
{% tab 인물 사진 %}

![세로 방향으로 나란히 표시되는 두 개의 전체 화면 인앱 메시지에 이미지와 텍스트 권장 사항이 자세히 설명되어 있습니다. 자세한 내용은 다음 섹션을 참조하세요.]({% image_buster /assets/img/full-screen-spec.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab 가로 %}

![가로 방향으로 나란히 표시되는 두 개의 전체 화면 인앱 메시지에서 이미지와 텍스트 추천을 자세히 설명합니다. 자세한 내용은 다음 섹션을 참조하세요.]({% image_buster /assets/img/full-screen-spec-landscape.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}

## 이미지

전체 화면 인앱 메시지는 기기의 전체 높이를 채우고 필요에 따라 가로(왼쪽 및 오른쪽)로 잘립니다. 이미지 및 텍스트 전체화면 메시지는 기기 높이의 50%를 채웁니다. 모든 전체 화면 인앱 메시지는 "노치형" 기기의 상태 표시줄을 채웁니다.

- 모든 이미지는 5MB 미만이어야 합니다.
- PNG, JPEG, [GIF]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs#gifs) 파일 형식만 허용됩니다.
- 이미지 크기는 500KB를 권장합니다.

{% alert tip %} 자신 있게 에셋을 제작하세요! 인앱 메시지 이미지 템플릿과 안전 영역 오버레이는 모든 크기의 디바이스에 잘 어울리도록 디자인되었습니다. [디자인 템플릿 ZIP 다운로드]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

### 세로

| 레이아웃 | 자산 크기 | 참고 |
|--- | --- | --- |
| 이미지 및 텍스트 | 6:5 화면비<br> 고해상도 1200 x 1000 픽셀<br> 최소 600 x 500 픽셀 | 크로핑은 모든 면에서 발생할 수 있지만, 이미지는 항상 뷰포트의 상위 50%를 채웁니다 |
| 이미지만 | 3:5 화면비<br> 고해상도 1200 x 2000 픽셀<br> 최소 600 x 1000 픽셀 | 키가 큰 기기에서는 왼쪽과 오른쪽 가장자리에서 잘림 현상이 발생할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 가로

| 레이아웃 | 자산 크기 | 참고 |
|--- | --- | --- |
| 이미지 및 텍스트 | 10:3 화면비<br> 고해상도 2000 x 600px<br> 최소 1000 x 300 픽셀 | 크로핑은 모든 면에서 발생할 수 있지만, 이미지는 항상 뷰포트의 상위 50%를 채웁니다 |
| 이미지만 | 5:3 화면비<br> 고해상도 2000 x 1200px<br> 최소 1000 x 600 픽셀 | 키가 큰 기기에서는 왼쪽과 오른쪽 가장자리에서 잘림 현상이 발생할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 이미지 안전 영역

Braze 플랫폼에서 전체 화면 인앱 메시지를 미리 볼 때, 여러 기기에 표시될 때 잘리지 않도록 메시지 영역에 이미지 안전지대를 활성화할 수 있습니다. 미리보기 창에서 이미지 안전 영역을 테스트하는 것 외에도 항상 [메시지를 테스트]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/)하는 것이 좋습니다.

!["이미지 안전 영역 표시"를 활성화한 상태에서 Braze에서 인앱 메시지 미리보기. The image safe zone is an overlay over the image that visualizes what parts of the image will be safe from cropping.]({% image_buster /assets/img/image-safe-zone-full-screen-in-app-message.png %})

## 더 큰 화면

태블릿 또는 데스크톱 브라우저에서는 다음 스크린샷과 같이 앱 화면 중앙에 전체 화면 인앱 메시지가 표시됩니다.

{% tabs %}
{% tab 인물 사진 %}

![세로 방향으로 큰 화면에 표시되는 전체 화면 인앱 메시지입니다. 메시지는 화면 중앙에 큰 모달로 표시됩니다.]({% image_buster /assets/img/full-screen-large-viewport.png %}){: style="border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab 가로 %}

![가로 방향으로 큰 화면에 표시되는 것처럼 인앱 메시지를 전체 화면으로 표시합니다. 메시지는 화면 중앙에 큰 모달로 표시됩니다.]({% image_buster /assets/img/full-screen-large-viewport-landscape.png %}){: style="max-width:80%;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}

