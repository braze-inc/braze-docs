---
nav_title: 카탈로그 사용
article_title: 카탈로그 사용
page_order: 1.5
description: "이 참고 문서에서는 Liquid를 통해 카탈로그를 사용하여 Braze 캠페인에서 비사용자 데이터를 참조하는 방법에 대해 설명합니다."
---

# 카탈로그 사용

> 카탈로그를 생성한 후에는 [Liquid를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) 통해 Braze 캠페인에서 비사용자 데이터를 참조할 수 있습니다. Liquid가 지원되는 드래그 앤 드롭 편집기의 어느 곳에서나 모든 메시징 채널에서 카탈로그를 사용할 수 있습니다.

## 메시징에서 카탈로그 사용

### 1단계: 개인화 유형 추가하기 {#step-one-personalization}

원하는 메시지 작성기에서 <i class="fas fa-plus-circle"></i> 더하기 아이콘을 선택하여 개인화 **추가** 모달을 열고 **개인화 유형으로** **카탈로그 항목을** 선택합니다. 그런 다음 **카탈로그 이름을** 선택합니다. 이전 예제를 사용하여 '게임' 카탈로그를 선택하겠습니다.

\![]({% image_buster /assets/img_archive/use_catalog_personalization.png %})

다음과 같은 Liquid 미리 보기를 즉시 확인할 수 있습니다:

{% raw %}
```liquid
{% catalog_items Games %}
```
{% endraw %}

### 2단계: 카탈로그 항목 선택

이제 카탈로그 항목을 추가할 차례입니다! 드롭다운을 사용하여 카탈로그 항목과 표시할 정보를 선택합니다. 이 정보는 카탈로그 생성에 사용되는 업로드한 CSV 파일의 열에 해당합니다.

예를 들어, 테일즈 게임의 제목과 가격을 참조하려면 카탈로그 항목으로 테일즈(1234)용 `id` 을 선택하고 `title` 및 `price` 을 요청하여 정보를 표시할 수 있습니다.

{% raw %}
```liquid
{% catalog_items Games 1234 %}
 
Get {{ items[0].title }} for just {{ items[0].price }}!
```
{% endraw %}

이렇게 하면 다음과 같이 렌더링됩니다:

> 테일즈를 단 7.49달러에 만나보세요!

## 카탈로그 내보내기

대시보드에서 카탈로그를 내보내는 방법에는 두 가지가 있습니다: 

- **카탈로그** 섹션에서 카탈로그 행 위로 마우스를 가져갑니다. 그런 다음 **카탈로그 내보내기** 버튼을 선택합니다.
- 카탈로그를 선택합니다. 그런 다음 카탈로그의 **미리 보기** 탭에서 카탈로그 **내보내기** 버튼을 선택합니다.

내보내기를 시작하면 CSV 파일을 다운로드할 수 있는 이메일이 전송됩니다. 이 파일을 검색하는 데 최대 4시간이 주어집니다.

## 추가 사용 사례

### 여러 항목

하나의 메시징에 하나의 항목만 넣을 수 있는 것은 아닙니다. **개인화 추가** 모달을 사용하여 한 번에 최대 3개의 카탈로그 항목을 추가할 수 있습니다. 메시지에 항목을 더 추가하려면 메시지 작성기에서 **개인화 추가를** 선택하고 표시할 추가 카탈로그 항목 및 정보를 선택합니다.

**카탈로그 항목에** 테일즈, 테슬라그라드, 아카라투스의 세 게임 `id` 을 추가하고 **표시할 정보에** `title` 을 선택한 이 예시를 확인하세요.

\![]({% image_buster /assets/img_archive/catalog_multiple_items.png %}){: style="max-width:70%" }

Liquid 주변에 텍스트를 추가하여 메시지를 더욱 개인화할 수 있습니다:

{% raw %}
```liquid
Get the ultimate trio {% catalog_items games 1234 1235 1236 %}
{{ items[0].title }}, {{ items[1].title }}, and {{ items[2].title }} today!
```
{% endraw %}

그러면 다음과 같이 반환됩니다:

```Get the ultimate trio Tales, Teslagrad, and Acaratus today!```

{% alert tip %}
[선택 항목을]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) 확인하여 데이터 그룹을 만들어 더욱 개인화된 메시징을 만들어 보세요!
{% endalert %}

### Liquid `if` 문 사용

카탈로그 항목을 사용하여 조건문을 만들 수 있습니다. 예를 들어 캠페인에서 특정 아이템이 선택되면 특정 메시지가 표시되도록 트리거할 수 있습니다.

이를 위해 이 예제에서와 같이 Liquid `if` 문을 사용합니다:

{% raw %}
```liquid
{% catalog_selection_items item-list selections %} 
{% if items[0].venue_name.size > 10 %}
Message if the venue name's size is more than 10 characters. 
{% elsif items[0].venue_name.size < 10 %}
Message if the venue name's size is less than 10 characters. 
{% else %} 
{% abort_message(no venue_name) %} 
{% endif %}
```
{% endraw %}

이 예에서는 커스텀 속성 `venue_name` 이 10자를 초과하거나 10자 미만인 경우 다른 메시징이 표시됩니다. `venue_name` 이 `blank` 인 경우 아무것도 표시되지 않습니다. 

`if` 문을 사용하기 전에 카탈로그 목록과 해당되는 경우 선택 항목을 선언해야 합니다. 이 예에서 `item-list` 은 카탈로그 목록이고 `selections` 은 선택 항목 이름입니다.

### 이미지 사용 {#using-images}

