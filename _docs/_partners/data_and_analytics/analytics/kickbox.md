---
nav_title: Kickbox
article_title: Kickbox
alias: /partners/kickbox/
description: "This reference article outlines the partnership between Braze and Kickbox, an email verification platform used to validate email lists or integrate verification into your application."
page_type: partner
search_tag: Partner
---

# Kickbox

> [Kickbox](https://kickbox.com/) is an all-in-one email verification platform, packed with the features, integrations, and security you need to keep your email data clean and deliverable. The Kickbox integration improves the deliverability of your Braze campaigns by using Kickbox email verification to identify undeliverable and low quality email addresses before you hit send.

Kickbox allows you to validate the quality of your users' email addresses at the moment a user profile is updated in Braze. This is achieved by a dedicated Canvas or campaign workflow, which is triggered by the population of a profile's `email` field.

The Canvas or campaign will send a webhook to Kickbox, sharing the user's email address. Kickbox will validate the email address and use the Braze REST API endpoint to update the user profile with a custom attribute detailing its quality.

## Prerequisites

| Requirement                           | Description                                                                   |
| --------------------------------------|-------------------------------------------------------------------------------|
| Kickbox account                       | An active Kickbox account is required to use this integration.                |
| Braze REST API Key   | A Braze REST API key with `users.track` permissions. <br><br>This can be created in the Braze dashboard by going to **Settings** > **APIs and Identifiers** > **API Keys**|
| Request access to the integration.     | Ask the Kickbox support team to grant you access to the Braze integration.        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integration

To integrate with Kickbox, follow the steps in [Integrating with Braze](https://docs.kickbox.com/docs/integrating-with-braze#/).

## Use cases

### Bulk verification

You may also choose to verify your entire list every few months or quarterly, to protect yourself from emails that churn or lists that degrade over time and slowly bring your deliverability down.

To do this, you'll need to change the **Entry Settings** settings of the workflow, as outlined by Kickbox. Instead of selecting **Action-Based Delivery**, select **Scheduled**. Then choose a scheduled time for your list to be verified all at once.

### Create verified segments

Kickbox's custom attributes have a consistent schema, matching the following examples.

{% raw %}
```json
   {
  "attributes": [
    {
      "email": "example1@kickbox.com",
      "_update_existing_only": true,
      "success": true,
      "code": null,
      "message": null,
      "result": "deliverable",
      "reason": "accepted_email",
      "role": false,
      "free": false,
      "disposable": false,
      "accept_all": false,
      "did_you_mean": null,
      "sendex": 1,
      "user": "example1",
      "domain": "kickbox.com"
    },
    {
      "email": "example2@gamil.com",
      "_update_existing_only": true,
      "success": true,
      "code": "44312",
      "message": "SMTP verification",
      "result": "undeliverable",
      "reason": "rejected_email",
      "role": false,
      "free": false,
      "disposable": false,
      "accept_all": false,
      "did_you_mean": "example2@gmail.com",
      "sendex": 0.23,
      "user": "example2",
      "domain": "gamil.com"
    }
  ]
}
```
{% endraw %}

This means you can create audience segments of users with verified email addresses so that your campaigns and Canvases have a higher delivery success rate, protecting your reputation with ESPs.

To do so, follow these steps:

1. In Braze, go to **Audience** > **Segments** > **Create Segment**.
2. In the **Filter Group** section, add the **Custom Attribute** filter and select "result" in the dropdown. 

Depending on your use case, it may be appropriate to create a segment where the Kickbox custom attribute "result" exists on a user profile, or where its value equals "deliverable". This filter can be used on its own to create a segment, or can be made a part of all future segments to validate all the users within. 