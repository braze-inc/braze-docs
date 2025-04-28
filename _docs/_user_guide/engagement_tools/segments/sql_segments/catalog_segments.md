---
nav_title: "Catalog Segments"
article_title: Catalog Segments
page_order: 1
page_type: reference
alias: "/catalog_segments/"
description: "This article describes how to create catalog segments, which use catalog data in SQL Segment Extensions to build audiences of users."
tool: Segments
---

# Catalog segments

> Catalog segments are a type of SQL Segment Extension that is created by combining catalog data with data from custom events or purchases. They can be referenced in a segment and then targeted by campaigns and Canvases. 

{% alert important %}
Catalog segments are currently in early access. Contact your customer success manager if you're interested in participating in this early access.
{% endalert %}

Catalog segments use SQL to join data from catalogs and data from custom events or purchases. To do so, you must have a common identifier field across your catalogs and your custom events or purchases. For example, the value of an item ID in a catalog must match the value of a property in a custom event.

## Creating a catalog segment

1. Go to **Segment Extensions** > **Create New Extension** > **Start With Template** and select a template. <br>![Modal with the option to create a catalog segment for events or purchases.][1]{: style="max-width:80%" }

{: start="2"}
2. The SQL editor automatically populates with a template. <br>![SQL editor with a pregenerated template.][2]{: style="max-width:80%" }<br>This template joins user event data with catalog data to segment users who engaged with certain catalog items.

3. Use the **Variables** tab to provide the necessary fields for your template before generating your segment. <br>For Braze to identify users based on their engagement with catalog items, you need to do the following: <br> - Select a catalog that contains a catalog field <br> - Select a custom event that contains an event property <br> - Match your catalog field and event property values

Here are guidelines to select the variables:

| Variable field | Description |
| --- | --- |
| `Catalog` | The name of the catalog you’re using to target users. |
| `Catalog field`| The field in your catalog that contains the same values as your `Custom event property`. This is often a type of ID. In the eCommerce use case, this would be `shopify_id`. |
| `Custom event` | The name of your custom event, which is the same event that contains a property with values matching your `Catalog field`. In the eCommerce use case, this would be `Made Order`. |
| `Custom event property` | The name of your custom event property, which matches values with your `Catalog field`. In the eCommerce example use case, this would be `Shopify_ID.`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="4"}
4. If needed, fill in additional optional fields for your use case to segment by a particular field value within your catalog:
- `Catalog field`: A particular field (column name) within this catalog
- `Value`: A specific value within that field or column <br><br> Using the health app as an example, let’s say that within the catalog for each doctor you could book, there’s a field called `specialty` that contains a value such as `vision` or `dental`. To segment users who have visited any doctors with the value `dental`, you can select `specialty` as the `Catalog field`, and select `dental` as the `Value`.

5. After creating a SQL Segment, we recommend clicking **Run Preview** to see if your query returns users or if there are errors. For more information about [previewing query results]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#previewing-results), managing [SQL Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#managing-sql-segment-extensions), and more, check out [SQL Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). 

## Use cases

### Health app

Let's say you have a health app and want to segment users who have booked a visit for the dentist. You also have the following:

- A catalog `Doctors` that contains the different doctors a patient can book, each assigned with a `doctor ID`
- A custom event `Booked Visit` with a `doctor ID` property that shares the same values as the `doctor ID` field in your catalog
- A `speciality` field within your catalog that contains the `dental` value

You would set up a catalog segment by using the following variables:

| Variable | Property |
| --- | --- |
| `Catalog`| Doctors |
| `Catalog field` | doctor ID |
| `Custom event`| Booked Visit|
| `Custom event property` | doctor ID |
| `(Under Filter SQL Results) Catalog field` | Specialty |
| `(Under Filter SQL Results) Value`| Dental |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### SaaS platform

Let’s say you have B2B SaaS platform and want to segment users who are employees of an existing customer. You also have the following:

- A catalog `Accounts` that contains the different accounts that are currently using your SaaS platform, each assigned with an `account ID`
- A custom event `Event Attendance` with an "account ID" property that shares the same values as the "account ID" field in your catalog
- A `Classification` field within your catalog that contains the `enterprise` value

You would set up a catalog segment by using the following variables:

| Variable | Property |
| --- | --- |
| `Catalog` | Accounts |
| `Catalog field `| account ID |
| `Custom event` | Event Attendance |
| `Custom event property` | account ID |
| `(Under Filter SQL Results) Catalog field` | Classification |
| `(Under Filter SQL Results) Value` | Enterprise |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Frequently asked questions

### Does running a catalog segment consume SQL Segment Extension credits?

Yes, catalog segments are powered by SQL and consume SQL Segment Extension credits. To learn more, check out [SQL Segments usage]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments#monitoring-your-sql-segments-usage).

### Does creating a catalog segment consume SQL Segment Extension allotments?

Yes. In the same way SQL Segment Extensions count toward your Segment Extension allotment, catalog segments also count toward that allotment.

### I have a catalog segment use case that the current template doesn't serve. How should I set that up?

Reach out to your customer support manager or [Braze Support]({{site.baseurl}}/user_guide/administrative/access_braze/support/) for additional guidance.

[1]: {% image_buster /assets/img/catalog-segments-template.png %}
[2]: {% image_buster /assets/img/catalog-segments-editor.png %}
