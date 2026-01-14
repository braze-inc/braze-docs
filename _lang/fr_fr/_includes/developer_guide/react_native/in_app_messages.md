{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Types de messages

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Modèle de données

Le modèle de message in-app est disponible dans le SDK React Native. Braze propose quatre types de messages in-app qui partagent le même modèle de données : **contextuel** **fenêtre modale**, **complet** et **HTML complet**.

### Messages

Le modèle de message in-app constitue la base de tous les messages in-app.

|Propriété          | Description                                                                                                            |
|------------------|------------------------------------------------------------------------------------------------------------------------|
|`inAppMessageJsonString` | La représentation JSON du message.                                                                                |
|`message`         | Le texte du message.                                                                                                      |
|`header`          | L'en-tête du message.                                                                                                    |
|`uri`             | L'URI associé à l'action de clic sur le bouton.                                                                       |
|`imageUrl`        | L'URL de l'image du message.                                                                                                 |
|`zippedAssetsUrl` | Les ressources zippées préparées pour afficher le contenu HTML.                                                                    |
|`useWebView`      | Indique si l'action de clic sur le bouton doit être redirigée à l'aide d'une vue web.                                            |
|`duration`        | La durée d'affichage du message.                                                                                          |
|`clickAction`     | Le type d'action « clic sur bouton ». Les types sont : `URI`, et `NONE`.                                     |
|`dismissType`     | Le type de fermeture du message. Les deux types sont : `SWIPE` et `AUTO_DISMISS`.                                                 |
|`messageType`     | Le type de message in-app pris en charge par le SDK. Les quatre types sont les suivants : `SLIDEUP`, `MODAL`, `FULL` et `HTML_FULL`.          |
|`extras`          | Le dictionnaire des suppléments de message. Valeur par défaut : `[:]`.                                                                   |
|`buttons`         | La liste des boutons sur le message in-app.                                                                             |
|`toString()`      | L'envoi de messages sous la forme d'une chaîne de caractères.                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour une référence complète du modèle d'envoi de messages in-app, consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage).

### Boutons

Des boutons peuvent être ajoutés aux messages in-app pour effectuer des actions et enregistrer des analyses. Le modèle de bouton constitue la base de tous les boutons de messages in-app.

|Propriété          | Description                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
|`text`            | Le texte du bouton.                                                                                                     |
|`uri`             | L'URI associé à l'action de clic sur le bouton.                                                                            |
|`useWebView`      | Indique si l'action de clic sur le bouton doit être redirigée à l'aide d'une vue web.                                                 |
|`clickAction`     | Le type d'action de clic traité lorsque l'utilisateur clique sur le bouton. Les types sont : `URI`, et `NONE`. |
|`id`              | L'ID du bouton dans le message.                                                                                               |
|`toString()`      | Le bouton sous forme de chaîne de caractères.                                                                                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour une référence complète du modèle de bouton, consultez la documentation [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html) et [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/button).
