---
nav_title: Enviar mensajes dentro de la aplicación
article_title: Mensajería dentro de la aplicación para Unity
channel: in-app messaging
platform: 
  - Unity
  - iOS
  - Android
page_order: 2
description: "En este artículo de referencia se cubren las directrices de configuración de la mensajería dentro de la aplicación para la plataforma Unity."

---

# Integración de mensajería dentro de la aplicación

> En este artículo de referencia se cubren las directrices de configuración de la mensajería dentro de la aplicación para la plataforma Unity.

## Configurar el comportamiento predeterminado de los mensajes dentro de la aplicación

{% tabs %}
{% tab Android %}

En Android, los mensajes dentro de la aplicación de Braze se muestran automáticamente de forma nativa. Para desactivar esta funcionalidad, anula la selección de **Mostrar automáticamente mensajes dentro de la aplicación** en el editor de configuración de Braze.

También puedes configurar `com_braze_inapp_show_inapp_messages_automatically` como `false` en la página `braze.xml` de tu proyecto Unity.

La operación inicial de visualización de mensajes dentro de la aplicación puede establecerse en la configuración de Braze mediante la opción "Operación inicial de visualización del administrador de mensajes dentro de la aplicación".

{% endtab %}
{% tab iOS %}

En iOS, los mensajes dentro de la aplicación de Braze se muestran automáticamente de forma nativa. Para desactivar esta funcionalidad, configura los oyentes del objeto del juego en el editor de configuración de Braze y asegúrate de que la opción **Braze Muestra mensajes dentro de la aplicación** no está seleccionada.

La operación inicial de visualización de mensajes dentro de la aplicación puede establecerse en la configuración de Braze mediante la opción "Operación inicial de visualización del administrador de mensajes dentro de la aplicación".

{% endtab %}
{% endtabs %}

## Configurar el comportamiento de visualización de mensajes dentro de la aplicación

Opcionalmente, puedes cambiar el comportamiento de visualización de los mensajes dentro de la aplicación en tiempo de ejecución mediante lo siguiente:

```csharp
// Sets in-app messages to display immediately when triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_NOW);

// Sets in-app messages to display at a later time and be saved in a stack.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER);

// Sets in-app messages to be discarded after being triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISCARD);
```

## Mostrar mensajes dentro de la aplicación bajo demanda

Puedes mostrar el siguiente mensaje dentro de la aplicación disponible en la pila mediante el método `DisplayNextInAppMessage()`. Los mensajes se añaden a esta pila de mensajes guardados si se elige `DISPLAY_LATER` o `BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER` como acción de visualización de mensajes dentro de la aplicación.

```csharp
Appboy.AppboyBinding.DisplayNextInAppMessage();
```

## Recepción de datos de mensajes dentro de la aplicación en Unity

Puedes registrar objetos del juego Unity para recibir notificaciones de mensajes dentro de la aplicación. Recomendamos configurar los oyentes del objeto del juego desde el editor de configuración de Braze. En el editor de configuración, las escuchas deben establecerse por separado para Android e iOS.

Si necesitas configurar la escucha de tu objeto del juego en tiempo de ejecución, utiliza `AppboyBinding.ConfigureListener()` y especifica `BrazeUnityMessageType.IN_APP_MESSAGE`.

## Análisis sintáctico de mensajes dentro de la aplicación

Los mensajes entrantes de `string` recibidos en la devolución de llamada de tu objeto del juego de mensajería dentro de la aplicación pueden analizarse en nuestros objetos modelo suministrados previamente para mayor comodidad.

Utiliza `InAppMessageFactory.BuildInAppMessage()` para analizar tu mensaje dentro de la aplicación. El objeto resultante será una instancia de [`IInAppMessage.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs) o [`IInAppMessageImmersive.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs) dependiendo de su tipo.

### Ejemplo de devolución de llamada de mensajes dentro de la aplicación

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

## Soporte de GIF

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

## Análisis

Los clics y las impresiones deben registrarse manualmente para los mensajes dentro de la aplicación no mostrados directamente por Braze.

Utiliza `LogClicked()` y `LogImpression()` en [`IInAppMessage`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs) para registrar los clics y las impresiones de tu mensaje.

Utiliza `LogButtonClicked(int buttonID)` en [`IInAppMessageImmersive`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs) para registrar los clics en los botones. Ten en cuenta que los botones se representan como listas de instancias [`InAppMessageButton`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/InAppMessageButton.cs), cada una de las cuales contiene un `ButtonID`.

## Escuchadores de acción personalizados

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

