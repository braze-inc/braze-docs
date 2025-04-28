---
nav_title: 항목 추천 사용
article_title: 메시징에서 항목 추천 사용
description: "이 도움말 문서에서는 메시지에서 항목 추천을 사용하는 방법에 대해 설명합니다."
page_order: 20
---

# 메시징에서 항목 추천 사용하기

> 추천이 학습된 후에는 Liquid를 사용하여 추천 항목을 가져와서 메시지에 표시할 수 있습니다. 여기서 핵심은 `product_recommendation` Liquid 객체로 직접 작업하는 것입니다. 이 문서에서는 `product_recommendation` Liquid 객체를 다루며 해당 지식을 실제로 적용하는 데 도움이 되는 튜토리얼이 포함되어 있습니다.

{% alert tip %}
이 문서에서는 Liquid 객체의 구문에 대해 자세히 설명합니다. 그러나 템플릿 텍스트 필드의 오른쪽 상단에 있는 **개인화 추가** 모달을 통해 기본값이 있는 [미리 서식이 지정된 변수를 삽입할]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#inserting-pre-formatted-variables) 수 있습니다.
{% endalert %}

Braze에서 AI 아이템 추천을 사용하는 방법에 대한 추가 지침은 [AI로 개인화된 경험 제작에 대한 Braze 학습 과정을][1] 참조하세요. 이 과정에서는 업계 사용 사례, 단계별 지침, AI 기반 추천이 포함된 인앱 메시지를 만들기 위한 추가 사용 사례를 다룹니다.

## 추천 개체의 해부학

`product_recommendation` 개체는 모델에서 권장하는 항목의 집합을 나타냅니다. 각 개체가 추천 항목을 나타내는 객체 배열로 구성된 관련 카탈로그에서 직접 데이터를 제공합니다.

- **구조:** 각 항목은 `items[index]` 으로 액세스되며, 인덱스는 0(첫 번째 항목의 경우)에서 시작하여 이후 항목에 대해 증가합니다.
- **카탈로그 필드:** 배열의 각 항목에는 카탈로그의 필드(열)에 해당하는 키-값 쌍이 포함되어 있습니다. 예를 들어 제품 추천을 위한 일반적인 카탈로그 필드에는 다음이 포함됩니다:
   - `name` 또는 `title`
   - `price`
   - `image_url`

## 리퀴드 태그

`product_recommendation` 개체에는 동적으로 생성된 제품 추천이 포함되어 있습니다. Liquid에서 이러한 데이터에 액세스하려면 메시지에서 데이터를 사용하기 전에 먼저 변수에 데이터를 할당해야 합니다.

### 추천 데이터 할당

항상 할당 태그로 시작하여 `product_recommendation` 데이터를 가져와 변수에 저장합니다.

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
```

{% endraw %}

- `RECOMMENDATION_NAME`: 이 이름을 Braze에서 생성한 AI 추천의 이름으로 바꿉니다.
- `items`: 추천 항목 배열을 저장하는 변수입니다.

### 개별 항목에 액세스

추천 데이터가 할당된 후에는 배열 인덱싱 및 점 표기법을 사용하여 특정 항목과 해당 필드를 참조할 수 있습니다:

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].name }} for {{ items[0].price }}
```

{% endraw %}

여러 항목을 포함하려면 각 항목을 인덱스로 개별적으로 참조하세요. `.name` 및 `.price` 카탈로그에서 해당 필드를 가져옵니다. 

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].name }} for {{ items[0].price }}
{{ items[1].name }} for {{ items[1].price }}
{{ items[2].name }} for {{ items[2].price }}
```

{% endraw %}

AI 추천은 여러 제품을 배열로 반환하며, 여기서 `items[0]` 은 첫 번째 항목, `items[1]` 은 두 번째 항목입니다. 권장 사항이 하나의 항목만 반환하는 경우 `items[1]` 을 참조하려고 하면 빈 필드가 표시됩니다.

## 이미지 추가

추천에 사용하는 카탈로그에 이미지 링크가 포함되어 있는 경우 메시지에서 해당 이미지를 참조할 수 있습니다. 

{% tabs %}

{% tab 드래그 앤 드롭 %}
이미지 필드가 있는 컴포저에서 컴포저의 해당 필드에 다음 액체를 추가합니다:

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].IMAGE_URL_FIELD }}
```

