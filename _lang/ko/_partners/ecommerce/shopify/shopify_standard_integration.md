---
nav_title: Shopify 표준 통합 설정
article_title: "Shopify 표준 통합 설정"
description: "이 참조 문서에서는 표준 Shopify 통합을 설정하는 방법을 설명합니다."
page_type: partner
search_tag: Partner
alias: /shopify_standard_integration/
page_order: 1
---

# Shopify 표준 통합 설정

> 이 페이지에서는 Shopify 온라인 스토어를 사용하는 사용자를 위한 표준 통합을 사용하여 Braze와 Shopify를 통합하는 방법을 안내합니다. Shopify 헤드리스 사이트를 사용하거나 더 맞춤화된 솔루션을 구현하려는 경우 [Shopify 커스텀 통합 설정]({{site.baseurl}}/shopify_custom_integration/)을 참조하세요.

## 1단계: Shopify 스토어 연결

1. Braze에서 **파트너 통합** > **기술 파트너**로 이동한 다음 "Shopify"를 검색합니다.

{% alert note %}
이전 탐색을 사용하는 경우 **통합** 아래에서 **기술 파트너**를 찾을 수 있습니다.
{% endalert %}

{: start="2"}
2. Shopify 파트너 페이지에서 **설정 시작**을 선택하여 통합 프로세스를 시작합니다.<br><br>![설정 시작 버튼이 있는 Shopify 통합 페이지.]({% image_buster /assets/img/Shopify/begin_setup.png %})<br><br> 
3. Shopify 앱 스토어에서 Braze 애플리케이션을 설치합니다.<br><br>![애플리케이션 설치 버튼이 있는 Braze 앱 스토어 페이지.]({% image_buster /assets/img/Shopify/shopify_log_in.png %}){: style="max-width:70%;"}

{% alert note %}
Shopify 계정이 둘 이상의 스토어와 연결되어 있는 경우 페이지 오른쪽 상단의 스토어 아이콘을 선택하고 **스토어 전환**을 선택하여 로그인한 스토어를 변경할 수 있습니다.
{% endalert %}

{: start="4"}
4. Braze 앱을 설치한 후 Shopify에 연결할 워크스페이스를 확인하기 위해 Braze로 리디렉션됩니다. Shopify 스토어는 하나의 워크스페이스에만 연결할 수 있습니다. 전환이 필요한 경우 올바른 워크스페이스를 선택하세요.<br><br>![올바른 워크스페이스에 있는지 확인하는 창.]({% image_buster /assets/img/Shopify/confirm_workspace1.png %}){: style="max-width:70%;"}

{: start="5"}
5. **설정 시작**을 선택합니다.<br><br>![도메인 입력 필드와 설정 시작 버튼이 있는 "통합 설정".]({% image_buster /assets/img/Shopify/choose_account.png %})

## 2단계: Braze Web SDK 활성화

Shopify 온라인 스토어의 경우 표준 설정을 선택하여 Braze Web SDK와 JavaScript SDK를 자동으로 구현할 수 있습니다.

![표준 설정 또는 커스텀 설정을 통해 구현하는 옵션이 있는 "Web SDK 활성화" 단계.]({% image_buster /assets/img/Shopify/sdk_setup.png %})

표준 설정 온보딩 경로를 선택한 후 Braze가 SDK를 초기화하고 로드할 시점을 다음 옵션 중에서 선택해야 합니다: 
- 사이트 방문 시(예: 세션 시작)
    - 식별된 사용자와 익명 사용자 모두 추적
- 계정 가입 시(예: 계정 로그인)
    - 식별된 사용자만 추적
    - 사이트 방문자가 계정에 가입하거나 로그인할 때 데이터 추적 시작

## 3단계: Shopify 데이터 구성

### 표준 데이터 설정

{% multi_lang_include alerts/important_alerts.md alert='Shopify cart token alias' %}

이제 추적할 Shopify 데이터를 선택합니다.

![행동 이벤트 및 사용자 속성을 추적하는 체크박스가 있는 "Shopify 데이터 추적" 섹션.]({% image_buster /assets/img/Shopify/tracking_shopify_data.png %})

