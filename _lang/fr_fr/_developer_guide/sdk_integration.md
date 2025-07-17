---
nav_title: Intégration du SDK
article_title: Intégration du SDK de Braze
description: "Découvrez comment intégrer le SDK de Braze."
page_order: 2.0
---

# Intégration du SDK de Braze

> Découvrez comment intégrer le SDK de Braze dans votre application mobile. Chaque SDK est hébergé dans son propre dépôt public GitHub, qui comprend des exemples d'applications entièrement constructibles que vous pouvez utiliser pour tester les fonctionnalités de Braze ou mettre en œuvre parallèlement à vos propres applications. Pour en savoir plus, consultez les [références, les référentiels et les exemples d'applications.]({{site.baseurl}}/developer_guide/references/) Pour plus d'informations générales sur le SDK, consultez le site [Getting started : Aperçu de l'intégration]({{site.baseurl}}/developer_guide/getting_started/integration_overview/).

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
Lors de l'assurance qualité de votre intégration SDK, utilisez le [débogueur SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging) pour résoudre les problèmes sans avoir à activer l'enregistrement des données pour votre application.
{% endalert %}
