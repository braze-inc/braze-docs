---
nav_title: The Trade Desk
article_title: Canvas Audience Sync to The Trade Desk
description: "This reference article covers how to use Braze Audience Sync with The Trade Desk to deliver advertisements based upon behavioral triggers, segmentation, and more."
alias: /trade_desk_audience_sync/
Tool:
  - Canvas
page_order: 7
---

# Audience Sync to The Trade Desk

> Using the Braze Audience Sync to The Trade Desk, you can dynamically sync your first-party user data from Braze directly into The Trade Desk for ad retargeting, lookalike modeling, and suppression. 

**Common use cases for audience syncing include:**

- Retargeting your existing users on The Trade Desk with personalized campaigns.
- Sending first-party data to The Trade Desk for exclusion targeting.
- Syncing users to new or existing audiences or CRM data segments.

## Prerequisites 

Make sure you have the following items created, completed, or accepted before setting up the Audience Sync step with The Trade Desk in Canvas.

| Requirement | Origin | Description |
| --- | --- | --- |
| API token | [The Trade Desk](https://partner.thetradedesk.com/v3/portal/api/doc/Authentication#ui-method-create) | A standard API token created in The Trade Desk platform. We recommend setting the API token lifetime to up to one year to avoid minimal disruption to your Canvases with The Trade Desk Audience Sync. |
| The Trade Desk Terms & Policies | The Trade Desk | You must agree to a UID2/CRM participation policy before being enabled to send data to The Trade Desk. Contact your representative at The Trade Desk to confirm you have the appropriate signature to enable data delivery to The Trade Desk.<br><br> {::nomarkdown}<ul><li>Confirm that CRM Data Management Access is enabled on your account&#8212your representative at The Trade Desk can help with this. You must have your advertiser ID.</li><li>Have your standard API token ready. You can follow the instructions on this page to generate one.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

### Step 1: Connect The Trade Desk account

To get started, go to **Partner Integrations** > **Technology Partners** > **The Trade Desk**. Provide the following details from your Trade Desk account:

- **API token**
- **Advertiser ID name** (this optional name identifies the advertiser account to reference in the Audience Sync Canvas step)
- **Advertiser ID** 

Then, select **Connect**.

![An example of an unconnected Audience Sync for The Trade Desk.]({% image_buster /assets/img/audience_sync/trade_desk/connect_sync.png %}){: style="max-width:90%;"}

### Step 2: Add an Audience Sync step with The Trade Desk

Add a component in your Canvas and select **Audience Sync**. Then, select **The Trade Desk** as the Audience Sync partner.

![Option to select your partner to sync with the Audience Sync step.]({% image_buster /assets/img/audience_sync/trade_desk/audience_sync_step.png %}){: style="max-width:90%;"}

### Step 3: Set up your sync

Next, configure your sync details:

1. Select an ad account.
2. Choose an existing audience or create a new audience.

![Audience Sync setup with an audience field containing the name "valentines2025".]({% image_buster /assets/img/audience_sync/trade_desk/choose_audience.png %}){: style="max-width:90%;"}

{: start="3"}
3. Select an action to either **Add Users to Audience** or **Remove Users from Audience**.

![Audience Sync setup to add users to audience.]({% image_buster /assets/img/audience_sync/trade_desk/audience_sync_step2.png %}){: style="max-width:90%;"}

{: start="4"}
4. Choose one of the following fields to match: **Email**, **Phone**, or **Mobile Advertiser ID**.

{% alert note %}
If you're syncing to an audience in The Trade Desk with a region set to the EU, phone number isn't supported by The Trade Desk. Reach out to The Trade Desk for phone number support in the EU region.
{% endalert %}

### Step 4: Launch your Canvas

After you have configured your Audience Sync to The Trade Desk, you're ready to launch the Canvas! The new audience will be created, and users who flow through the Audience Sync step will be passed into this audience on The Trade Desk. If your Canvas contains subsequent components, your users will advance to the next step in their user journey.

## Frequently asked questions

### How long will it take for the audience sizes to populate in The Trade Desk?

This can take up to 24 hours.

### What is the minimum audience size for The Trade Desk to populate within your ad account?

There is no minimum audience size for CRM audiences in The Trade Desk.

### How do I know if users have matched after passing users to The Trade Desk?

In The Trade Desk, received IDs will populate next to the segment.

- Received IDs are the number of IDs we received in the last 30 days.
- Active IDs are the number of IDs we've seen in bidding in the last seven days.

### How many audiences can The Trade Desk support?

There is no limit for how many audiences can be supported on The Trade Desk.
