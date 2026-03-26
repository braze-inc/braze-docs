{% multi_lang_include developer_guide/prerequisites/android.md %} Você também precisará [configurar mensagens no app]({{site.baseurl}}/developer_guide/in_app_messages).

## Configurando ouvintes de gerenciador personalizados

{% tabs %}
{% tab global listener %}
Enquanto o ouvinte `BrazeInAppMessageManager` pode lidar automaticamente com a exibição e o ciclo de vida das mensagens no app, você precisará implementar um ouvinte de gerenciador personalizado se quiser personalizar completamente suas mensagens.
{% endtab %}

{% tab html listener %}
O SDK da Braze tem uma classe padrão `DefaultHtmlInAppMessageActionListener` que é usada se nenhum ouvinte personalizado for definido e realiza a ação apropriada automaticamente. Se precisar de mais controle sobre como um usuário interage com diferentes botões dentro de uma mensagem no app em HTML personalizado, implemente uma classe `IHtmlInAppMessageActionListener` personalizada.

Esse ouvinte se aplica a __ambas__ as mensagens criadas com HTML personalizado e mensagens criadas usando o editor de arrastar e soltar (DnD). Ele não se aplica a IAMs tradicionais. IAMs tradicionais são os tipos de mensagem integrados da Braze, renderizados pelo SDK (por exemplo, slideup, modal e full), criados no criador de mensagens no app original usando layouts predefinidos. Diferentemente das IAMs em HTML personalizado e DnD, elas não passam pelo fluxo do ouvinte de ação HTML.

Se você definir um `IHtmlInAppMessageActionListener` personalizado, sua lógica substituirá o comportamento de clique padrão para _todas_ as mensagens DnD. Certifique-se de que sua equipe de marketing esteja ciente disso, pois pode afetar suas campanhas de maneiras inesperadas.
{% endtab %}
{% endtabs %}

### Etapa 1: Implemente o ouvinte de gerenciador personalizado

{% tabs %}
{% tab global listener %}
#### Etapa 1.1: Implemente `IInAppMessageManagerListener` 

Crie uma classe que implemente [`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html).

Os retornos de chamada em seu `IInAppMessageManagerListener` também serão chamados em vários pontos do ciclo de vida da mensagem no app. Por exemplo, se você definir um ouvinte de gerenciador personalizado quando uma mensagem no app for recebida da Braze, o método [`beforeInAppMessageDisplayed()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-displayed.html) será chamado. Se sua implementação desse método retornar [`InAppMessageOperation.DISCARD`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/-d-i-s-c-a-r-d/index.html), isso sinaliza para a Braze que a mensagem no app será tratada pelo app host e não deverá ser exibida pela Braze. Se [`InAppMessageOperation.DISPLAY_NOW`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/-d-i-s-p-l-a-y_-n-o-w/index.html) for retornado, a Braze tentará exibir a mensagem no app. Esse método deve ser usado se você optar por exibir a mensagem no app de forma personalizada.

`IInAppMessageManagerListener` também inclui métodos delegados para cliques em mensagens e botões, que podem ser usados em casos como interceptar uma mensagem quando um botão ou mensagem é clicado para processamento adicional.

#### Etapa 1.2: Conecte-se aos métodos do ciclo de vida da visualização do IAM (opcional)

A interface [`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html) tem métodos de visualização de mensagens no app chamados em pontos distintos do ciclo de vida da visualização de mensagens no app. Esses métodos são chamados na seguinte ordem:

1. [`beforeInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-opened.html): Chamado logo antes da mensagem no app ser adicionada à visualização da atividade. A mensagem no app ainda não está visível para o usuário neste momento.
2. [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html): Chamado logo após a mensagem no app ser adicionada à visualização da atividade. A mensagem no app agora está visível para o usuário nesse momento.
3. [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html): Chamado logo antes da mensagem no app ser removida da visualização da atividade. A mensagem no app ainda está visível para o usuário nesse momento.
4. [`afterInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-closed.html): Chamado logo após a mensagem no app ser removida da visualização da atividade. A mensagem no app não está mais visível para o usuário neste momento.

Observe que o tempo entre [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html) e [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html) é quando a visualização da mensagem no app está na tela, visível para o usuário.

{% alert note %}
A implementação desses métodos não é obrigatória. Eles são fornecidos apenas para rastrear e informar o ciclo de vida da visualização da mensagem no app. Você pode deixar essas implementações de método vazias.
{% endalert %}
{% endtab %}

{% tab html listener %}
Crie uma classe que implemente [`IHtmlInAppMessageActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-html-in-app-message-action-listener/index.html).

Os retornos de chamada em seu `IHtmlInAppMessageActionListener` serão chamados sempre que o usuário iniciar qualquer uma das seguintes ações dentro da mensagem HTML no app:

