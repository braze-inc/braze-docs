---
nav_title: Dyspatch
article_title: Dyspatch
alias: /partners/dyspatch
description: "This article outlines the partnership between Braze and Dyspatch, a drag-and-drop email builder that allows you to create beautiful, responsive, and engaging emails without the need to write code."
page_type: partner
search_tag: Partner

---

# Dyspatch

> [Dyspatch][1] offers an intuitive drag and drop email builder used to create beautiful, responsive, and engaging emails without needing to write code. Collaborate with your team to create and approve emails within Dyspatch and then export them to Braze, all in a few quick steps! 

The Dyspatch and Braze integration allow you to simplify your email creation lifecycle by exporting Dyspatch email templates directly to Braze.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Dyspatch account | A [Dyspatch account][3] with an [owner or admin role][4] is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API Key with full **Templates** permissions. <br><br> This can be created within the __Braze Dashboard -> Developer Console -> REST API Key -> Create New API Key__ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Integration

The Braze and Dyspatch integration lets you export Dyspatch email templates directly into your Braze media library or download your template and manually upload it. 

### Step 1: Create the Braze integration

In the Dyspatch administration portal, open your username drop-down menu and select **Integrations**. Create a new integration, select **Braze**, and enter your Braze API key.

In the **Localize Exports By** field, you can choose how you would like to manage localizations. This field allows you to [localize your email templates][6] and export them to Braze to easily send emails personalized by language or locale. 

![Dyspatch Export Template]({% image_buster /assets/img/dyspatch/dyspatch_integration_create.png %}){: style="max-width:50%;"}

### Step 2: Export template to Braze

After completing an email in Dyspatch, to send your template to Braze, view the published email template and click **Download/Export** and then **Export to Integration**.

If you want to upload your template manually, view the published email template and  click **Download/Export** and then **Download HTML**. Next, in the **Templates & Media > Email Templates** section of your Braze account, select **From File** to upload your template.

![Dyspatch Export Template]({% image_buster /assets/img/dyspatch/dyspatch_export.gif %})

{% alert important %}
Do not select **Inline CSS** in the **Sending Info** section for any Dyspatch email template in Braze. Dyspatch takes care of this by making sure your emails are robust, responsive, and ready to send.
{% endalert %}

### Usage

Find your uploaded Dyspatch template in your Braze account's **Templates & Media > Email Templates** section. You can now use this email template to start sending engaging email messages to your customers!

[1]: https://www.dyspatch.io
[2]: https://dashboard.braze.com/sign_in
[3]: https://www.dyspatch.io/login/
[4]: https://docs.dyspatch.io/administration/dyspatch_roles/
[5]: https://docs.dyspatch.io/exports/export_to_braze/#download-your-template
[6]: https://docs.dyspatch.io/localization/localizing_a_template/
