---
nav_title: Treasure Data for Currents
article_title: Treasure Data for Currents
description: "This reference article outlines the partnership between Braze Currents and Treasure Data, an enterprise customer data platform that allows you to write job results directly to Braze."
page_type: partner
tool: Currents
alias: /partners/treasure_data_for_currents/
search_tag: Partner
---


# Treasure Data for Currents

> [Treasure Data](https://www.treasuredata.com/) is a customer data platform (CDP) that collects and routes information from multiple sources to a variety of other locations in your marketing stack.

The Braze and Treasure Data integration allows you to seamlessly control the flow of information between the two systems. With Currents, you can also connect data to Treasure Data to make it actionable across the entire growth stack.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Treasure Data | A [Treasure Data account](https://console.treasuredata.com/users/sign_in) is required to take advantage of this partnership. |
| Currents | To export data back into Treasure Data, you need to have [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) set up for your account. |
| Treasure Data URL | This can be obtained by navigating to your Treasure Data dashboard and copying the ingestion URL.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Treasure Data logs each event in batches. 이벤트 수를 얻기 위해 Treasure Data를 쿼리하는 방법에 대한 자세한 내용은 [데이터 쿼리하기를](https://docs.treasuredata.com/articles/int/braze-currents-import-integration/a/h2__592056238) 참조하세요.<br><br>Treasure Data의 새로운 Braze 스트리밍 커넥터와 통합하려는 경우, [Braze 커런츠 스트리밍 가져오기 통합의](https://docs.treasuredata.com/articles/#!int/braze-currents-import-integration/q/braze/qid/72364/qp/4) 자세한 설정 단계를 참조하세요. Braze 내 통합 또는 설정에 대해 궁금한 점이 있으면 Braze 계정 팀에 문의하세요.
{% endalert %}

## Integration

The recommended approach to connecting with Treasure Data is through Postback API. This method doesn't require a default connector and data can be received through a push approach. All events sent in one data batch are inside of one field of one row in a JSON array, which needs to be parsed to get the required data.

{% alert important %}
Ingestion into Treasure Data through event-collector currently doesn't happen in real-time and may take up to five minutes.
{% endalert %}

### Step 1: Setup Treasure Data Postback API with Braze

Instructions for creating a Postback API can be found on the [Treasure Data website](https://docs.treasuredata.com/display/public/PD/Postback+API). Braze will directly send the updated events to Treasure Data in real time, with the exception of ingestion through event-collector. When completed, Treasure Data will provide a data source URL to copy for use in the next step.

### Step 2: Create Current

In Braze, navigate to **Currents** > **\+ Create Current** > **Treasure Data Export**. Provide an integration name, contact email, and your Treasure Data URL. Next, select what you want to track from the list of available events and click **Launch Current**.

All events sent to Treasure Data will include the user’s `external_user_id`. At this time, Braze does not send event data to Treasure Data for users who haven't set their `external_user_id`.

{% alert important %}
Keep your Treasure Data URL up to date. If your connector’s URL is incorrect, Braze won't be able to send events. 이 상태가 **5일** 이상 지속되면 커넥터의 이벤트가 삭제되고 데이터가 영구적으로 손실됩니다.
{% endalert %}

#### Example event field value
```json
{
    "events": [
        {
            "event_type": "users.message.email.Open",
            "id": "a1234567-89ab-cdef-0123-456789abcdef",
            "time": 1477502783,
            "user": {
                "user_id": "user_id",
                "timezone": "America/Chicago"
        },
            "properties": {
                "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
                "campaign_name": "Test Campaign",
                "dispatch_id": "12345qwert",
                "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
                "email_address": "test@example.com",
                "send_id": "f123456789abcdef01234567",
                "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
            }
        }
    ]
}
```

#### Example of the ingested view

![4]{: style="max-width:70%;"}

## Integration details

Braze supports exporting all data listed in the [Currents event glossaries]({{site.baseurl}}/user_guide/data/braze_currents/) (including all properties in both [message engagement]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) and [customer behavior]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) events) to Treasure Data.

The payload structure for exported data is the same as the payload structure for custom HTTP connectors, which can be viewed in the [examples repository for custom HTTP connectors](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).


[4]: {% image_buster /assets/img/treasure_data/treasure_data_ingested_view.png %}
