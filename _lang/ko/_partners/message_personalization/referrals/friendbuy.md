---
nav_title: Friendbuy
article_title: Friendbuy
description: "Learn how to integrate Friendbuy with Braze."
alias: /partners/friendbuy/
page_type: partner
search_tag: Partner

---

# Friendbuy

> [Friendbuy와](https://www.friendbuy.com/) Braze의 통합을 통해 이메일과 SMS 기능을 확장하는 동시에 추천 및 로열티 프로그램 커뮤니케이션을 손쉽게 자동화할 수 있습니다. Braze will generate customer profiles for all the opted-in phone numbers collected via Friendbuy.

_This integration is maintained by Friendbuy._

## Prerequisites

Before you start, you'll need the following:

| Prerequisite          | Description                                                                                                                              |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| A Friendbuy account   | A [Friendbuy account](https://retailer.friendbuy.io/) is required to take advantage of this partnership.                                                              |
| A Braze REST API key  | A Braze REST API key with `users.track` permissions. This can be created in the Braze dashboard from **Settings** > **API Keys**.        |
| A Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints), which depends on the URL for your Braze instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integrating Friendbuy

[Friendbuy에서](https://retailer.friendbuy.io/) **개발자 센터** > **연동** 카드로 이동한 다음 Braze 연동 카드에서 **연동 추가를** 선택합니다.

![Friendbuy의 Braze 통합 카드.]({% image_buster /assets/img/friendbuy/choosing_braze.png %}){: style="max-width:75%;"}

양식에 REST 엔드포인트와 API 키를 입력한 다음, **통합 설치**를 선택합니다.

![Friendbuy 통합 양식입니다.]({% image_buster /assets/img/friendbuy/install_form.png %}){: style="max-width:55%;"}

[Friendbuy 계정으로](https://retailer.friendbuy.io/) 돌아가서 페이지를 새로 고칩니다. 통합에 성공했다면 다음과 비슷한 메시지가 표시됩니다:

![통합 설치]({% image_buster /assets/img/friendbuy/install_success.png %}){: style="max-width:55%;"}

### 사용자 지정 속성

| Custom Attribute Name            | Definition                                                                                                                                         | Data Type |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| **Friendbuy Referral Status**    | Referrers are categorized as *Advocate* and referees are categorized as *Referred Friend*                                                          | String    |
| **Friendbuy Customer Name**      | The name the customer entered when submitting their info through a referral widget                                                                 | String    |
| **Friendbuy Referral Link**      | A personal referral link (PURL) generated for an Advocate. For example, https://fbuy.io/EzcW                                                       | String    |
| **Friendbuy Date of Last Share** | The date and time the Advocate last shared with a Friend via any share channel. If the Advocate has not shared yet, the property won't be visible. | Time      |
| **Friendbuy Campaign ID**        | The Campaign ID associated with the personal referral link generated for an Advocate                                                               | String    |
| **Friendbuy Campaign Name**      | The Campaign Name associated with the personal referral link generated for an Advocate                                                             | String    |
| **Friendbuy Coupon Code**        | The most recent Referral coupon code distributed to the customer. Note: only one code will be displayed                                            | String    |
| **Friendbuy Coupon Value**       | The currency value of the most recent coupon code distributed to the customer.                                                                     | Number    |
| **Friendbuy Coupon Status**      | The status of the most recent coupon code distributed to the customer. Note: status will be 'distributed' or 'redeemed'                            | String    |
| **Friendbuy Coupon Currency**    | Currency code (USD, CAD, etc.) or percent (%) associated with the most recent coupon code distributed to the customer.                             | String    |
| **Friendbuy Coupon Campaign ID** | The Campaign ID associated with the coupon code generated for a customer.                                                                          | String    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Default behavior

고객 데이터를 Braze로 전송하기 전에 고객은 추천 위젯을 통해 다음 상자 중 하나 이상의 확인란을 선택하여 옵트인해야 합니다:

![추천 위젯]({% image_buster /assets/img/friendbuy/referral_widget.png %})

{% alert note %}
Friendbuy uses the international standard (E.164) to verify real phone numbers. Invalid numbers, such as `555-555-5555`, will not be sent to Braze.
{% endalert %}

### Checkbox behavior

| Checkbox selected | Behavior                                                        |
|-------------------|-----------------------------------------------------------------|
| Email only        | Only the customer's email address is sent to Braze.             |
| Phone only        | Only the customer's phone number is sent to Braze.              |
| Neither           | No customer data is sent to Braze.                              |
| Both              | The customer's email address and phone number is sent to Braze. |


