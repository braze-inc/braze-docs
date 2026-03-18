---
nav_title: Filtering and segmentation operators
article_title: Filtering and segmentation operators
page_order: 2
page_type: reference
description: "This reference article covers how filtering and segmentation operators apply to custom attributes, event properties, and catalog selections in Braze."
toc_headers: h2
---

# Filtering and segmentation operators

> This reference article covers how filtering and segmentation operators compare across custom attributes on user profiles, event properties in segments, and [catalog selections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/). It isn't a glossary of every segment filter—for that list, see [Segmentation filters]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/). For supported data types and usage by type, see [Data types]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/).

The following table summarizes operators by data type and surface. It doesn't replace the full operator lists for custom attributes (see the tabs under [Custom attribute data types]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#custom-attribute-data-types) on the Data types page).

<table role="presentation" class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4">
  <thead>
    <tr>
      <th>Data type</th>
      <th>Custom attributes (segmentation)</th>
      <th>Event properties (segmentation)</th>
      <th>Catalog selection filters</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Boolean</td>
      <td><strong>IS</strong>, <strong>IS BLANK</strong>, <strong>IS NOT BLANK</strong></td>
      <td>True/false matching in property filters.</td>
      <td rowspan="6">Only <strong>equals</strong> and <strong>does not equal</strong> per filter row. See <a href="#considerations">Considerations</a>.</td>
    </tr>
    <tr>
      <td>Number</td>
      <td><strong>EXACTLY</strong>, <strong>DOES NOT EQUAL</strong>, <strong>MORE THAN</strong>, <strong>LESS THAN</strong>, <strong>IS BLANK</strong>, <strong>IS NOT BLANK</strong></td>
      <td>Numeric comparisons (for example, equals, more than, less than) in property filters.</td>
    </tr>
    <tr>
      <td>String</td>
      <td>Includes <strong>MATCHES REGEX</strong>, <strong>IS ANY OF</strong>, <strong>IS NONE OF</strong>, <strong>CONTAINS ANY OF</strong>, <strong>IS NOT BLANK</strong>, <strong>BLANK</strong>, and more—see the <strong>Strings</strong> tab under <a href="{{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#custom-attribute-data-types">Custom attribute data types</a>.</td>
      <td>Multiple values (for example, equal to any of) and other operators; the set differs from custom attribute filters.</td>
    </tr>
    <tr>
      <td>Time</td>
      <td><strong>BEFORE</strong>, <strong>AFTER</strong>, <strong>MORE THAN</strong> / <strong>LESS THAN</strong> (days ago or in the future), <strong>IS BLANK</strong>, <strong>IS NOT BLANK</strong></td>
      <td>Date and time operators in Segment Extension property filters.</td>
    </tr>
    <tr>
      <td>Array</td>
      <td>Includes <strong>INCLUDES VALUE</strong>, <strong>INCLUDES ANY OF</strong>, <strong>MATCHES REGEX</strong>, <strong>HAS A VALUE</strong>, <strong>IS EMPTY</strong>, and more—see <a href="{{site.baseurl}}/user_guide/data/activation/custom_data/data_types/?tab=arrays#custom-attribute-data-types">Custom attribute data types</a>.</td>
      <td>Operators depend on segment type—see <a href="#considerations">Considerations</a>. Storage and element rules differ by surface—see the <strong>Array</strong> tab under <a href="{{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#important-considerations">Data type considerations</a> on the Data types page.</td>
    </tr>
    <tr>
      <td>Object</td>
      <td>Filters on nested fields (paths). For more information, refer to <a href="{{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support/">Nested custom attributes</a>.</td>
      <td><strong>equals</strong> and <strong>does not equal</strong> on nested keys, plus patterns in <a href="{{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects/">Nested objects</a>.</td>
    </tr>
    <tr>
      <td>Array of objects</td>
      <td>Filters on fields inside objects in the array—see <a href="{{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects/">Array of objects</a>.</td>
      <td>Not supported</td>
      <td>Not supported</td>
    </tr>
  </tbody>
</table>

## Filter considerations {#considerations}

- **Event properties:** Operator choices depend on where you segment. [Segment Extensions]({{site.baseurl}}/user_guide/audience/segments/segment_extension/) use one set of property filters; standard segments use another when you filter on event properties (with a shorter lookback than extensions). For more information about behavior, windows, and setup, see [Custom event properties]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties/).
- **Catalog selections:** For every filterable column in a [catalog selection]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/), the **Operator** dropdown offers only **equals** and **does not equal** (same for all types that support catalog filters).

## Consolidated operators {#consolidated-operators}

Braze uses the following operator names for attribute filters, custom attribute filters, and nested custom attribute filters. If you had filters that used the old labels, Braze updates them automatically to the new operators.

| Data type | Old operator | New operator | Value |
| --- | --- | --- | --- |
| String | equals | is any of | At least one value |
| String | does not equal | is none of | At least one value |
| Array | includes value | includes any of | At least one value |
| Array | doesn't include value | includes none of | At least one value |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

For more information about full segmentation options by attribute type, see [Custom attribute data types]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#custom-attribute-data-types).
