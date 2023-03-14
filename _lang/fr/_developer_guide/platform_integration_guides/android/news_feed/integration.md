---
nav_title: Intégration
article_title: Intégration du fil d'actualité pour Android et FireOS
page_order: 1.2
platform: 
  - Android
  - FireOS
description: "Cet article couvre différents types de cartes de fil d'actualité, les différentes propriétés spécifiques à la carte disponibles et un exemple d’intégration personnalisé pour votre application Android ou FireOS."
channel:
  - fil d’actualité
  
---

# Intégration du fil d’actualité

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu - il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

Dans Android, le fil d'actualité est implémenté en tant que [fragment][2] disponible dans le projet de l’IU Braze pour Android. Consultez la [documentation Google concernant les fragments][3] pour plus d’informations sur l’ajout d’un fragment à une activité.

La classe `BrazeFeedFragment` se rafraîchira automatiquement, affichera le contenu du fil d'actualité et enregistrera l’analytique d’utilisation. Les cartes qui peuvent apparaître dans le fil d'actualité d’un utilisateur sont définies sur le tableau de bord de Braze.

## Types de cartes

Braze possède cinq types de cartes uniques : image de bannière, image sous-titrée, annonce textuelle et actualités courtes. Chaque type hérite des propriétés communes d’un modèle de base et possède les propriétés supplémentaires suivantes.

### Propriétés du modèle de carte de base

Le modèle de [carte de base][29] fournit le comportement fondamental pour toutes les cartes.  

|Propriété|Description|
|---|---|
| `getId()` | Renvoie l’ID de la carte défini par Braze. |
| `getViewed()` | Renvoie un booléen qui indique si la carte est lue ou non par l’utilisateur. |
| `getExtras()` | Renvoie un mappage des compléments clé-valeur de cette carte. |
| `setViewed(boolean)` | Définit le champ affiché d’une carte. |
| `getCreated()` | Renvoie le timestamp Unix du moment de création de la carte depuis le tableau de bord de Braze. |
| `getUpdated()` | Renvoie le timestamp Unix du moment de la dernière mise à jour de la carte depuis le tableau de bord de Braze. |
| `getCategories()` | Renvoie la liste des catégories attribuées à la carte. `ABKCardCategoryNoCategory` sera affecté aux cartes sans catégorie. |
| `isInCategorySet(EnumSet)` | Renvoie « vrai » si la carte appartient à l’ensemble de catégories donné. |
{: .reset-td-br-1 .reset-td-br-2}

### Propriétés de la carte image de bannière

Les [cartes image de bannière][30] sont des images à taille réelle cliquables.

|Propriété|Description|
|---|---|
| `getImageUrl()` | Renvoie l’URL de l’image de la carte. |
| `getUrl()` | Renvoie l’URL qui sera ouverte après avoir cliqué sur la carte. Il peut s’agir d’une URL HTTP ou HTTPS ou d’une URL de protocole. |
| `getDomain()` | Renvoie le texte de lien pour l’URL de propriété. |
{: .reset-td-br-1 .reset-td-br-2}

### Propriétés de carte image sous-titrée

Les [cartes images sous-titrées][31] sont des images à taille réelle cliquables accompagnées par un texte descriptif.

|Propriété|Description|
|---|---|
| `getImageUrl()` | Renvoie l’URL de l’image de la carte. |
| `getTitle()` | Renvoie le texte du titre de la carte. |
| `getDescription()` | Renvoie le texte du corps de la carte. |
| `getUrl()` | Renvoie l’URL qui sera ouverte après avoir cliqué sur la carte.  Il peut s’agir d’une URL HTTP ou HTTPS ou d’une URL de protocole. |
| `getDomain()` | Renvoie le texte de lien pour l’URL de propriété. |
{: .reset-td-br-1 .reset-td-br-2}

### Propriétés de la carte d’annonce textuelle (image sous-titrée sans image)

Les [cartes d’annonce textuelle][32] sont des cartes cliquables contenant un texte descriptif.

|Propriété|Description|
|---|---|
| `getTitle()` | Renvoie le texte du titre de la carte. |
| `getDescription()` | Renvoie le texte du corps de la carte. |
| `getUrl()` | Renvoie l’URL qui sera ouverte après avoir cliqué sur la carte. Il peut s’agir d’une URL HTTP ou HTTPS ou d’une URL de protocole. |
| `getDomain()` | Renvoie le texte de lien pour l’URL de propriété. |
{: .reset-td-br-1 .reset-td-br-2}

