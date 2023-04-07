---
nav_title: Intégration
article_title: Intégration de carte de contenu pour Android et FireOS
page_order: 0
platform: 
  - Android
  - FireOS
description: "Cet article de référence couvre l’intégration de la carte de contenu et les différents modèles de données et propriétés spécifiques à la carte disponibles pour votre application Android ou FireOS."
channel:
  - cartes de contenu
search_rank: 1
---

# Intégration des cartes de contenu

Dans Android, le flux de cartes de contenu est implémenté en tant que [fragment][2] disponible dans le projet de l’IU Braze pour Android. Consultez les [fragments de Google][3] pour plus d’informations sur l’ajout d’un fragment à une activité.

La classe [`ContentCardsFragment`][4] se rafraîchira automatiquement, affichera le contenu des cartes de contenu et enregistrera l’analytique d’utilisation. Les cartes qui peuvent apparaître dans le `ContentCards` d’un utilisateur sont créés sur le tableau de bord de Braze.

## Modèle de données de cartes de contenu

Le modèle de données de cartes de contenu est disponible dans le SDK Android.

## Modèle de carte de contenu {#card-types-for-android}

Braze possède trois types de cartes de contenu uniques qui partagent un modèle de base : bannière, image sous-titrée et classique. Chaque type hérite des propriétés communes d’un modèle de base et possède les propriétés supplémentaires suivantes.

### Propriétés du modèle de carte de contenu de base {#base-card-for-android}

Le modèle de [carte de base][29] fournit le comportement fondamental pour toutes les cartes.  

|Propriété | Description |
|---|---|
|`getId()` | Renvoie l’ID de la carte défini par Braze.|
|`getViewed()` | Renvoie un booléen qui indique si la carte est lue ou non par l’utilisateur.|
|`getExtras()` | Renvoie un mappage des compléments clé-valeur de cette carte.|
|`getCreated()`  | Renvoie le timestamp Unix du moment de création de la carte depuis Braze.|
|`getIsPinned` | Renvoie un booléen qui indique si la carte est épinglée.|
|`getOpenUriInWebView()`  | Renvoie un booléen qui indique si Uris devrait être ouvert pour cette carte <br> dans WebView de Braze, ou non.|
|`getExpiredAt()` | Récupère la date d’expiration de la carte.|
|`getIsRemoved()` | Renvoie un booléen qui reflète si l’utilisateur final a rejeté cette carte.|
|`getIsDismissible()`  | Renvoie un booléen qui indique si la carte est épinglée.|
{: .reset-td-br-1 .reset-td-br-2}

### Propriétés de la carte image de bannière {#banner-image-card-for-android}

Les [cartes image de bannière][30] sont des images à taille réelle cliquables.

|Propriété | Description |
|---|---|
|`getImageUrl()` | Renvoie l’URL de l’image de la carte.|
|`getUrl()` | Renvoie l’URL qui sera ouverte après avoir cliqué sur la carte. Il peut s’agir d’une URL http(s) ou d’une URL de protocole.|
|`getDomain()` | Renvoie le texte de lien pour l’URL de propriété.|
{: .reset-td-br-1 .reset-td-br-2}

### Propriétés de carte image sous-titrée {#captioned-image-card-for-android}

Les [cartes images sous-titrées][31] sont des images à taille réelle cliquables accompagnées par un texte descriptif.

|Propriété | Description |
|---|---|
|`getImageUrl()` | Renvoie l’URL de l’image de la carte.|
|`getTitle()` | Renvoie le texte du titre de la carte.|
|`getDescription()` | Renvoie le texte du corps de la carte.|
|`getUrl()` | Renvoie l’URL qui sera ouverte après avoir cliqué sur la carte. Il peut s’agir d’une URL http(s) ou d’une URL de protocole.|
|`getDomain()` | Renvoie le texte de lien pour l’URL de propriété. |
{: .reset-td-br-1 .reset-td-br-2}

### Propriétés de la carte classique {#text-Announcement-card-for-android}

Une carte classique sans image incluse entraînera une [carte d’annonce de texte][32]. Si une image est incluse, vous recevrez une [petite carte d’actualités][41].

