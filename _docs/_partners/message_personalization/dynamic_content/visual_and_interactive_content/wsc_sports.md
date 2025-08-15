---
nav_title: Wsc sports
article_title: WSC Sports
description: "This reference article outlines the partnership between Braze and WSC Sports, a sports video platform that allows you to include rich and robust sports media in your Braze push notifications."
alias: /partners/wsc_sports/
page_type: partner
search_tag: Partner

---

# WSC Sports

> The [WSC Sports](https://wsc-sports.com/) platform generates personalized sports videos for every digital platform and every sports fan - automatically and in real-time. 

_This integration is maintained by WSC Sports._

## About the integration

The Braze and WSC Sports integration allows you to include rich and robust sports media in your Braze push notifications. 

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| WSC account | A WSC account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with **Messages**, **Segments**, **Campaigns** and **Canvas** permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

The WSC Sports application handles the end-to-end process, from selecting the video to the arrival of the push notification on the end user's device. 

### Step 1: Select send settings

![]({% image_buster /assets/img/wsc_sports/braze_integration.jpg %} "braze_integration.jpg"){: style="float:right;max-width:25%;margin-bottom:15px;"}

Before starting the integration, make sure you have your desired campaign and user segments built in Braze. When completed, in the WSC Sports platform, select your desired video, and in the send settings, select Braze user segment and campaign ID you would like to use. Lastly, choose the time you would like your push message sent out. 

#### API call

Once sent, WSC Sports will deliver the push notification to the chosen user segments, using the following Braze endpoints, based on the options selected:
- [/messages/schedule/create]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages#create-scheduled-messages)
- [/messages/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#sending-messages-immediately-via-api-only)

The resulting body of the message is as follows: 
```
{
  "apple_push": {
    "alert": {
      "body": "Push Message Title"
    },
    "asset_url": "internalURI.mp4",
    "asset_file_type": "mp4"
  }
}
```

### Step 2: Test send

At this point, your campaign should be ready to test and send. Check the Braze error message logs if you run into errors. 


