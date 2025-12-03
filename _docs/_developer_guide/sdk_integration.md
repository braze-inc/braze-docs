---
nav_title: Integrating the SDK
article_title: Integrating the Braze SDK
description: "Learn how to integrate the Braze SDK."
page_order: 2.0
---

# ![Braze Logo]({% image_buster /assets/Braze_Primary_Icon_BLACK.svg %}){: style="float:right;width:120px;border:0;" class="noimgborder"}Integrating the Braze SDK

> Learn how to integrate the Braze SDK into your mobile app. Each SDK is hosted in its own public GitHub repository, which includes fully-buildable sample apps you can use to test Braze features or implement alongside your own applications. To learn more, see [References, Repositories, and Sample Apps]({{site.baseurl}}/developer_guide/references/). For more general information about the SDK, see [Getting started: Integration overview]({{site.baseurl}}/developer_guide/getting_started/integration_overview/).

{% alert tip %}

{% endalert %}

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/sdk_integration.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/sdk_integration.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/sdk_integration.md %}
{% endsdktab %}

{% sdktab cordova %}
{% multi_lang_include developer_guide/cordova/sdk_integration.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/sdk_integration.md %}
{% endsdktab %}

{% sdktab react native %}
{% multi_lang_include developer_guide/react_native/sdk_integration.md %}
{% endsdktab %}

{% sdktab roku %}
{% multi_lang_include developer_guide/roku/sdk_integration.md %}
{% endsdktab %}

{% sdktab unity %}
{% multi_lang_include developer_guide/unity/sdk_integration.md %}
{% endsdktab %}

{% sdktab unreal engine %}
{% multi_lang_include developer_guide/unreal_engine/sdk_integration.md %}
{% endsdktab %}

{% sdktab .NET MAUI %}
{% multi_lang_include developer_guide/xamarin/sdk_integration.md %}
{% endsdktab %}

{% sdktab chatgpt apps %}
{% multi_lang_include developer_guide/chatgpt_apps/sdk_integration.md %}
{% endsdktab %}
{% endsdktabs %}

{% alert note %}
While performing QA on your SDK integration, use the [SDK Debugger]({{site.baseurl}}/developer_guide/sdk_integration/debugging) to get troubleshoot issues without turning on verbose logging for your app.
{% endalert %}
