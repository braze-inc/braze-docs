---
nav_title: カスタムリスナー
article_title: Android と FireOS 用のカスタムアプリ内メッセージリスナー
platform: 
  - Android
  - FireOS
page_order: 3
description: "このリファレンス記事では、Android または FireOS アプリケーションのカスタムアプリ内メッセージングリスナーについて説明します。"
channel:
  - in-app messages

---

# カスタムリスナー

> このリファレンス記事では、Android または FireOS アプリケーションのカスタムアプリ内メッセージングリスナーについて説明します。

カスタムリスナーを使用してアプリ内メッセージをカスタマイズする前に、アプリ内メッセージの大部分を処理する[`BrazeInAppMessageManager`][34]を理解することが重要です。「アプリ内メッセージ連携ガイド」の[ステップ1][5]で説明したように、アプリ内メッセージを適切に機能させるためには登録する必要があります。

`BrazeInAppMessageManager`は Android でのアプリ内メッセージの表示を管理します。ヘルパークラスのインスタンスが含まれており、アプリ内メッセージのライフサイクルと表示の管理に役立ちます。これらのクラスにはすべて標準実装が用意されており、カスタムクラスの定義は完全に任意です。ただし、そうすることで、アプリ内メッセージの表示と動作を別のレベルで制御できます。これらのカスタマイズ可能なクラスには、以下が含まれています。