- Clica no botão Fechar
- Dispara um evento personalizado
- Clica em um URL dentro da mensagem HTML no app

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

### Etapa 2: Instruir a Braze a usar o ouvinte de gerenciador personalizado

{% tabs %}
{% tab global listener %}
Depois de criar `IInAppMessageManagerListener`, chame `BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener()` para instruir `BrazeInAppMessageManager`
a usar seu `IInAppMessageManagerListener` personalizado em vez do ouvinte padrão. Faça isso em seu [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) antes de qualquer outra chamada à Braze, para que o ouvinte personalizado seja definido antes que qualquer mensagem no app seja exibida.

#### Alteração de mensagens no app antes da exibição

Quando uma nova mensagem no app for recebida e já houver uma mensagem no app sendo exibida, a nova mensagem será colocada no topo da pilha e poderá ser exibida posteriormente.

No entanto, se não houver nenhuma mensagem no app sendo exibida, o seguinte método delegado em `IInAppMessageManagerListener` será chamado:

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

O valor de retorno `InAppMessageOperation()` pode controlar quando a mensagem deve ser exibida. O uso sugerido desse método seria postergar mensagens em determinadas partes do app, retornando `DISPLAY_LATER` quando as mensagens no app distraíssem a experiência do usuário no app.

| Valor de retorno `InAppMessageOperation` | Comportamento |
| -------------------------- | -------- |
| `DISPLAY_NOW` | A mensagem será exibida |
| `DISPLAY_LATER` | A mensagem será devolvida à pilha e exibida na próxima oportunidade disponível |
| `DISCARD` | A mensagem será descartada |
| `null` | A mensagem será ignorada. Esse método **NÃO** deve retornar `null` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Veja [`InAppMessageOperation`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/index.html) para obter mais detalhes.

{% alert tip %}
Se optar por `DISCARD` a mensagem no app e substituí-la pela visualização da mensagem no app, será necessário registrar manualmente os cliques e as impressões da mensagem no app.
{% endalert %}

No Android, isso é feito chamando `logClick` e `logImpression` em mensagens no app e `logButtonClick` em mensagens imersivas no app.

{% alert tip %}
Depois que uma mensagem no app tiver sido colocada na pilha, você poderá solicitar que ela seja recuperada e exibida a qualquer momento, chamando [`BrazeInAppMessageManager.getInstance().requestDisplayInAppMessage()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/request-display-in-app-message.html). Esse método solicita que a Braze exiba a próxima mensagem no app disponível na pilha.
{% endalert %}
{% endtab %}

{% tab html listener %}
Após a sua `IHtmlInAppMessageActionListener` ser criada, chame `BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener()` para instruir `BrazeInAppMessageManager` a usar seu `IHtmlInAppMessageActionListener` personalizado em vez do ouvinte de ação padrão.

Recomendamos que você configure seu `IHtmlInAppMessageActionListener` em seu [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) antes de qualquer outra chamada à Braze. Isso definirá o ouvinte de ação personalizado antes que qualquer mensagem no app seja exibida:

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

## Definindo fábricas personalizadas

Você pode substituir vários padrões por meio de objetos de fábrica personalizados. Esses podem ser registrados com o SDK da Braze conforme necessário para alcançar os resultados desejados. No entanto, se você decidir substituir uma fábrica, provavelmente precisará se referir explicitamente ao padrão ou reimplementar a funcionalidade fornecida pelo padrão da Braze. O trecho de código a seguir ilustra como fornecer implementações personalizadas das interfaces `IInAppMessageViewFactory` e `IInAppMessageViewWrapperFactory`.

{% tabs local %}
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

{% tabs %}
{% tab view %}
Os tipos de mensagens no app da Braze são versáteis o suficiente para cobrir a maioria dos casos de uso personalizados. No entanto, se você quiser definir totalmente a aparência visual de suas mensagens no app em vez de usar um tipo padrão, a Braze torna isso possível definindo uma fábrica de visualizações personalizadas.
{% endtab %}

{% tab view wrapper %}
O `BrazeInAppMessageManager` lida automaticamente com a colocação do modelo de mensagem no app na hierarquia de visualização de atividade existente por padrão usando [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html). Se precisar personalizar a forma como as mensagens no app são colocadas na hierarquia da visualização, você deverá usar um [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) personalizado.
{% endtab %}

{% tab animation %}
As mensagens no app têm um comportamento de animação predefinido. As mensagens `Slideup` deslizam para a tela; as mensagens `full` e `modal` aparecem e desaparecem gradualmente. Se você quiser definir comportamentos de animação personalizados para suas mensagens no app, a Braze torna isso possível configurando uma fábrica de animação personalizada.
{% endtab %}
{% endtabs %}

### Etapa 1: Implemente a fábrica

{% tabs %}
{% tab view %}
Crie uma classe que implemente [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html):

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

{% tab view wrapper %}
Crie uma classe que implemente [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) e retorne um [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html).

Essa fábrica é chamada imediatamente após a criação da visualização de mensagem no app. A maneira mais fácil de implementar um [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) personalizado é simplesmente estender o padrão [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html):

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

{% tab animation %}
Crie uma classe que implemente [`IInAppMessageAnimationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-animation-factory/index.html):

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

