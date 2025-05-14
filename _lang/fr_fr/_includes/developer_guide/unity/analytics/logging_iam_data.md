## S'abonner à des messages in-app

Vous pouvez lister des objets de jeu Unity pour être avertis des messages in-app entrants. Nous recommandons de définir des auditeurs d’objets de jeu à partir de l’éditeur de configuration Braze. Dans l’éditeur de configuration, les auditeurs doivent être définis séparément pour Android et iOS.

Si vous devez configurer votre auditeur d’objet de jeu lors de l’exécution, utilisez `AppboyBinding.ConfigureListener()` et spécifiez `BrazeUnityMessageType.IN_APP_MESSAGE`.

## Analyser les messages

Les messages `string` entrants reçus dans votre rappel d’objet de jeu de messages in-app peuvent être analysés dans nos objets de modèle pré-fournis pour plus de commodité.

Utiliser `InAppMessageFactory.BuildInAppMessage()` pour analyser votre message in-app. L'objet résultant sera soit une instance de [`IInAppMessage.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs) ou [`IInAppMessageImmersive.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs) en fonction de son type.

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

## Données d'envoi des messages

Les clics et les impressions doivent être enregistrés manuellement pour les messages in-app non affichés directement par Braze.

Utilisez `LogClicked()` et `LogImpression()` sur [`IInAppMessage`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs) pour enregistrer les clics et les impressions sur votre message.

Utilisez `LogButtonClicked(int buttonID)` sur [`IInAppMessageImmersive`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs) pour enregistrer les clics sur les boutons. Notez que les boutons sont conseillés sous forme de listes d'instances de[`InAppMessageButton`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/InAppMessageButton.cs) dont chacune contient une instance `ButtonID`.
