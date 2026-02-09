---
nav_title: Transifex
article_title: Transifex
alias: /partners/transifex/
description: "This reference article outlines the partnership between Braze and Transifex, a localization platform that allows you to automate translation freeing up your teams to focus on delivering brilliant customer experiences."
page_type: partner
search_tag: Partner

---

# Transifex

> [Transifex](https://www.transifex.com/) enables robust localization across your user base, no matter the language.

_This integration is maintained by Transifex._

## About the integration

The Braze and Transifex integration uses Connected Content to allow you to pull a resource string collection and include relevant translations in your messages instead of lines of language-based conditional formatting. This automates translation and frees up your teams to focus on delivering brilliant customer experiences.

{% alert important %}
As of April 7, 2022, Transifex has deprecated their API versions 2 and 2.5 to make way for version 3. v2 and v2.5 are no longer operational, and relevant requests will fail. <br><br>The following integration instructions reflect the version 3 update. Update your Connected Content calls accordingly.
{% endalert %}

## Prerequisites

| Requirement| Description|
| ---| ---|
|Transifex Account | A [Transifex account](https://www.transifex.com/signin/) is required to take advantage of this partnership. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

The Transifex integration uses Transifex's [resource translations API](https://developers.transifex.com/reference/get_resource-translations). The following cURL will allow you to see if your account has content values associated with translations. 

First, input the `<ORGANIZATION_NAME>`, `<PROJECT_NAME>`, and `<RESOURCE_NAME>` found in your Transifex account. Next, replace `<LANGUAGE>` with the language code you would like to filter translations by, and `<TRANSIFEX_BEARER_TOKEN>` with your Transifex [bearer token](https://developers.transifex.com/reference/api-authentication).

```
curl --request GET \
     --url 'https://rest.api.transifex.com/resource_translations?filter\[resource\]=o:<ORGANIZATION_NAME>:p:<PROJECT_NAME>:r:<RESOURCE_NAME>&filter\[language\]=l:<LANGUAGE>' \
     --header 'Accept: application/vnd.api+json' \
     --header 'Authorization: Bearer 1/<TRANSFIX_BEARER_TOKEN>'
```

For example, if your Transifex project is located at `https://www.transifex.com/appboy-3/french2/french_translationspo/`, the `project_name` will be "french2" and the `resource_name` will be "french_translationspo".

## Connected Content message example

This example code snippet utilizes the Transifex resource translation API and the user's `language` attribute. Based on your needs, you can then loop through the string objects and pull in the relevant content using the following Liquid: `{{strings.data[X].attributes.strings.other}}`.

{% raw %}
```
{% assign organization = "<ORGANIZATION_NAME>" %}
{% assign project = "<PROJECT_NAME>" %}
{% assign resource = "<RESOURCE_NAME>" %}

{% if {{${language}}} == "en" or {{${language}}} == "it" or {{${language}}} == "de" or {{${language}}} == "another_language_you_support"  %}
{% connected_content
     https://rest.api.transifex.com/resource_translations?filter[resource]=o:{{organization}}:p:{{project}}:r:{{resource}}&filter[language]=l:{{${language}}}
     :method GET
     :headers {
       "Authorization": "Bearer <TRANSIFEX_BEARER_TOKEN>"
  }
     :accept application/vnd.api+json
     :save strings
%}
{% endif %}

{% if {{strings}} != null and {{strings.data[0].attributes.strings.other}} != "" and {{${language}}} != null %}
  {{strings.data[0].attributes.strings.other}}
{% else %}
  {% abort_message('null or blank') %}
{% endif %}
```
{% endraw %}


[16]: [success@braze.com](mailto:success@braze.com)
