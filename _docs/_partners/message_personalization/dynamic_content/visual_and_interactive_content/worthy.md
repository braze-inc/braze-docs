---
nav_title: Worthy
article_title: Worthy
description: "This reference article outlines the partnership between Braze and Worthy, a message personalization platform which allows you to create personalized, rich in-app experiences and deliver them through Braze."
alias: /partners/worthy/
page_type: partner
search_tag: Partner

---

# Worthy

> The [Worthy](https://worthy.ai/) and Braze integration allows you to easily create personalized, rich in-app experiences using Worthy's drag-and-drop editor and deliver them through Braze. Additionally, Worthy will automatically do the following:

_This integration is maintained by Worthy._

## About the integration

- Create a Connected Content server and secured API for your messaging.
- Construct your in-app messages with analytics and click-tracking that will appear directly in Braze.
- Automatically export HTML via Worthy's drag-and-drop editor to use in **Custom Code** in-app message campaigns in Braze, complete with the required API connections and dynamic content you configure.

## Use cases

- Custom welcome experiences based on user onboarding selections
- In-app experiences for special events and promotions
- Gathering customer feedback and ratings based on app behavior
- Quickly testing potential app product ideas
- Rich notices, news, and community updates

## Prerequisites

| Requirement | Description |
| --- | --- |
| [Worthy](https://worthy.ai/) account | A Worthy account is required to take advantage of this partnership. |
| Braze SDK | You will need to configure the Braze SDK in your mobile application to send rich in-app messages. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integration

### Step 1: Create personalized messaging in Worthy

Navigate to your app in the Worthy dashboard, select the **Message Creator**, and create a personalized message you want to use to engage your users.

### Step 2: Create a Braze campaign

Create an [in-app message campaign]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/) in Braze and set the **Message Type** to **Custom Code**.

### Step 3: Copy your personalized message into Braze

In the Worthy message creator, click **Export** and select **Braze** to export your personalized message for use in Braze campaigns. Copy the exported content into the HTML text box under **HTML + Asset Zip** in the Braze campaign editor.

That's it! You can immediately test your personalized message using the **Test** tab in the Braze campaign editor. 