다음 이벤트는 표준 통합에서 기본적으로 활성화됩니다.

| Braze 권장 이벤트 | Shopify 커스텀 이벤트 | Shopify 커스텀 속성 |
| --- | --- | --- |
| {::nomarkdown}<ul><li>Product viewed</li><li>Cart updated</li><li>Checkout started</li><li>Order placed</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_account_login</li><li>shopify_paid_order</li><li>shopify_order_canceled</li><li>shopify_order_refunded</li><li>shopify_order_fulfilled</li><li>shopify_order_partially_fulfilled</li></ul>{:/} | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li><li>shopify_province</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2  .reset-td-br-3 role="presentation"}

통합을 통해 추적되는 데이터에 대한 자세한 내용은 [Shopify 데이터 기능]({{site.baseurl}}/shopify_data_features/)을 참조하세요.

{% multi_lang_include alerts/important_alerts.md alert='Shopify customer create' %}

### 과거 데이터 백필 설정

표준 설정을 통해 Shopify 통합 연결 이전 최근 90일간의 Shopify 고객 및 주문 데이터를 초기 로드할 수 있는 옵션이 있습니다. 이를 위해 통합의 일부로 초기 데이터 로드를 포함하는 체크박스를 선택하세요. 

{% alert note %}
과거 백필 데이터는 매출 보고에 포함되지 않습니다. 백필된 주문 완료 이벤트는 세분화에만 사용할 수 있습니다.
{% endalert %}

![과거 데이터 백필 토글.]({% image_buster /assets/img/Shopify/historical_data_backfill_sync.png %})

이 표에는 백필을 통해 초기 로드되는 데이터가 포함되어 있습니다.

| Braze 권장 이벤트 | Shopify 커스텀 이벤트 | Braze 표준 속성 | Braze 구독 상태 |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>Order placed</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>Email</li><li>First Name</li><li>Last Name</li><li>Phone</li><li>City</li><li>Country</li></ul>{:/} | {::nomarkdown}<ul><li>이 Shopify 스토어와 연결된 이메일 마케팅 구독</li><li>이 Shopify 스토어와 연결된 SMS 마케팅 구독</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

Shopify 고객 레코드가 Braze에 로드되면 Shopify 고객 ID가 Braze 외부 ID로 사용됩니다. 

{% alert note %}
활성 캠페인 또는 캔버스가 있는 기존 Braze 고객인 경우 자세한 내용은 [Shopify 데이터 기능]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill)을 참조하세요. 
{% endalert %}

### (고급) 커스텀 데이터 추적 설정

Braze SDK를 사용하면 이 통합의 표준 이벤트를 넘어서는 커스텀 이벤트 또는 커스텀 속성을 추적할 수 있습니다. 커스텀 이벤트는 스토어에서의 고유한 상호작용을 캡처합니다. 예를 들면 다음과 같습니다:

<style>
#custom-data td {
    word-break: break-word;
    width: 50%;
}
</style>

<table style="width: 100%;">
  <thead>
    <tr>
      <th style="width: 50%;">커스텀 이벤트</th>
      <th style="width: 50%;">커스텀 속성</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>커스텀 할인 코드 사용</li>
          <li>개인화된 제품 추천과의 상호작용</li>
          <li>주문에 선물 메시지 추가</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>선호 브랜드 또는 제품</li>
          <li>선호 쇼핑 카테고리</li>
          <li>멤버십 또는 로열티 상태</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

