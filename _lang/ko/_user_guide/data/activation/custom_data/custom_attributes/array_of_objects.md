---
nav_title: 객체 배열
article_title: 객체 배열
alias: "/array_of_objects/"
page_order: 0
page_type: reference
description: "이 참조 문서에서는 사용자 정의 속성을 위한 데이터 유형으로 객체 배열을 사용하는 방법, 제한 사항 및 사용 예제를 다룹니다." 
---

# 객체 배열

> 이 페이지에서는 관련 속성을 그룹화하기 위해 객체 배열을 사용하는 방법을 다룹니다. 예를 들어, 한 사용자에게 속하는 애완동물 객체, 노래 객체 및 계정 객체 그룹이 있을 수 있습니다. 이 객체 배열은 Liquid를 사용하여 메시지를 개인화하거나 객체 내의 어떤 요소가 기준과 일치하는 경우 청중 세그먼트를 생성하는 데 사용할 수 있습니다.

{% multi_lang_include nested_attribute_objects/supported_data_types.md %}

## 제한 사항

- 객체 배열은 API를 통해 전송되는 사용자 정의 속성을 위해 설계되었습니다. CSV 업로드는 지원되지 않습니다. 이는 CSV 파일의 쉼표가 열 구분 기호로 해석되며, 값의 쉼표가 구문 분석 오류를 일으킬 수 있기 때문입니다. 
- 객체 배열은 항목 수에 제한이 없지만 최대 크기는 100 KB입니다.
- 모든 Braze 파트너가 객체 배열을 지원하는 것은 아닙니다. 이 통합이 이 기능을 지원하는지 확인하려면 [파트너 문서]({{site.baseurl}}/partners/home)를 참조하십시오.

배열에서 항목을 업데이트하거나 제거하려면 키와 값으로 항목을 식별해야 하므로 배열의 각 항목에 대한 고유 식별자를 포함하는 것을 고려하십시오. 고유성은 배열에만 국한되며, 배열에서 특정 객체를 업데이트하고 제거하려는 경우 유용합니다. 이는 Braze에 의해 강제되지 않습니다.

{% alert tip %}
사용자 속성 객체에 대한 객체 배열 사용에 대한 자세한 내용은 [사용자 속성 객체]({{site.baseurl}}/api/objects_filters/user_attributes_object)를 참조하십시오.
{% endalert %}

## API 예제

{% tabs local %}
{% tab Create %}

다음은 `/users/track` 예제와 `pets` 배열입니다. 애완동물의 속성을 캡처하려면 `pets`을(를) 객체 배열로 나열하는 API 요청을 보내십시오. 각 객체에는 나중에 업데이트할 때 참조할 수 있는 고유한 `id`가 할당되어 있습니다.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Gus"
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Gerald"
        }
      ]
    }
  ]
}
```
{% endtab %}
{% tab Add %}

`$add` 연산자를 사용하여 배열에 다른 항목을 추가하십시오. 다음 예제는 사용자의 `pets` 배열에 세 개의 애완동물 객체를 추가하는 방법을 보여줍니다.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$add": [
          {
            "id": 3,
            "type": "dog",
            "breed": "corgi",
            "name": "Doug"
          },
          {
            "id": 4,
            "type": "fish",
            "breed": "salmon",
            "name": "Larry"
          },
           {
            "id": 5,
            "type": "bird",
            "breed": "parakeet",
            "name": "Mary"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% tab Update %}

`_merge_objects` 매개변수와 `$update` 연산자를 사용하여 배열 내 특정 객체의 값을 업데이트하십시오. 단순 [중첩 사용자 정의 속성]({{site.baseurl}}/nested_custom_attribute_support/#api-request-body) 객체에 대한 업데이트와 유사하게, 이는 깊은 병합을 수행합니다.

`$update`은(는) 배열 내 객체에서 중첩 속성을 제거하는 데 사용할 수 없습니다. 이를 수행하려면 배열에서 전체 항목을 제거한 다음 특정 키 없이 객체를 추가해야 합니다( `$remove`와 `$add`의 조합 사용).

다음 예제는 `4`의 `id`을(를) 가진 객체에 대해 `breed` 속성을 `goldfish`로 업데이트하는 방법을 보여줍니다. 이 요청 예제는 `id`가 `5`인 객체를 `Annette`의 새로운 `name`으로 업데이트합니다. `_merge_objects` 매개변수가 `true`으로 설정되어 있으므로 이 두 객체의 다른 모든 필드는 동일하게 유지됩니다.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "pets": {
        "$update": [
          {
            "$identifier_key": "id",
            "$identifier_value": 4,
            "$new_object": {
              "breed": "goldfish"
            }
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 5,
            "$new_object": {
              "name": "Annette"
            }
          }
        ]
      }
    }
  ]
}
```

