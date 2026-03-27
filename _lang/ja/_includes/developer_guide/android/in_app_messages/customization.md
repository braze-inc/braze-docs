{% multi_lang_include developer_guide/prerequisites/android.md %} [アプリ内メッセージの設定]({{site.baseurl}}/developer_guide/in_app_messages)も必要です。

## カスタムマネージャーリスナーの設定

{% tabs %}
{% tab global listener %}
`BrazeInAppMessageManager` リスナーはアプリ内メッセージの表示とライフサイクルを自動的に処理できますが、メッセージを完全にカスタマイズしたい場合はカスタムマネージャーリスナーを実装する必要があります。
{% endtab %}

{% tab html listener %}
Braze SDK にはデフォルトの `DefaultHtmlInAppMessageActionListener` クラスがあり、カスタムリスナーが定義されていない場合に使用され、適切なアクションを自動的に実行します。ユーザーがカスタム HTML アプリ内メッセージ内のさまざまなボタンを操作する方法をより詳細に制御する必要がある場合は、カスタム `IHtmlInAppMessageActionListener` クラスを実装します。

このリスナーは、カスタム HTML で作成されたメッセージとドラッグ＆ドロップ（DnD）エディターで作成されたメッセージの__両方__に適用されます。従来の IAM には適用されません。従来の IAM とは、Braze に組み込まれた SDK レンダリングのメッセージタイプ（スライドアップ、モーダル、フルなど）で、元のアプリ内メッセージ作成画面で定義済みのレイアウトを使用して作成されたものです。カスタム HTML や DnD IAM とは異なり、HTML アクションリスナーのフローを通過しません。

カスタム `IHtmlInAppMessageActionListener` を設定すると、そのロジックが_すべての_ DnD メッセージのデフォルトのクリック動作をオーバーライドします。マーケティングチームのキャンペーンに予期しない影響を与える可能性があるため、この点をチームに周知してください。
{% endtab %}
{% endtabs %}

### ステップ 1: カスタムマネージャーリスナーを実装する

{% tabs %}
{% tab global listener %}
#### ステップ 1.1: `IInAppMessageManagerListener` を実装する

[`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html) を実装するクラスを作成します。

`IInAppMessageManagerListener` 内のコールバックは、アプリ内メッセージのライフサイクルのさまざまな段階でも呼び出されます。例えば、Braze からアプリ内メッセージを受信した際にカスタムマネージャーリスナーを設定すると、[`beforeInAppMessageDisplayed()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-displayed.html) メソッドが呼び出されます。このメソッドの実装が [`InAppMessageOperation.DISCARD`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/-d-i-s-c-a-r-d/index.html) を返す場合、アプリ内メッセージがホストアプリによって処理され、Braze によって表示されるべきではないことを Braze に通知します。[`InAppMessageOperation.DISPLAY_NOW`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/-d-i-s-p-l-a-y_-n-o-w/index.html) が返された場合、Braze はアプリ内メッセージの表示を試みます。このメソッドは、アプリ内メッセージをカスタマイズされた方法で表示する場合に使用します。

`IInAppMessageManagerListener` には、メッセージやボタンのクリックに対するデリゲートメソッドも含まれています。これは、ボタンやメッセージがクリックされた際にメッセージをインターセプトして追加処理を行う場合などに利用できます。

#### ステップ 1.2: IAM ビューのライフサイクルメソッドにフックする（オプション）

[`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html) インターフェイスには、アプリ内メッセージビューのライフサイクルの異なるポイントで呼び出されるアプリ内メッセージビューメソッドがあります。これらのメソッドは次の順序で呼び出されます。

1. [`beforeInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-opened.html): アプリ内メッセージがアクティビティのビューに追加される直前に呼び出されます。この時点ではまだアプリ内メッセージはユーザーに表示されていません。
2. [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html): アプリ内メッセージがアクティビティのビューに追加された直後に呼び出されます。この時点で、アプリ内メッセージがユーザーに表示されます。
3. [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html): アプリ内メッセージがアクティビティのビューから削除される直前に呼び出されます。この時点でも、アプリ内メッセージはユーザーに表示されています。
4. [`afterInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-closed.html): アプリ内メッセージがアクティビティのビューから削除された直後に呼び出されます。この時点では、アプリ内メッセージはユーザーに表示されなくなります。

[`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html) と [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html) の間の時間が、アプリ内メッセージビューが画面上に表示され、ユーザーに見える状態にある期間です。

{% alert note %}
これらのメソッドの実装は必須ではありません。アプリ内メッセージビューのライフサイクルをトラッキングし、通知するためにのみ提供されています。これらのメソッドの実装は空のままにしておいても構いません。
{% endalert %}
{% endtab %}

