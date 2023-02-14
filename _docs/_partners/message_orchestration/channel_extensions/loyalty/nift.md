---
nav_title: Nift
article_title: Nift
description: "This article outlines the partnership between Braze and Nift, a two-side platform that helps companies acquire, engage and retain customers."
alias: /partners/nift/
page_type: partner
search_tag: Partner

---

# Nift

> [Nift](https://gonift.com/) helps companies acquire, engage and retain customers. The two-sided platform helps partners thank their customers with Nift gift cards. Thanking customers increases their lifetime value and generates incremental revenue. Nift gift cards can be used to access products and services supplied by brands relying on Nift's matchmaking technology to acquire new customers cost-effectively at scale.

The Braze and Nift integration allows you to automatically trigger "thank yous" containing Nift gifts at key moments in the customer lifecycle and identify which customers used their gift.

## Prerequisites

| Requirement | Description |
|---|---|
| Nift account | A Nift account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with all user data permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint | Your REST endpoint URL. Your endpoint will depend on the Braze URL for [your instance]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Step 1: Connect to Braze within Nift

Visit your [Nift Dashboard][2] and select **Integrations** under **Account**.

Next, scroll down to find **Braze** in the list of services and click **Connect**.

### Step 2: Add Braze credentials

On the **Link your Braze Account** page, provide your Braze REST API key and select your Braze Endpoint, which will depend on the Braze URL for [your instance]({{site.baseurl}}/api/basics/#endpoints).

!["Nift service integration page prompting the user for the Braze API key and Braze dashboard URL.][5]

Click **Link Account**.

### Step 3: Braze settings

When your customer uses the referral link on this page and selects a gift from one of our brands, we will mark them as processed in Braze.

!["Nift Braze Settings page after successfulling linking Nift and Braze.][6]

## Customization

On the Braze **Settings** page in Nift, you can change the customer ID parameter name in the referral link sent to your customers. We use this to mark your customers as processed in Braze when they have selected a gift from one of our brands.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://www.gonift.com/users/sign_in
[5]: {% image_buster /assets/img/nift/link_your_braze_account.png %}
[6]: {% image_buster /assets/img/nift/braze_account_linked.png %}