### Propriétés de la carte d’actualités courtes

Les [cartes d’actualités courtes][33] sont des cartes cliquables avec des images et un texte descriptif qui les accompagne.

|Propriété|Description|
|---|---|
| `getImageUrl()` | Renvoie l’URL de l’image de la carte. |
| `getTitle()` | Renvoie le texte du titre de la carte. |
| `getDescription()` | Renvoie le texte du corps de la carte. |
| `getUrl()` | Renvoie l’URL qui sera ouverte après avoir cliqué sur la carte. Il peut s’agir d’une URL HTTP ou HTTPS ou d’une URL de protocole. |
| `getDomain()` | Renvoie le texte de lien pour l’URL de propriété. |
{: .reset-td-br-1 .reset-td-br-2}

## Analytique de session

Les fragments d’IU Android ne suivent pas automatiquement l’analytique de session. Pour s’assurer que les sessions sont [correctement suivies][4], appelez `IBraze.openSession()` lorsque votre application est ouverte.

## Liaison

La liaison au fil d'actualité à partir d’un message in-app doit être activée en enregistrant le `BrazeFeedActivity` dans votre `AndroidManifest.xml`.

## Intégration de fil personnalisé

Si vous souhaitez afficher le fil de manière entièrement personnalisée, il est possible de le faire en utilisant vos propres vues remplies avec les données de nos modèles. Pour obtenir les modèles de fil d'actualité de Braze, vous devrez vous abonner aux mises à jour de fil d'actualité et utiliser les données du modèle qui en résulte pour renseigner vos vues. Vous devrez également enregistrer l’analytique des objets du modèle lorsque les utilisateurs interagissent avec vos vues.

### Partie 1 : S’abonner aux mises à jour du fil

Tout d’abord, déclarez une variable privée dans votre classe de fil personnalisée pour contenir votre abonné :

```java
// subscriber variable
private IEventSubscriber<FeedUpdatedEvent> mFeedUpdatedSubscriber;
```

Ensuite, ajoutez le code suivant pour vous abonner aux mises à jour de fil d'actualité de Braze, généralement à l’intérieur de vos activités de fil personnalisé `Activity.onCreate()` :

```java
// Remove the old subscription first
Braze.getInstance(context).removeSingleSubscription(mFeedUpdatedSubscriber, FeedUpdatedEvent.class);
mFeedUpdatedSubscriber = new IEventSubscriber<FeedUpdatedEvent>() {
  @Override
  public void trigger(final FeedUpdatedEvent event) {
    // This list of Card objects included in the FeedUpdatedEvent should be used to populate your News Feed views.
    List<Card> cards = event.getFeedCards();
    // your logic here
  }
};
Braze.getInstance(context).subscribeToFeedUpdates(mFeedUpdatedSubscriber);

// Request a refresh of feed data
Braze.getInstance(context).requestFeedRefresh();
```

Nous vous recommandons également de vous désabonnez lorsque votre activité personnalisée n’est plus visible. Ajoutez le code suivant à la méthode de cycle de vie `onDestroy()` de votre activité :

```
Braze.getInstance(context).removeSingleSubscription(mFeedUpdatedSubscriber, FeedUpdatedEvent.class);
```

### Partie 2 : Enregistrer l’analytique

Lorsque vous utilisez des vues personnalisées, vous devez enregistrer manuellement l’analytique, car elle ne peut être gérée automatiquement que lorsque vous utilisez des vues Braze.

Pour enregistrer un affichage du fil, appelez [`Braze.logFeedDisplayed()`][6].

Pour enregistrer une impression ou cliquer sur une carte, appelez [`Card.logClick()`][7] et [`Card.logImpression()`][8] respectivement.

[36]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/get-extras.html
[2]: http://developer.android.com/guide/components/fragments.html
[3]: https://developer.android.com/guide/fragments#Adding "Android Documentation: Fragments"
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/
[6]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-feed-displayed.html
[7]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html
[8]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/card_types/#card-types
[29]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html
[30]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-banner-image-card/index.html
[31]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html
[32]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html
[33]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html
