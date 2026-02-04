---
nav_title: Incorporar GIFs
article_title: Incorporar GIFs em Cartões de Conteúdo
page_order: 5
description: "Aprenda como incorporar GIFs em Cartões de Conteúdo usando o SDK do Braze."
channel:
  - content cards
platform:
  - Android
  - Swift
  - Web
  - FireOS
---

# Incorporar GIFs em Cartões de Conteúdo

> Aprenda como incorporar GIFs em Cartões de Conteúdo usando o SDK do Braze.

{% alert note %}
Para SDKs wrapper não listados, use o método nativo relevante do Android ou Swift. Tenha em mente que os SDKs do Braze para Android e Swift não suportam GIFs animados nativamente, então você implementará GIFs em Cartões de Conteúdo usando ferramentas de terceiros.
{% endalert %}

{% sdktabs %}
{% sdktab web %}
O suporte a GIF está incluído por padrão na integração do SDK Web.
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/_global/gifs.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/gifs.md %}
{% endsdktab %}
{% endsdktabs %}
