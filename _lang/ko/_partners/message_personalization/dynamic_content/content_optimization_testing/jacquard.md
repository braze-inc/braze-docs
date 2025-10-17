---
nav_title: Jacquard
article_title: Jacquard
alias: /partners/jacquard/
page_order: 1
description: "This reference article outlines the partnership between Braze and Jacquard Dynamic Optimisation that leverages Braze Currents and Connected Content to collect click tracking information from your subscribers through webhooks. Jacquard then ties those events back to your language variants for real-time language optimization."
page_type: partner
search_tag: Partner
---

# Jacquard Dynamic Optimisation

> [Jacquard](https://www.jacquard.com/) brings together artificial intelligence, computational linguistics, and a spirit of customer-centricity to help deploy brand language, at scale, across channels that are customized to your brand voice.

Dynamic Optimisation, powered by Jacquard X, leverages Braze Currents and Connected Content to collect click tracking information from your subscribers through webhooks. Jacquard then ties those events back to your language variants for real-time language optimization. 

## Prerequisites

| Requirement | Description |
|---|---|
| Jacquard account | A [Jacquard account](https://www.jacquard.com/) is required to take advantage of this partnership. |
| Jacquard connect server token | A long string of characters that will serve as your Braze campaign's password to access your Jacquard language.<br><br>You can request this from your Jacquard customer success manager if you haven't already been provided it. |
| Currents | In order to export data to Currents, you need to have [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) set up for your account. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Request Jacquard Amazon S3 credentials

You'll need Jacquard to set up a dedicated Amazon S3 bucket to receive your click tracking events from Braze. Reach out to your Jacquard customer success manager to start this process. When the bucket is created, you will be provided unique credentials to create your Current. 

### Step 2: Create Current

1. In Braze, select **Currents > Create New Current > Amazon S3 Data Export**. 
2. Next, name your Current and enter a contact email.
3. Add your Jacquard AWS access key ID and secret access key in the credentials box. Then, add "phrasee-braze-currents-exports" as the AWS S3 bucket name. 
4. Lastly, add the AWS S3 bucket folder you received from your Jacquard customer success manager. It will likely be your company's name.
5. Under **General Settings**, check the "Include events from anonymous users" box, and under **Manage Engagement Events** check "Email Click".
6. When you are finished, select **Launch Current**.

### Step 3: Request to remove personally identifiable information (PII).

Next, reach out to your Braze account team to ensure no personally identifiable information is transmitted to Jacquard.

By default, the Current will include certain PII attributes like email and address. Jacquard cannot and will not receive PII, so it's critical you make a request to your Braze account team to turn this off for any event data passed along to Jacquard.

### Step 4: Jacquard X code snippets 

Reach out to your Jacquard account team for the required code snippets.

These snippets leverage [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) and, after they're placed in your emails, will dynamically pull in language and a tracking pixel so Jacquard can optimize your language in real-time using Jacquard X.