|Propriété | Description |
|---|---|
|`getTitle()` | Renvoie le texte du titre de la carte. |
|`getDescription()` | Renvoie le texte du corps de la carte. |
|`getUrl()` | Renvoie l’URL qui sera ouverte après avoir cliqué sur la carte. Il peut s’agir d’une URL http(s) ou d’une URL de protocole. | 
|`getDomain()` | Renvoie le texte de lien pour l’URL de propriété. |
|`getImageUrl()` | Renvoie l’URL de l’image de la carte. Ceci s’applique uniquement à la carte classique d’actualités brèves. |
{: .reset-td-br-1 .reset-td-br-2}

## Méthodes de carte

Tous les objets de modèle de données `Card` proposent les méthodes d’analytique suivantes pour l’enregistrement des événements utilisateur sur les serveurs Braze.

|Méthode | Description |
|---|---|
|`logImpression()` | Enregistrer manuellement une impression sur Braze pour une carte particulière. |
|`logClick()` | Enregistrer manuellement un clic sur Braze pour une carte particulière. |
|`setIsDismissed()` | Enregistrer manuellement un rejet sur Braze pour une carte particulière. Si une carte est déjà marquée comme étant rejetée, elle ne peut pas être marquée comme étant de nouveau rejetée. |
{: .reset-td-br-1 .reset-td-br-2}

## Cartes de contenu personnalisées {#fully-custom-content-card-display-for-android}

Si vous souhaitez afficher les cartes de contenu de manière entièrement personnalisée, il est possible de le faire en utilisant vos propres vues remplies avec les données de nos modèles. Pour obtenir les modèles de cartes de contenu de Braze, vous devrez vous abonner aux mises à jour de cartes de contenu et utiliser les données du modèle qui en résultent pour renseigner vos vues. Vous devrez également enregistrer l’analytique des objets du modèle lorsque les utilisateurs interagissent avec vos vues.

### Partie 1 : S’abonner aux mises à jour des cartes de contenu

Tout d’abord, déclarez une variable privée dans votre classe personnalisée pour contenir votre abonné :

{% tabs %}
{% tab JAVA %}

```java
// subscriber variable
private IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
private var mContentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
```

{% endtab %}
{% endtabs %}

Ensuite, ajoutez le code suivant pour vous abonner aux mises à jour de cartes de contenu de Braze, généralement à l’intérieur de vos activités personnalisées de carte de contenu `Activity.onCreate()` :

{% tabs %}
{% tab JAVA %}

```java
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
mContentCardsUpdatedSubscriber = new IEventSubscriber<ContentCardsUpdatedEvent>() {
    @Override
    public void trigger(ContentCardsUpdatedEvent event) {
        // List of all Content Cards
        List<Card> allCards = event.getAllCards();

        // Your logic below
    }
};
Braze.getInstance(context).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber);
Braze.getInstance(context).requestContentCardsRefresh(true);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
mContentCardsUpdatedSubscriber = IEventSubscriber { event ->
  // List of all Content Cards
  val allCards = event.allCards

  // Your logic below
}
Braze.getInstance(context).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh(true)
```

{% endtab %}
{% endtabs %}

Nous vous recommandons également de vous désabonner lorsque votre activité personnalisée n’est plus visible. Ajoutez le code suivant à la méthode de cycle de vie `onDestroy()` de votre activité :

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
```

{% endtab %}
{% endtabs %}

### Partie 2 : Enregistrer l’analytique

Lorsque vous utilisez des vues personnalisées, vous devez enregistrer manuellement l’analytique, car elle ne peut être gérée automatiquement que lorsque vous utilisez des vues Braze.

Pour enregistrer une impression ou cliquer sur une carte, appelez [`Card.logClick()`][7] ou [`Card.logImpression()`][8] respectivement.

Pour les campagnes utilisant des cartes de contrôle pour les tests A/B, vous pouvez utiliser [`Card.isControl()`][55] pour déterminer si une carte sera vide et utilisée uniquement à des fins de suivi.

### Rejeter manuellement une carte de contenu

Vous pouvez enregistrer ou définir manuellement une carte de contenu particulière comme étant « rejetée » au niveau de Braze avec [`setIsDismissed`][57].

Si une carte est déjà marquée comme étant rejetée, elle ne peut pas être marquée comme étant de nouveau rejetée.

[7]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html
[8]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html
[55]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/is-control.html
[57]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html#-1644350493%2FProperties%2F-1725759721
[29]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html
[30]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-banner-image-card/index.html
[31]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html
[32]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html
[41]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html
[2]: https://developer.android.com/guide/components/fragments.html
[3]: https://developer.android.com/guide/fragments#Adding "Android Documentation: Fragments"
[4]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html
