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

> Catalog segments are an audience of users based on catalog data in SQL Segment Extensions. These SQL Segment Extensions can be referenced in a segment and then targeted by campaigns and Canvases. 

{% alert important %}
Catalog segments are currently in early access. Contact your customer success manager if you're interested in participating in this early access.
{% endalert %}

Catalog segments use SQL to join data from catalogs and data from custom events or purchases. To do so, you must have a common identifier field across your catalogs and your custom events or purchases. For example, the value of an item ID in a catalog must match the value of a property in a custom event.

## Use cases

### Ecommerce

- Catalog of products where the item ID value is equal to the Shopify ID
- Custom event `Made Order` with a property (such as `shopify_id`) that has the same value as the Shopify ID

### Health app

- Catalog of different doctors a patient can book, each with an item ID  
- Custom event `Booked Visit` with a property that has the same value as the item ID

## Creating a catalog segment

1. Go to **Segment Extensions** > **Create New Extension** > **Start With Template** and select the template **Catalog segment**. <br>![Modal with "Catalog segment" selected as the template to create.][1]{: style="max-width:70%" }

{: start="2"}
2. The SQL editor automatically populates with a template. <br>![SQL editor with a pregenerated template.][2]{: style="max-width:70%" }<br>The following fields in this template are left blank and must be filled out before the segment can be generated:

| Field | Description |
| --- | --- |
| `items.catalog.id` | This is the ID for a specific catalog, which can be pulled from the catalog URL in the Braze dashboard. |
| `id` | Replace `:id` (located before `::STRING`) with the event or purchase property that matches your item ID in the catalog. In the ecommerce use case, you would insert `shopify_id`. |
| `events.name` |  If using a custom event, you must either populate this with the name of your custom event or remove it if you'd like to filter on all events (events that don't have the property won't be joined on the catalog). In nearly all use cases, you will be adding the name of a specific custom event.<br><br>If using a purchase event, replace `event.name = ''` with `event.product_id = ''` and add the name of your product.|
{: .reset-td-br-1 .reset-td-br-2}

{: start=”3”}
3. If needed, fill in additional optional fields for your use case to segment by a particular field value within your catalog:
- `items.field_name`: A particular field (column name) within this catalog
- `items.field_value`: A specific value within that field or column <br><br> Using the health app as an example, let’s say that within the catalog for each doctor you could book, there’s a field called `specialty` that contains a value such as `vision` or `dental`. To segment users who have visited any doctors with the value `dental`, you can replace `items.field_name` with `specialty`, and replace `items.field_value` with `dental`. 

4. After creating a SQL Segment, we recommend clicking **Run Preview** to see if your query returns users or if there are errors. For more information about [previewing query results]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#previewing-results), managing [SQL Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#managing-sql-segment-extensions), and more, check out [SQL Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). 

## Frequently asked questions

### Does running a catalog segment consume SQL Segment Extension credits?

Yes, catalog segments are powered by SQL and consume SQL Segment Extension credits. To learn more, check out [SQL Segments usage]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments#monitoring-your-sql-segments-usage).

### Does creating a catalog segment consume SQL Segment Extension allotments?

Yes. In the same way SQL Segment Extensions count toward your Segment Extension allotment, catalog segments also count toward that allotment.

### I have a catalog segment use case that the current template doesn't serve. How should I set that up?

Reach out to your customer support manager or [Braze Support]({{site.baseurl}}/help/support/) for additional guidance.

[1]: {% image_buster /assets/img/catalog-segments-template.png %}
[2]: {% image_buster /assets/img/catalog-segments-editor.png %}