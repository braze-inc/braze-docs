---
nav_title: 중첩 고객 속성
article_title: 중첩 고객 속성
alias: "/nested_custom_attribute_support/"
page_order: 1
page_type: reference
description: "이 참조 문서에서는 중첩 고객 속성을 커스텀 속성의 데이터 유형으로 사용하는 방법과 제한 사항 및 사용 예시를 다룹니다."
---

# 중첩 고객 속성

> 이 페이지에서는 한 속성 집합을 다른 속성의 속성으로 정의할 수 있는 중첩 고객 속성에 대해 설명합니다. 즉, 커스텀 속성 오브젝트를 정의할 때 해당 오브젝트에 대한 추가 속성 집합을 정의할 수 있습니다.

{% multi_lang_include nested_attribute_objects/about_nested_attributes.md %}

{% multi_lang_include nested_attribute_objects/supported_data_types.md %}

## 제한 사항

- 중첩된 고객 속성은 Braze 소프트웨어 개발 키트 또는 API를 통해 전송된 고객 속성을 위한 것입니다. 
- 개체의 최대 크기는 100KB입니다.
- 키 이름과 문자열 값의 크기 제한은 255자입니다.
- 키 이름에는 공백을 포함할 수 없습니다.
- 마침표(`.`)와 달러 기호(`$`)는 중첩된 고객 속성을 고객 프로필에 보내려는 경우 API 페이로드에서 지원되지 않는 문자입니다.
- 모든 Braze 파트너가 중첩 고객 속성을 지원하는 것은 아닙니다. 특정 파트너 통합에서 이 기능을 지원하는지 확인하려면 [파트너 설명서를]({{site.baseurl}}/partners/home) 참조하세요.
- 중첩된 고객 속성은 커넥티드 오디언스 API 호출 시 필터로 사용할 수 없습니다.

## API 예제

{% tabs local %}
{% tab Create %}
다음은 '가장 많이 재생한 노래' 개체가 있는 `/users/track` 예제입니다. 노래의 속성을 캡처하기 위해 `most_played_song` 을 객체로 나열하는 API 요청을 객체 속성 집합과 함께 전송합니다.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "genre": "Jazz",
        "play_analytics": {
            "count": 1000,
            "top_10_listeners": true
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab Update %}
기존 객체를 업데이트하려면 요청에 `_merge_objects` 매개 변수를 사용하여 `users/track` 으로 POST를 보내세요. 이렇게 하면 업데이트가 기존 개체 데이터와 딥 병합됩니다. 심층 병합은 개체의 모든 레벨이 첫 번째 레벨이 아닌 다른 개체에 병합되도록 합니다. 이 예제에서는 이미 Braze에 `most_played_song` 개체가 있으며, 이제 `most_played_song` 개체에 새 필드 `year_released` 를 추가하고 있습니다.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "most_played_song": {
          "year_released": 1960
      }
    }
  ]
}
```

이 요청이 수신되면 커스텀 속성 오브젝트는 이제 다음과 같이 표시됩니다:

```json
"most_played_song": {
  "song_name": "Solea",
  "artist_name" : "Miles Davis",
  "album_name": "Sketches of Spain",
  "year_released": 1960,
  "genre": "Jazz",
  "play_analytics": {
     "count": 1000,
     "top_10_listeners": true
  }
}
```

{% alert warning %}
`_merge_objects` 을 `true` 으로 설정하지 않으면 개체를 덮어쓰게 됩니다. `_merge_objects` 기본값은 `false` 입니다.
{% endalert %}

{% endtab %}
{% tab Delete %}
커스텀 속성 오브젝트를 삭제하려면 커스텀 속성 오브젝트를 `null` 으로 설정하여 `users/track` 으로 POST를 보내세요.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": null
    }
  ]
}
```

{% alert note %}
이 방법은 [오브젝트 배열]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects) 내부의 중첩된 키를 삭제하는 데는 사용할 수 없습니다.
{% endalert %}

{% endtab %}
{% endtabs %}

## 소프트웨어 개발 키트 예제

{% sdk_min_versions android:25.0.0 ios:6.1.0 web:4.7.0 %}

{% tabs local %}
{% tab Android SDK %}

