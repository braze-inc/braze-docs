---
nav_title: Phrase
article_title: Phrase
alias: /partners/phrase/
description: "This reference article outlines the partnership between Braze and Phrase, a cloud-based software for localization. This integration allows you to translate email templates and Content Blocks without leaving the Braze interface."
page_type: partner
search_tag: Partner

---

# Phrase 

> [Phrase](https://phrase.com/) is a cloud-based software for localization management. Phrase enables automated translation workflows and supports continuous localization for agile teams.

_This integration is maintained by Phrase._

## About the integration

The Phrase and Braze integration allow you to translate email templates and Content Blocks without leaving the Braze interface. With the Phrase TMS integration for Braze, you can increase customer engagement and drive growth into new markets with seamless localization.

## Prerequisites

| Requirement | Description |
| --- | --- |
| Phrase TMS account | A Phrase TMS Ultimate or Enterprise account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with all permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

## Step 1: Phrase TMS Settings

In Phrase, navigate to **Settings > Integrations > Connectors > New**.

1. Provide a name for the connection and change the type to **Braze**.<br><br>
2. Enter the REST API key and the Braze REST endpoint. <br><br>
3. Select how the connector should import email templates with linked Content Blocks. 
- Selected email template only
- Include Content Blocks<br><br>
4. Select how the connector should export email template translations. 
- Create new item
- Original item
  - Original item exports translations to the same template/block. Language segments are defined by the provided attribute.<br><br>
    {% raw %}
    Provide the language attribute if original item is selected. The language attribute defines the language of the if/elsif argument. If you are using the original item option, it must be structured as shown below:

    ```liquid
    {% if {{custom_attribute.${attribute_name}}} == 'da-DK' %}
    danish content
    {% elsif {{custom_attribute.${attribute_name}}} == 'pt-PT' %}
    portuguese content
    {% elsif {{custom_attribute.${attribute_name}}} == 'sv-SE' %}
    swedish content
    {% else %}
    Original content
    {% endif %}
    ```
    Or using the assign keys/values mapping:
    ```liquid
    {% if {{custom_attribute.${attribute_name}}} == 'da-DK' %}
      {% assign abc_key1 = "danish_value1" %}
    {% elsif {{custom_attribute.${attribute_name}}} == 'pt-PT' %}
      {% assign abc_key = "portuguese value" %}
    {% elsif {{custom_attribute.${attribute_name}}} == 'sv-SE' %}
      {% assign abc_key = "swedish value" %}
    {% else %}
      {% assign abc_key = "Source language value" %}
    {% endif %}
    ```
    The above Liquid must be strictly followed, but the language attribute and language, keys, and value are adjustable.<br><br>
    Each language code can only be used once, However, multiple languages can be used for one segment, for example:
    ```liquid
    {% elsif {{custom_attribute.${attribute_name}}} == 'de-DE' or {{custom_attribute.${attribute_name}}} == 'de-AT' or {{custom_attribute.${attribute_name}}} == 'de-CH' %}
    {% endraw %}
    ```
5. Click **Test connection**. A checkmark will appear if the connection is successful. Hover over the icon to see additional details.<br><br>
7. Lastly, click **Save**. This connector will be available on the **Connectors** page.

## Step 3: Send content to Phrase and export back to Braze

1. First, set up the [submitter portal](https://support.phrase.com/hc/en-us/articles/5709602111132) to allow submitters to add files to requests directly from the online repository.<br><br>
2. Use [Automated Project Creation (APC)](https://support.phrase.com/hc/en-us/articles/5709647363356) to have Phrase TMS automatically create new projects when a change in the specified workflow states is detected.<br><br>
3. Selected content items are imported the very first time APC runs.

The [Connector API](https://cloud.memsource.com/web/docs/api#) can automate steps otherwise performed manually through the UI. [Webhooks](https://support.phrase.com/hc/en-us/articles/5709693398812) can be used to have Phrase TMS notify 3rd party systems about certain events (for example, a job status change).


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
