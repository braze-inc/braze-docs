---
nav_title: 카탈로그 사용
article_title: 카탈로그 사용
page_order: 1.5
description: "이 참조 문서에서는 카탈로그를 사용하여 Liquid를 통해 Braze 캠페인에서 비사용자 데이터를 참조하는 방법을 설명합니다."
---

# 카탈로그 사용

> 카탈로그를 생성한 후, [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid)를 통해 Braze 캠페인에서 비사용자 데이터를 참조할 수 있습니다. Liquid가 지원되는 드래그 앤 드롭 편집기의 어느 곳에서나 모든 메시징 채널에서 카탈로그를 사용할 수 있습니다.

## 메시지에서 카탈로그 사용

### 1단계: 개인화 유형 추가 {#step-one-personalization}

선택한 메시지 작성기에서 <i class="fas fa-plus-circle"></i> 더하기 아이콘을 선택하여 **개인화 추가** 모달을 열고 **개인화 유형**으로 **카탈로그 항목**을 선택합니다. 그런 다음 카탈로그 이름을 선택합니다. 이전 예제를 사용하여 "Games" 카탈로그를 선택하겠습니다.

![]({% image_buster /assets/img_archive/use_catalog_personalization.png %})

다음과 같은 Liquid 미리보기를 즉시 확인할 수 있습니다:

{% raw %}
```liquid
{% catalog_items Games %}
```
{% endraw %}

### 2단계: 카탈로그 항목 선택

이제 카탈로그 항목을 추가할 차례입니다! 드롭다운을 사용하여 카탈로그 항목과 표시할 정보를 선택합니다. 이 정보는 카탈로그 생성에 사용된 업로드한 CSV 파일의 열에 해당합니다.

예를 들어, Tales 게임의 제목과 가격을 참조하려면 카탈로그 항목으로 Tales의 `id`(1234)를 선택하고 표시할 정보로 `title` 및 `price`를 요청할 수 있습니다.

{% raw %}
```liquid
{% catalog_items Games 1234 %}
 
Get {{ items[0].title }} for just {{ items[0].price }}!
```
{% endraw %}

이렇게 하면 다음과 같이 렌더링됩니다:

> Get Tales for just 7.49!

## 카탈로그 내보내기

대시보드에서 카탈로그를 내보내는 방법에는 두 가지가 있습니다: 

- **카탈로그** 섹션에서 카탈로그 행 위로 마우스를 가져갑니다. 그런 다음 **카탈로그 내보내기** 버튼을 선택합니다.
- 카탈로그를 선택합니다. 그런 다음 카탈로그의 **미리보기** 탭에서 **카탈로그 내보내기** 버튼을 선택합니다.

내보내기를 시작하면 CSV 파일을 다운로드할 수 있는 이메일이 전송됩니다. 이 파일은 최대 4시간 이내에 다운로드할 수 있습니다.

## 추가 활용 사례

### 다중 항목

메시지에 항목 하나로 제한되지 않습니다. **개인화 추가** 모달을 사용하여 한 번에 최대 세 개의 카탈로그 항목을 추가할 수 있습니다. 더 추가하려면 작성기에서 **개인화 추가**를 다시 선택하고 추가 카탈로그 항목 및 표시할 정보를 선택합니다.

이 예제에서는 **카탈로그 항목**에 세 가지 게임인 Tales, Teslagrad, Acaratus의 `id`를 추가하고 **표시할 정보**에 `title`을 선택합니다.

![]({% image_buster /assets/img_archive/catalog_multiple_items.png %}){: style="max-width:70%" }

Liquid 주변에 텍스트를 추가하여 메시지를 더욱 개인화할 수 있습니다:

{% raw %}
```liquid
Get the ultimate trio {% catalog_items Games 1234 1235 1236 %}
{{ items[0].title }}, {{ items[1].title }}, and {{ items[2].title }} today!
```
{% endraw %}

그러면 다음과 같이 반환됩니다:

```Get the ultimate trio Tales, Teslagrad, and Acaratus today!```

{% alert tip %}
Check out [selections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) to create groups of data for more personalized messaging!
{% endalert %}

### Using Liquid `if` statements

You can use catalog items to create conditional statements. For example, you can trigger a certain message to display when a specific item is selected in your campaign. You must declare the catalog (and, if applicable, the selection) before referencing `items` in an `if` statement.

#### With catalog items

