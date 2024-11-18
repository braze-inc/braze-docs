---
nav_title: Escuchas personalizadas
article_title: Receptores de mensajes dentro de la aplicación personalizados para Android y FireOS
platform: 
  - Android
  - FireOS
page_order: 3
description: "Este artículo de referencia trata de las escuchas de mensajería dentro de la aplicación personalizadas para tu aplicación Android o FireOS."
channel:
  - in-app messages

---

# Escuchadores personalizados

> Este artículo de referencia trata de las escuchas de mensajería dentro de la aplicación personalizadas para tu aplicación Android o FireOS.

Antes de personalizar los mensajes dentro de la aplicación con escuchas personalizadas, es importante entender el sistema de gestión de mensajes de la aplicación [`BrazeInAppMessageManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html)que gestiona la mayoría de los mensajes dentro de la aplicación. Como se describe en [el paso 1]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/#step-1-braze-in-app-message-manager-registration) de la guía de integración de mensajes dentro de la aplicación, debe estar registrado para que los mensajes dentro de la aplicación funcionen correctamente.

`BrazeInAppMessageManager` gestiona la visualización de mensajes dentro de la aplicación en Android. Contiene instancias de clases ayudantes que le ayudan a gestionar el ciclo de vida y la visualización de los mensajes dentro de la aplicación. Todas estas clases tienen implementaciones estándar y definir clases personalizadas es completamente opcional. Sin embargo, hacerlo puede añadir otro nivel de control sobre la visualización y el comportamiento de los mensajes dentro de la aplicación. Estas clases personalizables incluyen:

- [`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html) - [Gestiona de forma personalizada la visualización de mensajes dentro de la aplicación y su comportamiento](#custom-manager-listener)
- [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) - [Crea vistas personalizadas de mensajes dentro de la aplicación](#custom-view-factory)
- [`IInAppMessageAnimationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-animation-factory/index.html) - [Define animaciones personalizadas de mensajes dentro de la aplicación](#custom-animation-factory)
- [`IHtmlInAppMessageActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-html-in-app-message-action-listener/index.html) - [Gestión personalizada de la visualización y el comportamiento de los mensajes HTML dentro de la aplicación](#custom-html-in-app-message-action-listener)
- [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) - [Gestión personalizada de la interacción jerárquica de la vista de mensajes dentro de la aplicación](#custom-view-wrapper-factory)

{% alert note %}
Este artículo incluye información sobre la Fuente de noticias, que está siendo obsoleta. Braze recomienda a los clientes que utilizan nuestra herramienta de fuente de noticias que se pasen a nuestro canal de mensajería de tarjetas de contenido: es más flexible, personalizable y fiable. Para más información, consulta la [guía de migración]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

## Receptor personalizado del administrador

`BrazeInAppMessageManager` gestiona automáticamente la visualización y el ciclo de vida de los mensajes dentro de la aplicación. Si necesitas más control sobre el ciclo de vida de un mensaje, establecer un administrador de escucha personalizado te habilitará para recibir el objeto de mensaje dentro de la aplicación en varios puntos del ciclo de vida del mensaje dentro de la aplicación, permitiéndote gestionar tú mismo su visualización, realizar el procesamiento posterior, reaccionar al comportamiento del usuario, procesar los [extras]({{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/customization/key_value_pairs/) del objeto y mucho más.

### Paso 1: Implementa un receptor de mensajes dentro de la aplicación para el administrador de mensajes

Crea una clase que implemente [`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html).

Las devoluciones de llamada en tu `IInAppMessageManagerListener` serán llamadas en varios puntos del ciclo de vida del mensaje dentro de la aplicación.

Por ejemplo, si estableces una escucha personalizada de administrador cuando se reciba un mensaje dentro de la aplicación desde Braze, se llamará al método `beforeInAppMessageDisplayed()`. Si tu implementación de este método devuelve [`InAppMessageOperation.DISCARD`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/index.html#27659854%2FClasslikes%2F-1725759721)indica a Braze que el mensaje dentro de la aplicación será gestionado por la aplicación anfitriona y que Braze no debe mostrarlo. Si se devuelve `InAppMessageOperation.DISPLAY_NOW`, Braze intentará mostrar el mensaje dentro de la aplicación. Este método debe utilizarse si decides mostrar el mensaje dentro de la aplicación de forma personalizada.

`IInAppMessageManagerListener` también incluye métodos delegados para los clics en el propio mensaje o en uno de los botones. Un caso de uso común sería interceptar un mensaje cuando se hace clic en un botón o en un mensaje para su posterior procesamiento.

### Paso 2: Engancha a los métodos del ciclo de vida de la vista de mensajes dentro de la aplicación (opcional)

La interfaz [`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html) tiene métodos de vista de mensajes dentro de la aplicación que se invocan en distintos puntos del ciclo de vida de la vista de mensajes dentro de la aplicación. Estos métodos se llaman en el orden siguiente

- [`beforeInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-opened.html) - Se llama justo antes de que el mensaje dentro de la aplicación se añada a la vista de la actividad. El mensaje dentro de la aplicación todavía no está visible para el usuario en este momento.
- [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html) - Se llama justo después de añadir el mensaje dentro de la aplicación a la vista de la actividad. El mensaje dentro de la aplicación es ahora visible para el usuario en este momento.
- [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html) - Se llama justo antes de que el mensaje dentro de la aplicación se elimine de la vista de la actividad. El mensaje dentro de la aplicación sigue siendo visible para el usuario en este momento.
- [`afterInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-closed.html) - Se llama justo después de que el mensaje dentro de la aplicación se elimine de la vista de la actividad. El mensaje dentro de la aplicación ya no es visible para el usuario en este momento.

Para mayor contexto, el tiempo transcurrido entre [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html) y [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html) es cuando la vista de mensajes dentro de la aplicación está en pantalla, visible para el usuario.

{% alert note %}
No es necesario aplicar estos métodos. Sólo se proporcionan para seguir e informar del ciclo de vida de la vista de mensajes dentro de la aplicación. Es funcionalmente aceptable dejar vacías las implementaciones de estos métodos.
{% endalert %}

### Paso 3: Ordena a Braze que utilice tu receptor de mensajes dentro de la aplicación como administrador

Una vez creado tu `IInAppMessageManagerListener`, llama a `BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener()` para dar instrucciones. `BrazeInAppMessageManager`
para utilizar tu `IInAppMessageManagerListener` personalizado en lugar de la escucha predeterminada.

Te recomendamos que configures tu `IInAppMessageManagerListener` en tu [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) antes de cualquier otra llamada a Braze. Esto establecerá la escucha personalizada antes de que se muestre cualquier mensaje dentro de la aplicación.

#### Alterar los mensajes dentro de la aplicación antes de mostrarlos

Cuando se reciba un nuevo mensaje dentro de la aplicación y ya se esté mostrando un mensaje dentro de la aplicación, el nuevo mensaje se colocará en la parte superior de la pila y se podrá mostrar más adelante.

Sin embargo, si no se muestra ningún mensaje dentro de la aplicación, se llamará al siguiente método delegado en `IInAppMessageManagerListener`:

{% tabs %}
{% tab JAVA %}
```java
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessageBase) {
  return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
override fun beforeInAppMessageDisplayed(inAppMessageBase: IInAppMessage): InAppMessageOperation {
  return InAppMessageOperation.DISPLAY_NOW
}
```
{% endtab %}
{% endtabs %}

El valor de retorno `InAppMessageOperation()` puede controlar cuándo debe mostrarse el mensaje. El uso sugerido de este método sería retrasar los mensajes en ciertas partes de la aplicación devolviendo `DISPLAY_LATER` cuando los mensajes dentro de la aplicación distrajeran la experiencia del usuario con la aplicación.

| `InAppMessageOperation` valor de retorno | Comportamiento |
| -------------------------- | -------- |
| `DISPLAY_NOW` | Se mostrará el mensaje |
| `DISPLAY_LATER` | El mensaje se devolverá a la pila y se mostrará en la siguiente oportunidad disponible |
| `DISCARD` | El mensaje será descartado |
| `null` | El mensaje será ignorado. Este método **NO** debe devolver `null` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Consulta [`InAppMessageOperation.java`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/index.html) para más detalles.

{% alert tip %}
Si eliges `DISCARD` el mensaje dentro de la aplicación y lo sustituyes por la vista de tu mensaje dentro de la aplicación, tendrás que registrar manualmente los clics y las impresiones del mensaje dentro de la aplicación.
{% endalert %}

En Android, esto se hace llamando a `logClick` y `logImpression` en los mensajes dentro de la aplicación y a `logButtonClick` en los mensajes inmersivos dentro de la aplicación.

{% alert tip %}
Una vez que un mensaje dentro de la aplicación se ha colocado en la pila, puedes solicitar que se recupere y se muestre en cualquier momento llamando a [`BrazeInAppMessageManager.getInstance().requestDisplayInAppMessage()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/request-display-in-app-message.html). Este método solicita a Braze que muestre el siguiente mensaje dentro de la aplicación disponible en la pila.
{% endalert %}

### Paso 4: Personalizar el comportamiento del tema oscuro (opcional) {#android-in-app-message-dark-theme-customization}

En la lógica predeterminada de `IInAppMessageManagerListener`, en `beforeInAppMessageDisplayed()`, se comprueba la configuración del sistema y se habilita condicionalmente el estilo de tema oscuro en el mensaje con el siguiente código:

{% tabs %}
{% tab JAVA %}
```java
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  if (inAppMessage instanceof IInAppMessageThemeable && ViewUtils.isDeviceInNightMode(BrazeInAppMessageManager.getInstance().getApplicationContext())) {
    ((IInAppMessageThemeable) inAppMessage).enableDarkTheme();
  }
  return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
  if (inAppMessage is IInAppMessageThemeable && ViewUtils.isDeviceInNightMode(BrazeInAppMessageManager.getInstance().applicationContext!!)) {
    (inAppMessage as IInAppMessageThemeable).enableDarkTheme()
  }
  return InAppMessageOperation.DISPLAY_NOW
}
```
{% endtab %}
{% endtabs %}

Si quieres utilizar tu propia lógica condicional, puedes llamar a [`enableDarkTheme`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-themeable/enable-dark-theme.html) en cualquier paso del proceso previo a la visualización.

## Vista personalizada de fábrica

Los tipos de mensajes dentro de la aplicación Braze son lo suficientemente versátiles como para cubrir la mayoría de los casos de uso personalizados. Sin embargo, si quieres definir completamente el aspecto visual de tus mensajes dentro de la aplicación en lugar de utilizar un tipo predeterminado, Braze lo hace posible configurando una fábrica de vistas personalizada.

### Paso 1: Implementa una fábrica de visualización de mensajes dentro de la aplicación

Crea una clase que implemente [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html):

{% tabs %}
{% tab JAVA %}
```java
public class CustomInAppMessageViewFactory implements IInAppMessageViewFactory {
  @Override
  public View createInAppMessageView(Activity activity, IInAppMessage inAppMessage) {
    // Uses a custom view for slideups, modals, and full in-app messages.
    // HTML in-app messages and any other types will use the Braze default in-app message view factories
    switch (inAppMessage.getMessageType()) {
      case SLIDEUP:
      case MODAL:
      case FULL:
        // Use a custom view of your choosing
        return createMyCustomInAppMessageView();
      default:
        // Use the default in-app message factories
        final IInAppMessageViewFactory defaultInAppMessageViewFactory = BrazeInAppMessageManager.getInstance().getDefaultInAppMessageViewFactory(inAppMessage);
        return defaultInAppMessageViewFactory.createInAppMessageView(activity, inAppMessage);
    }
  }
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
class CustomInAppMessageViewFactory : IInAppMessageViewFactory {
  override fun createInAppMessageView(activity: Activity, inAppMessage: IInAppMessage): View {
    // Uses a custom view for slideups, modals, and full in-app messages.
    // HTML in-app messages and any other types will use the Braze default in-app message view factories
    when (inAppMessage.messageType) {
      MessageType.SLIDEUP, MessageType.MODAL, MessageType.FULL ->
        // Use a custom view of your choosing
        return createMyCustomInAppMessageView()
      else -> {
        // Use the default in-app message factories
        val defaultInAppMessageViewFactory = BrazeInAppMessageManager.getInstance().getDefaultInAppMessageViewFactory(inAppMessage)
        return defaultInAppMessageViewFactory!!.createInAppMessageView(activity, inAppMessage)
      }
    }
  }
}
```
{% endtab %}
{% endtabs %}

### Paso 2: Ordena a Braze que utilice tu fábrica de visualización de mensajes dentro de la aplicación

Una vez creado tu `IInAppMessageViewFactory`, llama a `BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory()` para dar instrucciones. `BrazeInAppMessageManager`
para utilizar tu `IInAppMessageViewFactory` personalizado en lugar de la vista predeterminada de fábrica.

{% alert tip %}
Te recomendamos que configures tu `IInAppMessageViewFactory` en tu `Application.onCreate()` antes de cualquier otra llamada a Braze. Esto establecerá la fábrica de visualizaciones personalizadas antes de que se muestre cualquier mensaje dentro de la aplicación.
{% endalert %}

#### Implementar una interfaz de vista Braze

La vista de mensajes dentro de la aplicación `slideup` implementa [`IInAppMessageView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-view/index.html). Las vistas de mensajes de tipo `full` y `modal` implementan [`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html). Implementar una de estas clases permite a Braze añadir escuchadores de clics a tu vista personalizada cuando proceda. Todas las clases de vista Braze extienden la clase [`View`](http://developer.android.com/reference/android/view/View.html) de Android.

Implementar `IInAppMessageView` te permite definir una determinada parte de tu vista personalizada como clicable. Implementar [`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html) te permite definir vistas de botón de mensaje y una vista de botón de cierre.

## Fábrica de animación personalizada

Los mensajes dentro de la aplicación tienen un comportamiento de animación preestablecido. `Slideup` mensajes se deslizan dentro de la pantalla; `full` y `modal` mensajes aparecen y desaparecen. Si quieres definir comportamientos de animación personalizados para tus mensajes dentro de la aplicación, Braze lo hace posible configurando una fábrica de animación personalizada.

### Paso 1: Implementa una fábrica de animación de mensajes dentro de la aplicación

Crea una clase que implemente [`IInAppMessageAnimationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-animation-factory/index.html):

{% tabs %}
{% tab JAVA %}
```java
public class CustomInAppMessageAnimationFactory implements IInAppMessageAnimationFactory {

  @Override
  public Animation getOpeningAnimation(IInAppMessage inAppMessage) {
    Animation animation = new AlphaAnimation(0, 1);
    animation.setInterpolator(new AccelerateInterpolator());
    animation.setDuration(2000L);
    return animation;
  }

  @Override
  public Animation getClosingAnimation(IInAppMessage inAppMessage) {
    Animation animation = new AlphaAnimation(1, 0);
    animation.setInterpolator(new DecelerateInterpolator());
    animation.setDuration(2000L);
    return animation;
  }
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
class CustomInAppMessageAnimationFactory : IInAppMessageAnimationFactory {
  override fun getOpeningAnimation(inAppMessage: IInAppMessage): Animation {
    val animation: Animation = AlphaAnimation(0, 1)
    animation.interpolator = AccelerateInterpolator()
    animation.duration = 2000L
    return animation
  }

  override fun getClosingAnimation(inAppMessage: IInAppMessage): Animation {
    val animation: Animation = AlphaAnimation(1, 0)
    animation.interpolator = DecelerateInterpolator()
    animation.duration = 2000L
    return animation
  }
}
```
{% endtab %}
{% endtabs %}

### Paso 2: Ordena a Braze que utilice tu fábrica de visualización de mensajes dentro de la aplicación

Una vez creado tu `IInAppMessageAnimationFactory`, llama a `BrazeInAppMessageManager.getInstance().setCustomInAppMessageAnimationFactory()` para dar instrucciones. `BrazeInAppMessageManager`
para utilizar tu `IInAppMessageAnimationFactory` personalizado en lugar de la fábrica de animaciones predeterminada.

Te recomendamos que configures tu `IInAppMessageAnimationFactory` en tu [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) antes de cualquier otra llamada a Braze. Esto establecerá la fábrica de animación personalizada antes de que se muestre cualquier mensaje dentro de la aplicación.

## Receptor de acciones HTML personalizado de mensajes dentro de la aplicación

El SDK de Braze tiene una clase predeterminada `DefaultHtmlInAppMessageActionListener` que se utiliza si no se define un oyente personalizado y realiza la acción apropiada automáticamente. Si necesitas más control sobre cómo interactúa un usuario con los distintos botones dentro de un mensaje HTML personalizado dentro de la aplicación, implementa una clase personalizada `IHtmlInAppMessageActionListener`.

### Paso 1: Implementa una acción HTML personalizada de escucha de mensajes dentro de la aplicación

Crea una clase que implemente [`IHtmlInAppMessageActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-html-in-app-message-action-listener/index.html).

Las devoluciones de llamada en tu `IHtmlInAppMessageActionListener` serán llamadas siempre que el usuario inicie cualquiera de las siguientes acciones dentro del mensaje HTML dentro de la aplicación:

- Haz clic en el botón de cerrar
- Dispara un evento personalizado
- Clic en una URL dentro de un mensaje HTML dentro de la aplicación

{% tabs %}
{% tab JAVA %}
```java
public class CustomHtmlInAppMessageActionListener implements IHtmlInAppMessageActionListener {
  private final Context mContext;

  public CustomHtmlInAppMessageActionListener(Context context) {
    mContext = context;
  }

  @Override
  public void onCloseClicked(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
    Toast.makeText(mContext, "HTML In App Message closed", Toast.LENGTH_LONG).show();
    BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false);
  }

  @Override
  public boolean onCustomEventFired(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
    Toast.makeText(mContext, "Custom event fired. Ignoring.", Toast.LENGTH_LONG).show();
    return true;
  }

  @Override
  public boolean onNewsfeedClicked(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
    Toast.makeText(mContext, "Newsfeed button pressed. Ignoring.", Toast.LENGTH_LONG).show();
    BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false);
    return true;
  }

  @Override
  public boolean onOtherUrlAction(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
    Toast.makeText(mContext, "Custom url pressed: " + url + " . Ignoring", Toast.LENGTH_LONG).show();
    BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false);
    return true;
  }
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
class CustomHtmlInAppMessageActionListener(private val mContext: Context) : IHtmlInAppMessageActionListener {

    override fun onCloseClicked(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle) {
        Toast.makeText(mContext, "HTML In App Message closed", Toast.LENGTH_LONG).show()
        BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false)
    }

    override fun onCustomEventFired(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle): Boolean {
        Toast.makeText(mContext, "Custom event fired. Ignoring.", Toast.LENGTH_LONG).show()
        return true
    }

    override fun onNewsfeedClicked(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle): Boolean {
        Toast.makeText(mContext, "Newsfeed button pressed. Ignoring.", Toast.LENGTH_LONG).show()
        BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false)
        return true
    }

    override fun onOtherUrlAction(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle): Boolean {
        Toast.makeText(mContext, "Custom url pressed: $url . Ignoring", Toast.LENGTH_LONG).show()
        BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false)
        return true
    }
}
```
{% endtab %}
{% endtabs %}

### Paso 2: Indica a Braze que utilice tu receptor de acciones de mensajes HTML dentro de la aplicación

Una vez creado tu `IHtmlInAppMessageActionListener`, llama a `BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener()` para indicar a `BrazeInAppMessageManager` que utilice tu `IHtmlInAppMessageActionListener` personalizado en lugar del oyente de acción predeterminado.

Te recomendamos que configures tu `IHtmlInAppMessageActionListener` en tu [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) antes de cualquier otra llamada a Braze. Esto configurará el receptor de acciones personalizado antes de que se muestre cualquier mensaje dentro de la aplicación:

{% tabs %}
{% tab JAVA %}
```java
BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener(new CustomHtmlInAppMessageActionListener(context));
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener(CustomHtmlInAppMessageActionListener(context))
```
{% endtab %}
{% endtabs %}

## Fábrica personalizada de envoltorios de vistas

El sitio `BrazeInAppMessageManager` se encarga automáticamente de colocar el modelo de mensajes dentro de la aplicación en la jerarquía de vistas de actividad existente de forma predeterminada utilizando [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html). Si necesitas personalizar la forma en que se colocan los mensajes dentro de la aplicación en la jerarquía de vistas, debes utilizar una función personalizada [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html).

### Paso 1: Implementa una fábrica de envoltorios de vistas de mensajes dentro de la aplicación

Crea una clase que implemente [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) y devuelva un [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html).

Esta fábrica se llama inmediatamente después de crear la vista de mensajes dentro de la aplicación. La forma más sencilla de implementar un programa personalizado [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) es ampliar el [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html) predeterminado:

{% tabs %}
{% tab JAVA %}
```java
public class CustomInAppMessageViewWrapper extends DefaultInAppMessageViewWrapper {
  public CustomInAppMessageViewWrapper(View inAppMessageView,
                                       IInAppMessage inAppMessage,
                                       IInAppMessageViewLifecycleListener inAppMessageViewLifecycleListener,
                                       BrazeConfigurationProvider brazeConfigurationProvider,
                                       Animation openingAnimation,
                                       Animation closingAnimation, View clickableInAppMessageView) {
    super(inAppMessageView,
        inAppMessage,
        inAppMessageViewLifecycleListener,
        brazeConfigurationProvider,
        openingAnimation,
        closingAnimation,
        clickableInAppMessageView);
  }

  @Override
  public void open(@NonNull Activity activity) {
    super.open(activity);
    Toast.makeText(activity.getApplicationContext(), "Opened in-app message", Toast.LENGTH_SHORT).show();
  }

  @Override
  public void close() {
    super.close();
    Toast.makeText(mInAppMessageView.getContext().getApplicationContext(), "Closed in-app message", Toast.LENGTH_SHORT).show();
  }
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
class CustomInAppMessageViewWrapper(inAppMessageView: View,
                                    inAppMessage: IInAppMessage,
                                    inAppMessageViewLifecycleListener: IInAppMessageViewLifecycleListener,
                                    brazeConfigurationProvider: BrazeConfigurationProvider,
                                    openingAnimation: Animation,
                                    closingAnimation: Animation, clickableInAppMessageView: View) : 
    DefaultInAppMessageViewWrapper(inAppMessageView, 
        inAppMessage, 
        inAppMessageViewLifecycleListener, 
        brazeConfigurationProvider, 
        openingAnimation, 
        closingAnimation, 
        clickableInAppMessageView) {

  override fun open(activity: Activity) {
    super.open(activity)
    Toast.makeText(activity.applicationContext, "Opened in-app message", Toast.LENGTH_SHORT).show()
  }

  override fun close() {
    super.close()
    Toast.makeText(mInAppMessageView.context.applicationContext, "Closed in-app message", Toast.LENGTH_SHORT).show()
  }
}
```
{% endtab %}
{% endtabs %}

### Paso 2: Ordena a Braze que utilice tu fábrica personalizada de envoltorios de vistas

Una vez creado tu [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html), llama a [`BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-custom-in-app-message-view-factory.html) para indicar a `BrazeInAppMessageManager` que utilice tu vista personalizada [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) en lugar de la fábrica de envoltorios de vistas predeterminada.

Te recomendamos que configures tu [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) en tu [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) antes de cualquier otra llamada a Braze. Esto configurará la fábrica del envoltorio de la vista personalizada antes de que se muestre cualquier mensaje dentro de la aplicación:

{% tabs %}
{% tab JAVA %}
```java
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(new CustomInAppMessageViewWrapper());
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(CustomInAppMessageViewWrapper())
```
{% endtab %}
{% endtabs %}

