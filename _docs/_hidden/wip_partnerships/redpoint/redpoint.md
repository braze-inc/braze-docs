---
nav_title: Redpoint
article_title: Redpoint Partner Page
page_order: 1

description: "This is the Google Search and SEO description that will appear; try to make this informative and concise, yet brief."
alias: /partners/redpoint/

page_type: partner
search_tag: Partner
hidden: true
layout: dev_guide
---

# Redpoint

> The [Redpoint][2] technology platform drives personalized omnichannel AND real-time experiences at scale

The Redpoint to Braze integration allows you to onboard and enrich Braze user profiles with your first-party Redpoint CDP and orchestration data. Redpoint's CDP golden record attributes can be exposed selectively in Braze user records. The integration supports an onboarding mode which upserts user records in Braze and also an append mode which will only update a user if the record exists already in Braze. 

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Braze REST API key | A Braze REST API key with `users.track` permissions.  <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance. |
| Redpoint Data Management Braze artifacts | The Braze integration is supported by a set of Redpoint Data Management artifacts. Contact [Redpoint Support][3] to request the artifacts for your version of Redpoint Data Management |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can create an API key at **Developer Console** > **API Settings**.
{% endalert %}

## Use cases

Create Braze segments based on your first-party Redpoint CDP and orchestration data. Leverage Redpoint's advanced segmentation, scheduling and automation capabilities to control how and when CDP data is imported to Braze. 

The following custom attributes can be created on the Braze user record:

* **rpi_cdp_attributes** - Redpoint CDP profile attributes
* **rpi_audience_outputs** - audience output tags where the user is targeted in a Redpoint Outbound Delivery Braze channel execution
* **rpi_offers** - offer tags where the user is targeted in a Redpoint Outbound Delivery Braze channel execution
* **rpi_contact_ids** - offer history contact IDs where the user is targeted in a Redpoint Outbound Delivery Braze channel execution
* **rpi_channel_exec_ids** - channel execution IDs where the user is targeted in a Redpoint Outbound Delivery Braze channel execution

![][4]{: style="max-width:75%;"}

{% alert note %}
Redpoint provides two export templates and channels for passing data to Braze. The **Braze Onboarding and Upsert** channel and export template are intended to be used for onboarding or updating user records when data has changed. After the intial onboarding of CDP records to Braze, please ensure that subsequent Redpoint Interaction workflows which use this channel are designed to select only records that have changed since the initial onboarding sync.
{% endalert %}

## Integration

### Setup Outbound Delivery Braze channels in Redpoint Interaction (RPI)

#### RPI setup step 1: create export templates for upsert and append-only operations

Create a new export template and name it **Braze Onboarding and Upsert**. This template defines the core mappings between the Redpoint CDP and the Braze user record, along with any additional custom RPI attributes you want to expose on the Braze record. Drag Redpoint CDP attributes into the **Attribute** column corresponding to the following Braze user properties and be sure to label them accordingly in the **Header Row Value** column:

* external_Id
* first_name
* last_name
* email
* country
* dob
* gender
* home_city
* phone

In addition, add the **Output Name** attribute from the Offer History table and any additional custom Redpoint attributes you want to add to the Braze record. The image below shows a sample export template configured for upsert operations, with the additional attributes Education, Income, and Marital Status:

![][7]{: style="max-width:75%;"}

Create a second export template for append-only operations named **Braze Append**. This template should only include the attributes for **external_id** and Offer History **Output Name**:

![][8]{: style="max-width:75%;"}

On both export templates, navigate to the **Options** tab and set the **Date Format** to the value of **Custom Format** and then declare the format as **yyyy-MM-dd** as shown below.

![][16]{: style="max-width:75%;"}

#### RPI setup step 2: create Outbound Delivery channels for upsert and append-only operations

Create two new RPI channels of type **Outbound Delivery** and name them **Braze Append** and **Braze Onboarding and Upsert**:

![][9]{: style="max-width:75%;"}

From the **Channel Specific** tab in the channel configuration screen:

