---
nav_title: Transifex
alias: /partners/transifex/
description: "This article outlines the partnership between Braze and Transifex, a localization platform that allows you to automate translation so your teams are freed up to focus on delivering brilliant customer experiences."
---

# About Transifex

Transifex enables powerful localization across your user base, no matter what the language is. Transifex and Braze's Connected Content feature empowers you to automate translation so your teams are freed up to focus on delivering brilliant customer experiences.

## Prerequisites

| Requirement| Origin| Access| Description|
| ---| ---| ---|
|Transifex Account | Transifex | https://www.transifex.com/signin/ | You must first have a Transifex account to access their SDK integration information. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

Set up basic authentication for your account in the __Connected Content__ tab in __Manage Settings__.

![Basic Authentication Credential Management][34]

Click __New Credential__. You can then name your credentials and put in your username and password for that account.

![Basic Authentication Credential Creation][35]

You can then use this basic authentication credential for calls to Transifex.

## Connected Content Integration

This integration will allow you to type in a source string instead of copying and pasting the translation for every language into the message composer.

The code for our Transifex integration was built using Transifex's translation [strings API][31].

The following CURL will allow you to see if your Transifex account has context values associated with translations:

```
curl -i -L --user username:password -X GET https://www.transifex.com/api/2/project/<project_name>/resource/<resource_name>/translation/en/strings
```

Input the project and resource name into CURL. You can find these values in the URL of your Transifex account.

![Transifex_account][32]

An example response with a blank context field is pictured below:

![terminal_response][33]

## Transifex Integration Code Example

Here is example code that utilizes the Transifex Strings API and the user's "language" attribute.

{% raw %}
```
{% assign key = "<Insert Key Here>" %}
{% assign context = "<Insert Context Here>" %}
{% assign source_string = key | append: ':' | append: context %}
{% assign project = "<Insert Project Name Here>" %}
{% assign resource = "<Insert Resource Name Here" %}
{% assign source_hash = source_string | md5 %}

{% if {{${language}}} == "en" or {{${language}}} == "it" or {{${language}}} == "de" or {{${language}}} == "another_language_you_support"  %}
{% connected_content https://www.transifex.com/api/2/project/{{project}}/resource/{{resource}}/translation/{{${language}}}/string/{{source_hash}}/ :basic_auth <Insert Basic Auth Credential Name Here> :save strings %}
{% endif %}

{% if {{strings}} != null and {{strings.translation}} != "" and {{${language}}} != null %}
  {{strings.translation}}
{% else %}
  {% abort_message('null or blank') %}
{% endif %}
```

You can also leverage the user's `{{${most_recent_locale}}}` if you want to include a variation based upon a user's specific version of a language such as `zh_CN` or `pt_BR`.

{% endraw %}

[16]: [success@braze.com](mailto:success@braze.com)
[31]: https://docs.transifex.com/api/translation-strings
[32]: {% image_buster /assets/img_archive/TransifexUI.png %}
[33]: {% image_buster /assets/img_archive/terminal.png %}
[34]: {% image_buster /assets/img_archive/basic_auth_mgmt.png %}
[35]: {% image_buster /assets/img_archive/basic_auth_token.png %}
