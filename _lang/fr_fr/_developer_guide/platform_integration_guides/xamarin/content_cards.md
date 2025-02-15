---
nav_title: Cartes de contenu
article_title: Cartes de contenu pour Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
channel: content cards
page_order: 3
description: "Cet article de référence couvre les directives d’implémentation des cartes de contenu pour la plateforme Xamarin."

---

# Intégration d’une carte de contenu

> Découvrez comment configurer les cartes de contenu iOS, Android et FireOS pour la plateforme Xamarin.

Le SDK Braze comprend un flux de cartes par défaut pour vous permettre de vous lancer dans les cartes de contenu. Le flux de cartes par défaut inclus avec le SDK Braze traitera tous les suivis d’analyse, les rejets et le rendu des cartes de contenu d’un utilisateur.

Pour savoir comment intégrer les cartes de contenu dans votre application Xamarin, consultez notre [guide d'intégration Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/data_models/) et notre [guide d'intégration iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/integration/).

## Conditions préalables

Pour utiliser cette fonctionnalité, vous devrez [intégrer le SDK Braze pour la plateforme Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/).

## Méthodes de carte de contenu

Vous pouvez utiliser ces méthodes supplémentaires pour créer un flux de cartes de contenu personnalisé dans votre application :

| Méthode                                   | Description                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `requestContentCardsRefresh()`           | Demande les dernières cartes de contenu au serveur Braze SDK.                                           |
| `getContentCards()`                      | Récupère les cartes de contenu du SDK Braze Cela renverra la dernière liste de cartes du serveur. |
| `logContentCardClicked(cardId)`          | Enregistre un clic pour l’ID de carte de contenu donné. Cette méthode est uniquement utilisée pour les analyses.                    |
| `logContentCardImpression(cardId)`       | Enregistre une impression pour l’ID de carte de contenu donné.                                                      |
| `logContentCardDismissed(cardId)`        | Enregistre un rejet pour l’ID de carte de contenu donné.                                                        |

## Modèle de données de la carte de contenu

Le SDK Braze Xamarin comporte trois types de cartes de contenu uniques qui partagent un modèle de base : **bannière**, **image légendée** et **classique**. Chaque type hérite des propriétés communes d’un modèle de base et possède les propriétés supplémentaires suivantes.

### Propriétés du modèle de carte de contenu de base

|Propriété           | Description                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------------------|
|`idString`         | L'ID de la carte est défini par Braze.                                                                                            |
|`created`          | L’horodatage UNIX du moment de création de la carte depuis Braze.                                                             |
|`expiresAt`        | L’horodatage UNIX du moment d’expiration de la carte. Lorsque la valeur est inférieure à 0, cela signifie que la carte n'expire jamais.      |
|`viewed`           | Si la carte est lue ou non par l'utilisateur. Ceci ne permet pas d'enregistrer les analyses.                                           |
|`clicked`          | Si la carte a été cliquée par l'utilisateur.                                                                         |
|`pinned`           | Détermine si la carte est épinglée.                                                                                            |
|`dismissed`        | Détermine si l’utilisateur a rejeté cette carte. Marquer comme rejetée une carte qui l'a déjà été n'est pas possible. |
|`dismissible`      | Détermine si la carte peut être ou non rejetée par l’utilisateur.                                                                           |
|`urlString`        | (Facultatif) Chaîne de caractères URL associée à l'action de clic sur la carte.                                                       |
|`openUrlInWebView` | Indique si les URL de cette carte doivent être ouvertes dans le WebView de Braze ou non.                                                 |
|`isControlCard`    | Si cette carte est une carte de contrôle. Les cartes de contrôle ne doivent pas être montrées à l'utilisateur.                                |
|`extras`           | Mappage des suppléments clé-valeur pour cette carte.                                                                             |
|`isTest`           | Que cette carte soit une carte de test.                                                                                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour une référence complète de la carte de base, consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct).

### Propriétés du modèle de carte de contenu de bannière

Les cartes de bannière sont des images cliquables et de taille réelle.

|Propriété           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | L’URL de l’image de la carte.                                                                                      |
|`imageAspectRatio` | Le rapport hauteur/largeur de l'image de la carte. Il est censé servir d'indice avant que le chargement de l'image ne soit terminé. Veuillez noter que la propriété peut ne pas être fournie dans certaines circonstances. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour une référence complète de la carte bannière, consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct) (désormais renommée en image uniquement).

### Image légendée des propriétés du modèle de cartes de contenu

Les cartes d'images légendées sont des images cliquables en taille réelle accompagnées d'un texte descriptif.

|Propriété           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | L’URL de l’image de la carte.                                                                                      |
|`imageAspectRatio` | Le rapport hauteur/largeur de l'image de la carte. Il est censé servir d'indice avant que le chargement de l'image ne soit terminé. Veuillez noter que la propriété peut ne pas être fournie dans certaines circonstances. |
|`title`            | Le texte du titre pour la carte.                                                                                      |
|`cardDescription`  | Texte de description de la carte.                                                                                |
|`domain`           | (Facultatif) Texte du lien pour l'URL de propriété, par exemple, `"braze.com/resources/"`. Il peut être affiché sur l’interface utilisateur de la carte pour indiquer l’action/la direction du clic sur la carte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour une référence complète de la carte d'image sous-titrée, consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct).

### Propriétés du modèle de carte de contenu classique

Les cartes classiques comportent un titre, une description et une image facultative à gauche du texte.

|Propriété           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | (Facultatif) L'URL de l'image de la carte.                                                                           |
|`title`            | Le texte du titre pour la carte.                                                                                      |
|`cardDescription`  | Texte de description de la carte.                                                                                |
|`domain`           | (Facultatif) Texte du lien pour l'URL de propriété, par exemple, `"braze.com/resources/"`. Il peut être affiché sur l’interface utilisateur de la carte pour indiquer l’action/la direction du clic sur la carte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour une référence complète de la carte de contenu classique (annonce textuelle), consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct). Pour une référence complète de la carte d'image classique (courte nouvelle), consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct).

## Support GIF

{% multi_lang_include wrappers/gif_support/content_cards.md %}