* Associate the export templates create above to their respective channel
* Define an **Export path format** on both channels that point to a shared network, ftp or external content provider location which is accessible to both Redpoint Interaction and Redpoint Data Management. The export directory format on both channels will be identical and should end with \\[Channel]\\[Offer]\\[Workflow ID]

![][10]{: style="max-width:75%;"}

![][11]{: style="max-width:50%;"}

From the **Post Execution** tab in the channel configuration screen:

Check the option to call a service URL and enter the Redpoint Data Management web service url. This entry will be identical on both the Onboarding and Append channel.   

![][14]{: style="max-width:75%;"}

### Setup supporting Braze components in Redpoint Data Management (RPDM)

The archive containing RPDM artifacts to support the Braze integration contains a README with detailed instructions for setting up the required components. The following are the areas which are most important for setting environment specific configuration between Braze, RPI and RPDM:

#### Update the RPI to Braze automation with your Braze REST endpoint and base RPI output directory 

After importing the Braze related artifacts into Redpoint Data Management, open the automation named **AUTO_Process_RPI_to_Braze** and update the following 2 Automation settings with the values for your environment:

* **BRAZE_API_URL** - The Braze REST endpoint
* **BASE_OUTPUT_DIRECTORY** - The shared output directory between Redpoint Interaction and Redpoint Data Management

![][5]{: style="max-width:40%;"}


#### Update the RPI to Braze append project 

The Redpoint Data Management project named **PROJ_RPI_to_Braze_Append** contains the outbound delivery export file schema and mappings for the rpi_cdp_attributes custom attribute object in Braze. Update the file input schema and document injector tool named **RPI to Braze Document Injector** with any additional custom CDP attributes defined on the export file template. This examples shows the additional mapping of education, income, and marital status:

![][6]{: style="max-width:40%;"}

## Using the Redpoint to Braze integration

The Outbound Delivery Braze channel can now be leveraged within Redpoint Interaction workflows. Follow the standard practices for creating selection rules and audiences in RPI, and building associated workflow schedules and triggers. To enable the sync of an RPI Audience output to Braze, create an outbound delivery offer and associate it to either the **Braze Onboarding and Upsert** or the **Braze Append** channel depending on whether the intent is to create or upsert new records in Braze or to only append campaign data if the record already exists in Braze.

![][13]{: style="max-width:75%;"}

Once the workflow has executed successfully in RPI, the orchestration and CDP data sourced from RPI can now be used to create segments in Braze:

![][12]{: style="max-width:75%;"}

You can view the Redpoint associated properties on the user record:

![][15]{: style="max-width:75%;"}

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://www.redpointglobal.com
[3]: https://support.redpointglobal.com/hc/en-us/restricted?return_to=https%3A%2F%2Fsupport.redpointglobal.com%2Fhc%2Fen-us
[4]: {% image_buster /assets/img/redpoint/rpi_to_braze_custom_attributes.png %}
[5]: {% image_buster /assets/img/redpoint/rpi_to_braze_auto_variables.png %}
[6]: {% image_buster /assets/img/redpoint/rpi_to_braze_doc_injector_mappings.png %}
[7]: {% image_buster /assets/img/redpoint/rpi_to_braze_upsert_export_format.png %}
[8]: {% image_buster /assets/img/redpoint/rpi_to_braze_append_export_format.png %}
[9]: {% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_general.png %}
[10]: {% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_specific.png %}
[11]: {% image_buster /assets/img/redpoint/rpi_to_braze_export_directory_setup.png %}
[12]: {% image_buster /assets/img/redpoint/rpi_to_braze_build_braze_segment.png %}
[13]: {% image_buster /assets/img/redpoint/rpi_to_braze_rpi_canvas.png %}
[14]: {% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_post_execution.png %}
[15]: {% image_buster /assets/img/redpoint/rpi_to_braze_record_example.png %}
[16]: {% image_buster /assets/img/redpoint/rpi_to_braze_export_format_config.png %}

