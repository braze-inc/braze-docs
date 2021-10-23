---
nav_title: Worthy
article_title: Worthy
description: "The Worthy and Braze integration allows you to easily create personalized, rich in-app experiences using Worthy's drag and drop editor that can be delivered via Braze."
alias: /partners/worthy/
page_type: partner
search_tag: Partner

---

# Worthy

> Worthy is the easiest way to create personalized messages an in-app experiences.

This article will walk you through the process of integrating Worthy with your Braze environment. After completing the steps outlined in this reference, you will be able to create rich, personalized in-app experiences in Worthy that can be sent via Braze. Additionally:

- Worthy will automatically create a connected content server and secured API for your messaging
- Worthy will automatically instruction your in-app messages with analytics and click tracking that will appear directly in Braze
- Worthy's drag and drop editor will automatically export HTML for Braze Custom Code campaigns with the required API connections and dynamic content you configure

#### Use Cases

- Custom welcome experiences based on user onboarding selections
- In-app experiences for special events and promotions
- Gathering customer feedback and ratings based on app behavior
- Quickly testing potential app product ideas
- Rich notices, news, and community updates

## Requirements
| Requirement | Origin | Access | Description |
|---|---|---|---|
| Braze SDK | Braze | Braze | You will need to configure the Braze SDK in your mobile application in order to send rich in-app messages.
| Worthy Account | Worthy | [Worthy](https://worthy.ai/) | A Worthy account is required to use the Worthy message creator. |


## Personalized Message Integration

### Step 1: Create Personalized Messaging in Worthy

Navigate to your app in the Worthy dashboard, select the Message Creator, and create a personalized message you want to engage your users with.

### Step 2: Create A Braze Campaign

Create a campaign in Braze and set the Message Type to `Custom Code`.

### Step 3: Copy Your Personalized Message Into Braze

In the Worthy Message Creator, click Export and select Braze to export your personalized message for use in Braze campaigns. Copy the exported content into text box under HTML + Asset Zip in the Braze Campaign Editor.

### Step 4: Send Personalized Messages!

That's it! You can immediately test your personalized message using the Test tab in the Braze Campaign Editor. 
