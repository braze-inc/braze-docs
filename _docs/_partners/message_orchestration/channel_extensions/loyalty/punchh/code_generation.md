---
nav_title: Dynamic Code Generation
article_title: Punchh Dynamic Code Generation
page_order: 2
description: "This reference article outlines how to use Punchh dynamic code generation in Braze."
page_type: partner
search_tag: Partner
---

# Dynamic code generation

> A coupon code is a unique code that can be used by a single user (either single or multiple use). The Punchh framework generates coupon codes, which can be processed within a mobile app or at the point-of-sale (POS) system.

Using the Punchh coupon framework and Braze, you can achieve the following scenarios:

- Generate a coupon code when the guest clicks a coupon generation link in an email: The coupon code will be generated dynamically and shown on a web page.
- Generate a coupon code when the guest opens an email: The coupon code will be generated dynamically and shown as an image within the email.

## How to integrate Punchh dynamic coupon code generation

### Step 1: Create a coupon campaign in Punchh

1. Using a Punchh coupon campaign, create a dynamic generation coupon campaign as shown in the following image.
2. The Punchh coupon framework will generate the following parameters to enable dynamic coupon generation:
    - Dynamic coupon generation token: This is a system-generated security token for encryption.
    - Dynamic coupon generation URL: This URL will be embedded in the email as a link or image, as required by the business.

![The form for creating a coupon campagin in Punchh.]({% image_buster /assets/img/punchh/punchh8.png %}){: style="max-width:60%;"}

### Step 2: Generate signature and construct URL

The JWT.IO library decodes, verifies, and generates JSON web tokens, an open, industry-standard RFC 7519 method for representing claims securely between two parties. 

The following `ClaimType` names can be used to ensure the uniqueness of guests and coupons:

- `email`: represents the user's email address. 
- `campaign_id`: represents the system-generated Punchh campaign ID. 
- `first_name`: captures the user's first name. 
- `last_name`: captures the user's last name.

To use the Punchh dynamic coupon code API, a JWT Token must be constructed. Add the following Liquid template to your Braze dashboard in the message body of the channel you'd like to use:

{% raw %}
```liquid
{% capture header %}{"alg":"HS256","typ":"JWT"}{% endcapture %}

{% capture payload %}{"campaign_id":"CAMPAIGN_ID","email":"{{${email_address}}}","first_name":"{{${first_name}}}","last_name":"{{${last_name}}}"}{% endcapture %}

{% capture signature_structure %}{{header | base64_encode}}.{{payload | base64_encode | remove: '='}}{% endcapture %}

{% assign secret = "DYNAMIC_COUPON_GENERATION_TOKEN" %}

{% assign final_signature = {{signature_structure | hmac_sha256_base64: secret}} %}

{% capture jwt %}{{signature_structure}}.{{final_signature | remove: '='}}{% endcapture %}

```
{% endraw %}

Replace the following:

| Placeholder        | Description                                          |
|--------------------|------------------------------------------------------|
| `SERVER_NAME`                     | The name of your server.              |
| `DYNAMIC_COUPON_GENERATION_TOKEN` | Your dynamic coupon generation token. |
| `CAMPAIGN_ID`                     | Your campaign ID.                     |

### Step 3: Append coupon code to message body

#### Link to Punchh web page

To link to a Puncch-hosted web page, add the following snippet to your message body.

{% raw %}
```liquid
https://SERVER_NAME.punchh.com/request_coupons/DYNAMIC_COUPON_GENERATION_TOKEN?sign={{jwt}}
```
{% endraw %}

Replace the following:

| Placeholder        | Description                                          |
|--------------------|------------------------------------------------------|
| `SERVER_NAME`                     | The name of your server.              |
| `DYNAMIC_COUPON_GENERATION_TOKEN` | Your dynamic coupon generation token. |

When a user clicks the coupon URL, they'll be redirected to a Punchh-hosted web page, where their generated coupon will be displayed.

![Example confirmation message after a user successfully generates a coupon code.]({% image_buster /assets/img/punchh/punchh7.png %})

#### Extract code via JSON as plain text

To return a JSON response, add `.json` before the sign query parameter of the Punchh URL as shown in the following snippet:

{% raw %}
```liquid
https://SERVER_NAME.punchh.com/request_coupons/DYNAMIC_COUPON_GENERATION_TOKEN.json?sign={{jwt}}
```
{% endraw %}

Replace the following:

| Placeholder        | Description                                          |
|--------------------|------------------------------------------------------|
| `SERVER_NAME`                     | The name of your server.              |
| `DYNAMIC_COUPON_GENERATION_TOKEN` | Your dynamic coupon generation token. |

You could then leverage [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) to insert the code as plain text into any message body. For example:

{% raw %}
```liquid
{% connected_content https://SERVER_NAME.punchh.com/request_coupons/DYNAMIC_COUPON_GENERATION_TOKEN.json?sign={{jwt}} :save punchh_coupon %}
{{punchh_coupon.coupon}}
```
{% endraw %}

#### Link image inside email content

To link the coupon code inside an image, add the following snippet to your message body:

{% raw %}
```liquid
<img src="https://SERVER_NAME.punchh.com/request_coupons/DYNAMIC_COUPON_GENERATION_TOKEN.png?sign={{jwt}}">`
```
{% endraw %}

Replace the following:

| Placeholder        | Description                                          |
|--------------------|------------------------------------------------------|
| `SERVER_NAME`                     | The name of your server.              |
| `DYNAMIC_COUPON_GENERATION_TOKEN` | Your dynamic coupon generation token. |

Your output will be similar to the following:

![Rendered output of the coupon code image tag.]({% image_buster /assets/img/punchh/punchh9.png %})

## Associated error messages

| Error code | Error message | Description |
| --- | --- | --- |
| `coupon_code_expired` | This promo code has expired | The code is used after its configured expiration date. |
| `coupon_code_success` | Congratulations, Promo Code Applied Successfully. | The code is used successfully. |
| `coupon_code_error` | Please enter a valid promo code | The code used is invalid. |
| `coupon_code_type_error` | Incorrect coupon type. This coupon can only be redeemed at `%{coupon_type}`. | When a code supposed to be used at the POS is used in the Mobile app, this error will occur. |
| `usage_exceeded` | The usage for this coupon code's campaign is full. Please try next time. | The usage of the code exceeds the number of users allowed to use it. For example, if the dashboard configuration allows a code to be used by 3,000 users and the number of users exceeds 3,000, this error will occur. |
| `usage_exceeded_by_guest` | This promo code has already been processed. | The usage of the code by a user exceeds the number of times a user can use it. For example, the dashboard configuration allows a single code to be used three times by a user. If it is used more than that, this error will occur. |
| `already_used_by_other_guest` | This promo code has already been used by some other guest. | Another user has already used the code. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

[1]: {% image_buster /assets/img/punchh/punchh7.png %}
[2]: {% image_buster /assets/img/punchh/punchh8.png %}
[3]: {% image_buster /assets/img/punchh/punchh9.png %}
