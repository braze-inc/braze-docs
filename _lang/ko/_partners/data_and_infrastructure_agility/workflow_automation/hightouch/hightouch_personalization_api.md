---
nav_title: 하이터치 개인화 API
article_title: 하이터치 개인화 API
description: "이 참조 문서에서는 클라우드 데이터 웨어하우스 내의 모든 데이터 집합을 기반으로 지연 시간이 짧은 데이터 API를 호스팅하는 관리형 서비스인 Braze와 Hightouch의 개인화 API 간의 통합에 대해 설명합니다. 이 참조 문서에서는 Hightouch 개인화 API가 해결하는 사용 사례, 사용하는 데이터, 구성 방법, Braze와 통합하는 방법을 설명합니다."
page_type: partner
search_tag: Partner
---

# 하이터치 개인화 API

> Hightouch의 [개인화 API](https://hightouch.com/docs/destinations/personalization-api)는 클라우드 데이터 웨어하우스에 있는 모든 데이터 세트를 기반으로 지연 시간이 짧은 데이터 API를 호스팅할 수 있는 관리형 서비스입니다.

![][3]

Braze와 Hightouch의 통합을 통해 API를 [Braze 연결된 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/)와 함께 사용하면 전송 시점에 최신 고객 또는 오브젝트 데이터를 캠페인이나 캔버스로 가져올 수 있습니다.

Hightouch의 개인화 API는 Braze 구성 내에서 사용할 수 있는 REST 엔드포인트를 제공합니다. Specifically, you can use the Braze Connected Content offering to make a GET request to the Personalization API to retrieve all information related to a particular identifier. 이 API를 통해 공개되는 데이터는 고객, 제품 또는 기타 오브젝트 데이터를 나타낼 수 있습니다. 

![][2]

## 전제 조건

| 요구 사항| 설명|
| ---| ---| 
| 개인화 API가 활성화된 [하이터치 계정](https://app.hightouch.com/login)  | 이 파트너십을 활용하려면 Hightouch [비즈니스 티어 계정](https://hightouch.com/pricing)이 필요합니다.|
| 정의된 사용 사례 | API를 설정하기 전에 이 통합에 대한 사용 사례를 결정해야 합니다. 일반적인 사용 사례는 다음 목록을 참조하세요. |
| 클라우드 데이터 웨어하우스 또는 기타 소스에 저장된 데이터 | Hightouch는 [25개 이상의 데이터 소스와](https://hightouch.com/integrations) 통합됩니다. |
| 하이터치 API 키 | **Hightouch > 설정 > API 키 > API 키 추가**에서 생성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% tabs %}
{% tab 사용 사례 %}

### 활용 사례

시작하기 전에 개인화 API를 어떻게 사용할지 정확히 계획하는 것이 도움이 됩니다.

일반적인 사용 사례는 다음과 같습니다:
- 이메일 템플릿, 캠페인 또는 인앱 경험에 개인화된 제품 추천을 간편하게 삽입할 수 있는 **제품 권장** 사항
- 동적 제품 추천으로 마케팅 접점을 강화하여 **개인화된 마케팅 캠페인 강화** 
- **인앱 또는 웹 개인화 제공**(예: 맞춤형 검색 결과, 코호트 기반 가격 책정, 메시지, 기사 추천 또는 가장 가까운 매장 위치 등)
- **금융 또는 의료 데이터에 기반한 추천** \- 금융 데이터는 [엄격한 데이터 보안 정책](https://hightouch.com/docs/security/overview#compliance)을 통해 Hightouch가 충족하는 엄격한 요구 사항을 가지고 있습니다. Hightouch를 사용하면 세분화 기준에 사용된 기본 속성을 노출하지 않고도 금융 또는 의료 데이터를 기반으로 고객 세그먼트를 생성할 수 있습니다.

{% endtab %}
{% tab 데이터 세트 %}

### 데이터 세트

개인화 API는 웨어하우스에서 선택한 데이터에 대한 캐시 역할을 하므로 이미 추천 데이터가 저장되어 있어야 합니다. 필요한 경우 Hightouch를 사용하여 템플릿에 따라 변환할 수 있습니다. 이러한 유형의 데이터에는 다음이 포함됩니다:
- 지역, 연령 또는 기타 인구통계 정보와 같은 사용자 메타데이터
- 과거 구매, 페이지 조회, 클릭 등을 포함한 사용자 행동 또는 이벤트.

{% endtab %}
{% endtabs %}

## 통합

### 1단계: Hightouch에 데이터 소스 연결

Hightouch [소스](https://hightouch.com/docs/getting-started/concepts#sources)는 조직의 비즈니스 데이터가 있는 위치입니다. 이 경우 사용자 데이터가 저장되는 곳이면 어디든 가능합니다.
1. Hightouch에서 **소스 개요 > 소스 추가**로 이동합니다. 데이터 웨어하우스를 소스로 선택합니다.<br><br>
2. 관련 자격 증명을 입력합니다(출처에 따라 다를 수 있음). 

자세한 내용은 관련 소스 [설명서](https://hightouch.com/docs)를 참조하세요.

### 2단계: 모델 데이터

하이터치 모델은 소스에서 가져올 데이터를 정의합니다. 새 모델을 설정하려면 다음 단계를 따르세요:

1. Hightouch에서 [**모델 개요**](https://app.hightouch.com/models) > **모델 추가**로 이동하여 방금 연결한 소스를 선택합니다. <br><br>
2. 다음으로 [모델링 방법을](https://hightouch.com/docs/models/creating-models) 선택합니다. 모든 정보가 하나의 테이블에 조인되어야 하므로 시각적 테이블 선택기를 사용하여 정의할 수 있습니다. 또는 원하는 열만 포함하도록 SQL을 작성하거나 기존 dbt 모델, Looker Look 또는 Sigma 통합 문서에 의존할 수 있습니다.<br><br>
3. 계속하기 전에 모델을 미리 보고 관심 있는 데이터를 쿼리하고 있는지 확인합니다. 기본적으로 Braze는 미리 보기를 처음 100개의 레코드로 제한합니다. 데이터 유효성을 검사한 후 **계속**을 클릭합니다.<br><br>
4. 모델 이름(예: "사용자 추천")을 지정합니다.<br><br>
5. 마지막으로, 기본 키를 선택하고 **마침**을 클릭합니다. 기본 키는 고유 식별자가 있는 열이어야 합니다. 개인화 API를 호출하여 특정 사용자의 추천을 검색하는 데 사용할 필드이기도 합니다.

### 3단계: 개인화 API 구성

요청을 받기 위한 API 준비는 두 단계로 이루어집니다:
- 인프라에서 가장 가까운 지역에서 개인화 API 활성화하기
- 동기화를 생성하여 하이터치 관리 캐시에서 구체화할 모델 정의하기

두 가지를 모두 완료하려면 다음 지침을 따르세요:

1. Hightouch에서 [**대상**](https://app.hightouch.com/destinations)으로 이동하여 생성된 Hightouch 개인화 API를 선택합니다. 이 대상을 활성화하지 않은 경우 [Hightouch 지원](mailto:friends@hightouch.com)에 문의하세요.<br><br>
2. 다음으로 적절한 지역을 선택합니다. 인프라에서 가장 가까운 지역을 선택하면 응답 시간을 줄일 수 있습니다. 인프라에서 가까운 지역이 표시되지 않는 경우 [Hightouch 지원](mailto:friends@hightouch.com)에 문의하세요.<br><br>
3. [**동기화** 개요 페이지로](https://app.hightouch.com/syncs) 이동하여 **동기화 추가** 버튼을 클릭합니다. 그런 다음 관련 모델과 이전에 설정한 대상을 선택합니다.<br><br> 
4. 영숫자로 된 컬렉션 이름을 입력합니다. 컬렉션은 개념적으로 데이터베이스 테이블과 유사합니다. 각각 고객 또는 인보이스와 같은 특정 데이터 유형을 나타내야 합니다. 컬렉션 이름은 영숫자이어야 하며 개인화 API 엔드포인트의 일부가 됩니다.<br><br>
5. 다음으로, 모델에서 레코드 조회를 위한 기본 인덱스로 사용할 열을 지정합니다. 이 필드는 모음의 각 레코드를 고유하게 식별해야 하며 종종 모델의 기본 키와 동일합니다. 개인화 API는 여러 인덱스에 대한 조회를 지원합니다. 예를 들어 `user_id`, `anonymous_id` 또는 `email_address`를 사용하여 고객 프로필을 검색할 수 있습니다. 여러 인덱스를 활성화하려면 [Hightouch 지원](mailto:friends@hightouch.com)에 문의하세요.<br><br>
6. 필드 매퍼를 사용하여 모델의 어떤 열을 API 응답 페이로드에 포함할지 지정합니다. 이러한 필드의 이름을 변경하고 고급 매퍼를 사용하여 Liquid 템플릿 언어를 사용하여 변환을 적용할 수 있습니다.<br><br>
7. 사용 사례에 적합한 [삭제 동작](https://www.hightouch.com/docs/destinations/personalization-api#delete-behavior)을 선택합니다.<br><br>
8. 마지막으로, **계속**을 클릭한 다음, [동기화 스케줄](https://hightouch.com/docs/syncs/schedule-sync-ui)을 선택합니다.

이제 Hightouch는 웨어하우스의 데이터를 관리형 데이터베이스에 동기화하여 개인화 API를 통해 공개합니다.

### 4단계: Braze 커넥티드 콘텐츠를 통한 개인화 API 호출

개인화 API 인스턴스를 설정한 후에는 Braze 연결된 콘텐츠 엔드포인트로 사용할 수 있습니다. 

API는 `https://personalization.{region}.hightouch.com` 에서 액세스할 수 있습니다(예: `https://personalization.us-west-2.hightouch.com`). 

이 엔드포인트 `/v1/collections/:collection_name/records/:index_key/:index_value`를 사용하여 정보를 사용할 수 있습니다.

예를 들어, 캠페인이나 캔버스에 이 스니펫을 포함할 수 있습니다:

{% raw %}

```liquid
{% connected_content
     https://personalization.us-west-2.hightouch.com/v1/collections/customer/records/id/12345
     :method get
     :headers {
       "Authorization": "Bearer {{YOUR-API-KEY}}"
  }
     :content_type application/json
     :save customer
%}
```
{% endraw %}

Liquid 템플릿을 사용하여 JSON 페이로드에서 반환된 속성정보를 참조하고 메시징에 사용할 수 있습니다.

다음은 페이로드 예제입니다.

```json
{
    "user_id": 12345,
    "full_name": "Jane Doe",
    "lifetime_value": 1492.18,
    "churn_risk": 0.04,
    "90_day_summary": {
        "num_songs_listened": 813,
        "top_genres": [
            "house",
            "techno",
            "ambient"
        ],
        "top_artists": [
            "deadmau5",
            "Marsh",
            "Enamour"
        ],
    },
    "recommendations": {
        "concerts": [
            {
                "artist": "Aphex Twin",
                "location": "San Francisco, CA",
                "event_date": "2023-01-31"
            },
            {
                "artist": "Sultan + Shepard",
                "location": "San Francisco, CA",
                "event_date": "2023-02-25"
            }
        ],
        "upcoming_album_release": {
            "title": "Universal Language",
            "artist": "Simon Doty",
            "label": "Anjunadeep",
            "release_date": "2023-04-28"
        }
    },
}
```

다음 Liquid 참조는 이 예제 데이터를 반환합니다:

| 리퀴드 템플릿 | 반환된 예제 |
| --- | --- |
| {% raw %}`{{artists.recommendations.concerts[0].artist}}`{% endraw %}| Aphex Twin |
| {% raw %}`{{artists.recommendations.concerts[0].location}}`{% endraw %}| 샌프란시스코, 캘리포니아 |
| {% raw %}`{{artists.recommendations.upcoming_album_release.title}}`{% endraw %}| 범용 언어 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 문제 해결

궁금한 점이 있으면 [하이터치 지원팀에](mailto:friends@hightouch.com) 문의하여 도움을 받으세요.

[1]: {% image_buster /assets/img/hightouch/cohort5.png %}
[2]: {% image_buster /assets/img/hightouch/cohort6.png %}  
[3]: {% image_buster /assets/img/hightouch/cohort7.png %}  
