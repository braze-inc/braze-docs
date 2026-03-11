---
nav_title: Integre o SDK
article_title: Integre o SDK do Braze
description: "Aprenda como integrar o SDK do Braze."
page_order: 2.0
---

# ![Logotipo do Braze]({% image_buster /assets/Braze_Primary_Icon_BLACK.svg %}){: style="float:right;width:120px;border:0;" class="noimgborder"}Integre o SDK do Braze

> Aprenda como integrar o SDK do Braze. Cada SDK é hospedado em seu próprio repositório público no GitHub, que inclui aplicativos de exemplo totalmente compiláveis que você pode usar para testar os recursos do Braze ou implementar ao lado de suas próprias aplicações. Para saber mais, veja [Referências, Repositórios e Aplicativos de Exemplo]({{site.baseurl}}/developer_guide/references/). Para mais informações gerais sobre o SDK, veja [Introdução: Visão geral da integração]({{site.baseurl}}/developer_guide/getting_started/integration_overview/).

{% alert tip %}
Após integrar o SDK, você pode ativar [Autenticação do SDK]({{site.baseurl}}/developer_guide/sdk_integration/authentication/) para adicionar uma camada adicional de segurança, impedindo solicitações não autorizadas ao SDK. A autenticação do SDK está disponível para Web, Android, Swift, React Native, Flutter, Unity, Cordova, .NET MAUI (Xamarin) e Expo.
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
Ao realizar QA na sua integração do SDK, use o [Depurador do SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging) para solucionar problemas sem ativar o registro detalhado para seu app.
{% endalert %}
