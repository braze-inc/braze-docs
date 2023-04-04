---
nav_title: Envoi de messages in-app
article_title: Envoi de messages in-app pour Unity
channel: Envoi de messages in-app
platform: 
  - Unity
  - iOS
  - Android
page_order: 2
description: "Cet article de référence couvre les directives d’intégration de messagerie in-app pour la plateforme Unity."

---

# Envoi de messages in-app

## Configuration du comportement par défaut des messages in-app

{% tabs %}
{% tab Android %}

Sur Android, les messages in-app de Braze sont nativement affichés automatiquement. Pour désactiver cette fonctionnalité, désélectionnez **Afficher automatiquement les messages in-app** dans l’éditeur de configuration Braze.

Vous pouvez également définir `com_braze_inapp_show_inapp_messages_automatically` sur `false` dans votre projet Unity `braze.xml`.

L’opération d’affichage du message in-app initial peut être configurée dans la configuration de Braze, via « Opération d’affichage du gestionnaire initial de message in-app ».

{% endtab %}
{% tab iOS %}

Sur iOS, les messages in-app de Braze sont nativement affichés automatiquement. Pour désactiver cette fonctionnalité, définissez les auditeurs d’objet de jeu dans l’éditeur de configuration Braze et assurez-vous que **Braze affiche les messages in-app** ne soit pas sélectionné.

{% endtab %}
{% endtabs %}

## Configuration du comportement d’affichage des messages in-app

Vous pouvez éventuellement modifier le comportement d’affichage des messages in-app au moment de l’exécution via les éléments suivants :

```csharp
// Sets in-app messages to display immediately when triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_NOW);

// Sets in-app messages to display at a later time and be saved in a stack.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER);

// Sets in-app messages to be discarded after being triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISCARD);
```

## Affichage des messages In-App à la demande

Vous pouvez afficher le prochain message in-app disponible dans la pile à l’aide de la méthode `DisplayNextInAppMessage()`. Les messages sont ajoutés à la pile des messages enregistrés si`DISPLAY_LATER` ou `BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER` est choisi dans l’action d’affichage du message in-app.

```csharp
Appboy.AppboyBinding.DisplayNextInAppMessage();
```

## Réception des données de message in-app dans Unity

Vous pouvez lister des objets de jeu Unity pour être avertis des messages in-app entrants. Nous recommandons de définir des auditeurs d’objets de jeu à partir de l’éditeur de configuration Braze. Dans l’éditeur de configuration, les auditeurs doivent être définis séparément pour Android et iOS.

Si vous devez configurer votre auditeur d’objet de jeu lors de l’exécution, utilisez `AppboyBinding.ConfigureListener()` et spécifiez `BrazeUnityMessageType.IN_APP_MESSAGE`.

## Analyse des messages in-app

Les messages `string` entrants reçus dans votre rappel d’objet de jeu de messages in-app peuvent être analysés dans nos objets de modèle pré-fournis pour plus de commodité.

Utiliser `InAppMessageFactory.BuildInAppMessage()` pour analyser votre message in-app. L’objet résultant sera une instance de [`IInAppMessage.cs`][13] ou [`IInAppMessageImmersive.cs`][12] selon son type.

### Exemple de rappel de message in-app

```csharp
// Automatically logs a button click, if present.
void InAppMessageReceivedCallback(string message) {
  IInAppMessage inApp = InAppMessageFactory.BuildInAppMessage(message);
  if (inApp is IInAppMessageImmersive) {
    IInAppMessageImmersive inAppImmersive = inApp as IInAppMessageImmersive;
    if (inAppImmersive.Buttons != null && inAppImmersive.Buttons.Count > 0) {
      inAppImmersive.LogButtonClicked(inAppImmersive.Buttons[0].ButtonID);
    }
  }
}
```

## Analytique

Les clics et les impressions doivent être enregistrés manuellement pour les messages in-app non affichés directement par Braze.

Utilisez `LogClicked()` et `LogImpression()` dans [`IInAppMessage`][13] pour consigner les clics et les impressions sur votre message.

Utilisez `LogButtonClicked(int buttonID)` dans [`IInAppMessageImmersive`][12] pour enregistrer les clics sur le bouton. Notez que les boutons sont représentés comme des listes d’instances [`InAppMessageButton`][8] chacune d’entre elles contenant `ButtonID`.

[8]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/InAppMessage/InAppMessageButton.cs
[12]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs
[13]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs
