---
nav_title: Blings
article_title: Blings
description: "This reference article outlines the integration between Braze and Blings."
alias: /partners/blings/
page_type: partner
search_tag: Partner
---

# Blings

> [Blings](https://www.blings.io/) is a next-generation personalized video platform that enables you to deliver real-time, interactive, and data-driven video experiences across channels at scale.  

_This integration is maintained by Blings._

## Prerequisites  

| Requirement     | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| Blings account  | A Blings account is required to take advantage of this partnership.         |  

## Integration  

If you are interested in activating the Blings and Braze integration, contact Blings support to receive your personalized HTML snippet.  

### Step 1: Request your snippet

Contact Blings for the HTML snippet that corresponds to your campaign use case.  

### Step 2: Create a Braze campaign  

In Braze, create a new email or in-app message campaign and insert the HTML snippet provided by Blings.  

### Step 3: Replace the default Blings parameters with Braze personalization Liquid tags  

Swap the placeholders in the snippet provided by Blings with Braze Liquid personalization tags so that user data is dynamically pulled.  

For example, let's consider this snippet: 

{% raw %}
```liquid
https://blings.mp5.live/timhortons?&user_points={Points}&Name={First_Name}
```  

After being updated with Braze tokens, the snippet would become:  

```liquid
https://blings.mp5.live/timhortons?&user_points={{custom_attribute.${points}}}&Name={{${first_name}}}
```  
{% endraw %}

![Blings gif in Braze campaign.]({% image_buster /assets/img/blings/blings_braze_campaign.png %})  

### Step 4: Test and launch  

Preview the campaign in Braze to confirm the personalized fields are populating correctly. After validating, deploy your personalized interactive video campaign at scale.  

## Getting support  

For any questions or to request your snippet, contact Blings at [support@blings.io](mailto:support@blings.io) or refer to the [Blings help center](https://blings.gitbook.io/blings-knowledge-base/documentation).  
