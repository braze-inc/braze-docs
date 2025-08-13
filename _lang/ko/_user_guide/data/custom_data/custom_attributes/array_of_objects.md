---
nav_title: 오브젝트 배열
article_title: 오브젝트 배열
alias: "/array_of_objects/"
page_order: 0
page_type: reference
description: "이 참조 문서에서는 객체 배열을 커스텀 속성의 데이터 유형으로 사용하는 데 따른 제한 사항과 사용 예시를 설명합니다." 
---

# 객체 배열

> 이 페이지에서는 객체 배열을 사용하여 관련 속성을 그룹화하는 방법에 대해 설명합니다. 예를 들어, 한 사용자에게 속하는 애완동물 객체, 노래 객체 및 계정 객체 그룹이 있을 수 있습니다. 이러한 개체 배열을 사용하여 Liquid로 메시지를 개인화하거나 개체 내의 요소가 기준과 일치하는 경우 오디언스 세그먼트를 만들 수 있습니다.

## 제한 사항

- 객체 배열은 API를 통해 전송되는 사용자 정의 속성을 위한 것입니다. CSV 업로드는 지원되지 않습니다. 이는 CSV 파일의 쉼표가 열 구분 기호로 해석되고 값의 쉼표가 구문 분석 오류를 유발하기 때문입니다. 
- 객체 배열은 항목 수에 제한이 없지만 최대 크기는 100KB입니다.
- 모든 Braze 파트너가 오브젝트 배열을 지원하는 것은 아닙니다. 통합에서 이 기능을 지원하는지 확인하려면 [파트너 설명서]({{site.baseurl}}/partners/home)를 참조하세요.

배열의 항목을 업데이트하거나 제거하려면 키와 값으로 항목을 식별해야 하므로 배열의 각 항목에 고유 식별자를 포함하는 것이 좋습니다. 고유성은 배열로만 범위가 지정되며 배열에서 특정 개체를 업데이트하고 제거하려는 경우에 유용합니다. 이는 Braze에서 강제하지 않습니다.

{% alert tip %}
사용자 속성 개체에 대한 개체 배열을 사용하는 방법에 대한 자세한 내용은 [사용자 속성 개체를]({{site.baseurl}}/api/objects_filters/user_attributes_object) 참조하세요.
{% endalert %}

## API 예제

{% tabs local %}
{% tab 만들기 %}

다음은 `pets` 배열을 사용한 `/users/track` 예제입니다. 펫의 속성을 캡처하려면 `pets`를 객체 배열로 나열하는 API 요청을 보내세요. 각 객체에는 나중에 업데이트할 때 참조할 수 있는 고유한 `id` 주소가 할당되어 있습니다.

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
{% tab 추가 %}

`$add` 연산자를 사용하여 배열에 다른 항목을 추가합니다. 다음 예는 사용자의 `pets` 배열에 3개의 펫 객체를 추가하는 것을 보여줍니다.

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
{% tab 업데이트 %}

`_merge_objects` 매개변수와 `$update` 연산자를 사용하여 배열 내의 특정 객체에 대한 값을 업데이트합니다. 단순 [중첩된 사용자 지정 속성]({{site.baseurl}}/nested_custom_attribute_support/#api-request-body) 개체에 대한 업데이트와 유사하게 심층 병합을 수행합니다.

Note that `$update` can't be used to remove a nested property from an object inside an array. To do this, you'll need to remove the entire item from the array and then add the object without that specific key (using a combination of `$remove` and `$add`).

다음 예제는 `id`가 `4`인 개체에 대해 `breed` 속성정보를 `goldfish`로 업데이트하는 것을 보여줍니다. 이 요청 예제는 또한 `id`의 개체를 `5`로 업데이트하여 `Annette`의 새로운 `name`으로 업데이트합니다. `_merge_objects` 매개 변수는 `true`로 설정되어 있으므로 이 두 개체의 다른 모든 필드는 동일하게 유지됩니다.

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
`_merge_objects`를 참으로 설정하지 않으면 개체를 덮어쓰게 됩니다. `_merge_objects`는 기본적으로 거짓입니다.
{% endalert %}

{% endtab %}
{% tab 제거 %}

일치하는 키(`$identifier_key`) 및 값(`$identifier_value`)과 함께 `$remove` 연산자를 사용하여 배열에서 개체를 제거합니다.

다음 예제는 `pets` 배열에서 값이 `1`인 `id`, 값이 `2`인 `id`, 값이 `dog`인 `type`을 가진 개체를 제거하는 예제입니다 . `dog` 값이 `type`인 객체가 여러 개 있는 경우 일치하는 모든 객체가 제거됩니다.

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

## SDK 예제

{% tabs local %}
{% tab Android SDK %}

**생성**
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

**추가**
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

**업데이트**
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

**삭제**
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

{% endtab %}
{% tab Swift SDK %}

**생성**
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

**추가**
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

**업데이트**
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

**삭제**
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

{% alert important %}
AppboyKit에는 중첩 커스텀 속성이 지원되지 않습니다.
{% endalert %}

{% endtab %}
{% tab 웹 SDK %}

**생성**
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

**추가**
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

**업데이트**
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

**삭제**
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

{% endtab %}
{% endtabs %}

## Liquid 템플릿

이 `pets` 배열을 사용하여 메시지를 맞춤 설정할 수 있습니다. 다음 Liquid 템플릿 예제에서는 앞의 API 요청에서 저장된 커스텀 속성 개체 속성을 참조하여 메시징에 사용하는 방법을 보여 줍니다.

{% raw %}
```liquid
{% assign pets = {{custom_attribute.${pets}}} %} 
 
{% for pet in pets %}
I have a {{pet.type}} named {{pet.name}}! They are a {{pet.breed}}.
{% endfor %} 
```
{% endraw %}

이 시나리오에서는 Liquid를 사용하여 `pets` 배열을 반복하고 각 애완동물에 대한 문을 인쇄할 수 있습니다. `pets` 사용자 지정 속성에 [변수를 할당하고]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables) 점 표기법을 사용하여 객체의 속성에 액세스합니다. 개체 이름 뒤에 마침표 `.`를 붙인 다음 속성 이름을 지정합니다.

