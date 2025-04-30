## Personalizar el comportamiento de visualización

Puedes cambiar el comportamiento de visualización de los mensajes dentro de la aplicación en tiempo de ejecución mediante lo siguiente:

```csharp
// Sets in-app messages to display immediately when triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_NOW);

// Sets in-app messages to display at a later time and be saved in a stack.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER);

// Sets in-app messages to be discarded after being triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISCARD);
```

## Configuración de una escucha personalizada

Si necesitas más control sobre cómo interactúa un usuario con los mensajes dentro de la aplicación, utiliza un `BrazeInAppMessageListener` y asígnalo a `Appboy.AppboyBinding.inAppMessageListener`. Para los delegados que no quieras utilizar, puedes dejarlos simplemente como `null`.

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
