---
nav_title: 권장 사항 사용
article_title: 메시징에서 항목 추천 사용
description: "이 도움말 문서에서는 메시징에서 항목 추천을 사용하는 방법에 대해 설명합니다."
page_order: 1.2
---

# 메시징에 항목 추천 사용하기

> 추천이 학습된 후에는 Liquid를 사용하여 `product_recommendation` Liquid 객체로 직접 작업하여 메시징에 추천 항목을 가져와 표시할 수 있습니다.

{% alert tip %}
단계별 안내는 Braze 학습 과정을 확인하세요: [AI로 개인화된 경험 제작](https://learning.braze.com/ai-item-recommendations-use-case/1996254).
{% endalert %}

## 전제 조건

메시징에 추천 기능을 사용하려면 먼저 [추천 엔진을 만들고 훈련시켜야]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/) 합니다. 교육은 10분에서 36시간까지 소요될 수 있으며, 교육이 완료되거나 오류가 발생하면 이메일을 받게 됩니다.

## 메시징에 권장 사항 사용하기

### 1단계: Liquid 코드 추가하기

제품 추천 교육이 완료된 후에는 Liquid로 메시지를 개인화하여 해당 카탈로그에서 가장 인기 있는 제품을 삽입할 수 있습니다.

{% tabs local %}
{% tab pre-formatted code %}
개인화 유형으로 항목 추천이 있는 '개인화 추가' 모달을 클릭합니다.]({% image_buster /assets/img/add_personalization.png %}){: style="max-width:30%;float:right;margin-left:15px;"}

메시지 작성기의 **개인화 추가** 섹션에서 Liquid를 생성할 수 있습니다:

1. 개인화를 지원하는 모든 메시지 작성기에서 다음을 선택합니다. <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="개인화 추가하기"></i> 을 선택하여 개인화 창을 엽니다.
2. **개인화 유형에서** **항목 추천을** 선택합니다.
3. **항목 권장 사항 이름에서** 방금 만든 권장 사항을 선택합니다.
4. **예측 항목 수에** 삽입할 상위 제품 수를 입력합니다. 예를 들어 가장 많이 구매한 상위 3개 항목을 표시할 수 있습니다.
5. **표시할 정보의** 경우 카탈로그에서 각 항목에 포함할 필드를 선택합니다. 각 항목에 대한 이러한 필드의 값은 이 권장 사항과 관련된 카탈로그에서 가져옵니다.
6. **복사** 아이콘을 선택하고 메시지에서 필요한 위치에 Liquid를 붙여넣습니다.
{% endtab %}

{% tab custom code %}
카탈로그의 `product_recommendation` 오브젝트를 참조하여 커스텀 Liquid 코드를 작성할 수 있습니다. 여기에는 해당 카탈로그에 대해 동적으로 생성된 모든 제품 추천 데이터가 포함되며, 각 개체가 추천 항목을 담당하는 오브젝트 배열로 구성됩니다.

|사양|세부 정보|
|-------------|-------|
|**구조**|각 항목은 `items[index]` 으로 액세스되며, 인덱스는 0(첫 번째 항목의 경우)에서 시작하여 이후 항목에 대해 증가합니다.|
|**카탈로그 필드**|배열의 각 항목에는 카탈로그의 필드(열)에 해당하는 키-값 쌍이 포함되어 있습니다. 예를 들어 제품 추천을 위한 일반적인 카탈로그 필드에는 다음이 포함됩니다:<br>- `name` 또는 `title`<br>- `price`<br>- `image_url`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

`assign` 태그를 사용하여 `product_recommendation` 데이터를 가져와 변수에 할당합니다.

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
```
{% endraw %}

다음을 교체합니다:

|입력 안내|설명|
|-----------|-----------|
|`recommendation_name`|Braze에서 생성한 AI 추천의 이름입니다.|
|`items`|추천 항목 배열을 저장하는 변수입니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

다음으로 배열 인덱싱 및 점 표기법을 사용하여 특정 항목과 해당 필드를 참조합니다:

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].name }} for {{ items[0].price }}
```
{% endraw %}

여러 항목을 포함하려면 각 항목을 인덱스로 개별적으로 참조하세요. `.name` 및 `.price` 카탈로그에서 해당 필드를 가져옵니다. 

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].name }} for {{ items[0].price }}
{{ items[1].name }} for {{ items[1].price }}
{{ items[2].name }} for {{ items[2].price }}
```
{% endraw %}

AI 추천은 여러 제품을 배열로 반환하는데, `items[0]` 이 첫 번째 항목이고 `items[1]` 이 두 번째 항목입니다. 추천이 하나의 항목만 반환하는 경우 `items[1]` 을 참조하려고 하면 비어 있는 필드가 표시됩니다.
{% endtab %}
{% endtabs %}

### 2단계: 이미지 참조(선택 사항)

추천 카탈로그에 이미지 링크가 포함되어 있는 경우 메시징에서 이를 참조할 수 있습니다. 

{% tabs %}
{% tab Drag-and-drop%}
이메일 드래그 앤 드롭 편집기에서 이메일에 이미지 블록을 추가한 다음 이미지 블록을 선택하여 **이미지 속성을** 엽니다.

드래그 앤 드롭 편집기의 이미지 속성 패널]({% image_buster /assets/img/image_with_liquid.png %}){: style="max-width:45%"}

**Liquid로 이미지를** 토글한 다음 **동적 URL** 필드에 다음을 추가합니다:

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].image_url_field }}
```
{% endraw %}

다음을 교체합니다:

|입력 안내|설명|
|-----------|-----------|
|`recommendation_name`|추천의 이름입니다.|
|`image_url_field`|카탈로그에서 이미지 URL이 포함된 필드의 이름입니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

미리보기 및 테스트 이메일에 플레이스홀더 이미지를 포함하려면 **이미지 선택을** 선택한 다음 미디어 라이브러리에서 이미지를 선택하거나 호스팅 사이트에서 이미지의 URL을 입력합니다.
{% endtab %}

{% tab HTML %}
HTML 이미지 참조의 경우 카탈로그의 이미지 URL 필드에 이미지 `src` 속성을 설정합니다. 제품 이름이나 설명과 같은 다른 필드를 대체 텍스트로 사용할 수 있습니다.

{% raw %}
```html
{% assign items = {{product_recommendation.${recommendation_name}}} %}
<img src="{{ items[0].image_url_field }}" alt="{{ items[0].name }}">
```
{% endraw %}

다음을 교체합니다:

|입력 안내|설명|
|-----------|-----------|
|`recommendation_name`|추천의 이름입니다.|
|`image_url_field`|카탈로그에서 이미지 URL이 포함된 필드의 이름입니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}
