---
nav_title: Guía de Implementación Avanzada (Opcional)
article_title: Guía de implementación de mensajes dentro de la aplicación para Android (Opcional)
platform: Android
page_order: 6
description: "Esta guía de implementación avanzada abarca consideraciones sobre códigos de mensajes dentro de la aplicación de Android y FireOS, tres casos de uso construidos por nuestro equipo y fragmentos de código que los acompañan."
channel:
  - in-app messages
---
<br>
{% alert important %}
¿Buscas la guía básica de integración del desarrollador de mensajes dentro de la aplicación? Encuéntralo [aquí]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/#in-app-messaging-integration).
{% endalert %}

# Guía de implementación avanzada

> Esta guía de implementación opcional y avanzada abarca consideraciones sobre códigos de mensajes dentro de la aplicación, tres casos de uso personalizados creados por nuestro equipo y fragmentos de código que los acompañan. ¡Visita nuestro repositorio de demostraciones Braze [aquí](https://github.com/braze-inc/braze-growth-shares-android-demo-app)! Ten en cuenta que esta guía de implementación se centra en una implementación de Kotlin, pero se proporcionan fragmentos de código Java para los interesados. ¿Buscas implementaciones HTML? ¡Echa un vistazo a nuestro [repositorio de plantillas HTML](https://github.com/braze-inc/in-app-message-templates)!

## Consideraciones sobre códigos

La siguiente guía ofrece una integración personalizada opcional para desarrolladores que se puede utilizar además de los mensajes predeterminados dentro de la aplicación. Se incluyen componentes de vista y fábricas personalizadas según sea necesario con cada caso de uso, ofreciendo ejemplos para ampliar la funcionalidad y personalizar de forma nativa el aspecto de tus mensajes dentro de la aplicación. En algunas instancias, hay varias formas de conseguir resultados similares. La implementación óptima dependerá del caso de uso concreto.

### Fábricas personalizadas

El SDK de Braze permite a los desarrolladores anular una serie de valores predeterminados mediante objetos personalizados de fábrica. Se pueden registrar con el SDK de Braze según sea necesario para conseguir los resultados deseados. En la mayoría de los casos, sin embargo, si decides anular una fábrica, tendrás que remitirte explícitamente a la predeterminada o volver a implementar la funcionalidad proporcionada por la predeterminada de Braze. El siguiente fragmento de código ilustra cómo proporcionar implementaciones personalizadas de las interfaces `IInAppMessageViewFactory` y `IInAppMessageViewWrapperFactory`. Una vez que tengas una sólida comprensión de los conceptos que hay detrás de anular nuestras fábricas predeterminadas, consulta nuestros [casos de uso](#sample-use-cases) para empezar a implementar la funcionalidad de mensajería dentro de la aplicación personalizada.

{% tabs %}
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

## Casos prácticos

A continuación te presentamos tres casos de uso. Cada caso de uso tiene fragmentos de código y un vistazo a cómo pueden verse y utilizarse los mensajes dentro de la aplicación en el panel de Braze:
- [Mensaje personalizado deslizamiento hacia arriba dentro de la aplicación](#custom-slideup-in-app-message)
- [Mensaje modal personalizado dentro de la aplicación](#custom-modal-in-app-message)
- [Mensaje completo personalizado dentro de la aplicación](#custom-full-in-app-message)

### Mensaje personalizado deslizable dentro de la aplicación

Mientras creas tu mensaje deslizable dentro de la aplicación, puede que notes que no puedes modificar la ubicación del mensaje utilizando los métodos predeterminados. Una modificación como ésta es posible subclasificando la clase `DefaultInAppMessageViewWrapper` para ajustar los parámetros de diseño. Puedes ajustar la posición final en la pantalla anulando el método `getLayoutParams` que devuelve el `LayoutParams` modificado con tus propios valores de posicionamiento personalizados. Visita el [CustomSlideUpInAppMessageViewWrapper](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/inapp/slideup/CustomSlideUpInAppMessageViewWrapper.kt) para empezar.

#### Envoltorio de vista personalizado<br><br>

{% tabs %}
{% tab Kotlin %}
**Anula y devuelve parámetros de diseño personalizados**<br>
Dentro del método `getLayoutParams`, puedes utilizar el método de la superclase para acceder al `LayoutParameters` original del mensaje dentro de la aplicación. Luego, puedes ajustar la posición sumando o restando según desees.

```kotlin
class CustomSlideUpInAppMessageViewWrapper(inAppMessageView: View?,
                                           inAppMessage: IInAppMessage?,
                                           inAppMessageViewLifecycleListener: IInAppMessageViewLifecycleListener?,
                                           configurationProvider: BrazeConfigurationProvider?,
                                           openingAnimation: Animation?,
                                           closingAnimation: Animation?,
                                           clickableInAppMessageView: View?) : DefaultInAppMessageViewWrapper(inAppMessageView,
    inAppMessage,
    inAppMessageViewLifecycleListener,
    configurationProvider,
    openingAnimation,
    closingAnimation,
    clickableInAppMessageView) {

    override fun getLayoutParams(inAppMessage: IInAppMessage?): ViewGroup.LayoutParams {
        val params = super.getLayoutParams(inAppMessage) as FrameLayout.LayoutParams
        params.bottomMargin = params.bottomMargin + 500 //move the view up by 500 pixels
        return params
    }
}
```
{% endtab %}
{% tab Java %}
**Anula y devuelve parámetros de diseño personalizados**<br>
Dentro del método `getLayoutParams`, puedes utilizar el método de la superclase para acceder al `LayoutParameters` original del mensaje dentro de la aplicación. Luego, puedes ajustar la posición sumando o restando según desees.

```java
class CustomSlideUpInAppMessageViewWrapper extends DefaultInAppMessageViewWrapper {

    public CustomInAppMessageViewWrapper(View inAppMessageView,
                                           IInAppMessage inAppMessage,
                                           IInAppMessageViewLifecycleListener inAppMessageViewLifecycleListener,
                                           BrazeConfigurationProvider configurationProvider,
                                           Animation openingAnimation,
                                           Animation closingAnimation,
                                           View clickableInAppMessageView){
        super(inAppMessageView,
                inAppMessage,
                inAppMessageViewLifecycleListener,
                configurationProvider,
                openingAnimation,
                closingAnimation,
                clickableInAppMessageView)

    }
    
    @Override
    public ViewGroup.LayoutParams getLayoutParams(IInAppMessage inAppMessage){
        FrameLayout.LayoutParams params = (FrameLayout.LayoutParams)super.getLayoutParams(inAppMessage)
        params.bottomMargin = params.bottomMargin + 500 //move the view up by 500 pixels
        return params
    }
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Kotlin %}
**Suministra una fábrica personalizada para devolver tu envoltorio personalizado**<br>
Para que el SDK de Braze utilice tu envoltorio personalizado, también tienes que proporcionar una implementación personalizada de `IInAppMessageViewWrapperFactory` que devuelva tu envoltorio personalizado. Puedes implementar directamente el método `IInAppMessageViewWrapperFactory`, o bien subclasificar `BrazeInAppMessageViewWrapperFactory` y anular únicamente el método `createInAppMessageViewWrapper`:

```kotlin
class CustomInAppMessageViewWrapperFactory : BrazeInAppMessageViewWrapperFactory() {

    override fun createInAppMessageViewWrapper(
        inAppMessageView: View?,
        inAppMessage: IInAppMessage?,
        inAppMessageViewLifecycleListener: IInAppMessageViewLifecycleListener?,
        configurationProvider: BrazeConfigurationProvider?,
        openingAnimation: Animation?,
        closingAnimation: Animation?,
        clickableInAppMessageView: View?
    ): IInAppMessageViewWrapper {
        return if (inAppMessage is InAppMessageSlideup) {
            CustomSlideUpInAppMessageViewWrapper( //return our custom view wrapper only for slideups
                inAppMessageView,
                inAppMessage,
                inAppMessageViewLifecycleListener,
                configurationProvider,
                openingAnimation,
                closingAnimation,
                clickableInAppMessageView
            )
        } else {
            super.createInAppMessageViewWrapper( //defer to the default implementation for all other IAM types
                inAppMessageView,
                inAppMessage,
                inAppMessageViewLifecycleListener,
                configurationProvider,
                openingAnimation,
                closingAnimation,
                clickableInAppMessageView
            )
        }
    }
}
```
{% endtab %}
{% tab Java %}
**Suministra una fábrica personalizada para devolver tu envoltorio personalizado**<br>
Para que el SDK de Braze utilice tu envoltorio personalizado, tienes que proporcionar una implementación de `IInAppMessageViewWrapperFactory` personalizada que devuelva tu envoltorio personalizado. Puedes implementar directamente el método `IInAppMessageViewWrapperFactory`, o bien subclasificar `BrazeInAppMessageViewWrapperFactory` y anular únicamente el método `createInAppMessageViewWrapper`:

```java
class CustomInAppMessageViewWrapperFactory extends BrazeInAppMessageViewWrapperFactory {
    @Override
    public IInAppMessageViewWrapper createInAppMessageViewWrapper(View inAppMessageView, 
        IInAppMessage inAppMessage, 
        IInAppMessageViewLifecycleListener inAppMessageViewLifecycleListener, 
        BrazeConfigurationProvider configurationProvider, 
        Animation openingAnimation, 
        Animation closingAnimation, 
        View clickableInAppMessageView){
        if (inAppMessage instanceof InAppMessageSlideup){
            return new CustomSlideUpInAppMessageViewWrapper( //return our custom view wrapper only for slideups
                inAppMessageView,
                inAppMessage,
                inAppMessageViewLifecycleListener,
                configurationProvider,
                openingAnimation,
                closingAnimation,
                clickableInAppMessageView);
        }else{
            return super.createInAppMessageViewWrapper(//defer to the default implementation for all other IAM types
                inAppMessageView,
                inAppMessage,
                inAppMessageViewLifecycleListener,
                configurationProvider,
                openingAnimation,
                closingAnimation,
                clickableInAppMessageView);
        }
    }
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Kotlin %}
**Registra tu fábrica en Braze**<br>
Una vez que hayas creado tu fábrica envolvente personalizada, regístrala en el SDK envolvente de Braze a través de `BrazeInAppMessageManager`:

```kotlin
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(CustomInAppMessageViewWrapperFactory())
```
{% endtab %}
{% tab Java %}
**Registra tu fábrica en Braze**<br>
Una vez que hayas creado tu fábrica envolvente personalizada, regístrala en el SDK envolvente de Braze a través de `BrazeInAppMessageManager`:

```java
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(new CustomInAppMessageViewWrapperFactory());
```
{% endtab %}
{% endtabs %}

### Mensaje modal personalizado dentro de la aplicación

Una `BrazeInAppMessageModalView` puede subclasificarse para aprovechar una `Spinner` que ofrezca formas atractivas de recopilar valiosos atributos del usuario. El siguiente ejemplo muestra cómo puedes utilizar el Contenido conectado para capturar atributos personalizados de una lista dinámica de elementos. Visita la página [`TeamPickerView`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/inapp/modal/TeamPickerView.kt) para empezar.

{% tabs %}
{% tab Kotlin %}
**Utilizando `view_type` para el comportamiento de visualización de la IU**<br>
El objeto `IInAppMessage` tiene un diccionario `extras` que podemos consultar para encontrar la clave `view_type` (si existe) y mostrar el tipo de vista correcto. Es importante tener en cuenta que los mensajes dentro de la aplicación se configuran para cada mensaje, por lo que las vistas modales personalizadas y predeterminadas pueden funcionar armoniosamente.

```kotlin
override fun createInAppMessageView(activity: Activity, inAppMessage: IInAppMessage): View {
  return when {
      inAppMessage.extras?.get("view_type") == "picker" -> {
          getCustomPickerView(activity, inAppMessage)
      }
      //...
      else -> {
          //Defer to default
          BrazeInAppMessageManager
              .getInstance()
              .getDefaultInAppMessageViewFactory(inAppMessage).createInAppMessageView(activity, inAppMessage)
      }
  }
}
```
{% endtab %}
{% tab Java %}
**Utilizando `view_type` para el comportamiento de visualización de la IU**<br>
El objeto `IInAppMessage` tiene un diccionario `extras` que podemos consultar para encontrar la clave `view_type` (si existe) y mostrar el tipo de vista correcto. Es importante tener en cuenta que los mensajes dentro de la aplicación se configuran para cada mensaje, por lo que las vistas modales personalizadas y predeterminadas pueden funcionar armoniosamente.

```java
@Override
public View createInAppMessageView(Activity activity, IInAppMessage inAppMessage) {
    if("picker".equals(inAppMessage.getExtras().get("view_type"))){
        return getCustomPickerView(activity, inAppMessage);
    } else {
        //Defer to default
        BrazeInAppMessageManager
          .getInstance()
          .getDefaultInAppMessageViewFactory(inAppMessage)
          .createInAppMessageView(activity, inAppMessage);
    }
}
```
{% endtab %}
{% endtabs %}

**Anula y proporciona una vista personalizada**<br>
Proporciona un diseño que imite el mensaje dentro de la aplicación modal estándar, pero proporciona tu vista como elemento raíz y luego infla ese diseño 
```xml
<com.braze.advancedsamples.inapp.modal.TeamPickerView xmlns:android="http://schemas.android.com/apk/res/android"
                                                      xmlns:tools="http://schemas.android.com/tools"
                                                      android:layout_width="match_parent"
                                                      android:layout_height="match_parent"
                                                      android:padding="0.0dp"
                                                      android:id="@+id/team_picker_view">
    <!-- ... -->
    <Spinner android:layout_width="match_parent" android:layout_height="wrap_content"
                     android:id="@+id/team_spinner"/>
    <!-- ... -->                                                      
</com.braze.advancedsamples.inapp.modal.TeamPickerView>
```

{% tabs %}
{% tab Kotlin %}
**Infla y personaliza la vista**<br>
Antes de recargar los componentes de `Spinner`, la variable de mensaje `inAppMessage` se muestra como una cadena. Este mensaje debe formatearse como una matriz de elementos para que se muestre correctamente. Por ejemplo, esto se puede conseguir utilizando `String.split(",")`.

```kotlin
private fun getCustomView(activity: Activity, inAppMessage: IInAppMessage): TeamPickerView {
        val view = activity.layoutInflater.inflate(R.layout.team_picker_dialog, null) as TeamPickerView
        val teams = inAppMessage.message.split(",")
        view.setTeams(teams)
        return view
    }
```
{% endtab %}
{% tab Java %}
**Infla y personaliza la vista**<br>
Antes de recargar los componentes de `Spinner`, la variable de mensaje `inAppMessage` se muestra como una _cadena_. Este mensaje debe formatearse como una matriz de elementos para que se muestre correctamente. Por ejemplo, esto se puede conseguir utilizando `String.split(",")`.

```java
private TeamPickerView getCustomView(Activity activity, IInAppMessage inAppMessage) {
        TeamPickerView view = (TeamPickerView) activity.getLayoutInflater().inflate(R.layout.team_picker_dialog, null);
        String[] teams = inAppMessage.getMessage().split(",");
        view.setTeams(teams);
        return view
    }
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Kotlin %}
**Asignar atributo personalizado**<br>
Utilizando la subclase de la vista, después de que un usuario pulse enviar, pasa el atributo con su correspondiente valor seleccionado a Braze y descarta el mensaje dentro de la aplicación llamando a `messageClickableView.performClick()`.

```kotlin
    override fun onClick(v: View?) {
        val selectedTeam = spinner.selectedItem as String
        messageClickableView.performClick()
        Braze.getInstance(ctx).getCurrentUser { brazeUser ->
            brazeUser?.setCustomUserAttribute("FavoriteTeam", selectedTeam)
        }
    }
```
{% endtab %}
{% tab Java %}
**Asignar atributo personalizado**<br>
Utilizando la subclase de la vista, después de que un usuario pulse enviar, pasa el atributo con su correspondiente valor seleccionado a Braze y descarta el mensaje dentro de la aplicación llamando a `messageClickableView.performClick()`.

```java
    @Override
    public void onClick(View v) {
        String selectedTeam = (String) spinner.getSelectedItem();
        messageClickableView.performClick();
        Braze.getInstance(ctx).getCurrentUser(brazeUser -> {
            brazeUser.setCustomUserAttribute("FavoriteTeam", selectedTeam);
        });
    }
```
{% endtab %}
{% endtabs %}

### Mensaje completo personalizado dentro de la aplicación
Implementar un mensaje dentro de la aplicación inmersivo (a pantalla completa) totalmente personalizado implica un enfoque similar al descrito en la sección para implementar un [mensaje dentro de la aplicación modal personalizado](#custom-modal-in-app-message). En esta instancia, sin embargo, simplemente amplía `BrazeInAppMessageFullView` y personalízalo como necesites. Recuerda que la vista se mostrará sobre la UI de la aplicación, y las vistas en Android por defecto son transparentes. Esto significa que tendrás que definir un fondo tal que el mensaje dentro de la aplicación oculte el contenido que hay detrás. Al ampliar `BrazeInAppMessageFullView`, el SDK de Braze se encargará de interceptar los eventos táctiles de la vista y de realizar la acción adecuada. Al igual que con el ejemplo modal, puedes anular este comportamiento para determinados controles (como los controles de `Switch` ) para recoger la opinión del usuario.

{% tabs %}
{% tab Kotlin %}
**Utilizando `view_type` para el comportamiento de visualización de la IU**<br>
Añadiremos otro `view_type` extra para nuestra nueva personalización inmersiva. Revisando el método `createInAppMessageView`, añade una opción para la IU de "interruptores":

```kotlin
override fun createInAppMessageView(activity: Activity, inAppMessage: IInAppMessage): View {
    return when {
        inAppMessage.extras?.get("view_type") == "picker" -> {
            getCustomPickerView(activity, inAppMessage)
        }
        inAppMessage.extras?.get("view_type") == "switches" -> {
            getCustomImmersiveView(activity, inAppMessage) // new customization
        }
        else -> {
            //Defer to default
            BrazeInAppMessageManager
                .getInstance()
                .getDefaultInAppMessageViewFactory(inAppMessage).createInAppMessageView(activity, inAppMessage)
        }
    }
}
```
{% endtab %}
{% tab Java %}
**Utilizando `view_type` para el comportamiento de visualización de la IU**<br>
Añadiremos otro `view_type` extra para nuestra nueva personalización inmersiva. Revisando el método `createInAppMessageView`, añade una opción para la IU de "interruptores":

```java
@Override
public View createInAppMessageView(Activity activity, IInAppMessage inAppMessage) {
    if("picker".equals(inAppMessage.getExtras().get("view_type"))){
        return getCustomPickerView(activity, inAppMessage);
    } else if ("switches".equals(inAppMessage.getExtras().get("view_type"))) {
        return getCustomImmersiveView(activity, inAppMessage); // new customization
    } else {
        //Defer to default
        BrazeInAppMessageManager
          .getInstance()
          .getDefaultInAppMessageViewFactory(inAppMessage)
          .createInAppMessageView(activity, inAppMessage);
    }
}
```
{% endtab %}
{% endtabs %}

**Anula y proporciona una vista personalizada**<br>
Proporciona un diseño que imite el mensaje dentro de la aplicación modal estándar, pero proporciona tu vista como elemento raíz y luego infla ese diseño 
```xml
<?xml version="1.0" encoding="utf-8"?>
<com.braze.advancedsamples.immersive.CustomImmersiveInAppMessage
        xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas.android.com/tools" android:layout_width="match_parent"
        android:layout_height="wrap_content">
    <!-- giving the parent layout a white backround color will obscure the app behind the IAM. You could also do this within your custom view -->
    <LinearLayout android:background="@color/white" android:layout_width="match_parent" android:layout_height="match_parent" android:gravity="center"> 
        <!-- ... -->
        <androidx.recyclerview.widget.RecyclerView android:layout_width="match_parent"
                                                       android:layout_height="wrap_content"
                                                       android:id="@+id/option_list"/>
        <!-- ... -->
    </LinearLayout>
</com.braze.advancedsamples.immersive.CustomImmersiveInAppMessage>
```

{% tabs %}
{% tab Kotlin %}
**Infla y personaliza la vista**<br>
Antes de configurar las opciones del componente `RecyclerView`, la variable de mensaje `inAppMessage` se muestra como una _cadena_. Este mensaje debe formatearse como una matriz de elementos para que se muestre correctamente. Por ejemplo, esto se puede conseguir utilizando `String.split(",")`. Las páginas `title` y `subtitle` también se extraen del paquete `extras`.

```kotlin
private fun getCustomImmersiveView(activity: Activity, inAppMessage: IInAppMessage): CustomImmersiveInAppMessage{
    val view = activity.layoutInflater.inflate(R.layout.full_screen_iam, null) as CustomImmersiveInAppMessage
    val options = inAppMessage.message.split(",")
    view.setOptions(options)
    inAppMessage.extras?.get("title").let { view.setTitle(it) }
    inAppMessage.extras?.get("subtitle").let {view.setSubtitle(it) }
    return view
}
```
{% endtab %}
{% tab Java %}
**Infla y personaliza la vista**<br>
Antes de configurar las opciones del componente `RecyclerView`, la variable de mensaje `inAppMessage` se muestra como una _cadena_. Este mensaje debe formatearse como una matriz de elementos para que se muestre correctamente. Por ejemplo, esto se puede conseguir utilizando `String.split(",")`. Las páginas `title` y `subtitle` también se extraen del paquete `extras`.

```java
private CustomImmersiveInAppMessage getCustomImmersiveView(Activity activity, IInAppMessage inAppMessage) {
    CustomImmersiveInAppMessage view = (CustomImmersiveInAppMessage) activity.layoutInflater.inflate(R.layout.full_screen_iam, null);
    String[] options = inAppMessage.message.split(",");
    view.setOptions(options);
    String title = inAppMessage.getExtras().get("title");
    view.setTitle(title);
    String subtitle = inAppMessage.getExtras().get("subtitle"); 
    view.setSubtitle(subtitle);
    return view;
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Kotlin %}
**Asignar atributo personalizado**<br>
Utilizando la subclase vista, después de que un usuario alterne uno de los interruptores, pasa el atributo asociado y el estado de alternar a Braze.

```kotlin
fun logClick(value:String, checked:Boolean){
    Braze.getInstance(ctx).logCustomEvent("SwitchChanged", BrazeProperties())
}

inner class OptionViewHolder(item: View): RecyclerView.ViewHolder(item), View.OnClickListener{

    var value: String = ""

    override fun onClick(p0: View?) {
        if (p0 is Switch){
            val checked = p0.isChecked
            p0.isChecked = !p0.isChecked
            logClick(value, checked)
        }
    }
}
override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): OptionViewHolder {
    return OptionViewHolder(mInflater.inflate(R.layout.switch_cell, null))
}

override fun onBindViewHolder(holder: OptionViewHolder, position: Int) {
    holder.itemView.findViewById<TextView>(R.id.label).text = options[position]
    holder.value = options[position]
}
```
{% endtab %}
{% tab Java %}
**Asignar atributo personalizado**<br>
Utilizando la subclase vista, después de que un usuario alterne uno de los interruptores, pasa el atributo asociado y el estado de alternar a Braze.

```java
private void logClick(String value, boolean checked){
    Braze.getInstance(ctx).logCustomEvent("SwitchChanged", new BrazeProperties());
}

private class OptionViewHolder extends RecyclerView.ViewHolder, implements View.OnClickListener{

    private String value = "";

    public OptionViewHolder(View item){
        super(item);
    }

   
    @Override
    public void onClick(View view) {
        if (view instanceof Switch){
            Switch switchView = (Switch) view;
            boolean checked = switchView.isChecked;
            switchView.isChecked = !switchView.isChecked;
            logClick(value, checked)
        }
    }
}

@Override
public OptionViewHolder onCreateViewHolder(ViewGroup parent, Int viewType) {
    return new OptionViewHolder(mInflater.inflate(R.layout.switch_cell, null));
}

@Override
public void onBindViewHolder(OptionViewHolder holder, Int position) {
    ((TextView)holder.getItemView().findViewById(R.id.label)).setText(options.get(position));
    holder.value = options.get(position);
}
```
{% endtab %}
{% endtabs %}

#### Interceptar toques de mensajes dentro de la aplicación
![Un dispositivo Android que muestra filas de configuraciones y alternancias. La vista personalizada maneja los botones, y cualquier toque fuera de los controles de los botones es manejado por el mensaje dentro de la aplicación y lo descartará.]({% image_buster /assets/img/iam_implementation_guide_android.png %}){: style="float:right;max-width:30%;margin-left:10px;border:0"}
Interceptar los toques de mensajes dentro de la aplicación es crucial para que los botones personalizados de mensajes completos dentro de la aplicación funcionen correctamente. Por predeterminado, todas las vistas de mensajes dentro de la aplicación añaden escuchas `onClick` al mensaje, para que los usuarios puedan descartar mensajes sin botones. Cuando añades controles personalizados que deben responder a la entrada del usuario (como botones personalizados), puedes registrar un receptor `onClick` con la vista de forma normal. Cualquier toque fuera de los controles personalizados descartará el mensaje dentro de la aplicación como de costumbre, mientras que los toques recibidos por los controles personalizados invocarán a tu receptor `onClick`. 