{% raw %}
```liquid
{% catalog_items Games 1234 %}
{% if items[0].on_sale == true %}
  {{ items[0].title }} is on sale! Get it for {{ items[0].price }}.
{% else %}
  Check out {{ items[0].title }} at full price.
{% endif %}
```
{% endraw %}

이 예제에서 `catalog_items` 태그는 `Games` 카탈로그에서 항목 `1234`를 가져오고, `if` 문은 `on_sale` 필드를 확인하여 다른 메시지를 표시합니다.

#### 카탈로그 선택 항목 사용

{% raw %}
```liquid
{% catalog_selection_items item-list selections %} 
{% if items[0].venue_name.size > 10 %}
Message if the venue name's size is more than 10 characters. 
{% elsif items[0].venue_name.size <= 10 %}
Message if the venue name's size is 10 characters or fewer. 
{% else %} 
{% abort_message('no venue_name') %} 
{% endif %}
```
{% endraw %}

이 예제에서는 `venue_name` 필드의 문자 수가 10자보다 많은지 적은지에 따라 다른 메시지가 표시됩니다. `venue_name`이 비어 있으면 메시지가 중단됩니다.

{% alert tip %}
Liquid 구문 오류를 방지하려면 메시지 작성기에서 **+** 더하기 버튼을 선택하여 카탈로그 Liquid 태그를 자동으로 삽입하세요.
{% endalert %}

### 이미지 사용 {#using-images}

카탈로그에서 이미지를 참조하여 메시징에 사용할 수도 있습니다. 이렇게 하려면 이미지의 Liquid 필드에서 `catalogs` 태그와 `item` 오브젝트를 사용합니다.

예를 들어, Games 카탈로그의 `image_link`를 Tales 프로모션 메시지에 추가하려면 **카탈로그 항목** 필드에 `id`를 선택하고 **표시할 정보** 필드에 `image_link`를 선택합니다. 이렇게 하면 이미지 필드에 다음 Liquid 태그가 추가됩니다:

{% raw %}
```liquid
{% catalog_items Games 1234 %}

{{ items[0].image_link }}
```
{% endraw %}

![이미지 필드에 카탈로그 Liquid 태그가 사용된 콘텐츠 카드 작성기.]({% image_buster /assets/img_archive/catalog_image_link1.png %})

Liquid가 렌더링되었을 때의 모습은 다음과 같습니다:

![카탈로그 Liquid 태그가 렌더링된 콘텐츠 카드 예시.]({% image_buster /assets/img_archive/catalog_image_link2.png %}){: style="max-width:50%" }

### 카탈로그 항목 템플릿 지정

템플릿을 사용하여 커스텀 속성을 기반으로 카탈로그 항목을 동적으로 가져올 수도 있습니다. 예를 들어 사용자가 카탈로그의 게임 ID 배열을 포함하는 커스텀 속성 `wishlist`를 가지고 있다고 가정해 보겠습니다.

```json
{
    "attributes": [
        {
            "external_id": "user_id",
            "wishlist": ["1234", "1235"]
        }
    ]
}
```

{% alert note %}
카탈로그의 JSON 오브젝트는 API를 통해서만 수집됩니다. CSV 파일을 사용하여 JSON 오브젝트를 업로드할 수 없습니다.
{% endalert %}

Liquid 템플릿을 사용하면 위시리스트 ID를 동적으로 가져와서 메시지에서 사용할 수 있습니다. 이렇게 하려면 커스텀 속성에 [변수를 할당]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables)한 다음 **개인화 추가** 모달을 사용하여 배열에서 특정 항목을 가져옵니다. 카탈로그 항목 ID로 참조되는 변수는 올바르게 참조되려면 중괄호로 감싸야 합니다(예: `{{result}}`).

{% alert tip %}
배열은 `1`이 아닌 `0`에서 시작한다는 점을 기억하세요.
{% endalert %}

예를 들어, 사용자에게 Tales(카탈로그에서 사용자가 위시리스트에 추가한 항목)가 세일 중임을 알리기 위해 메시지 작성기에 다음을 추가할 수 있습니다:

{% raw %}
```liquid
{% assign wishlist = {{custom_attribute.${wishlist}}}%}
{% catalog_items Games {{ wishlist[0] }} %}

Get {{ items[0].title }} now for {{ items[0].price }}!
```
{% endraw %}

다음과 같이 표시됩니다:
> Get Tales now for just 7.49!

템플릿을 사용하면 개별 커스텀 속성, 이벤트 속성정보 또는 기타 템플릿 가능한 필드에 따라 각 사용자마다 다른 카탈로그 항목을 렌더링할 수 있습니다.

