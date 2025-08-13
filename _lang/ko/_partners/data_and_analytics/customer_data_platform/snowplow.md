---
nav_title: Snowplow
article_title: Snowplow
description: "This reference article outlines the partnership between Braze and Snowplow, an open-source data collection platform, that allow you to forward Snowplow events to Braze through Google Tag Manager server-side tagging."
alias: /partners/snowplow/
page_type: partner
search_tag: Partner

---

# Snowplow

> [Snowplow](https://snowplowanalytics.com) is a scalable open-source platform for rich, high-quality, low-latency data collection. It is designed to collect high-quality, complete behavioral data for enterprise businesses.

_This integration is maintained by Snowplow._

## About the integration

The Braze and Snowplow integration enables users to forward Snowplow events to Braze through Google Tag Manager server-side tagging. The Snowplow Braze tag allows you to send events to Braze while offering additional flexibility and control:
- Full visibility into all transformations on the data
- Ability to evolve sophistication over time
- All data remains in your private cloud until you choose to forward it
- Ease of setup due to rich libraries of tags and familiar Google Tag Manager UI

Leverage Snowplow's rich behavioral data to drive powerful customer-centric interactions in Braze and deliver personalized messages in real-time.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Snowplow pipeline | A Snowplow pipeline needs to be up and running. |
| Google Tag Manager server-side | GTM-SS needs to be deployed and the [Snowplow client for GTM-SS](https://docs.snowplowanalytics.com/docs/forwarding-events-to-destinations/forwarding-events/google-tag-manager-server-side/snowplow-client-for-gtm-ss/) set up. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use cases

### Personalized, action-based delivery
Use any of the large number of rich events that Snowplow collects by default, or define your custom events to shape even more granular customer journeys that make sense for your business. Leverage Snowplow's rich behavioral data to design customer funnels and unlock value for your marketing and product teams, helping them to maximize conversion and product usage through Braze.

### Dynamic segmentation
Create dynamic audiences in Braze based on Snowplow's high-quality behavioral data: As users take actions in your product, app, or website, you can leverage the real-time behavioral data that Snowplow collects to automatically add or remove users from relevant segments in Braze.

## Integration

### Step 1: Template installation

#### Manual installation

1. Download the [`template.tpl`](https://github.com/snowplow/snowplow-gtm-server-side-braze-tag/blob/main/template.tpl) template file.
2. Create a new tag in the **Templates** section of a Google Tag Manager server container.
3. Click the **More Actions** menu in the top right-hand corner, and select **Import**.
4. Import your downloaded template file and save it.

#### Tag Manager gallery

Coming soon! This tag is pending approval to be included in the GTM gallery.

### Step 2: Braze tag setup

With the template installed, add the Braze tag to your GTM-SS container.

1. From the **Tag** tab, select **New**, then select the **Braze Tag** as your tag configuration.
2. Select your desired trigger for the events you wish to forward to Braze.
3. Enter the required parameters and configure your tag (more details can be found in the following Customization section).
4. Click **Save**.

## Customization

### Required tag parameters

The following table lists the required tag parameters you must include in your Braze tag setup.

| Parameter | Description |
| --------- | ----------- |
| Braze REST API endpoint | Set this to the URL of your Braze REST [endpoint]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
| Braze API key | Set this to your Braze [API key]({{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys) that will be included in each request. |
| Braze `external_id` | Set this key to the client event property that corresponds to your users' `external_id` and will be used as the [Braze user identifier]({{site.baseurl}}/developer_guide/rest_api/basics/#external-user-id-explanation). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Event mapping

The following table lists event mapping options concerning the Snowplow event as claimed by the [Snowplow client](https://docs.snowplowanalytics.com/docs/forwarding-events-to-destinations/forwarding-events/google-tag-manager-server-side/snowplow-client-for-gtm-ss/).

| Mapping option | Description |
| --------- | ----------- |
| Include self describing event | Turned on by default. Indicates if the Snowplow self-describing event data will be included in the event's properties objects sent to Braze. |
| Snowplow event context rules | Describes how the Braze tag will use the context entities attached to a Snowplow event. |
| Extract entity from array if single element | Snowplow entities are always in arrays, as multiple of the same entity can be attached to an event. This option will pick the single element from the array if the array only contains a single element. |
| Include all entities in the event object | Turned on by default. Includes all entities on an event within the Braze event's properties object. Disable this option to select individual entities for inclusion. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Advanced event mapping

#### Event property rules

If you want to include other properties from the client event and map them onto the Braze event, reference the rules in the following table: 

| Event property rules | Description |
| --------- | ----------- |
| Include common event properties | Enabled by default, this option sets whether to automatically include the event properties from the [common event definition](https://developers.google.com/tag-platform/tag-manager/server-side/common-event-data) in the properties of the Braze event. |
| Additional user property and event property mapping rules | Specify the property key from the client event and the properties' object key you would like to map it to (or leave the mapped key blank to keep the same name). You can use key path notation here (for example, `x-sp-tp2.p` for a Snowplow events platform or `x-sp-contexts.com_snowplowanalytics_snowplow_web_page_1.0.id` for a Snowplow events page view id (in array index 0) or pick non-Snowplow properties if using an alternative client.<br><br>Event property mapping rules populate the Braze event properties object.|
| Include common user properties| Enabled by default, this option sets whether to include the `user_data` properties from the common event definition in the Braze user attributes object.|
| Event time property | This option lets you specify the client event property to populate the event time (in ISO-8601 format) or leave it empty to use the current time (default behavior). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Entity mapping

Using the Snowplow entity mapping table, the entities can be remapped to have different names in Braze and included in event properties, or user attributes objects. 

The entity can be specified in two different formats:
- Major version match: `x-sp-contexts_com_snowplowanalytics_snowplow_web_page_1` where `com_snowplowanalytics_snowplow` is the event vendor, `web_page` is the schema name and `1` is the major version number. `x-sp-` can also be omitted from this if desired.
- Full schema match: `iglu:com.snowplowanalytics.snowplow/webPage/jsonschema/1-0-0`
<br><br>

| Entity mapping option | Description |
| --------- | ----------- |
| Include unmapped entities in event | When remapping or moving some entities to user attributes with the preceding customization, this option enables you to ensure that all unmapped entities (such as any entities not found in the [event property rules](#event-property-rules)) will be included in the properties object of the Braze event. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


