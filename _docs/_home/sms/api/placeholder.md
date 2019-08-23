---
nav_title: SMS API
page_order: 0
---

# SMS Object Specification for Messaging

## Send SMS Messages to Users via API Only
`/messages/send`

```
{
    "api_key":  {{api_key}},
    "broadcast": "",
    "external_user_ids": "",
    "user_aliases": {
    	"alias_name" : "",
    	"alias_label" : ""
    },
    "segment_id": "",
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "eye_color",
          "comparison": "equals",
          "value": "blue"
        }
      },
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_foods",
          "comparison": "includes_value",
          "value": "pizza"
        }
      },
      {
        "OR": [
          {
            "custom_attribute": {
              "custom_attribute_name": "last_purchase_time",
              "comparison": "less_than_x_days_ago",
              "value": 2
            }
          },
          {
            "push_subscription_status": {
              "comparison": "is",
              "value": "opted_in"
            }
          }
        ]
      },
      {
        "email_subscription_status": {
          "comparison": "is_not",
          "value": "subscribed"
        }
      },
      {
        "last_used_app": {
          "comparison": "after",
          "value": "2019-07-22T13:17:55+0000"
        }
      }
    ]
  },
    "campaign_id": "",
    "send_id": "",
    "override_frequency_capping": "",
    "recipient_subscription_state": "",
    "messages": {
    	"sms": {
    		"app_id": "req",
    		"body": "req",
    		"message_variation_id": "req",
    		"external_api_id": ""
    	}
   	}
}
```

## Schedule SMS Messages to Users via API Only
`/messages/schedule/create`
```
{
    "api_key":  {{api_key}},
    "broadcast": "",
    "external_user_ids": "",
    "user_aliases": {
    	"alias_name" : "",
    	"alias_label" : ""
    },
    "segment_id": "",
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "eye_color",
          "comparison": "equals",
          "value": "blue"
        }
      },
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_foods",
          "comparison": "includes_value",
          "value": "pizza"
        }
      },
      {
        "OR": [
          {
            "custom_attribute": {
              "custom_attribute_name": "last_purchase_time",
              "comparison": "less_than_x_days_ago",
              "value": 2
            }
          },
          {
            "push_subscription_status": {
              "comparison": "is",
              "value": "opted_in"
            }
          }
        ]
      },
      {
        "email_subscription_status": {
          "comparison": "is_not",
          "value": "subscribed"
        }
      },
      {
        "last_used_app": {
          "comparison": "after",
          "value": "2019-07-22T13:17:55+0000"
        }
      }
    ]
  },
    "campaign_id": "",
    "send_id": "",
    "override_messaging_limits": false,
  "recipient_subscription_state": "subscribed",
  "schedule": {
    "time": "",
    "in_local_time": true,
    "at_optimal_time": true
  },
  "messages": {
    	"sms": {
        "app_id": "req",
    		"body": "req",
    		"message_variation_id": "req",
    		"external_api_id": ""
    	}
   	}
}
```

##

'/messages/schedule/update'
'messages/schedule/delete'
'campaigns/trigger/(send || schedule/(create || update || delete))'
'canvas/trigger/(send || schedule/(create || update || delete))'

```
message_variation_id (per usual structure of these objects)
body
external api id for a FromPool
```

Tested /messages/send and /messages/schedule/create API endpoints:

Send SMS successfully
Support liquid in body field too
Return an error response as expected, if message_service_id/body/app_id is invalid or missing
If body length is too long, API will return a 201 but SMS would fail to send. A aborted message saying "Twilio SMS bodies must not be over 1600 characters." is displayed in messaging activity log.

/campaigns/trigger/send and /campaigns/trigger/schedule/create are tested with liquid as well.



# SMS Campaign Request Return Addition

message: sms