### CSV 업로드

추가할 새 카탈로그 항목이나 업데이트할 카탈로그 항목의 CSV를 업로드할 수 있습니다. 항목 목록을 삭제하려면 항목 ID의 CSV를 업로드하여 삭제할 수 있습니다.

### Liquid 사용

Liquid 로직을 사용하여 카탈로그를 수동으로 구성할 수도 있습니다. 그러나 존재하지 않는 ID를 입력해도 Braze는 여전히 오브젝트가 없는 항목 배열을 반환한다는 점에 유의하세요. 배열의 크기를 확인하고 `if` 문을 사용하여 빈 배열의 경우를 처리하는 등의 오류 처리를 포함하는 것을 권장합니다.

#### Liquid를 포함한 카탈로그 항목 템플릿

[연결된 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content)와 유사하게, 카탈로그 항목의 Liquid 콘텐츠를 렌더링하려면 Liquid 태그에서 `:rerender` 플래그를 사용해야 합니다. `:rerender` 플래그는 한 단계 깊이에만 적용되므로 중첩된 Liquid 태그 호출에는 적용되지 않는다는 점에 유의하세요.

카탈로그 항목에 고객 프로필 필드가 포함되어 있는 경우(Liquid 개인화 태그 내), Liquid를 올바르게 렌더링하기 위해 이러한 값은 메시지에서 템플릿 지정 이전에 Liquid에서 먼저 정의되어야 합니다. `:rerender` 플래그가 제공되지 않으면 원시 Liquid 콘텐츠가 렌더링됩니다.

예를 들어 "Messages"라는 이름의 카탈로그에 이 Liquid가 있는 항목이 있는 경우:

![]({% image_buster /assets/img_archive/catalog_liquid_templating.png %}){: style="max-width:80%;"}

다음 Liquid 콘텐츠를 렌더링하려면:

{% raw %}
```liquid
Hi ${first_name},

{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

다음과 같이 표시됩니다:

{% raw %}
```
Hi Peter,

Welcome to our store, Peter!
```
{% endraw %}

{% alert note %}
카탈로그 Liquid 태그는 카탈로그 내에서 재귀적으로 사용할 수 없습니다.
{% endalert %}

## 카탈로그 데이터 구조화

카탈로그 데이터를 구조화하는 방법을 계획할 때, 의도한 사용 사례에서 시작하여 그에 맞게 카탈로그를 설계하세요. 카탈로그의 각 행은 하나의 항목(고유한 `id` 포함)을 나타냅니다. 열에는 URL, 설명 텍스트, 이미지 URL, 가격, 평점, 크기 또는 색상 등 해당 항목의 속성이 포함되어야 합니다.

### 표준 카탈로그 호출을 사용해야 하는 경우

표준 카탈로그 호출에서는 `id` 열에 대해 값을 매칭합니다. 커스텀 속성 또는 이벤트 속성정보(ID 문자열)를 카탈로그 Liquid 태그에 삽입하면 단일 항목에 대한 여러 속성을 메시지에 가져올 수 있습니다. 일반적인 사용 사례는 다음과 같습니다:

- 최근 조회한 제품 또는 서비스
- 위시리스트 항목
- 위치별 거래
- 구매한 제품
- 라이프사이클 단계 콘텐츠
- 가장 최근 검색한 제품 또는 서비스

### 카탈로그 선택 항목을 사용해야 하는 경우

[카탈로그 선택 항목]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/)을 사용하면 카탈로그의 모든 열에 대해 필터링하고 최대 50개의 일치하는 항목을 반환할 수 있습니다. 선택 항목 필터에 커스텀 속성 또는 이벤트 속성정보를 삽입하면 각 사용자에 맞게 결과가 개인화됩니다. 일반적인 사용 사례는 다음과 같습니다:

- 카테고리가 사용자의 선호도와 일치하는 항목
- 사용자가 선호하는 브랜드, 요리 또는 크기와 일치하는 항목
- 구독 유형 또는 로열티 등급 콘텐츠
- 사용자의 평균 주문 금액 범위 내의 제품

핵심 차이점은 표준 카탈로그 호출은 `id`로 알려진 단일 항목을 조회하는 반면, 카탈로그 선택 항목은 카탈로그 전체를 쿼리하여 필터 기준에 일치하는 여러 항목을 반환한다는 것입니다.

[1]: {% image_buster /assets/img_archive/use_catalog_personalization.png %}
[2]: {% image_buster /assets/img_archive/catalog_multiple_items.png %}