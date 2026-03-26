# 実装例

> このオプションの上級実装ガイドでは、アプリ内メッセージコードに関する考慮事項、Braze チームが作成した 3 つのカスタムユースケース、付属のコードスニペットについて説明します。Braze Demo リポジトリには[こちら](https://github.com/braze-inc/braze-growth-shares-android-demo-app)からアクセスできます。この実装ガイドは、Kotlin 実装を中心に扱っていますが、興味のある方のために Java のスニペットが提供されています。HTML の実装をお探しですか?Braze の[HTML テンプレートリポジトリ](https://github.com/braze-inc/in-app-message-templates)をご確認ください。

## コードに関する考慮事項

次のガイドでは、デフォルトのアプリ内メッセージに加えてオプションで使用できる、開発者向けカスタム統合機能について説明します。各ユースケースにはカスタムビューコンポーネントとファクトリーが必要に応じて含まれており、機能を拡張したり、アプリ内メッセージの外観をネイティブにカスタマイズしたりするためのサンプルが用意されています。同様の結果を得る方法が複数ある場合があります。最適な実装は、特定のユースケースによって異なります。

### カスタムファクトリー

Braze SDK を使用すると、開発者はカスタムファクトリーオブジェクトを通じて多くのデフォルトをオーバーライドできます。カスタムファクトリーオブジェクトを必要に応じて Braze SDK に登録して、目的の結果を得ることができます。ただし、ほとんどの場合、ファクトリーをオーバーライドする場合は、明示的にデフォルトに従うか、Braze デフォルトで提供される機能を再実装する必要があります。次のコードスニペットは、`IInAppMessageViewFactory` および `IInAppMessageViewWrapperFactory` インターフェイスのカスタム実装を提供する方法を示しています。デフォルトファクトリーのオーバーライドの背後にある概念をしっかりと理解したら、[ユースケース](#sample-use-cases)を確認してカスタムのアプリ内メッセージング機能の実装を開始してください。

{% tabs %}
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

## ユースケース

私たちは以下に3つのユースケースを提供しました。各ユースケースにはコードスニペットが含まれており、アプリ内メッセージがBrazeダッシュボードでどのように表示され、使用されるかを確認できます。
- [実装例](#implementation-examples)
  - [コードに関する考慮事項](#code-considerations)
    - [カスタムファクトリー](#custom-factories)
  - [ユースケース](#use-cases)
    - [カスタムスライドアップアプリ内メッセージ](#custom-slide-up-in-app-message)
      - [カスタムビューラッパー](#custom-view-wrapper)
    - [カスタムモーダルアプリ内メッセージ](#custom-modal-in-app-message)
    - [カスタムフルアプリ内メッセージ](#custom-full-in-app-message)
      - [アプリ内メッセージタッチのインターセプト](#intercepting-in-app-message-touches)

### カスタムスライドアップアプリ内メッセージ

スライドアップのアプリ内メッセージを作成しているときに、デフォルトの方法ではメッセージの配置を変更できないことに気付くかもしれません。このような変更は、`DefaultInAppMessageViewWrapper` クラスをサブクラス化してレイアウトパラメーターを調整することで可能になります。画面上の最終位置を調整するには、変更された `LayoutParams` を返す `getLayoutParams` メソッドを独自のカスタム位置決め値でオーバーライドします。開始するには、[CustomSlideUpInAppMessageViewWrapper](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/inapp/slideup/CustomSlideUpInAppMessageViewWrapper.kt) をご覧ください。

#### カスタムビューラッパー<br><br>

{% tabs %}
{% tab Kotlin %}
**カスタムレイアウトパラメーターをオーバーライドして返す**<br>
`getLayoutParams` メソッド内では、スーパークラスメソッドを使用して、アプリ内メッセージの元の `LayoutParameters` にアクセスできます。次に、必要に応じて加算または減算して位置を調整できます。

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
**カスタムレイアウトパラメーターをオーバーライドして返す**<br>
`getLayoutParams` メソッド内では、スーパークラスメソッドを使用して、アプリ内メッセージの元の `LayoutParameters` にアクセスできます。次に、必要に応じて加算または減算して位置を調整できます。

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
**カスタムラッパーを返すためのカスタムファクトリーを指定する**<br>
Braze SDK でカスタムラッパーを使用するには、カスタムラッパーを返すカスタム `IInAppMessageViewWrapperFactory` 実装も指定する必要があります。`IInAppMessageViewWrapperFactory` を直接実装することも、`BrazeInAppMessageViewWrapperFactory` をサブクラス化して `createInAppMessageViewWrapper` メソッドのみをオーバーライドすることもできます。

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
**カスタムラッパーを返すためのカスタムファクトリーを指定する**<br>
Braze SDK でカスタムラッパーを使用するには、カスタムラッパーを返すカスタム `IInAppMessageViewWrapperFactory` 実装を指定する必要があります。`IInAppMessageViewWrapperFactory` を直接実装することも、`BrazeInAppMessageViewWrapperFactory` をサブクラス化して `createInAppMessageViewWrapper` メソッドのみをオーバーライドすることもできます。

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
**ファクトリーを Braze に登録する**<br>
カスタムラッパーファクトリーを作成したら、`BrazeInAppMessageManager` を使用して Braze SDK に登録します。

```kotlin
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(CustomInAppMessageViewWrapperFactory())
```
{% endtab %}
{% tab Java %}
**ファクトリーを Braze に登録する**<br>
カスタムラッパーファクトリーを作成したら、`BrazeInAppMessageManager` を使用して Braze SDK に登録します。

```java
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(new CustomInAppMessageViewWrapperFactory());
```
{% endtab %}
{% endtabs %}

### カスタムモーダルアプリ内メッセージ

`BrazeInAppMessageModalView` をサブクラス化すると、貴重なユーザー属性を収集する魅力的な方法となる `Spinner` を活用できます。次の例は、コネクテッドコンテンツを使用して項目の動的リストからカスタム属性をキャプチャする方法を示しています。開始するには、[`TeamPickerView`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/inapp/modal/TeamPickerView.kt) にアクセスしてください。

{% tabs %}
{% tab Kotlin %}
**UI 表示動作に `view_type` を使用**<br>
`IInAppMessage` オブジェクトの `extras` ディクショナリをクエリすると、`view_type` キー (ある場合) を検索して正しいタイプのビューを表示できます。アプリ内メッセージはメッセージごとに設定されるため、カスタムとデフォルトのモーダルビューが調和して機能することに注意してください。

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
**UI 表示動作に `view_type` を使用**<br>
`IInAppMessage` オブジェクトの `extras` ディクショナリをクエリすると、`view_type` キー (ある場合) を検索して正しいタイプのビューを表示できます。アプリ内メッセージはメッセージごとに設定されるため、カスタムとデフォルトのモーダルビューが調和して機能することに注意してください。

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

**オーバーライドしてカスタムビューを提供する**<br>
標準のモーダルアプリ内メッセージを模倣したレイアウトを提供しますが、ビューをルート要素として指定し、そのレイアウトをインフレートします 
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
**ビューをインフレートしてカスタマイズする**<br>
`Spinner` コンポーネントをリロードする前に、`inAppMessage` メッセージ変数は文字列として出力されます。正しく表示するには、このメッセージを項目の配列としてフォーマットする必要があります。例として、これは `String.split(",")` を使用して実現できます。

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
**ビューをインフレートしてカスタマイズする**<br>
`Spinner` コンポーネントをリロードする前に、`inAppMessage` メッセージ変数は_文字列_として出力されます。正しく表示するには、このメッセージを項目の配列としてフォーマットする必要があります。例として、これは `String.split(",")` を使用して実現できます。

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
**カスタム属性を割り当てる**<br>
ユーザーが [送信] を押した後、ビューサブクラスを使用して、属性とそれに対応する選択済みの値を Braze に渡し、`messageClickableView.performClick()` を呼び出してアプリ内メッセージを閉じます。

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
**カスタム属性を割り当てる**<br>
ユーザーが [送信] を押した後、ビューサブクラスを使用して、属性とそれに対応する選択済みの値を Braze に渡し、`messageClickableView.performClick()` を呼び出してアプリ内メッセージを閉じます。

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

### カスタムフルアプリ内メッセージ
完全にカスタムの没入型 (全画面) アプリ内メッセージを実装するには、[カスタマイズされたモーダルアプリ内メッセージ](#custom-modal-in-app-message)の実装に関するセクションで説明したのと同様のアプローチが必要です。ただし、この例では、単に `BrazeInAppMessageFullView` を拡張し、必要に応じてカスタマイズします。ビューはアプリケーション UI 上に表示され、Android のビューはデフォルトで透明であることに注意してください。つまり、アプリ内メッセージによって背景の内容が見えにくくなるような背景を定義する必要があります。`BrazeInAppMessageFullView` を拡張することにより、Braze SDK はビュー上のタッチイベントのインターセプトを処理し、適切なアクションを実行します。モーダルの例と同様に、特定のコントロール (`Switch` コントロールなど) でこの動作をオーバーライドして、ユーザーからのフィードバックを収集できます。

{% tabs %}
{% tab Kotlin %}
**UI 表示動作に `view_type` を使用**<br>
新しい没入型カスタマイズのために、`view_type` エクストラをもう 1 つ追加します。`createInAppMessageView` メソッドをもう一度見直して、「スイッチ」UI のオプションを追加します。

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
**UI 表示動作に `view_type` を使用**<br>
新しい没入型カスタマイズのために、`view_type` エクストラをもう 1 つ追加します。`createInAppMessageView` メソッドをもう一度見直して、「スイッチ」UI のオプションを追加します。

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

**オーバーライドしてカスタムビューを提供する**<br>
標準のモーダルアプリ内メッセージを模倣したレイアウトを提供しますが、ビューをルート要素として指定し、そのレイアウトをインフレートします 
```xml
<?xml version="1.0" encoding="utf-8"?>
<com.braze.advancedsamples.immersive.CustomImmersiveInAppMessage
        xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas.android.com/tools" android:layout_width="match_parent"
        android:layout_height="wrap_content">
    <!-- giving the parent layout a white background color will obscure the app behind the IAM. You could also do this within your custom view -->
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
**ビューをインフレートしてカスタマイズする**<br>
`RecyclerView` コンポーネントのオプションを設定する前に、`inAppMessage` メッセージ変数が_文字列_として出力されます。正しく表示するには、このメッセージを項目の配列としてフォーマットする必要があります。例として、これは `String.split(",")` を使用して実現できます。`title`と`subtitle`も`extras`バンドルから抽出されます。

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
**ビューをインフレートしてカスタマイズする**<br>
`RecyclerView` コンポーネントのオプションを設定する前に、`inAppMessage` メッセージ変数が_文字列_として出力されます。正しく表示するには、このメッセージを項目の配列としてフォーマットする必要があります。例として、これは `String.split(",")` を使用して実現できます。`title`と`subtitle`も`extras`バンドルから抽出されます。

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
**カスタム属性を割り当てる**<br>
ユーザーがいずれかのスイッチを切り替えた後、ビューサブクラスを使用して、関連する属性とトグルステータスを Braze に渡します。

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
**カスタム属性を割り当てる**<br>
ユーザーがいずれかのスイッチを切り替えた後、ビューサブクラスを使用して、関連する属性とトグルステータスを Braze に渡します。

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

#### アプリ内メッセージタッチのインターセプト
![Androidデバイスが設定とトグルの行を表示しています。カスタムビューはボタンを処理し、ボタンコントロールの外側でのタッチはアプリ内メッセージによって処理され、閉じられます。]({% image_buster /assets/img/iam_implementation_guide_android.png %}){: style="float:right;max-width:30%;margin-left:10px;border:0"}
カスタムフルアプリ内メッセージボタンを正しく機能させるには、アプリ内メッセージのタッチをインターセプトすることが重要です。デフォルトでは、すべてのアプリ内メッセージビューに`onClick`リスナーが追加されるため、ユーザーはボタンなしでメッセージを閉じることができます。カスタムボタンなど、ユーザー入力に応答するカスタムコントロールを追加する場合は、通常どおりビューに`onClick`リスナーを登録できます。カスタムコントロールの外側をタッチすると、通常通りアプリ内メッセージが閉じられ、カスタムコントロールが受け取ったタッチはあなたの`onClick`リスナーを呼び出します。 

