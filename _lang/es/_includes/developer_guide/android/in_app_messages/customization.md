{% multi_lang_include developer_guide/prerequisites/android.md %} También tendrás que [configurar los mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/in_app_messages).

## Configuración de oyentes personalizados del administrador

{% tabs %}
{% tab oyente global %}
Aunque el receptor de `BrazeInAppMessageManager` puede gestionar automáticamente la visualización y el ciclo de vida de los mensajes dentro de la aplicación, tendrás que implementar un receptor de administrador personalizado si quieres personalizar completamente tus mensajes.
{% endtab %}

{% tab oyente html %}
El SDK de Braze tiene una clase predeterminada `DefaultHtmlInAppMessageActionListener` que se utiliza si no se define un oyente personalizado y realiza la acción apropiada automáticamente. Si necesitas más control sobre cómo interactúa un usuario con los distintos botones dentro de un mensaje HTML personalizado dentro de la aplicación, implementa una clase personalizada `IHtmlInAppMessageActionListener`.
{% endtab %}
{% endtabs %}

### Paso 1: Implementar la escucha personalizada del administrador

{% tabs %}
{% tab oyente global %}
#### Paso 1.1: Pon en marcha `IInAppMessageManagerListener` 

Crea una clase que implemente [`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html).

Las devoluciones de llamada de tu `IInAppMessageManagerListener` también serán llamadas en varios puntos del ciclo de vida de los mensajes dentro de la aplicación. Por ejemplo, si estableces una escucha personalizada del administrador cuando se reciba un mensaje dentro de la aplicación desde Braze, se llamará al método [`beforeInAppMessageDisplayed()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-displayed.html) será llamado. Si tu implementación de este método devuelve [`InAppMessageOperation.DISCARD`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/-d-i-s-c-a-r-d/index.html)indica a Braze que el mensaje dentro de la aplicación será gestionado por la aplicación anfitriona y que Braze no debe mostrarlo. Si se devuelve [`InAppMessageOperation.DISPLAY_NOW`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/-d-i-s-p-l-a-y_-n-o-w/index.html) Braze intentará mostrar el mensaje dentro de la aplicación. Este método debe utilizarse si decides mostrar el mensaje dentro de la aplicación de forma personalizada.

`IInAppMessageManagerListener` también incluye métodos delegados para clics de mensajes y botones, que pueden utilizarse en casos como interceptar un mensaje cuando se hace clic en un botón o mensaje para su posterior procesamiento.

#### Paso 1.2: Engancharse a los métodos del ciclo de vida de la vista IAM (opcional)

La interfaz [`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html) tiene métodos de vista de mensajes dentro de la aplicación que se invocan en distintos puntos del ciclo de vida de la vista de mensajes dentro de la aplicación. Estos métodos se llaman en el orden siguiente

1. [`beforeInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-opened.html): Se llama justo antes de que el mensaje dentro de la aplicación se añada a la vista de la actividad. El mensaje dentro de la aplicación todavía no está visible para el usuario en este momento.
2. [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html): Se llama justo después de añadir el mensaje dentro de la aplicación a la vista de la actividad. El mensaje dentro de la aplicación es ahora visible para el usuario en este momento.
3. [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html): Se llama justo antes de que el mensaje dentro de la aplicación se elimine de la vista de la actividad. El mensaje dentro de la aplicación sigue siendo visible para el usuario en este momento.
4. [`afterInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-closed.html): Se llama justo después de que el mensaje dentro de la aplicación se elimine de la vista de la actividad. El mensaje dentro de la aplicación ya no es visible para el usuario en este momento.

Nota que el tiempo entre [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html) y [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html) es cuando la vista de mensajes dentro de la aplicación está en pantalla, visible para el usuario.

{% alert note %}
No es necesario aplicar estos métodos. Sólo se proporcionan para seguir e informar del ciclo de vida de la vista de mensajes dentro de la aplicación. Puedes dejar vacías las implementaciones de estos métodos.
{% endalert %}
{% endtab %}

{% tab oyente html %}
Crea una clase que implemente [`IHtmlInAppMessageActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-html-in-app-message-action-listener/index.html).

Las devoluciones de llamada en tu `IHtmlInAppMessageActionListener` serán llamadas siempre que el usuario inicie cualquiera de las siguientes acciones dentro del mensaje HTML dentro de la aplicación:

- Haz clic en el botón de cerrar
- Dispara un evento personalizado
- Clic en una URL dentro de un mensaje HTML dentro de la aplicación