커스텀 데이터를 추적하면 사용자 행동에 대한 심층적인 인사이트를 확보하고 추가적인 개인화를 지원할 수 있습니다. 커스텀 이벤트를 구현하려면 `theme.liquid` 파일에서 [스토어프론트의 테마 코드](https://help.shopify.com/en/manual/online-store/themes/theme-structure/extend/edit-theme-code)를 편집해야 합니다. 개발자의 도움이 필요할 수 있습니다.

예를 들어, 다음 JavaScript 스니펫은 현재 사용자가 뉴스레터를 구독하는지 추적하고 이를 Braze의 프로필에 커스텀 이벤트로 기록합니다:

```javascript
braze.logCustomEvent(
  “subscribed_to_newsletter”,
  {
    newsletterName: ‘News and Offers’,
    customerEmail: ‘customer_1@gmail.com’,
    sendOffers: true
  }
);

```

이벤트 또는 커스텀 속성을 기록하려면 사용자의 기기에서 SDK가 초기화(활동 수신 대기)되어 있어야 합니다. 커스텀 데이터 기록에 대해 자세히 알아보려면 [User object](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) 및 [logCustomEvent object](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent)를 참조하세요.

## 4단계: 사용자 관리 방법 구성하기 {#step-4}

드롭다운에서 `external_id` 유형을 선택합니다. 

!["가입자 수집" 섹션.]({% image_buster /assets/img/Shopify/external_id_standard.png %})

{% alert important %}
이메일 주소 또는 해시된 이메일 주소를 Braze 외부 ID로 사용하면 데이터 소스 전반에서 ID 관리를 간소화할 수 있습니다. 그러나 사용자 개인정보 보호 및 데이터 보안에 대한 잠재적 위험을 고려하는 것이 중요합니다.<br><br>

- **추측 가능한 정보:** 이메일 주소는 쉽게 추측할 수 있어 공격에 취약합니다.
- **악용 위험:** 악의적인 사용자가 웹 브라우저를 변조하여 다른 사람의 이메일 주소를 외부 ID로 전송하면 민감한 메시지나 계정 정보에 접근할 수 있습니다.
{% endalert %}

기본적으로 Braze는 Shopify의 이메일을 외부 ID로 사용하기 전에 소문자로 자동 변환합니다. 이메일 또는 해시된 이메일을 외부 ID로 사용하는 경우, 외부 ID로 할당하기 전이나 다른 데이터 소스에서 해시하기 전에 이메일 주소도 소문자로 변환되었는지 확인하세요. 이렇게 하면 외부 ID의 불일치를 방지하고 Braze에서 중복 고객 프로필이 생성되는 것을 막을 수 있습니다.

{% alert note %}
다음 단계는 외부 ID 선택에 따라 달라집니다:<br><br>
- **커스텀 외부 ID 유형을 선택한 경우:** 4.1~4.3단계를 완료하여 커스텀 외부 ID 구성을 설정합니다.
- **Shopify 고객 ID, 이메일 또는 해시된 이메일을 선택한 경우:** 4.1~4.3단계를 건너뛰고 바로 4.4단계로 진행합니다.
{% endalert %}

### 4.1단계: `braze.external_id` 메타필드 만들기

1. Shopify 관리자 패널에서 **설정** > **메타필드 및 메타오브젝트**로 이동합니다.
2. **고객** > **정의 추가**를 선택합니다.
3. **이름**에 `braze.external_id`를 입력합니다. 
4. 자동 생성된 네임스페이스와 키(`custom.braze_external_id`)를 선택하여 편집하고 `braze.external_id`로 변경합니다.
5. **유형**에서 **ID 유형**을 선택합니다.

메타필드가 생성되면 고객에 대해 메타필드를 채웁니다. 다음과 같은 방법을 권장합니다:

- **고객 생성 웹훅 수신:** [`customer/create` 이벤트](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks)를 수신하도록 웹훅을 설정합니다. 이를 통해 새 고객이 생성될 때 메타필드를 작성할 수 있습니다.
- **기존 고객 백필:** [Admin API](https://shopify.dev/docs/api/admin-graphql) 또는 [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer)를 사용하여 이전에 생성된 고객의 메타필드를 백필합니다.

### 4.2단계: 외부 ID를 검색할 엔드포인트 만들기

외부 ID를 검색하기 위해 Braze가 호출할 수 있는 공용 엔드포인트를 만들어야 합니다. 이를 통해 Shopify에서 `braze.external_id` 메타필드를 직접 제공할 수 없는 시나리오에서 Braze가 ID를 가져올 수 있습니다.

#### 엔드포인트 사양

**방법:** GET

Braze는 다음 매개변수를 엔드포인트로 전송합니다:

| 매개변수            | 필수 | 데이터 유형 | 설명                                                      |
|----------------------|----------|-----------|------------------------------------------------------------------|
| shopify_customer_id  | 예      | 문자열    | Shopify 고객 ID입니다.                                         |
| shopify_storefront   | 예      | 문자열    | 요청에 대한 스토어프론트 이름입니다. 예: `<storefront_name>.myshopify.com` |
| email_address        | 아니요       | 문자열    | 로그인한 사용자의 이메일 주소입니다. <br><br>특정 웹훅 시나리오에서는 이 필드가 누락될 수 있습니다. 엔드포인트 로직에서 null 값을 처리할 수 있어야 합니다(예: 내부 로직에 필요한 경우 shopify_customer_id를 사용하여 이메일을 가져옵니다). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

#### 엔드포인트 예시

```http
GET https://mystore.com/custom_id?shopify_customer_id=1234&email_address=bob@braze.com&shopify_storefront=dev-store.myshopify.com
```

#### 예상 응답
Braze는 외부 ID JSON을 반환하는 `200` 상태 코드를 기대합니다:
```json
{
  "external_id": "my_external_id"
}
```

#### 유효성 검사
`shopify_customer_id` 및 `email_address`(있는 경우)가 Shopify의 고객 값과 일치하는지 검증하는 것이 중요합니다. [Shopify Admin API](https://shopify.dev/docs/api/admin-graphql) 또는 [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer)를 사용하여 이러한 매개변수의 유효성을 검사하고 올바른 `braze.external_id` 메타필드를 검색할 수 있습니다.

#### 실패 동작 및 병합
`200` 이외의 상태 코드는 모두 실패로 간주됩니다.

- **병합 영향:** 엔드포인트가 실패하면(`200`이 아닌 값을 반환하거나 시간 초과), Braze는 외부 ID를 검색할 수 없습니다. 따라서 Shopify 사용자와 Braze 고객 프로필 간의 병합은 해당 시점에 이루어지지 않습니다.
- **재시도 로직:** Braze는 표준 즉시 네트워크 재시도를 시도할 수 있지만, 실패가 지속되면 다음 적격 이벤트(예: 사용자가 프로필을 업데이트하거나 결제를 완료할 때)까지 병합이 연기됩니다.
- **지원 가능성:** 적시에 사용자 병합을 지원하려면 엔드포인트의 가용성이 높고 선택 사항인 `email_address` 필드를 원활하게 처리할 수 있는지 확인하세요.

### 4.3단계: 외부 ID 입력

[4단계](#step-4)를 반복하고 Braze 외부 ID 유형으로 커스텀 외부 ID를 선택한 후 엔드포인트 URL을 입력합니다.

#### 고려 사항

- Braze가 엔드포인트에 요청을 보낼 때 외부 ID가 생성되지 않은 경우, 통합은 `changeUser` 함수가 호출될 때 기본적으로 Shopify 고객 ID를 사용합니다. 이 단계는 익명 사용자 프로필을 식별된 고객 프로필과 병합하는 데 매우 중요합니다. 따라서 일시적으로 워크스페이스 내에 여러 유형의 외부 ID가 존재할 수 있습니다.
- `braze.external_id` 메타필드에서 외부 ID를 사용할 수 있으면 통합에서 이 외부 ID에 우선순위를 지정하여 할당합니다. 
    - 이전에 Shopify 고객 ID가 Braze 외부 ID로 설정된 경우 `braze.external_id` 메타필드 값으로 대체됩니다. 

### 4.4단계: Shopify에서 이메일 또는 SMS 옵트인 수집(선택 사항)

Shopify에서 이메일 또는 SMS 마케팅 옵트인을 수집하는 옵션이 있습니다. 

이메일 또는 SMS 채널을 사용하는 경우 이메일 및 SMS 마케팅 옵트인 상태를 Braze에 동기화할 수 있습니다. Shopify에서 이메일 마케팅 옵트인을 동기화하면 Braze는 해당 특정 스토어와 연결된 모든 사용자에 대해 이메일 구독 그룹을 자동으로 생성합니다. 이 구독 그룹에 고유한 이름을 지정해야 합니다.

![이메일 또는 SMS 마케팅 옵트인을 수집하는 옵션이 있는 "가입자 수집" 섹션.]({% image_buster /assets/img/Shopify/collect_email_subscribers.png %})

{% alert note %}
[Shopify 개요]({{site.baseurl}}/shopify_overview/)에서 언급한 바와 같이, 서드파티 캡처 양식을 사용하려면 개발자가 Braze SDK 코드를 통합해야 합니다. 이를 통해 양식 제출에서 이메일 주소와 글로벌 이메일 구독 상태를 캡처할 수 있습니다. 구체적으로 `theme.liquid` 파일에 다음 메서드를 구현하고 테스트해야 합니다:<br><br>
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail): 고객 프로필에 이메일 주소를 설정합니다
- [setEmailNotificationSubscriptionType](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype): 글로벌 이메일 구독 상태를 업데이트합니다
{% endalert %}

## 5단계: 제품 동기화(선택 사항)

Shopify 스토어의 모든 제품을 Braze 카탈로그에 동기화하여 더 깊은 메시징 개인화를 구현할 수 있습니다. 자동 업데이트가 거의 실시간으로 이루어지므로 카탈로그에 최신 제품 세부 정보가 반영됩니다. 자세한 내용은 [Shopify 제품 동기화]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/)를 확인하세요.

!["카탈로그 제품 식별자"로 "Shopify Variant ID"가 설정된 설정 프로세스의 4단계.]({% image_buster /assets/img/Shopify/sync_products_step1.png %}){: style="max-width:80%;"}

## 6단계: 채널 활성화(선택 사항)

설정에서 구성하여 개발자 없이 인앱 메시지를 활성화할 수 있습니다.

![인브라우저 메시징 옵션이 있는 채널 활성화 설정 단계.]({% image_buster /assets/img/Shopify/activate_channels_standard.png %})

{% alert note %}
Braze는 인브라우저 메시지를 통해 이메일 주소 및 전화번호와 같은 방문자 정보를 수집합니다. 이 정보는 Shopify로 전송됩니다. 판매자는 이 데이터를 통해 매장 방문자를 인식하고 보다 개인화된 쇼핑 경험을 제공할 수 있습니다. 자세한 내용은 [Visitor API](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api)를 참조하세요.
{% endalert %}

### 추가 SDK 채널 지원

Braze SDK는 콘텐츠 카드를 포함한 다양한 메시징 채널을 지원합니다.

#### 콘텐츠 카드 및 기능 플래그

콘텐츠 카드 또는 기능 플래그를 추가하려면 개발자와 협력하여 필요한 SDK 코드를 `theme.liquid` 파일에 직접 삽입해야 합니다. 자세한 지침은 [Braze SDK 통합]({{site.baseurl}}/developer_guide/sdk_integration/)을 참조하세요. 

#### 웹 푸시 알림

현재 웹 푸시는 Shopify 통합에서 지원되지 않습니다. 지원을 요청하려면 [Braze 제품 포털]({{site.baseurl}}/user_guide/administrative/access_braze/portal/)을 통해 제품 요청을 제출하세요.

## 7단계: 설정 완료

1. 설정을 구성한 후 **설정 완료**를 선택합니다.
2. Shopify 테마 설정에서 Braze 앱 임베드를 활성화합니다. **Shopify 열기**를 선택하면 Shopify 계정으로 리디렉션되어 스토어의 테마 설정에서 앱 임베드를 활성화할 수 있습니다. 

![Shopify에서 Braze 앱 임베드를 활성화해야 한다는 배너와 Shopify 열기 버튼.]({% image_buster /assets/img/Shopify/open_shopify.png %})

{: start="3"}
3. 앱 임베드를 활성화하면 설정이 완료됩니다!
통합 설정, 초기 데이터 동기화 상태 및 활성 Shopify 이벤트를 확인할 수 있는지 확인하세요. <br><br>![통합 설정을 표시하는 Shopify 파트너 페이지.]({% image_buster /assets/img/Shopify/install_complete.png %})