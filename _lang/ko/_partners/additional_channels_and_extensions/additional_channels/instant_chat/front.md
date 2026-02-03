---
nav_title: Front
article_title: Front
description: "Learn how to integrate Front with Braze"
alias: /partners/front/
page_type: partner
search_tag: Partner

---

# Front

> Front's integration enables you to leverage Braze Data Transformation and webhooks from each platform to set up a two-way conversational SMS pipeline.

The incoming webhook from Front will contain a payload that includes the message sent by the live agent. The request will need to be reformatted before it can be accepted by Braze endpoints. The Front Data Transformation template will reformat the payload and write a custom event to the user profile titled **Outbound SMS Sent,** with the message body being passed as an event property.

Before setting up a new transformation in Braze, we recommend reviewing the support matrix for each tier in our [Data Transformation]({{site.baseurl}}/user_guide/data/data_transformation/overview/) documentation. Our Free and Pro tiers offer a different number of active transformations and incoming requests per month. Confirm the current plan you’re on can support your use case.

## Prerequisites

Before you start, you'll need the following:

| Prerequisite             | Description                                                               |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| A Front account            | A Front account is required to take advantage of this partnership.|
| Braze Data Transformation Webhook URL | [Braze Data Transformation]({{site.baseurl}}/user_guide/data/data_transformation/overview/) will be used to reformat the incoming webhook from Front so it can be accepted by the Braze /users/track endpoint.|
| A Front REST API Key         | A Front REST API key will be used to make an outbound webhook request from Braze to Front. |

## Use cases

- Streamline your lead generation process using Braze automated SMS messaging to identify user preferences and enable live sales agents to follow up and close sales.
- Re-engage customers who abandoned their shopping carts by driving sales conversions through automated SMS responses and live chat support.

## Integrating Front

### Step 1: Create a data transformation

First, you'll create a new data transformation in Braze. The following steps are simplified; for a full walkthrough, see [Creating a transformation]({{site.baseurl}}/user_guide/data/data_transformation/creating_a_transformation/).

1. In Braze, go to **Data Settings** > **Data Transformations**, then select **Create Transformation** .
2. Under **Editing Experience**, select **Start from scratch**.
3. Under **Select Destination**, select **POST: Track Users**.
4. Copy and paste the following transformation template, then save and activate endpoint.
    {% raw %}
    ```liquid

    // This is a default template that you can use as a starting point. Feel free to delete this entirely to start from
    // scratch, or to delete specific components as you see fit

    // First, this code defines a variable, "brazecall", to build up a /users/track request
    // Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in
    // desired values in your /users/track request with JS dot notation, such as payload.x.y.z

    let brazecall = {
    "events": [
      {
      "phone": payload.recipients[1].handle,
      "_update_existing_only": true,
      "name": "Outbound SMS Sent",
      "time": new Date().toISOString(),
      "properties": {
        "message_id": payload.id,
        "message_body": payload.body,
        "front_author_username": payload.author.username
      }
      }
    ]
    };

    // After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
    return brazecall;
    ```
    {% endraw %}

    Your transformation should be similar to the following:

    ![데이터 변환의 예.]({% image_buster /assets/img/front/data_transformation.png %})

{% alert tip %}
You can modify this template to meet your specific needs. For example, you can customize the pre-set custom event name. For more information, see [Data transformation overview]({{site.baseurl}}/user_guide/data/data_transformation/overview/).
{% endalert %}

### Step 2: Create an outbound SMS campaign

Next, you'll create an SMS campaign that will listen for webhooks from Front and an custom SMS response to your customers.

#### Step 2.1: Compose your message

In the **Message** textbox, add the following Liquid code, along with any opt-out language or other static content.

{% raw %}
```liquid
{{event_properties.${message_body}}}
```
{% endraw %}

Your message should be similar to the following:

![Liquid 코드를 사용한 메시지의 예.]({% image_buster /assets/img/front/sms_to_braze.png %}){: style="max-width:80%;"}

#### 2.2 Schedule the delivery

For the delivery type, select **Action-Based delivery**; then for the custom event trigger, select **Outbound SMS Sent**.

!["전달 일정" 페이지.]({% image_buster /assets/img/front/custom_event_trigger.png %})

{% alert note %}
This custom event is the Data Transformation that writes to the user’s profile. Agent messages will be saved as an event property on this event.
{% endalert %}

Finally, under **Delivery Controls**, enable re-eligibility.

!["배송 관리"에서 재자격이 활성화됩니다.]({% image_buster /assets/img/front/braze_reeligibility.png %})

### 3단계: Create a custom channel

In the Front dashboard, go to **Settings** > **Channels** > **Add Channels**, then select **Custom Channel** and enter a name for your new Braze channel.

![Front 대시보드에서 Braze를 위한 커스텀 채널.]({% image_buster /assets/img/front/front_custom_channel.png %})

### 4단계: Configure the settings

