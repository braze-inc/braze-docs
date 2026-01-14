---
nav_title: Nift
article_title: Nift
description: "This reference article outlines the partnership between Braze and Nift, a two-side platform that helps companies acquire, engage, and retain customers."
alias: /partners/nift/
page_type: partner
search_tag: Partner

---

# Nift

> [Nift](https://gonift.com/) helps companies acquire, engage and retain customers. The two-sided platform helps partners thank their customers with Nift gift cards. Thanking customers increases their lifetime value and generates incremental revenue.

_This integration is maintained by Nift._

## About the integration

The Braze and Nift integration allows you to automatically trigger "thank-yous" containing Nift gifts at key moments in the customer lifecycle and identify which customers used their gift. Nift gift cards can be used to access products and services supplied by brands relying on Nift's matchmaking technology to acquire new customers cost-effectively at scale.

## Prerequisites

| Requirement | Description |
|---|---|
| Nift account | A Nift account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with all user data permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | Your REST endpoint URL. Your endpoint will depend on the Braze URL for [your instance]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Connect to Braze in Nift

Visit your [Nift dashboard](https://www.gonift.com/users/sign_in), navigate to **Accounts** > **Integrations** > **Braze**, and click **Connect**.

### Step 2: Add Braze credentials

On the **Link your Braze Account** page, provide your Braze REST API key and select your Braze endpoint, which will depend on the Braze URL for [your instance]({{site.baseurl}}/api/basics/#endpoints).

You can change the customer ID parameter name in the referral link sent to your customers. Nift will use this to mark your customers as processed in Braze when they have selected a gift from one of our brands.

Click **Link Account**.

!["Nift service integration page prompting the user for the Braze API key and Braze dashboard URL.]({% image_buster /assets/img/nift/link_your_braze_account.png %})

## Using the integration

To use the integration, distribute the referral link in your messaging. When your customer uses the referral link and selects a gift from one of our brands, Nift will mark them as processed in Braze.

After integrating with Braze, Nift will automatically push events to the existing customer Braze record with the following data:

- Event name: `nift_processed`
- Time: The time the customer selected/used the gift



