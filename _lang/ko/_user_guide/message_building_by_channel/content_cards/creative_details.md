---
nav_title: 크리에이티브 디테일
article_title: 콘텐츠 카드의 크리에이티브 세부 정보
page_order: 1
description: "이 문서에서는 세 가지 표준 콘텐츠 카드 유형에 대한 이미지 크기 권장 사항 및 해지 동작과 같은 창의적인 세부 사항을 다룹니다."
channel:
  - content cards
tool: Media

---

# 콘텐츠 카드의 크리에이티브 세부 정보

> 콘텐츠 카드와 해당 카드가 위치한 피드를 사용자 지정하는 작업은 캠페인 생성 프로세스 중에는 수행할 수 없으며, 엔지니어 및 개발자와 협력하여 카드를 만들고 사용자 지정해야 합니다. 기술적인 자세한 내용은 [개발자 문서][7]]를 참조하세요.

## 콘텐츠 카드 유형

{% tabs %}
{% tab 클래식 %}

클래식 카드는 표준 메시징과 알림을 보내거나 아이콘으로 메시지를 시각적으로 분류하는 데 유용합니다. 이미지는 선택 사항이지만 1:1 비율이어야 합니다.

![권장 세부 정보가 포함된 클래식 카드 이미지와 클래식 카드 예시]({% image_buster /assets/img/content_card_classic.png %}){: style="max-width:45%;border:0;"}

| 카드 기능 | 세부 정보 |
| --- | ---|
| 헤더 텍스트 | 18px; 굵게 <br> 한 줄의 텍스트가 가장 이상적입니다. <br> 여기에서 Liquid를 사용하여 메시지를 맞춤 설정할 수 있습니다. |
| 메시지 텍스트 | 13px; 일반 무게 <br> 2~4줄의 텍스트가 가장 이상적입니다. <br> 여기에서 Liquid를 사용하여 메시지를 맞춤 설정할 수 있습니다. |
| 링크 텍스트 | 선택 사항입니다. <br> 13 px <br> 웹 페이지로 연결하거나 앱 내에서 딥링크로 연결합니다. |
| 이미지 | 선택 사항입니다. <br> 1:1 비율이어야 합니다. <br> 이미지 품질은 60 x 60 픽셀을 권장합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab 캡션 이미지 %}

캡션 이미지 카드는 대규모 세일이나 새로운 앱 기능과 같은 중요한 콘텐츠를 과시하고 관심을 끌 수 있는 좋은 방법입니다.

![권장 세부 정보가 포함된 캡션 이미지 카드 이미지 및 캡션 이미지 카드 예시]({% image_buster /assets/img/content_card_captioned.png %}){: style="max-width:90%;border:0;"}

| 카드 기능 | 세부 정보 |
| --- | ---|
| 헤더 텍스트 | 18px; 굵게 <br> 한 줄의 텍스트가 가장 이상적입니다. <br> 여기에서 Liquid를 사용하여 메시지를 맞춤 설정할 수 있습니다. |
| 메시지 텍스트 | 13px; 일반 무게 <br> 2~4줄의 텍스트가 가장 이상적입니다. <br> 여기에서 Liquid를 사용하여 메시지를 맞춤 설정할 수 있습니다. |
| 링크 텍스트 | 선택 사항입니다. <br> 13 px <br> 웹 페이지로 연결하거나 앱 내에서 딥링크로 연결합니다. |
| 이미지 | 4:3 비율을 권장합니다. <br> 최소 너비는 600 픽셀입니다.  <br> 고해상도 PNG, JPEG, GIF를 지원합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab 배너 %}

화려한 것을 원한다면 배너 카드가 적합합니다. 원하는 대로 완전히 맞춤 설정할 수 있습니다. 다른 곳에서 콘텐츠를 만들고 업로드하면 나만의 멋진 카드가 완성됩니다.

![권장 세부 정보가 포함된 배너 이미지 및 배너 예시]({% image_buster /assets/img/content_card_banner.png %}){: style="max-width:45%;border:0;"}

| 카드 기능 | 세부 정보 |
| --- | ---|
| 연결된 카드 | 선택 사항입니다. <br> 13 px <br> 온클릭 동작은 웹 페이지로 연결되는 링크 또는 앱 내 딥링크로 연결됩니다. |
| 이미지 | 모든 종횡비가 지원됩니다. <br> 최소 너비는 600 픽셀입니다.  <br> 고해상도 PNG, JPEG, GIF를 지원합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## 글로벌 크리에이티브 세부 정보 {#general}

콘텐츠 카드에는 처음부터 뛰어난 기능이 포함되어 있습니다. 현재로서는 Braze 계정에서 기본적으로 카드 스타일링을 할 수 없지만, 통합하는 동안 유형별 콘텐츠 카드와 콘텐츠 카드 피드에서 스타일링할 수 있습니다. 자세한 내용은 [콘텐츠 카드 커스텀하기][4]를 참조하세요.

### 해지 동작

사용자가 카드를 해지하려면 다음 스크린샷과 같이 모바일에서 스와이프하거나 `close X` 기능을 사용하면 됩니다. `x`는 웹 SDK의 경우에만 마우스를 가져가면 나타납니다.

![카드의 스와이프 또는 닫기 해지 동작을 보여주는 이미지][5]

사용자가 모든 카드를 삭제했거나 새 업데이트를 푸시하지 않은 경우, 사용자의 피드는 일반적으로 다음과 같이 표시됩니다.

![빈 콘텐츠 카드 피드 이미지][6]{: style="max-width:45%"}

{% alert tip %}
사용자가 관련 작업을 수행할 때 콘텐츠 카드가 해제되도록 설정하여 관련성을 유지하세요. 예를 들어, 사용자가 이미 구매한 제품에 대한 오퍼가 계속 표시되지 않도록 프로모션 콘텐츠 카드가 구매 즉시 해제되도록 설정할 수 있습니다.
{% endalert %}

### 콘텐츠 카드에서 GIF 사용

| Android용 콘텐츠 카드 | iOS용 콘텐츠 카드 | 웹용 콘텐츠 카드 |
| --- | --- |---|
| Android SDK는 기본적으로 애니메이션 GIF를 지원하지 않습니다. GIF 지원 활성화에 대한 자세한 내용은 [GIF]({{site.baseurl}}/developer_guide/content_cards/embedding_gifs/?sdktab=android)를 참조하세요. | Swift SDK는 기본적으로 애니메이션 GIF 지원을 제공하지 않습니다. GIF 지원 활성화에 대한 자세한 내용은 [GIF 지원 튜토리얼](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support)을 참조하세요. | GIF 지원은 웹 SDK 통합에 기본적으로 포함되어 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

<br><br>

[1]: {% image_buster /assets/img/content_card_classic.png %}
[2]: {% image_buster /assets/img/content_card_captioned.png %}
[3]: {% image_buster /assets/img/content_card_banner.png %}
[4]: {{site.baseurl}}/developer_guide/customization_guides/content_cards
[5]: {% image_buster /assets/img/dismissal-cc.png %}
[6]: {% image_buster /assets/img/empty-cc.png %}
[7]: {{site.baseurl}}/developer_guide/getting_started/customization_overview