In the outbound API endpoint field, enter the Data Transformation Webhook URL [you created earlier](#step-1-set-up-a-data-transformation-in-braze). All outbound messages from live agents on your new Braze channel will be sent here. This channel also provides an endpoint URL for Braze to forward SMS messages to in the **Incoming URL** Field.

Be sure to make a note of this URL—you'll need it later.

![Front에서 새로 생성된 Braze 채널의 채널 설정.]({% image_buster /assets/img/front/front_custom_channel2.png %}){: style="max-width:65%;"}

### 5단계: Set up inbound-SMS forwarding

Next, you’ll create two new webhook campaigns in Braze so you can forward inbound SMS from customers to the Front inbox.

|Number|Purpose|
|---|---|
|Webhook campaign 1|Signals to Front that a live chat conversation is being requested.|
|Webhook campaign 2|Forwards all conversational SMS responses sent inbound from the customer to the Front inbox.|
{: .reset-td-br-1 .reset-td-br-2 }

#### Step 5.1: Create an SMS keyword category

In the Braze dashboard, go to **Audience**, choose your **SMS subscription group**, then select **Add Custom Keyword**. To create an exclusive SMS keyword category for Front, fill out the following fields.

|Field|Description|
|---|---|
|Keyword Category|The name of your keyword category, such as `FrontSMS1`.|
|Keywords|Your custom keywords, such as `TIMETOMOW`. Avoid common words to prevent accidental triggers. Keep in mind, keywords are case insensitive, so `lawn` would match `LAWN`.|
|Reply Message|키워드가 감지될 때 전송될 메시지, 예를 들어 "조경사가 곧 연락드릴 것입니다."|
{: .reset-td-br-1 .reset-td-br-2 }

![Braze의 SMS 키워드 카테고리 예시.]({% image_buster /assets/img/front/front_keyword.png %}){: style="max-width:65%;"}

#### 5.2단계: Create your first webhook campaign

In the Braze dashboard, create your first webhook campaign using the URL [you created previously](#step-3-configure-the-settings-for-your-new-custom-braze-channel).

![Braze에서 생성해야 할 첫 번째 웹훅 캠페인의 예.]({% image_buster /assets/img/front/sms_to_front.png %}){: style="max-width:65%;"}

Add the following to your request body:

{% raw %}
```liquid
{ 
 "sender": {
  "handle": "{{${phone_number}}}",
  "name": "{{${user_id}}}"
 },
 "body_format": "markdown",
 "metadata": {
  "headers": {
   "first_name": "{{${first_name}}}",
   "last_name": "{{${last_name}}}"
  }
 },
 "body": "{{sms.${inbound_message_body} | default : "no body available" }}"
}
```
{% endraw %}

In the Settings tab, configure your `Authorization`, `content-type`, and `accept` request headers.

![세 개의 필수 헤더가 포함된 요청의 예.]({% image_buster /assets/img/front/webhook_settings.png %}){: style="max-width:65%;"}

#### 5.3단계: Schedule the first delivery

For **Schedule Delivery**, select **Action-Based Delivery**, then choose **Send an SMS Inbound Message** for your trigger type. Also add the SMS subscription group and keyword category you [set up previously](#step-51-create-an-sms-keyword-category).

![첫 번째 웹훅 캠페인의 '전송 예약' 페이지입니다.]({% image_buster /assets/img/front/front_actionbased_keyword.png %})

Under **Delivery Controls**, enable re-eligibility.

![첫 번째 웹훅 캠페인의 '전달 제어'에서 재자격이 선택되었습니다.]({% image_buster /assets/img/front/braze_reeligibility.png %})

#### Step 5.4: Create your second webhook campaign

두 번째 웹훅 캠페인이 첫 번째와 일치하므로 [첫 번째 캠페인을 복제하고 이름을 바꿀 수 있습니다.]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns/#duplicating-segments-or-campaigns)

#### Step 5.5: Schedule the second delivery

For **Schedule Delivery**, set the **action-based trigger** and the **SMS subscription group** to the same as [your the first delivery](#step-53-schedule-the-first-delivery). However, for **keyword category**, choose **Other**.

![두 번째 웹훅 캠페인을 위한 "예정된 전달" 페이지, 키워드 카테고리로 "기타"가 선택됨.]({% image_buster /assets/img/front/front_actionbased_other_keyword.png %})

#### Step 5.6: Add an audience filter

Your webhook campaign can now forward inbound SMS responses from your customers. To filter SMS responses so only messages for live chats are forwarded, add the **Last Received Message From Specific Campaign** segmentation filter to the **Target Audiences Step**.

!["특정 캠페인에서 마지막으로 수신한 메시지"가 선택된 오디언스 필터.]({% image_buster /assets/img/front/front_segment_last_received_message.png %}){: style="max-width:65%;"}

Then configure your filter:

1. For **Campaign**, select the SMS campaign [you previously created](#step-2-create-an-outbound-sms-campaign).
2. For **Operator**, select **Less Than**.
3. For **Time Window**, choose the length of time a chat should stay open without a response from the customer.

![선택된 오디언스 필터의 구성 설정.]({% image_buster /assets/img/front/front_target_audience.png %})

## 고려 사항

### Billable Segments

- SMS messages at Braze are charged per message segment. Understanding what defines a segment and how these messages will be split is key in understanding how you will be billed for messages. See more information in our [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/).
- Long agent responses will consume more billable segments.

### 데이터 포인트 기록

Currently this integration requires a custom event to be written to a user profile every single time a live agent sends an SMS from Front. 이는 몇 개의 메시지만 지속되는 빠른 교환에 적합할 수 있지만, 대화가 길어질수록 데이터 포인트의 의미도 커집니다. Braze 데이터 포인트의 뉘앙스에 대한 질문이 있는 경우, 귀하의 Braze 계정 매니저가 답변할 수 있습니다.

### SMS 메시지에 링크 포함

Sending a link from the Front live chat will render with extra HTML tags.

### Attaching image file from Front

Image files in Front will not render in SMS messages sent from Braze.

### Opt-outs 

Conversational messages have a higher risk of containing the word “stop” or similar vernacular that can be recognized as fuzzy opt-outs.
