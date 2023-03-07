---
nav_title: Dynamic Code Generation
article_title: Punchh Dynamic Code Generation
page_order: 5
description: "This reference article outlines how to use Punchh dynamic code generation in Braze."
page_type: partner
search_tag: Partner

---


# Punchh dynamic coupon code generation in Braze

A coupon code is a unique code that can be used by a single user (either single or multiple use). The Punchh framework generates coupon codes, which can be processed within a mobile app or at the POS.

Using the Punchh coupon framework and Braze, the following scenarios can be achieved:
1. Generate a coupon code when the guest clicks a coupon generation link in an email: The coupon code will be generated dynamically and shown on a web page.
2. Generate a coupon code when the guest opens an email: The coupon code will be generated dynamically and shown as an image within the email.

## How to integrate Punchh dynamic coupon code generation

### Step 1: Create a coupon campaign in Punchh

1. Using a Punchh coupon campaign, create a dynamic generation coupon campaign as shown in the following image.
2. The Punchh coupon framework will generate the following parameters to enable dynamic coupon generation: 
    - Dynamic coupon generation token: This is a system-generated security token for encryption.
    - Dynamic coupon generation URL: This URL will be embedded in the email as a link or image, as required by the business.

![][2]{: style="max-width:60%;"}    

### Step 2: Generate signature and construct URL

JWT.IO library is used to decode, verify, and generate JSON web tokens, an open, industry-standard RFC 7519 method for securely representing claims between two parties. 

The `ClaimType` names mentioned below can be used to ensure the uniqueness of guests and coupons.
- `email`: represents the user's email address. 
- `campaign_id`: represents the system-generated Punchh campaign ID. 
- `first_name`: captures the user's first name. 
- `last_name`: captures the user's last name.

To use the Punchh dynamic coupon code API, a JWT Token must be constructed. The following shows how this can be accomplished using Liquid within Braze:

{% raw %}
```liquid
{% capture header %}{"typ":"JWT","alg":"HS256"}{% endcapture %}

{% capture payload %} {"email":"{{${email_address}}}","first_name":"{{${first_name}}}","last_name":"{{${last_name}}}","campaign_id":YOUR-CAMPAIGN-ID}{% endcapture %}

{% capture signature_structure %}{{header | base64_encode}}.{{payload | base64_encode}}{% endcapture %}

{% assign secret = "YOUR-DYNAMIC-COUPON-GENERATION-TOKEN" %}

{% assign final_signature = {{signature_structure | hmac_sha256_base64: {{secret}} %}

{% capture jwt %}{{signature_structure}}.{{final_signature | remove: '='}}{% endcapture %}
```
{% endraw %} 
### Step 3: Append coupon code in email content

#### Link to Punchh web page

On clicking the coupon URL, the user will be redirected to a Punchh-hosted web page, where the generated coupon will be displayed to the user as shown in the following image. For example,
`https://SERVER_NAME_GOES_HERE.punchh.com/request_coupons/YOUR-DYNAMIC-COUPON-GENERATION-TOKEN?sign={{jwt}}`

![][1]

#### Link image inside email content

The coupon code will be shown as an image within the email. For example,
`<img src="https://SERVER_NAME_GOES_HERE.punchh.com/request_coupons/YOUR-DYNAMIC-COUPON-GENERATION-TOKEN.png?sign={{jwt}}">`

![][3]

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