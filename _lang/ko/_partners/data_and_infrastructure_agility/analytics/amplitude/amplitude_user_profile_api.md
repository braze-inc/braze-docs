---
nav_title: 앰플리튜드 및 커넥티드 콘텐츠
article_title: 앰플리튜드 및 커넥티드 콘텐츠
page_order: 0
alias: /partners/amplitude_api_endpoints/
page_type: partner
description: "Amplitude의 고객 프로필 API는 Amplitude의 고객 프로필을 제공합니다. 여기에는 사용자 속성, 계산된 사용자 속성, 해당 사용자를 포함하는 코호트의 코호트 ID 목록 및 권장 사항이 포함됩니다."
search_tag: Partner

---

# 앰플리튜드 및 커넥티드 콘텐츠

> Amplitude의 고객 프로필 API는 Amplitude의 고객 프로필을 제공합니다. 여기에는 사용자 속성, 계산된 사용자 속성, 해당 사용자를 포함하는 코호트의 코호트 ID 목록 및 권장 사항이 포함됩니다. 다음은 커넥티드 콘텐츠와 함께 사용할 수 있는 일반적인 Amplitude API 엔드포인트 목록입니다.

## 엔드포인트 매개변수

다음 표에는 고객 프로필 API 호출에 사용할 수 있는 매개변수가 나와 있습니다.

| 매개변수 | 필수 | 설명 |
| --------- | -------- | ----------- |
| `user_id` | 선택 사항 | 쿼리할 사용자 ID(외부 데이터베이스 ID)로, `device_id`를 설정하지 않은 경우 필수입니다. |
| `device_id` | 선택 사항 | 쿼리할 기기 ID(익명 ID)로, `user_id`를 설정하지 않은 경우 필수입니다. |
| `get_recs` | 선택 사항<br>(기본값: false) | 이 사용자에 대한 추천 결과를 반환합니다. |
| `rec_id` | 선택 사항 | 검색할 추천으로, `get_recs`가 true이면 필수입니다. `rec_ids` 을 쉼표로 구분하여 여러 권장 사항을 가져올 수 있습니다. |
| `rec_type` | 선택 사항 | 기본 실험 제어 설정을 재정의하면 `rec_type=model`은 모델링된 추천을 반환하고 `rec_type=random`은 무작위 추천을 반환합니다. 향후 다른 옵션이 추가될 수 있습니다. |
| `get_amp_props` | 선택 사항<br>(기본값: false) | 계산을 제외한 이 사용자에 대한 전체 사용자 속성 집합을 반환합니다. |
| `get_cohort_ids` | 선택 사항<br>(기본값: false) | 추적하도록 설정된 이 사용자가 속한 모든 코호트 ID의 목록을 반환합니다. 기본적으로 코호트 멤버십은 임의의 코호트의 사용자에 대해 추적되지 않습니다. |
| `get_computations` | 선택 사항<br>(기본값: false) | 이 사용자에 대해 활성화된 모든 계산 목록을 반환합니다. |
| `comp_id` | 선택 사항 | 이 사용자에 대해 활성화할 수 있는 단일 계산을 반환합니다. 존재하지 않는 경우 null 값을 반환합니다. `get_computations`가 true이면 아카이브되거나 삭제되지 않는 한 이 값을 포함한 모든 값을 가져옵니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

다음 표에서는 Amplitude의 응답에서 가장 일반적으로 볼 수 있는 매개변수를 다룹니다.

| 응답 매개변수 | 설명 |
| ------------------ | ----------- |
| `rec_id` | 요청된 추천 ID입니다. |
| `child_rec_id` | 모델 성능을 개선하기 위한 내부 실험의 일환으로 Amplitude가 백엔드에서 사용할 수 있는 보다 자세한 추천 ID. 대부분의 경우 `rec_id`와 동일합니다. |
| `items` | 이 사용자에 대한 권장 사항 목록입니다. |
| `is_control` | 이 사용자가 대조군에 속해 있으면 true. |
| `recommendation_source` | 이 권장 사항을 생성하는 데 사용된 모델 이름 |
| `last_updated` | 이 권장 사항이 마지막으로 생성되고 동기화된 시점의 타임스탬프입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 공통 진폭 엔드포인트

### 추천 받기

#### 엔드포인트
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_recs=true&rec_id=testRecId`
{% endraw %}
#### 응답 예시
```json
{
  "userData": {
    "recommendations": [
      {
        "rec_id": "testRecId",
        "child_rec_id": "testRecId",
        "items": [
          "cookie",
          "cracker",
          "chocolate milk",
          "donut",
          "croissant"
        ],
        "is_control": false,
        "recommendation_source": "model",
        "last_updated": 1608670720
      }
    ],
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": null,
    "cohort_ids": null
  }
}
```

### 여러 추천 받기

#### 엔드포인트
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_recs=true&rec_id=testRecId,testRecId2`
{% endraw %}
#### 응답 예시
```json
{
  "userData": {
    "recommendations": [
      {
        "rec_id": "testRecId",
        "child_rec_id": "testRecId",
        "items": [
          "cookie",
          "cracker",
          "chocolate milk",
          "donut",
          "croissant"
        ],
        "is_control": false,
        "recommendation_source": "model",
        "last_updated": 1608670720
      },
            {
        "rec_id": "testRecId2",
        "child_rec_id": "testRecId2",
        "items": [
          "bulgogi",
          "bibimbap",
          "kimchi",
          "croffles",
          "samgyeopsal"
        ],
        "is_control": false,
        "recommendation_source": "model2",
        "last_updated": 1608670658
      }
    ],
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": null,
    "cohort_ids": null
  }
}
```

### 사용자 속성 가져오기

#### 엔드포인트
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_amp_props=true`
{% endraw %}
#### 응답 예시
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "library": "http/1.0",
      "first_used": "2020-01-13",
      "last_used": "2021-03-24",
      "number_property": 12,
      "boolean_property": true
    },
    "cohort_ids": null
  }
}
```

### 코호트 ID 가져오기

#### 엔드포인트
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_cohort_ids=true`
{% endraw %}
#### 응답 예시
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": null,
    "cohort_ids": ["cohort1", "cohort3", "cohort7"]
  }
}
```

### 단일 계산 가져오기

#### 엔드포인트
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&comp_id=testCompId`
{% endraw %}
#### 응답 예시
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "computed-prop-2": "3"
    },
    "cohort_ids": null
  }
}
```

### 모든 계산 가져오기

#### 엔드포인트
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_computations=true`
{% endraw %}
#### 응답 예시
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "computed-prop-1": "5000000.0",
      "computed-prop-2": "3"
    },
    "cohort_ids": null
  }
}
```

