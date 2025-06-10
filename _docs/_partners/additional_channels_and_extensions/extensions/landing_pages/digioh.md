---
nav_title: Digioh
article_title: Digioh
description: "This reference article outlines the partnership between Braze and Digioh, a survey platform that lets you easily create pop-ups, forms, surveys, and communication preference centers that drive real engagement through your Braze campaigns."
alias: /partners/digioh/
page_type: partner
search_tag: Partner

---

# Digioh

> [Digioh](https://www.digioh.com/) helps you grow your lists, capture first-party data, and put your data to use in your Braze campaigns.

_This integration is maintained by Digioh._

## About the integration

The Braze and Digioh integration allows you to use their flexible drag-and-drop builder to create on-brand forms, pop-ups, performance centers, landing pages, and surveys that connect you with your customers. Digioh will aid in integration set up and help build, design, and launch your first campaign for you.

!["Create flexible email and communications preference centers with Digioh"]({% image_buster /assets/img/digioh/pref_pop_examples.png %}){: style="border:0"}

## Prerequisites

| Requirement | Description |
|---|---|
|Digioh account | A [Digioh account](https://www.digioh.com/) is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze API `/users/track/` endpoint | Your REST endpoint URL with the `/users/track/` details appended to it. Your endpoint will depend on the [Braze URL for your instance]({{site.baseurl}}/api/basics/#endpoints).<br><br>For example, if your REST API endpoint is `https://rest.iad-01.braze.com` your `/users/track/` endpoint will be `https://rest.iad-01.braze.com/users/track/`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integration 

To integrate Digioh, you must first configure the Braze connector. When completed, you will need to apply the integration to a lightbox (widget). Visit [Digioh](https://help.digioh.com/knowledgebase/digioh-integration-basics/) to read more about integration basics.

### Step 1: Create Digioh integration 

In Digioh, click the **Integrations** tab and then the **New Integration** button. Select **Braze** from the **Integration** dropdown and name the integration. 

!["Select the correct integration from the dropdown"]({% image_buster /assets/img/digioh/2.png %}){: style="max-width:50%;"}

Next, enter the Braze REST API key and your Braze API `/users/track/` endpoint. 

Lastly, use the map fields section to map additional custom fields beyond email and name. The following code snippet shows an example payload. When completed, select **Create Integration**.

```json
{
    "attributes" : [
         {
           "external_id": "[EMAIL_MD5]",
           "email" : "[EMAIL]"
         }
     ]
}
```

### Step 2: Create a Digioh lightbox

Use the Digioh [design editor](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/) to build a lightbox (widget). <br>
Interested in seeing a gallery of ways to leverage the design editor? Visit the Digioh [theme gallery](https://www.digioh.com/theme-gallery).

### Step 3: Apply integration

To apply this integration to a Digioh [lightbox](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/), navigate to the **Boxes** page and select **Add** or **Edit** link in the **Integrations** column. This can also be added from the **Integration** section of the editor.

!["Add the integration to a lightbox"]({% image_buster /assets/img/digioh/3.png %}){: style="max-width:90%"}

Here, select **Add Integration**, choose your desired integration, and **Save**. Digioh will now pass your captured leads to Braze in real-time.


