---
nav_title: Integração do SDK
article_title: Integração do SDK do Braze
description: "Saiba como integrar o Braze SDK."
page_order: 2.0
---

# ![Logotipo do Braze]({% image_buster /assets/Braze_Primary_Icon_BLACK.svg %}){: style="float:right;width:120px;border:0;" class="noimgborder"}Integração do SDK do Braze

> Saiba como integrar o Braze SDK em seu app para dispositivos móveis. Cada SDK é hospedado em seu próprio repositório público do GitHub, que inclui apps de amostra totalmente compiláveis que você pode usar para testar os recursos do Braze ou implementar junto com seus próprios aplicativos. Para saber mais, consulte [Referências, repositórios e aplicativos de amostra]({{site.baseurl}}/developer_guide/references/). Para saber mais informações gerais sobre o SDK, consulte [Getting started: Visão geral da integração]({{site.baseurl}}/developer_guide/getting_started/integration_overview/).

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
Ao realizar o controle de qualidade na integração do SDK, use o [depurador do SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging) para solucionar problemas sem ativar o registro detalhado do seu aplicativo.
{% endalert %}