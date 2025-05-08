---
nav_title: Intégration
article_title: Intégration de carte de contenu pour Android et FireOS
page_order: 0
platform: 
  - Android
  - FireOS
description: "Cet article de référence couvre l’intégration de la carte de contenu et les différents modèles de données et propriétés spécifiques à la carte disponibles pour votre application Android ou FireOS."
channel:
  - content cards
search_rank: 1
---

# Intégration des cartes de contenu

> Cet article de référence couvre l’intégration de la carte de contenu et les différents modèles de données et propriétés spécifiques à la carte disponibles pour votre application Android ou FireOS.

{% alert note %}
Lorsque vous êtes prêt à vous lancer dans la mise en œuvre et la personnalisation, consultez le [Guide de personnalisation des cartes de contenu]({{site.baseurl}}/developer_guide/customization_guides/content_cards).
{% endalert %}

Dans Android, le flux de cartes de contenu est implémenté en tant que [fragment](https://developer.android.com/guide/components/fragments.html) disponible dans le projet de l’IU Braze pour Android. Consultez la documentation [Fragments de Google ](https://developer.android.com/guide/fragments#Adding "(Documentation Android : Fragments)") pour obtenir des informations sur l'ajout d'un fragment à une activité.

La classe [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) se rafraîchira automatiquement, affichera le contenu des cartes de contenu et enregistrera l’analyse d’utilisation. Les cartes qui peuvent apparaître dans le `ContentCards` d’un utilisateur sont créés sur le tableau de bord de Braze.

## Modèle de données de cartes de contenu {#card-types-for-android}

Le modèle de données de cartes de contenu est disponible dans le SDK Android. Pour une référence complète du modèle de données des cartes de contenu, reportez-vous à la [documentation de référence du SDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html).

Braze propose quatre types de cartes de Content-Type uniques qui partagent un modèle de base : [image seule](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html), [image légendée](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html), [classique (annonce textuelle)](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) et [classique (nouvelles brèves)](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html). Chaque type hérite des propriétés communes d’un modèle de base et possède les propriétés supplémentaires suivantes.

Voir [Enregistrer les analyses]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics) pour plus d'informations sur l’abonnement aux données de cartes.

### Propriétés du modèle de carte de contenu de base {#base-card-for-android}

Le modèle de [carte de base](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) fournit un comportement fondamental pour toutes les cartes.  

|Propriété | Description |
|---|---|
|`getId()` | Renvoie l’ID de la carte défini par Braze.|
|`getViewed()` | Renvoie un booléen qui indique si la carte est lue ou non par l’utilisateur.|
|`getExtras()` | Renvoie un mappage des compléments clé-valeur de cette carte.|
|`getCreated()`  | Renvoie le timestamp unix de l'heure de création de la carte à partir de Braze.|
|`getIsPinned` | Retourne un booléen qui indique si la carte est épinglée.|
|`getOpenUriInWebView()`  | Renvoie un booléen qui indique si Uris devrait être ouvert pour cette carte <br> dans Braze WebView, ou non.|
|`getExpiredAt()` | Récupère la date d’expiration de la carte.|
|`getIsRemoved()` | Renvoie un booléen qui reflète si l’utilisateur final a rejeté cette carte.|
|`getIsDismissible()`  | Retourne un booléen qui indique si la carte est épinglée.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriétés de la carte image seulement {#banner-image-card-for-android}

Les [cartes avec image seulement](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) sont des images cliquables en taille réelle.

|Propriété | Description |
|---|---|
|`getImageUrl()` | Renvoie l’URL de l’image de la carte.|
|`getUrl()` | Renvoie l’URL qui sera ouverte après avoir cliqué sur la carte. Il peut s’agir d’une URL http(s) ou d’une URL de protocole.|
|`getDomain()` | Renvoie le texte de lien pour l’URL de propriété.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriétés de carte image sous-titrée {#captioned-image-card-for-android}

Les [cartes d'images légendées](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) sont des images cliquables en taille réelle accompagnées d'un texte descriptif.

|Propriété | Description |
|---|---|
|`getImageUrl()` | Renvoie l’URL de l’image de la carte.|
|`getTitle()` | Renvoie le texte du titre de la carte.|
|`getDescription()` | Renvoie le texte du corps de la carte.|
|`getUrl()` | Renvoie l’URL qui sera ouverte après avoir cliqué sur la carte. Il peut s’agir d’une URL http(s) ou d’une URL de protocole.|
|`getDomain()` | Renvoie le texte de lien pour l’URL de propriété. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propriétés de la carte classique {#text-Announcement-card-for-android}

Une carte classique sans image incluse donnera lieu à un [faire-part textuel](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html). Si une image est incluse, vous recevrez une [petite carte d’actualités](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html).

|Propriété | Description |
|---|---|
|`getTitle()` | Renvoie le texte du titre de la carte. |
|`getDescription()` | Renvoie le texte du corps de la carte. |
|`getUrl()` | Renvoie l’URL qui sera ouverte après avoir cliqué sur la carte. Il peut s’agir d’une URL http(s) ou d’une URL de protocole. | 
|`getDomain()` | Renvoie le texte de lien pour l’URL de propriété. |
|`getImageUrl()` | Renvoie l’URL de l’image de la carte. Ceci s’applique uniquement à la carte classique d’actualités brèves. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Méthodes de carte

Tous les objets de modèle de données [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) proposent les méthodes d'analyse suivantes pour l’enregistrement des événements utilisateur sur les serveurs Braze.

|Méthode | Description |
|---|---|
|`logImpression()` | Enregistrer manuellement une impression sur Braze pour une carte particulière. |
|`logClick()` | Enregistrer manuellement un clic sur Braze pour une carte particulière. |
|`setIsDismissed()` | Enregistrer manuellement un rejet sur Braze pour une carte particulière. Si une carte est déjà marquée comme étant rejetée, elle ne peut pas être marquée comme étant de nouveau rejetée. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

