---
nav_title: Dyspatch
article_title: Dyspatch
alias: /partners/dyspatch
description: "This article outlines the partnership between Braze and Dyspatch, a drag-and-drop email builder that allows to create beautiful, responsive, and engaging emails without the need to write code."
page_type: partner
search_tag: Partner

---

# Dyspatch


> use [dyspatch][1] and braze together to simplify your email creation lifecycle and deliver engaging email experiences at scale. 

With Dyspatch, use the intuitive drag and drop email builder to create beautiful, responsive, and engaging emails without needing to write code. Collaborate with your team to create and approve emails within Dyspatch and then export them to Braze, all in a couple of quick steps! 

## Integration requirements

Requirement   | Source | Description
--------------|--------| -----
Braze API Key | [Braze](https://dashboard.braze.com/sign_in) | The API key must have the *Template's* permission enabled before use.
Dyspatch Account | [Dyspatch][3] | To export an email from Dyspatch the account will need to have an [owner or admin role][4] assigned.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Integration
export email templates from dyspatch directly into your braze media library with dyspatch's braze integration. dyspatch also supports [downloading your email template][5] to manually import it to braze.

### Step 1: create a braze integration
You will need to have a [Dyspatch admin role][4] assigned to create an integration and you'll also want to have your Braze API key with __Template's__ permission ready for this step.

In Dyspatch's Administration portal, open your username drop-down menu, and select __Integrations__.

![Dyspatch Export Template]({% image_buster /assets/img/dyspatch/dyspatch_admin_dropdown.png %}){: style="max-width:60%;"}

Create a new integration, select Braze and enter your Braze API key.

![Dyspatch Export Template]({% image_buster /assets/img/dyspatch/dyspatch_integration_create.png %}){: style="max-width:50%;"}

You can choose how you would like to manage localizations when creating your Braze integration. This way you can use Dyspatch to [localize your email templates][6] and export them to Braze to easily send emails personalized by language or locale. Select either the Braze property __Language__ or __Most Recent Locale__ for your localized templates.

### Step 2: export an email from dyspatch into braze
After your team has approved an email, click __Download/Export__ when viewing the published email template and select __Export to Integration__ to send your Dyspatch email template to your Braze account.

![Dyspatch Export Template]({% image_buster /assets/img/dyspatch/dyspatch_export.gif %})

{% alert important %}
 __Inline CSS__ in the __Sending Info__ section for any Dyspatch email template in Braze should __not be selected__.  Dyspatch takes care of this by making sure your emails are robust, responsive, and ready to send.

{% endalert %}

### Usage
your new email template can be found in the __templates & media > email templates__ section of your braze account. you can now use this email template to start sending engaging email messages to your customers!

[1]: https://www.dyspatch.io
[2]: https://dashboard.braze.com/sign_in
[3]: https://www.dyspatch.io/login/
[4]: https://docs.dyspatch.io/administration/dyspatch_roles/
[5]: https://docs.dyspatch.io/exports/export_to_braze/#download-your-template
[6]: https://docs.dyspatch.io/localization/localizing_a_template/