{% alert warning %}
`_merge_objects`를 true로 설정해야 하며, 그렇지 않으면 객체가 덮어쓰여집니다. 기본적으로 `_merge_objects`은 false입니다.
{% endalert %}

{% endtab %}
{% tab Remove %}

일치하는 키(`$identifier_key`) 및 값(`$identifier_value`)과 결합하여 `$remove` 연산자를 사용하여 배열에서 객체를 제거하십시오.

다음 예제는 `pets` 배열에서 `id`의 값이 `1`인 객체, `id`의 값이 `2`인 객체, `type`의 값이 `dog`인 객체를 제거하는 방법을 보여줍니다. `dog` 값이 `type`인 객체가 여러 개 있는 경우 모든 일치하는 객체가 제거됩니다.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$remove": [
          // Remove by ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Remove any dog
          {
            "$identifier_key": "type",
            "$identifier_value": "dog"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

### 타임스탬프

객체 배열에 타임스탬프와 같은 필드를 포함할 때는 일반 문자열이나 유닉스 에포크 정수 대신 `$time` 형식을 사용하십시오.

```json
{
  "attributes": [
    {
      "external_id": "user123",
      "purchases": [
        {
          "item_name": "T-shirt",
          "price": 19.99,
          "purchase_time": {
            "$time": "2020-05-28"
          }
        }
      ]
    }
  ]
}
```

{% alert tip %}
자세한 내용은 [중첩 사용자 정의 속성]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support)을(를) 참조하십시오.
{% endalert %}

## SDK 예제

{% tabs local %}
{% tab Android SDK %}
{% subtabs %}
{% subtab Create %}
```kotlin
val json = JSONArray()
    .put(JSONObject()
        .put("id", 1)
        .put("type", "dog")
        .put("breed", "beagle")
        .put("name", "Gus"))
    .put(JSONObject()
        .put("id", 2)
        .put("type", "cat")
        .put("breed", "calico")
        .put("name", "Gerald")
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json)
}
```
{% endsubtab %}

{% subtab Add %}
```kotlin
val json = JSONObject()
    .put("\$add", JSONArray()
        .put(JSONObject()
            .put("id", 3)
            .put("type", "dog")
            .put("breed", "corgi")
            .put("name", "Doug"))
        .put(JSONObject()
            .put("id", 4)
            .put("type", "fish")
            .put("breed", "salmon")
            .put("name", "Larry"))
        .put(JSONObject()
            .put("id", 5)
            .put("type", "bird")
            .put("breed", "parakeet")
            .put("name", "Mary")
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}

{% subtab Update %}
```kotlin
val json = JSONObject()
    .put("\$update", JSONArray()
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 4)
            .put("\$new_object", JSONObject()
                .put("breed", "goldfish")
            )
        )
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 5)
            .put("\$new_object", JSONObject()
                .put("name", "Annette")
            )
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}

