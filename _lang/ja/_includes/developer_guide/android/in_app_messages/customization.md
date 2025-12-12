{% multi_lang_include developer_guide/prerequisites/android.md %} [アプリ内メッセージを設定する必要もあります]({{site.baseurl}}/developer_guide/in_app_messages)。

## 個別マネージャーリスナの設定

{% tabs %}
{% tab グローバルリスナー %}
`BrazeInAppMessageManager` リスナーはアプリ内メッセージの表示とライフサイクルを自動的に処理できますが、メッセージを完全にカスタマイズしたい場合は、カスタムマネージャーリスナーを実装する必要があります。
{% endtab %}

{% tab htmlリスナー %}
Braze SDK にはデフォルトの`DefaultHtmlInAppMessageActionListener`クラスがあり、カスタムリスナーが定義されていない場合に使用され、適切なアクションを自動的に実行します。ユーザーがカスタムの HTML アプリ内メッセージ内のさまざまなボタンを操作する方法をより詳細に制御する必要がある場合は、カスタム`IHtmlInAppMessageActionListener`クラスを実装します。
{% endtab %}
{% endtabs %}

### ステップ 1: ユーザ定義マネージャーリスナの実装

{% tabs %}
{% tab グローバルリスナー %}
#### ステップ1.1：`IInAppMessageManagerListener` を実装する 

[`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html)を実装するクラスを作成します。

`IInAppMessageManagerListener` 内のコールバックも、アプリ内メッセージライフサイクルのさまざまな時点で呼び出されます。たとえば、Braze からアプリ内メッセージを受信したときにカスタムマネージャー リスナーを設定すると、[`beforeInAppMessageDisplayed()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-displayed.html) メソッドが呼び出されます。このメソッドの実装により[`InAppMessageOperation.DISCARD`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/-d-i-s-c-a-r-d/index.html)が返される場合、それはアプリ内メッセージがホストアプリによって処理され、Braze によって表示されるべきではないことを Braze に知らせます。[`InAppMessageOperation.DISPLAY_NOW`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/-d-i-s-p-l-a-y_-n-o-w/index.html) が返された場合、Braze はアプリ内メッセージを表示しようとします。この方法は、アプリ内メッセージをカスタマイズされた方法で表示することを選択した場合に使用する必要があります。

`IInAppMessageManagerListener` また、メッセージクリックやボタンの代理メソッドも含まれます。これは、ボタンやメッセージがクリックされたときにメッセージを傍受して処理する場合などに使用できます。

#### ステップ1.2：IAM ビューのライフサイクルメソッドへのフック(オプション)

[`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html)インターフェイスには、アプリ内メッセージビューのライフサイクルの異なるポイントで呼び出されるアプリ内メッセージビューメソッドがあります。これらのメソッドは次の順序で呼び出されます。

1. [`beforeInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-opened.html):アプリ内メッセージがアクティビティのビューに追加される直前に呼び出されます。この時点ではまだアプリ内メッセージはユーザーに表示されません。
2. [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html):アプリ内メッセージがアクティビティのビューに追加された直後に呼び出されます。この時点で、アプリ内のメッセージがユーザーに表示されます。
3. [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html):アプリ内メッセージがアクティビティーのビューから削除される直前に呼び出されます。この時点でも、アプリ内メッセージはユーザーに表示されます。
4. [`afterInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-closed.html):アプリ内メッセージがアクティビティーのビューから削除された直後に呼び出されます。この時点では、アプリ内メッセージはユーザーに表示されなくなります。

[`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html)と[`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html)の間の時間は、アプリ内メッセージビューがスクリーンに表示され、ユーザーに表示される時間です。

{% alert note %}
これらのメソッドの実装は必須ではありません。これらは、アプリ内メッセージビューのライフサイクルを追跡および通知するためにのみ提供されます。これらのメソッド実装は空のままにすることができます。
{% endalert %}
{% endtab %}

{% tab htmlリスナー %}
[`IHtmlInAppMessageActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-html-in-app-message-action-listener/index.html)を実装するクラスを作成します。

`IHtmlInAppMessageActionListener`内のコールバックは、ユーザーが HTML アプリ内メッセージ内で以下のアクションを開始するたびに呼び出されます。

- 閉じるボタンをクリックする
- カスタムイベントを起動する
- HTML アプリ内メッセージ内の URL をクリックする

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

### ステップ 2:カスタムマネージャーリスナを使用するようにBrazeに指示します

