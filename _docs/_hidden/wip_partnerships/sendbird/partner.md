---
nav_title: Sendbird
article_title: Sendbird
page_order: 1

description: "This reference article outlines the partnership between Braze and Sendbird, a leading in-app messaging solution for brands to reach and engage with their customers."
alias: /partners/sendbird/

page_type: partner
search_tag: Partner
hidden: true
---

# Sendbird

> [Sendbird][4] Notifications offers marketers and product managers a powerful new channel to communicate with their customers in-app with persistent, interactive one-way messages. These messages can be used for any communication, and are most commonly used for promotional and transactional purposes.

Sendbird partners with marketing automation solutions like Braze to enable PMs and marketers to segment audiences and personalize Notifications sends, as well as trigger Notifications as part of a user journey. These integrations also make it easy for our business users to send Notifications directly from their marketing automation workflows.

The Sendbird-Braze integration allows users to:
* Utilize Braze's segmentation and triggering capabilities to initiate personalized in-app notifications.
* Create tailored in-app notifications on the Sendbird Notifications platform, which are then delivered within the app environment, enhancing user engagement.

By harnessing the joint capabilities of Braze and Sendbird Notifications, businesses can elevate customer engagement and drive higher conversion rates through effective in-app notification strategies.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Sendbird account | A Sendbird account is required to take advantage of this partnership. |
| Sendbird UIKit | You must have the Sendbird UIKit installed in your [iOS][2] or [Android][3] app. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

![][13]

The Braze and Sendbird Notifications integration offers a range of use cases to boost customer engagement and deliver an exceptional user experience:

- Marketing: Enhance targeted campaigns with personalized promotions and recommendations tailored to users' preferences, such as providing exclusive discounts based on browsing history or past purchases.
- Transactional: Elevate customer communication through real-time updates on orders, deliveries, billing, and payments, including notifications regarding order status, shipping details, and estimated delivery times.

By leveraging this integration, businesses can unlock numerous possibilities to further improve user engagement and create a superior customer experience.

## Integration

### Step 1: Create a notification template

Templates are the core of how Sendbird Notifications works. They allow brands to send personalized in-app notifications by building and using multiple templates for each channel. Templates can be created and customized on Sendbird Dashboard without writing code.

See Sendbird documentation to learn more about [Templates][7].

![][10]

### Step 2: Set up the Braze integration on Sendbird Dashboard

From Sendbird Dashboard, select your application, navigate to **Notifications > Integrations**, and click **Add** under **Braze** section. Here, you will need your Braze REST API key and Braze REST endpoint.

Once you have filled in all fields, click **Save** to complete the integration and access the integration endpoints and API token.

![][11]

### Step 3: Install Sendbird Notification Builder

Sendbird Notification Builder is a Google Chrome extension that allows you to send customized notifications through the Sendbird on the Braze Dashboard. Install the extension from the [Chrome Web Store][6].

![][12]

#### Add Sendbird credentials to the extension

Once the extension is installed, click the Sendbird icon in your browser's toolbar and select **Settings**. Copy your app ID and API token from the **Sendbird Notification Builder** section on the **Integrations** page of the Step 2 above into the Settings.

### Step 4: Map Sendbird user ID to Braze user ID

A Sendbird user ID needs to be added to a Braze user profile as a [custom attribute][5] for the integration to be used. You can upload and update user profiles via CSV files from the [User Import][8] page. Alternatively, you can use the Braze user ID as the Sendbird user ID.

### Step 5: Set up your webhook template

From **Templates & Media**, go to **Webhook Templates** and choose the **Sendbird Webhook Template**. Note that this template will only be available if you have installed the Sendbird Notification Builder extension.

![][9]

1. Provide a template name and add teams and tags, as necessary.
2. Copy a Realtime or Batch endpoint from the Sendbird dashboard into the **Webhook URL**.
3. In the **Receiver** field, click the "plus" icon and insert the user attribute mapped to the Sendbird user ID.
    1. `{{ '{{' }}custom_attribute.${sendbird_id}}}` if you are using a custom attribute `sendbird_id` as the Sendbird user ID.
    1. `{{ '{{' }}${user_id}}}` in case you are using Braze user ID as the Sendbird user ID.
4. In the **Settings** tab, replace `SENDBIRD_API_TOKEN` with the Notifications API token from the Sendbird dashboard.
5. Save the template.

## Using this integration

### Campaigns

1. Go to your Braze dashboard.
2. On the **Campaigns** page, click **Create Campaign** and select **Webhook**.
3. Select the webhook template you created above. It's highly recommended you use the Batch endpoint for campaigns.
4. Select a template in the **Template** dropdown.
5. Customize the template by editing its variables in the **Compose** tab.

### Canvas

1. From a new or existing Canvas, add a **Message** component. 
2. Open the component and select **Webhook** from the **Messaging Channels**.
3. Select the webhook template you created above. It's highly recommended you use the Realtime endpoint for canvases.
4. Select a template in the **Template** dropdown.
5. Customize the template by editing its variables in the **Compose** tab.

## Customization

### Track delivery and open status

To integrate the notifications' delivery and open status event with the campaign’s conversion metric, add a custom event on the Braze dashboard.

1. From the Braze dashboard, go to **Settings > Manage Settings > Custom Events**, and click **+ Add Custom Event**.
2. Once you’ve created a custom event, click **Manage Properties**, add a property named "status", and choose "String" for the property type.
3. When you compose a notification in campaigns or canvases, enter the name of the custom event into the **Event Name** field.

This custom event will be triggered twice for each notification; when a message is sent, and when a user opens the message.

1. When a message is sent: a custom event is triggered with `SENT` status.
1. When a message is read: a custom event is triggered with `READ` status.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://sendbird.com/docs/notifications/v1/uikit/ios/install-uikit
[3]: https://sendbird.com/docs/notifications/v1/uikit/android/install-uikit
[4]: https://sendbird.com/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/
[6]: https://chrome.google.com/webstore/detail/apbhgfffamdcdogeijjcnjbmghahoaji
[7]: https://sendbird.com/docs/notifications/v1/templates
[8]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv
[9]: {% image_buster /assets/img/sendbird/webhook-template.png %}
[10]: {% image_buster /assets/img/sendbird/sendbird-dashboard-template.png %}
[11]: {% image_buster /assets/img/sendbird/sendbird-dashboard-integrations.png %}
[12]: {% image_buster /assets/img/sendbird/sendbird-notification-builder.png %}
[13]: {% image_buster /assets/img/sendbird/use-cases.png %}
