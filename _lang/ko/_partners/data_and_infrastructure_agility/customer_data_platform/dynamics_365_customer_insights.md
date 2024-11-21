---
nav_title: Dynamics 365 고객 인사이트
article_title: Dynamics 365 고객 인사이트
description: "이 참조 문서에서는 캠페인이나 캔버스에서 사용하도록 고객 세그먼트를 Braze로 내보낼 수 있는 선도적인 엔터프라이즈 고객 데이터 플랫폼인 Dynamics 365 Customer Insights와 Braze 간의 파트너십을 간략히 설명합니다."
alias: /partners/dynamics_365_customer_insights/
page_type: partner
search_tag: Partner
---

# Dynamics 365 고객 인사이트
 
> [Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/)는 고객을 360도로 파악하여 개인화된 고객 경험을 제공하는 선도적인 엔터프라이즈 고객 데이터 플랫폼입니다.

Braze와 Dynamics 365 Customer Insights 통합을 통해 캠페인이나 캔버스에서 사용하도록 고객 세그먼트를 Braze로 내보낼 수 있습니다.

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Dynamics 365 고객 인사이트 계정 | 이 파트너십을 활용하려면 [Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) 계정이 필요합니다. 필요한 플러그인에 액세스하려면 관리자 액세스 권한이 있어야 Dynamics 365 Customer Insights 계정 내에서 연결을 보고 편집할 수 있습니다. |
| Braze REST API 키 | 모든 권한이 부여된 Braze REST API 키가 필요합니다. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: Braze 연결 설정

Customer Insights에서 **관리자 > 연결**로 이동합니다. 그런 다음, **연결 추가**를 선택하고 **Braze**를 선택하여 연결을 구성합니다. 

1. **표시 이름** 필드에 연결에 알아볼 수 있는 이름을 입력합니다. 
2. 이 연결을 사용할 수 있는 사용자를 선택합니다. 이 필드를 비워두면 기본값은 관리자가 됩니다. 자세한 내용은 [기여자가 내보내기를 위해 연결을 사용하도록 허용](https://docs.microsoft.com/en-us/dynamics365/customer-insights/connections#allow-contributors-to-use-a-connection-for-exports)을 참조하세요.
3. 계속 로그인하려면 Braze API 키를 입력하세요.
4. 데이터 및 개인정보 보호 준수를 확인하려면 **동의함**을 선택합니다.
5. Braze에 대한 연결을 초기화하려면 **연결**을 선택합니다.
6. **내보내기 사용자로 본인 추가**를 선택하고 Customer Insights 자격 증명을 제공합니다.
7. **저장**을 선택하여 연결을 완료합니다. 

### 2단계: 내보내기 구성

이 유형의 연결에 액세스할 수 있는 경우 이 내보내기를 구성할 수 있습니다. 자세한 내용은 [내보내기 개요](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#set-up-a-new-export)를 참조하세요.

1. 고객 인사이트에서 **데이터 > 내보내기로** 이동합니다. 새 내보내기를 생성하려면 **대상 추가**를 선택합니다.
2. **내보내기용 연결** 필드에서 브레이즈 섹션에 대한 연결을 선택합니다. 이 섹션 이름이 표시되지 않으면 이 유형의 연결을 사용할 수 없는 것입니다. 
3. 호스트 이름 필드에 REST 엔드포인트를 `rest.iad-03.braze.com` 형식으로 입력합니다.
4. **데이터 일치** 섹션의 **이메일** 필드에서 고객의 이메일 주소를 나타내는 필드를 선택합니다. 다음으로 **고객 ID** 필드에서 고객의 Braze ID를 나타내는 필드를 선택합니다. 데이터 일치를 위한 추가적인 선택적 필드를 선택할 수도 있습니다. 
5. 마지막으로, **저장**을 선택합니다. 

내보내기를 저장한다고 해서 내보내기가 바로 실행되는 것은 아닙니다. 이 내보내기는 [예약된 새로 고침이](https://docs.microsoft.com/en-us/dynamics365/customer-insights/system#schedule-tab) 있을 때마다 실행됩니다. [온디맨드 데이터 내보내기](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#run-exports-on-demand)를 수행할 수도 있습니다. 

### 이 통합 사용

세그먼트를 Braze로 성공적으로 내보내면 고객 프로필에서 Dynamics 365 Customer Insights에 있는 세그먼트와 이름이 동일한 커스텀 속성으로 세그먼트를 찾을 수 있습니다. 

이러한 사용자의 세그먼트를 만들려면 Braze에서 **세그먼트로** 이동하여 새 세그먼트를 만든 다음 **사용자 지정 속성을** 필터로 선택합니다. 여기에서 Dynamics 365 사용자 지정 속성을 선택할 수 있습니다. 세그먼트가 생성된 후에는 캠페인이나 캔버스를 만들 때 오디언스 필터로 선택할 수 있습니다.

{% alert note %}
이 통합에 대한 자세한 내용은 Microsoft의 Braze [통합 문서](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-braze)를 참조하세요.
{% endalert %}

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints