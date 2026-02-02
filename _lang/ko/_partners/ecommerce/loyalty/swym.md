---
nav_title: Swym
article_title: Swym
description: "이 참고 문서에서는 쇼핑객이 제품을 저장하고 웹사이트, 모바일 앱, 리테일 스토어에서 원활하게 쇼핑을 이어갈 수 있도록 지원하는 Braze와 Swym의 파트너십에 대해 설명합니다."
alias: /partners/swym/
page_type: partner
search_tag: Partner
---

# Swym

> [Swym은](https://getswym.com/) 위시리스트, 나중에 저장, 선물 등록 및 재고 부족 알림을 통해 이커머스 브랜드가 쇼핑 의도를 파악할 수 있도록 지원합니다. 풍부한 권한 기반 데이터를 사용하여 하이퍼 타겟팅 캠페인을 제작하고 개인화된 쇼핑 경험을 제공하여 참여를 유도하고 전환율을 높이며 로열티를 높일 수 있습니다.

*이 통합은 Swym에서 유지 관리합니다.*

## 통합 정보

Swym과 Braze의 통합을 통해 고객의 의도를 판매로 전환하는 개인화된 이벤트 중심 마케팅 캠페인을 제공할 수 있습니다. 통합 기능을 사용하면 쇼핑객이 중단한 부분을 다시 시작하고, 쇼핑 여정 전반에 걸쳐 다른 사람들과 협업하며, 성능/성과가 뛰어난 리타겟팅 캠페인을 받을 수 있습니다.

## 필수 조건

Before you start, you'll need the following:

| Prerequisite          | 설명                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Swym  | 전자상거래 플랫폼(Shopify 또는 BigCommerce)에 Swym 위시리스트 플러스, 백 인 스톡 앱 또는 둘 다 설치되어 있어야 하며 Enterprise 플랜을 사용 중이어야 합니다.       |
| A Braze REST API key  | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| A Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance.                                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## 사용 사례

Swym의 위시리스트 플러스 및 품절 알림 앱을 Braze와 연결하면 위시리스트 추가, 품절 알림, 가격 인하 알림, 리마인더 등의 쇼핑객 활동 이벤트를 커스텀 이벤트로 Braze에 자동으로 전송할 수 있습니다. 이러한 이벤트는 Braze에서 자동화된 메시지를 트리거하는 데 사용할 수 있으며, 이를 통해 시의적절하고 관련성 있는 매력적인 커뮤니케이션을 제공하여 고객이 다시 구매로 이어질 수 있도록 유도합니다.

## Swym 통합하기

### 1단계: Swym 앱을 Braze에 연결하기

현재 Swym과의 Braze 커런츠 통합은 관리형 통합이며 셀프 서비스가 아닙니다. 시작하려면 Swym 지원팀( [support@getswym.com](mailto:support@getswym.com) )에 문의하여 다음 정보를 제공하면 Swym에서 대신 통합을 설정할 수 있습니다:

1. `users.track` 권한으로 Braze 대시보드에서 [REST API 키를]({{site.baseurl}}/api/basics/#about-rest-api-keys) 생성합니다.

![Braze에서 API 키 생성하기.]({% image_buster /assets/img/swym/braze-api-key.png %})

{% alert important %}
API 키를 보호하기 위해 Swym에서는 일회성 자동 파괴 링크 도구(예: [OneTimeSecret](https://onetimesecret.com/))를 사용하여 자격 증명을 안전하게 공유할 것을 권장합니다.
{% endalert %}

{: start="2"}
2\. Braze는 대시보드와 REST 엔드포인트를 위한 여러 인스턴스를 관리합니다. 프로비저닝할 인스턴스에 대한 [REST 엔드포인트를]({{site.baseurl}}/api/basics/#endpoints) 입력합니다.

3. API 키와 인스턴스 URL을 Swym 지원팀에 공유하면 통합을 설정하고 확인을 통해 응답해 드립니다.

4. 설정이 완료되면 Swym의 커스텀 이벤트가 Braze에 자동으로 등록됩니다. Braze 대시보드에서 **데이터 설정** > 커스텀 이벤트로 이동하여 등록된 Swym 이벤트 목록을 확인할 수 있습니다. 

5. 해당 커스텀 이벤트의 **속성 관리를** 선택하면 각 Swym 이벤트의 속성을 볼 수 있습니다. 이러한 속성정보에는 메시지를 개인화하는 데 사용할 수 있는 이벤트 값이 포함되어 있습니다.

![Braze의 커스텀 속성.]({% image_buster /assets/img/swym/braze-custom-properties.png %})

### 2단계: Braze에 보내고 싶은 이벤트 가입하기

위시리스트 플러스 앱에서 **마케팅** 탭으로 이동하여 **자동화** 섹션을 찾습니다. 여기에서 가입할 이벤트를 선택할 수 있습니다. 

![가입할 이벤트.]({% image_buster /assets/img/swym/braze-event-subscription.png %})

#### Swym 위시리스트 플러스 앱 이벤트

| Event name | 이 이벤트가 트리거되는 경우 |  
|------------|------------------------------|  
| 위시리스트 공유 | 쇼핑객이 다른 사람과 위시리스트를 공유하는 경우 |  
| 위시리스트에 추가 | 쇼핑객이 위시리스트에 상품을 추가하는 경우 |  
| 위시리스트 알림 | 쇼핑객의 위시리스트에 있는 품목에 대한 알림|   
| 나중에 알림을 위해 저장됨 | 쇼핑객의 나중에 저장된 품목에 대한 알림 |  
| 가격 하락 알림 | 위시리스트에 있는 제품 판매 시작 |  
| 재고 부족 알림 | 위시리스트에 있는 제품의 재고가 부족합니다. |  
| 재고 없음 알림 | 위시리스트에 있는 제품이 재입고되었습니다. |  
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Swym 재고 알림 앱 이벤트

| 이벤트 이름 | 이 이벤트가 트리거되는 경우 |  
|------------|------------------------------|  
| 재고 있음 확인 | 제품이 재입고되면 알림을 받도록 가입한 구매자 |  
| 재입고 알림 | 구매자가 품절 알림을 요청한 제품이 재입고된 경우 |  
| 재입고 알림 | 후속 알림(일반적으로 첫 번째 재입고 알림 후 약 24시간 후, 구성 가능)|   
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### 3단계: Create a Braze campaign or Canvas

쇼핑객을 위한 개인화된 메시지 전달을 자동화하려면 가입한 각 이벤트에 대해 별도의 캠페인 또는 Braze에서 캔버스를 생성해야 합니다. 각 캠페인 또는 캔버스는 특정 이벤트에 따라 트리거되도록 구성하고 해당 이벤트 속성정보를 사용하여 메시지에 동적 콘텐츠를 채우도록 해야 합니다. 단계별 안내는 [시작하기를 참조하세요: 캠페인 및 캔버스]({{site.baseurl}}/user_guide/getting_started/campaigns_canvases/).

![액션 기반 이벤트입니다.]({% image_buster /assets/img/swym/braze-canvas-setup.png %})

자세한 내용은 [스윔 도움말 센터를](https://help.getswym.com/en/articles/12344153-braze-integration) 참조하거나 스윔 지원팀( [support@getswym.com](mailto:support@getswym.com))으로 문의하세요. 