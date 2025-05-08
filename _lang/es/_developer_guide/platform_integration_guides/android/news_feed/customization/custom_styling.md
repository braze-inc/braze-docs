---
nav_title: Estilo personalizado
article_title: Estilo personalizado de la fuente de noticias para Android y FireOS
page_order: 0
platform: 
  - Android
  - FireOS
description: "Este artículo de referencia explica cómo añadir un estilo personalizado a la fuente de noticias en tu aplicación Android o FireOS."
channel:
  - news feed
  
---

# Estilo personalizado

> Este artículo de referencia explica cómo añadir un estilo personalizado a la fuente de noticias en tu aplicación Android o FireOS. 

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Los elementos de la interfaz de usuario de Braze vienen con un aspecto predeterminado que se ajusta a las directrices de la interfaz de usuario estándar de Android y proporciona una experiencia sin fisuras. Puedes ver estos estilos predeterminados en el archivo `res/values/style.xml` de la distribución del SDK de Braze:

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

Si lo prefieres, puedes anular estos estilos para crear un aspecto que se adapte mejor a tu aplicación. Para anular un estilo, cópialo en su totalidad en el archivo `styles.xml` de tu proyecto y haz modificaciones. Debes copiar todo el estilo en tu archivo local `styles.xml` para que todos los atributos estén correctamente configurados.

{% tabs local %}
{% tab Anulación correcta del estilo %}

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
{% tab Anulación de estilo incorrecta %}

```xml
<style name="Braze.Feed.List">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
</style>
```
{% endtab %}
{% endtabs %}

## Elementos de estilo de la fuente

A continuación se describen los elementos tematizables de la interfaz de usuario de Braze y sus nombres a efectos de estilo:

{% gallery %}{% image_buster /assets/img_archive/Image27Theming.png %}
{% image_buster /assets/img_archive/Image28Theming.png %}
{% image_buster /assets/img_archive/Image29Theming.png %}
{% image_buster /assets/img_archive/Image30Theming.png %}{% endgallery %}

## Configuración de una fuente personalizada

Braze permite configurar una fuente personalizada utilizando la [guía de familias de fuentes]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization). Para utilizarlo, anula un estilo para tarjetas y utiliza el atributo `fontFamily` para indicar a Braze que utilice tu familia de fuentes personalizada.

Por ejemplo, para actualizar la fuente de todos los títulos de las tarjetas de noticias breves, anula el estilo `Braze.Cards.ShortNews.Title` y haz referencia a tu familia de fuentes personalizada. El valor del atributo debe apuntar a una familia de fuentes de tu directorio `res/font`.

Aquí tienes un ejemplo truncado con una familia de fuentes personalizada, `my_custom_font_family`, a la que se hace referencia en la última línea:

```
<style name="Braze.Cards.ShortNews.Title">
  <item name="android:layout_height">wrap_content</item>
  ...
  <item name="android:fontFamily">@font/my_custom_font_family</item>
  <item name="fontFamily">@font/my_custom_font_family</item>
</style>
```

