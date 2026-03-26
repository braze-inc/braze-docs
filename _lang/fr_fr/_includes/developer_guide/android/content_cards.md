## Conditions préalables

Avant de pouvoir utiliser les cartes de contenu Braze, il est nécessaire d'effectuer l'intégration du [SDK Android Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android) dans votre application. Cependant, aucune configuration supplémentaire n'est nécessaire.

## Fragments Google

Dans Android, le flux de cartes de contenu est implémenté en tant que [fragment](https://developer.android.com/guide/components/fragments.html) disponible dans le projet de l’IU Braze pour Android. La classe [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) se rafraîchira automatiquement, affichera le contenu des cartes de contenu et enregistrera l’analyse d’utilisation. Les cartes qui peuvent apparaître dans le `ContentCards` d’un utilisateur sont créés sur le tableau de bord de Braze.

Pour savoir comment ajouter un fragment à une activité, veuillez consulter [la documentation de Google sur les fragments](https://developer.android.com/guide/fragments#Adding).

## Types et caractéristiques des cartes

Le modèle de données Content Cards est disponible dans le SDK Android et propose les types de cartes de contenu uniques suivants. Chaque type partage un modèle de base, ce qui leur permet d'hériter des propriétés communes du modèle de base, en plus d'avoir leurs propres propriétés uniques. Pour obtenir la documentation de référence complète, veuillez consulter [`com.braze.models.cards`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html).

### Modèle de carte de base {#base-card-for-android}

Le modèle de [carte de base](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) fournit un comportement fondamental pour toutes les cartes.  

|Propriété | Description |
|---|---|
|`getId()` | Renvoie l’ID de la carte défini par Braze.|
|`getViewed()` | Renvoie un booléen qui indique si la carte est lue ou non par l’utilisateur.|
|`getExtras()` | Renvoie un mappage des compléments clé-valeur de cette carte.|
|`getCreated()`  | Renvoie le timestamp unix de l'heure de création de la carte à partir de Braze.|
|`isPinned` | Retourne un booléen qui indique si la carte est épinglée.|
|`getOpenUriInWebView()`  | Renvoie un booléen qui indique si Uris devrait être ouvert pour cette carte <br> dans Braze WebView, ou non.|
|`getExpiredAt()` | Récupère la date d’expiration de la carte.|
|`isRemoved()` | Renvoie un booléen qui reflète si l’utilisateur final a rejeté cette carte.|
|`isDismissibleByUser()`  | Renvoie une valeur booléenne indiquant si la carte peut être supprimée par l'utilisateur.|
|`isClicked()` | Renvoie une valeur booléenne qui indique si cette carte a été cliquée.|
|`isDismissed` | Renvoie une valeur booléenne indiquant si la carte a été fermée. Veuillez définir sur`true`  pour marquer la carte comme rejetée. Si une carte est déjà marquée comme étant rejetée, elle ne peut pas être marquée comme étant de nouveau rejetée.|
|`isControl()` | Renvoie une valeur booléenne si cette carte est une carte de contrôle et ne doit pas être rendue.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Image uniquement {#banner-image-card-for-android}

Les [cartes avec image seulement](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) sont des images cliquables en taille réelle.

|Propriété | Description |
|---|---|
|`getImageUrl()` | Renvoie l’URL de l’image de la carte.|
|`getUrl()` | Renvoie l’URL qui sera ouverte après avoir cliqué sur la carte. Il peut s’agir d’une URL http(s) ou d’une URL de protocole.|
|`getDomain()` | Renvoie le texte de lien pour l’URL de propriété.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Image légendée {#captioned-image-card-for-android}

Les [cartes d'images légendées](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) sont des images cliquables en taille réelle accompagnées d'un texte descriptif.

|Propriété | Description |
|---|---|
|`getImageUrl()` | Renvoie l’URL de l’image de la carte.|
|`getTitle()` | Renvoie le texte du titre de la carte.|
|`getDescription()` | Renvoie le texte du corps de la carte.|
|`getUrl()` | Renvoie l’URL qui sera ouverte après avoir cliqué sur la carte. Il peut s’agir d’une URL http(s) ou d’une URL de protocole.|
|`getDomain()` | Renvoie le texte de lien pour l’URL de propriété. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Classique {#text-Announcement-card-for-android}

Une carte classique sans image incluse donnera lieu à un [faire-part textuel](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html). Si une image est incluse, vous recevrez une [petite carte d’actualités](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html).

|Propriété | Description |
|---|---|
|`getTitle()` | Renvoie le texte du titre de la carte. |
|`getDescription()` | Renvoie le texte du corps de la carte. |
|`getUrl()` | Renvoie l’URL qui sera ouverte après avoir cliqué sur la carte. Il peut s’agir d’une URL http(s) ou d’une URL de protocole. | 
|`getDomain()` | Renvoie le texte de lien pour l’URL de propriété. |
|`getImageUrl()` | Renvoie l’URL de l’image de la carte. Ceci s’applique uniquement à la carte classique d’actualités brèves. |
|`isDismissed` | Renvoie une valeur booléenne indiquant si la carte a été fermée. Veuillez définir sur`true`  pour marquer la carte comme rejetée. Si une carte est déjà marquée comme étant rejetée, elle ne peut pas être marquée comme étant de nouveau rejetée. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Méthodes de carte

Tous les objets de modèle de données [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) proposent les méthodes d'analyse suivantes pour l’enregistrement des événements utilisateur sur les serveurs Braze.

|Méthode | Description |
|---|---|
|`logImpression()` | Enregistrer manuellement une impression sur Braze pour une carte particulière. |
|`logClick()` | Enregistrer manuellement un clic sur Braze pour une carte particulière. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
