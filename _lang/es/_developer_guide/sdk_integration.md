---
nav_title: Integración del SDK
article_title: Integración del SDK de Braze
description: "Aprende a integrar el SDK de Braze."
page_order: 2.0
---

# ![Logo Braze]({% image_buster /assets/Braze_Primary_Icon_BLACK.svg %}){: style="float:right;width:120px;border:0;" class="noimgborder"}Integración del SDK Braze

> Aprende a integrar el SDK de Braze en tu aplicación móvil. Cada SDK está alojado en su propio repositorio público de GitHub, que incluye aplicaciones de muestra totalmente compilables que puedes utilizar para probar las características de Braze o implementarlas junto con tus propias aplicaciones. Para saber más, consulta [Referencias, Repositorios y Ejemplos de aplicaciones]({{site.baseurl}}/developer_guide/references/). Para más información general sobre el SDK, consulta [Introducción: Visión general de la integración]({{site.baseurl}}/developer_guide/getting_started/integration_overview/).

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
Mientras realizas el control de calidad de tu integración de SDK, utiliza [el depurador de SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging) para solucionar problemas sin activar el registro detallado de tu aplicación.
{% endalert %}