{% tab html listener %}
[`IHtmlInAppMessageActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-html-in-app-message-action-listener/index.html) を実装するクラスを作成します。

`IHtmlInAppMessageActionListener` 内のコールバックは、ユーザーが HTML アプリ内メッセージ内で以下のアクションを開始するたびに呼び出されます。

- 閉じるボタンをクリックする
- カスタムイベントを発火する
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

### ステップ 2: Braze にカスタムマネージャーリスナーを使用するよう指示する

{% tabs %}
{% tab global listener %}
`IInAppMessageManagerListener` を作成したら、`BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener()` を呼び出して、`BrazeInAppMessageManager` にデフォルトのリスナーの代わりにカスタムの `IInAppMessageManagerListener` を使用するよう指示します。他の Braze 呼び出しの前に [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) でこれを実行してください。そうすることで、アプリ内メッセージが表示される前にカスタムリスナーが設定されます。

#### 表示前のアプリ内メッセージの変更

新しいアプリ内メッセージを受信し、すでに表示されているアプリ内メッセージがある場合、新しいメッセージはスタックの一番上に置かれ、後で表示できます。

ただし、アプリ内メッセージが表示されていない場合は、`IInAppMessageManagerListener` の以下のデリゲートメソッドが呼び出されます。

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

`InAppMessageOperation()` の戻り値により、メッセージを表示するタイミングを制御できます。このメソッドの推奨される使い方は、アプリ内メッセージがユーザーのアプリ体験を妨げる場合に `DISPLAY_LATER` を返すことで、アプリの特定の部分でメッセージの表示を遅延させることです。

| `InAppMessageOperation` 戻り値 | 動作 |
| -------------------------- | -------- |
| `DISPLAY_NOW` | メッセージが表示されます |
| `DISPLAY_LATER` | メッセージはスタックに返され、次に利用可能な機会に表示されます |
| `DISCARD` | メッセージは破棄されます |
| `null` | メッセージは無視されます。このメソッドは `null` を返す**べきではありません** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

詳細については、[`InAppMessageOperation`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/index.html) を参照してください。

{% alert tip %}
アプリ内メッセージを `DISCARD` し、独自のアプリ内メッセージビューに置き換える場合は、アプリ内メッセージのクリック数とインプレッション数を手動で記録する必要があります。
{% endalert %}

Android では、アプリ内メッセージで `logClick` と `logImpression` を呼び出し、没入型のアプリ内メッセージでは `logButtonClick` を呼び出すことで行います。

{% alert tip %}
アプリ内メッセージがスタックに置かれたら、[`BrazeInAppMessageManager.getInstance().requestDisplayInAppMessage()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/request-display-in-app-message.html) を呼び出すことでいつでもそのメッセージの取得と表示をリクエストできます。このメソッドは、Braze に対しスタックから次に利用可能なアプリ内メッセージを表示するようリクエストします。
{% endalert %}
{% endtab %}

{% tab html listener %}
`IHtmlInAppMessageActionListener` を作成したら、`BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener()` を呼び出して、`BrazeInAppMessageManager` にデフォルトのアクションリスナーの代わりにカスタムの `IHtmlInAppMessageActionListener` を使用するよう指示します。

Braze への他の呼び出しの前に、[`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) で `IHtmlInAppMessageActionListener` を設定することをお勧めします。これにより、アプリ内メッセージが表示される前にカスタムアクションリスナーが設定されます。

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

## カスタムファクトリの設定

カスタムファクトリオブジェクトを通じて、いくつかのデフォルト設定をオーバーライドできます。これらは必要に応じて Braze SDK に登録して、目的の結果を得ることができます。ただし、ファクトリをオーバーライドする場合、明示的にデフォルトに委ねるか、Braze のデフォルトが提供する機能を再実装する必要があります。次のコードスニペットは、`IInAppMessageViewFactory` および `IInAppMessageViewWrapperFactory` インターフェイスのカスタム実装を提供する方法を示しています。

{% tabs local %}
{% tab Kotlin %}
**アプリ内メッセージの種類**<br>

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
**アプリ内メッセージの種類**<br> 

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
Braze のアプリ内メッセージタイプには、ほとんどのカスタムユースケースをカバーする汎用性があります。しかし、デフォルトのタイプを使用する代わりにアプリ内メッセージの視覚的な外観を完全に定義したい場合、Braze ではカスタムビューファクトリを設定することでそれが可能です。
{% endtab %}

{% tab view wrapper %}
`BrazeInAppMessageManager` は、デフォルトで [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html) を使用して、既存のアクティビティビュー階層へのアプリ内メッセージモデルの配置を自動的に処理します。アプリ内メッセージをビュー階層に配置する方法をカスタマイズする必要がある場合は、カスタムの [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) を使用する必要があります。
{% endtab %}

{% tab animation %}
アプリ内メッセージにはアニメーションの動作がプリセットされています。`Slideup` メッセージは画面にスライドし、`full` や `modal` メッセージはフェードインおよびフェードアウトします。アプリ内メッセージにカスタムアニメーションの動作を定義したい場合、Braze ではカスタムアニメーションファクトリを設定することでそれが可能です。
{% endtab %}
{% endtabs %}

### ステップ 1: ファクトリを実装する

{% tabs %}
{% tab view %}
[`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) を実装するクラスを作成します。

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
[`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) を実装し、[`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) を返すクラスを作成します。

