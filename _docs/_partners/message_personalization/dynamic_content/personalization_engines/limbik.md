---
nav_title: Limbik
article_title: Limbik
description: "This reference article outlines the partnership between Braze and Limbik, an AI resonance layer that predicts how audiences interpret and respond to messages using synthetic audiences and forecasting."
alias: /partners/limbik/
page_type: partner
search_tag: Partner
---

# Limbik

> [Limbik](https://limbik.com/cognitive-ai) is your AI resonance layer—predicting how real audiences interpret and respond to messages, concepts, and AI outputs before they reach the market. Powered by continuous primary research across 60+ countries and 25+ languages, Limbik delivers human-validated synthetic audiences—digital populations that simulate real audience response at machine speed and with research-grade accuracy (95% confidence, 1.5% to 3% margin of error). Limbik gives you the ability to immediately ensure your messaging resonates with what your target audience believes and feels.

*This integration is managed by Limbik.*

## Requirements

The following are required to use Limbik with Braze:

| Prerequisite | Description |
| --- | --- |
| Limbik `account_id` | Speak to your Limbik account team, or make a GET request to Limbik’s `organisation` endpoint  |
| Limbik `auth_token` | Make a POST request to Limbik’s `login` endpoint |
| Braze REST API key | A Braze REST API key with "Messages" permissions. Create one in the Braze dashboard under **Settings** > **API Keys**. |
| Braze `campaign_id` | Go to **Messaging** > **Campaigns** and select a campaign. If the campaign you want does not exist yet, create one and save it. At the bottom of the campaign page, find the Campaign API identifier. |

Before using any of the forecast endpoints, you must first identify which organization (`account_id`) you have access to. While most customers have only one organization, some accounts may have multiple organizations available.

{% details Retrieve available organizations %}

Query the organizations endpoint to retrieve your available organizations:

```sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/organizations' \
  -H 'accept: application/json'
```

{% enddetails %}

{% details Example Response %}

```json
{
  "data": [
    {
      "uid": "aca61bd5-7132-499c-946e-42d092cc1156",
      "name": "Braze API"
    }
  ]
}
```

Select the `uid` from your desired organization to use as the `account_id` header in all subsequent API requests.

{% enddetails %}

## Authentication

To access the API endpoints, you need a bearer token for authentication. Obtain your token by authenticating with your credentials.

{% details Login request %}

```sh
curl -X 'POST' \
  'https://cortex.prod.limbik.com/rest/api/auth/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "your_username",
  "password": "your_password"
}'
```

{% enddetails %}

{% details Example response %}

The response contains an `access_token` that you can use as the bearer token in all subsequent API requests:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer"
}
```

Include this token in the `Authorization` header for all API requests:

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

{% alert note %}
You can use API platforms like Postman to set up automated workflows that call multiple REST API endpoints from different organizations, such as the following workflow.
{% endalert %}

{% enddetails %}

## Use case - Generating message copy

By using both Braze and Limbik’s REST API endpoints, you can use Limbik’s generative forecasts to create message copy and send it through Braze messaging channels, or adjust existing copy to improve impact for your audience. Both platforms expose functionality you can call programmatically to build sophisticated workflows. 

This documentation outlines two examples: generating message copy in Limbik and using this copy in a subsequent message sent through Braze, as well as using Limbik to score the quality of a given message for your chosen audience.

{% details Limbik generative forecast request %}

Use this endpoint to generate a message and return it in a forecast template. The structure of a request to this endpoint is as follows:

```json

GET: https://cortex.prod.limbik.com/rest/api/forecasts/generate/template?prompt={{prompt}}

: account_id {{XXXXXX}}
:Authorization {{XXXXX}}
:accept application/json

```

{% enddetails %}

{% details Example response %}
```json

Limbik Forecast Template Response Example
[{
  "type": "Message",
  "displayText": "Formula one next race",
  "additionalDetail": "The latest dev in Formula...",
  "messages": [
    {
      "body": "The latest dev in Formula ..."
    }
  ],
  "population": {
    "id": 56,
    "name": "us2",
    "org_enabled": true,
    "org_visible": true,
    "categories": [],
    "display_name": "US Adults",
    "composite_key": "us2",
    "enabled": true
  }
}]
```

The key element for this use case is the `additionalDetail` field, which contains the message copy that Limbik generated. 

Use this value to populate a message sent to Braze. For example, with the POST `/campaigns/trigger/send` endpoint, use `additionalDetail` to populate a payload field. With the POST `/messages/send` endpoint, use it to populate the message object of your choice. 

{% enddetails %}

### Response fields

The response contains the following key fields:

- **`type`:** The message type (for example, `"Generate"` for AI-generated content, `"Message"` for validated messages)
- **`displayText`:** A short title or summary of the message
- **`additionalDetail`**: **The complete AI-generated message copy** - This is the primary field containing the full message text that you can send through your messaging platform
- **`population`:** The target population and segments for this message

### Using with Braze

The `additionalDetail` field from Limbik's response contains the message copy you send to Braze. One common integration pattern is to pass that value in the `trigger_properties.payload` when calling the Braze trigger send endpoint. In the following example, replace `{{additionalDetail}}` with the actual string from Limbik's `additionalDetail` field, and replace `{{YOUR_CAMPAIGN_ID}}` with your campaign ID.

### Braze trigger message request example

```json
{
  "campaign_id": "{{YOUR_CAMPAIGN_ID}}",
  "trigger_properties": {
    "payload": "{{additionalDetail}}"
  },
  "broadcast": true
}
```

## Use case - Synthetic audience details 

To build on use the first use case, use Limbik’s endpoint `/rest/api/populations/{account_id}/{population_id}`.

This endpoint returns key data points that describe the makeup of Limbik’s synthetic audiences, such as gender, location, and so on. You can use these values to populate Connected Audience objects when calling Braze’s messaging endpoints. 

{% alert note %}
Connected Audience objects cannot target users based on Braze’s “default” attributes, so you must story any attributes you want to target in Braze as custom attributes.
{% endalert %}

To obtain forecast scores for specific segments, identify the available countries and their corresponding segments.

### Step 1: List available countries

Retrieve the list of countries available for your account:

```sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/populations/list/aca61bd5-7132-499c-946e-42d092cc1156' \
  -H 'accept: application/json'