{% subtabs %}
{% subtab JAVA %}
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
  public boolean onOtherUrlAction(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
    Toast.makeText(mContext, "Custom url pressed: " + url + " . Ignoring", Toast.LENGTH_LONG).show();
    BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false);
    return true;
  }
}
```
{% endsubtab %}
{% subtab KOTLIN %}
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

    override fun onOtherUrlAction(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle): Boolean {
        Toast.makeText(mContext, "Custom url pressed: $url . Ignoring", Toast.LENGTH_LONG).show()
        BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false)
        return true
    }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Paso 2: Indica a Braze que utilice el receptor personalizado del administrador

{% tabs %}
{% tab oyente global %}
Después de crear `IInAppMessageManagerListener`, llama a `BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener()` para darle instrucciones. `BrazeInAppMessageManager`
para utilizar tu `IInAppMessageManagerListener` personalizado en lugar de la escucha predeterminada. Hazlo en tu [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) antes de cualquier otra llamada a Braze, para que la escucha personalizada se configure antes de que se muestren los mensajes dentro de la aplicación.

#### Alterar los mensajes dentro de la aplicación antes de mostrarlos

Cuando se reciba un nuevo mensaje dentro de la aplicación y ya se esté mostrando un mensaje dentro de la aplicación, el nuevo mensaje se colocará en la parte superior de la pila y se podrá mostrar más adelante.

Sin embargo, si no se muestra ningún mensaje dentro de la aplicación, se llamará al siguiente método delegado en `IInAppMessageManagerListener`:

{% subtabs %}
{% subtab JAVA %}
```java
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
  return InAppMessageOperation.DISPLAY_NOW
}
```
{% endsubtab %}
{% endsubtabs %}

El valor de retorno `InAppMessageOperation()` puede controlar cuándo debe mostrarse el mensaje. El uso sugerido de este método sería retrasar los mensajes en ciertas partes de la aplicación devolviendo `DISPLAY_LATER` cuando los mensajes dentro de la aplicación distrajeran la experiencia del usuario con la aplicación.

| `InAppMessageOperation` valor de retorno | Comportamiento |
| -------------------------- | -------- |
| `DISPLAY_NOW` | Se mostrará el mensaje |
| `DISPLAY_LATER` | El mensaje se devolverá a la pila y se mostrará en la siguiente oportunidad disponible |
| `DISCARD` | El mensaje será descartado |
| `null` | El mensaje será ignorado. Este método **NO** debe devolver `null` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Consulta [`InAppMessageOperation`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/index.html) para más detalles.

{% alert tip %}
Si eliges `DISCARD` el mensaje dentro de la aplicación y lo sustituyes por la vista de tu mensaje dentro de la aplicación, tendrás que registrar manualmente los clics y las impresiones del mensaje dentro de la aplicación.
{% endalert %}

En Android, esto se hace llamando a `logClick` y `logImpression` en los mensajes dentro de la aplicación y a `logButtonClick` en los mensajes inmersivos dentro de la aplicación.

{% alert tip %}
Una vez que un mensaje dentro de la aplicación se ha colocado en la pila, puedes solicitar que se recupere y se muestre en cualquier momento llamando a [`BrazeInAppMessageManager.getInstance().requestDisplayInAppMessage()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/request-display-in-app-message.html). Este método solicita a Braze que muestre el siguiente mensaje dentro de la aplicación disponible en la pila.
{% endalert %}
{% endtab %}

{% tab oyente html %}
Una vez creado tu `IHtmlInAppMessageActionListener`, llama a `BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener()` para indicar a `BrazeInAppMessageManager` que utilice tu `IHtmlInAppMessageActionListener` personalizado en lugar del oyente de acción predeterminado.

Te recomendamos que configures tu `IHtmlInAppMessageActionListener` en tu [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) antes de cualquier otra llamada a Braze. Esto configurará el receptor de acciones personalizado antes de que se muestre cualquier mensaje dentro de la aplicación:

{% subtabs %}
{% subtab JAVA %}
```java
BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener(new CustomHtmlInAppMessageActionListener(context));
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener(CustomHtmlInAppMessageActionListener(context))
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Configuración de fábricas personalizadas

Puedes anular una serie de predeterminados mediante objetos personalizados de fábrica. Se pueden registrar con el SDK de Braze según sea necesario para conseguir los resultados deseados. Sin embargo, si decides anular una fábrica, es probable que tengas que diferir explícitamente al predeterminado o reimplementar la funcionalidad proporcionada por el predeterminado de Braze. El siguiente fragmento de código ilustra cómo proporcionar implementaciones personalizadas de las interfaces `IInAppMessageViewFactory` y `IInAppMessageViewWrapperFactory`.

{% tabs local %}
{% tab Kotlin %}
**Tipos de mensajes dentro de la aplicación**<br>

```kotlin
class BrazeDemoApplication : Application(){
 override fun onCreate() {
    super.onCreate()
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener(true, true))
    BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(CustomInAppMessageViewWrapperFactory())
    BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory(CustomInAppMessageViewFactory())
  }
}
```
{% endtab %}
{% tab Java %}
**Tipos de mensajes dentro de la aplicación**<br> 

```java
public class BrazeDemoApplication extends Application {
  @Override
  public void onCreate{
    super.onCreate();
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener(true, true));
    BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(new CustomInAppMessageViewWrapperFactory());
    BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory(new CustomInAppMessageViewFactory());
  }
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab ver %}
Los tipos de mensajes dentro de la aplicación Braze son lo suficientemente versátiles como para cubrir la mayoría de los casos de uso personalizados. Sin embargo, si quieres definir completamente el aspecto visual de tus mensajes dentro de la aplicación en lugar de utilizar un tipo predeterminado, Braze lo hace posible configurando una fábrica de vistas personalizada.
{% endtab %}

{% tab ver envoltorio %}
El sitio `BrazeInAppMessageManager` se encarga automáticamente de colocar el modelo de mensajes dentro de la aplicación en la jerarquía de vistas de actividad existente de forma predeterminada utilizando [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html). Si necesitas personalizar la forma en que se colocan los mensajes dentro de la aplicación en la jerarquía de vistas, debes utilizar una función personalizada [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html).
{% endtab %}

{% tab animación %}
Los mensajes dentro de la aplicación tienen un comportamiento de animación preestablecido. `Slideup` mensajes se deslizan dentro de la pantalla; `full` y `modal` mensajes aparecen y desaparecen. Si quieres definir comportamientos de animación personalizados para tus mensajes dentro de la aplicación, Braze lo hace posible configurando una fábrica de animación personalizada.
{% endtab %}
{% endtabs %}

### Paso 1: Implementa la fábrica

{% tabs %}
{% tab ver %}
Crea una clase que implemente [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html):

{% subtabs %}
{% subtab JAVA %}
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
{% endsubtab %}
{% subtab KOTLIN %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab ver envoltorio %}
Crea una clase que implemente [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) y devuelva un [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html).

Esta fábrica se llama inmediatamente después de crear la vista de mensajes dentro de la aplicación. La forma más sencilla de implementar un programa personalizado [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) es ampliar el [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html) predeterminado:

{% subtabs %}
{% subtab JAVA %}
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
{% endsubtab %}
{% subtab KOTLIN %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab animación %}
Crea una clase que implemente [`IInAppMessageAnimationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-animation-factory/index.html):

{% subtabs %}
{% subtab JAVA %}
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
{% endsubtab %}
{% subtab KOTLIN %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Paso 2: Ordena a Braze que utilice la fábrica

{% tabs %}
{% tab ver %}
Una vez creado tu `IInAppMessageViewFactory`, llama a `BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory()` para dar instrucciones. `BrazeInAppMessageManager`
para utilizar tu `IInAppMessageViewFactory` personalizado en lugar de la vista predeterminada de fábrica.

{% alert tip %}
Te recomendamos que configures tu `IInAppMessageViewFactory` en tu `Application.onCreate()` antes de cualquier otra llamada a Braze. Esto establecerá la fábrica de visualizaciones personalizadas antes de que se muestre cualquier mensaje dentro de la aplicación.
{% endalert %}

#### Cómo funciona

La vista de mensajes dentro de la aplicación `slideup` implementa [`IInAppMessageView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-view/index.html). Las vistas de mensajes de tipo `full` y `modal` implementan [`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html). Implementar una de estas clases permite a Braze añadir escuchadores de clics a tu vista personalizada cuando proceda. Todas las clases de vista Braze extienden la clase [`View`](http://developer.android.com/reference/android/view/View.html) de Android.

Implementar `IInAppMessageView` te permite definir una determinada parte de tu vista personalizada como clicable. Implementar [`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html) te permite definir vistas de botón de mensaje y una vista de botón de cierre.
{% endtab %}

