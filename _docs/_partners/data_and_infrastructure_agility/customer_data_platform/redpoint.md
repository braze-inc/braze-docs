---
nav_title: Redpoint
article_title: Redpoint 
page_order: 7.1
description: "The Redpoint to Braze integration allows you to onboard and enrich Braze user profiles with your first-party data."
alias: /partners/redpoint/
page_type: partner
search_tag: Partner
layout: dev_guide
---

# Redpoint

> This integration allows you to onboard and enrich Braze user profiles with your first-party data from the [Redpoint][2] CDP.

Using the Redpoint to Braze integration, you can create Braze segments based on your Redpoint CDP data. Leverage Redpoint's advanced segmentation, scheduling, and automation capabilities to control how and when CDP data is imported to Braze. 

Redpoint provides two modes for passing data to Braze: 

1. The **Braze Onboarding and Upsert** mode upserts a user profile from Redpoint into Braze. This is intended to be used for onboarding or updating user records when data has changed. 
2. The **Braze Append** mode will update a user profile if that user already exists in Braze. 

You will configure both an export template and outbound channel for each mode.

{% alert note %}
"Upsert" is a combination of the words "update" and "insert." It is used when you want to insert a new record into a database table if it doesn't already exist or update the record if it does exist. In essence, "upsert" checks whether a particular record is present in the database, and if it is, it updates it; if it's not, it inserts it as a new record.
{% endalert %}

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br>This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance. |
| Redpoint Data Management artifacts | The Braze integration is supported by a set of Redpoint Data Management artifacts. Contact [Redpoint Support][3] to request the artifacts for your version of Redpoint Data Management. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can create an API key at **Developer Console** > **API Settings**.
{% endalert %}

## Redpoint CDP custom attributes

The following custom attributes can be added to a Braze user profile from Redpoint:

| Field               | Description                                                                                                       |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `rpi_cdp_attributes` | Redpoint CDP profile attributes                                                                                  |
| `rpi_audience_outputs`| Array of audience output tags where the user is targeted in a Redpoint Outbound Delivery Braze channel execution         |
| `rpi_offers`         | Array of offer tags where the user is targeted in a Redpoint Outbound Delivery Braze channel execution                   |
| `rpi_contact_ids`    | Array of offer history contact IDs where the user is targeted in a Redpoint Outbound Delivery Braze channel execution     |
| `rpi_channel_exec_ids`| Array of channel execution IDs where the user is targeted in a Redpoint Outbound Delivery Braze channel execution       |
{: .reset-td-br-1 .reset-td-br-2}

![][4]{: style="max-width:75%;"}

## Integration

You will create your outbound channels and templates in Redpoint Interaction (RPI). 

### Create the Braze Onboarding and Upsert template

In RPI, create a new export template and name it **Braze Onboarding and Upsert**. This template defines the core mappings between the Redpoint CDP and the Braze user profile, along with any additional custom attributes you want to add to your user profiles in Braze. 

Drag Redpoint CDP attributes into the **Attribute** column. Set the **Header Row Value** to the corresponding to the following Braze user properties. 

Here is a list of Redpoint CDP attributes and their corresponding Braze attributes:

| Redpoint Attribute | Header Row Value |
|--------------------|------------------|
| PID                | `external_id`    |
| Fist Name          | `first_name`     |
| Last Name          | `last_name`      |
| Primary Email      | `email`          |
| Primary Country    | `country`        |
| DOB                | `dob`            |
| Gender             | `gender`         |
| Primary City       | `home_city`      |
| Primary Phone      | `phone`          |
{: .reset-td-br-1 .reset-td-br-2}

Add the **Output Name** attribute from the Offer History table.

Lastly, add any additional custom Redpoint attributes you want to merge into Braze. 

For example, here is sample export template configured for merge operations, with the additional attributes Education, Income, and Marital Status:

![][7]{: style="max-width:75%;"}

#### Create the Braze Append template

Create a second export template for append-only operations named **Braze Append**. 

You will set only two attributes for this template. Set **PID** to the **Header Row** of `external_id`. Set **Output Name** to the **Header Row** of `output_name`. 

![A sample export template with the `external_id` and output name attributes.][8]{: style="max-width:75%;"}

#### Set date format

On both export templates, navigate to the **Options** tab and set the **Date Format** to the value of **Custom Format**. Declare the format as **yyyy-MM-dd**.

![The options tab showing date format set to yyyy-MM-dd.][16]{: style="max-width:75%;"}

### Create outbound channels

In RPI, create two new channels. Set both channels to **Outbound Delivery**. Name one channel **Braze Onboarding and Upsert** and the other **Braze Append**.

![][9]{: style="max-width:75%;"}

{% alert note %}
After the initial onboarding of your CDP records to Braze, please ensure that subsequent Redpoint Interaction workflows which use the Braze Onboarding and Upsert channel are designed to select only records that have changed since the initial onboarding sync.
{% endalert %}

### Configure the channels

#### Set template and export path format

Navigate to the **General** tab in the Channels **Configuration** screen. 

Set the appropriate export template to each respective channel. 

Then, define an **Export path format** on both channels that point to a shared network, ftp, or external content provider location which is accessible to both Redpoint Interaction and Redpoint Data Management. 

![][10]{: style="max-width:75%;"}

The export directory format on both channels will be identical and should end with \\[Channel]\\[Offer]\\[Workflow ID].

![][11]{: style="max-width:50%;"}

#### Configure post execution

Navigate to the **Post Execution** tab in the Channels **Configuration** screen. 

Check the **Post-execution** checkbox to call a service URL after channel execution. Enter your Redpoint Data Management web service URL. This entry will be identical on both your Onboarding and Append channel.   

![][14]{: style="max-width:75%;"}

### Set up supporting Braze components in Redpoint Data Management 

The archive containing Redpoint Data Management (RPDM) artifacts to support the Braze integration contains a README with detailed instructions for setting up the required components. The following are the areas which are most important for setting environment specific configuration between Braze, RPI, and RPDM:

#### Update the RPI to Braze automation with your Braze REST endpoint and base RPI output directory 

After importing the Braze related artifacts into Redpoint Data Management, open the automation named **AUTO_Process_RPI_to_Braze** and update the following 2 Automation settings with the values for your environment:

* **BRAZE_API_URL** - The Braze REST endpoint
* **BASE_OUTPUT_DIRECTORY** - The shared output directory between Redpoint Interaction and Redpoint Data Management

![][5]{: style="max-width:40%;"}


#### Update the RPI to Braze append project 

The Redpoint Data Management project named **PROJ_RPI_to_Braze_Append** contains the outbound delivery export file schema and mappings for the `rpi_cdp_attributes` custom attribute object in Braze. Update the file input schema and document injector tool named **RPI to Braze Document Injector** with any additional custom CDP attributes defined on the export file template. This examples shows the additional mapping of education, income, and marital status:

![][6]{: style="max-width:40%;"}

## Using the Redpoint to Braze integration

The Outbound Delivery Braze channel can now be leveraged within Redpoint Interaction workflows. Follow the standard practices for creating selection rules and audiences in RPI, and building associated workflow schedules and triggers. To enable the sync of an RPI Audience output to Braze, create an outbound delivery offer and associate it to either the **Braze Onboarding and Upsert** or the **Braze Append** channel depending on whether the intent is to create or merge new records in Braze or to only append campaign data if the record already exists in Braze.

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

