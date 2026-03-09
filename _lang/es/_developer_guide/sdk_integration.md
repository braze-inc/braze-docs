---
nav_title: Integrar el SDK
article_title: Integra el SDK de Braze
description: "Aprende a realizar la integración del SDK de Braze."
page_order: 2.0
---

# ![Logotipo]({% image_buster /assets/Braze_Primary_Icon_BLACK.svg %}){: style="float:right;width:120px;border:0;" class="noimgborder"} de Braze Integrar el SDK de Braze

> Aprende a realizar la integración del SDK de Braze. Cada SDK está alojado en su propio repositorio público de GitHub, que incluye aplicaciones de muestra totalmente compilables que puedes utilizar para probar las características de Braze o implementar junto con tus propias aplicaciones. Para obtener más información, consulta [Referencias, repositorios y aplicaciones de ejemplo]({{site.baseurl}}/developer_guide/references/). Para obtener información más general sobre el SDK, consulta [Introducción: Visión general de la integración]({{site.baseurl}}/developer_guide/getting_started/integration_overview/).

{% alert tip %}
Después de la integración del SDK, puedes habilitar [la autenticación del SDK]({{site.baseurl}}/developer_guide/sdk_integration/authentication/) para añadir una capa adicional de seguridad, ya que evita las solicitudes no autorizadas al SDK. La autenticación SDK está disponible para Web, Android, SWIFT, React Native, Flutter, Unity, Cordova, .NET MAUI (Xamarin) y Expo.
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

{% sdktab .NET MAUI (Xamarin) %}
{% multi_lang_include developer_guide/xamarin/sdk_integration.md %}
{% endsdktab %}

{% sdktab chatgpt apps %}
{% multi_lang_include developer_guide/chatgpt_apps/sdk_integration.md %}
{% endsdktab %}

{% sdktab vega %}
{% multi_lang_include developer_guide/vega/sdk_integration.md %}
{% endsdktab %}
{% endsdktabs %}

{% alert note %}
Mientras realizas el control de calidad de la integración de SDK, utiliza el [depurador del SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging) para solucionar problemas sin activar el registro detallado de tu aplicación.
{% endalert %}
