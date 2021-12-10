---
nav_title: Personnalisation de la police
article_title: Personnalisation de police pour Android/FireOS
platform:
  - Android
  - Pare-feu
page_order: 7
description: "Cet article de référence couvre les options de personnalisation de la police telles que la définition d'une famille de polices et montre comment la référencer tout au long de votre application."
---

# Personnalisation de la police

Les polices du Braze SDK peuvent être définies via XML en utilisant les bibliothèques AndroidX selon [Font in XML Guide][1]. Pour utiliser votre police personnalisée avec le Braze SDK, vous devrez d'abord créer une famille de polices.

## Créer une famille de polices

Ce qui suit est un exemple de définition de famille de polices personnalisées en utilisant le [guide de la famille de polices][2]. Pour cet exemple, nous utilisons la police [Bungee Shade][3].

```XML
<?xml version="1. " encoding="utf-8"?>
<font-family xmlns:android="http://schemas.android.com/apk/res/android"
             xmlns:app="http://schemas.android.com/apk/res-auto">

  <! -Note : Vous devez déclarer les deux ensembles d'attributs
      pour que vos polices soient chargées sur les appareils fonctionnant sous Android 8. (API niveau 26) ou moins.
      Voir https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml.html -->

  <font android:fontStyle="normal"
        android:fontWeight="400"
        android:font="@font/bungeeshade"

        app:fontStyle="normal"
        app:fontWeight="400"
        app:font="@font/bungeeshade"/>
</font-family>
```

Après avoir stocké la définition de la famille de polices dans `/res/font/bungee_font_family.xml`, nous pouvons la appeler en XML `@font/bungee_font_family`.

## Référencement de votre famille de polices

Maintenant que la famille de polices est créée, vous pouvez remplacer les valeurs par défaut du style Braze dans votre `styles.xml` pour inclure des références à la famille de polices.

Par exemple, la substitution de styles suivants utiliserait la famille de polices `bungee` d'en haut pour _tous les_ messages Braze dans l'application et une famille de polices différente pour _toutes les cartes_ Braze News Feed.

```
<style name="Braze.InAppMessage">
  <item name="android:fontFamily">@font/bungee_font_family</item>
  <item name="fontFamily">@font/bungee_font_family</item>
</style>

<style name="Braze.Cards">
  <item name="android:fontFamily">@font/another_custom_font_family</item>
  <item name="fontFamily">@font/another_custom_font_family</item>
</style>
```

{% alert warning %}
  Les attributs de style `android:fontFamily` et `fontFamily` doivent être configurés pour maintenir la compatibilité entre toutes les versions du SDK.
{% endalert %}

[1]: https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml.html
[2]: https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml.html#font-family
[3]: https://fonts.google.com/specimen/Bungee+Shade
