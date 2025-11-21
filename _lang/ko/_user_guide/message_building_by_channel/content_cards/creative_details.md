---
nav_title: 크리에이티브 세부 정보
article_title: 콘텐츠 카드용 크리에이티브 세부 정보
page_order: 1
description: "이 문서에서는 세 가지 표준 콘텐츠 카드 유형에 대한 이미지 크기 권장 사항 및 해제 동작과 같은 크리에이티브 세부 사항을 다룹니다."
channel:
  - content cards
tool: Media

---

# 콘텐츠 카드용 크리에이티브 세부 정보

> 콘텐츠 카드와 콘텐츠 카드가 위치한 피드를 커스터마이징하는 작업은 캠페인 생성 과정에서 수행할 수 없으며, 엔지니어링 및 개발자와 협력하여 카드를 구축하고 커스터마이징해야 합니다. 기술적인 자세한 내용은 [개발자 설명서를]({{site.baseurl}}/developer_guide/getting_started/customization_overview) 참조하세요.

## 콘텐츠 카드 유형

{% tabs %}
{% tab Classic %}

클래식 카드는 표준 메시징 및 알림을 표시하거나 아이콘으로 메시지를 시각적으로 분류하는 데 유용합니다. 이미지는 선택 사항이지만 1:1 비율이어야 합니다.

추천 세부 정보가 포함된 클래식 카드 이미지 및 클래식 카드 예시]({% image_buster /assets/img/content_card_classic.png %}){: style="max-width:45%;border:0;"}

| 카드 기능 | 세부 정보 |
| --- | ---|
| 헤더 텍스트 | 18px; 굵게 <br> 한 줄의 텍스트가 가장 이상적입니다. <br> 여기에서 Liquid를 사용하여 메시지를 개인화할 수 있습니다. |
| 메시지 텍스트 | 13px; 일반 무게 <br> 2~4줄의 텍스트가 가장 이상적입니다. <br> 여기에서 Liquid를 사용하여 메시지를 개인화할 수 있습니다. |
| 링크 텍스트 | 선택 사항입니다. <br> 13픽셀 <br> 웹 페이지로 링크하거나 앱 내에서 딥링킹합니다. |
| 이미지 | 선택 사항입니다. <br> 1:1 비율이어야 합니다. <br> 이미지 품질은 60 x 60 픽셀을 권장합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Captioned Image %}

자막 콘텐츠 카드는 큰 세일이나 새로운 앱 기능과 같은 중요한 콘텐츠를 자랑하고 관심을 끌 수 있는 좋은 방법입니다.

추천 세부 정보가 포함된 캡션 이미지 카드 이미지 및 캡션 이미지 카드 예시]({% image_buster /assets/img/content_card_captioned.png %}){: style="max-width:90%;border:0;"}

| 카드 기능 | 세부 정보 |
| --- | ---|
| 헤더 텍스트 | 18px; 굵게 <br> 한 줄의 텍스트가 가장 이상적입니다. <br> 여기에서 Liquid를 사용하여 메시지를 개인화할 수 있습니다. |
| 메시지 텍스트 | 13px; 일반 무게 <br> 2~4줄의 텍스트가 가장 이상적입니다. <br> 여기에서 Liquid를 사용하여 메시지를 개인화할 수 있습니다. |
| 링크 텍스트 | 선택 사항입니다. <br> 13픽셀 <br> 웹 페이지로 링크하거나 앱 내에서 딥링킹합니다. |
| 이미지 | 4:3 비율을 권장합니다. <br> 최소 너비는 600 픽셀입니다.  <br> 고해상도 PNG, JPEG, GIF를 지원합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Image-only %}

보다 창의적인 제어를 원한다면 이미지 전용 카드가 적합합니다. 원하는 도구를 사용하여 이미지를 만들고 이 카드 유형에 이미지를 업로드합니다.

추천 세부 정보가 포함된 이미지 전용 콘텐츠 카드 이미지 및 이미지 전용 예시]({% image_buster /assets/img/content_card_banner.png %}){: style="max-width:45%;border:0;"}

| 카드 기능 | 세부 정보 |
| --- | ---|
| 연결된 카드 | 선택 사항입니다. <br> 13픽셀 <br> 온클릭 동작은 웹 페이지로 연결되는 링크 또는 앱 내 딥링킹으로 연결됩니다. |
| 이미지 | 모든 종횡비를 지원합니다. <br> 최소 너비는 600 픽셀입니다.  <br> 고해상도 PNG, JPEG, GIF를 지원합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## 글로벌 크리에이티브 세부 정보 {#general}

콘텐츠 카드는 처음부터 뛰어난 기능을 갖추고 있습니다. 현재로서는 Braze 계정에서 기본적으로 카드 스타일링을 할 수 없지만, 통합 중에 유형별 콘텐츠 카드와 콘텐츠 카드 피드에서 스타일링할 수 있습니다. 자세한 내용은 [콘텐츠 카드 커스텀하기를]({{site.baseurl}}/developer_guide/content_cards/) 참조하세요.

### 해고 행동

사용자가 카드를 방출하려면 다음 스크린샷과 같이 모바일에서 카드를 스와이프하거나 `close X` 기능을 사용할 수 있습니다. 웹 소프트웨어 개발 키트에 대해서만 마우스를 가져가면 `x` 이 표시됩니다.

\![카드의 스와이프 또는 닫기 방출 동작을 보여주는 이미지]({% image_buster /assets/img/dismissal-cc.png %})

사용자가 모든 카드를 해제했거나 새 업데이트를 푸시하지 않은 경우 사용자의 피드는 일반적으로 다음과 같이 표시됩니다:

\![빈 콘텐츠 카드 피드 이미지]({% image_buster /assets/img/empty-cc.png %}){: style="max-width:45%"}

{% alert tip %}
사용자가 관련 작업을 수행할 때 콘텐츠 카드가 해제되도록 설정하여 관련성을 유지하세요. 예를 들어, 사용자가 이미 구매한 제품에 대한 오퍼가 계속 표시되지 않도록 사용자가 구매하는 즉시 프로모션 콘텐츠 카드가 해제되도록 설정할 수 있습니다.
{% endalert %}

### 콘텐츠 카드에서 GIF 사용

| Android용 콘텐츠 카드 | iOS용 콘텐츠 카드 | 웹용 콘텐츠 카드 |
| --- | --- |---|
| Android 소프트웨어 개발 키트는 기본값으로 애니메이션 GIF를 지원하지 않습니다. GIF 지원 활성화에 대한 자세한 내용은 [GIF를]({{site.baseurl}}/developer_guide/content_cards/embedding_gifs/?sdktab=android) 참조하세요. | Swift 소프트웨어 개발 키트는 기본값으로 애니메이션 GIF를 지원하지 않습니다. GIF 지원 활성화에 대한 자세한 내용은 [GIF 지원 튜토리얼을](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support) 참조하세요. | GIF 지원은 웹 SDK 통합에 기본값으로 포함되어 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

<br><br>

