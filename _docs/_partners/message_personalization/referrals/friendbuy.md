---
nav_title: Friendbuy
article_title: Friendbuy
description: "Learn how to integrate Friendbuy with Braze."
alias: /partners/friendbuy/
page_type: partner
search_tag: Partner

---

# Friendbuy

> Use the integration between [Friendbuy](https://www.friendbuy.com/) and Braze to expand your email and SMS capabilities while effortlessly automating your referral and loyalty program communications. Braze will generate customer profiles for all the opted-in phone numbers collected via Friendbuy.

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

In [Friendbuy](https://retailer.friendbuy.io/), go to **Developer Center** > **Integrations**, then on the Braze integration card select **Add integration**.

![The Braze integration card in Friendbuy.]({% image_buster /assets/img/friendbuy/choosing_braze.png %}){: style="max-width:75%;"}

In the form, enter your REST endpoint and API Key, then select **Install Integration**.

![The Friendbuy integration form.]({% image_buster /assets/img/friendbuy/install_form.png %}){: style="max-width:55%;"}

Go to back to your [Friendbuy account](https://retailer.friendbuy.io/) and refresh the page. If your integration was successful, you'll see a message similar to the following:

![integration installed]({% image_buster /assets/img/friendbuy/install_success.png %}){: style="max-width:55%;"}

### Custom attributes

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

Before customer data can be sent to Braze, customers must opt-in through the referral widget by checking one or more boxes of the following boxes:

![referral widget]({% image_buster /assets/img/friendbuy/referral_widget.png %})

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


