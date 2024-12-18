---
nav_title: in-app Messaging
article_title: Envoi de messages in-app pour Unity
channel: in-app messaging
platform: 
  - Unity
  - iOS
  - Android
page_order: 2
description: "Cet article de référence couvre les directives de configuration de l’envoi de messages in-app pour la plateforme Unity."

---

# Intégration de messages in-app

> Cet article de référence couvre les directives de configuration de l’envoi de messages in-app pour la plateforme Unity.

## Configuration du comportement par défaut des messages in-app

{% tabs %}
{% tab Android %}

Sur Android, les messages in-app de Braze sont nativement affichés automatiquement. Pour désactiver cette fonctionnalité, désélectionnez l'option **Afficher automatiquement les messages in-app** dans l'éditeur de configuration de Braze.

Vous pouvez également définir `com_braze_inapp_show_inapp_messages_automatically` sur `false` dans votre projet Unity `braze.xml`.

L’opération d’affichage du message in-app initial peut être configurée dans la configuration de Braze, via « Opération d’affichage du gestionnaire initial de message in-app ».

{% endtab %}
{% tab iOS %}

Sur iOS, les messages in-app de Braze sont nativement affichés automatiquement. Pour désactiver cette fonctionnalité, définissez les auditeurs d’objet de jeu dans l’éditeur de configuration Braze et assurez-vous que **Braze affiche les messages in-app** ne soit pas sélectionné.

L’opération d’affichage du message in-app initial peut être configurée dans la configuration de Braze, via « Opération d’affichage du gestionnaire initial de message in-app ».

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

## Affichage des messages in-app à la demande

Vous pouvez afficher le prochain message in-app disponible dans la pile à l’aide de la méthode `DisplayNextInAppMessage()`. Les messages sont ajoutés à la pile des messages enregistrés si`DISPLAY_LATER` ou `BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER` est choisi dans l’action d’affichage du message in-app.

```csharp
Appboy.AppboyBinding.DisplayNextInAppMessage();
```

## Réception des données de message in-app dans Unity

Vous pouvez lister des objets de jeu Unity pour être avertis des messages in-app entrants. Nous recommandons de définir des auditeurs d’objets de jeu à partir de l’éditeur de configuration Braze. Dans l’éditeur de configuration, les auditeurs doivent être définis séparément pour Android et iOS.

Si vous devez configurer votre auditeur d’objet de jeu lors de l’exécution, utilisez `AppboyBinding.ConfigureListener()` et spécifiez `BrazeUnityMessageType.IN_APP_MESSAGE`.

## Analyse des messages in-app

Les messages `string` entrants reçus dans votre rappel d’objet de jeu de messages in-app peuvent être analysés dans nos objets de modèle pré-fournis pour plus de commodité.

Utiliser `InAppMessageFactory.BuildInAppMessage()` pour analyser votre message in-app. L'objet résultant sera soit une instance de [`IInAppMessage.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs) ou [`IInAppMessageImmersive.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs) en fonction de son type.

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

## Support GIF

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

## Analyse

Les clics et les impressions doivent être enregistrés manuellement pour les messages in-app non affichés directement par Braze.

Utilisez `LogClicked()` et `LogImpression()` sur [`IInAppMessage`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs) pour enregistrer les clics et les impressions sur votre message.

Utilisez `LogButtonClicked(int buttonID)` sur [`IInAppMessageImmersive`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs) pour enregistrer les clics sur les boutons. Notez que les boutons sont conseillés sous forme de listes d'instances de[`InAppMessageButton`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/InAppMessageButton.cs) dont chacune contient une instance `ButtonID`.

## Ecoutes d'actions personnalisées

Si vous avez besoin de plus de contrôle sur la façon dont un utilisateur interagit avec les messages in-app, utilisez un `BrazeInAppMessageListener` et attribuez-le à `Appboy.AppboyBinding.inAppMessageListener`. Concernant les délégués que vous ne souhaitez pas utiliser, vous pouvez simplement les laisser définis comme `null`.

```csharp
BrazeInAppMessageListener listener = new BrazeInAppMessageListener() {
  BeforeInAppMessageDisplayed = BeforeInAppMessageDisplayed,
  OnInAppMessageButtonClicked = OnInAppMessageButtonClicked,
  OnInAppMessageClicked       = OnInAppMessageClicked,
  OnInAppMessageHTMLClicked   = OnInAppMessageHTMLClicked,
  OnInAppMessageDismissed     = OnInAppMessageDismissed,
};
Appboy.AppboyBinding.inAppMessageListener = listener;

public void BeforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  // Executed before an in-app message is displayed.
}

public void OnInAppMessageButtonClicked(IInAppMessage inAppMessage, InAppMessageButton inAppMessageButton) {
  // Executed whenever an in-app message button is clicked.
}

public void OnInAppMessageClicked(IInAppMessage inAppMessage) {
  // Executed whenever an in-app message is clicked.
}

public void OnInAppMessageHTMLClicked(IInAppMessage inAppMessage, Uri uri) {
  // Executed whenever an HTML in-app message is clicked.
}

public void OnInAppMessageDismissed(IInAppMessage inAppMessage) {
  // Executed whenever an in-app message is dismissed without a click.
}
```