このファクトリは、アプリ内メッセージビューが作成された直後に呼び出されます。カスタムの [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) を実装する最も簡単な方法は、デフォルトの [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html) を拡張することです。

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
[`IInAppMessageAnimationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-animation-factory/index.html) を実装するクラスを作成します。

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

### ステップ 2: Braze にファクトリを使用するよう指示する

{% tabs %}
{% tab view %}
`IInAppMessageViewFactory` を作成したら、`BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory()` を呼び出して、`BrazeInAppMessageManager` にデフォルトのビューファクトリの代わりにカスタムの `IInAppMessageViewFactory` を使用するよう指示します。

{% alert tip %}
Braze への他の呼び出しの前に、`Application.onCreate()` で `IInAppMessageViewFactory` を設定することをお勧めします。これにより、アプリ内メッセージが表示される前にカスタムビューファクトリが設定されます。
{% endalert %}

#### 仕組み

`slideup` のアプリ内メッセージビューは [`IInAppMessageView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-view/index.html) を実装しています。`full` および `modal` タイプのメッセージビューは [`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html) を実装しています。これらのクラスのいずれかを実装することで、Braze は必要に応じてクリックリスナーをカスタムビューに追加できます。すべての Braze ビュークラスは Android の [`View`](http://developer.android.com/reference/android/view/View.html) クラスを拡張しています。

`IInAppMessageView` を実装すると、カスタムビューの特定の部分をクリック可能として定義できます。[`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html) を実装すると、メッセージボタンビューと閉じるボタンビューを定義できます。
{% endtab %}

{% tab view wrapper %}
[`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) を作成したら、[`BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-custom-in-app-message-view-factory.html) を呼び出して、`BrazeInAppMessageManager` にデフォルトのビューラッパーファクトリの代わりにカスタムの [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) を使用するよう指示します。

Braze への他の呼び出しの前に、[`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) で [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) を設定することをお勧めします。これにより、アプリ内メッセージが表示される前にカスタムビューラッパーファクトリが設定されます。

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
`IInAppMessageAnimationFactory` を作成したら、`BrazeInAppMessageManager.getInstance().setCustomInAppMessageAnimationFactory()` を呼び出して、`BrazeInAppMessageManager` にデフォルトのアニメーションファクトリの代わりにカスタムの `IInAppMessageAnimationFactory` を使用するよう指示します。

Braze への他の呼び出しの前に、[`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) で `IInAppMessageAnimationFactory` を設定することをお勧めします。これにより、アプリ内メッセージが表示される前にカスタムアニメーションファクトリが設定されます。
{% endtab %}
{% endtabs %}

## カスタムスタイル

Braze の UI 要素は、Android 標準の UI ガイドラインにマッチしたデフォルトのルックアンドフィールで提供され、シームレスな体験を提供します。このリファレンス記事では、Android または FireOS アプリケーションのアプリ内メッセージングのカスタムスタイリングについて説明します。

### デフォルトスタイルの設定