{% tabs %}
{% tab グローバルリスナー %}
`IInAppMessageManagerListener` を作成したら、`BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener()` を呼び出して指示します `BrazeInAppMessageManager`
デフォルトのリスナーの代わりにカスタムの`IInAppMessageManagerListener`を使用するよう指示します。これは、[`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) で他のBraze 呼び出しの前に行います。そのため、カスタムリスナーはアプリ内メッセージs が表示される前に設定されます。

#### 表示前のアプリ内メッセージの変更

新しいアプリ内メッセージを受信し、すでに表示されているアプリ内メッセージがある場合、新しいメッセージはスタックの一番上に置かれ、後で表示できます。

ただし、アプリ内メッセージが表示されない場合は、`IInAppMessageManagerListener`の以下のデリゲートメソッドが呼び出されます。

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

`InAppMessageOperation()`の戻り値により、メッセージを表示するタイミングを制御できます。この方法が推奨されるケースは、アプリ内メッセージがアプリのユーザーエクスペリエンスを妨害する場合に`DISPLAY_LATER`を返すことで、アプリの特定の部分でメッセージを遅延させることです。

| `InAppMessageOperation` 戻り値 | 動作 |
| -------------------------- | -------- |
| `DISPLAY_NOW` | メッセージが表示される |
| `DISPLAY_LATER` | メッセージはスタックに返され、次に利用可能な機会に表示されます。 |
| `DISCARD` | メッセージは破棄される |
| `null` | メッセージは無視される。このメソッドは `null` を**返しません** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

詳細については、[`InAppMessageOperation`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/index.html)を参照してください。

{% alert tip %}
アプリ内メッセージを`DISCARD`し、アプリ内メッセージビューに置き換える場合は、アプリ内メッセージのクリック数とインプレッション数を手動で記録する必要があります。
{% endalert %}

Android では、アプリ内メッセージで`logClick`と`logImpression`を呼び出し、全画面のアプリ内メッセージでは`logButtonClick`を呼び出すことで行われます。

{% alert tip %}
アプリ内メッセージがスタックに置かれたら、[`BrazeInAppMessageManager.getInstance().requestDisplayInAppMessage()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/request-display-in-app-message.html)を呼び出すことでいつでもそのメッセージの取得と表示を要求できます。このメソッドは、Braze に対しスタックから次に利用可能なアプリ内メッセージを表示するように要求します。
{% endalert %}
{% endtab %}

{% tab htmlリスナー %}
`IHtmlInAppMessageActionListener` が作成されたら、`BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener()` を呼び出して、`BrazeInAppMessageManager` にデフォルト アクションリスナーの代わりにカスタム`IHtmlInAppMessageActionListener` を使用するように指示します。

Braze への他の呼び出しの前に、[`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate())に`IHtmlInAppMessageActionListener`を設定することをお勧めします。これにより、アプリ内メッセージが表示される前にカスタムアクションリスナーが設定されます。

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

## カスタムファクトリーの設定

カスタムファクトリオブジェクトを使用して、いくつかのデフォルトを上書きできます。カスタムファクトリーオブジェクトを必要に応じて Braze SDK に登録して、目的の結果を得ることができます。ただし、ファクトリを上書きする場合は、デフォルトに明示的に遅延するか、Braze デフォルトが提供する機能を再実装する必要があります。次のコードスニペットは、`IInAppMessageViewFactory` および `IInAppMessageViewWrapperFactory` インターフェイスのカスタム実装を提供する方法を示しています。

{% tabs local %}
{% tab Kotlin %}
**アプリ内メッセージのタイプ**<br>

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
**アプリ内メッセージのタイプ**<br> 

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
{% tab ビュー %}
Braze のアプリ内メッセージタイプには、ほとんどのカスタムユースケースをカバーする汎用性があります。しかし、デフォルトのタイプを使用する代わりにアプリ内メッセージの視覚的な外観を完全に定義したい場合、Braze ではカスタムビューファクトリを設定することで行うことができます。
{% endtab %}

{% tab アプリを表示する %}
`BrazeInAppMessageManager`は、デフォルトで[`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html)を使用して、既存のアクティビティビュー階層へのアプリ内メッセージモデルの配置を自動的に処理します。アプリ内メッセージをビュー階層に配置する方法をカスタマイズする必要がある場合は、カスタムの[`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html)を使用する必要があります。
{% endtab %}

{% tab アニメーション %}
アプリ内メッセージにはアニメーションの動作がプリセットされています。`Slideup`メッセージは画面にスライドし、`full`や`modal`メッセージはフェードインおよびフェードアウトします。アプリ内メッセージにカスタムアニメーションの動作を定義する場合、Braze ではカスタムアニメーションファクトリを設定することで行うことができます。
{% endtab %}
{% endtabs %}

### ステップ 1: 工場の導入

{% tabs %}
{% tab ビュー %}
[`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html)を実装するクラスを作成します。

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