{% tab ver envoltorio %}
Después de crear tu [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) se haya creado, llama a [`BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-custom-in-app-message-view-factory.html) para indicar a `BrazeInAppMessageManager` que utilice tu vista personalizada [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) en lugar de la fábrica de envoltorios de vistas predeterminada.

Te recomendamos que configures tu [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) en tu [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) antes de cualquier otra llamada a Braze. Esto configurará la fábrica del envoltorio de la vista personalizada antes de que se muestre cualquier mensaje dentro de la aplicación:

{% subtabs %}
{% subtab JAVA %}
```java
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(new CustomInAppMessageViewWrapper());
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(CustomInAppMessageViewWrapper())
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab animación %}
Una vez creado tu `IInAppMessageAnimationFactory`, llama a `BrazeInAppMessageManager.getInstance().setCustomInAppMessageAnimationFactory()` para dar instrucciones. `BrazeInAppMessageManager`
para utilizar tu `IInAppMessageAnimationFactory` personalizado en lugar de la fábrica de animaciones predeterminada.

Te recomendamos que configures tu `IInAppMessageAnimationFactory` en tu [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) antes de cualquier otra llamada a Braze. Esto establecerá la fábrica de animación personalizada antes de que se muestre cualquier mensaje dentro de la aplicación.
{% endtab %}
{% endtabs %}

## Estilos personalizados

Los elementos de la interfaz de usuario de Braze vienen con un aspecto predeterminado que se ajusta a las directrices de la interfaz de usuario estándar de Android y proporciona una experiencia sin fisuras. Este artículo de referencia trata del estilo personalizado de la mensajería dentro de la aplicación para tu aplicación Android o FireOS.

### Configuración de un estilo predeterminado

