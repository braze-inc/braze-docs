---
nav_title: Intégration
article_title: Intégration du fil d’actualité pour Android et FireOS
page_order: 1.2
platform: 
  - Android
  - FireOS
description: "Cet article de référence couvre différents types de cartes de fil d’actualité, les différentes propriétés spécifiques à la carte disponibles et un exemple d’intégration personnalisé pour votre application Android ou FireOS."
channel:
  - news feed
  
---

# Intégration du fil d’actualité

> Cet article de référence couvre différents types de cartes de fil d’actualité, les différentes propriétés spécifiques à la carte disponibles et un exemple d’intégration personnalisé pour votre application Android ou FireOS.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Sous Android, le fil d'actualité est mis en œuvre sous la forme d'un [fragment](http://developer.android.com/guide/components/fragments.html) disponible dans le projet Android UI de Braze. Reportez-vous à la [documentation de Google sur les fragmentsAndroid](https://developer.android.com/guide/fragments#Adding "Documentation : Fragments") pour obtenir des informations sur l'ajout d'un fragment à une activité.

La classe `BrazeFeedFragment` se rafraîchira automatiquement, affichera le contenu du fil d’actualité et enregistrera l’analyse d’utilisation. Les cartes qui peuvent apparaître dans le fil d’actualité d’un utilisateur sont définies sur le tableau de bord de Braze.

## Types de cartes

Braze possède cinq types de cartes uniques : image de bannière, image sous-titrée, annonce textuelle et actualités courtes. Chaque type hérite des propriétés communes d’un modèle de base et possède les propriétés supplémentaires suivantes.

### Propriétés du modèle de carte de base

Le modèle de [carte de base](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) fournit un comportement fondamental pour toutes les cartes.  

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
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriétés de la carte image de bannière

Les [cartes-images des bannières](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-banner-image-card/index.html) sont des images cliquables en taille réelle.

|Propriété|Description|
|---|---|
| `getImageUrl()` | Renvoie l’URL de l’image de la carte. |
| `getUrl()` | Renvoie l’URL qui sera ouverte après avoir cliqué sur la carte. Il peut s’agir d’une URL HTTP ou HTTPS ou d’une URL de protocole. |
| `getDomain()` | Renvoie le texte de lien pour l’URL de propriété. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriétés de carte image sous-titrée

Les [cartes d'images légendées](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) sont des images cliquables en taille réelle accompagnées d'un texte descriptif.

|Propriété|Description|
|---|---|
| `getImageUrl()` | Renvoie l’URL de l’image de la carte. |
| `getTitle()` | Renvoie le texte du titre de la carte. |
| `getDescription()` | Renvoie le texte du corps de la carte. |
| `getUrl()` | Renvoie l’URL qui sera ouverte après avoir cliqué sur la carte.  Il peut s’agir d’une URL HTTP ou HTTPS ou d’une URL de protocole. |
| `getDomain()` | Renvoie le texte de lien pour l’URL de propriété. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriétés de la carte d’annonce textuelle (image sous-titrée sans image)

Les [cartes d'annonce textuelles](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) sont des cartes cliquables contenant un texte descriptif.

|Propriété|Description|
|---|---|
| `getTitle()` | Renvoie le texte du titre de la carte. |
| `getDescription()` | Renvoie le texte du corps de la carte. |
| `getUrl()` | Renvoie l’URL qui sera ouverte après avoir cliqué sur la carte. Il peut s’agir d’une URL HTTP ou HTTPS ou d’une URL de protocole. |
| `getDomain()` | Renvoie le texte de lien pour l’URL de propriété. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriétés de la carte d’actualités courtes

Les [cartes d'actualités courtes](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) sont des cartes cliquables contenant des images et un texte descriptif.

|Propriété|Description|
|---|---|
| `getImageUrl()` | Renvoie l’URL de l’image de la carte. |
| `getTitle()` | Renvoie le texte du titre de la carte. |
| `getDescription()` | Renvoie le texte du corps de la carte. |
| `getUrl()` | Renvoie l’URL qui sera ouverte après avoir cliqué sur la carte. Il peut s’agir d’une URL HTTP ou HTTPS ou d’une URL de protocole. |
| `getDomain()` | Renvoie le texte de lien pour l’URL de propriété. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Analytique de session

Les fragments d’IU Android ne suivent pas automatiquement les analyses de session. Pour vous assurer que les sessions font l’objet d’un [suivi approprié]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/), appelez `IBraze.openSession()` lorsque votre application est ouverte.

## Liaison

La liaison au fil d’actualité à partir d’un message in-app doit être activée en enregistrant le `BrazeFeedActivity` dans votre `AndroidManifest.xml`.

## Intégration de fil personnalisé

Si vous souhaitez afficher le flux de manière totalement personnalisée, il est possible de le faire en utilisant vos propres vues alimentées par les données de nos modèles. Pour obtenir des modèles de fil d'actualité, vous devrez vous abonner aux mises à jour du fil d'actualité et utiliser les données du modèle résultant pour alimenter vos vues. Vous devrez également enregistrer l’analyse des objets du modèle lorsque les utilisateurs interagissent avec vos vues.

### Partie 1 : S’abonner aux mises à jour du fil

Tout d’abord, déclarez une variable privée dans votre classe de fil personnalisée pour contenir votre abonné :

```java
// subscriber variable
private IEventSubscriber<FeedUpdatedEvent> mFeedUpdatedSubscriber;
```

Ensuite, ajoutez le code suivant pour vous abonner aux mises à jour de fil d’actualité de Braze, généralement à l’intérieur de vos activités de fil personnalisé `Activity.onCreate()` :

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

Nous vous recommandons également de vous désabonner lorsque votre activité personnalisée n’est plus visible. Ajoutez le code suivant à la méthode de cycle de vie `onDestroy()` de votre activité :

```
Braze.getInstance(context).removeSingleSubscription(mFeedUpdatedSubscriber, FeedUpdatedEvent.class);
```

### Partie 2 : Enregistrer les analyses

Lorsque vous utilisez des vues personnalisées, vous devez enregistrer manuellement l’analyse, car elle ne peut être gérée automatiquement que lorsque vous utilisez des vues Braze.

Pour enregistrer un affichage du flux, appelez [`Braze.logFeedDisplayed()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-feed-displayed.html).

Pour enregistrer une impression ou cliquer sur une carte, appelez le [`Card.logClick()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html) et [`Card.logImpression()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html) respectivement.