**만들기**
```kotlin
val json = JSONObject()
    .put("song_name", "Solea")
    .put("artist_name", "Miles Davis")
    .put("album_name", "Sketches of Spain")
    .put("genre", "Jazz")
    .put(
        "play_analytics",
        JSONObject()
            .put("count", 1000)
            .put("top_10_listeners", true)
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("most_played_song", json)
}
```

**업데이트**
```kotlin
val json = JSONObject()
    .put("year_released", 1960)

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("most_played_song", json, true)
}
```

**삭제**
```kotlin
braze.getCurrentUser { user ->
    user.unsetCustomUserAttribute("most_played_song")
}
```

{% endtab %}
{% tab Swift SDK %}

**만들기**
```swift
let json: [String: Any?] = [
  "song_name": "Solea",
  "artist_name": "Miles Davis",
  "album_name": "Sketches of Spain",
  "genre": "Jazz",
  "play_analytics": [
    "count": 1000,
    "top_10_listeners": true,
  ],
]

braze.user.setCustomAttribute(key: "most_played_song", dictionary: json)
```

**업데이트**
```swift
let json: [String: Any?] = [
  "year_released": 1960
]

braze.user.setCustomAttribute(key: "most_played_song", dictionary: json, merge: true)
```

**삭제**
```swift
braze.user.unsetCustomAttribute(key: "most_played_song")
```

{% endtab %}
{% tab Web SDK %}

**만들기**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "song_name": "Solea",
  "artist_name": "Miles Davis",
  "album_name": "Sketches of Spain",
  "genre": "Jazz",
  "play_analytics": {
    "count": 1000,
    "top_10_listeners": true
  }
};
braze.getUser().setCustomUserAttribute("most_played_song", json);
```

**업데이트**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "year_released": 1960
};
braze.getUser().setCustomUserAttribute("most_played_song", json, true);

```

**삭제**
```javascript
import * as braze from "@braze/web-sdk";
braze.getUser().setCustomUserAttribute("most_played_song", null);
```

{% endtab %}
{% endtabs %}

## 개체 속성으로 날짜 캡처하기

날짜를 개체 속성으로 캡처하려면 `$time` 키를 사용해야 합니다. 다음 예제에서는 "중요 날짜" 개체를 사용하여 개체 속성 집합인 `birthday` 및 `wedding_anniversary` 을 캡처합니다. 이 날짜의 값은 `$time` 키가 있는 객체이며, null 값일 수 없습니다.

{% alert note %}
처음에 날짜를 개체 속성으로 캡처하지 않았다면 모든 사용자에 대해 `$time` 키를 사용하여 이 데이터를 다시 전송하는 것이 좋습니다. 그렇지 않으면 `$time` 속성을 사용할 때 불완전한 세그먼트가 발생할 수 있습니다. 그러나 중첩된 고객 속성의 `$time` 값이 올바르게 서식이 지정되지 않은 경우 중첩된 고객 속성 전체가 업데이트되지 않습니다.
{% endalert %}

```json
{
  "attributes": [ 
    {
      "external_id": "time_with_nca_test",
      "important_dates": {
        "birthday": {"$time" : "1980-01-01"},
        "wedding_anniversary": {"$time" : "2020-05-28"}
      }
    }
  ]
}
```

{% alert note %}
중첩된 고객 속성의 경우 연도가 0보다 작거나 3000보다 크면 Braze는 사용자에게 이러한 값을 저장하지 않습니다.
{% endalert %}

## Liquid 템플레이트

다음 Liquid 템플릿 예제는 이전 API 요청에서 저장된 커스텀 속성 오브젝트 속성을 참조하여 메시징에 사용하는 방법을 보여줍니다.

`custom_attribute` 개인화 태그와 점 표기법을 사용하여 개체의 속성에 액세스합니다. 오브젝트 이름(오브젝트 배열을 참조하는 경우 배열 내 위치)을 지정한 다음 점(마침표), 속성 이름을 지정합니다.

{% raw %}
`{{custom_attribute.${most_played_song}[0].artist_name}}` - "마일스 데이비스"
<br> `{{custom_attribute.${most_played_song}[0].song_name}}` - "Solea"
<br> `{{custom_attribute.${most_played_song}[0].play_analytics.count}}` - "1000"
{% endraw %}

