---
nav_title: Style personnalisé
article_title: "Style de fil d'actualité personnalisé pour Android et FireOS"
page_order: 0
platform: 
  - Android
  - FireOS
description: "Cet article de référence montre comment ajouter des styles de fil d'actualité personnalisé à votre application Android ou FireOS."
channel:
  - news feed
  
---

# Style personnalisé

> Cet article de référence montre comment ajouter des styles de fil d'actualité personnalisé à votre application Android ou FireOS. 

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Les éléments de l’IU de Braze sont dotés d’un aspect et d’une convivialité par défaut qui correspondent aux directives de l’IU standard d’Android et offrent une expérience transparente. Vous pouvez voir ces styles par défaut dans le fichier `res/values/style.xml` dans la distribution du SDK Braze :

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

Si vous préférez, vous pouvez écraser ces styles pour créer un aspect et une convivialité qui conviennent mieux à votre application. Pour remplacer un style, copiez-le dans son intégralité dans le fichier `styles.xml` dans votre projet et apportez des modifications. Le style entier doit être copié sur votre fichier `styles.xml` local pour que tous les attributs soient correctement définis.

{% tabs local %}
{% tab Corriger le remplacement de style %}

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
{% tab Style incorrect remplacé %}

```xml
<style name="Braze.Feed.List">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
</style>
```
{% endtab %}
{% endtabs %}

## Éléments de style de fil

Voici une description et les noms des éléments de l’IU de Braze pouvant être utilisés dans des thèmes à des fins de style :

{% gallery %}{% image_buster /assets/img_archive/Image27Theming.png %}
{% image_buster /assets/img_archive/Image28Theming.png %}
{% image_buster /assets/img_archive/Image29Theming.png %}
{% image_buster /assets/img_archive/Image30Theming.png %}{% endgallery %}

## Définir une police personnalisée

Braze permet de définir une police personnalisée en utilisant le [guide de la famille de polices]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization). Pour l’utiliser, remplacez un style pour les cartes et utilisez l’attribut `fontFamily` pour indiquer à Braze d’utiliser votre famille de polices personnalisée.

Par exemple, pour mettre à jour la police sur tous les titres des cartes d’actualités courtes, remplacez le style `Braze.Cards.ShortNews.Title` et référencez votre famille de polices personnalisée. La valeur d’attribut doit pointer vers une famille de polices dans votre répertoire `res/font`.

Voici un exemple tronqué avec une famille de polices personnalisées `my_custom_font_family`, référencé sur la dernière ligne :

```
<style name="Braze.Cards.ShortNews.Title">
  <item name="android:layout_height">wrap_content</item>
  ...
  <item name="android:fontFamily">@font/my_custom_font_family</item>
  <item name="fontFamily">@font/my_custom_font_family</item>
</style>
```