{% endraw %}

이메일 드래그 앤 드롭 편집기의 경우:

1. 이메일에 이미지 블록을 추가합니다.
2. 이미지 블록( **찾아보기** 버튼이 아닌)을 선택하여 **이미지 속성** 패널을 엽니다.
3. **Liquid로 이미지를** 켭니다. 
4. Liquid 스니펫을 **동적 URL** 필드에 붙여넣습니다.

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].IMAGE_URL_FIELD }}
```

{% endraw %}

![드래그 앤 드롭 편집기의 이미지 속성 패널]({% image_buster /assets/img/image_with_liquid.png %}){: style="max-width:60%"}

{:start="5"}

5. 미리 보기 및 테스트 이메일에 플레이스홀더 이미지를 포함하려면 **이미지 선택을** 눌러 미디어 라이브러리에서 플레이스홀더 이미지를 추가하거나 이미지가 호스팅되는 URL을 입력합니다.

{% endtab %}

{% tab HTML %}

HTML 이미지 참조의 경우 카탈로그의 이미지 URL 필드에 이미지 `src` 속성을 설정합니다. 제품 이름이나 설명과 같은 다른 필드를 대체 텍스트로 사용할 수 있습니다.

{% raw %}

```html
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
<img src="{{ items[0].IMAGE_URL_FIELD }}" alt="{{ items[0].name }}">
```

{% endraw %}

{% endtab %}

{% endtabs %}

-  `MY_RECOMMENDATION_NAME` 을 추천의 이름으로 바꿉니다.
- `IMAGE_URL_FIELD` 을 카탈로그에서 이미지 URL이 포함된 필드 이름으로 바꿉니다.


## Tutorial: 버려진 장바구니 이메일 생성

이 튜토리얼에서는 Braze AI 아이템 추천을 사용하여 사용자의 선호도나 행동에 따라 제품을 추천하는 동적 이메일을 만드는 방법에 대해 알아봅니다. 

여러분이 온라인 의류 소매업체 'Flash & Thread'의 마케터라고 가정해 보겠습니다. 장바구니에 상품을 남긴 고객의 재참여를 유도하고 추가 제품을 업셀링하고자 합니다. 버려진 항목과 개인화된 추천을 표시하는 이메일을 만드는 것이 목표입니다.

### 1단계: 카탈로그 준비

추천은 카탈로그에서 항목을 가져옵니다. 카탈로그 만들기 단계를 따릅니다. 카탈로그에 이러한 필드가 포함되어 있는지 확인하세요:

| 필드 | 데이터 유형 | 설명 |
| --- | --- | --- |
| ID | 문자열 | 카탈로그의 각 항목에 대한 고유 식별자 |
| 이름 | 문자열 | "스트라이프 니트 스웨터"와 같은 제품 이름입니다. |
| 가격 | 숫자 | 제품 가격은 '49.99'와 같이 표시됩니다. |
| image_url | 문자열 | 제품 이미지를 가리키는 URL입니다. HTTPS로 보안되어야 합니다. 이미지가 미디어 라이브러리에서 호스팅되는 경우 자산 위로 마우스를 가져가 URL을 복사합니다. |
| 카테고리 | 문자열 | "스웨터" 또는 "액세서리"와 같은 제품 카테고리입니다. |
| 색상 | 문자열 | "네이비/회색"과 같이 제품을 설명하는 색상입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


#### 카탈로그 예시

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>

<table class="tg">
  <tr>
    <th>ID</th>
    <th>이름</th>
    <th>가격</th>
    <th>image_url</th>
    <th>카테고리</th>
    <th>색상</th>
  </tr>
  <tr>
    <td>1001</td>
    <td>스트라이프 니트 스웨터</td>
    <td>49.99</td>
    <td>https://{{media_library}}/images/67a41294f5eac400685ce908/original.png?1738805908</td>
    <td>스웨터</td>
    <td>네이비/그레이</td>
  </tr>
  <tr>
    <td>1002</td>
    <td>커스텀 요트 클럽 슈즈</td>
    <td>79.99</td>
    <td>https://{{media_library}}/images/67a4136fe5a7660068bbe046/original.png?1738806127</td>
    <td>신발</td>
    <td>해군</td>
  </tr>
  <tr>
    <td>1003</td>
    <td>업무용 신발로 돌아가기</td>
    <td>89.99</td>
    <td>https://{{media_library}}/images/67a41370f542c1006798c26e/original.png?1738806128</td>
    <td>신발</td>
    <td>핑크/골드</td>
  </tr>
  <tr>
    <td>1004</td>
    <td>여름의 끝 모자</td>
    <td>29.99</td>
    <td>https://{{media_library}}/images/67a4136fbf6f620068511b67/original.png?1738806127</td>
    <td>액세서리</td>
    <td>화이트 플로럴</td>
  </tr>
</table>


### 2단계: 추천 설정

1. 카탈로그에서 **추천 생성을** 선택합니다.
2. AI 아이템 추천 만들기][3] 의 단계를 따르세요. 
3. 추천 유형은 **AI 개인화를** 선택합니다.
4. 방금 만든 카탈로그를 사용하여 추천을 학습시킵니다. 시간이 다소 걸릴 수 있으며 교육이 완료되면 이메일을 보내드립니다.

### 3단계: 이메일 만들기

추천이 교육을 마치면 메시징에 사용할 수 있습니다.

1. 끌어서 놓기 편집기로 이메일을 작성합니다.
2. 메시지 본문에서 카탈로그에서 추천을 가져올 위치에 이미지 블록을 추가합니다. 
3. 이미지 블록을 선택하고 **이미지 속성** 패널에서 **리퀴드가 포함된 이미지를** 켭니다. 
4. 이 Liquid 스니펫을 동적 URL 필드에 붙여넣습니다.


{% raw %}

```liquid
{% assign items = {{product_recommendation.${abandoned_cart}}} %}
{{ items[0].image_url }}
```

{% endraw %}

{: start="5"}

5. 이미지 아래에 단락 블록을 추가합니다. 여기에 제품 이름과 지원 세부 정보를 추가할 수 있습니다. 
6. 블록에 다음 리퀴드 스니펫을 붙여넣습니다. 이렇게 하면 카탈로그에서 첫 번째 추천의 이름, 카테고리, 색상 및 가격을 가져와 별도의 줄로 추가합니다. 

{% raw %}

```liquid
{% assign items = {{product_recommendation.${abandoned_cart}}} %}
{{ items[0].name }}
{{ items[0].category }}
{{ items[0].color }}
${{ items[0].price }}
```

{% endraw %}

{: start="7"}

7. 두 스니펫 모두에서 `abandoned_cart` 를 Braze에서 추천 이름으로 바꿉니다.
8. 항목 필드 이름(`{{ items[0].field_name }}`)이 카탈로그의 열 이름과 일치하는지 다시 확인합니다.
9. 블록을 반복할 때마다 배열을 하나씩 증가시켜 카탈로그에서 다음 추천 항목을 가져옵니다. 예를 들어, 배열이 `{{ items[0].name }}` 로 시작하므로 다음 항목은 `{{ items[1].name }}` 이 됩니다.

### 4단계: 메시지 미리보기

실제 사용자에게 메시지가 어떻게 표시되는지 확인합니다:

1. 편집기에서 **미리보기 및 테스트** 탭으로 이동합니다.
2. 드롭다운에서 **무작위 사용자를** 선택합니다.
3. **무작위 사용자 가져오기를** 선택하여 대상 그룹에서 사용자를 가져오고 해당 데이터와 함께 이메일이 어떻게 표시될지 미리 봅니다.

미리보기는 선택한 사용자에게 추천에 연결된 필수 속성 또는 이벤트 데이터가 있는 한 AI 추천을 포함하여 Liquid를 완전히 렌더링합니다.

추천이 미리 보기에 표시되지 않으면 다음을 확인하세요:

- 사용자가 추천 모델을 학습시킨 관련 제품 또는 이벤트와 상호 작용한 적이 있는 경우
- 추천 자체는 성공적으로 학습되었습니다.
- Liquid 코드가 올바른 권장 사항 및 필드를 올바르게 참조합니다.



[1]: https://learning.braze.com/ai-item-recommendations-use-case/1996254
[2]: {% image_buster /assets/img/image_with_liquid.png %}
[3]: {{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations#creating-an-ai-item-recommendation