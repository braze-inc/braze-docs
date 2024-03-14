---
nav_title: Friendbuy
article_title: Friendbuy
description: "Learn how to integrate Friendbuy with Braze."
alias: /partners/friendbuy/
page_type: partner
search_tag: Partner
layout: dev_guide

---

# Friendbuy

> Leverage the integration between Friendbuy and Braze to expand your email and SMS capabilities while effortlessly automating your referral and loyalty program communications. Braze will generate customer profiles for all the opted-in phone numbers collected via Friendbuy.

## Prerequisites

Before you start, you'll need the following:

| Prerequisite          | Description                                                                                                                              |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| A Friendbuy account   | A [Friendbuy account][1] is required to take advantage of this partnership.                                                              |
| A Braze REST API key  | A Braze REST API key with `users.track` permissions. This can be created in the Braze dashboard from **Settings** > **API Keys**.        |
| A Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints), which depends on the URL for your Braze instance. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can create an API key at **Developer Console** > **API Settings**.
{% endalert %}

## Integrating Friendbuy

In [Friendbuy][1], go to **Developer Center** > **Integrations**, then on the Braze integration card select **Add integration**.

![The Braze integration card in Friendbuy.]()

In FIELD_NAME, enter your REST endpoint and API Key, then select **Install Integration**.

![The Friendbuy integration form.][101]

Go to back to your [Friendbuy account][1] and refresh the page. If you successfully integrated Braze, you'll see a message similar to the following:

![integration installed][102]

## How customer data is sent to Braze

Customer data collected in your referral program will be added to the respective Braze profile after a customer interacts with your referral program widgets. Email is used as the identifier for creating and updating Braze profiles. Important to note, customer data will **only** be sent to Braze if the customer **opts-in** through the referral widget by selecting the opt-in boxes.

For example, if a customer enters both their email and phone number in the widget but only checks the opt-in box for email marketing (and leaves the SMS marketing opt-in box unchecked), then only the email address will be sent to Braze. If a customer submits their contact information without either opt-in box checked, customer data will not be sent to Braze since consent was not collected.

The opt-in checkboxes are required to collect consent from the customer indicating they would like to receive additional emails and/or SMS messages from your company. See an example referral widget below:

![referral widget][103]

{% alert note %}
We use the international standard (E.164) to confirm valid phone numbers. If an invalid number is submitted, it will not be sent to Braze. Ex: 555-555-5555.
{% endalert %}

### Custom Attributes

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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

[1]: https://retailer.friendbuy.io/
[101]: {% image_buster /assets/img/Friendbuy/install_form.png %}
[102]: {% image_buster /assets/img/Friendbuy/install_success.png %}
[103]: {% image_buster /assets/img/Friendbuy/referral_widget.png %}
