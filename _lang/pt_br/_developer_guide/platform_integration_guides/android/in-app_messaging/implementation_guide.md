---
nav_title: Guia de implementação avançada (opcional)
article_title: Guia de implementação de mensagem no app para Android (Opcional)
platform: Android
page_order: 6
description: "Este guia de implementação avançado traz considerações de código de mensagem no app para Android e FireOS, três casos de uso criados por nossa equipe e snippets que os acompanham."
channel:
  - in-app messages
---
<br>
{% alert important %}
Está procurando o guia básico para desenvolvedores de integração de mensagens no app? Acesse [aqui]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/#in-app-messaging-integration).
{% endalert %}

# Guia de implementação avançada

> Este guia de implementação opcional e avançado cobre considerações de código de mensagem no app, três casos de uso personalizados criados por nossa equipe e trechos de código acompanhantes. Visite nosso repositório de Demonstração Braze [aqui](https://github.com/braze-inc/braze-growth-shares-android-demo-app)! Note que este guia de implementação está centrado em uma implementação Kotlin, mas são fornecidos trechos em Java para os interessados. Procurando por implementações HTML? Dê uma olhada em nosso [repositório de modelos HTML](https://github.com/braze-inc/in-app-message-templates)!

## Considerações de código

O guia a seguir oferece uma integração de desenvolvedor personalizada opcional para ser usada além das mensagens no app padrão. Componentes de visualização personalizados e fábricas são incluídos conforme necessário com cada caso de uso, oferecendo exemplos para estender a funcionalidade e personalizar nativamente a aparência e a sensação de suas mensagens no app. Em alguns casos, existem várias maneiras de alcançar resultados semelhantes. A implementação ideal dependerá do caso de uso específico.

### Fábricas personalizadas

O SDK da Braze permite que os desenvolvedores substituam vários padrões por meio de objetos de fábrica personalizados. Esses podem ser registrados com o SDK da Braze conforme necessário para alcançar os resultados desejados. Na maioria dos casos, no entanto, se você decidir substituir uma fábrica, precisará ou adiar explicitamente para o padrão ou reimplementar a funcionalidade fornecida pelo padrão da Braze. O trecho de código a seguir ilustra como fornecer implementações personalizadas das interfaces `IInAppMessageViewFactory` e `IInAppMessageViewWrapperFactory`. Depois de ter uma compreensão sólida dos conceitos por trás da substituição de nossas fábricas padrão, confira nossos [casos de uso](#sample-use-cases) para começar a implementar a funcionalidade de envio de mensagens no app.

{% tabs %}
{% tab Kotlin %}
**Tipos de mensagens no app**<br>

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
**Tipos de mensagens no app**<br> 

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

## Casos de uso

Fornecemos três casos de uso abaixo. Cada caso de uso tem trechos de código e uma visão de como as mensagens no app podem parecer e ser usadas no dashboard do Braze:
- [Mensagem no app do tipo slideup personalizado](#custom-slideup-in-app-message)
- [Mensagem no app do tipo modal personalizado](#custom-modal-in-app-message)
- [Mensagem no app completa personalizada](#custom-full-in-app-message)

### Mensagem no app personalizada de deslizar para cima

Ao criar sua mensagem no app de slide-up, você pode notar que não é possível modificar a posição da mensagem usando métodos padrão. A modificação como esta é possível subclasseando a classe `DefaultInAppMessageViewWrapper` para ajustar os parâmetros de layout. Você pode ajustar a posição final na tela substituindo o método `getLayoutParams` retornando o `LayoutParams` modificado com seus próprios valores de posicionamento personalizados. Visite o [CustomSlideUpInAppMessageViewWrapper](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/inapp/slideup/CustomSlideUpInAppMessageViewWrapper.kt) para começar.

#### Wrapper de visualização personalizada<br><br>

{% tabs %}
{% tab Kotlin %}
**Substituir e retornar parâmetros de layout personalizados**<br>
Dentro do método `getLayoutParams`, você pode usar o método da superclasse para acessar o `LayoutParameters` original para a mensagem no app. Em seguida, você pode ajustar a posição adicionando ou subtraindo conforme desejado.

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
**Substituir e retornar parâmetros de layout personalizados**<br>
Dentro do método `getLayoutParams`, você pode usar o método da superclasse para acessar o `LayoutParameters` original para a mensagem no app. Em seguida, você pode ajustar a posição adicionando ou subtraindo conforme desejado.

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
**Forneça uma fábrica personalizada para retornar seu wrapper personalizado**<br>
Para que o SDK da Braze use seu wrapper personalizado, você também precisa fornecer uma implementação `IInAppMessageViewWrapperFactory` personalizada que retorne seu wrapper personalizado. Você pode implementar `IInAppMessageViewWrapperFactory` diretamente ou criar uma subclasse `BrazeInAppMessageViewWrapperFactory` e substituir apenas o método `createInAppMessageViewWrapper`:

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
**Forneça uma fábrica personalizada para retornar seu wrapper personalizado**<br>
Para que o SDK da Braze use seu wrapper personalizado, você precisa fornecer uma implementação `IInAppMessageViewWrapperFactory` personalizada que retorne seu wrapper personalizado. Você pode implementar `IInAppMessageViewWrapperFactory` diretamente ou criar uma subclasse `BrazeInAppMessageViewWrapperFactory` e substituir apenas o método `createInAppMessageViewWrapper`:

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
**Registre sua fábrica com a Braze**<br>
Depois de criar sua fábrica de wrappers personalizados, registre-a no SDK da Braze através do `BrazeInAppMessageManager`:

```kotlin
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(CustomInAppMessageViewWrapperFactory())
```
{% endtab %}
{% tab Java %}
**Registre sua fábrica com a Braze**<br>
Depois de criar sua fábrica de wrappers personalizados, registre-a no SDK da Braze através do `BrazeInAppMessageManager`:

```java
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(new CustomInAppMessageViewWrapperFactory());
```
{% endtab %}
{% endtabs %}

### Mensagem no app do tipo modal personalizado

Um `BrazeInAppMessageModalView` pode ser subclassificado para aproveitar um `Spinner` que oferece maneiras engajadas de coletar valiosas atribuições do usuário. O exemplo a seguir mostra como você pode usar o Conteúdo Conectado para capturar atributos personalizados de uma lista dinâmica de itens. Visite o [`TeamPickerView`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/inapp/modal/TeamPickerView.kt) para começar.

{% tabs %}
{% tab Kotlin %}
**Uso de `view_type` para comportamento de exibição da interface do usuário**<br>
O objeto `IInAppMessage` tem um dicionário `extras` que podemos consultar para encontrar a chave `view_type` (se houver) e exibir o tipo correto de visualização. É importante notar que as mensagens no app são configuradas por mensagem, então as visualizações modais personalizadas e padrão podem funcionar de forma harmoniosa.

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
**Uso de `view_type` para comportamento de exibição da interface do usuário**<br>
O objeto `IInAppMessage` tem um dicionário `extras` que podemos consultar para encontrar a chave `view_type` (se houver) e exibir o tipo correto de visualização. É importante notar que as mensagens no app são configuradas por mensagem, então as visualizações modais personalizadas e padrão podem funcionar de forma harmoniosa.

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

**Substituir e fornecer visualização personalizada**<br>
Forneça um layout que imite a mensagem modal padrão no app, mas forneça sua visualização como o elemento raiz e, em seguida, infle esse layout 
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
**Inflar e personalizar a vista**<br>
Antes de recarregar os componentes `Spinner`, a variável de mensagem `inAppMessage` é exibida como uma string. Esta mensagem deve ser formatada como uma matriz de itens para ser exibida corretamente. Por exemplo, isso pode ser feito usando `String.split(",")`.

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
**Inflar e personalizar a vista**<br>
Antes de recarregar os componentes do `Spinner`, a variável de mensagem `inAppMessage` é exibida como uma _string_. Esta mensagem deve ser formatada como uma matriz de itens para ser exibida corretamente. Por exemplo, isso pode ser feito usando `String.split(",")`.

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
**atribuir atributo personalizado**<br>
Usando a subclasse de visualização, após um usuário pressionar enviar, passe o atributo com seu valor selecionado correspondente para a Braze e feche a mensagem no app chamando `messageClickableView.performClick()`.

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
**atribuir atributo personalizado**<br>
Usando a subclasse de visualização, após um usuário pressionar enviar, passe o atributo com seu valor selecionado correspondente para a Braze e feche a mensagem no app chamando `messageClickableView.performClick()`.

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

### Mensagem no app completa personalizada
Implementar uma mensagem no app totalmente personalizada e imersiva (tela cheia) envolve uma abordagem semelhante à descrita na seção para implementar uma [mensagem no app modal personalizada](#custom-modal-in-app-message). Neste caso, no entanto, basta estender `BrazeInAppMessageFullView` e personalizar conforme necessário. Lembre-se de que a visualização será exibida sobre a interface do usuário do aplicativo, e as visualizações no Android por padrão são transparentes. Isso significa que você precisará definir um plano de fundo de forma que a mensagem no app obscureça o conteúdo por trás dela. Ao estender `BrazeInAppMessageFullView`, o SDK da Braze lidará com a interceptação de eventos de toque na visualização e tomará a ação apropriada. Como no exemplo modal, você pode substituir esse comportamento para certos controles (como controles `Switch`) para coletar feedback do usuário.

{% tabs %}
{% tab Kotlin %}
**Uso de `view_type` para comportamento de exibição da interface do usuário**<br>
Adicionaremos mais um `view_type` extra para nossa nova personalização imersiva. Revisitando o método`createInAppMessageView`, adicione uma opção para a interface "switches":

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
**Uso de `view_type` para comportamento de exibição da interface do usuário**<br>
Adicionaremos mais um `view_type` extra para nossa nova personalização imersiva. Revisitando o método`createInAppMessageView`, adicione uma opção para a interface "switches":

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

**Substituir e fornecer visualização personalizada**<br>
Forneça um layout que imite a mensagem modal padrão no app, mas forneça sua visualização como o elemento raiz e, em seguida, infle esse layout 
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
**Inflar e personalizar a vista**<br>
Antes de definir as opções para o componente `RecyclerView`, a variável de mensagem `inAppMessage` é exibida como uma _string_. Esta mensagem deve ser formatada como uma matriz de itens para ser exibida corretamente. Por exemplo, isso pode ser feito usando `String.split(",")`. O `title` e o `subtitle` também são extraídos do pacote `extras`.

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
**Inflar e personalizar a vista**<br>
Antes de definir as opções para o componente `RecyclerView`, a variável de mensagem `inAppMessage` é exibida como uma _string_. Esta mensagem deve ser formatada como uma matriz de itens para ser exibida corretamente. Por exemplo, isso pode ser feito usando `String.split(",")`. O `title` e o `subtitle` também são extraídos do pacote `extras`.

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
**atribuir atributo personalizado**<br>
Usando a subclasse de visualização, após um usuário alternar um dos switches, passe o atributo associado e o status do switch para a Braze.

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
**atribuir atributo personalizado**<br>
Usando a subclasse de visualização, após um usuário alternar um dos switches, passe o atributo associado e o status do switch para a Braze.

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

#### Interceptação de toques em mensagens no app
![Um dispositivo Android exibindo linhas de configurações e alternâncias. A visualização personalizada lida com os botões, e quaisquer toques fora dos controles dos botões são tratados pela mensagem no app e a dispensarão.]({% image_buster /assets/img/iam_implementation_guide_android.png %}){: style="float:right;max-width:30%;margin-left:10px;border:0"}
A interceptação de toques em mensagens no app é crucial para fazer com que os botões personalizados de mensagem no app funcionem corretamente. Por padrão, todas as visualizações de mensagem no app adicionam `onClick` ouvintes à mensagem, para que os usuários possam dispensar mensagens sem botões. Quando você adiciona controles personalizados que devem responder à entrada do usuário (como botões personalizados), você pode registrar um `onClick` ouvinte com a visualização normalmente. Qualquer toque fora dos controles personalizados descartará a mensagem no app como de costume, enquanto toques recebidos pelos controles personalizados invocarão seu listener `onClick`. 