```

From the response, identify the country you want to use. For example, the United States has an `id` of `56`.

### Step 2: Retrieve available segments

After you retrieve the country ID, retrieve the full list of segments for that country. 

{% details Example call %}

```sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/populations/aca61bd5-7132-499c-946e-42d092cc1156/56' \
  -H 'accept: application/json'
```

{% alert note %}
The response can be large. Cache this data (for example, in Redis) by name or key for better performance.
{% endalert %}

{% enddetails %}
 
{% details Example response %} 

```json
//For example, to target females in the US adult population

[
  {
    "id": 56,
    "name": "us2",
    "composite_key": "us2",
    "categories": [
      {
        "id": 9331,
        "name": "gender",
        "composite_key": "us2::gender",
        "segments": [
          {
            "id": 63793,
            "name": "female",
            "composite_key": "us2::gender::female",
          }
        ]
      }
    ]
  }
]
```

{% alert note %}
- Segments are specified using a simplified composite key format (for example, `gender::female`).
- The full composite key from the API response (`us2::gender::female`) is shortened to just the category and segment name.
- For a complete reference of available populations and segments, see [Limbik audiences](https://audiences.limbik.com/).
{% endalert %}

Using the composite key value for your chosen forecast message, you can map these synthetic audience descriptors to values on real user profiles in Braze. 

For example, you can use the composite key (`fr1::education_level::master_s_degree`) in a Braze Connected Audience object as follows:

```json
{
  "AND":
    [
{
  "custom_attribute":
    {
      "custom_attribute_name": "education_level",
      "comparison": "equals",
      "value": "masters"
    }
}
   ]
}
```

{% enddetails %}

## Use case - Evaluating forecast score

You can use Limbik to create an estimated score for a message against a synthetic audience. Do this programmatically with Limbik’s `forecasting/sync` endpoint. 

### Option 1 - Synchronous forecast

You can use the response payload from the template generation directly with the synchronous forecast endpoint:

{% details Example generic request %}

```sh
curl -X 'POST' \
  'https://cortex.prod.limbik.com/rest/api/forecasts/synchronous' \
  -H 'accept: application/json' \
  -H 'account_id: aca61bd5-7132-499c-946e-42d092cc1156' \
  -H 'Content-Type: application/json' \
  -d '{
  "type": "Generate",
  "displayText": "Formula one season testing 2026",
  "additionalDetail": "🚀 Day 1 of 2026 F1 Bahrain testing just dropped BOMBS! Lando Norris edged out Max Verstappen for P1 in McLaren'\''s beast, with Ferrari hot on their heels 🔥. But the real shocker? Cadillac'\''s debutants Sergio Perez & Valtteri Bottas smashed 107 laps – nearly TWO race distances! New kids on the block are HERE to stay. Audi'\''s radical upgrades already turning heads too. Who'\''s your early fave for Australia? 👀 #F12026 #BahrainTesting #LandoNorris",
  "population": {
    "population": "us2",
    "segments": []
  }
}'
```

{% enddetails %}

{% details Example response (abbreviated) %}

```json
{
  "uid": "6c5e28ef-8796-4659-a743-d842a06c9bf7",
  "datetime": "2026-02-11T20:04:06.545+00:00",
  "userId": "9cdd921c-f62f-46a6-902f-a6b0d1702f99",
  "accountId": "aca61bd5-7132-499c-946e-42d092cc1156",
  "name": "Formula one season t...",
  "user_message_context": "",
  "population": [
    {
      "name": "us2",
      "display_name": "US Adults",
      "categories": []
    }
  ],
  "privacy_compliant": false,
  "model_outputs": {
    "belmetrics": {
      "metrics": {
        "moe": 0.02144,
        "pfi": "0.3611",
        "min_val": 0.2941,
        "mean_val": 0.41831
        }
      }
    },
    "virmetrics": {
      "metrics": {
        "moe": 0.02381,
        "pfi": "0.3611",
        "min_val": 0.2,
        "mean_val": 0.30395
      }
    },
    "model_variant": "v4_0_0"
  }
}
```

{% enddetails %}

### Option 2: Prepare forecast payload with segments

Create your forecast payload using the selected segments. Segments use a simplified composite key format.

{% details Example segment-specific request %}

```json
{
  "type": "Generate",
  "displayText": "Formula one season testing 2026",
  "additionalDetail": "🚀 Day 1 of 2026 F1 Bahrain testing just dropped BOMBS! Lando Norris edged out Max Verstappen for P1 in McLaren's beast, with Ferrari hot on their heels 🔥. But the real shocker? Cadillac's debutants Sergio Perez & Valtteri Bottas smashed 107 laps – nearly TWO race distances! New kids on the block are HERE to stay. Audi's radical upgrades already turning heads too. Who's your early fave for Australia? 👀 #F12026 #BahrainTesting #LandoNorris",
  "population": {
    "population": "us2",
    "segments": [
      "gender::female"
    ]
  }
}
```

{% enddetails %}