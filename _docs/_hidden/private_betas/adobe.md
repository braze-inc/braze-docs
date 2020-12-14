---
nav_title: Adobe
alias: /partners/adobe/
description: "The Braze and Adobe CDP integration allows brands to connect and map their Adobe data (custom attributes and segments) to Braze in real-time. Brands can then act on this data, delivering personalized targeted experiences to those users."
page_type: partner
---

{% alert note %}
The Adobe and Braze integration is currently in beta. Please contact your Braze account manager if you are interested in participating in the beta.
{% endalert %}

# Adobe
 
> Built on the Adobe Experience Platform, Adobe's Real-time Customer Data Platform (Real-time CDP) helps companies bring together known and anonymous data from multiple enterprise sources in order to create customer profiles that can be used to provide personalized customer experiences across all channels and devices in real-time.

The Braze and Adobe CDP integration allows brands to connect and map their Adobe data (custom attributes and segments) to Braze in real-time. Brands can then act on this data, delivering personalized targeted experiences to those users. With Adobe, the integration is intuitive. Simply take any Adobe [identity](https://experienceleague.adobe.com/docs/experience-platform/identity/namespaces.html?lang=en), map it to a Braze external ID, and send it off to the Braze platform. All data sent will be accessible in Braze through a new `AdobeExperiencePlatformSegments` attribute. 

## Pre-Requisites

| Requirement | Description |
| ----------- | ----------- |
| Adobe Account | You must have an active Adobe account to utilize their services with Braze |
| Braze REST API Key | A Braze REST API Key with `users.track` permissions. <br><br> This can be created within the __Braze Dashboard -> Developer Console -> REST API Key -> Create New API Key__ |
| Braze REST Endpoint | Your REST Endpoint URL. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Please note that the sending of additional custom attributes may cause data points concerns. We advise speaking with your respective rep for a better understanding of this potential data point increase.
{% endalert %}

## Integration Overview

### Step 1: Connect Adobe Account to Braze Destination

From the Adobe settings page, select __Destinations__ under __Collections__. From there, locate the Braze tile and select __Configure__. 

![Connect][1]

{% alert note %}
If a connection with Braze already exists, you will see an Activate button on the destination card. For more information about the difference between Activate and Configure, refer to the Catalog section of the Adobe destination workspace [documentation](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/destinations/destinations-interface/destinations-workspace.html?lang=en#catalog).
{% endalert %}

### Step 2: Provide Braze Token
![Token][3]{: style="float:right;max-width:40%;margin-left:15px;"}
In the account step, provide your Braze account token API key. For more information on how to obtain your API key in the Braze [REST API Key Overview](https://www.braze.com/docs/api/api_key/). Enter this key and click __Connect to destination__.

### Step 3: Authentication

Next, you will be presented with the Authentication step. Here, you must enter your Braze connection details:
- __Name__: Enter the name you would like to recognize this destination by in the future.
- __Destination__: Enter a description that will help you identify this destination.
- __Endpoint Instance__: Please reach out to your Braze representative about which endpoint instance you should use. 
- __Marketing Use Case__: Marketing use cases indicate the intent for which data will be exported to the destination. You can select from Adobe-defined marketing use cases or you can create your own marketing use case. To read more about Adobe marketing use cases, visit their [Data Governance in Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en#destinations) documentation.

![Authentication][4]{: style="max-width:60%;"}

### Step 4: Create Destination
Lastly, click __Create destination__. Your destination has now been created. You can click __Save & Exit__ if you want to activate segments later, or you can select __Next__ to continue the workflow and select segments to Activate. 

### Step 5: Activate Segments
Activate the data you have in the Adobe Real-Time CDP by mapping segments to the Braze destination.

Listed below are the general steps required to activate a segment. For thorough guidance on Adobe segments and the segment activation workflow, visit their [Segment Documentation](https://experienceleague.adobe.com/docs/experience-platform/destinations/ui/activate-destinations.html?lang=en#prerequisites).

1. Select and activate the Braze destination.
2. Select applicable segments.
4. Configure scheduling and file names for each segment you export.
5. Select attributes to send to Braze.
6. Review and verify activation.

### Step 6: Field Mapping

To correctly send your audience data from Adobe Experience Platform to Braze, you must complete the field mapping step. Mapping consists of creating a link between the Adobe Experience Data Model fields and the corresponding Braze Platform fields.

1. In the Mapping Step, click __Add new mapping__.<br>![Mapping][5]{: style="max-width:50%;"}<br><br>
2. In the Source Field Section, click the arrow button next to the empty field, this will open the Select source field window.<br>![Source][6]<br><br>
3. From the Select source field window, you must select Adobe attributes to map to your Braze attributes. <br>![Field][7]{: style="max-width:70%;"}<br><br>Next, you must select the identity namespace. This option is used to map a Platform identity namespace to a Braze namespace.<br>![Identity][8]{: style="max-width:80%;"}<br> Choose your source fields, then click __Select__.<br><br>
4. In the Target Field section, click the mapping icon to the right of the field.<br>![Tagret][9]{: style="max-width:90%;"} <br><br>
5. In the Select target field window, you can choose between three categories of target fields:<br><br>• __Select attributes__: Use this option to map your Adobe XDM attributes to standard Braze attributes.<br>• __Select identity namespace__: Use this option to map Platform identity namespaces to Braze identity namespaces.<br>• __Select custom attributes__: Use this option to map Adobe XDM attributes to custom Braze attributes that you defined in your Braze account. <br><br>![Attributes][10]{: style="max-width:60%;"}<br><br>__You can also use this option to rename existing XDM attributes into Braze.__ For example, mapping a `lastname` XDM attribute to a custom `Last_Name` attribute in Braze, will create the `Last_Name` attribute in Braze if it doesn't already exist, and map the `lastname` XDM attribute to it. <br><br> Choose your target fields, the click __Select__.<br><br>
6. You should now see your field mapping in the list.<br>![List][11]<br><br>
7. To add more mappings, repeat steps 1 through 6 as necessary. 

## Example

Let's say your XDM profile schema and your Braze instance contains the following attributes and identities:

|     | XDM Profile Schema | Braze Instance |
| --- | ------------------ | -------------- |
| Attributes | - `person.name.firstname`<br>- `person.name.lastname`<br>- `mobilePhone.number`| - `FirstName`<br>- `LastName`<br>- `PhoneNumber`|
| Identities | - `Email`<br>- `Google Ad ID (GAID)`<br>- `Apple ID For Advertisers (IDFA)` | - `external_id` |

The correct mapping would look like this:

![Correct][12]

## Exported Data
To verify if data has been exported successfully to Braze, check your Braze account. Adobe Experience Platform segments are exported to Braze under the `AdobeExperiencePlatformSegments` attribute.

## Data Usage and Governance
All Adobe Experience Platform destinations are compliant with data usage policies when handling your data. For detailed information on how the Adobe Experience Platform enforces data governance, see Adobe's [Data Governance in Real-Time CDP](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en) documentation. 

[1]: {% image_buster /assets/img/adobe/braze-destination-configure.png %} 
[2]: {% image_buster /assets/img/adobe/braze-destination-activate.png %} 
[3]: {% image_buster /assets/img/adobe/braze-destination-account.png %}
[4]: {% image_buster /assets/img/adobe/braze-destination-authentication.png %}
[5]: {% image_buster /assets/img/adobe/braze-destination-mapping.png %} 
[6]: {% image_buster /assets/img/adobe/braze-destination-mapping-source.png %} 
[7]: {% image_buster /assets/img/adobe/braze-destination-mapping-attributes.png %} 
[8]: {% image_buster /assets/img/adobe/braze-destination-mapping-namespaces.png %} 
[9]: {% image_buster /assets/img/adobe/braze-destination-mapping-target.png %} 
[10]: {% image_buster /assets/img/adobe/braze-destination-mapping-target-fields.png %} 
[11]: {% image_buster /assets/img/adobe/braze-destination-mapping-complete.png %} 
[12]: {% image_buster /assets/img/adobe/braze-destination-mapping-example.png %} 