- [`IInAppMessageManagerListener`][21] - [アプリ内メッセージの表示と動作のカスタム管理](#custom-manager-listener)
- [`IInAppMessageViewFactory`][42] - [カスタムアプリ内メッセージビューの構築](#custom-view-factory)
- [`IInAppMessageAnimationFactory`][20] - [カスタムアプリ内メッセージのアニメーションの定義](#custom-animation-factory)
- [`IHtmlInAppMessageActionListener`][86] - [HTML のアプリ内メッセージの表示と動作のカスタム管理](#custom-html-in-app-message-action-listener)
- [`IInAppMessageViewWrapperFactory`][88] - [アプリ内メッセージビューの階層操作のカスタム管理](#custom-view-wrapper-factory)

{% alert note %}
この記事には、廃止予定のニュースフィードの情報が含まれています。Braze では、ニュースフィードツールをご利用のお客様に、コンテンツカードのメッセージングチャネルへの移行を推奨しています。柔軟性、カスタマイズ性、信頼性が向上します。詳細については、[移行ガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。
{% endalert %}

## カスタムマネージャーリスナー

`BrazeInAppMessageManager`は、アプリ内メッセージの表示とライフサイクルを自動的に処理します。メッセージのライフサイクルをより詳細に制御する必要がある場合は、カスタムマネージャーリスナーを設定すると、アプリ内メッセージライフサイクルのさまざまなポイントでアプリ内メッセージオブジェクトを受け取ることができ、その表示を自分で処理したり、さらなる処理を実行したり、ユーザーの動作に反応したり、オブジェクトの[エクストラ][14]などを処理したりすることができます。

### ステップ1: アプリ内メッセージマネージャーリスナーを実装する

[`IInAppMessageManagerListener`][21]を実装するクラスを作成します。

`IInAppMessageManagerListener`内のコールバックは、アプリ内メッセージライフサイクルのさまざまなポイントで呼び出されます。

例えば、Braze からアプリ内メッセージを受け取ったときにカスタムマネージャーリスナーを設定すると、`beforeInAppMessageDisplayed()`メソッドが呼び出されます。このメソッドの実装により[`InAppMessageOperation.DISCARD`][83]が返される場合、それはアプリ内メッセージがホストアプリによって処理され、Braze によって表示されるべきではないことを Braze に知らせます。`InAppMessageOperation.DISPLAY_NOW`が返された場合、Braze はアプリ内メッセージの表示を試行します。この方法は、アプリ内メッセージをカスタマイズされた方法で表示することを選択した場合に使用する必要があります。

`IInAppMessageManagerListener`には、メッセージ自体またはいずれかのボタンのクリックに対するデリゲートメソッドも含まれます。一般的なユースケースは、ボタンやメッセージがクリックされたときにメッセージをインターセプトしてさらに処理する場合です。

### ステップ2: アプリ内メッセージビューのライフサイクルメソッドにフックする (オプション)

[`IInAppMessageManagerListener`][21]インターフェイスには、アプリ内メッセージビューのライフサイクルの異なるポイントで呼び出されるアプリ内メッセージビューメソッドがあります。これらのメソッドは次の順序で呼び出されます。

- [`beforeInAppMessageViewOpened`][92] - アプリ内メッセージがアクティビティのビューに追加される直前に呼び出されます。この時点ではまだアプリ内メッセージはユーザーに表示されません。
- [`afterInAppMessageViewOpened`][93] - アプリ内メッセージがアクティビティのビューに追加された直後に呼び出されます。この時点で、アプリ内のメッセージがユーザーに表示されます。
- [`beforeInAppMessageViewClosed`][94] - アプリ内メッセージがアクティビティのビューから削除される直前に呼び出されます。この時点でも、アプリ内メッセージはユーザーに表示されます。
- [`afterInAppMessageViewClosed`][95] - アプリ内メッセージがアクティビティのビューから削除された直後に呼び出されます。この時点では、アプリ内メッセージはユーザーに表示されなくなります。

具体的には、[`afterInAppMessageViewOpened`][93]と[`beforeInAppMessageViewClosed`][94]の間の時間は、アプリ内メッセージビューが画面に表示され、ユーザーが閲覧できる状態にある時間です。

{% alert note %}
これらのメソッドの実装は必須ではありません。これらは単にアプリ内のメッセージビューのライフサイクルを追跡し、通知するために提供されています。これらのメソッドの実装は空にしておいても機能的には問題ありません。
{% endalert %}

### ステップ3: Braze にアプリ内メッセージマネージャリスナーを使用するように指示する

`IInAppMessageManagerListener`を作成したら、`BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener()`を呼び出して`BrazeInAppMessageManager`に対し
デフォルトのリスナーの代わりにカスタムの`IInAppMessageManagerListener`を使用するよう指示します。

Braze への他の呼び出しの前に、[`Application.onCreate()`][82]に`IInAppMessageManagerListener`を設定することをお勧めします。これにより、アプリ内メッセージが表示される前にカスタムリスナーが設定されます。

#### 表示前のアプリ内メッセージの変更

新しいアプリ内メッセージを受信し、すでに表示されているアプリ内メッセージがある場合、新しいメッセージはスタックの一番上に置かれ、後で表示できます。

ただし、アプリ内メッセージが表示されない場合は、`IInAppMessageManagerListener`の以下のデリゲートメソッドが呼び出されます。

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

`InAppMessageOperation()`の戻り値により、メッセージを表示するタイミングを制御できます。この方法が推奨されるケースは、アプリ内メッセージがアプリのユーザーエクスペリエンスを妨害する場合に`DISPLAY_LATER`を返すことで、アプリの特定の部分でメッセージを遅延させることです。

| `InAppMessageOperation`の戻り値 | 動作 |
| -------------------------- | -------- |
| `DISPLAY_NOW` | メッセージが表示されます |
| `DISPLAY_LATER` | メッセージはスタックに返され、次に利用可能な機会に表示されます |
| `DISCARD` | メッセージは破棄されます |
| `null` | メッセージは無視されます。このメソッドは`null`を**返しません** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

詳細については、[`InAppMessageOperation.java`][45]を参照してください。

{% alert tip %}
アプリ内メッセージを`DISCARD`し、アプリ内メッセージビューに置き換える場合は、アプリ内メッセージのクリック数とインプレッション数を手動で記録する必要があります。
{% endalert %}

Android では、アプリ内メッセージで`logClick`と`logImpression`を呼び出し、全画面のアプリ内メッセージでは`logButtonClick`を呼び出すことで行われます。

{% alert tip %}
アプリ内メッセージがスタックに置かれたら、[`BrazeInAppMessageManager.getInstance().requestDisplayInAppMessage()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/request-display-in-app-message.html)を呼び出すことでいつでもそのメッセージの取得と表示を要求できます。このメソッドは、Braze に対しスタックから次に利用可能なアプリ内メッセージを表示するように要求します。
{% endalert %}

### ステップ 4ダークテーマの動作のカスタマイズ (オプション){#android-in-app-message-dark-theme-customization}

デフォルトの`IInAppMessageManagerListener`ロジックでは、`beforeInAppMessageDisplayed()`の場合システム設定がチェックされ、条件付きで次のコードでメッセージのダークテーマスタイルが有効になります。

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

独自の条件付きロジックを使用する場合は、表示前処理の任意のステップで[`enableDarkTheme`][97]を呼び出すことができます。

## カスタムビューファクトリ

Braze のアプリ内メッセージタイプには、ほとんどのカスタムユースケースをカバーする汎用性があります。しかし、デフォルトのタイプを使用する代わりにアプリ内メッセージの視覚的な外観を完全に定義したい場合、Braze ではカスタムビューファクトリを設定することで行うことができます。

### ステップ1: アプリ内メッセージビューファクトリを実装する

[`IInAppMessageViewFactory`][87]を実装するクラスを作成します。

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

### ステップ2: Braze にアプリ内メッセージビューファクトリを使用するように指示する

`IInAppMessageViewFactory`を作成したら、`BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory()`を呼び出して`BrazeInAppMessageManager`に対し
デフォルトのビューファクトリの代わりにカスタムの`IInAppMessageViewFactory`を使用するよう指示します。

{% alert tip %}
Braze への他の呼び出しの前に、`Application.onCreate()`に`IInAppMessageViewFactory`を設定することをお勧めします。これにより、アプリ内メッセージが表示される前にカスタムビューファクトリが設定されます。
{% endalert %}

#### Braze ビューインターフェイスの実装

`slideup`のアプリ内メッセージビューは[`IInAppMessageView`][25]を実装しています。`full`および`modal`のタイプのメッセージビューは、[`IInAppMessageImmersiveView`][24]を実装しています。これらのクラスのいずれかを実装することで、Braze は必要に応じてクリックリスナーをカスタムビューに追加できます。すべての Braze ビュークラスは Android の[`View`][18]クラスを拡張しています。

`IInAppMessageView`を実装すると、カスタムビューの一部をクリック可能と定義できます。[`IInAppMessageImmersiveView`][24]を実装すると、メッセージボタンビューと閉じるボタンビューを定義できます。

## カスタムアニメーションファクトリ

アプリ内メッセージにはアニメーションの動作がプリセットされています。`Slideup`メッセージは画面にスライドし、`full`や`modal`メッセージはフェードインおよびフェードアウトします。アプリ内メッセージにカスタムアニメーションの動作を定義する場合、Braze ではカスタムアニメーションファクトリを設定することで行うことができます。

### ステップ1: アプリ内のメッセージアニメーションファクトリを実装する

[`IInAppMessageAnimationFactory`][20]を実装するクラスを作成します。

{% tabs %}
{% tab JAVA %}
\`\`\`java
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
class CustomInAppMessageAnimationFactory :IInAppMessageAnimationFactory {
override fun getOpeningAnimation(inAppMessage: IInAppMessage): Animation {
val animation: Animation = AlphaAnimation(0, 1)
animation.interpolator = AccelerateInterpolator()
animation.duration = 2000L
return animation
}

  override fun getClosingAnimation(inAppMessage:IInAppMessage):Animation {
val animation: Animation = AlphaAnimation(1, 0)
animation.interpolator = DecelerateInterpolator()
animation.duration = 2000L
return animation
}
    }
    \`\`\`
    {% endtab %}
    {% endtabs %}

### ステップ2: Braze にアプリ内メッセージビューファクトリを使用するように指示する

`IInAppMessageAnimationFactory`を作成したら、`BrazeInAppMessageManager.getInstance().setCustomInAppMessageAnimationFactory()`を呼び出して`BrazeInAppMessageManager`に対し
デフォルトのアニメーションの代わりにカスタムの`IInAppMessageAnimationFactory`を使用するよう指示します。

Braze への他の呼び出しの前に、[`Application.onCreate()`][82]に`IInAppMessageAnimationFactory`を設定することをお勧めします。これにより、アプリ内メッセージが表示される前にカスタムアニメーションファクトリが設定されます。

## カスタムの HTML アプリ内メッセージアクションリスナー

Braze SDK にはデフォルトの`DefaultHtmlInAppMessageActionListener`クラスがあり、カスタムリスナーが定義されていない場合に使用され、適切なアクションを自動的に実行します。ユーザーがカスタムの HTML アプリ内メッセージ内のさまざまなボタンを操作する方法をより詳細に制御する必要がある場合は、カスタム`IHtmlInAppMessageActionListener`クラスを実装します。

### ステップ1: カスタムの HTML アプリ内メッセージアクションリスナーを実装する

[`IHtmlInAppMessageActionListener`][86]を実装するクラスを作成します。

`IHtmlInAppMessageActionListener`内のコールバックは、ユーザーが HTML アプリ内メッセージ内で以下のアクションを開始するたびに呼び出されます。

- 閉じるボタンをクリックする
- カスタムイベントを起動する
- HTML アプリ内メッセージ内の URL をクリックする

{% tabs %}
{% tab JAVA %}
\`\`\`java
public class CustomHtmlInAppMessageActionListener implements IHtmlInAppMessageActionListener {
  private final Context mContext;

  public CustomHtmlInAppMessageActionListener(Context context) {
    mContext = context;
  }

  @Override
  public void onCloseClicked(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
    Toast.makeText(mContext, "HTML In App Message closed", Toast.LENGTH\_LONG).show();
    BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false);
  }

  @Override
  public boolean onCustomEventFired(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
    Toast.makeText(mContext, "Custom event fired.Ignoring.", Toast.LENGTH\_LONG).show();
    return true;
  }

  @Override
  public boolean onNewsfeedClicked(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
    Toast.makeText(mContext, "Newsfeed button pressed.Ignoring.", Toast.LENGTH\_LONG).show();
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
    class CustomHtmlInAppMessageActionListener(private val mContext:Context) :IHtmlInAppMessageActionListener {

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
\`\`\`
{% endtab %}
{% endtabs %}

### ステップ2: Braze に HTML アプリ内メッセージアクションリスナーの使用を指示する

`IHtmlInAppMessageActionListener`を作成したら、`BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener()`を呼び出して、デフォルトのアクションリスナーの代わりにカスタム`IHtmlInAppMessageActionListener`を使用するように`BrazeInAppMessageManager`に指示します。

Braze への他の呼び出しの前に、[`Application.onCreate()`][82]に`IHtmlInAppMessageActionListener`を設定することをお勧めします。これにより、アプリ内メッセージが表示される前にカスタムアクションリスナーが設定されます。

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

## カスタムビューラッパーファクトリ

`BrazeInAppMessageManager`は、デフォルトで[`DefaultInAppMessageViewWrapper`][89]を使用して、既存のアクティビティビュー階層へのアプリ内メッセージモデルの配置を自動的に処理します。アプリ内メッセージをビュー階層に配置する方法をカスタマイズする必要がある場合は、カスタムの[`IInAppMessageViewWrapperFactory`][88]を使用する必要があります。

### ステップ1: アプリ内メッセージビューラッパーファクトリを実装する

[`IInAppMessageViewWrapperFactory`][88]を実装し、[`IInAppMessageViewWrapper`][90]を返すクラスを作成します。

このファクトリは、アプリ内メッセージビューが作成された直後に呼び出されます。カスタムの[`IInAppMessageViewWrapper`][90]を実装する最も簡単な方法は、デフォルトの[`DefaultInAppMessageViewWrapper`][89]を拡張することです。

{% tabs %}
{% tab JAVA %}
\`\`\`java
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
    Toast.makeText(activity.getApplicationContext(), "Opened in-app message", Toast.LENGTH\_SHORT).show();
  }

  @Override
  public void close() {
    super.close();
    Toast.makeText(mInAppMessageView.getContext().getApplicationContext(), "Closed in-app message", Toast.LENGTH\_SHORT).show();
  }
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
class CustomInAppMessageViewWrapper(inAppMessageView:View,
                                    inAppMessage：IInAppMessage,
                                    inAppMessageViewLifecycleListener:IInAppMessageViewLifecycleListener,
                                    brazeConfigurationProvider:BrazeConfigurationProvider,
                                    openingAnimation:Animation,
                                    closingAnimation:Animation, clickableInAppMessageView:View) :
    DefaultInAppMessageViewWrapper(inAppMessageView,
        inAppMessage,
        inAppMessageViewLifecycleListener,
        brazeConfigurationProvider,
        openingAnimation,
        closingAnimation,
        clickableInAppMessageView) {

  override fun open(activity:Activity) {
    super.open(activity)
    Toast.makeText(activity.applicationContext, "Opened in-app message", Toast.LENGTH\_SHORT).show()
  }

  override fun close() {
    super.close()
    Toast.makeText(mInAppMessageView.context.applicationContext, "Closed in-app message", Toast.LENGTH\_SHORT).show()
  }
}
\`\`\`
{% endtab %}
{% endtabs %}

### ステップ2: Braze にカスタムビューラッパーファクトリを使用するように指示する

[`IInAppMessageViewWrapper`][90]を作成したら、[`BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory()`][91]を呼び出して、デフォルトのビューラッパーファクトリの代わりにカスタムの[`IInAppMessageViewWrapperFactory`][88]を使用するように`BrazeInAppMessageManager`に指示します。

Braze への他の呼び出しの前に、[`Application.onCreate()`][82]に[`IInAppMessageViewWrapperFactory`][88]を設定することをお勧めします。これにより、アプリ内メッセージが表示される前にカスタムビューラッパーファクトリが設定されます。

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

[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/#step-1-braze-in-app-message-manager-registration
[14]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/customization/key_value_pairs/
[18]: http://developer.android.com/reference/android/view/View.html
[20]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-animation-factory/index.html
[21]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html
[24]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html
[25]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-view/index.html
[34]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html
[42]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html
[45]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/index.html
[82]: https://developer.android.com/reference/android/app/Application.html#onCreate()
[83]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/index.html#27659854%2FClasslikes%2F-1725759721
[86]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-html-in-app-message-action-listener/index.html
[87]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html
[88]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html
[90]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html
[91]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-custom-in-app-message-view-factory.html
[92]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-opened.html
[93]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html
[94]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html
[95]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-closed.html
[97]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-themeable/enable-dark-theme.html
[98]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html#requestDisplayInAppMessage--
[89]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html
