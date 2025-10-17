---
nav_title: Adobe
article_title: Adobe
description: "This page outlines the partnership between Braze and Adobe, a customer data platform, that allows brands to connect and map their Adobe data (custom attributes and segments) to Braze in real-time. Brands can then act on this data, delivering personalized, targeted experiences to those users."
page_type: partner
page_order: 1
search_tag: Partner

---

# Adobe

> Built on the Adobe Experience Platform, Adobe's real-time customer data platform brings together known and anonymous data from multiple enterprise sources to create customer profiles. These profiles can then be used to provide personalized experiences across all channels and devices in real-time.

The Braze and Adobe CDP integration connects and maps your brand's Adobe data (custom attributes and segments) to Braze in real-time. You can then act on this data, delivering personalized, targeted experiences to your users. With Adobe, the integration is intuitive. Simply take any Adobe [identity](https://experienceleague.adobe.com/docs/experience-platform/identity/namespaces.html?lang=en), map it to a Braze external ID, and send it off to the Braze platform. All data sent will be accessible in Braze through a new `AdobeExperiencePlatformSegments` attribute.

{% alert important %}
The Adobe Experience Platform integration currently doesn't support dynamic audience membership. This means it can only add values to user profiles, not remove them.
{% endalert %}

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Adobe account | An [Adobe account](https://account.adobe.com/) is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze instance | Your Braze instance can be obtained from your Braze onboarding manager or can be found on the [API overview page]({{site.baseurl}}/api/basics/#endpoints). |
| Braze REST endpoint | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
The sending of additional custom attributes will increase your data point usage. We suggest speaking with your customer success manager to better understand this potential data point increase.
{% endalert %}

## Integration

### Step 1: Configure Braze destination

From the Adobe **Settings** page, select **Destinations** under **Collections**. From there, locate the **Braze** tile and select **Configure**. 

![]({% image_buster /assets/img/adobe/braze-destination-configure.png %})

{% alert note %}
If a connection with Braze already exists, you'll see an **Activate** button on the destination card. For more information about the difference between activate and configure, refer to the catalog section of the Adobe destination workspace [documentation](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/destinations/destinations-interface/destinations-workspace.html?lang=en#catalog).
{% endalert %}

### Step 2: Provide Braze token

In the **Account** step, provide your Braze API key and select **Connect to destination**.

![]({% image_buster /assets/img/adobe/braze-destination-account.png %}){: style="max-width:60%"}

### Step 3: Authentication

Next, in the  **Authentication** step, enter your Braze connection details:
- **Name**: Enter the name you'd like to recognize this destination by in the future.
- **Destination**: Enter a description that will help you identify this destination.
- **Endpoint instance**: Enter your Braze endpoint instance.
- **Marketing use case**: Marketing use cases indicate the intent for which data will be exported to the destination. You can select from Adobe-defined marketing use cases or create your own marketing use case. To read more about Adobe marketing use cases, visit [Data governance in Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en#destinations).

![]({% image_buster /assets/img/adobe/braze-destination-authentication.png %}){: style="max-width:60%;"}

### Step 4: Create destination
Select **Create destination**. Your destination has been created. You can select **Save & Exit** to activate segments later or **Next** to continue the workflow and select segments to activate. 

### Step 5: Activate segments
Activate the data you have in the Adobe real-time CDP by mapping segments to the Braze destination.

The following list highlights the general steps required to activate a segment. For thorough guidance on Adobe segments and the segment activation workflow, visit [Adobe](https://experienceleague.adobe.com/docs/experience-platform/destinations/ui/activate-destinations.html?lang=en#prerequisites).

1. Select and activate the Braze destination.
2. Select applicable segments.
4. Configure scheduling and file names for each segment you export.
5. Select attributes to send to Braze.
6. Review and verify activation.

### Step 6: Field mapping

To correctly send your audience data from the Adobe Experience Platform to Braze, you must complete the field mapping step. Mapping creates a link between the Adobe Experience data model fields and the corresponding Braze platform fields.

1. In the mapping step, select **Add new mapping**.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping.png %}){: style="max-width:50%;"}<br><br>
2. In the source field section, select the arrow button next to the empty field to open the select source field window.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-source.png %})<br><br>
3. In the window, select Adobe attributes to map to your Braze attributes. <br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-attributes.png %}){: style="max-width:70%;"}<br><br>Next, select the identity namespace. This option is used to map a platform identity namespace to a Braze namespace.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-namespaces.png %}){: style="max-width:80%;"}<br> Choose your source fields, then select **Select**.<br><br>
4. In the target field section, select the mapping icon beside the field.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-target.png %}){: style="max-width:90%;"} <br><br>
5. In the select target field window, you can choose between three categories of target fields:<br><br>• **Select identity namespace**: Use this option to map Platform identity namespaces to Braze identity namespaces.<br>• **Select custom attributes**: Use this option to map Adobe XDM attributes to custom Braze attributes that you defined in your Braze account. <br><br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-target-fields.png %}){: style="max-width:60%;"}<br><br>**You can also use this option to rename existing XDM attributes into Braze.** For example, mapping a `lastname` XDM attribute to a custom `Last_Name` attribute in Braze, will create the `Last_Name` attribute in Braze if it doesn't already exist, and map the `lastname` XDM attribute to it. <br><br> Choose your target fields, then select **Select**.<br><br>
6. Your field mapping should appear in the list.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-complete.png %})<br><br>
7. To add more mappings, repeat steps 1 through 6, as necessary. 

## Use case

Let's say your XDM profile schema and your Braze instance contains the following attributes and identities:

|     | XDM profile schema | Braze instance |
| --- | ------------------ | -------------- |
| Attributes | - `person.name.firstname`<br>- `person.name.lastname`<br>- `mobilePhone.number`| - `FirstName`<br>- `LastName`<br>- `PhoneNumber`|
| Identities | - `Email`<br>\- Google Ad ID (`GAID`)<br>\- Apple ID For Advertisers (`IDFA`) | - `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

The correct mapping would look like this:

![Destination mappings: IdentityMap:IDFA mapped to IdentityMap:external_id, IdentityMap:GAID mapped to IdentityMap:external_id, IdentityMap:Email mapped to IdentityMap:external_id, xdm:mobilePhone.number mapped to CustomAttribute:PhoneNumber, xdm:person.name.lastName mapped to CustomAtrribute:LastName, xdm:person.name.firstName mapped to CustomAttribute:FirstName]({% image_buster /assets/img/adobe/braze-destination-mapping-example.png %})

## Exported data
To verify if data has been exported successfully to Braze, check your Braze account. Adobe Experience Platform segments are exported to Braze under the `AdobeExperiencePlatformSegments` attribute.

## Data usage and governance
All Adobe Experience Platform destinations are compliant with data usage policies when handling your data. See [Data governance in real-time CDP](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en) for detailed information on how the Adobe Experience Platform enforces data governance. 

