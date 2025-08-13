---
nav_title: Tellius
article_title: Tellius
alias: /partners/Tellius/
description: "이 참조 문서에서는 BI 엔지니어에 의존하지 않고도 데이터를 활용하여 대시보드를 구축하고 인사이트를 생성하여 더 나은 마케팅 의사 결정을 내릴 수 있도록 지원하는 의사 결정 인텔리전스 및 증강 분석 플랫폼인 Braze와 Tellius의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# Tellius

> 의사 결정 인텔리전스 및 증강 분석 플랫폼인 [Tellius](https://www.tellius.com/)를 사용하면 자연어 검색을 통해 데이터에 대한 질문에 답하고 인공지능 기반 안내 인사이트를 통해 '이유'를 더 심층적으로 이해할 수 있습니다.

Braze와 Tellius의 통합을 통해 사용자는 BI 엔지니어에게 의존하지 않고도 데이터를 활용하여 대시보드를 구축하고 인사이트를 생성하여 더 나은 마케팅 의사 결정을 내릴 수 있습니다. 이 통합을 위해 Braze 데이터가 Snowflake에 저장되어야 합니다. 여기서 Tellius는 직접 연결하여 실시간 모드 통합을 통해 쿼리를 푸시다운할 수 있습니다.

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Tellius 계정 | 이 파트너십을 활용하려면 Tellius 계정이 필요합니다. [무료 평가판](https://www.tellius.com/free-trial/)으로 Tellius의 여정을 시작할 수 있습니다.|
| Snowflake 데이터 공유 프로그램 | 현재 Snowflake 고객인 경우, Braze 담당자에게 Snowflake 데이터 공유 프로그램에 대해 문의하여 Braze 데이터를 Snowflake 인스턴스로 연결합니다.|
| Snowflake Reader 계정 | Snowflake 고객이 아닌 경우 Braze 담당자에게 연락하여 Braze 데이터에 액세스할 수 있도록 프로비저닝할 수 있는 Snowflake 리더 계정에 대해 문의하세요.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: Snowflake를 통해 Braze에 대한 액세스 확보

Braze는 세분화된 고객 데이터를 Snowflake에 저장합니다. Braze Snowflake 데이터 공유 프로그램을 통해 또는 Snowflake 리더 계정을 획득하여 Braze 데이터를 활용해 인사이트를 생성할 수 있습니다. 

[Snowflake 통합]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/)에 따라 설정합니다. 

### 2단계: Snowflake에서 Tellius를 Braze 데이터에 연결

다음 방법 중 하나를 통해 Tellius를 Snowflake의 Braze 데이터에 연결합니다.

- 직접 액세스: Tellius에 데이터를 로드하려면 [데이터 세트 로드](https://help.tellius.com/article/jn6o59d5gk-load-datasets) 단계를 따르세요.
- OAuth 액세스: Snowflake에 대한 OAuth 액세스를 사용하려면 [OAuth 인증](https://help.tellius.com/article/11517w63b6-oauth-authentication-for-snowflake) 단계를 따르세요.

### 3단계: 로드된 데이터로 Tellius에서 비즈니스 보기 생성

자연어 검색 및 자동화된 인사이트를 사용하려면 [비즈니스 보기](https://help.tellius.com/article/hy9yvh5tom-create-business-view)를 생성하고 Snowflake 연결에서 데이터 세트를 선택합니다.

### 4단계: Tellius를 사용하여 데이터에서 최대한의 가치 창출

Tellius에는 플랫폼의 기능을 안내하는 가이드 인터페이스가 있습니다. 추가 질문과 안내는 전체 [지식 자료](https://help.tellius.com/)를 참조하세요.