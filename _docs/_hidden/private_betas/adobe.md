---
nav_title: Adobe
alias: /partners/adobe/
description: ""
page_type: partner
---

# Adobe

> Built on the Adobe Experience Platform, Real-time Customer Data Platform (Real-time CDP) helps companies bring together known and anonymous data from multiple enterprise sources in order to create customer profiles that can be used to provide personalized customer experiences across all channels and devices in real time.

Real-time CDP includes tools for data governance, identity management, advanced segmentation, and data science so that you can build profiles and define audiences, as well as derive rich insights while being able to enforce strict data governance policies.

Our Adobe integration allows brands to connect and map their Adobe data to Braze. 

## Pre-Requisites

| Requirement | Description |
| ----------- | ----------- |
| Adobe Account | You must have an active Adobe account to utilize their services with Braze |
| Braze REST API Key | A Braze REST API Key with `users.track` permissions. <br><br> This can be created within the __Braze Dashboard -> Developer Console -> REST API Key -> Create New API Key__ |
| Braze REST Endpoint | Your REST Endpoint URL. Your endpoint will depend on the Braze URL for your instance. |

{% alert important %}
Please note that sending of additional custom attributes may cause data points concerns. We advise speaking with your respective rep for a better understanding of this potential data point increase.
{% endalert %}


## Integration Overview

### Step 1: Connect Adobe Account to Braze Destination

From the Adobe settings page, select Destinations found under Collections. From there, locate the Braze tile and select Configure. 

![Connect][1]

{% alert note %}
If a connection with Braze already exists, you will see an Activate button on the destination card. For more information about the difference between Activate and Configure, refer to the Catalog section of the Adobe destination workspace [documentation](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/destinations/destinations-interface/destinations-workspace.html?lang=en#catalog).
{% endalert %}

### Step 2: Provide Braze Token
![Token][3]{: style="float:right;max-width:40%;margin-left:15px;"}
In the account step, provide your Braze account token API key. For more information on how to obtain your API key in the Braze [REST API Key Overview](https://www.braze.com/docs/api/api_key/). Enter this key and click Connect to destination.

### Step 3: Authentication

Upon clicking Next, you will be presented with the Authentication step. Here, you must enter your Braze connection details:
- __Name__: Enter the name you would like to recognize this destination by in the future.
- __Destination__: Enter a description that will help you identify this destination.
- __Endpoint Instance__: Please reach out to your Braze representative about which endpoint instance you should use. 
- __Marketing Use Case__: Marketing use cases indicate the intent for which data will be exported to the destination. You can select from Adobe-defined marketing use cases or you can create your own marketing use case. To read more about Adobe marketing use cases, visit their [Data Governance in Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en#destinations) documentation.

![Authentication][4]{: style="max-width:60%;"}

### Step 4: Create Destination
Lastly, click Create destination. Your destination is now created. You can click Save & Exit if you want to activate segments later, or you can select Next to continue the workflow and select segments to Activate. 

### Step 5: Activate Segments

To read more about Adobe's Segment activation workflow, visit their [Segment Documentation]().

### Step 6: Field Mapping

To correctly send your audience data from Adobe Experience Platform to Braze, you must complete the field mapping step. Mapping consists of creating a link between the Adobe Experience Data Model fields and the corresponding Braze Platform fields.

1. In the Mapping Step, click __Add new mapping__.<br>![Mapping][5]{: style="max-width:50%;"}<br><br>
2. In the Source Field Section, click the arrow button next to the empty field, this will open the Select source field window.<br>![Source][6]<br><br>
3. From the Select source field window, you must select attributes to map to your Braze attributes. <br>![Field][7]{: style="max-width:70%;"}<br><br>Next, you must select the identity namespace. This option is used to map a Platform identity namespace to a Braze namespace.<br>![Identity][8]{: style="max-width:80%;"}<br> Choose your source fields, then click __Select__.<br><br>
4. In the Target Field section, click the mapping icon to the right of the field.<br>![Tagret][9]{: style="max-width:90%;"} <br><br>
5. In the Select target field window, you can choose between three categories of target fields:<br>- __Select Attributes__: Use this option to map your Adobe XDM attributes to standard Braze attributes.<br>- __Select identity namespace__: Use this option to map Platform identity namespaces to Braze identity namespaces.<br>- __Select custom attributes__: Use this option to map Adobe XDM attributes to custom Braze attributes that you defined in your Braze account. <br><br>![Attributes][10]{: style="max-width:60%;"}<br><br> You can also use this option to rename existing XDM attributes into Braze. For example, mapping a `lastname` XDM attribute to a custom `Last_Name` attribute in Braze, will create the `Last_Name` attribute in Braze if it doesn't already exist, and map the `lastname` XDM attribute to it.<br><br> Choose your target fields, the click __Select__.<br><br>
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
Al Adobe Experience Platform destinations are compliant with data usage policies when handling your data. For detailed information on how the Adobe Experience Platform enforces data governance, see Adobe's [Data Governance in Real-Time CDP](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en) documentation. 

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