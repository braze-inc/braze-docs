## À propos des cartes de contenu Xamarin

Le SDK Xamarin de Braze inclut un flux de cartes par défaut pour vous permettre de démarrer avec les cartes de contenu. Le flux de cartes par défaut inclus avec le SDK Braze traitera tous les suivis d’analyse, les rejets et le rendu des cartes de contenu d’un utilisateur.

{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## Types de cartes et propriétés

Le SDK Xamarin de Braze dispose de trois types de cartes de contenu uniques qui partagent un modèle de base : [Bannière](#xamarin_banner), [Image légendée](#xamarin_captioned-image) et [Classique](#xamarin_classic). Chaque type hérite des propriétés communes d’un modèle de base et possède les propriétés supplémentaires suivantes.

### Modèle de carte de base

|Propriété           | Description                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------------------|
|`idString`         | L'ID de la carte est défini par Braze.                                                                                            |
|`created`          | L’horodatage UNIX du moment de création de la carte depuis Braze.                                                             |
|`expiresAt`        | L’horodatage UNIX du moment d’expiration de la carte. Lorsque la valeur est inférieure à 0, cela signifie que la carte n'expire jamais.      |
|`viewed`           | Si la carte est lue ou non par l'utilisateur. Ceci ne permet pas d'enregistrer les analyses.                                           |
|`clicked`          | Si la carte a été cliquée par l'utilisateur.                                                                         |
|`pinned`           | Si la carte est épinglée.                                                                                            |
|`dismissed`        | Indique si l'utilisateur a fermé la carte de contenu. Marquer comme rejetée une carte qui l'a déjà été n'est pas possible. |
|`dismissible`      | Détermine si la carte peut être ou non rejetée par l’utilisateur.                                                                           |
|`urlString`        | (Facultatif) Chaîne de caractères de l'URL associée à l'action de clic sur la carte.                                                       |
|`openUrlInWebView` | Indique si les URL de cette carte doivent être ouvertes dans le WebView de Braze ou non.                                                 |
|`isControlCard`    | Si cette carte est une carte de contrôle. Les cartes de contrôle ne doivent pas être montrées à l'utilisateur.                                |
|`extras`           | Mappage des suppléments clé-valeur pour cette carte.                                                                             |
|`isTest`           | Que cette carte soit une carte de test.                                                                                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour une référence complète de la carte de base, consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct).

### Bannière

Les cartes de bannière sont des images cliquables et de taille réelle.

|Propriété           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | L’URL de l’image de la carte.                                                                                      |
|`imageAspectRatio` | Le rapport hauteur/largeur de l'image de la carte. Il sert d'indice avant que le chargement de l'image ne soit terminé. Veuillez noter que la propriété peut ne pas être fournie dans certaines circonstances. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour une référence complète de la carte bannière, consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct) (désormais renommée en image uniquement).

### Image avec légende

Les cartes d'images légendées sont des images cliquables en taille réelle accompagnées d'un texte descriptif.

|Propriété           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | L’URL de l’image de la carte.                                                                                      |
|`imageAspectRatio` | Le rapport hauteur/largeur de l'image de la carte. Il sert d'indice avant que le chargement de l'image ne soit terminé. Veuillez noter que la propriété peut ne pas être fournie dans certaines circonstances. |
|`title`            | Le texte du titre pour la carte.                                                                                      |
|`cardDescription`  | Texte de description de la carte.                                                                                |
|`domain`           | (Facultatif) Texte du lien pour l'URL de propriété, par exemple, `"braze.com/resources/"`. Il peut être affiché sur l’interface utilisateur de la carte pour indiquer l’action/la direction du clic sur la carte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour une référence complète de la carte d'image sous-titrée, consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct).

### Classique

Les cartes classiques comportent un titre, une description et une image facultative à gauche du texte.

|Propriété           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | (Facultatif) L'URL de l'image de la carte.                                                                           |
|`title`            | Le texte du titre pour la carte.                                                                                      |
|`cardDescription`  | Texte de description de la carte.                                                                                |
|`domain`           | (Facultatif) Texte du lien pour l'URL de propriété, par exemple, `"braze.com/resources/"`. Il peut être affiché sur l’interface utilisateur de la carte pour indiquer l’action/la direction du clic sur la carte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour une référence complète de la carte de contenu classique (annonce textuelle), consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct). Pour une référence complète de la carte d'image classique (courte nouvelle), consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct).

## Méthodes de carte

Vous pouvez utiliser ces méthodes supplémentaires pour créer un flux de cartes de contenu personnalisé dans votre application :

| Méthode                                   | Description                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `requestContentCardsRefresh()`           | Demande les dernières cartes de contenu au serveur Braze SDK.                                           |
| `getContentCards()`                      | Récupère les cartes de contenu du SDK Braze Cela renverra la dernière liste de cartes du serveur. |
| `logContentCardClicked(cardId)`          | Enregistre un clic pour l’ID de carte de contenu donné. Cette méthode est uniquement utilisée pour les analyses.                    |
| `logContentCardImpression(cardId)`       | Enregistre une impression pour l’ID de carte de contenu donné.                                                      |
| `logContentCardDismissed(cardId)`        | Enregistre un rejet pour l’ID de carte de contenu donné.                                                        |
