---
nav_title: Estilo personalizado
article_title: Estilo personalizado do feed de notícias para iOS
platform: iOS
page_order: 0
description: "Este artigo de referência aborda como implementar o estilo personalizado do feed de notícias e substituir as imagens padrão em seu aplicativo iOS."
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Estilo personalizado

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

A integração do `SDWebImage` é necessária se você planeja usar nossa Braze UI para exibir imagens nas mensagens no app do iOS, no feed de notícias ou nos cartões de conteúdo.

## Substituição de imagens padrão

O Braze permite que os clientes substituam as imagens padrão existentes por suas próprias imagens personalizadas. Para realizar isso, crie um novo arquivo `png` com a imagem personalizada e adicione-o ao pacote de imagens do app. Em seguida, renomeie o arquivo com o nome da imagem para substituir a imagem padrão em nossa biblioteca. Além disso, faça o upload das versões `@2x` e `@3x` das imagens para acomodar diferentes tamanhos de telefone. As imagens disponíveis para substituição nos cartões de conteúdo incluem: As imagens disponíveis para substituição no feed de notícias incluem:

* Indicador do ícone de leitura: `Icons_Read`
* Imagem de espaço reservado: `img-noimage-lrg`

{% alert important %}
Substituir imagens padrão atualmente não é permitido em nossa integração Xamarin iOS.
{% endalert %}