Liquid를 사용하여 노래 이름과 청취자가 해당 노래를 재생한 횟수를 메시징에 템플릿으로 만들기]({% image_buster /assets/img_archive/nca_liquid_2.png %})

## 세그먼트 세분화

중첩된 고객 속성을 기반으로 세그먼트를 구축하여 사용자를 더욱 타겟팅할 수 있습니다. 이렇게 하려면 커스텀 속성 오브젝트를 기준으로 세그먼트를 필터링한 다음 세그먼트화할 속성 이름과 관련 값의 경로를 지정합니다. 해당 경로가 어떻게 생겼는지 잘 모르겠다면 [스키마를 생성하고](#generate-schema) 중첩된 개체 탐색기를 사용하여 Braze가 해당 경로를 채우도록 할 수 있습니다.

속성에 경로를 추가한 후 **유효성** 검사를 선택하여 경로 필드의 값이 유효한지 확인합니다.

\![청취자가 지정된 횟수 이상 노래를 재생한 경우 가장 많이 재생한 노래 커스텀 속성을 기준으로 필터링하기]({% image_buster /assets/img_archive/nca_segmentation_2.png %})

중첩 고객 속성으로 세그먼트화하려면 중첩 **고객** 속성 필터를 선택하여 특정 중첩 고객 속성을 선택할 수 있는 드롭다운을 표시합니다.

\![]({% image_buster /assets/img_archive/nested_custom_attributes.png %}){: style="max-width:70%;"}

중첩된 고객 속성 세그먼트로 작업할 때 데이터 유형별로 그룹화된 새로운 비교기에 액세스할 수 있습니다. 예를 들어 `play_analytics.count` 는 숫자이므로 **숫자** 카테고리에서 비교기를 선택할 수 있습니다.

\![중첩된 고객 속성의 데이터 유형에 따라 연산자를 선택하는 사용자]({% image_buster /assets/img_archive/nca_comparator.png %})

### 시간 데이터 유형에 대한 필터링

중첩된 시간 커스텀 속성을 필터링할 때 날짜 값을 비교할 때 **연도** 또는 **시간** 카테고리 아래의 연산자를 사용하여 필터링하도록 선택할 수 있습니다. 

**연도** 카테고리에서 연산자를 선택하면 중첩된 고객 속성 값의 전체 타임스탬프 대신 월과 일만 비교를 위해 확인됩니다. **시간** 카테고리에서 연산자를 선택하면 연도를 포함한 전체 타임스탬프가 비교됩니다.

### 다중 기준 세그먼트 세분화

**다중 기준 세분화를** 사용하여 단일 개체 내에서 여러 기준과 일치하는 세그먼트를 만들 수 있습니다. 이렇게 하면 지정된 모든 기준과 일치하는 오브젝트 배열이 하나 이상 있는 사용자에게 세그먼트에 대한 자격이 부여됩니다. 예를 들어, 사용자는 키가 비어 있지 않고 숫자가 0보다 큰 경우에만 이 세그먼트와 일치합니다.

**세그먼트에 대한 Liquid 복사** 기능을 사용하여 이 세그먼트에 대한 Liquid 코드를 생성하고 이를 메시지에서 사용할 수도 있습니다. 예를 들어, 계정 오브젝트 배열과 과세 대상 계정이 활성화된 고객을 타겟팅하는 세그먼트가 있다고 가정해 보겠습니다. 고객이 활성 및 과세 대상 계정 중 하나와 연결된 계정 목표에 기여하도록 하려면 고객을 넛지하는 메시지를 만들 수 있습니다. 

다중 기준 세분화 확인란이 선택된 예시 세그먼트입니다.]({% image_buster /assets/img_archive/nca_multi_criteria.png %})

**세그먼트에 대해 Copy Liquid를** 선택하면 Braze는 활성 상태이고 과세 대상인 계정만 포함된 오브젝트 배열을 반환하는 Liquid 코드를 자동으로 생성합니다.

{% raw %}

```
{% assign segmented_nested_objects = '' | split: '' %}
{% assign obj_array = {{custom_attribute.${accounts}}} %}
{% for obj in obj_array %}
  {% if obj["account_type"] == 'taxable' and obj["active"] == true %}
    {% assign segmented_nested_objects = obj_array | slice: forloop.index0 | concat: segmented_nested_objects | reverse %}
  {% endif %}
{% endfor %}
```

