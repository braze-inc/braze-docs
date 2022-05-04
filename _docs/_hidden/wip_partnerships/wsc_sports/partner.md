---
nav_title: WSC Sports
article_title: WSC Sports
page_order: 1

description: "WSC Sports' platform generates personalized sports videos for every digital platform and every sports fan - automatically and in real-time."
alias: /partners/wsc_sports/

page_type: partner
search_tag: Partner
hidden: true

---

# WSC Sports

> [WSC Sports'][2] platform generates personalized sports videos for every digital platform and every sports fan - automatically and in real-time. 

WSC Sports uses Braze integration to deliver rich and robust media to customers via push notifications.

## Prerequisites


| Requirement | Description |
| ----------- | ----------- |
| WSC account | A WSC account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

### Sending push notifications
### Sending rich media push notifications

## Integration

### Step 1: Segments and Campaigns

Set the user segements and you campaigns in the Braze developer console

### Step 2: Endpoint usage

Our actions will deliver a request to the following braze endpoints:
| Endpoint | 
| ----------- | 
| /messages/schedule/create | 
| /messages/send |
{: .reset-td-br-1 }

### Step 3: Using Clipro

The clipro app will handle the creation of you request

### Step 4: Preview your request

At this point, your campaign should be ready to test and send. Check the Braze developer console error message logs if you run into errors. 

{% alert important %}
Remember to save your template before leaving the page! <br>Updated webhook templates can be found in the **Saved Webhook Templates** list when creating a new [webhook campaign]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/). 
{% endalert %}


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://wsc-sports.com/