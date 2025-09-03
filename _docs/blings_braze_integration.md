---
nav_title: Blings
article_title: Blings
description: "This reference article outlines the integration between Braze and Blings."
alias: /partners/blings/
page_type: partner
search_tag: Partner
layout: dev_guide

---

# Blings

> [Blings](https://www.blings.io/) is a next-generation personalized video platform that enables brands to deliver real-time, interactive, and data-driven video experiences across channels at scale.  

_This integration is maintained by Blings._

## Prerequisites  

| Requirement     | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| Blings account  | A Blings account is required to take advantage of this partnership.         |  

## Integration Instructions  

If you are interested in activating the Blings and Braze integration, please contact Blings support to receive your personalized HTML snippet.  

### Step 1: Request Your Snippet  
Reach out to Blings for the HTML snippet that corresponds to your campaign use case.  

### Step 2: Create a Braze Campaign  
In Braze, create a new email or in-app message campaign and insert the HTML snippet provided by Blings.  

### Step 3: Replace the default Blings parameters with Braze Personalization liquid tags  
Swap the placeholders in the snippet provided by Blings with Braze liquid personalization tags so that customer data is pulled dynamically.  

**Example:**  

Original snippet:  

```
https://blings.mp5.live/timhortons?&user_points={Points}&Name={First_Name}
```  

Updated with Braze tokens:  

```
https://blings.mp5.live/timhortons?&user_points={{custom_attribute.${points}}}&Name={{${first_name}}}
```  

![Example Image](images/image1.png)  

### Step 4: Test and Launch  
Preview the campaign in Braze to confirm the personalized fields are populating correctly. Once validated, deploy your personalized interactive video campaign at scale.  

## Support  

For any questions or to request your snippet, contact Blings directly at [support@blings.io](mailto:support@blings.io) or go to the [help center](https://blings.gitbook.io/blings-knowledge-base/documentation).  