카탈로그의 이미지를 참조하여 메시징에 사용할 수도 있습니다. 이렇게 하려면 이미지의 경우 Liquid 필드에 `catalogs` 태그와 `item` 객체를 사용합니다.

예를 들어, 게임 카탈로그의 `image_link` 을 테일즈 프로모션 메시지에 추가하려면 **카탈로그 항목** 필드에 `id` 을 선택하고 **표시할 정보** 필드에 `image_link` 을 선택합니다. 이렇게 하면 이미지 필드에 다음과 같은 Liquid 태그가 추가됩니다:

{% raw %}
```liquid
{% catalog_items Games 1234 %}

{{ items[0].image_link }}
```
{% endraw %}

!!! 이미지 필드에 사용된 카탈로그 Liquid 태그가 있는 콘텐츠 카드 작성기입니다.]({% image_buster /assets/img_archive/catalog_image_link1.png %})

Liquid가 렌더링된 모습은 다음과 같습니다:

\![카탈로그 Liquid 태그가 렌더링된 콘텐츠 카드 예시.]({% image_buster /assets/img_archive/catalog_image_link2.png %}){: style="max-width:50%" }

### 카탈로그 항목 템플릿 지정

템플릿을 사용하여 커스텀 속성을 기반으로 카탈로그 항목을 동적으로 가져올 수도 있습니다. 예를 들어 사용자가 카탈로그의 게임 ID 배열을 포함하는 커스텀 속성 `wishlist` 을 가지고 있다고 가정해 보겠습니다.

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
카탈로그의 JSON 개체는 API를 통해서만 수집됩니다. CSV 파일을 사용하여 JSON 객체를 업로드할 수 없습니다.
{% endalert %}

Liquid 템플릿을 사용하면 위시리스트 ID를 동적으로 가져온 다음 메시징에 사용할 수 있습니다. 이렇게 하려면 커스텀 속성에 [변수를 할당하고]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables) **개인화 추가** 모달을 사용하여 배열에서 특정 항목을 가져옵니다. 카탈로그 항목 ID로 참조되는 변수는 `{{result}}` 와 같이 중괄호로 묶어야 올바르게 참조할 수 있습니다.

{% alert tip %}
배열은 `1` 이 아닌 `0` 에서 시작한다는 점을 기억하세요.
{% endalert %}

예를 들어, 사용자에게 테일즈(카탈로그에서 사용자가 원했던 아이템)가 세일 중임을 알리기 위해 메시지 작성기에 다음을 추가할 수 있습니다:

{% raw %}
```liquid
{% assign wishlist = {{custom_attribute.${wishlist}}}%}
{% catalog_items Games {{ wishlist[0] }} %}

Get {{ items[0].title }} now, for just {{ items[0].price }}!
```
{% endraw %}

다음과 같이 표시됩니다:
> 지금 테일즈를 단 7.49달러에 만나보세요!

템플릿을 사용하면 개별 커스텀 속성, 이벤트 속성정보 또는 기타 템플릿 가능한 필드를 기반으로 각 사용자별로 다른 카탈로그 항목을 렌더링할 수 있습니다.

### CSV 업로드하기

추가할 새 카탈로그 항목의 CSV를 업로드하거나 업데이트할 항목을 카탈로그화할 수 있습니다. 항목 목록을 삭제하려면 항목 ID의 CSV를 업로드하여 삭제할 수 있습니다.

### Liquid 사용

Liquid 로직을 사용하여 카탈로그를 수동으로 조합할 수도 있습니다. 그러나 존재하지 않는 ID를 입력해도 Braze는 오브젝트가 없는 오브젝트 배열을 반환한다는 점에 유의하세요. 배열의 크기를 확인하고 `if` 문을 사용하여 빈 배열 사례를 설명하는 등의 오류 처리를 포함할 것을 권장합니다.

{% alert note %}
Liquid는 현재 카탈로그 내에서 사용할 수 없습니다. Liquid 개인화가 카탈로그의 셀 안에 나열된 경우 동적 값은 렌더링되지 않고 실제 Liquid만 표시됩니다.
{% endalert %}

#### Liquid를 포함한 카탈로그 항목 템플릿화

[연결된 콘텐츠와]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) 마찬가지로 카탈로그 항목의 Liquid 콘텐츠를 렌더링하려면 Liquid 태그에 `:rerender` 플래그를 사용해야 합니다. `:rerender` 플래그는 한 단계 깊이에 불과하므로 중첩된 Liquid 태그 호출에는 적용되지 않는다는 점에 유의하세요.

카탈로그 항목에 고객 프로필 필드(Liquid 개인화 태그 내)가 포함된 경우 이러한 값을 메시지 앞부분과 템플릿 전에 Liquid에서 정의해야 Liquid를 올바르게 렌더링할 수 있습니다. `:rerender` 플래그가 제공되지 않으면 원시 Liquid 콘텐츠를 렌더링합니다.

예를 들어 '메시지'라는 이름의 카탈로그에 이 Liquid가 있는 항목이 있는 경우입니다:

\![]({% image_buster /assets/img_archive/catalog_liquid_templating.png %}){: style="max-width:80%;"}

다음 Liquid 콘텐츠를 렌더링합니다:

{% raw %}
```liquid
Hi ${first_name}

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
Catalog Liquid 태그는 카탈로그 내에서 재귀적으로 사용할 수 없습니다.
{% endalert %}


[1]: {% image_buster /assets/img_archive/use_catalog_personalization.png %}
[2]: {% image_buster /assets/img_archive/catalog_multiple_items.png %}
