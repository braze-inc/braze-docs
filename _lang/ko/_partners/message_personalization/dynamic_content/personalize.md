---
nav_title: Personalize.AI
article_title: Personalize.AI
description: "이 참조 문서에서는 개인화된 추천을 통해 매출 성장을 촉진하는 AI 기반 SaaS 비즈니스 플랫폼인 Braze와 Personalize.AI의 파트너십에 대해 설명합니다."
alias: /partners/personalize/
page_type: partner
search_tag: Partner
---

# Personalize.AI

> [Personalize.AI](https://www.zs.com/solutions/artificial-intelligence-and-analytics/personalize-ai/) 는 Braze와 파트너 관계를 맺고 Braze를 통해 개인화된 메시지와 혜택을 전달하여 점진적인 수익을 창출합니다. 

Braze와 Personalize.AI 통합을 통해 메시지 개인화 및 타겟팅을 위해 Personalize.AI에서 Braze 플랫폼으로 데이터를 내보낼 수 있습니다.

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Personalize.AI 인스턴스 | 이 파트너십을 이용하려면 Personalize.AI 인스턴스가 필요합니다. |
| Braze REST API 키 | 모든 권한이 있는 Braze REST API 키입니다. <br><br>Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL. 엔드포인트는 [인스턴스의 Braze URL에][1] 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용 사례

* 유연한 계층화를 포함한 테스트를 배포하여 고객 피드백을 통한 결과 도출
* 처리, 타이밍 및 콘텐츠를 포함하여 항목 및 오퍼에 대한 개인화된 추천 제공
* Braze를 통해 우선순위가 지정된 목표를 파악하고 최적의 오디언스 타겟팅
* 이탈한 사용자의 재참여 기회 식별
* 지리적 위치 데이터를 활용하여 새로 오픈한 위치에 적합한 잠재고객 찾기
* 유사 모델링을 사용하여 신규 사용자에 대해 사용 가능한 제한된 데이터를 기반으로 가장 관련성이 높은 추천과 매칭
* 고객 라이프사이클 전반에 걸쳐 고객 참여를 유도할 수 있는 올바른 방법 파악하기 
* 고객이탈 가능성을 사전에 평가하고 위험 점수를 부여하여 고객이탈의 조기 지표 검색
* 개인화된 개입으로 고객을 타겟팅하여 비활성 고객 방지

## 통합

### Personalize.AI에서 Braze와의 연결 구성 

1. Personalize.AI 에서 Personalize.AI 인스턴스의 **운영화** 아래에 있는 **통합** 탭으로 이동합니다.
2. **Braze**를 클릭합니다. 
3. Braze와의 통합을 구성하세요.
    * **연결 이름:** 연결 이름을 지정합니다. 통합이 Personalize.AI 에서 참조되는 방식입니다.
    * **동기화 빈도:** 동기화 빈도는 Personalize.AI 데이터를 Braze로 내보내는 빈도를 제어합니다. **일별**, **주별** 또는 **월별을** 선택합니다. 
    * **API 키:** Braze API 키를 추가합니다.
    * **API URL:** Braze REST 엔드포인트 URL을 추가합니다.
4. **내보내기**를 클릭하여 데이터를 Braze로 내보냅니다.

데이터를 내보낸 후에는 Personalize.AI에서 통합 중 설정한 동기화 빈도에 따라 결정된 간격으로 데이터를 Braze에 계속 전달합니다.

## 이 통합 사용

Personalize.AI 는 개인화된 타겟팅에 사용되는 식별자를 Braze로 내보냅니다. 이러한 커스텀 속성은 각 고객에 대한 타이밍, 콘텐츠, 처리 및 오퍼를 나타냅니다. 통합에 따라 필드를 이벤트로 전달하거나 고객 프로필에 저장하는 대신 [연결된 텐츠 API][2]로 가져올 수 있습니다. Personalize.AI는 식별자로 `external_id` 사용을 지원합니다.

Braze로 가져온 데이터 속성에는 일관된 용어에 따라 캔버스에서 사용할 수 있도록 직관적으로 이름이 지정됩니다. 예를 들어 Personalize.AI의 `C402_Target_Variant` 속성은 Braze에 `"P.AI_Model_Treatment"`로 내보내집니다. Personalize.AI에서 내보낸 속성은 기존 속성이나 사용 추적을 방해하지 않도록 설계되었습니다. 이러한 속성은 지속적으로 유효성을 검사하여 안심하고 참조할 수 있는지 확인합니다. 

예를 들어, 다음은 고객이탈에 초점을 맞춘 캔버스 예제와 관련된 고객 속성 집합입니다.

| Personalize.AI 속성 | 값 |
| ----------- | ------------- | 
| `Customer_ID` | 12345 |
| `Target_Canvas` | C4 |
| `Target_Objective` |  "Churn_Mitigation" |
| `C4_Target_Date` | 3/1/2023 |
| `C4_Target_Variant` | 치료 |
| `C4_Treatment` | "P.AI_Model" |
| `C4_Offer_Value` | $3 |
| `C4_Item_Recom` | "Caesar Salad" |
| `C4_Subject_Line` | "We miss you" |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/public_apis/