여기에서 `segmented_nested_objects` 을 사용하여 메시지를 개인화할 수 있습니다. 이 예에서는 첫 번째 활성 과세 대상 계정에서 목표를 가져와서 개인화하려고 합니다:

```
Get to your {{segmented_nested_objects[0].goal}} goal faster, make a deposit using our new fast deposit feature!
```

{% endraw %}

그러면 고객에게 다음과 같은 메시지가 반환됩니다: "은퇴 목표를 더 빨리 달성하고 새로운 빠른 입금 기능을 사용하여 입금하세요!"

### 중첩된 개체 탐색기를 사용하여 스키마 생성하기 {#generate-schema}

중첩된 개체 경로를 외울 필요 없이 개체에 대한 스키마를 생성하여 세그먼트 필터를 구축할 수 있습니다. 이렇게 하려면 다음 단계를 수행하세요.

#### 1단계: 스키마 생성

이 예제에서는 방금 Braze로 전송한 `accounts` 오브젝트 배열이 있다고 가정합니다:

```json
"accounts": [
  {"type": "taxable",
  "balance": 22500,
  "active": true},
  {"type": "non-taxable",
  "balance": 0,
  "active": true},
 ]
```

Braze 대시보드에서 **데이터 설정** > 커스텀 속성으로 이동합니다.

오브젝트 또는 오브젝트 배열을 검색합니다. **속성 이름** 열에서 **스키마 생성을** 선택합니다.

\![]({% image_buster /assets/img_archive/nca_generate_schema.png %})

{% alert tip %}
전송한 데이터의 양에 따라 스키마가 생성되는 데 몇 분 정도 걸릴 수 있습니다.
{% endalert %}

스키마가 생성되면 **스키마 생성** 버튼 대신 <i class="fas fa-plus"></i> 더하기 버튼이 새로 나타납니다. 클릭하면 이 중첩된 고객 속성에 대해 Braze가 알고 있는 내용을 확인할 수 있습니다. 

스키마 생성 중에 Braze는 이전에 전송된 데이터를 살펴보고 이 속성에 대한 데이터의 이상적인 표현을 구축합니다. Braze는 중첩된 값에 대한 데이터 유형도 분석하여 추가합니다. 이는 주어진 중첩 속성에 대해 Braze로 전송된 이전 데이터를 샘플링하여 수행됩니다.

`accounts` 오브젝트 배열의 경우, 오브젝트 배열 내에 다음을 포함하는 오브젝트가 있는 것을 볼 수 있습니다:

- 키가 `active` 인 부울 유형 (계정의 활성 여부에 관계없이)
- 키가 `balance` (계정의 잔액)인 숫자 유형입니다.
- 키가 `type` (비과세 또는 과세 계정)인 문자열 유형입니다.

\![]({% image_buster /assets/img_archive/nca_schema.png %}){: style="max-width:50%" }

이제 데이터를 분석하고 데이터 표현을 구축했으니 세그먼트를 구축해 보겠습니다.

#### 2단계: 세그먼트 구축하기

잔액이 100 미만인 고객을 타겟팅하여 입금을 유도하는 메시지를 보내도록 하겠습니다.

세그먼트를 만들고 필터를 추가합니다 `Nested Custom Attribute`, 그런 다음 오브젝트 또는 오브젝트 배열을 검색하고 선택합니다. 여기에 `accounts` 오브젝트 배열을 추가했습니다. 

\![]({% image_buster /assets/img_archive/nca_segment_schema.png %})

경로 필드에서 <i class="fas fa-plus"></i> 더하기 버튼을 선택합니다. 그러면 오브젝트 또는 오브젝트 배열의 표현이 나타납니다. 나열된 항목 중 하나를 선택하면 Braze가 경로 필드에 해당 항목을 삽입합니다. 이 예제에서는 균형을 맞춰야 합니다. 잔액을 선택하면 경로(이 경우 `[].balance`)가 경로 필드에 자동으로 채워집니다.

\![]({% image_buster /assets/img_archive/nca_segment_schema2.png %}){: style="max-width:70%" }

**유효성** 검사를 선택하여 경로 필드의 콘텐츠가 유효한지 확인한 다음 필요에 따라 나머지 필터를 구축할 수 있습니다. 여기서는 잔액이 100 미만이어야 한다고 지정했습니다.

