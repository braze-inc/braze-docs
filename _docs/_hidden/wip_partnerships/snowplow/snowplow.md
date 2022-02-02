---
nav_title: Snowplow
article_title: Snowplow (via GTM Server-Side)
page_order: 1

description: "The Braze and Snowplow integration enables users to forward Snowplow events to Braze through Google Tag Manager Server-side."
alias: /partners/snowplow/

page_type: partner
search_tag: Partner
hidden: true

---

# Snowplow (via GTM Server-Side)

> [Snowplow][1] is a scalable open-source platform for rich, high quality, low-latency data collection. It is designed to collect high quality, complete behavioral data for enterprise business.

The Braze and Snowplow integration enables users to forward Snowplow events to Braze through Google Tag Manager Server-side. The Snowplow Braze Tag for Google Tag Manager Server-side allows sending events to Braze while offering additional flexibility and control:

* Full visibility into all transformations on the data
* Ability to evolve sophistication over time
* All data remains in your private cloud until you choose to forward it
* Ease of setup due to rich libraries of tags and familiar GTM UI

Leverage Snowplow’s rich behavioral data to drive powerful customer-centric interactions in Braze and deliver personalized messages in real-time.

## Prerequisites

The prerequisites listed below are necessary to forward Snowplow event data to Braze through GTM-SS.

| Requirement | Description |
| ----------- | ----------- |
| Snowplow pipeline | A Snowplow pipeline needs to be up and running. |
| GTM Server-side | GTM-SS needs to be deployed and the [Snowplow Client for GTM-SS][2] to be setup. |
| Braze REST API key | A Braze REST API Key with `users.track` permissions. <br><br> This can be created within the __Braze Dashboard -> Developer Console -> REST API Key -> Create New API Key__ |
| Braze REST endpoint | [Your REST endpoint URL][3]. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

Use Snowplow’s rich behavioral data to power your customer interactions in Braze.

### Personalized, action-based delivery

Send your customers the right message at the right time through the right channel - based on the actions they took in your product, app or website. Use any of the large number of rich events that Snowplow collects out-of-the-box, or define your own custom events to shape even more granular customer journeys that make sense for your business. Leverage Snowplow’s rich behavioral data to design customer funnels and unlock value for your marketing and product teams, helping them to maximize conversion and product usage through Braze.

### Dynamic Segmentation

Create dynamic audiences in Braze based on Snowplow’s high-quality behavioral data: As users take actions in your product, app or website, you can leverage the real-time behavioural data that Snowplow collects to automatically add or remove users from relevant segments in Braze.

## Integration

### Step 1: Template installation

#### Tag Manager Gallery

**Coming Soon** This tag is pending approval to be included in the GTM Gallery.

#### Manual Installation

* Download the [template file][7]`template.tpl` – Ctrl+S (Win) or Cmd+S (Mac) to save the file, or right click the link on this page and select "Save Link As..."
* Create a new Tag in the Templates section of a Google Tag Manager Server container
* Click the More Actions menu, in the top right hand corner, and select Import
* Import `template.tpl` downloaded in Step 1
* Click Save

### Step 2: Braze Tag Setup

With the template installed, you can now add the Braze Tag to your GTM SS Container.

* From the Tag tab, select “New”, then select the Braze Tag as your Tag Configuration
* Select your desired Trigger for the events you wish to forward to Braze.
* Enter the required parameters and configure your Tag (more details in the Customization section below).
* Click Save

## Customization

### Braze REST API Endpoint (required)

Set this to the URL of your Braze REST [endpoint][3].

### Braze API Key (required)

Set this to your Braze [API Key][4] that will be included in each request.

### Braze external_id (required)

Set this key to the client event property that corresponds to your users' `external_id` and will be used as the [Braze User Identifier][5].

### Snowplow Event Mapping Options

This section includes the mapping rules that concern a Snowplow event as claimed by the [Snowplow Client][2]:

#### Include Self Describing event

This option indicates if the Snowplow Self-Describing event data will be included in the event's properties object that will be sent to Braze. By default, this option is enabled.

#### Snowplow Event Context Rules

This section describes how the Braze Tag will use the context Entities attached to a Snowplow Event.

##### Extract entity from Array if single element

Snowplow Entities are always in Arrays, as multiple of the same entity can be attached to an event. This option will pick the single element from the array if the array only contains a single element.

##### Include all Entities in event object

Leaving this option enabled (default) ensures that all Entities on an event will be included within the Braze event's properties object.

Disabling this option, reveals the options so that individual entities can be selected for inclusion.

##### Snowplow Entity Mapping

Using the "Snowplow Entity Mapping" table, the entities can also be remapped to have different names in the Braze and can be included in either event's properties or user attributes object.. The entity can be specified in two different formats:

* Major version match: `x-sp-contexts_com_snowplowanalytics_snowplow_web_page_1` where `com_snowplowanalytics_snowplow` is the event vendor, `web_page` is the schema name and `1` is the Major version number. `x-sp-` can also be omitted from this if desired
* Full schema match: `iglu:com.snowplowanalytics.snowplow/webPage/jsonschema/1-0-0`

##### Include unmapped entities in event

When remapping or moving some entities to User Attributes with the above customization, this option enables you to ensure that all unmapped entities (i.e. any entites not found in the "Snowplow Entity Mapping" rules above) will be included in the properties object of the Braze event.

### Additional Event Mapping Options

If you wish to pick other properties from the Client event and map them onto the Braze event, these can be specified in this section.

#### Event Property Rules

##### Include common event properties

Enabled by default, this option sets whether to automatically include the event properties from the [Common Event definition][6] in the properties of the Braze event.

##### Additional Event Property Mapping Rules

Specify the Property Key from the Client Event, and then the properties' object key you could like to map it to or leave the mapped key blank to keep the same name. You can use Key Path notation here (e.g. `x-sp-tp2.p` for a Snowplow events platform or `x-sp-contexts.com_snowplowanalytics_snowplow_web_page_1.0.id` for a Snowplow events page view id (in array index 0) or pick non-Snowplow properties if using an alternative Client. These keys will populate the Braze event's properties object.

##### Include common user properties

Enabled by default, this option sets whether to include the `user_data` properties from the common event definition in the Braze User Attributes object.


##### Additional User Property Mapping Rules

Using this table, you can additionally specify the Property Key from the Client Event, and then the User Attribute key you could like to map it to (or leave the mapped key blank to keep the same name). You can use Key Path notation here (e.g. `x-sp-tp2.p` for a Snowplow events platform or `x-sp-contexts_com_snowplowanalytics_snowplow_web_page_1.0.id` for a Snowplow events page view id (note the array index 0) or pick non-Snowplow properties if using an alternative Client.

### Advanced Event Settings

Finally, this section offers an additional configuration option:

#### Event time property

This option enables you to specify the client event property to populate the event time (in ISO-8601 format) or leave it empty to use the current time (default behaviour).

[1]: https://snowplowanalytics.com
[2]: https://docs.snowplowanalytics.com/docs/forwarding-events-to-destinations/forwarding-events/google-tag-manager-server-side/snowplow-client-for-gtm-ss/
[3]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[4]: {{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[5]: {{site.baseurl}}/developer_guide/rest_api/basics/#external-user-id-explanation
[6]: https://developers.google.com/tag-platform/tag-manager/server-side/common-event-data
[7]: https://github.com/snowplow/snowplow-gtm-server-side-braze-tag/blob/main/template.tpl