デフォルトのスタイルは、Braze SDK の [`styles.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml) ファイルで確認できます。

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

必要に応じて、これらのスタイルをオーバーライドし、アプリにより適したルックアンドフィールを作成できます。

スタイルをオーバーライドするには、スタイル全体をプロジェクトの `styles.xml` ファイルにコピーし、変更を加えます。すべての属性が正しく設定されるようにするには、スタイル全体をローカルの `styles.xml` にコピーする必要があります。これらのカスタムスタイルは、個々の UI 要素を変更するためのものであり、レイアウトを全面的に変更するものではないことに注意してください。レイアウトレベルの変更はカスタムビューで処理する必要があります。

{% alert note %}
XML を修正することなく、Braze キャンペーンでいくつかの色を直接カスタマイズできます。Braze ダッシュボードで設定した色は、他の場所で設定した色よりも優先されることに注意してください。
{% endalert %}

### フォントのカスタマイズ

カスタムフォントを設定するには、フォントファイルを `res/font` ディレクトリ内に配置します。使用するには、メッセージテキスト、ヘッダー、ボタンテキストのスタイルをオーバーライドし、`fontFamily` 属性を使用して Braze にカスタムフォントファミリを使用するよう指示します。

例えば、アプリ内メッセージボタンテキストのフォントを更新するには、`Braze.InAppMessage.Button` スタイルをオーバーライドし、カスタムフォントファミリを参照します。属性値は、`res/font` ディレクトリのフォントファミリを指す必要があります。

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

ボタンテキストの `Braze.InAppMessage.Button` スタイルとは別に、メッセージテキストのスタイルは `Braze.InAppMessage.Message`、メッセージヘッダーのスタイルは `Braze.InAppMessage.Header` です。アプリ内メッセージの全テキストにカスタムフォントファミリを使用する場合は、`Braze.InAppMessage` スタイルにフォントファミリを設定できます。このスタイルは、すべてのアプリ内メッセージの親スタイルとなります。

{% alert important %}
他のカスタムスタイルと同様に、すべての属性が正しく設定されるようにするには、スタイル全体をローカルの `styles.xml` にコピーする必要があります。
{% endalert %}

## メッセージの却下

### スワイプしてスライドアップメッセージを閉じる

デフォルトでは、スライドアップのアプリ内メッセージはスワイプ操作で閉じることができます。スワイプの方向はスライドアップの位置によって決まります。

- **左または右にスワイプ:** 位置に関係なくスライドアップを閉じます。
- **下からスライドアップ:** 上から下にスワイプするとメッセージを閉じます。下から上にスワイプしても閉じません。
- **上からスライドアップ:** 下から上にスワイプするとメッセージを閉じます。上から下にスワイプしても閉じません。

このスワイプ動作はデフォルトの [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html) に組み込まれており、スライドアップのアプリ内メッセージにのみ適用されます。モーダルおよびフル画面のアプリ内メッセージは、スワイプによる閉じ操作をサポートしていません。この動作をカスタマイズするには、[カスタムビューラッパーファクトリ](#android_setting-custom-factories)を実装できます。

{% alert note %}
スライドアップメッセージの外側をタップしても、デフォルトではメッセージは閉じられません。この動作はモーダルメッセージとは異なります。モーダルメッセージは外部タップによる閉じ処理を設定できます。スライドアップの場合、スワイプ操作か閉じるボタンでメッセージを閉じてください。
{% endalert %}

### 戻るボタンによる閉じ操作を無効化する

デフォルトでは、ハードウェアの戻るボタンにより Braze のアプリ内メッセージは閉じます。この動作は、[`BrazeInAppMessageManager.setBackButtonDismissesInAppMessageView()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-back-button-dismisses-in-app-message-view.html) を使用してメッセージごとに無効にできます。

次の例にある `disable_back_button` は、アプリ内メッセージに設定されているカスタムのキーと値のペアで、戻るボタンでメッセージを閉じることを許可するかどうかを示します。

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
この機能が無効になっている場合は、代わりにホストアクティビティのハードウェアの戻るボタンのデフォルト動作が使用されることに注意してください。これにより、戻るボタンで表示中のアプリ内メッセージではなく、アプリケーションが終了する場合があります。
{% endalert %}

### 外部タップによる閉じ操作を有効化する

デフォルトでは、外部タップによるモーダルの閉じ操作は `false` に設定されています。この値を `true` に設定すると、ユーザーがアプリ内メッセージの外側をタップした際にモーダルアプリ内メッセージが閉じられます。この動作は、以下を呼び出すことで切り替えることができます。

```java
BrazeInAppMessageManager.getInstance().setClickOutsideModalViewDismissInAppMessageView(true)
```

## 向きのカスタマイズ

アプリ内メッセージに固定の向きを設定するには、最初に[カスタムのアプリ内メッセージマネージャーリスナーを設定]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android#android_setting-custom-manager-listeners)します。次に、`beforeInAppMessageDisplayed()` デリゲートメソッド内で `IInAppMessage` オブジェクトの向きを更新します。

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

タブレットデバイスの場合、アプリ内メッセージは実際の画面の向きに関係なく、ユーザーが設定した向きのスタイルで表示されます。

## ダークテーマを無効化する {#android-in-app-message-dark-theme-customization}

デフォルトでは、`IInAppMessageManagerListener` の `beforeInAppMessageDisplayed()` はシステム設定を確認し、以下のコードでメッセージにダークテーマのスタイルを条件付きで有効にします。

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

これを変更するには、表示前のプロセスのどのステップでも [`enableDarkTheme`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-themeable/enable-dark-theme.html) を呼び出して、独自の条件付きロジックを実装できます。

## Google Play のレビュープロンプトをカスタマイズする

Google によって設定された制限事項と制約のため、カスタムの Google Play レビュープロンプトは現在 Braze でサポートされていません。これらのプロンプトをうまく統合できたユーザーもいますが、[Google Play のクォータ](https://developer.android.com/guide/playcore/in-app-review#quotas)により成功率が低いケースもあります。ご自身の責任において統合してください。[Google Play アプリ内レビュープロンプト](https://developer.android.com/guide/playcore/in-app-review)のドキュメントを参照してください。