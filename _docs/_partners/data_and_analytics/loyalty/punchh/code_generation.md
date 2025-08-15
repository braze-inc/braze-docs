---
nav_title: Dynamic code generation
article_title: Punchh Dynamic Code Generation
page_order: 2
description: "This reference article outlines how to use Punchh dynamic code generation in Braze."
page_type: partner
search_tag: Partner
---

# Dynamic code generation with Punchh

> A coupon code is a unique code that can be used by a single user (either single or multiple use). The Punchh framework generates coupon codes, which can be processed within a mobile app or at the point-of-sale (POS) system.

_This integration is maintained by Punchh._

## About the integration

Using the Punchh coupon framework and Braze, you can achieve the following scenarios:

- Generate a coupon code when the guest clicks a coupon generation link in an email: The coupon code will be generated dynamically and shown on a web page.
- Generate a coupon code when the guest opens an email: The coupon code will be generated dynamically and shown as an image within the email.

## Integrating dynamic coupon code generation

### Step 1: Create a coupon campaign

1. Using a Punchh coupon campaign, create a dynamic generation coupon campaign as shown in the following image.
2. The Punchh coupon framework will generate the following parameters to enable dynamic coupon generation:
    - Dynamic coupon generation token: This is a system-generated security token for encryption.
    - Dynamic coupon generation URL: This URL will be embedded in the email as a link or image, as required by the business.

![The form for creating a coupon campaign in Punchh.]({% image_buster /assets/img/punchh/punchh8.png %}){: style="max-width:60%;"}

### Step 2: Generate signature and construct URL

The JWT.IO library decodes, verifies, and generates JSON web tokens, an open, industry-standard RFC 7519 method for representing claims securely between two parties. 

The following `ClaimType` names can be used to ensure the uniqueness of guests and coupons:

- `campaign_id`: represents the system-generated Punchh campaign ID.
- `email`: represents the user's email address. 
- `first_name`: captures the user's first name. 
- `last_name`: captures the user's last name.

To use the Punchh dynamic coupon code API, a JWT Token must be constructed. Add the following Liquid template to your Braze dashboard in the message body of the channel you'd like to use:

{% raw %}
```liquid
{% assign header = '{"alg":"HS256","typ":"JWT"}' | base64_encode | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% capture payload_raw %}

{
  "campaign_id": "CAMPAIGN_ID",
  "email": "{{${email_address}}}",
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}"
}

{% endcapture %}

{% assign payload = payload_raw | replace: ' ', '' | replace: '\n', '' | base64_encode | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% assign unsigned_token = header | append: "." | append: payload %}

{% assign secret = "DYNAMIC_COUPON_GENERATION_TOKEN" %}

{% assign signature_raw = unsigned_token | hmac_sha256_base64: secret %}

{% assign signature = signature_raw | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% assign jwt = unsigned_token | append: "." | append: signature %}

```
{% endraw %}


Replace the following:

| Placeholder        | Description                                          |
|--------------------|------------------------------------------------------|
| `DYNAMIC_COUPON_GENERATION_TOKEN` | Your dynamic coupon generation token. |
| `CAMPAIGN_ID`                     | Your campaign ID.                     |

### Step 3: Append coupon code to message body

#### Linking to Punchh web page

To link to a Puncch-hosted web page, add `{% raw %}{{jwt}}{% endraw %}` to the dynamic generation URL [you created earlier](#step-1-create-a-coupon-campaign-in-punchh). Your link should be similar to the following: 

{% raw %}
```
https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX?sign={{jwt}}
```
{% endraw %}

When a user clicks the coupon URL, they'll be redirected to a Punchh-hosted web page, where their generated coupon will be displayed.

![Example confirmation message after a user successfully generates a coupon code.]({% image_buster /assets/img/punchh/punchh7.png %})

#### Extracting code via JSON as plain text

To return a JSON response, append `{% raw %}{{jwt}}{% endraw %}` to the dynamic generation URL [you created earlier](#step-1-create-a-coupon-campaign-in-punchh), then add `.json` after the token in the URL string. Your link should be similar to the following:

{% raw %}
```liquid
https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.json?sign={{jwt}}
```
{% endraw %}

You could then leverage [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) to insert the code as plain text into any message body. For example:

{% raw %}
```liquid
{% connected_content https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.json?sign={{jwt}} :save punchh_coupon %}
{{punchh_coupon.coupon}}
````
{% endraw %}

#### Linking an image inside email content

To link the coupon code inside an image:

1. Append `{% raw %}{{jwt}}{% endraw %}` to the dynamic generation URL [you created earlier](#step-1-create-a-coupon-campaign-in-punchh).
2. Add `.png` after the token in the URL string.
3. Embed your link in an HTML {% raw %}`<img>`{% endraw %} tag.

{% tabs local %}
{% tab example input %}
{% raw %}
```liquid
<img src="https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.png?sign={{jwt}}">
````
{% endraw %}
{% endtab %}

{% tab example output %}
![Rendered output of the coupon code image tag.]({% image_buster /assets/img/punchh/punchh9.png %})
{% endtab %}
{% endtabs %}

## Error messages

| Error code | Error message | Description |
| --- | --- | --- |
| `coupon_code_expired` | This promo code has expired | The code is used after its configured expiration date. |
| `coupon_code_success` | Congratulations, Promo Code Applied Successfully. | The code is used successfully. |
| `coupon_code_error` | Please enter a valid promo code | The code used is invalid. |
| `coupon_code_type_error` | Incorrect coupon type. This coupon can only be redeemed at `%{coupon_type}`. | When a code supposed to be used at the POS is used in the Mobile app, this error will occur. |
| `usage_exceeded` | The usage for this coupon code's campaign is full. Please try next time. | The usage of the code exceeds the number of users allowed to use it. For example, if the dashboard configuration allows a code to be used by 3,000 users and the number of users exceeds 3,000, this error will occur. |
| `usage_exceeded_by_guest` | This promo code has already been processed. | The usage of the code by a user exceeds the number of times a user can use it. For example, the dashboard configuration allows a single code to be used three times by a user. If it is used more than that, this error will occur. |
| `already_used_by_other_guest` | This promo code has already been used by some other guest. | Another user has already used the code. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

