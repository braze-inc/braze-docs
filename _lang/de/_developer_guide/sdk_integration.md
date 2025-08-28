---
nav_title: Einbinden des SDK
article_title: Integration des Braze SDK
description: "Erfahren Sie, wie Sie das Braze SDK integrieren können."
page_order: 2.0
---

# ![Braze Logo]({% image_buster /assets/Braze_Primary_Icon_BLACK.svg %}){: style="float:right;width:120px;border:0;" class="noimgborder"}Integration des Braze SDK

> Erfahren Sie, wie Sie das Braze SDK in Ihre mobile App integrieren können. Jedes SDK wird in seinem eigenen öffentlichen GitHub-Repository gehostet, das vollständig kompilierbare Beispiel-Apps enthält, mit denen Sie die Features von Braze testen oder neben Ihren eigenen Anwendungen implementieren können. Weitere Informationen finden Sie unter [Referenzen, Repositories und Beispiel-Apps]({{site.baseurl}}/developer_guide/references/). Weitere allgemeine Informationen über das SDK finden Sie unter [Erste Schritte: Übersicht über die Integration]({{site.baseurl}}/developer_guide/getting_started/integration_overview/).

{% alert tip %}

{% endalert %}

{% sdktabs %}
{% sdktab android %}
{% multi_lang_include developer_guide/android/sdk_integration.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/sdk_integration.md %}
{% endsdktab %}

{% sdktab web %}
{% multi_lang_include developer_guide/web/sdk_integration.md %}
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

{% sdktab xamarin %}
{% multi_lang_include developer_guide/xamarin/sdk_integration.md %}
{% endsdktab %}
{% endsdktabs %}

{% alert note %}
Verwenden Sie bei der QA Ihrer SDK-Integration den [SDK-Debugger]({{site.baseurl}}/developer_guide/sdk_integration/debugging), um Fehlerbehebungen durchzuführen, ohne die ausführliche Protokollierung für Ihre App zu aktivieren.
{% endalert %}