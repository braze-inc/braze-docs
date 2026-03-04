# Limbik 

Limbik is your AI resonance layer—predicting how real audiences interpret and respond to messages, concepts, and AI outputs before they reach the market. Powered by continuous primary research across 60+ countries and 25+ languages, Limbik delivers human-validated synthetic audiences—digital populations that simulate real audience response at machine speed and with research-grade accuracy (95% confidence, 1.5–3% margin of error). Limbik gives you the ability to immediately ensure your messaging resonates with what your target audience believes and feels.

## Requirements

| Prerequisite | Description |
|--|--|
| Limbik account_id | Speak to your Limbik account team, or make a GET request to Limbik’s “Organisation” endpoint  |
| Limbik Auth_token |Make a POST request to Limbik’s “Login” endpoint |
| Braze Rest API_Key |A Braze REST API key with messages permissions. |
| Braze campaign_id |Go to Messaging > Campaigns and select a pre-existing campaign. If the campaign you want does not exist yet, create one and save it. At the bottom of the individual campaign page, you can find your Campaign API Identifier. |

Before using any of the forecast endpoints, you must first identify which organization (account_id) you have access to. While most customers will have only one organization, some accounts may have multiple organizations available.

### Retrieve Available Organizations

Query the organizations endpoint to retrieve your available organizations:

```sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/organizations' \
  -H 'accept: application/json'
```

### Example Response

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


## Authentication

To access the API endpoints, you need a bearer token for authentication. Obtain your token by authenticating with your credentials:

### Login Request

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

### Response

The response will contain an `access_token` that you should use as the bearer token in all subsequent API requests:

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

---


{% alert Note %}
API Platforms like Postman can be leveraged by customers to set up automated workflows that interact with multiple Rest API endpoints from different organisations, like the workflow described below
{%endalert%}

# Use case 1 - Generating Message Copy

By leveraging both Braze and Limbik AI’s Rest API endpoints, customers can programmatically make best use of Limbik’s Generative forecasts to generate intelligently designed message copy through Braze Messaging channels, or modify existing copy to maximise impact for the chosen audience. Limbik and Braze both offer a wide array of functionality that can be accessed programmatically through the respective endpoints, allowing for the development of many sophisticated workflows. 

This documentation will outline two examples: generating message copy in Limbik, and using this copy in a subsequent message sent through Braze, as well as using Limbik to score the quality of a given message for your chosen audience.

## Limbik Generative Forecast Request

This endpoint allows users to generate a message and return it in a forecast template. The structure of a request to this endpoint is as follows:


```json

GET: https://cortex.prod.limbik.com/rest/api/forecasts/generate/template?prompt={{prompt}}

: account_id {{XXXXXX}}
:Authorization {{XXXXX}}
:accept application/json

```



### Response
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


The key element for the purposes of this use case is the “additionalDetails” field, which contains a string, the message copy that Limbik has generated. 

This can be used to populate a message sent to Braze. For instance, if making use of the POST /campaigns/trigger/send endpoint, the additionalDetail field could be used to populate a payload field. Alternatively, if sending through the POST /messages/send endpoint, the copy could be used to populate the message object of your choice. 

### Response Fields

The response contains the following key fields:

- **`type`**: The message type (e.g., `"Generate"` for AI-generated content, `"Message"` for validated messages)
- **`displayText`**: A short title or summary of the message
- **`additionalDetail`**: **The complete AI-generated message copy** - This is the primary field containing the full message text that can be sent through your messaging platform
- **`population`**: The target population and segments for this message

## Using with Braze

The `additionalDetail` field contains the message copy that can be sent to Braze. Here are two common integration patterns:

### Braze Trigger Message Request Example 

```json

{
  "campaign_id": "{{YOUR_CAMPAIGN_ID}}",
  "trigger_properties": {
    "payload" : "{{additionalDetail}}"
    },
  "broadcast": true
    }
```



# Use Case 2 - Synthetic audience details 

To build on the workflow outlined above , we can leverage Limbik’s endpoint /rest/api/populations/{account_id}/{population_id}.

This endpoint returns key data points that describe the make-up of Limbik’s synthetic audiences, such as gender, location etc. Users can take these elements and use them to populate connected audience objects, used when making request to Braze’s messaging endpoints. 

{%alert Note %}
Connected Audience objects cannot target users based on Braze’s “default” attributes, so any attributes that users wish to target must be captured in Braze as Custom Attributes.
{%endalert%}

To obtain forecast scores for specific segments, you first need to identify the available countries and their corresponding segments.

## Step 1: List Available Countries

Retrieve the list of countries available for your account:


```sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/populations/list/aca61bd5-7132-499c-946e-42d092cc1156' \
  -H 'accept: application/json'
```



From the response, identify the country you wish to use. For example, the United States has an `id` of `56`.

## Step 2: Retrieve Available Segments

Once you have the country ID, retrieve the full list of segments available for that country:

```sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/populations/aca61bd5-7132-499c-946e-42d092cc1156/56' \
  -H 'accept: application/json'
```



{% alert Note%} The response can be quite large. API users are advised to cache this data (for example, in Redis) by name or key for improved performance.{%endalert%}
 
### Response 

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



{% alert Note %}
- Segments are specified using a simplified composite key format (e.g., `gender::female`)
- The full composite key from the API response (`us2::gender::female`) is shortened to just the category and segment name
- Refer to this [document](https://audiences.limbik.com/) for a complete reference of available populations and segments
{%endalert%}

Informed by the composite key value for the chosen forecast message, users can map these synthetic audience descriptors to values which may be available on real user profiles in Braze. 

For instance, the composite key (‘fr1::education_level::master_s_degree’) could be leveraged in a Braze Connected Audience object as

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


# Use case 3 - Evaluating Forecast Score

Another key feature offered by Limbik is the ability to create an estimated score of a message against a synthetic audience. This can be achieved programmatically via Limbik’s forecasting/sync endpoint. 


## Option 1 - Synchronous Forecast

The response payload from the template generation can be used directly with the synchronous forecast endpoint:

### Example Generic Request

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



### Response ( abbreviated )

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
        "mean_val": 0.41831,
        }
      }
    },
    "virmetrics": {
      "metrics": {
        "moe": 0.02381,
        "pfi": "0.3611",
        "min_val": 0.2,
        "mean_val": 0.30395,
      }
    },
    "model_variant": "v4_0_0"
  }
}
```

## Option  2: Prepare Forecast Payload with Segments

Create your forecast payload using the selected segments. Note that segments use a simplified composite key format

### Example Segment-specific Request

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




