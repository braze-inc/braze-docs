---
nav_title: SalesWings
article_title: SalesWings
page_order: 1

description: "This reference article outlines the partnership between Braze and SalesWings, a lead scoring platform that offers a user-friendly, no-code solution to identify leads' interests."
alias: /partners/your_partner_name/

page_type: partner
search_tag: Partner
hidden: true
layout: dev_guide
---

# SalesWings

[SalesWings][1] is a lead scoring platform that offers a user-friendly, no-code solution to identify your leads' true interests.  

The Braze and SalesWings integration allows you to identify the leads who click on the links in your Braze email campaigns, so you can tag and prioritize these leads in SalesWings for your Marketing and Sales teams.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| SalesWings account | A [SalesWings][1] account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.export.ids` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint | [Your REST endpoint URL][2]. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

**TODO Philip**: describe the use case of identifying leads from email leads.

## Integration

### Step 1: Set up the Braze Connection in your SalesWings account

To connect SalesWings to Braze, you will need to go to the [settings][3] page of your SalesWings account. On the page, expand the **Braze Integration** section, enter the Braze REST API key and Braze REST endpoint as described in [prerequisites][4] and click **Save changes**.

### Step 2: Set up a Braze email campaign with personalized links

**TODO Philip**: describe creating a Braze campaign with personalized links leading to your website with SalesWings tracking script installed

### Step 3: Access identified leads in SalesWings cockpit or Salesforce Sales Cloud

**TODO Philip**: describe what could be done with identified leads in SalesWings 

---
[1]: https://www.saleswingsapp.com
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: https://helium.saleswings.pro/settings
[4]: #prerequisites