{% subtab Delete %}
```kotlin
val json = JSONObject()
    .put("\$remove", JSONArray()
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 1)
        )
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 2)
        )
        .put(JSONObject()
            .put("\$identifier_key", "type")
            .put("\$identifier_value", "dog")
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Swift SDK %}
{% subtabs %}
{% subtab Create %}
```swift
let json: [[String: Any?]] = [
  [
    "id": 1,
    "type": "dog",
    "breed": "beagle",
    "name": "Gus"
  ],
  [
    "id": 2,
    "type": "cat",
    "breed": "calico",
    "name": "Gerald"
  ]
]

braze.user.setCustomAttribute(key: "pets", array: json)
```
{% endsubtab %}

{% subtab Add %}
```swift
let json: [String: Any?] = [
  "$add": [
    [
      "id": 3,
      "type": "dog",
      "breed": "corgi",
      "name": "Doug"
    ],
    [
      "id": 4,
      "type": "fish",
      "breed": "salmon",
      "name": "Larry"
    ],
    [
      "id": 5,
      "type": "bird",
      "breed": "parakeet",
      "name": "Mary"
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}

{% subtab Update %}
```swift
let json: [String: Any?] = [
  "$update": [
    [
      "$identifier_key": "id",
      "$identifier_value": 4,
      "$new_object": [
        "breed": "goldfish"
      ]
    ],
    [
      "$identifier_key": "id",
      "$identifier_value": 5,
      "$new_object": [
        "name": "Annette"
      ]
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}

{% subtab Delete %}
```swift
let json: [String: Any?] = [
  "$remove": [
    [
      "$identifier_key": "id",
      "$identifier_value": 1,
    ],
    [
      "$identifier_key": "id",
      "$identifier_value": 2,
    ],
    [
      "$identifier_key": "type",
      "$identifier_value": "dog",
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
AppboyKit에서는 중첩 사용자 정의 속성이 지원되지 않습니다.
{% endalert %}
{% endtab %}

{% tab Web SDK %}
{% subtabs local %}
{% subtab Create %}
```javascript
import * as braze from "@braze/web-sdk";
const json = [{
  "id": 1,
  "type": "dog",
  "breed": "beagle",
  "name": "Gus"
}, {
  "id": 2,
  "type": "cat",
  "breed": "calico",
  "name": "Gerald"
}];
braze.getUser().setCustomUserAttribute("pets", json);
```
{% endsubtab %}

{% subtab Add %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$add": [{
    "id":  3,
    "type":  "dog",
    "breed":  "corgi",
    "name":  "Doug",
  }, {
    "id":  4,
    "type":  "fish",
    "breed":  "salmon",
    "name":  "Larry",
  }, {
    "id":  5,
    "type":  "bird",
    "breed":  "parakeet",
    "name":  "Mary",
  }]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}

{% subtab Update %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$update": [
    {
      "$identifier_key": "id",
      "$identifier_value": 4,
      "$new_object": {
        "breed": "goldfish"
      }
    },
    {
      "$identifier_key": "id",
      "$identifier_value": 5,
      "$new_object": {
        "name": "Annette"
      }
    }
  ]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}

{% subtab Delete %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$remove": [
    {
      "$identifier_key": "id",
      "$identifier_value": 1,
    },
    {
      "$identifier_key": "id",
      "$identifier_value": 2,
    },
    {
      "$identifier_key": "type",
      "$identifier_value": "dog",
    }
  ]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Liquid 템플릿

이 `pets` 배열을 사용하여 메시지를 개인화할 수 있습니다. 다음 Liquid 템플릿 예제는 이전 API 요청에서 저장된 사용자 정의 속성 객체 속성을 참조하고 이를 메시징에 사용하는 방법을 보여줍니다.

{% raw %}
```liquid
{% assign pets = {{custom_attribute.${pets}}} %} 
 
{% for pet in pets %}
I have a {{pet.type}} named {{pet.name}}! They are a {{pet.breed}}.
{% endfor %} 
```
{% endraw %}

이 시나리오에서는 Liquid를 사용하여 `pets` 배열을 반복하고 각 애완동물에 대한 문장을 출력할 수 있습니다. [변수 할당]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables)을(를) `pets` 사용자 정의 속성에 할당하고 점 표기법을 사용하여 객체의 속성에 접근합니다. 객체의 이름을 지정한 다음, 마침표 `.`를 추가하고 속성 이름을 추가합니다.

## 세분화

객체 배열을 기반으로 사용자를 세분화할 때, 배열의 어떤 객체라도 기준에 맞으면 사용자가 세그먼트에 적합합니다. 

새 세그먼트를 만들고 **중첩 사용자 정의 속성**을(를) 필터로 선택합니다. 그런 다음 객체 배열의 이름을 검색하고 선택합니다.

\![객체 배열로 필터링.]({% image_buster /assets/img_archive/array_of_objects_segmenting_1.gif %})

점 표기법을 사용하여 객체 배열에서 사용하려는 필드를 지정합니다. 텍스트 필드를 빈 대괄호 `[]`로 시작하여 Braze에 객체 배열 내에서 찾고 있음을 알립니다. 그 후, 마침표 `.`를 추가하고 사용하려는 필드의 이름을 추가합니다.

예를 들어, `pets` 객체 배열을 `type` 필드를 기준으로 필터링하려면 `[].type`을 입력하고 필터링할 애완동물 유형을 선택합니다. 예: `snake`.

\![애완동물 유형이 뱀과 같은 경우 필터링.]({% image_buster /assets/img_archive/array_of_objects_segmenting_3.png %})

또는 `type`이(가) `dog`인 애완동물을 필터링할 수 있습니다. 여기 사용자는 최소한 한 마리의 개를 가지고 있어야 하므로 해당 사용자는 "개 유형의 애완동물을 최소한 한 마리 이상 가진 모든 사용자"의 세그먼트에 해당합니다.

\![애완동물 유형이 개와 같은 필터.]({% image_buster /assets/img_archive/array_of_objects_segmenting_2.png %})

### 중첩 수준

하나의 배열 중첩 수준(다른 배열 내의 배열)으로 세그먼트를 만들 수 있습니다. 예를 들어, 다음 속성을 고려할 때, `pets[].name`이 `Gus`를 포함하는 세그먼트를 만들 수 있지만, `pets[].nicknames[]`이 `Gugu`를 포함하는 세그먼트를 만들 수는 없습니다.

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Gus",
          "nicknames": [
            "Gugu",
            "Gusto"
          ]
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Gerald",
          "nicknames": [
            "GeGe",
            "Gerry"
          ]
        }
      ]
    }
  ]
}
```
{% endraw %}

## 데이터 포인트

데이터 포인트는 속성을 생성, 업데이트 또는 제거하는지에 따라 다르게 기록됩니다.

{% tabs local %}
{% tab Create %}

새 배열을 생성하면 객체의 각 속성에 대해 하나의 데이터 포인트가 기록됩니다. 이 예제는 여덟 개의 데이터 포인트가 필요합니다. 각 애완동물 객체는 네 개의 속성을 가지고 있으며 두 개의 객체가 있습니다.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Gus"
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Gerald"
        }
      ]
    }
  ]
}
```
{% endtab %}
{% tab Update %}

기존 배열을 업데이트하면 추가된 각 속성에 대해 하나의 데이터 포인트가 기록됩니다. 이 예제는 두 개의 데이터 포인트가 필요합니다. 각 두 개의 객체에서 하나의 속성만 업데이트하기 때문입니다.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "pets": {
        "$update": [
          {
            "$identifier_key": "id",
            "$identifier_value": 4,
            "$new_object": {
              "breed": "goldfish"
            }
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 5,
            "$new_object": {
              "name": "Annette"
            }
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% tab Remove %}

배열에서 객체를 제거하면 전송하는 각 제거 기준에 대해 하나의 데이터 포인트가 기록됩니다. 이 예제는 세 개의 데이터 포인트가 필요합니다. 이 문장으로 여러 마리의 개를 제거할 수 있지만 말입니다.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$remove": [
          // Remove by ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Remove any dog
          {
            "$identifier_key": "type",
            "$identifier_value": "dog"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

