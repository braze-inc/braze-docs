---
nav_title: Estilo Personalizado
article_title: Estilo personalizado do feed de notícias para Android e FireOS
page_order: 0
platform: 
  - Android
  - FireOS
description: "Este artigo de referência cobre como adicionar estilo personalizado ao feed de notícias no seu aplicativo Android ou FireOS."
channel:
  - news feed
  
---

# Estilo personalizado

> Este artigo de referência cobre como adicionar estilo personalizado ao feed de notícias no seu aplicativo Android ou FireOS. 

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Os elementos da {Braze} UI vêm com uma aparência padrão que corresponde às diretrizes padrão de UI do {Android} e proporciona uma experiência perfeita. Você pode ver esses estilos padrão no arquivo `res/values/style.xml` na distribuição do SDK da Braze:

```xml
  <style name="Braze"/>
  <!-- Feed -->
  <style name="Braze.Feed"/>
  <style name="Braze.Feed.List">
    <item name="android:background">@android:color/transparent</item>
    <item name="android:divider">@android:color/transparent</item>
    <item name="android:dividerHeight">16.0dp</item>
    <item name="android:paddingLeft">12.5dp</item>
    <item name="android:paddingRight">5.0dp</item>
    <item name="android:scrollbarStyle">outsideInset</item>
  </style>
  ...
  </style>
```

Se preferir, você pode substituir esses estilos para criar uma aparência que melhor se adapte ao seu app. Para substituir um estilo, copie-o na sua totalidade para o arquivo `styles.xml` no seu projeto e faça modificações. O estilo completo deve ser copiado para o seu arquivo `styles.xml` local para que todos os atributos sejam configurados corretamente.

{% tabs localização %}
{% tab Estilo de correção substituído %}

```xml
<style name="Braze.Feed.List">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
  <item name="android:divider">@android:color/transparent</item>
  <item name="android:dividerHeight">16.0dp</item>
  <item name="android:paddingLeft">12.5dp</item>
  <item name="android:paddingRight">5.0dp</item>
  <item name="android:scrollbarStyle">outsideInset</item>
</style>
```
{% endtab %}
{% tab Substituição de estilo incorreta %}

```xml
<style name="Braze.Feed.List">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
</style>
```
{% endtab %}
{% endtabs %}

## Elementos de estilo de feed

Veja a seguir uma descrição dos elementos de UI da Braze que podem ser tematizados e seus nomes para fins de estilização:

{% gallery %}{% image_buster /assets/img_archive/Image27Theming.png %}
{% image_buster /assets/img_archive/Image28Theming.png %}
{% image_buster /assets/img_archive/Image29Theming.png %}
{% image_buster /assets/img_archive/Image30Theming.png %}{% endgallery %}

## Definindo uma fonte personalizada

Braze permite definir uma fonte personalizada usando o [guia de família de fontes]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization). Para usá-lo, substitua um estilo para cartões e use o atributo `fontFamily` para instruir a Braze a usar sua família de fontes personalizada.

Por exemplo, para atualizar a fonte em todos os títulos de cartões de notícias curtas, substitua o estilo `Braze.Cards.ShortNews.Title` e faça referência à sua família de fontes personalizada. O valor do atributo deve apontar para uma família de fontes no seu diretório `res/font`.

Aqui está um exemplo truncado com uma família de fontes personalizadas, `my_custom_font_family`, referenciada na última linha:

```
<style name="Braze.Cards.ShortNews.Title">
  <item name="android:layout_height">wrap_content</item>
  ...
  <item name="android:fontFamily">@font/my_custom_font_family</item>
  <item name="fontFamily">@font/my_custom_font_family</item>
</style>
```

