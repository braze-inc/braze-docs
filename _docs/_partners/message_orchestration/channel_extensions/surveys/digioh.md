---
nav_title: Digioh
article_title: Digioh
page_order: 1
description: "Digioh lets you easily create pop-ups, forms, surveys, and communication preference centers that drive real engagement through your Braze campaigns."
alias: /partners/digioh/
page_type: partner
search_tag: Partner

---

# Digioh

> [Digioh](https://www.digioh.com/) helps you grow your lists, capture first-party data, and put your data to use in your Braze campaigns. The drag-and-drop builder makes it easy to create on-brand forms, pop-ups, preference centers, landing pages, and surveys that connect you with your customers. Integration setup is included in every package, and Digioh will also help build, design, and launch your first campaign for you.

!["Create flexible email and communications preference centers with Digioh"][5]{: style="border:0"}

## Requirements

| Requirement | Origin | Access | Description |
|---|---|---|---|
| Braze API Key | Braze | You will need to create a new API Key.<br><br>This can be created in the __Developer Console -> API Settings -> Create New API Key__ with __users.track__ permissions. | You will need to copy this key to your Digioh account - see the instructions below. |
| Braze REST Endpoint | Braze | You will need the server endpoint your account uses to access Braze's API. [See Braze's API documentation for details][6].  | You will need to copy this URL to your Digioh account - see the instructions below. |
| Digioh Account | Digioh | [https://www.digioh.com/](https://www.digioh.com/)  | You will need to have a Digioh account. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Integration details

### Step 1: Create Digioh integration 

In the Digioh platform, click the **Integrations** tab, and create the **+ New Integration** button.

Next, select **Braze** from the **Integration** dropdown and name the integration. Enter the **Braze API Key** and **Braze REST Endpoint** from your Braze account in the fields provided. Click **Create Integration**. 

!["Select the correct integration from the dropdown"][2]{: style="max-width:50%;"}

### Step 2: Map additional fields

On the **Integrations** page, use the **Map Fields** link to map additional fields beyond email and name.

### Step 3: Apply integration

To apply the integration to a [lightbox](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/), use the **Add** or **Edit** link in the **Integrations** column on the **Boxes** page.

!["Add the integration to a box"][3]{: style="max-width:80%"}

You can also add it from the **Integration** section of the editor.

!["Add the integration to a box in the editor"][4]{: style="max-width:30%"}

That's all there is to it! Digioh will now pass your captured leads to Braze in real-time.

[2]: {% image_buster /assets/img/digioh/2.png %}
[3]: {% image_buster /assets/img/digioh/3.png %}
[4]: {% image_buster /assets/img/digioh/4.png %}
[5]: {% image_buster /assets/img/digioh/pref_pop_examples.png %}
[6]: https://www.braze.com/docs/api/basics/#endpoints