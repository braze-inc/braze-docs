## À propos des cartes de contenu React Native

Les SDK Braze incluent un flux de cartes par défaut pour vous permettre de démarrer avec les cartes de contenu. Pour afficher le flux de carte, vous pouvez utiliser la méthode `Braze.launchContentCards()`. Le flux de cartes par défaut inclus avec le SDK Braze traitera tous les suivis, les masquages et le rendu des cartes de contenu d’un utilisateur.

{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Méthodes pour les cartes

Pour créer votre propre interface utilisateur, vous pouvez obtenir une liste des cartes disponibles et écouter des mises à jour des cartes :

```javascript
// Set initial cards
const [cards, setCards] = useState([]);

// Listen for updates as a result of card refreshes, such as:
// a new session, a manual refresh with `requestContentCardsRefresh()`, or after the timeout period
Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, async (update) => {
    setCards(update.cards);
});

// Manually trigger a refresh of cards
Braze.requestContentCardsRefresh();
```

{% alert important %}
Si vous choisissez de créer votre propre interface utilisateur, vous devez appeler `logContentCardImpression` pour recevoir des analyses pour ces cartes. Ceci inclut les cartes `control`, qui doivent faire l’objet d’un suivi même si elles ne sont pas affichées pour l'utilisateur.
{% endalert %}

Vous pouvez utiliser ces méthodes supplémentaires pour créer un flux de cartes de contenu personnalisé dans votre application :

| Méthode                                   | Description                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `launchContentCards()`                   | Lance l'élément d'interface utilisateur Cartes de contenu.                                                                 |
| `requestContentCardsRefresh()`           | Demande les dernières cartes de contenu au serveur Braze SDK. La liste de cartes qui en résulte est transmise à chacun des [récepteurs d'événements de carte de contenu](#reactnative_cards-methods) précédemment enregistrés. |
| `getContentCards()`                      | Récupère les cartes de contenu du SDK Braze Ceci renvoie une promesse qui se résout avec la dernière liste de cartes du serveur. |
| `getCachedContentCards()`                | Renvoie le tableau de cartes de contenu le plus récent du cache.                                            |
| `logContentCardClicked(cardId)`          | Enregistre un clic pour l’ID de carte de contenu donné. Cette méthode est uniquement utilisée pour les analyses. Pour exécuter l'action de clic, appelez `processContentCardClickAction(cardId)` en plus.                                                        |
| `logContentCardImpression(cardId)`       | Enregistre une impression pour l’ID de carte de contenu donné.                                                      |
| `logContentCardDismissed(cardId)`        | Enregistre un rejet pour l’ID de carte de contenu donné.                                                        |
| `processContentCardClickAction(cardId)`  | Effectuer l'action d'une carte particulière.                                                               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Types de cartes et propriétés

Le modèle de données Content Cards est disponible dans le SDK React Native et propose les types de cartes Content Cards suivants : [Image seule](#image-only), [Image légendée](#captioned-image) et [Classique](#classic). Il existe également un type de carte spécial " [Contrôle"](#control), qui est renvoyé aux utilisateurs qui font partie du groupe de contrôle pour une carte donnée. Chaque type hérite des propriétés communes d'un modèle de base en plus de ses propriétés uniques.

{% alert tip %}
Pour une référence complète du modèle de données de la carte de contenu, consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard).
{% endalert %}

### Modèle de carte de base

Le modèle de carte de base fournit un comportement fondamental pour toutes les cartes.

|Propriété      | Description                                                                                                            |
|--------------|------------------------------------------------------------------------------------------------------------------------|
|`id`          | L'ID de la carte est défini par Braze.                                                                                            |
|`created`     | L’horodatage UNIX du moment de création de la carte depuis Braze.                                                             |
|`expiresAt`   | L’horodatage UNIX du moment d’expiration de la carte. Lorsque la valeur est inférieure à 0, cela signifie que la carte n'expire jamais.      |
|`viewed`      | Si la carte est lue ou non par l'utilisateur. Ceci ne permet pas d'enregistrer les analyses.                                           |
|`clicked`     | Si la carte a été cliquée par l'utilisateur.                                                                         |
|`pinned`      | Si la carte est épinglée.                                                                                            |
|`dismissed`   | Indique si l'utilisateur a fermé la carte de contenu. Marquer comme rejetée une carte qui l'a déjà été n'est pas possible. |
|`dismissible` | Détermine si la carte peut être ou non rejetée par l’utilisateur.                                                                           |
|`url`         | (Facultatif) Chaîne de caractères de l'URL associée à l'action de clic sur la carte.                                                       |
|`openURLInWebView` | Indique si les URL de cette carte doivent être ouvertes dans le WebView de Braze ou non.                                            |
|`isControl`   | Si cette carte est une carte de contrôle. Les cartes de contrôle ne doivent pas être montrées à l'utilisateur.                                |
|`extras`      | Mappage des suppléments clé-valeur pour cette carte.                                                                             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour une référence complète de la carte de base, consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct).

### Image uniquement

Les cartes avec image seulement sont des images cliquables en taille réelle.

|Propriété           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`             | Le type de carte de contenu, `IMAGE_ONLY`.                                                                              |
|`image`            | L’URL de l’image de la carte.                                                                                      |
|`imageAspectRatio` | Le rapport hauteur/largeur de l'image de la carte. Il sert d'indice avant que le chargement de l'image ne soit terminé. Veuillez noter que la propriété peut ne pas être fournie dans certaines circonstances. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour une référence complète de la carte image seule, consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct).

### Image avec légende

Les cartes d'images légendées sont des images cliquables en taille réelle accompagnées d'un texte descriptif.

|Propriété           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`             | Le type de carte de contenu, `CAPTIONED`.                                                                               |
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
|`type`             | Le type de carte de contenu, `CLASSIC`.                                                                                 |
|`image`            | (Facultatif) L'URL de l'image de la carte.                                                                           |
|`title`            | Le texte du titre pour la carte.                                                                                      |
|`cardDescription`  | Texte de description de la carte.                                                                                |
|`domain`           | (Facultatif) Texte du lien pour l'URL de propriété, par exemple, `"braze.com/resources/"`. Il peut être affiché sur l’interface utilisateur de la carte pour indiquer l’action/la direction du clic sur la carte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour une référence complète de la carte de contenu classique (annonce textuelle), consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct). Pour la carte image classique (nouvelles brèves), voir la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct).

### Contrôle

Les cartes de contrôle incluent toutes les propriétés de base, avec quelques différences importantes. Et surtout :

- La propriété `isControl` est garantie `true`.
- La propriété `extras` est garantie vide.

Pour une référence complète de la carte de contrôle, consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-control-card/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control-swift.struct).