### Etapa 2: Instruir a Braze a usar a fábrica

{% tabs %}
{% tab view %}
Após a sua `IInAppMessageViewFactory` ser criada, chame `BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory()` para instruir `BrazeInAppMessageManager`
a usar seu `IInAppMessageViewFactory` personalizado em vez da fábrica de visualização padrão.

{% alert tip %}
Recomendamos configurar seu `IInAppMessageViewFactory` em seu `Application.onCreate()` antes de qualquer outra chamada à Braze. Isso definirá a fábrica de visualizações personalizadas antes que qualquer mensagem no app seja exibida.
{% endalert %}

#### Como funciona

A visualização de mensagens no app `slideup` implementa [`IInAppMessageView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-view/index.html). As visualizações de mensagens dos tipos `full` e `modal` implementam [`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html). A implementação de uma dessas classes permite que a Braze adicione ouvintes de cliques à sua visualização personalizada, quando apropriado. Todas as classes de visualização da Braze estendem a classe [`View`](http://developer.android.com/reference/android/view/View.html) do Android.

A implementação de `IInAppMessageView` permite que você defina uma determinada parte da visualização personalizada como clicável. A implementação de [`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html) permite que você defina visualizações de botões de mensagem e uma visualização de botão fechar.
{% endtab %}

{% tab view wrapper %}
Após a sua [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) ser criada, chame [`BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-custom-in-app-message-view-factory.html) para instruir `BrazeInAppMessageManager` a usar seu [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) personalizado em vez da fábrica de wrapper de visualização padrão.

Recomendamos que você defina seu [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) em seu [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) antes de qualquer outra chamada à Braze. Isso definirá a fábrica do wrapper de visualização personalizado antes que qualquer mensagem no app seja exibida:

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
{% tab animation %}
Depois que seu `IInAppMessageAnimationFactory` for criado, chame `BrazeInAppMessageManager.getInstance().setCustomInAppMessageAnimationFactory()` para instruir `BrazeInAppMessageManager`
a usar seu `IInAppMessageAnimationFactory` personalizado em vez da fábrica de animação padrão.

Recomendamos que você configure seu `IInAppMessageAnimationFactory` em seu [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) antes de qualquer outra chamada à Braze. Isso definirá a fábrica de animação personalizada antes que qualquer mensagem no app seja exibida.
{% endtab %}
{% endtabs %}

## Estilos personalizados

Os elementos de UI da Braze vêm com uma aparência padrão que corresponde às diretrizes padrão de UI do Android e proporciona uma experiência integrada. Este artigo de referência aborda o estilo personalizado de mensagens no app para seu aplicativo Android ou FireOS.

### Definindo um estilo padrão

Você pode ver os estilos padrão no arquivo [`styles.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml) do SDK da Braze:

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

Se preferir, você pode substituir esses estilos para criar uma aparência que se adapte melhor ao seu app.

Para substituir um estilo, copie-o integralmente para o arquivo `styles.xml` em seu projeto e faça as modificações. Todo o estilo deve ser copiado para seu arquivo local `styles.xml` para que todos os atributos sejam definidos corretamente. Observe que esses estilos personalizados são para alterações em elementos individuais da interface do usuário, não para alterações em massa nos layouts. As alterações no nível do layout precisam ser tratadas com visualizações personalizadas.

{% alert note %}
Você pode personalizar algumas cores diretamente em sua campanha da Braze sem modificar o XML. Lembre-se de que as cores definidas no dashboard da Braze substituirão as cores que você definir em qualquer outro lugar.
{% endalert %}

### Personalizando a fonte

Você pode definir uma fonte personalizada localizando a tipografia no diretório `res/font`. Para usá-la, substitua o estilo do texto da mensagem, dos cabeçalhos e do texto do botão e use o atributo `fontFamily` para instruir a Braze a usar sua família de fontes personalizada.

Por exemplo, para atualizar a fonte do texto do botão de mensagem no app, substitua o estilo `Braze.InAppMessage.Button` e faça referência à sua família de fontes personalizada. O valor do atributo deve apontar para uma família de fontes em seu diretório `res/font`.

Aqui está um exemplo truncado com uma família de fontes personalizada, `my_custom_font_family`, referenciada na última linha:

```xml
  <style name="Braze.InAppMessage.Button">
    <item name="android:layout_height">wrap_content</item>
    ...
    <item name="android:paddingBottom">15.0dp</item>
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

Além do estilo `Braze.InAppMessage.Button` para o texto do botão, o estilo para o texto da mensagem é `Braze.InAppMessage.Message` e o estilo para os cabeçalhos da mensagem é `Braze.InAppMessage.Header`. Se quiser usar sua família de fontes personalizada em todos os textos possíveis de mensagens no app, você poderá definir sua família de fontes no estilo `Braze.InAppMessage`, que é o estilo pai de todas as mensagens no app.

{% alert important %}
Assim como ocorre com outros estilos personalizados, o estilo inteiro deve ser copiado para o arquivo local `styles.xml` para que todos os atributos sejam definidos corretamente.
{% endalert %}

## Dispensar mensagens

### Deslizando para dispensar mensagens slideup

Por padrão, mensagens no app slideup podem ser dispensadas com um gesto de deslizar. A direção do deslizar depende da posição do slideup:

- **Deslizar para a esquerda ou direita:** Dispensa o slideup independentemente de sua posição.
- **Slideup de baixo:** Deslizar de cima para baixo dispensa a mensagem. Deslizar de baixo para cima não a dispensa.
- **Slideup de cima:** Deslizar de baixo para cima dispensa a mensagem. Deslizar de cima para baixo não a dispensa.

Esse comportamento de deslizar está integrado ao [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html) padrão e se aplica apenas a mensagens slideup no app. Mensagens modais e full no app não suportam deslizar para dispensar. Para personalizar esse comportamento, você pode implementar uma [fábrica de wrapper de visualização personalizada](#android_setting-custom-factories).

{% alert note %}
Tocar fora de uma mensagem slideup não a dispensa por padrão. Esse comportamento difere das mensagens modais, que podem ser configuradas para dispensar ao tocar fora. Para slideups, use o gesto de deslizar ou o botão de fechar para dispensar a mensagem.
{% endalert %}

### Desabilitando dispensar com o botão voltar

Por padrão, o botão Voltar do hardware dispensa as mensagens no app da Braze. Esse comportamento pode ser desativado por mensagem via [`BrazeInAppMessageManager.setBackButtonDismissesInAppMessageView()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-back-button-dismisses-in-app-message-view.html). 

No exemplo a seguir, `disable_back_button` é um par chave-valor personalizado definido na mensagem no app que indica se a mensagem deve permitir que o botão voltar a dispense:

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
Observe que, se essa funcionalidade estiver desativada, será usado o comportamento padrão do botão Voltar do hardware da atividade host. Isso pode fazer com que o botão voltar feche o aplicativo em vez da mensagem no app exibida.
{% endalert %}

### Habilitando dispensar ao tocar fora

Por padrão, dispensar o modal usando um toque fora é definido como `false`. Definir esse valor como `true` resultará no fechamento da mensagem no app modal quando o usuário tocar fora da mensagem no app. Esse comportamento pode ser ativado chamando:

```java
BrazeInAppMessageManager.getInstance().setClickOutsideModalViewDismissInAppMessageView(true)
```

## Personalizando a orientação

Para definir uma orientação fixa para uma mensagem no app, primeiro [defina um ouvinte personalizado do gerenciador de mensagens no app]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android#android_setting-custom-manager-listeners). Em seguida, atualize a orientação no objeto `IInAppMessage` no método delegado `beforeInAppMessageDisplayed()`:

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

Para dispositivos tablet, as mensagens no app aparecerão no estilo de orientação preferido do usuário, independentemente da orientação real da tela.

## Desabilitando o tema escuro {#android-in-app-message-dark-theme-customization}

Por padrão, o `beforeInAppMessageDisplayed()` de `IInAppMessageManagerListener` verifica as configurações do sistema e habilita condicionalmente o estilo do tema escuro na mensagem com o seguinte código:

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

Para mudar isso, você pode chamar [`enableDarkTheme`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-themeable/enable-dark-theme.html) em qualquer etapa do processo pré-exibição para implementar sua própria lógica condicional.

## Personalizando o prompt de avaliação do Google Play

Devido às limitações e restrições definidas pelo Google, os prompts personalizados de avaliação do Google Play não são compatíveis com a Braze no momento. Embora alguns usuários tenham conseguido integrar esses prompts com sucesso, outros apresentaram baixas taxas de sucesso devido às [cotas do Google Play](https://developer.android.com/guide/playcore/in-app-review#quotas). Faça a integração por sua própria conta e risco. Consulte a documentação sobre [os prompts de avaliação no app do Google Play](https://developer.android.com/guide/playcore/in-app-review).