---
nav_title: Messagerie intégrée
article_title: Messagerie intégrée pour l'unité
channel: Messagerie intégrée
platform:
  - Unité
  - iOS
  - Android
page_order: 2
description: "Cet article de référence couvre les directives d'intégration de la messagerie dans l'application pour la plate-forme Unity."
---

# Messagerie intégrée

## Configuration du comportement des messages par défaut dans l'application

{% tabs %}
{% tab Android %}

Sur Android, les messages dans l'application de Braze sont affichés automatiquement en natif. Pour désactiver cette fonctionnalité, désélectionnez "Afficher automatiquement les messages dans l'application" dans l'éditeur de configuration de Braze.

You may alternatively set `com_appboy_inapp_show_inapp_messages_automatically` to `false` in your Unity project's `braze.xml`.

{% endtab %}
{% tab iOS %}

Sur iOS, les messages dans l'application de Braze sont affichés automatiquement en natif. Pour désactiver cette fonctionnalité, définissez les écouteurs d'objets du jeu dans l'éditeur de configuration de Braze, et assurez-vous que "Braze Display In-App Messages" n'est pas sélectionné.

{% endtab %}
{% endtabs %}

## Configuration du comportement d'affichage des messages dans l'application

Vous pouvez éventuellement modifier le comportement d'affichage des messages In-App au moment de l'exécution:

```csharp
// Définit les messages In-App à afficher immédiatement lorsqu'ils sont déclenchés.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_NOW);

// Définit les messages dans l'application à afficher plus tard et à être enregistrés dans une pile.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER);

// Définit les messages In-App à être rejetés après avoir été déclenchés.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISCARD);
```

## Réception des données du message dans l'application dans Unity

Vous pouvez enregistrer des objets Unity Game pour être averti des messages entrants dans l'application. Nous vous recommandons de configurer les écouteurs d'objets du jeu à partir de l'éditeur de configuration de Braze. Dans l'éditeur de configuration, les écouteurs doivent être définis séparément pour Android et iOS.

- Si vous avez besoin de configurer l'écouteur d'objet du jeu à l'exécution, utilisez `AppboyBinding.ConfigureListener()` et spécifiez `BrazeUnityMessageType.IN_APP_MESSAGE`.

## Analyse des messages dans l'application

Les messages entrants de `chaîne` reçus dans la fonction de rappel d'objet du jeu de message peuvent être analysés dans nos objets modèles pré-fournis pour plus de commodité.

Utilisez `InAppMessageFactory.BuildInAppMessage()` pour analyser votre message dans l'application. L'objet résultant sera soit une instance de [`IInAppMessage.cs`][13] ou [`IInAppMessageImmersive.cs`][12] selon son type.

### Exemple de rappel de message dans l'application

```csharp
// Enregistre automatiquement un clic de bouton, si présent.
void InAppMessageReceivedCallback(string message) {
  IInAppMessage inApp = InAppMessageFactory. uildInAppMessage(message);
  if (inApp est IInAppMessageImmersive) {
    IInAppMessageImmersive inAppImmersive = inApp as IInAppMessageImmersive;
    si (inAppImmersive. uttons != null && inAppImmersive.Buttons.Count > 0) {
      inAppImmersive. ogButtonClicked(inAppImmersive.Buttons[0].ButtonID);
    }
  }
}
```

## Analyses

Les clics et les impressions doivent être enregistrés manuellement pour les messages dans l'application qui ne sont pas affichés directement par Braze.

Utilisez `LogClicked()` et `LogImpression()` sur [`IInAppMessage`][13] pour enregistrer les clics et les impressions de votre message.

Utilisez `LogButtonClicked(int buttonID)` sur [`IInAppMessageImmersive`][12] pour enregistrer les clics de bouton. Notez que les boutons sont représentés comme des listes d'instances[`InAppMessageButton`][8] dont chacune contient un `ButtonID`.

[8]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/InAppMessage/InAppMessageButton.cs
[12]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/InAppMessage/IInAppMessageImmersive.cs
[12]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/InAppMessage/IInAppMessageImmersive.cs
[13]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/InAppMessage/IInAppMessage.cs
[13]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/InAppMessage/IInAppMessage.cs
