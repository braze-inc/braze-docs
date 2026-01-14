---
nav_title: StackAdapt
article_title: StackAdapt
description: "This reference article outlines the partnership between Braze and StackAdapt."
alias: /partners/stackadapt/
page_type: partner
search_tag: Partner
---

# StackAdapt

> [StackAdapt](https://www.stackadapt.com/) is the leading AI-powered marketing platform used by digital marketers to deliver targeted performance-driven advertising.

_This integration is maintained by StackAdapt._

The Braze and StackAdapt integration allows you to sync user profile data from Braze into the StackAdapt Data Hub. By connecting the two platforms, you can create a unified view of your customers and activate first-party data to improve ad performance.

## Use cases

- **Re-engage lapsed users:** Identify users who have unsubscribed from email marketing lists in Braze and target them with programmatic ads on StackAdapt to re-engage them through a different channel.
- **Create multi-channel experiences:** Extend a user's journey beyond email. For example, if a user clicks on an email campaign in Braze, you can use StackAdapt to show them a complementary programmatic ad, reinforcing the message and driving further action.
- **Personalize at scale:** Leverage granular data points from Braze, such as "Home City" or "Language", to serve highly relevant, localized, and language-specific ads and emails.
- **Deepen understanding of your audience:** By syncing profile attributes, you can create richer audience segments in StackAdapt, enabling more precise targeting and personalized ad experiences.

## Prerequisites

| Requirement | Description         |
| ----------- | ------------------- |
| **StackAdapt Account**  | You need an active StackAdapt account with permissions to manage Data Hub integrations. |
| **Braze REST API key**  | A Braze REST API key with the following permissions: <br>- users.export.ids<br>- users.export.segment<br>- email.unsubscribe<br>- email.hard_bounces<br>- messages.schedule_broadcasts<br>- campaigns.list<br>- campaigns.details<br>- canvas.list<br>- canvas.details<br>- segments.list<br>- segments.details<br>- purchases.product_list<br>- events.list<br>- feed.list<br>- feed.details<br>- templates.email.info<br>- templates.email.list<br>- subscription.status.get<br>- subscription.groups.get<br><br>This can be created in the Braze dashboard from **Settings** > **API Keys.** |
| **Braze REST endpoint** | [Your REST endpoint URL](https://www.braze.com/docs/api/basics/#endpoints). Your endpoint depends on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## How it works

The StackAdapt Data Hub connects directly to your Braze account to pull user profile attributes. This allows you to leverage your Braze customer data directly within StackAdapt for advanced audience segmentation and activation.

### Data flow

1. StackAdapt initiates a secure connection to your Braze instance using the provided API credentials.
2. StackAdapt retrieves user profile data and specifically the properties you have selected and mapped.
3. The data is normalized and ingested into your StackAdapt Data Hub, becoming available for segmentation and use in your campaigns.
4. The integration allows for scheduled data syncs (for example, daily) to keep your StackAdapt audiences up-to-date with the latest profile data from Braze.

## Fields synced

StackAdapt can sync a variety of Braze profile fields, including, but not limited to:

{% tabs local %}
{% tab Standard attributes %}
- Email
- Date of Birth
- First Name
- Last Name
- Phone
- Home City
- Country
- Gender
- Time Zone
- Created At
- External ID
- Language 

{% endtab %}
{% tab Custom attributes %}
Attributes that are specific to your app or business, defined based on your specific business needs.

{% endtab %}
{% tab Attribution data %}
- Attributed Ad
- Attributed Adgroup
- Attributed Campaign
- Attributed Source

{% endtab %}
{% tab Subscription status %}
- Email Subscription Status
- Push Subscription Status 

It is crucial to accurately map fields in Braze that reflect user consent for marketing communications (for example, email subscription status) so that your advertising efforts remain compliant with user preferences and privacy regulations.

{% endtab %}
{% endtabs %}

## Setting up the integration

Follow these steps to import your Braze user profiles:

1. Log into your StackAdapt account.
2. In the navigation menu, select **Data Hub**.
3. Select **Import Profiles**, then select **Braze** from the list of available integrations.
4. Enter your Braze API credentials when prompted.
- **Braze REST API Key:** Located in Braze by going to **Settings** > **API Keys**. As a security best practice, we recommend creating a dedicated API key for your StackAdapt integration.
- **Braze App Key:** Located in Braze by going to **Settings** > **API Keys** or **Manage Apps**.
- **Braze REST Endpoint URL:** The base URL for your Braze instance (for example, ```https://rest.iad-01.braze.com```).
5. Select **Connect** to verify the credentials.

![Braze connection in StackAdapt.]({% image_buster /assets/img/stackadapt/stackadapt_braze_connection_settings.png %})

{: start="6"}
6. Choose your connection and select your StackAdapt advertiser.
7. Configure your **Property Mappings**. Review and confirm the default mappings and pre-selected properties that StackAdapt suggests.
8. (Optional) If you want to import additional properties, select them by checking the respective checkboxes and specify if they contain PII and their data type.

![Braze connection in StackAdapt.]({% image_buster /assets/img/stackadapt/stackadapt_mappings.png %})

{: start="9"}
9. Add your profiles to a **List** or create a new one so you can group and segment your profiles
10. Select **Activate Integration** to start the initial data sync.

## Considerations

- **Importing custom events and properties:** This feature is not yet supported.
- **Data latency:** It can take up to 24 hours to import all of the user profile data.
- **Consent management:** Confirm that your data collection practices in Braze align with privacy regulations and that you have the necessary consent to use customer data for advertising purposes. StackAdapt relies on the consent status passed from your source systems.
- **Attribute consistency:** To maximize the effectiveness of your data, maintain consistency in how attributes are named and populated in Braze before syncing them to StackAdapt.
