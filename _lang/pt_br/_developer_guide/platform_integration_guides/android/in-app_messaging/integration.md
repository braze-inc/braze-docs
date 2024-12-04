---
nav_title: Integração
article_title: Integração de mensagens no app para Android e FireOS
page_order: 1
platform: 
  - Android
  - FireOS
description: "Este artigo de referência aborda como integrar o envio de mensagens no app em seu aplicativo para Android ou FireOS."
channel:
  - in-app messages
search_rank: 2
---

# Integração de mensagens no app

> Este artigo de referência aborda como integrar o envio de mensagens no app em seu aplicativo para Android ou FireOS.

[As mensagens no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) ajudam a levar conteúdo aos seus usuários sem interromper o dia deles com uma notificação por push. Mensagens no app personalizadas e sob medida aprimoram a experiência do usuário e ajudam o público a obter o máximo valor do seu app. Com vários layouts e ferramentas de personalização para escolher, as mensagens no app engajam seus usuários mais do que nunca.

Para ver exemplos de mensagens no app, confira nossos [estudos de caso](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html).

## Tipos de mensagens no app

O Braze oferece vários tipos de mensagens no app padrão, cada uma personalizável com mensagens, imagens, ícones [Font Awesome](https://fontawesome.com/icons?d=gallery&p=2), ações de clique, análises de dados, estilo editável e esquemas de cores. Os tipos disponíveis atualmente são:

- [`Slideup`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html)
- [`Modal`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html)
- [`Full`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html)
- [`HTML`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html)

Também é possível definir sua própria [exibição personalizada de mensagens no app]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/#custom-view-factory).

Todas as mensagens no app implementam a interface [`IInAppMessage`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html) que define o comportamento e as características básicas de todas as mensagens no app. [`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html) é uma classe abstrata que implementa `IInAppMessage` e fornece a implementação básica de mensagens no app. Todas as classes de mensagens no app são subclasses de `InAppMessageBase`.

Além disso, há uma subinterface de `IInAppMessage` chamada [`IInAppMessageImmersive`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-immersive/index.html) que adiciona [botões](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html) de ação de clique e de análise de dados ativados, bem como texto de cabeçalho e um botão de fechar.

{% alert important %}
Para mensagens no app contendo botões, a mensagem `clickAction` também será incluída na carga útil final se a ação de clique for adicionada antes de adicionar o texto do botão.
{% endalert %}

[`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html) é uma classe abstrata que implementa `IInAppMessageImmersive` e fornece a implementação fundamental da mensagem no app `immersive`. As mensagens no app `Modal` são uma subclasse de `InAppMessageImmersiveBase`.

As mensagens no app em HTML são instâncias [`InAppMessageHtml`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html), que implementam [`IInAppMessageHtml`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-html/index.html), outra subclasse de `IInAppMessage`.

### Comportamentos esperados por tipo de mensagem

É assim que seus usuários abrem um dos nossos tipos de mensagem no app padrão.

{% tabs local %}
{% tab Slideup %}
[`Slideup`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html) As mensagens no app são assim chamadas porque "deslizam para cima" ou "deslizam para baixo" a partir da parte superior ou inferior da tela. Eles cobrem uma pequena parte da tela e fornecem um recurso de envio de mensagens eficaz e não intrusivo.

![Uma mensagem no app que desliza da parte inferior da tela do telefone exibindo "Os seres humanos são complicados. O engajamento personalizado não deveria ser." Em segundo plano, a mesma mensagem no app exibida no canto inferior direito de uma página da Internet.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}
[`Modal`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html) As mensagens no app aparecem no centro da tela e são emolduradas por um painel translúcido. Úteis para o envio de mensagens mais críticas, eles podem ser equipados com dois botões de ação por clique e com análise de dados ativada.

![Uma mensagem modal no app no centro da tela do telefone exibindo "Os seres humanos são complicados. O engajamento personalizado não deveria ser." No plano de fundo, está a mesma mensagem no app exibida no centro de uma página da Internet.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Tela inteira %}
[`Full`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html) As mensagens no app são úteis para maximizar o conteúdo e o impacto da sua comunicação com o usuário. A metade superior de uma mensagem no app `full` contém uma imagem, e a metade inferior exibe texto e até dois botões de ação de clique e de análise de dados.

![Uma mensagem no app, em tela inteira, exibida em toda a tela do telefone, que diz: "Os seres humanos são complicados. O engajamento personalizado não deveria ser." No plano de fundo está a mesma mensagem no app exibida em grande parte no centro de uma página da Internet.]({% image_buster /assets/img_archive/In-App_Full.png %})

{% endtab %}
{% tab HTML personalizado %}
[`HTML`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html) As mensagens no app são úteis para criar conteúdo totalmente personalizado para o usuário. O conteúdo HTML definido pelo usuário da mensagem no app é exibido em `WebView` e pode, opcionalmente, conter outros conteúdos avançados, como imagens e fontes, permitindo controle total sobre a aparência e a funcionalidade da mensagem. <br><br>As mensagens no app Android suportam uma interface JavaScript `brazeBridge` para chamar métodos no Braze Web SDK a partir do seu HTML; consulte nossas <a href="{{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/">práticas recomendadas</a> para obter mais detalhes.

![Uma mensagem no app em HTML com um carrossel de conteúdo e botões interativos.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% alert important %}
Atualmente, não oferecemos suporte à exibição de mensagens no app em HTML personalizado em um iFrame nas plataformas iOS e Android.
{% endalert %} 

{% endtab %}
{% endtabs %}

#### Definição de tipos de mensagens no app personalizadas

O objeto de mensagem no app `slideup` estende [`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html).
As mensagens do tipo `full` e `modal` se estendem [`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html). A extensão de uma dessas classes lhe dá a opção de adicionar funcionalidade personalizada às mensagens no app geradas localmente.

## Integração {#in-app-messaging-integration}

### Etapa 1: Registro do gerenciador de mensagens no app do Braze

A exibição de mensagens no app é gerenciada pela classe [`BrazeInAppMessageManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html). Todas as atividades do seu app devem ser registradas no site `BrazeInAppMessageManager` para permitir que ele adicione visualizações de mensagens no app à hierarquia de visualizações. Há duas maneiras de fazer isso:

#### Integração de retorno de chamada do ciclo de vida da atividade (recomendado)

A [integração do retorno de chamada do ciclo de vida da atividade]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android) lida automaticamente com o registro de mensagens no app; não é necessária nenhuma integração extra. Essa é a integração recomendada para lidar com o registro de mensagens no app.

#### Registro manual de mensagens no app

{% alert warning %}
Se você fez a integração do ciclo de vida da atividade, *não* deve fazer uma integração manual de mensagens no app.
{% endalert %}

Primeiro, em [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()), chame [`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html):

{% tabs %}
{% tab JAVA %}

```java
BrazeInAppMessageManager.getInstance().ensureSubscribedToInAppMessageEvents(context);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().ensureSubscribedToInAppMessageEvents(context)
```

{% endtab %}
{% endtabs %}

Em seguida, em todas as atividades em que as mensagens no app podem ser exibidas, [`registerInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/register-in-app-message-manager.html) deve ser chamado no `onResume()` dessa atividade:

{% tabs %}
{% tab JAVA %}

```java
@Override
public void onResume() {
  super.onResume();
  // Registers the BrazeInAppMessageManager for the current Activity. This Activity will now listen for
  // in-app messages from Braze.
  BrazeInAppMessageManager.getInstance().registerInAppMessageManager(activity);
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
public override fun onResume() {
  super.onResume()
  // Registers the BrazeInAppMessageManager for the current Activity. This Activity will now listen for
  // in-app messages from Braze.
  BrazeInAppMessageManager.getInstance().registerInAppMessageManager(this)
}
```

{% endtab %}
{% endtabs %}

Por fim, em todas as atividades em que [`registerInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/register-in-app-message-manager.html) foi chamado, [`unregisterInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/unregister-in-app-message-manager.html) deve ser chamado no `onPause()` da atividade:

{% tabs %}
{% tab JAVA %}

```java
@Override
public void onPause() {
  super.onPause();
  // Unregisters the BrazeInAppMessageManager for the current Activity.
  BrazeInAppMessageManager.getInstance().unregisterInAppMessageManager(activity);
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
public override fun onPause() {
  super.onPause()
  // Unregisters the BrazeInAppMessageManager.
  BrazeInAppMessageManager.getInstance().unregisterInAppMessageManager(this)
}
```

{% endtab %}
{% endtabs %}

### Etapa 2: Lista de bloqueio do gerenciador de mensagens no app (opcional)

Em sua integração, você pode exigir que determinadas atividades em seu app não mostrem mensagens no app. A [integração do retorno de chamada do ciclo de vida da atividade]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android) oferece uma maneira fácil de fazer isso.

O código de exemplo a seguir adiciona duas atividades à lista de bloqueio de registro de mensagens no app: `SplashActivity` e `SettingsActivity`.

{% tabs %}
{% tab JAVA %}

```java
public class MyApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    Set<Class> inAppMessageBlocklist = new HashSet<>();
    inAppMessageBlocklist.add(SplashActivity.class);
    inAppMessageBlocklist.add(SettingsActivity.class);
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener(inAppMessageBlocklist));
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    val inAppMessageBlocklist = HashSet<Class<*>>()
    inAppMessageBlocklist.add(SplashActivity::class.java)
    inAppMessageBlocklist.add(SettingsActivity::class.java)
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener(inAppMessageBlocklist))
  }
}
```

{% endtab %}
{% endtabs %}