\![]({% image_buster /assets/img_archive/nca_segment_schema_3.png %})

그거예요! 데이터 구조에 대해 알 필요 없이 중첩된 고객 속성을 사용하여 세그먼트를 만들 수 있습니다. Braze의 중첩된 개체 탐색기는 데이터의 시각적 표현을 생성하고 세그먼트 생성에 필요한 것을 정확하게 탐색하고 선택할 수 있게 해줍니다.

### 중첩된 고객 속성 변경 트리거하기

중첩된 고객 속성 오브젝트가 변경될 때 트리거할 수 있습니다. 이 옵션은 오브젝트 배열을 변경하는 데 사용할 수 없습니다. 경로 탐색기를 볼 수 있는 옵션이 표시되지 않으면 스키마를 생성했는지 확인하세요. 

\![]({% image_buster /assets/img_archive/nca_triggered_changes2.png %})

예를 들어, 다음 액션 기반 캠페인에서 **커스텀 속성 값 변경에** 대한 새 트리거 동작을 추가하여 동네 사무실 기본 설정을 변경한 사용자를 타겟팅할 수 있습니다. 

\![]({% image_buster /assets/img_archive/nca_triggered_changes.png %})

### 개인화

**개인화 추가** 모달을 사용하여 메시징에 중첩된 고객 속성을 삽입할 수도 있습니다. 개인화 유형으로 **중첩 고객 속성을** 선택합니다. 다음으로 최상위 속성 및 속성 키를 선택합니다. 

예를 들어 아래 개인화 모달에서는 사용자의 기본 설정에 따라 지역 동네 사무실의 중첩된 고객 속성을 삽입합니다.

\![]({% image_buster /assets/img_archive/nca_personalization.png %}){: style="max-width:70%" }

{% alert tip %}
중첩된 고객 속성을 삽입하는 옵션이 표시되지 않으면 스키마가 생성되었는지 확인하세요.
{% endalert %}

### 스키마 재생성 {#regenerate-schema}

스키마가 생성된 후에는 24시간에 한 번씩 재생성할 수 있습니다. 이 섹션에서는 스키마를 다시 생성하는 방법에 대해 설명합니다. 스키마에 대한 자세한 내용은 이 문서에서 [스키마 생성에](#generate-schema) 대한 섹션을 참조하세요.

중첩된 고객 속성에 대한 스키마를 다시 생성하려면 다음과 같이 하세요:

1. **데이터 설정** > 커스텀 속성으로 이동합니다.
2. 중첩된 고객 속성을 검색합니다.
3. 속성의 속성 **이름** 열에서 <i class="fas fa-plus"></i> 을 선택하여 스키마를 관리합니다.
4. 모달이 나타납니다. **스키마 재생성을** 선택합니다.

스키마가 마지막으로 재생성된 후 24시간이 지나지 않은 경우 스키마 재생성 옵션이 비활성화됩니다. 스키마를 다시 생성하면 새 객체만 감지되며 현재 스키마에 존재하는 객체는 삭제되지 않습니다.

{% alert important %}
기존 오브젝트가 있는 오브젝트 배열의 스키마를 재설정하려면 새 커스텀 속성을 만들어야 합니다. 스키마 재생성은 기존 개체를 삭제하지 않습니다.
{% endalert %}

스키마를 다시 생성한 후 데이터가 예상대로 나타나지 않는다면 속성이 충분히 자주 수집되지 않았을 수 있습니다. 사용자 데이터는 주어진 중첩 속성에 대해 Braze로 전송된 이전 데이터에서 샘플링됩니다. 속성이 충분히 수집되지 않으면 스키마에서 해당 속성이 선택되지 않습니다.

## 데이터 포인트

전송되는 모든 키는 데이터 포인트를 소비합니다. 예를 들어, 고객 프로필에서 초기화된 이 개체는 7개의 데이터 포인트로 계산됩니다:

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "year_released": 1960,
        "genre": "Jazz",
        "play_analytics": {
          "count": 1000,
          "top_10_listeners": true
        }
      }
    }
  ]
}
```

{% alert note %}
커스텀 속성 오브젝트를 `null` 로 업데이트하면 데이터 포인트도 소모됩니다.
{% endalert %}