{% tab アプリを表示する %}
[`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html)を実装し、[`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html)を返すクラスを作成します。

このファクトリは、アプリ内メッセージビューが作成された直後に呼び出されます。カスタムの[`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html)を実装する最も簡単な方法は、デフォルトの[`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html)を拡張することです。

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

{% tab アニメーション %}
[`IInAppMessageAnimationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-animation-factory/index.html)を実装するクラスを作成します。

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

### ステップ 2:Brazeに使用を指示する

{% tabs %}
{% tab ビュー %}
`IInAppMessageViewFactory` が作成されたら、`BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory()` を呼び出して指示します `BrazeInAppMessageManager`
デフォルトのビューファクトリの代わりにカスタムの`IInAppMessageViewFactory`を使用するよう指示します。

{% alert tip %}
Braze への他の呼び出しの前に、`Application.onCreate()`に`IInAppMessageViewFactory`を設定することをお勧めします。これにより、アプリ内メッセージが表示される前にカスタムビューファクトリが設定されます。
{% endalert %}

#### 仕組み

`slideup`のアプリ内メッセージビューは[`IInAppMessageView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-view/index.html)を実装しています。`full`および`modal`のタイプのメッセージビューは、[`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html)を実装しています。これらのクラスのいずれかを実装することで、Braze は必要に応じてクリックリスナーをカスタムビューに追加できます。すべての Braze ビュークラスは Android の[`View`](http://developer.android.com/reference/android/view/View.html)クラスを拡張しています。

`IInAppMessageView`を実装すると、カスタムビューの一部をクリック可能と定義できます。[`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html)を実装すると、メッセージボタンビューと閉じるボタンビューを定義できます。
{% endtab %}

{% tab アプリを表示する %}
[`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) が作成された後、[`BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-custom-in-app-message-view-factory.html) を呼び出して、`BrazeInAppMessageManager` にデフォルトビューwr factory の代わりにカスタム[`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) を使用するよう指示します。

Braze への他の呼び出しの前に、[`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate())に[`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html)を設定することをお勧めします。これにより、アプリ内メッセージが表示される前にカスタムビューラッパーファクトリが設定されます。

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
{% tab アニメーション %}
`IInAppMessageAnimationFactory`を作成したら、`BrazeInAppMessageManager.getInstance().setCustomInAppMessageAnimationFactory()`を呼び出して`BrazeInAppMessageManager`に対し
デフォルトのアニメーションの代わりにカスタムの`IInAppMessageAnimationFactory`を使用するよう指示します。

Braze への他の呼び出しの前に、[`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate())に`IInAppMessageAnimationFactory`を設定することをお勧めします。これにより、アプリ内メッセージが表示される前にカスタムアニメーションファクトリが設定されます。
{% endtab %}
{% endtabs %}

## カスタムスタイル

Braze の UI 要素は、Android 標準の UI ガイドラインにマッチしたデフォルトのルックアンドフィールで提供され、シームレスな体験を提供します。このリファレンス記事では、Android または FireOS アプリケーションのアプリ内メッセージングのカスタムスタイリングについて説明します。

### デフォルト形式を設定する

