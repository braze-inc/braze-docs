{% multi_lang_include developer_guide/prerequisites/android.md %}

## Utilisation de polices personnalisées

### Étape 1 : Créer une famille de polices

Voici un exemple de définition d'une famille de polices personnalisée à l'aide du [guide des familles de polices](https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml.html#font-family). Pour cet exemple, nous utilisons la [police Bungee Shade](https://fonts.google.com/specimen/Bungee+Shade).

```html
<?xml version="1.0" encoding="utf-8"?>
<font-family xmlns:android="http://schemas.android.com/apk/res/android"
             xmlns:app="http://schemas.android.com/apk/res-auto">

  <!--Note: You must declare both sets of attributes
      so that your fonts load on devices running Android 8.0 (API level 26) or lower.
      See https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml.html -->

  <font android:fontStyle="normal"
        android:fontWeight="400"
        android:font="@font/bungeeshade"

        app:fontStyle="normal"
        app:fontWeight="400"
        app:font="@font/bungeeshade"/>
</font-family>
```

Après avoir stocké la définition de la famille de polices dans `/res/font/bungee_font_family.xml`, nous pouvons nous y référer dans le XML en tant que `@font/bungee_font_family`.

### Étape 2 : Référencez votre famille de polices

Maintenant que la famille de polices est créée, vous pouvez substituer le style Braze par défaut dans votre `styles.xml` pour inclure des références à la famille de polices.

Par exemple, la substitution de styles suivante utiliserait la famille de polices `bungee` pour tous les messages in-app Braze.

```html
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
Les deux attributs de style `android:fontFamily` et `fontFamily` doivent être définis pour maintenir la compatibilité entre toutes les versions de SDK.
{% endalert %}
