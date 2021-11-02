---
nav_title: Worthy
article_title: Worthy
description: "This article outlines the partnership between Braze and Worthy, a message personalization platform which allows you to create personalized, rich in-app experiences and deliver them through Braze."
alias: /partners/worthy/
page_type: partner
search_tag: Partner

---

# Worthy

> The Worthy and Braze integration allows you to easily create personalized, rich in-app experiences using Worthy's drag and drop editor and deliver them through Braze.

This article walks you through the process of integrating Worthy with your Braze environment. After completing the steps outlined in this article, you can create rich, personalized in-app experiences in Worthy that can be sent via Braze. 

Additionally, Worthy will automatically do the following:

- Create a connected content server and secured API for your messaging.
- Construct your in-app messages with analytics and click tracking that will appear directly in Braze.
- Automatically export HTML via Worthy's drag and drop editor to use in **Custom Code** in-app message campaigns in Braze, complete with the required API connections and dynamic content you configure.

## Use cases

- Custom welcome experiences based on user onboarding selections
- In-app experiences for special events and promotions
- Gathering customer feedback and ratings based on app behavior
- Quickly testing potential app product ideas
- Rich notices, news, and community updates

## Requirements

| Requirement | Origin | Access | Description |
|---|---|---|---|
| Braze SDK | Braze | Braze | You will need to configure the Braze SDK in your mobile application in order to send rich in-app messages. |
| Worthy Account | Worthy | [Worthy](https://worthy.ai/) | You will need a Worthy account to use the Worthy message creator. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Personalized message integration

### Step 1: Create personalized messaging in Worthy

Navigate to your app in the Worthy dashboard, select the **Message Creator**, and create a personalized message you want to engage your users with.

### Step 2: Create a Braze campaign

Create an [in-app message campaign]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/) in Braze and set the **Message Type** to **Custom Code**.

### Step 3: Copy your personalized message into Braze

In the Worthy Message Creator, click **Export** and select Braze to export your personalized message for use in Braze campaigns. Copy the exported content into the HTML text box under **HTML + Asset Zip** in the Braze campaign editor.

### Step 4: Send personalized messages!

That's it! You can immediately test your personalized message using the **Test** tab in the Braze campaign editor. 