デフォルトのスタイルは、Braze SDK の[`styles.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml)ファイルで確認できます。

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

必要に応じて、これらのスタイルをオーバーライドし、アプリにより適したルックアンドフィールを作成することができます。

スタイルを上書きするには、スタイル全体をプロジェクトの`styles.xml`ファイルにコピーし、変更を加えます。すべての属性が正しく設定されるようにするには、スタイル全体をローカルの`styles.xml`にコピーする必要があります。これらのカスタムスタイルは、個々の UI 要素を変更するためのものであり、レイアウトを全面的に変更するものではないことに注意してください。レイアウトレベルの変更はカスタムビューで処理する必要があります。

{% alert note %}
XMLを修正することなく、Brazeキャンペーンでいくつかの色を直接カスタマイズできる。Brazeダッシュボードで設定した色は、他の場所で設定した色よりも優先されることを覚えておいてほしい。
{% endalert %}

### フォントのカスタマイズ

カスタムフォントを設定するには、`res/font` ディレクトリに書体を配置します。使用するには、メッセージテキスト、ヘッダー、ボタンテキストのスタイルをオーバーライドし、`fontFamily`属性を使用して、Braze にカスタムフォントファミリを使用するように指示します。

例えば、アプリ内メッセージボタンテキストのフォントを更新するには、`Braze.InAppMessage.Button`スタイルをオーバーライドし、カスタムフォントファミリを参照します。属性値は、`res/font`ディレクトリのフォントファミリを指す必要があります。

以下は、最後の行でカスタムフォントファミリ `my_custom_font_family` が参照されている部分的なコード例です。

```xml
  <style name="Braze.InAppMessage.Button">
    <item name="android:layout_height">wrap_content</item>
    ...
    <item name="android:paddingBottom">15.0dp</item>
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

ボタンテキストの`Braze.InAppMessage.Button`スタイルは別として、メッセージテキストのスタイルは`Braze.InAppMessage.Message`、メッセージヘッダーのスタイルは`Braze.InAppMessage.Header`です。アプリ内メッセージの全テキストにカスタムフォントファミリを使用する場合は、`Braze.InAppMessage`スタイルにフォントファミリを設定することができます。このスタイルは、すべてのアプリ内メッセージの親スタイルとなります。

{% alert important %}
他のカスタムスタイルと同様に、すべての属性が正しく設定されるようにするには、スタイル全体をローカルの`styles.xml`にコピーする必要があります。
{% endalert %}

## メッセージの解雇

### バックボタンの消去を無効にする

デフォルトでは、ハードウェアの [戻る] ボタンにより Braze のアプリ内メッセージは閉じます。この動作は、[`BrazeInAppMessageManager.setBackButtonDismissesInAppMessageView()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-back-button-dismisses-in-app-message-view.html)を使用してメッセージごとに無効にできます。 

次の例にある`disable_back_button`は、アプリ内メッセージに設定されているカスタムのキーと値のペアで、[戻る] ボタンでメッセージを閉じることを許可するかどうかを示します。

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
この機能が無効になっている場合は、代わりにホストアクティビティのハードウェアの [戻る] ボタンのデフォルト動作が使用されることに注意してください。これにより、[戻る] ボタンで表示されるアプリ内メッセージではなく、アプリケーションが終了することがあります。
{% endalert %}

### 外部タップ解雇の有効化

デフォルトでは、外部タップを使用したモーダルの削除は`false` に設定されています。この値を`true`に設定した場合、ユーザーがアプリ内メッセージの外側をタップすると、モーダルアプリ内メッセージが閉じられます。この動作は、以下を呼び出すことで切り替えることができます。

```java
BrazeInAppMessageManager.getInstance().setClickOutsideModalViewDismissInAppMessageView(true)
```

## 方向のカスタマイズ

アプリ内メッセージに固定方向を設定するには、最初に[カスタムのアプリ内メッセージマネージャーリスナーを設定]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android#android_setting-custom-manager-listeners)します。次に、`beforeInAppMessageDisplayed()` デリゲートメソッドの`IInAppMessage` オブジェクトの向きを更新します。

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

タブレット端末の場合、アプリ内メッセージは、実際の画面の向きに関係なく、ユーザーが希望する向きのスタイルで表示されます。

## ダークテーマを無効にする {#android-in-app-message-dark-theme-customization}

デフォルトでは、`IInAppMessageManagerListener` の`beforeInAppMessageDisplayed()` はシステム設定を確認し、次のコードを使用してメッセージの暗いテーマスタイルを条件付きで有効にします。

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

これを変更するには、事前表示処理の任意のステップで[`enableDarkTheme`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-themeable/enable-dark-theme.html) を呼び出して、独自の条件付きロジックをインプリメントできます。

## Google Play レビュープロンプトのカスタマイズ

Google によって設定された制限事項と制約のため、カスタムの Google Play レビュープロンプトは現在 Braze でサポートされていません。これらのプロンプトをうまく統合できたユーザーもいれば、[Google Play のクォータ](https://developer.android.com/guide/playcore/in-app-review#quotas)によって成功率が低いユーザーもいます。ご自身の責任において統合してください。[Google Play アプリ内レビュープロンプト](https://developer.android.com/guide/playcore/in-app-review)のドキュメントを参照してください。
