---
nav_title: Lemnisk
article_title: Lemnisk
description: "This reference article details the partnership between Braze and Lemnisk, a AI-enabled customer data platform-led Marketing Automation platform, allowing you to stream user data collected at Lemnisk from various sources, into Braze to activate them across various channel and destinations using Braze's tools."
alias: /partners/lemnisk/
page_type: partner
search_tag: Partner

---

# Lemnisk

> [Lemnisk](https://www.lemnisk.co/), is an AI-powered Customer Data Platform (CDP) and Marketing Automation solution that enables real-time capture, unification, and activation of customer data from diverse, siloed sources. It seamlessly delivers this unified data across various martech and business platforms, while offering robust, real-time analytics to track every stage of the customer data lifecycle. 

_This integration is maintained by Lemnisk._

## About the integration

Lemnisk and Braze integration will allow brands and enterprises unlock the full potential of Braze by acting as a CDP-led intelligence layer that unifies user data across platforms in real time, and sending the user's information and behviours collected to Braze in real-time. Lemnisk delivers enriched customer profiles—blending behavioral signals and personal attributes—directly into Braze, enabling brands to personalize messaging from Braze with deeper context.

## Prerequisites

| Requirement | Description |
| --- | --- |
| Lemnisk and Braze Accounts | An existing user of [Lemnisk](https://www.lemnisk.co/) and [Braze](https://www.braze.com/) can take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track` permission. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance](https://portal.aws.amazon.com/billing/signup#/start). |
| S3 authentication | You will need access to an Amazon Web Services (S3) server to export and import the data. |
| Access key ID<br>Secret access key | The access key ID and secret access key will allow you to authenticate your S3 server for importing and exporting. |
| AWS bucket | You will need to connect to S3 within the plugin. After authentication, the available buckets will show in a dropdown menu. This is where files to be imported or exported are stored. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integration

### Step 1: Creating a Braze connection

In BlueConic, select **Connections** in the navigation bar, and then **Add Connection**. In the prompt that appears, search **Braze** and select **Braze connection**. 

Expand or collapse available metadata fields in the connection by clicking the gray chevron icon. Within these fields, you can favorite this connection, name your connection, add labels, include a description, and choose to get email notifications if the connection [runs or fails to run](https://support.blueconic.com/hc/en-us/articles/205957522#h_01F4VR7SG7NKB3FMQXCB2Q8JNZ). 

Save your settings.

### Step 2: Configuring a Braze connection

To configure the connection between BlueConic and Braze, you must add your Braze account credentials and Amazon Web Services (S3) account information to authenticate the connection. 

1. In BlueConic, select **Set up and run** in the **Setup** section in the left panel.<br><br>
2. In the Braze authentication page that opens, enter your Braze REST API endpoint and Braze API key.<br>
![]({% image_buster /assets/img/blueconic/braze2.png %}){: style="max-width:80%;"}<br><br>
3. In the S3 setup and authentication section, enter these credentials: Amazon Web Services (S3) access key ID, secret access key, and S3 bucket. They need to be the [same credentials]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) you configured when setting up your Braze and Amazon S3 integration. Save your settings. <br>![]({% image_buster /assets/img/blueconic/braze3.png %}){: style="max-width:80%;"}

### Step 3: Creating import or export goals (import mapping)

Once the authentication is complete, you must create at least one import or export goal, turn the connection on, and schedule or run the connection.

{% tabs %}
{% tab Import %}

1. Select **Import data into BlueConic** in the left panel to open the Braze data configuration page.<br><br>
2. Select the location of the data in Braze. Here, you can tell BlueConic where to find the data to be imported by selecting your Braze audience.<br>![The BlueConic Braze audience set as "BlueConic Test Users".]({% image_buster /assets/img/blueconic/braze4.png %}){: style="max-width:80%;"}<br><br>
3. Next, map identifiers between Braze and BlueConic. <br>![The Braze field "External ID" set to map to the BlueConic "Braze external ID" field.]({% image_buster /assets/img/blueconic/braze5.png %}){: style="max-width:80%;"}<br><br> To link the customer data between the two systems, enter one or more customer identifiers.<br>Use the **Allow creation...** checkbox to allow BlueConic to create new profiles for data that does not match an existing BlueConic profile.<br><br>
4. Next, match the BlueConic data fields you are exporting to Braze fields. Use the dropdown fields to select either the BlueConic profile identifier or a profile property on the left and select the corresponding Braze profile identifier. Next, use the dropdown menu to specify how imported content should be added to existing values: added, summed, set only if the profile property is empty, or set to clear (if the Braze field is empty).<br>![]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>Use the **Add Mapping** button to create additional mapping rows as needed. You can add multiple mapping rows with the **Add remaining fields** option. BlueConic detects the remaining Braze fields and matches them with BlueConic profile properties. You can set the merge strategy for imports (set, add, sum, set if empty or clear) and provide a custom prefix to the names of BlueConic profile properties.<br><br>
5. Lastly, select **Run the connection** to start the connection. Visit [BlueConic](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections) to learn more about scheduling and running connections.
{% endtab %}
{% tab Export %}

1. Select **Export data to Braze** in the left panel to configure your data export from BlueConic to Braze.<br><br>
2. Choose a BlueConic segment for the export. Only profiles in this segment with matching identifiers in Braze will be exported.<br>![A BlueConic segment of 20k profiles.]({% image_buster /assets/img/blueconic/braze8.png %}){: style="max-width:80%;"}<br><br>
3. Next, link identifiers between BlueConic profiles and Braze fields. You can optionally choose to let BlueConic create new records if no existing match is found.<br>![The Braze field "External ID" set to map to the BlueConic "Braze external ID" field.]({% image_buster /assets/img/blueconic/braze7.png %}){: style="max-width:80%;"}<br><br>
4. Next, match the BlueConic data fields you are exporting to Braze fields. Use the dropdown menu from the BlueConic icon to choose the type of [information](https://support.blueconic.com/hc/en-us/articles/4405501836955-Braze-Connection#creating-export-goals) you want to export. Available information includes profile properties, BlueConic profile identifiers, associated segments, all viewed interactions, permission levels, and a static text value.<br>![]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>
5. Lastly, click **Run the connection** to start the connection. Visit [BlueConic](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections) to learn more about scheduling and running connections.
{% endtab %}
{% endtabs %}

## Step 4: Toggle connection on

Use the toggle next to the Braze connection title to toggle the connection on and off. A connection must be on to run during scheduled times. 

