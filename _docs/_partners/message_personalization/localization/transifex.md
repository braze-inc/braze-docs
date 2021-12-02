---
nav_title: Transifex
article_title: Transifex
alias: /partners/transifex/
description: "This article outlines the partnership between Braze and Transifex, a localization platform that allows you to automate translation freeing up your teams to focus on delivering brilliant customer experiences."
page_tpe: partner
search_tag: Partner

---

# About Transifex

> Transifex enables robust localization across your user base, no matter the language. 

The Transifex and Braze integration leverage Connected Content, allowing you to include a source string in your messages instead of lines of language-based conditional formatting. This, in turn, automates translation and frees up your teams to focus on delivering brilliant customer experiences.

## Prerequisites

| Requirement| Origin| Access| Description|
| ---| ---| ---|
|Transifex Account | Transifex | [https://www.transifex.com/signin/](https://www.transifex.com/signin/) | You must first have a Transifex account to access their SDK integration information. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Integration

### Step 1: Set up basic authentication

To set up basic authentication for your account, navigate to the Braze platform, under __Manage Settings__, open the __Connected Content__ tab. Here you will provide the credentials used for all Connected Content calls to Transifex.

![Basic Authentication Credential Management][34]

Click __New Credential__, name your credential, and add your user name and password for your Transifex account.

![Basic Authentication Credential Creation][35]

### Step 2: Connected Content

The Transifex integration uses Transifex's translation [strings API][31]. The following CURL will allow you to see if your Transifex account has context values associated with translations. Input the `PROJECT_NAME` and `RESOURCE_NAME` found in your Transifex account. 

```
curl -i -L --user username:password -X GET https://www.transifex.com/api/2/project/<PROJECT_NAME>/resource/<RESOURCE_NAME>/translation/en/strings
```

For example, if your Transifex project is located at `https://www.transifex.com/appboy-3/french2/french_translationspo/`, the `project_name` will be "french2" and the `resource_name` will be "french_translationspo".

An example response with a blank context field is pictured below:

![Terminal response][33]{: style="max-width:60%;"}

## Connnected Content message example

This example code snippet utilizes the Transifex Strings API and the user's `language` attribute. 

{% raw %}
```
{% assign key = "<API_KEY>" %}
{% assign context = "<CONTENT>" %}
{% assign source_string = key | append: ':' | append: context %}
{% assign project = "<PROJECT_NAME>" %}
{% assign resource = "<RESOURCE_NAME>" %}
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
{% endraw %}

{% alert tip %}
You can also leverage the user's {% raw %}`{{${most_recent_locale}}}`{% endraw %} if you want to include a variation based upon a user's specific version of a language such as `zh_CN` or `pt_BR`.
{% endalert %}


[16]: [success@braze.com](mailto:success@braze.com)
[31]: https://docs.transifex.com/api/translation-strings
[32]: {% image_buster /assets/img_archive/TransifexUI.png %}
[33]: {% image_buster /assets/img_archive/terminal.png %}
[34]: {% image_buster /assets/img_archive/basic_auth_mgmt.png %}
[35]: {% image_buster /assets/img_archive/basic_auth_token.png %}