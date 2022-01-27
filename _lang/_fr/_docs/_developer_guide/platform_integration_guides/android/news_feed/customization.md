---
nav_title: Personnalisation
article_title: Personnalisation des fils d'actualité pour Android/FireOS
page_order: 2
platform:
  - Android
  - Pare-feu
description: "Cet article de référence couvre la façon de personnaliser votre fil d'actualité dans votre application Android."
channel:
  - fil d'actualité
---

# Personnalisation du fil d'actualité

## Default styling

Les éléments de Braze UI sont fournis avec un look et une sensation par défaut qui correspond aux directives de l'interface utilisateur standard d'Android et fournit une expérience transparente. Vous pouvez voir ces styles par défaut dans le fichier `res/values/style.xml` dans la distribution Braze SDK.

```xml
  <style name="Braze"/>
  <! - Flux -->
  <style name="Braze.Feed"/>
  <style name="Braze.Feed.List">
    <item name="android:background">@android:color/transparent</item>
    <item name="android:divider">@android:color/transparent</item>
    <item name="android:dividerHeight">16. dp</item>
    <item name="android:paddingLeft">12.5dp</item>
    <item name="android:paddingRight">5. dp</item>
    <item name="android:scrollbarStyle">outsideInset</item>
  </style>
...
  </style>
```

## Overriding styles

Si vous préférez, vous pouvez remplacer ces styles pour créer un look et une sensation qui convient mieux à votre application. Pour remplacer un style, copiez-le dans son intégralité dans le fichier `styles.xml` de votre propre projet et apportez des modifications. Le style entier doit être copié dans votre fichier local `styles.xml` pour que tous les attributs soient correctement définis.

#### Surcharge de style correcte

```xml
<style name="Braze.Feed.List">
  <item name="android:background">@color/menthe</item>
  <item name="android:cacheColorHint">@color/menthe</item>
  <item name="android:divider">@android:color/transparent</item>
  <item name="android:dividerHeight">16. dp</item>
  <item name="android:paddingLeft">12.5dp</item>
  <item name="android:paddingRight">5. dp</item>
  <item name="android:scrollbarStyle">outsideInset</item>
</style>
```

#### Surcharge de style incorrecte

```xml
<style name="Braze.Feed.List">
  <item name="android:background">@color/menthe</item>
  <item name="android:cacheColorHint">@color/menthe</item>
</style>
```

## Éléments de style de flux

Ci-dessous se trouve une description des éléments thématiques de Braze UI et de leurs noms à des fins de style :

{% gallery %}{% image_buster /assets/img_archive/Image27Theming.png %}
{% image_buster /assets/img_archive/Image28Theming.png %}
{% image_buster /assets/img_archive/Image29Theming.png %}
{% image_buster /assets/img_archive/Image30Theming.png %}{% endgallery %}

## Définir une police personnalisée

Braze permet de définir une police personnalisée en utilisant le guide de la famille de polices [][40]. Pour l'utiliser, remplacez un style pour les cartes et utilisez l'attribut `fontFamily` pour demander à Braze d'utiliser votre famille de polices personnalisée.

Par exemple, pour mettre à jour la police sur tous les titres pour les cartes d'actualités courtes, remplacez le style `Appboy.Cards.ShortNews.Title` et référencez votre famille de polices personnalisées. La valeur de l'attribut doit pointer vers une famille de polices dans votre répertoire `res/font`.

Voici un exemple tronqué avec une famille de polices personnalisées, `my_custom_font_family`, référencé sur la dernière ligne:

```
<style name="Braze.Cards.ShortNews.Title">
  <item name="android:layout_height">wrap_content</item>
...
  <item name="android:fontFamily">@font/my_custom_font_family</item>
  <item name="fontFamily">@font/my_custom_font_family</item>
</style>
```

## Définition d'un fil d'actualité personnalisé cliquez sur listener

Vous pouvez gérer manuellement les clics sur Flux d'actualités en définissant un clic sur écouteur personnalisé. Cela permet d'utiliser des cas tels que l'utilisation sélective du navigateur web natif pour ouvrir des liens Web.

