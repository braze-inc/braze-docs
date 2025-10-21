---
nav_title: Kickbox
article_title: Kickbox
alias: /partners/kickbox/
description: "This reference article outlines the partnership between Braze and Kickbox. Kickbox makes it easy to verify your email lists, or integrate email verification into your application"
page_type: partner
search_tag: Partner
---

# Kickbox

> [Kickbox](https://kickbox.com/) is your all-in-one email verification platform, packed with the features, integrations and security you need to keep your email data clean and deliverable.

Improve the deliverability of your Braze campaigns by using Kickbox email verification. Identify undeliverable and low quality email addresses before you hit send.

## Prerequisites

| Requirement                           | Description                                                                   |
| --------------------------------------|-------------------------------------------------------------------------------|
| Kickbox account                       | An active Kickbox account is required to use this integration.                |
| Braze Rest API Key   | A Braze Rest API Key with users.track permissions <br><br>This can be created in the Braze Dashboard via Settings > APIs and Identifiers > API Keys|
| Request access to the integration     | Ask Kickbox support team to grant you access to the Braze integration.        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## About the Integration

Kickbox allows users to validate the quality of their users' email addresses at the moment a user profile is updated in Braze. This is achieved by a dedicated Canvas or Campaign flow, which is triggered by the population of a profile's "email" field. <br><br>The Canvas or Campaign will send a webhook to Kickbox, sharing the user's email address. Kickbox will validate the email address and use Braze's Rest API endpoint to update the user profile with a custom attribute detailing its quality.

## Integration

To integrate with Kickbox, follow the steps in [Integrating with Braze](https://docs.kickbox.com/docs/integrating-with-braze#/).

## Use Cases

###Bulk Verification

You may also choose to verify your entire list every few months or quarterly, to protect yourself from emails that churn or lists that degrade over time and slowly bring your deliverability down.<br><br>To do this, you need only change one part of the workflow outlined by Kickbox, the Entry Schedule settings. Rather than selecting "Action-Based Delivery", select "Scheduled". Then choose a scheduled time for your list to be verified all at once.

###Create Verified Segments

Kickbox's custom attributes have a consistent schema, matching the examples below

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

Braze users can therefore create audience segments of users with verified email addresses to ensure that their Campaigns and Canvasses have a higher delivery success rate, protecting their reputation with ESPs.<br><br>In the Braze Dashboard, navigate to Audience > Segments > Create Segment > Filter Group > Custom Attribute > result. Depending on the use case, it may be appropriate to create a Segment where the Kickbox Custom Attribute "result" exists on a profile, or where its value equals "deliverable".<br>This filter can be used on it's own to create a Segment, or could be made a part of all future Segments to ensure the validity of all the users within. 