Puedes ver los estilos predeterminados en el archivo del SDK de Braze [`styles.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml):

```xml
  <style name="Braze"/>
  <style name="Braze.InAppMessage"/>
  <style name="Braze.InAppMessage.Header">
    <item name="android:layout_height">wrap_content</item>
    <item name="android:layout_width">match_parent</item>
    <item name="android:padding">0.0dp</item>
    <item name="android:background">@android:color/transparent</item>
    <item name="android:textColor">@color/com_braze_inappmessage_header_text</item>
    <item name="android:textSize">20.0sp</item>
    <item name="android:lineSpacingMultiplier">1.3</item>
    <item name="android:gravity">center</item>
    <item name="android:textStyle">bold</item>
    <item name="android:layout_centerHorizontal">true</item>
  </style>
```

Si lo prefieres, puedes anular estos estilos para crear un aspecto que se adapte mejor a tu aplicación.

Para anular un estilo, cópialo en su totalidad en el archivo `styles.xml` de tu proyecto y haz modificaciones. Debes copiar todo el estilo en tu archivo local `styles.xml` para que todos los atributos estén correctamente configurados. Ten en cuenta que estos estilos personalizados son para cambios en elementos individuales de la interfaz de usuario, no para cambios generales en los diseños. Los cambios a nivel de diseño deben gestionarse con vistas personalizadas.

{% alert note %}
Puedes personalizar algunos colores directamente en tu campaña Braze sin modificar el XML. Ten en cuenta que los colores establecidos en el panel de Braze anularán los colores que establezcas en cualquier otro lugar.
{% endalert %}

### Personalizar la fuente

Puedes establecer un tipo de letra personalizado localizándolo en el directorio `res/font`. Para utilizarlo, anula el estilo para el texto del mensaje, los encabezados y el texto del botón y utiliza el atributo `fontFamily` para indicar a Braze que utilice tu familia de fuentes personalizada.

Por ejemplo, para actualizar la fuente del texto de tu botón de mensajes dentro de la aplicación, anula el estilo `Braze.InAppMessage.Button` y haz referencia a tu familia de fuentes personalizada. El valor del atributo debe apuntar a una familia de fuentes de tu directorio `res/font`.

Aquí tienes un ejemplo truncado con una familia de fuentes personalizada, `my_custom_font_family`, a la que se hace referencia en la última línea:

```xml
  <style name="Braze.InAppMessage.Button">
    <item name="android:layout_height">wrap_content</item>
    ...
    <item name="android:paddingBottom">15.0dp</item>
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

Aparte del estilo `Braze.InAppMessage.Button` para el texto de los botones, el estilo para el texto de los mensajes es `Braze.InAppMessage.Message` y el estilo para las cabeceras de los mensajes es `Braze.InAppMessage.Header`. Si quieres utilizar tu familia de fuentes personalizada en todo el texto posible de los mensajes dentro de la aplicación, puedes establecer tu familia de fuentes en el estilo `Braze.InAppMessage`, que es el estilo padre de todos los mensajes dentro de la aplicación.

{% alert important %}
Al igual que con otros estilos personalizados, debes copiar todo el estilo en tu archivo local `styles.xml` para que todos los atributos estén correctamente configurados.
{% endalert %}

## Desestimación de mensajes

### Desactivar el botón de retroceso

De manera predeterminada, el botón de retroceso del hardware descarta los mensajes dentro de la aplicación de Braze. Este comportamiento puede desactivarse por mensaje mediante [`BrazeInAppMessageManager.setBackButtonDismissesInAppMessageView()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-back-button-dismisses-in-app-message-view.html). 

En el siguiente ejemplo, `disable_back_button` es un par clave-valor personalizado establecido en el mensaje dentro de la aplicación que indica si el mensaje debe permitir el botón de retroceso para descartar el mensaje:

{% tabs %}
{% tab JAVA %}
```java
BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(new DefaultInAppMessageManagerListener() {
  @Override
  public void beforeInAppMessageViewOpened(View inAppMessageView, IInAppMessage inAppMessage) {
    super.beforeInAppMessageViewOpened(inAppMessageView, inAppMessage);
    final Map<String, String> extras = inAppMessage.getExtras();
    if (extras != null && extras.containsKey("disable_back_button")) {
      BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(false);
    }
  }

  @Override
  public void afterInAppMessageViewClosed(IInAppMessage inAppMessage) {
    super.afterInAppMessageViewClosed(inAppMessage);
    BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(true);
  }
});
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(object : DefaultInAppMessageManagerListener() {
  override fun beforeInAppMessageViewOpened(inAppMessageView: View, inAppMessage: IInAppMessage) {
    super.beforeInAppMessageViewOpened(inAppMessageView, inAppMessage)
    val extras = inAppMessage.extras
    if (extras != null && extras.containsKey("disable_back_button")) {
      BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(false)
    }
  }

  override fun afterInAppMessageViewClosed(inAppMessage: IInAppMessage) {
    super.afterInAppMessageViewClosed(inAppMessage)
    BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(true)
  }
})
```
{% endtab %}
{% endtabs %}

{% alert note %}
Ten en cuenta que si esta función está desactivada, se utilizará en su lugar el comportamiento predeterminado del botón de retroceso del hardware de la actividad anfitriona. Esto puede hacer que el botón Atrás cierre la aplicación en lugar del mensaje dentro de la aplicación que se muestra.
{% endalert %}

### Habilitación de los despidos fuera del grifo

Por predeterminado, el cierre del modal mediante un toque externo está configurado en `false`. Si estableces este valor en `true`, el mensaje modal dentro de la aplicación se cancelará cuando el usuario pulse fuera del mensaje dentro de la aplicación. Este comportamiento se puede alternar llamando a:

```java
BrazeInAppMessageManager.getInstance().setClickOutsideModalViewDismissInAppMessageView(true)
```

## Personalizar la orientación

Para establecer una orientación fija para un mensaje dentro [de la aplicación, establece primero una escucha personalizada del administrador de mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android#android_setting-custom-manager-listeners). A continuación, actualiza la orientación en el objeto `IInAppMessage` en el método delegado `beforeInAppMessageDisplayed()`:

{% tabs %}
{% tab JAVA %}
```java
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  // Set the orientation to portrait
  inAppMessage.setOrientation(Orientation.PORTRAIT);
  return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
  // Set the orientation to portrait
  inAppMessage.orientation = Orientation.PORTRAIT
  return InAppMessageOperation.DISPLAY_NOW
}
```
{% endtab %}
{% endtabs %}

Para dispositivos de tableta, los mensajes dentro de la aplicación aparecerán en el estilo de orientación preferido por el usuario, independientemente de la orientación real de la pantalla.

## Desactivar el tema oscuro {#android-in-app-message-dark-theme-customization}

Por predeterminado, `IInAppMessageManagerListener`'s `beforeInAppMessageDisplayed()` comprueba la configuración del sistema y habilita condicionalmente el estilo de tema oscuro en el mensaje con el siguiente código:

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

Para cambiar esto, puedes llamar a [`enableDarkTheme`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-themeable/enable-dark-theme.html) en cualquier paso del proceso previo a la visualización para aplicar tu propia lógica condicional.

## Personalizar el aviso de revisión de Google Play

Debido a las limitaciones y restricciones establecidas por Google, Braze no admite actualmente los avisos de revisión personalizados de Google Play. Mientras que algunos usuarios han podido integrar estas indicaciones con éxito, otros han mostrado bajas tasas de éxito debido a [las cuotas de Google Play](https://developer.android.com/guide/playcore/in-app-review#quotas). Realiza la integración por tu cuenta y riesgo. Consulta la documentación sobre [las indicaciones de revisión dentro de la aplicación en Google Play](https://developer.android.com/guide/playcore/in-app-review).
