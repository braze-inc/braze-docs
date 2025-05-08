---
nav_title: Ouvintes personalizados
article_title: Ouvintes de mensagens no app personalizados para Android e FireOS
platform: 
  - Android
  - FireOS
page_order: 3
description: "Este artigo de referência aborda os listeners personalizados de envio de mensagens no app para seu aplicativo Android ou FireOS."
channel:
  - in-app messages

---

# Ouvintes personalizados

> Este artigo de referência aborda os listeners personalizados de envio de mensagens no app para seu aplicativo Android ou FireOS.

Antes de personalizar as mensagens no app com listeners personalizados, é importante entender a função [`BrazeInAppMessageManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html)que lida com a maior parte do envio de mensagens no app. Conforme descrito na [etapa 1]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/#step-1-braze-in-app-message-manager-registration) do guia de integração de mensagens no app, ele deve ser registrado para que as mensagens no app funcionem adequadamente.

`BrazeInAppMessageManager` gerencia a exibição de mensagens no app no Android. Ele contém instâncias de classes auxiliares que o ajudam a gerenciar o ciclo de vida e a exibição de mensagens no app. Todas essas classes têm implementações padrão e a definição de classes personalizadas é totalmente opcional. No entanto, isso pode adicionar outro nível de controle sobre a exibição e o comportamento das mensagens no app. Essas classes personalizáveis incluem:

- [`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html) - [Gerenciamento personalizado da exibição e do comportamento de mensagens no app](#custom-manager-listener)
- [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) - [Crie visualizações personalizadas de mensagens no app](#custom-view-factory)
- [`IInAppMessageAnimationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-animation-factory/index.html) - [Defina animações personalizadas de mensagens no app](#custom-animation-factory)
- [`IHtmlInAppMessageActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-html-in-app-message-action-listener/index.html) - [Gerenciamento personalizado do comportamento e da exibição de mensagens no app em HTML](#custom-html-in-app-message-action-listener)
- [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) - [Gerenciamento personalizado da interação da hierarquia de exibição de mensagens no app](#custom-view-wrapper-factory)

{% alert note %}
Este artigo inclui informações sobre feed de notícias, que está sendo descontinuado. A Braze recomenda que os clientes que usam nossa ferramenta de feed de notícias migrem para o canal de envio de mensagens Content Cards - é mais flexível, personalizável e confiável. Para saber mais, consulte o [guia de migração]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

## Ouvinte de gerente personalizado

O site `BrazeInAppMessageManager` lida automaticamente com a exibição e o ciclo de vida das mensagens no app. Se precisar de mais controle sobre o ciclo de vida de uma mensagem, a configuração de um ouvinte de gerenciador personalizado ativará o recebimento do objeto de mensagem no app em vários pontos do ciclo de vida da mensagem no app, permitindo que você mesmo lide com a exibição, execute processamento adicional, reaja ao comportamento do usuário, processe os [extras]({{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/customization/key_value_pairs/) do objeto e muito mais.

### Etapa 1: Implemente um ouvinte do gerenciador de mensagens no app

Crie uma classe que implemente o [`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html).

Os retornos de chamada em seu `IInAppMessageManagerListener` serão chamados em vários pontos do ciclo de vida das mensagens no app.

Por exemplo, se você definir um ouvinte de gerenciador personalizado quando uma mensagem no app for recebida da Braze, o método `beforeInAppMessageDisplayed()` será chamado. Se sua implementação desse método retornar [`InAppMessageOperation.DISCARD`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/index.html#27659854%2FClasslikes%2F-1725759721)isso sinaliza para a Braze que a mensagem no app será tratada pelo aplicativo host e não deverá ser exibida pela Braze. Se `InAppMessageOperation.DISPLAY_NOW` for retornado, a Braze tentará exibir a mensagem no app. Esse método deve ser usado se você optar por exibir a mensagem no app de forma personalizada.

`IInAppMessageManagerListener` também inclui métodos delegados para cliques na própria mensagem ou em um dos botões. Um caso de uso comum seria a interceptação de uma mensagem quando um botão ou mensagem é clicado para processamento posterior.

### Etapa 2: Conecte-se aos métodos do ciclo de vida do modo de exibição de mensagens no app (opcional)

A interface [`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html) tem métodos de visualização de mensagens no app chamados em pontos distintos do ciclo de vida da visualização de mensagens no app. Esses métodos são chamados na seguinte ordem:

- [`beforeInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-opened.html) - Chamada imediatamente antes de a mensagem no app ser adicionada à exibição da atividade. A mensagem no app ainda não está visível para o usuário neste momento.
- [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html) - Chamada logo após a mensagem no app ser adicionada à exibição da atividade. A mensagem no app agora está visível para o usuário nesse momento.
- [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html) - Chamada imediatamente antes de a mensagem no app ser removida da exibição da atividade. A mensagem no app ainda está visível para o usuário nesse momento.
- [`afterInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-closed.html) - Chamada logo após a mensagem no app ser removida da visualização da atividade. A mensagem no app não está mais visível para o usuário neste momento.

Para fins de contexto adicional, o tempo entre [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html) e [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html) é quando a exibição da mensagem no app está na tela, visível para o usuário.

{% alert note %}
A implementação desses métodos não é obrigatória. Eles são fornecidos apenas para rastrear e informar o ciclo de vida da visualização de mensagens no app. É funcionalmente aceitável deixar essas implementações de método vazias.
{% endalert %}

### Etapa 3: Instrua o Braze a usar seu ouvinte do gerenciador de mensagens no app

Depois que seu `IInAppMessageManagerListener` for criado, ligue para `BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener()` para instruir `BrazeInAppMessageManager`
para usar seu `IInAppMessageManagerListener` personalizado em vez do listener padrão.

Recomendamos que você configure seu `IInAppMessageManagerListener` em seu [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) antes de qualquer outra chamada para o Braze. Isso definirá o ouvinte personalizado antes que qualquer mensagem no app seja exibida.

#### Alteração de mensagens no app antes da exibição

Quando uma nova mensagem no app for recebida e já houver uma mensagem no app sendo exibida, a nova mensagem será colocada no topo da pilha e poderá ser exibida posteriormente.

No entanto, se não houver nenhuma mensagem no app sendo exibida, o seguinte método delegado em `IInAppMessageManagerListener` será chamado:

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

O valor de retorno `InAppMessageOperation()` pode controlar quando a mensagem deve ser exibida. O uso sugerido desse método seria a postergação de mensagens em determinadas partes do aplicativo, retornando `DISPLAY_LATER` quando as mensagens no app distraíssem a experiência do usuário no aplicativo.

| `InAppMessageOperation` valor de retorno | Comportamento |
| -------------------------- | -------- |
| `DISPLAY_NOW` | A mensagem será exibida |
| `DISPLAY_LATER` | A mensagem será devolvida à pilha e exibida na próxima oportunidade disponível |
| `DISCARD` | A mensagem será descartada |
| `null` | A mensagem será ignorada. Esse método **NÃO** deve retornar `null` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Veja [`InAppMessageOperation.java`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/index.html) para obter mais detalhes.

{% alert tip %}
Se optar por `DISCARD` a mensagem no app e substituí-la pela visualização da mensagem no app, será necessário registrar manualmente os cliques e as impressões da mensagem no app.
{% endalert %}

No Android, isso é feito chamando `logClick` e `logImpression` em mensagens no app e `logButtonClick` em mensagens imersivas no app.

{% alert tip %}
Depois que uma mensagem no app tiver sido colocada no stack, você poderá solicitar que ela seja recuperada e exibida a qualquer momento, chamando [`BrazeInAppMessageManager.getInstance().requestDisplayInAppMessage()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/request-display-in-app-message.html). Esse método solicita que a Braze exiba a próxima mensagem no app disponível no stack.
{% endalert %}

### Etapa 4: Personalização do comportamento do tema escuro (opcional) {#android-in-app-message-dark-theme-customization}

Na lógica padrão do site `IInAppMessageManagerListener`, em `beforeInAppMessageDisplayed()`, as configurações do sistema são verificadas e ativam condicionalmente o estilo de tema escuro na mensagem com o seguinte código:

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

Se quiser usar sua própria lógica condicional, você pode chamar [`enableDarkTheme`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-themeable/enable-dark-theme.html) em qualquer etapa do processo de pré-exibição.

## Fábrica de visualização personalizada

Os tipos de mensagens no app do Braze são versáteis o suficiente para cobrir a maioria dos casos de uso personalizados. No entanto, se você quiser definir totalmente a aparência visual de suas mensagens no app em vez de usar um tipo padrão, o Braze torna isso possível definindo uma fábrica de visualizações personalizadas.

### Etapa 1: Implementar uma fábrica de exibição de mensagens no app

Crie uma classe que implemente [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html):

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

### Etapa 2: Instrua a Braze a usar sua fábrica de visualização de mensagens no app

Depois que seu `IInAppMessageViewFactory` for criado, ligue para `BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory()` para instruir `BrazeInAppMessageManager`
para usar seu `IInAppMessageViewFactory` personalizado em vez da visualização padrão de fábrica.

{% alert tip %}
Recomendamos configurar seu `IInAppMessageViewFactory` em seu `Application.onCreate()` antes de qualquer outra chamada para o Braze. Isso definirá a fábrica de visualizações personalizadas antes que qualquer mensagem no app seja exibida.
{% endalert %}

#### Implementação de uma interface de visualização do Braze

A visualização de mensagens no app `slideup` implementa [`IInAppMessageView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-view/index.html). As exibições de mensagens dos tipos `full` e `modal` implementam [`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html). A implementação de uma dessas classes permite que o Braze adicione ouvintes de cliques à sua exibição personalizada, quando apropriado. Todas as classes de visualização do Braze estendem a classe [`View`](http://developer.android.com/reference/android/view/View.html) do Android.

A implementação do site `IInAppMessageView` permite que você defina uma determinada parte da visualização personalizada como clicável. A implementação de [`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html) permite que você defina visualizações de botões de mensagem e uma visualização de botão fechar.

## Fábrica de animação personalizada

As mensagens no app têm um comportamento de animação predefinido. As mensagens `Slideup` deslizam para a tela; as mensagens `full` e `modal` aparecem e desaparecem. Se você quiser definir comportamentos de animação personalizados para suas mensagens no app, o Braze torna isso possível configurando uma fábrica de animação personalizada.

### Etapa 1: Implemente uma fábrica de animação de mensagens no app

Crie uma classe que implemente [`IInAppMessageAnimationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-animation-factory/index.html):

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

### Etapa 2: Instrua a Braze a usar sua fábrica de visualização de mensagens no app

Depois que seu `IInAppMessageAnimationFactory` for criado, ligue para `BrazeInAppMessageManager.getInstance().setCustomInAppMessageAnimationFactory()` para instruir `BrazeInAppMessageManager`
para usar seu site personalizado `IInAppMessageAnimationFactory` em vez da animação padrão de fábrica.

Recomendamos que você configure seu `IInAppMessageAnimationFactory` em seu [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) antes de qualquer outra chamada para o Braze. Isso definirá a fábrica de animação personalizada antes que qualquer mensagem no app seja exibida.

## Ouvinte de ação de mensagem no app em HTML personalizado

O SDK da Braze tem uma classe padrão `DefaultHtmlInAppMessageActionListener` que é usada se nenhum ouvinte personalizado for definido e realiza a ação apropriada automaticamente. Se precisar de mais controle sobre como um usuário interage com diferentes botões dentro de uma mensagem no app em HTML personalizado, implemente uma classe `IHtmlInAppMessageActionListener` personalizada.

### Etapa 1: Implementar um ouvinte de ação de mensagem no app em HTML personalizado

Crie uma classe que implemente o [`IHtmlInAppMessageActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-html-in-app-message-action-listener/index.html).

Os retornos de chamada em seu `IHtmlInAppMessageActionListener` serão chamados sempre que o usuário iniciar qualquer uma das seguintes ações dentro da mensagem HTML no app:

- Clica no botão Fechar
- Dispara um evento personalizado
- Cliques em um URL dentro de uma mensagem HTML no app

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

### Etapa 2: Instrua a Braze a usar seu ouvinte de ação de mensagem no app em HTML

Depois que o `IHtmlInAppMessageActionListener` for criado, chame o `BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener()` para instruir o `BrazeInAppMessageManager` a usar o `IHtmlInAppMessageActionListener` personalizado em vez do action listener padrão.

Recomendamos que você configure seu `IHtmlInAppMessageActionListener` em seu [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) antes de qualquer outra chamada para o Braze. Isso definirá o ouvinte de ação personalizado antes que qualquer mensagem no app seja exibida:

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

## Fábrica de wrapper de exibição personalizados

O site `BrazeInAppMessageManager` lida automaticamente com a colocação do modelo de mensagem no app na hierarquia de exibição de atividade existente por padrão usando [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html). Se precisar personalizar a forma como as mensagens no app são colocadas na hierarquia da visualização, você deverá usar um arquivo [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html).

### Etapa 1: Implementar uma fábrica de wrapper de exibição de mensagens no app

Crie uma classe que implemente [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) e retorna um arquivo [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html).

Essa fábrica é chamada imediatamente após a criação da exibição de mensagem no app. A maneira mais fácil de implementar um [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) personalizado é simplesmente estender o padrão [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html):

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

### Etapa 2: Instrua a Braze a usar sua fábrica de wrapper de exibição personalizada

Depois que seu [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) for criado, chame [`BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-custom-in-app-message-view-factory.html) para instruir o site `BrazeInAppMessageManager` a usar seu [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) personalizado em vez da fábrica de wrapper de exibição padrão.

Recomendamos que você defina seu [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) em seu [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) antes de qualquer outra chamada para o Braze. Isso definirá a fábrica do wrapper de exibição personalizado antes que qualquer mensagem no app seja exibida:

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

