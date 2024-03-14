---
nav_title: Friendbuy
article_title: Friendbuy
page_order: 1

description: "Friendbuy integration set-up documentation."
alias: /partners/Friendbuy/

page_type: partner
search_tag: Partner
layout: dev_guide
---

# Friendbuy

> Leverage the integration between Friendbuy and Braze to expand your email and SMS capabilities while effortlessly automating your referral and loyalty program communications. Braze will generate customer profiles for all the opted-in phone numbers collected via Friendbuy.

## Installation Instructions

1. REST Endpoint is needed to integrate with Braze. This can be found [here][1].
  - Use the table provided on the API overview page to match the URL of the dashboard you use to the correct REST Endpoint.
  - To find your URL, log into Braze. If the URL you see is https://dashboard-01.braze.com, the corresponding REST Endpoint would be https://rest.iad-01.braze.com.
  - If you need assistance, open a [support ticket](https://www.braze.com/docs/braze_support/).
2. Confirm your API Key. In your Braze account, go to **Settings > API Keys**. A REST API key is required with every request to the Braze API. When generating a new API key, be sure to select the *User Data* and *Email* permissions.
3. Log into your [Friendbuy][3] account and go to **Developer Center > Integrations** tab > click on **Add integration** on the Braze integration card.
4. Paste your **REST Endpoint**, and your **API Key** in the provided fields.
    ![integration form fields][101]
5. Click **Install Integration....**
6. Go back into your **Friendbuy** account and refresh the page to confirm the Braze integration has been successfully installed. A blue checkmark and success message will appear on the card confirming installation.

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

| Custom Attribute Name            | Definition                                                                                          | Data Type |
|----------------------------------|-----------------------------------------------------------------------------------------------------|-----------|
| **Friendbuy Referral Status**    | Referrers are categorized as *Advocate* and referees are categorized as *Referred Friend*           | String    |
| **Friendbuy Customer Name**      | The name the customer entered when submitting their info through a referral widget                 | String    |
| **Friendbuy Referral Link**      | A personal referral link (PURL) generated for an Advocate. For example, https://fbuy.io/EzcW        | String    |
| **Friendbuy Date of Last Share** | The date and time the Advocate last shared with a Friend via any share channel. If the Advocate has not shared yet, the property won't be visible. | Time      |
| **Friendbuy Campaign ID**        | The Campaign ID associated with the personal referral link generated for an Advocate                | String    |
| **Friendbuy Campaign Name**      | The Campaign Name associated with the personal referral link generated for an Advocate              | String    |
| **Friendbuy Coupon Code**        | The most recent Referral coupon code distributed to the customer. Note: only one code will be displayed | String    |
| **Friendbuy Coupon Value**       | The currency value of the most recent coupon code distributed to the customer.                      | Number    |
| **Friendbuy Coupon Status**      | The status of the most recent coupon code distributed to the customer. Note: status will be 'distributed' or 'redeemed' | String    |
| **Friendbuy Coupon Currency**    | Currency code (USD, CAD, etc.) or percent (%) associated with the most recent coupon code distributed to the customer. | String    |
| **Friendbuy Coupon Campaign ID** | The Campaign ID associated with the coupon code generated for a customer.                           | String    |

[1]: https://www.braze.com/docs/api/basics/
[3]: https://retailer.friendbuy.io/

[101]: {% image_buster /assets/img/Friendbuy/install_form.png %}
[102]: {% image_buster /assets/img/Friendbuy/install_success.png %}
[103]: {% image_buster /assets/img/Friendbuy/referral_widget.png %}