## 세분화

객체 배열을 기반으로 사용자를 세그먼트화할 때 배열의 객체가 조건과 일치하는 경우 사용자는 세그먼트에 대한 자격을 얻게 됩니다. 

새 세그먼트를 만들고 **중첩 커스텀 속성**을 필터로 선택합니다. 그런 다음 개체 배열의 이름을 검색하고 선택합니다.

![Filter by array of objects.]({% image_buster /assets/img_archive/array_of_objects_segmenting_1.gif %})

점 표기법을 사용하여 개체 배열에서 사용할 필드를 지정합니다. 빈 대괄호(`[]`)로 텍스트 필드를 시작하여 Braze에 객체 배열 내부를 보고 있음을 알립니다. 그런 다음 마침표 `.`를 추가한 다음 사용하려는 필드 이름을 입력합니다.

예를 들어 `type` 필드를 기준으로 `pets` 개체 배열을 필터링하려면 `[].type`을 입력하고 필터링할 애완동물 유형(예: `snake`)을 선택합니다.

![Filter by pet type equals snake.]({% image_buster /assets/img_archive/array_of_objects_segmenting_3.png %})

또는 `dog` 의 `type`을 가진 반려동물을 필터링할 수도 있습니다. 여기서 사용자는 반려견을 한 마리 이상 키우고 있으므로 '반려견을 한 마리 이상 키우는 모든 사용자'라는 세그먼트에 해당합니다.

![Filter by pet type equals dog.]({% image_buster /assets/img_archive/array_of_objects_segmenting_2.png %})

### 중첩 수준

최대 한 단계의 배열 중첩(다른 배열 내의 배열)으로 세그먼트를 만들 수 있습니다. 예를 들어 다음 속성이 주어지면 `pets[].name` 포함 `Gus` 에 대한 세그먼트는 만들 수 있지만 `pets[].nicknames[]` 포함 `Gugu`에 대한 세그먼트는 만들 수 없습니다.

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

데이터 포인트는 속성 생성, 업데이트 또는 제거 여부에 따라 다르게 소비됩니다.

{% tabs local %}
{% tab 만들기 %}

새 배열을 만들면 객체의 각 속성에 대해 하나의 데이터 포인트가 소모됩니다. 이 예제에는 8개의 데이터 포인트가 필요하며, 각 애완동물 개체에는 4개의 속성이 있고 2개의 개체가 있습니다.

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
{% tab 업데이트 %}

기존 배열을 업데이트하면 추가되는 속성마다 데이터 포인트가 하나씩 소모됩니다. 이 예제에서는 두 개체에서 각각 하나의 속성만 업데이트하므로 두 개의 데이터 포인트가 필요합니다.

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
{% tab 제거 %}

배열에서 개체를 제거하면 전송하는 제거 기준마다 하나의 데이터 포인트가 소모됩니다. 이 예제에서는 이 문으로 여러 개의 개를 제거하더라도 데이터 포인트가 3개 필요합니다.

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

