---
nav_title: Amplitude and Connected Content
article_title: Amplitude and Connected Content
page_order: 0
alias: /partners/amplitude_api_endpoints/
page_type: partner
description: "Amplitude's User Profile API serves Amplitude user profiles. This includes user properties, computed user properties, a list of cohort IDs of cohorts that include the user, and recommendations."
search_tag: Partner

---

# Amplitude and Connected Content

> Amplitude's user profile API serves Amplitude user profiles. This includes user properties, computed user properties, a list of cohort IDs of cohorts that include the user, and recommendations. The following lists common Amplitude API endpoints that an be used with Connected Content.

## Endpoint parameters

The following table lays out the parameters you can use in your calls to the user profile API.

| Parameter | Required | Description |
| --------- | -------- | ----------- |
| `user_id` | Optional | User id (external database id) to be queried, required unless `device_id` is set. |
| `device_id` | Optional | Device id (anonymous id) to be queried, required unless `user_id` is set. |
| `get_recs` | Optional<br>(Defaults to false) | Return a recommendation result for this user. |
| `rec_id` | Optional | Recommendation(s) to be retrieved, required if `get_recs` is true. Multiple recommendations can be fetched by separating the `rec_ids` with commas. |
| `rec_type` | Optional | Overrides the default experimental control setting and `rec_type=model` will return modeled recommendations and `rec_type=random` return random recommendations. Other options may exist in the future. |
| `get_amp_props` | Optional<br>(Defaults to false) | Return a full set of user properties for this user, not including computations. |
| `get_cohort_ids` | Optional<br>(Defaults to false) | Return a list of all of the cohort IDs that this user is a part of that have been set up to be tracked. By default cohort membership is not tracked for users for any cohort. |
| `get_computations` | Optional<br>(Defaults to false) | Return a list of all of the computations that are enabled for this user. |
| `comp_id` | Optional | Return a single computation that might be enabled for this user. It will return a null value if it does not exist. If `get_computations` is true, all values will be fetched, including this one (unless it is archived or deleted).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

The following table covers the parameters you can most typically expect to see in Amplitude's responses.

| Response Parameter | Description |
| ------------------ | ----------- |
| `rec_id` | The recommendation id that was requested. |
| `child_rec_id` | A more detailed recommendation id that Amplitude may use on the backend as part of an internal experiment to improve model performance. In most cases, this will be the same as `rec_id`. |
| `items` | List of recommendations for this user. |
| `is_control` | true if this user is part of the control group. |
| `recommendation_source` | Name of the model that was used to generate this recommendation |
| `last_updated` | Timestamp of when this recommendation was last generated and synced. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Common Amplitude endpoints

### Get a recommendation

#### Endpoint
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_recs=true&rec_id=testRecId`
{% endraw %}
#### Example response
```json
{
  "userData": {
    "recommendations": [
      {
        "rec_id": "testRecId",
        "child_rec_id": "testRecId",
        "items": [
          "cookie",
          "cracker",
          "chocolate milk",
          "donut",
          "croissant"
        ],
        "is_control": false,
        "recommendation_source": "model",
        "last_updated": 1608670720
      }
    ],
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": null,
    "cohort_ids": null
  }
}
```

### Get multiple recommendations

#### Endpoint
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_recs=true&rec_id=testRecId,testRecId2`
{% endraw %}
#### Example response
```json
{
  "userData": {
    "recommendations": [
      {
        "rec_id": "testRecId",
        "child_rec_id": "testRecId",
        "items": [
          "cookie",
          "cracker",
          "chocolate milk",
          "donut",
          "croissant"
        ],
        "is_control": false,
        "recommendation_source": "model",
        "last_updated": 1608670720
      },
            {
        "rec_id": "testRecId2",
        "child_rec_id": "testRecId2",
        "items": [
          "bulgogi",
          "bibimbap",
          "kimchi",
          "croffles",
          "samgyeopsal"
        ],
        "is_control": false,
        "recommendation_source": "model2",
        "last_updated": 1608670658
      }
    ],
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": null,
    "cohort_ids": null
  }
}
```

### Get user properties

#### Endpoint
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_amp_props=true`
{% endraw %}
#### Example response
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "library": "http/1.0",
      "first_used": "2020-01-13",
      "last_used": "2021-03-24",
      "number_property": 12,
      "boolean_property": true
    },
    "cohort_ids": null
  }
}
```

### Get cohort IDs

#### Endpoint
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_cohort_ids=true`
{% endraw %}
#### Example response
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": null,
    "cohort_ids": ["cohort1", "cohort3", "cohort7"]
  }
}
```

### Get a single computation

#### Endpoint
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&comp_id=testCompId`
{% endraw %}
#### Example response
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "computed-prop-2": "3"
    },
    "cohort_ids": null
  }
}
```

### Get all computations

#### Endpoint
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_computations=true`
{% endraw %}
#### Example response
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "computed-prop-1": "5000000.0",
      "computed-prop-2": "3"
    },
    "cohort_ids": null
  }
}
```

