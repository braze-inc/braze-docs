---
nav_title: Talon.One
alias: /partners/talonone/
---

# Talon.One

[Talon.One](https://talon.one/) is an stream-lined solution to providing personalized incentives for any mobile marketing CRM. With it, launching contextual 1-to-1 coupons, referrals, discounts, and loyalty campaigns is now easier and faster. Coupled with the use of a flexible rules engine to boost your conversion and retention rates without burning the promotion budget, Talon.One's Braze integration can help take your loyalty or coupon program to the next level.

## Prerequisites

| Requirement    | Origin                                                | Description                                                             |
| -------------- | ----------------------------------------------------- | ----------------------------------------------------------------------- |
| Braze Campaign | [Braze Settings](https://dashboard.braze.com/sign_in) | An active Braze campaign that vouchers and codes will be generated for. |

{% alert important %}
While the integration is straightforward with any api calls and Braze liquid variables needed outlined below, the one gotcha that stands out is around the rate-limiting that is required, and how this may impact the approach a client takes towards orchestrating an engagement. Talon.One **_requires_** a rate-limit of 500 messages per minute.

Details on how to modify your rate-limit can be found [here](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-speed-rate-limiting).
{% endalert %}

## API Integration

## Coupon Setup

You can modify the form of generated codes for any campaign by navigating to the Coupon Code Generator for that campaign found under **Campaign -> Settings -> Coupon Code Generator**

![Talon.One Coupon Settings]({% image_buster /assets/img/talonone_coupon_settings.png %})

## Endpoint Usage

Because Braze-connected content only supports **string** data types, a custom endpoint has to be used that will convert everything to the correct data type.
This endpoint contains the following built-in properties ((\*) Required):

- applicationID (\*)
- campaignID (\*)
- identifier (\*)
- integrationID
- startDate
- expiryDate

### Exaple One: Required Properties

```bash
curl https://demo.talon.one/v1/braze/createcoupon \
 -X POST \
 -H 'Authorization: Bearer [sessionToken]' \
 -d '{
        "applicationID": "1",
        "campaignID: "1",
        "identifier": "an-example-identifier"
}'
```

### Example Two: All Built-In Properties

```bash
curl https://demo.talon.one/v1/braze/createcoupon \
 -X POST \
 -H 'Authorization: Bearer [sessionToken]' \
 -d '{
        "applicationID": "1",
        "campaignID": "1",
        "identifier": "an-example-identifier",
        "integrationID": "an-example-integrationID",
        "startDate": "2019-06-12T09:00:00Z",
        "expiryDate": "2019-06-13T09:00:00Z"
}'
```

### Example Three: Custom Attributes

Custom attributes can also be passed directly as long as they are notated with a dot prefix and still wrapped in a string as shown below.

```bash
curl https://demo.talon.one/v1/braze/createcoupon \
 -X POST \
 -H 'Authorization: Bearer [sessionToken]' \
 -d '{
        "applicationID": "1",
        "campaignID": "1",
        "identifier": "an-example-identifier"
        ".stringAtrrName": "examplestring",
        ".listOfNumbers": "[1,2,3,4,5,6,7,8,9,10]",
    }'
```

## Using This Integration

To trigger the Talon.One coupon creation event, you will have to use Braze's [Connected Content Feature](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/). However, the coupon creation event can still be used in any campaign message body or any canvas message body.

## Configuring Connected Content Feature

### Step One: Add the connected content tag to the body of your message

![Talon.One Connected Content Tag]({% image_buster /assets/img/talonone_connected_content.png %})

{% alert tip %}
You can access Braze attributes by using liquid tags (e.g. {{${user_id}}} to pass the user id)
{% endalert %}

### Step Two: Add the URL to the createCoupon endpoint of your Talon.One deployment

![Talon.One Creat Coupon URL ]({% image_buster /assets/img/talonone_createcoupon_url.png %})

### Step Three: Add the authorization header and the method _(POST)_ of the request

![Talon.One Authorization Header]({% image_buster /assets/img/talonone_auth_header.png %})

{% alert important %}
Further details on how to generate a session token can be found [here](https://developers.talon.one/Management-API/Authentication).
{% endalert %}

### Step Four: Add the body of the request containing the coupon code specs mentioned above

![Talon.One Request Parameters]({% image_buster /assets/img/talonone_request_params.png %})

{% alert important %}
The **identifier** parameter is necessary to prevent the creation of multiple coupons for one message, and each paramter should be separated with an "&" as shown above.
{% endalert %}

### Step Five: Storing the Talon.One result

Add the "save" parameter at the end to store the Talon.One response as a Braze variable. In the example below, the Talon.One response is being saved in a variable name _result_.

![Talon.One Save Response]({% image_buster /assets/img/talonone_save_response.png %})

### Step Six: Usage

Use a [liquid tag](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/liquid/overview/) to show the value of the generated code in the message.

![Talon.One Liquid Tags]({% image_buster /assets/img/talonone_liquid_tag.png %})

### Code snippet

```handlebars
{% connected_content https://[YOUR_SUBDOMAIN].talon.farm/v1/braze/createcoupon

:headers {
"authorization": "Bearer [sessionToken]"
}
:method post
:body applicationID=1&campaignID=1488&identifier={{campaign.${message_api_id}}}&integrationID={{${user_id}}}
:content_type application/json
:save result
%}

{{result.value}}
```

{% alert tip %}
While you can acess the coupon code with `{{result.value}}` as shown above, which will return the generated value similar to `44D4-U4PL` you can also access
the whole response from Talon.One with `{{result}}` which will look similar to `{"id"=>1548040, "value"=>"44D4-U4PL", "__http_status_code__"=>200}`
{% endalert %}

# Troubleshooting

As with other Connected Content integrations, much of the troubleshooting will be centered around ensuring syntax is correct (e.g. the right liquid tags are used depending on if it is a canvas or campaign, referencing the right value in the json response).

Outside of syntax and setting up the call right, another potential area of troubleshooting to be aware of is the rate limit that you would want to implement in to the Braze campaign/Canvas. As per Felix's note, if the rate limit is not respects, "...(Talon.One) can not guarantee, neither that every code will be generated nor that the response will be there in time".
