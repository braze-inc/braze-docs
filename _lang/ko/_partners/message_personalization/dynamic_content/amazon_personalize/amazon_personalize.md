---
nav_title: Amazon Personalize
article_title: Amazon Personalize
alias: /partners/amazon_personalize/
description: "이 참조 문서에서는 Braze와 Amazon Personalize의 참조 아키텍처 및 통합에 대해 간략하게 설명합니다. 이 참조 문서에서는 Amazon Personalize가 제공하는 사용 사례, 작동하는 데이터, 서비스 구성 방법 및 이를 Braze와 통합하는 방법을 이해하는 데 도움이 됩니다."
page_type: partner
search_tag: Partner
---

# Amazon Personalize
<!--
{% multi_lang_include video.html id="xFZ3HMleYYE" align="right" %}
-->
> Amazon Personalize는 나만의 아마존 머신 러닝 추천 시스템을 하루 종일 사용하는 것과 같습니다. 20년 이상의 추천 경험을 바탕으로 한 Amazon Personalize를 사용하면 실시간 개인화 상품 및 콘텐츠 추천과 타겟 마케팅 프로모션을 통해 고객 참여를 향상시킬 수 있습니다.

_This integration is maintained by Amazon Personalize._

## 통합 정보

머신 러닝과 사용자가 정의하는 알고리즘을 사용하여 Amazon Personalize는 웹사이트 및 애플리케이션에 대한 고품질 추천을 출력하는 모델을 훈련하는 데 도움을 줄 수 있습니다. 이러한 모델을 사용하면 사용자의 과거 행동을 기반으로 추천 목록을 만들고, 관련성별로 항목을 정렬하고, 유사성에 따라 다른 항목을 추천할 수 있습니다. 그런 다음 Amazon Personalize API에서 얻은 목록을 Braze 커넥티드 콘텐츠에서 사용하여 개인화된 Braze 추천 캠페인을 실행할 수 있습니다. Amazon Personalize와의 통합을 통해 고객은 모델을 학습시키는 데 사용되는 매개 변수를 자유롭게 제어하고 알고리즘의 결과를 최적화하는 선택적 비즈니스 목표를 정의할 수 있습니다. 

이 참조 문서에서는 Amazon Personalize가 제공하는 사용 사례, 작동하는 데이터, 서비스 구성 방법 및 이를 Braze와 통합하는 방법을 이해하는 데 도움이 됩니다.

## 전제 조건

| 요구 사항| 설명|
| ---| ---| 
| Amazon Web Service 계정 | 이 파트너십을 이용하려면 AWS 계정이 필요합니다. AWS 계정이 있으면 Amazon Personalize 콘솔, AWS CLI(명령줄 인터페이스) 또는 AWS SDK를 통해 Amazon Personalize에 액세스할 수 있습니다. |
| 정의된 사용 사례 | 모델을 만들기 전에 이 통합에 대한 사용 사례를 결정해야 합니다. 일반적인 사용 사례는 다음 목록을 참조하세요. |
| 데이터 세트 | Amazon 개인화 추천 모델에는 세 가지 유형의 데이터 세트, 상호 작용, 사용자 및 항목이 필요합니다. 각 데이터 세트에 대한 요구 사항을 확인하려면 다음 세부 정보를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% tabs %}
{% tab 사용 사례 %}

**활용 사례**

모델을 만들기 전에 이 통합에 대한 사용 사례를 결정해야 합니다. 몇 가지 일반적인 사용 사례는 다음과 같습니다:
- 이전 상호 작용을 기반으로 사용자에게 항목을 추천하여 사용자에게 진정한 개인화된 경험을 제공합니다.
- 각 사용자에게 맞춤화된 항목 목록 또는 검색 결과를 제공하여 사용자와의 관련성별로 항목을 표시함으로써 인게이지먼트를 높입니다.
- 유사한 항목에 대한 추천을 찾아 사용자가 새로운 항목을 검색할 수 있도록 도와줍니다.

다음 가이드에서는 사용자 맞춤 추천 레시피에 대해 집중적으로 설명합니다.

{% endtab %}
{% tab 데이터 세트 %}

**데이터 세트**

Amazon 개인화 추천 모델을 시작하려면 세 가지 유형의 데이터 세트가 필요합니다:

- 상호 작용
  - 사용자와 항목 간의 과거 상호 작용을 저장합니다.
  - `USER_ID`, `ITEM_ID`, `EVENT_TYPE`, `TIMESTAMP` 값이 필요하며 선택적으로 이벤트에 대한 메타데이터를 허용합니다.
- 사용자
  - 사용자에 대한 메타데이터 저장
  - `USER_ID` 값과 성별, 나이, 로열티 멤버십 등 하나 이상의 메타데이터 필드(문자열 또는 숫자)가 필요합니다.
- 항목
  - 항목에 대한 메타데이터 저장
  - `ITEM_ID` 및 항목을 설명하는 하나 이상의 메타데이터 필드(텍스트, 범주 또는 숫자)가 필요합니다.

사용자 추천 레시피의 경우 각각 최소 2번 이상의 상호 작용이 있는 최소 25명의 고유 사용자로부터 1,000포인트 이상의 상호 작용 데이터가 포함된 상호 작용 데이터 세트를 제공해야 합니다. 이러한 데이터 세트는 S3에 저장된 CSV 파일을 사용하여 대량으로 업로드하거나 API를 통해 점진적으로 업로드할 수 있습니다.

{% endtab %}
{% endtabs %}

## 모델 만들기

### 1단계: 교육 중

데이터 집합을 가져오면 솔루션을 만들 수 있습니다. 솔루션은 Amazon Personalize [레시피](https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html) (알고리즘) 중 하나를 사용하여 모델을 학습시킵니다. 저희의 경우 `USER_PERSONALIZATION` 레시피를 사용합니다. 솔루션을 학습하면 모델의 성능 메트릭을 기반으로 평가할 수 있는 솔루션 버전(학습된 모델)이 생성됩니다.

Amazon 개인화를 사용하면 모델이 학습에 사용하는 하이퍼파라미터를 조정할 수 있습니다. 예를 들어, 다음과 같습니다.
- Amazon 개인화 콘솔에 있는 '사용자 기록 길이 백분위수' 매개 변수를 사용하면 교육에 포함할 사용자 기록의 백분위수를 조정할 수 있습니다:<br><br>![최소 최대 사용자 프로필 설정][3]
  - `min_user_history_length_percentile`: 기록 길이가 매우 짧은 사용자 비율을 제외하므로 인기 항목을 제거하고 보다 심층적인 기본 패턴을 기반으로 추천을 구축하는 데 도움이 될 수 있습니다.
  - `max_user_history_length_percentile`: 기록 길이가 매우 긴 항목으로 훈련할 때 고려할 사용자 비율을 조정합니다.

숨겨진 차원 수는 복잡한 데이터 세트의 더 복잡한 패턴을 감지하는 데 도움이 되며, 동시에 시간에 따른 역전파 기법(BPTT)은 높은 가치의 작업을 유도하는 일련의 이벤트가 발생한 후 초기 이벤트에 대한 리워드를 조정합니다.

또한 Amazon Personalize는 서로 다른 값으로 여러 버전의 솔루션을 동시에 실행하여 자동 하이퍼파라미터 튜닝을 제공합니다. 튜닝을 사용하려면 솔루션을 생성할 때 **HPO 수행**을 켭니다.

### 2단계: 평가 및 비교

솔루션 교육이 완료되면 솔루션을 평가하고 다른 버전을 비교할 준비가 된 것입니다. 각 솔루션 버전은 계산된 메트릭을 표시합니다. 사용 가능한 일부 지표에는 다음이 포함됩니다:

- **할인 누적 이익 정규화:** 권장되는 항목 순서를 실제 항목 목록과 비교하고 각 항목에 목록 내 위치에 해당하는 가중치를 부여합니다.
- **정확도 @k:** 적절하게 추천된 항목의 양을 모든 추천 항목의 양으로 나눈 값(여기서 `k`는 항목 수)
- **평균 상호 순위:** 첫 번째, 가장 높은 순위의 추천에 초점을 맞추고 일치하는 첫 번째 추천이 표시되기 전에 표시되는 추천 항목 수를 계산합니다.
- **커버리지:** 데이터 세트의 총 고유 항목 수에 대한 고유 추천 항목의 비율

## 추천 받기

만족스러운 솔루션 버전을 만들었으면 이제 권장 사항을 사용할 차례입니다. 권장 사항에 액세스하는 방법에는 두 가지가 있습니다:

1. 실시간 캠페인<br>캠페인은 최소 트랜잭션 처리량이 정의된 배포된 솔루션 버전입니다. 트랜잭션은 추천 출력을 얻기 위한 단일 API 호출이며, 최솟값이 1인 초당 트랜잭션 수(TPS)로 정의됩니다. 캠페인은 부하가 증가할 경우 리소스를 확장하지만 최솟값 이하로 떨어지지는 않습니다. 콘솔, AWS CLI 또는 코드의 AWS SDK를 통해 권장 사항을 쿼리할 수 있습니다.<br><br>
2. 배치 작업<br>일괄 작업은 권장 사항을 S3 버킷으로 내보냅니다. 이 작업은 추천을 내보낼 사용자 ID 목록이 포함된 JSON 파일 입력을 사용합니다. 그런 다음, 올바른 권한과 출력 대상을 지정하면 작업을 실행할 준비가 된 것입니다. 런타임은 데이터 세트의 크기와 권장 사항 목록 길이에 따라 달라집니다.

### 필터

필터를 사용하면 항목의 ID, 이벤트 유형 또는 메타데이터에 따라 항목을 제외하여 추천 출력을 조정할 수 있습니다. 연령이나 로열티 멤버십 상태와 같은 메타데이터를 기준으로 사용자를 필터링할 수도 있습니다. 필터를 사용하면 간편하게 사용자가 이미 상호 작용한 항목의 추천을 방지할 수 있습니다.

## Braze와 결과 통합

생성된 모델 및 추천 캠페인을 사용하면 콘텐츠 카드 및 커넥티드 콘텐츠를 사용하여 사용자를 위한 Braze 캠페인을 실행할 준비가 된 것입니다.
Braze 캠페인을 실행하기 전에 API를 통해 이러한 추천을 제공할 수 있는 서비스를 만들어야 합니다. [워크샵 문서의 3단계][1]에 따라 AWS 서비스를 사용하여 서비스를 배포할 수 있습니다. 추천을 제공하는 독립적인 백엔드 서비스를 직접 배포할 수도 있습니다.

### 콘텐츠 카드 캠페인 사용 사례

목록에서 첫 번째 추천 아이템으로 콘텐츠 카드 캠페인을 실행해 보겠습니다.<br><br>
다음 예제에서는 다음을 쿼리합니다.
`GET http://<service-endpoint.com>/recommendations?user_id=user123` 엔드포인트에 `user_id` 매개변수를 추가하면 추천 항목 목록을 반환합니다.

```json
[
  {
    "id": "abc123",
    "url": "http://productpage.com/product/abc123",
    "name": "First Item",
    "price": 39.99,
    "image": "http://pp.cdn.com/abvh3321pjb1j"
  },
  {
    "id": "xyz987",
    "url": "http://productpage.com/product/xyz987",
    "name": "Great Item",
    "price": 19.99,
    "image": "http://pp.cdn.com/234bjl1gioj1b2b"
  },
  ...
]
```

Braze 대시보드에서 새 [콘텐츠 카드 캠페인]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/)을 생성합니다. 메시지 텍스트 필드에서 커넥티드 콘텐츠 리퀴드 블록을 생성하여 API를 쿼리하고 `recommendations` 변수에 응답을 저장합니다:

{% raw %}

```liquid
{% connected_content https:/<service-endpoint.com>/recommendations?user_id={{${user_id}}} :save recommendations %}
```

그런 다음 결과 배열의 첫 번째 항목을 참조하여 사용자에게 콘텐츠를 표시할 수 있습니다:

```liquid
This seems like a great fit for you:
{% recommendations[0].name %}
{% recommendations[0].price %}
```

{% endraw %}

제목, 이미지, URL 링크를 포함한 전체 콘텐츠 카드의 모습은 다음과 같습니다:

![메시지 본문과 '이미지 추가' 필드에 연결된 콘텐츠가 추가된 캠페인의 이미지입니다. 이 이미지는 사용자를 추천 URL로 연결하는 '웹 URL로 리디렉션' 필드에 추가된 콘텐츠 로직을 보여줍니다.][2]


[1]: {{site.baseurl}}/partners/message_personalization/dynamic_content/amazon_personalize/workshop/#step-3-send-personalized-emails-from-braze
[2]: {% image_buster /assets/img/amazon_personalize/content-card-campaign.png %}
[3]: {% image_buster /assets/img/amazon_personalize/min_and_max_user_percentile.png %}