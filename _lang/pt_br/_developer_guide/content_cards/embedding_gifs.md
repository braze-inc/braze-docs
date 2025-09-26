---
nav_title: Incorporação de GIFs
article_title: Incorporação de GIFs em cartões de conteúdo
page_order: 5
description: "Saiba como incorporar GIFs em cartões de conteúdo usando o SDK do Braze."
channel:
  - content cards
platform:
  - Android
  - Swift
  - Web
  - FireOS
---

# Incorporação de GIFs em cartões de conteúdo

> Saiba como incorporar GIFs em cartões de conteúdo usando o SDK do Braze.

{% alert note %}
Para SDKs de wrapper não listados, use o método nativo relevante do Android ou Swift. Lembre-se de que os SDKs do Android e do Swift Braze não oferecem suporte nativo a GIFs animados, portanto, você implementará GIFs de cartão de conteúdo usando ferramentas de terceiros.
{% endalert %}

{% sdktabs %}
{% sdktab android %}
{% multi_lang_include developer_guide/android/_global/gifs.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/gifs.md %}
{% endsdktab %}

{% sdktab web %}
No momento, os GIFs do cartão de conteúdo não são compatíveis com o SDK do Braze.
{% endsdktab %}
{% endsdktabs %}
