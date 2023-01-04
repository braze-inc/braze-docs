---
nav_title: Phrasee React
article_title: Phrasee React
page_order: 2
description: "This article outlines the partnership between Braze and Phrasee React that leverages Braze Currents and Connected Content to collect click tracking information from your subscribers via webhooks. Phrasee then ties those events back to your language variants for real-time language optimization."
page_type: partner
search_tag: Partner

---

# Phrasee React

> [Phrasee][1] brings together artificial intelligence, computational linguistics, and a spirit of customer-centricity to help deploy brand language, at scale, across channels that are customized to your brand voice.

Phrasee [React](https://phrasee.co/platform/react/), powered by Phrasee X, leverages Braze Currents and Connected Content to collect click tracking information from your subscribers via webhooks. Phrasee then ties those events back to your language variants for real-time language optimization. 

## Prerequisites

| Requirement | Description |
|---|---|
| Phrasee account | A [Phrasee account][3] is required to take advantage of this partnership. |
| Phrasee connect server token | A long string of characters that will serve as your Braze campaign's password to access your Phrasee language.<br><br>You can request this from your Phrasee customer success manager if you haven't already been provided it. |
| Currents (Optional) | In order to export data to Currents, you need to have [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) set up for your account. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Step 1: Request Phrasee Amazon S3 credentials

You'll need Phrasee to set up a dedicated Amazon S3 bucket to receive your click tracking events from Braze. Reach out to your Phrasee customer success manager to start this process. When the bucket is created, you will be provided unique credentials to create your Current. 

### Step 2: Create Current

1. In Braze, click **Currents > Create New Current > Amazon S3 Data Export**. 
2. Next, name your Current and enter a contact email.
3. Add your Phrasee AWS access key ID and secret access key in the credentials box. Then, add "phrasee-braze-currents-exports" as the AWS S3 bucket name. 
4. Lastly, add the AWS S3 bucket folder you received from your Phrasee customer success manager. It will likely be your company's name.
5. Under **General Settings**, check the "Include events from anonymous users" box, and under **Manage Engagement Events** check "Email Click".
6. When you are finished, click **Launch Current**.

### Step 3: Request to remove personally identifiable information (PII).

Next, reach out to your Braze account team to ensure no personally identifiable information is transmitted to Phrasee.

By default, the Current will include certain PII attributes like email and address. Phrasee cannot and will not receive PII, so it's critical you make a request to your Braze account team to turn this off for any event data passed along to Phrasee.

### Step 4: Phrasee X code snippets 

The linked code snippets leverage [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) and, once placed in your emails, will dynamically pull in language and a tracking pixel so Phrasee can optimize your language in real-time using Phrasee X.

These code snippets can be found in [Phrasee's documentation](https://support.phrasee.co/en/articles/6101325-braze-dynamic-optimization-code-snippets). 

{% alert tip %}
If you are having trouble viewing the code snippets, make sure you are logged in to Phrasee.
{% endalert %} 

[1]: https://phrasee.co/
[3]: mailto:awesome@phrasee.co