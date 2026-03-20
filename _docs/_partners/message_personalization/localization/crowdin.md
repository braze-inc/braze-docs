---
nav_title: Crowdin
article_title: Crowdin
description: "Use the Crowdin integration to translate campaigns, Canvas experiences, email templates, and Content Blocks with Translation Memory, glossaries, and machine translation."
alias: /partners/crowdin/
page_type: partner
search_tag: Partner

---

# Crowdin

> [Crowdin](https://crowdin.com/) is an AI-driven localization management platform that helps teams automate the translation of their software, apps, and marketing content.

Connect Crowdin to Braze to manage translations for your campaigns and Canvas experiences. Automated synchronization works with machine translation, Translation Memory, and glossaries so human and automated workflows stay consistent.

_This integration is maintained by Crowdin._

## About the integration

Crowdin offers two apps for Braze: [Braze Campaigns & Canvas](https://store.crowdin.com/braze-content-translation) and [Braze Email Templates](https://store.crowdin.com/braze-app). Choose based on the Braze features you localize. The following table compares them.

### Choosing the right Crowdin app

| Channel/feature | Braze Campaigns & Canvas | Braze Email Templates |
| --- | --- | --- |
| **Campaigns** | ✅ Supported | ❌ Not supported |
| **Canvas steps** | ✅ Supported | ❌ Not supported |
| **Email templates** | ❌ Not supported | ✅ Supported |
| **Content Blocks** | ❌ Not supported | ✅ Supported |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Prerequisites

| Requirement | Description |
| --- | --- |
| **Crowdin account** | A [Crowdin.com account](https://accounts.crowdin.com/register) or [Crowdin Enterprise account](https://accounts.crowdin.com/workspace/create) is required. |
| **Crowdin project** | Before you connect Braze, [create a translation project](https://support.crowdin.com/creating-project/) in Crowdin or Crowdin Enterprise. |
| **Braze REST API key** | A Braze REST API key with permissions for campaigns, Canvas, Content Blocks, custom attributes, email, and templates. |
| **Braze REST endpoint** | Your specific Braze REST endpoint URL (for example, `https://rest.iad-03.braze.com`). |
| **Braze multi-language settings** | Locales must be configured in your Braze dashboard under **Settings** > **Localization Settings**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Braze Campaigns & Canvas integration

If you localize content inside live messages, use the [Braze Campaigns & Canvas app](https://store.crowdin.com/braze-content-translation) to sync translatable strings from your Campaign and Canvas drafts with Braze multi-language support.

For a video walkthrough, see [Braze Campaigns & Canvas integration](https://youtu.be/ahG1ET4VRKA).

### Step 1: Set up multi-language settings in Braze

Before you connect Crowdin, add your target languages in Braze.

1. In Braze, go to **Settings** > **Localization Settings**.
2. Add the languages you plan to support.

![Braze Locales page under Settings, showing locale names, locale keys, and Add locale.]({% image_buster /assets/img/crowdin/braze_locales.png %}){: style="max-width:85%;"}

{: start="3"}
3. Note each **Locale key** (for example, `en-US`, `fr-FR`, `es-ES`). You use these values when you map languages in Crowdin.

### Step 2: Set up the Braze project in Crowdin

1. In your Crowdin Enterprise or Crowdin.com account, go to the **Store** in the left-hand menu.
2. Search for **Braze Campaigns & Canvas**, then click **Install**.

![Crowdin Store with Braze Campaigns & Canvas selected and Install highlighted.]({% image_buster /assets/img/crowdin/crowdin_store_campaigns_canvas.png %}){: style="max-width:85%;"}

{: start="3"}
3. Select the project (or projects) where you want to use this integration.
4. To open the integration, go to your project **Integrations** > **Braze Campaigns & Canvas**.

#### Connecting Braze to Crowdin

Authorize the connection with your Braze API credentials:

![Crowdin Braze Campaigns & Canvas connection form with REST API key, REST endpoint, and Log in with Braze Campaigns & Canvas.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_login.png %}){: style="max-width:85%;"}

- **Braze REST API key:** Create this in Braze under **Settings** > **APIs and Identifiers** > **API Keys**. Grant the permissions this integration needs (campaigns, Canvas, Content Blocks, and custom attributes).
- **Braze REST endpoint:** Enter the URL for your Braze instance (for example, `https://rest.iad-03.braze.com`). For more information, see [REST API endpoints]({{site.baseurl}}/api/basics/#endpoints).

![Braze REST API Keys page with Create API Key and the REST Endpoint copy control.]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %}){: style="max-width:85%;"}

- Click **Log in with Braze Campaigns & Canvas**.

### Step 3: Configure language mapping in Crowdin

After you connect your account, map each Crowdin project language to the matching Braze locale.

1. In the Braze Campaigns & Canvas integration dashboard, click the **Settings** gear icon in the top-right corner.

![Braze Campaigns & Canvas integration screen with Settings in the top action bar.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_settings.png %}){: style="max-width:85%;"}

{: start="2"}
2. Open the **General Settings** tab.
3. **Enter locale keys:** Crowdin lists your project languages (for example, French, Italian). In each field, enter the matching **Braze locale key**.
   - For example, if Braze uses `it` for Italian, enter `it` next to Italian in Crowdin.
   - Each entry must match the **Locale key** for that locale in Braze **Localization Settings** exactly.

![Settings modal on the General Settings tab, showing file filter fields and language mapping rows (for example, French mapped to fr).]({% image_buster /assets/img/crowdin/crowdin_language_mapping_settings.png %}){: style="max-width:85%;"}

{: start="4"}
4. Click **Save** to confirm the mapping.

### Step 4: Add translation tags to your Braze message

Crowdin reads the same Liquid **translation tags** Braze uses for multi-language messages. Add {% raw %}`{% translation your_id_here %}` and `{% endtranslation %}`{% endraw %} around every piece of text, image URL, or link URL you want translated. Each block needs a unique `id` (for example, `greeting` or `welcome_header`).

**Example:**

{% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

For HTML, Liquid in links, and other patterns, follow the same rules as in [Translating locales]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales) (for example, keep tags around the smallest segments possible, and wrap only language-specific parts of URLs when localizing links).

Save your Braze message as a **Draft** before Crowdin can detect and pull the content.

### Step 5: Manage translations in Crowdin

The integration screen has two sides:

- **Right side (Braze):** Your campaigns and Canvases.
- **Left side (Crowdin):** Content already synced for translation.

![Crowdin and Braze Campaigns & Canvas panels with folders for campaigns and locales, Sync to Braze, and Sync to Crowdin.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_sync_panels.png %}){: style="max-width:85%;"}

#### Syncing content

1. On the **Braze (Right)** side, select the checkbox for the campaign or Canvas to translate.
2. Click **Sync to Crowdin**.
3. When the sync is complete, the file appears on the **Crowdin (Left)** side. Translators can open the strings in the Crowdin Editor.

#### Returning translations to Braze

1. When translations are 100% complete in Crowdin, return to the **Integrations** tab.
2. Select the completed content on the **Crowdin (Left)** side.
3. Click **Sync to Braze**. This pushes the translated strings into the corresponding language variants in your Braze campaign.

### Step 6: Preview the message as a multi-language user in Braze

To confirm the integration:

1. Open your campaign in the **Braze Message Composer**.
2. Go to the **Test** tab.
3. Select **Preview Message as User**.
4. Search for a user profile that has a `language` attribute matching one of your translated locales.
5. Confirm that the content switches from the source language to the translated version.

## Braze Email Templates integration

If you localize email at the template level, use the [Braze Email Templates app](https://store.crowdin.com/braze-app) to sync HTML from your Braze Media Library.

For a video walkthrough, see [Braze Email Templates integration](https://youtu.be/g0YMKW3jEjk).

### Step 1: Install the app

1. In your Crowdin project, go to the **Store** tab.
2. Search for **Braze Email Templates** and click **Install**.

![Crowdin Store with Braze Email Templates selected and Install highlighted.]({% image_buster /assets/img/crowdin/crowdin_store_email_templates.png %}){: style="max-width:85%;"}

{: start="3"}
3. Select the project (or projects) where you want to use this integration.
4. To open the integration, go to your project **Integrations** > **Braze Email Templates**.

### Step 2: Connect to Braze

Authorize the connection with your Braze API credentials:

![Crowdin Braze Email Templates connection form with REST API key, REST endpoint, and Log in with Braze Email Templates.]({% image_buster /assets/img/crowdin/crowdin_email_templates_login.png %}){: style="max-width:85%;"}

1. **Braze REST API key:** Grant `templates.email` and `content_blocks` (read and write). Create the key in Braze under **Settings** > **APIs and Identifiers** > **API Keys**.

![Braze REST API Keys page with Create API Key and the REST Endpoint copy control.]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %}){: style="max-width:85%;"}

{: start="2"}
2. **Braze REST endpoint:** Use your instance-specific URL (for example, `https://rest.iad-03.braze.com`).
3. Click **Log in with Braze Email Templates**.

### Step 3: Sync content for translation

The integration screen shows your Braze library:

- **Right side (Braze):** **Email Templates** and **Content Blocks** you can sync.
- **Left side (Crowdin):** Content in translation.

1. On the **Braze (Right)** side, select the checkbox next to the templates or blocks you want to localize.
2. Click **Sync to Crowdin**.
3. Crowdin pulls the HTML source. Translators work in the Crowdin Editor with a live **WYSIWYG preview** so the layout stays intact.

![Crowdin Editor Preview tab showing localized email HTML and translatable strings.]({% image_buster /assets/img/crowdin/crowdin_editor_wysiwyg_preview.png %}){: style="max-width:85%;"}

### Step 4: Deliver translated templates

When translations reach 100% completion:

1. Select the completed files on the **Crowdin (Left)** side.
2. Click **Sync to Braze**.
3. Crowdin automatically creates localized versions of these assets in your Braze Media Library (for example, `Template_Name_fr`).

![Crowdin and Braze Email Templates panels listing Email Templates and Content Blocks, with Sync to Braze and Sync to Crowdin.]({% image_buster /assets/img/crowdin/crowdin_email_templates_sync_panels.png %}){: style="max-width:85%;"}