### Étape 1 : Implémenter un fil d'actualités cliquer sur listener

Créez une classe qui implémente [IFeedClickActionListener][37]. Implémenter la méthode `onFeedCardClicked()` , qui sera appelée lorsque l'utilisateur clique sur une carte de flux d'actualités.

### Étape 2 : Instructez Braze pour utiliser votre lecteur de flux d'actualités cliquez sur listener

Une fois que votre `IFeedClickActionListener` est créé, appelez `AppboyFeedManager.getInstance().setFeedCardClickActionListener()` pour instructer `AppboyFeedManager` d'utiliser votre propre `IFeedClickActionListener`.

## Affichage de flux entièrement personnalisé

Si vous souhaitez afficher le flux de manière complètement personnalisée, il est possible de le faire en utilisant vos propres vues remplies de données de nos [modèles][9]. Pour obtenir des modèles Braze's News Feed, vous devrez vous abonner aux mises à jour du fil d'actualité et utiliser les données du modèle qui en résultent pour remplir vos vues. Vous devrez également enregistrer les analyses sur les objets du modèle lorsque les utilisateurs interagissent avec vos vues.

### Partie 1 : S'abonner aux mises à jour des flux

Tout d'abord, déclarez une variable privée dans votre classe de flux personnalisé pour conserver votre abonné :

```java
// variable d'abonné
privée IEventSubscriber<FeedUpdatedEvent> mFeedUpdatedSubscriber;
```

Ensuite, ajoutez le code suivant pour vous abonner aux mises à jour de flux de Braze, généralement à l'intérieur de votre activité de flux personnalisé `Activity.onCreate()`:

```java
// Supprime d'abord l'ancien abonnement
Braze.getInstance(context).removeSingleSingleSubscription(mFeedUpdatedSubscriber, FeedUpdatedEvent. laiton);
mFeedUpdatedSubscriber = new IEventSubscriber<FeedUpdatedEvent>() {
  @Override
  public void trigger(final FeedUpdatedEvent event) {
    // Cette liste d'objets de carte inclus dans le FeedUpdatedEvent devrait être utilisée pour remplir vos vues de flux d'actualités.
    Listez<Card> cartes = event.getFeedCards();
    // votre logique ici
  }
};
Braze.getInstance(contexte). ubscribeToFeedUpdates(mFeedUpdatedSubscriber);

// Demande un rafraîchissement des données du flux
Braze.getInstance(context).requestFeedRefresh();
```

Nous vous recommandons également de vous désabonner lorsque votre activité de flux personnalisé se déconnecte. Add the following code to your activity's `onDestroy()` lifecycle method:

```
Braze.getInstance(context).removeSingleSingleSubscription(mFeedUpdatedSubscriber, FeedUpdatedEvent.class);
```

### Partie 2 : Analyses de la journalisation

Lorsque vous utilisez des vues personnalisées, vous devrez également enregistrer manuellement les analytiques, car les analyses ne sont gérées automatiquement que lorsque vous utilisez les vues Braze.

Pour enregistrer un affichage du flux, appelez [`Appboy.logFeedDisplayed()`][6].

Pour enregistrer une impression ou cliquer sur une carte, appelez [`Card.logClick()`][7] et [`Card.logImpression()`][8] respectivement.
[18]: {% image_buster /assets/img_archive/Image27Theming.png %} "Flux Android" [19]: {% image_buster /assets/img_archive/Image28Theming. ng %} "Cartes Android" [20]: {% image_buster /assets/img_archive/Image29Theming.png %} "Android Empty" [21]: {% image_buster /assets/img_archive/Image30Theming.png %} "Erreur réseau Android"


[6]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy/-appboy/log-feed-displayed.html
[7]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-card/log-click.html
[8]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.models.cards/-card/log-impression.html
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/card_types/#card-types
[37]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/java/com/appboy/ui/feed/listeners/IFeedClickActionListener.java
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization
