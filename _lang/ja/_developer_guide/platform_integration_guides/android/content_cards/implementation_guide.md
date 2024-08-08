---
nav_title: 高度な実装ガイド (オプション)
article_title: Android 用コンテンツカード実装ガイド (オプション) 
platform: Android
page_order: 7
description: "この高度な実装ガイドでは、Android コンテンツカードのコードに関する考慮事項、当社チームが構築した3つのユースケース、付随するコードスニペット、およびロギングインプレッション、クリック、および削除に関するガイダンスについて説明します。"
channel:
  - content cards

---
# 高度な実装ガイド (オプション)

> このオプションおよび高度な実装ガイドでは、コンテンツカードコードの考慮事項、当社チームが作成した3つのカスタムユースケース、付随するコードスニペット、およびロギングインプレッション、クリック、および削除に関するガイダンスについて説明します。[こちらから](https://github.com/braze-inc/braze-growth-shares-android-demo-app) Braze Demo リポジトリにアクセスしてください。この実装ガイドは、Kotlin 実装を中心に扱っていますが、興味のある人のために Java のスニペットが提供されています。

{% alert important %}
基本的なコンテンツカード開発者統合ガイドをお探しですか?[こちら]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/integration/)にあります。<br><br>コンテンツカードのカスタマイズの詳細については、[カスタマイズガイド]({{site.baseurl}}/developer_guide/customization_guides/content_cards)を参照してください。
{% endalert %}

## コードに関する考慮事項

### ステートメントおよびヘルパーファイルのインポート

コンテンツカードを作成する場合は、単一のマネージャーシングルトンを介して Braze SDK を公開する必要があります。このパターンにより、ユースケースに適した共通の抽象化の背後にある Braze 実装の詳細からアプリケーションコードを保護します。また、コードの追跡、デバッグ、変更も容易になります。マネージャの実装例は、[こちら](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt)でご覧いただけます。

### カスタムオブジェクトとしてのコンテンツカード

アプリケーションで既に使用されている独自のカスタムオブジェクトを拡張して、コンテンツカードデータを運ぶことができます。これにより、データのソースをアプリケーションコードで既に理解されている形式に抽象化できます。データソースの抽象化は、異なるデータバックエンドと互換性があり、同時に動作する柔軟性を提供します。この例では、`ContentCardable`抽象ベースクラスを定義して、既存のデータ (この例では、ローカル JSON ファイルからフィードされます) と Braze SDK からフィードされる新しいデータの両方を表します。また、ベースクラスは、元の`Card`実装にアクセスする必要がある消費者のコンテンツカードの生データも公開します。

Braze SDK から`ContentCardable`インスタンスを初期化する場合、`class_type` extra を使用して、コンテンツカードを具象サブクラスにマップします。次に、Braze ダッシュボード内で設定された追加のキーと値のペアを使用して、必要なフィールドに入力します。

これらのコードに関する考慮事項をしっかりと理解したら、[ユースケース](#sample-use-cases)をチェックして、独自のカスタムオブジェクトの実装を開始します。

{% tabs local %}
{% tab No Card Dependencies %}
{% subtabs global %}
{% subtab Kotlin %}
**`Card`依存関係なし**<br>
`ContentCardData` は、`Card` の解析された共通の値を表します。

\`\`\`kotlin
abstract class ContentCardable (){

    var cardData: ContentCardData? = null

    constructor(data:Map<String, Any>):this(){
        cardData = ContentCardData(data[idString] as String,
            ContentCardClass.valueFrom(data[classType] as String),
            data[created] as Long,
            data[dismissable] as Boolean)
    }

    val isContentCard: Boolean
        get() = cardData != null

    fun logContentCardClicked() {
        BrazeManager.getInstance().logContentCardClicked(cardData?.contentCardId)
    }

    fun logContentCardDismissed() {
        BrazeManager.getInstance().logContentCardDismissed(cardData?.contentCardId)
    }

    fun logContentCardImpression() {
        BrazeManager.getInstance().logContentCardImpression(cardData?.contentCardId)
    }
}

data class ContentCardData (var contentCardId:String,
                            var contentCardClassType:ContentCardClass,
                            var createdAt:Long,
                            var dismissable:Boolean)
\`\`\`
{% endsubtab %}
{% subtab Java %}
**`Card`依存関係なし**<br>
`ContentCardData` は、`Card` の解析された共通の値を表します。

\`\`\`java
public abstract class ContentCardable{

  private ContentCardData cardData = null;

  public ContentCardable(Map<String, Object> data){
      cardData = new ContentCardData()
      cardData.contentCardId = (String) data.get(idString);
      cardData.contentCardClassType = contentCardClassType.valueOf((String)data.get(classType));
      cardData.createdAt = Long.parseLong((String)data.get(createdAt));
      cardData.dismissable = Boolean.parseBoolean((String)data.get(dismissable));
  }

  public ContentCardable(){

  }

  public boolean isContentCard(){
    return cardData != null;
  }

  public void logContentCardClicked() {
    if (isContentCard()){
      BrazeManager.getInstance().logContentCardClicked(cardData.contentCardId)
    }
  }

  public void logContentCardDismissed() {
    if(isContentCard()){
      BrazeManager.getInstance().logContentCardDismissed(cardData.contentCardId)
    }
  }

  public void logContentCardImpression() {
    if(isContentCard()){
      BrazeManager.getInstance().logContentCardImpression(cardData.contentCardId)
    }
  }
}

public class ContentCardData{
  public String contentCardId;
  public ContentCardClass contentCardClassType;
  public long createdAt;
  public boolean dismissable;
}
\`\`\`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Custom Objects %}
{% subtabs global %}
{% subtab Kotlin %}
**カスタムオブジェクトイニシャライザ**<br>
`Card` からの MetaData は、具象サブクラスの変数を入力するために使用されます。サブクラスによっては、初期化時に異なる値を抽出する必要があります。Braze ダッシュボードで設定されたキーと値のペアは、「extras」ディクショナリに表示されます。

```kotlin
class Tile: ContentCardable {
    constructor(metadata:Map<String, Any>):super(metadata){
        val extras = metadata[extras] as? Map<String, Any>
        title = extras?.get(Keys.title) as? String
        image = extras?.get(Keys.image) as? String
        detail = metadata[ContentCardable.detail] as? String
        tags = (metadata[ContentCardable.tags] as? String)?.split(",")
        val priceString = extras?.get(Keys.price) as? String
        if (priceString?.isNotEmpty() == true){
            price = priceString.toDouble()
        }
        id = floor(Math.random()*1000).toInt()
    }
  }
```
{% endsubtab %}
{% subtab Java %}
**カスタムオブジェクトイニシャライザ**<br>
`Card` からの MetaData は、具象サブクラスの変数を入力するために使用されます。サブクラスによっては、初期化時に異なる値を抽出する必要があります。Braze ダッシュボードで設定されたキーと値のペアは、「extras」ディクショナリに表示されます。

\`\`\`java
public class Tile extends ContentCardable {

    public Tile(Map<String, Object> metadata){
        super(metadata);
        this.detail = (String) metadata.get(ContentCardable.detail);
        this.tags = ((String)metadata.get(ContentCardable.tags)).split(",");
        if (metadata.containsKey(Keys.extras)){
            Map<String, Object> extras = metadata.get(Keys.extras);
            this.title = (String)extras.get(Keys.title);
            this.price = Double.parseDouble((String)extras.get(Keys.price));
            this.image = (String)extras.get(Keys.image);

        }
    }
}
\`\`\`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Identifying Types %}
{% subtabs global %}
{% subtab Kotlin %}
**タイプの識別**<br>
`ContentCardClass` enum は、Braze ダッシュボードの`class_type`値を表し、SDK によって提供される文字列から enum を初期化するメソッドを提供します。

\`\`\`kotlin
enum class ContentCardClass{
    AD,
    COUPON,
    NONE,
    ITEM\_TILE,
    ITEM\_GROUP,
    MESSAGE\_FULL\_PAGE,
    MESSAGE\_WEB\_VIEW;

    companion object {
        // This value must be synced with the `class_type` value that has been set up in your
        // Braze dashboard or its type will be set to `ContentCardClassType.none.`
        fun valueFrom(str: String?): ContentCardClass {
            return when(str?.toLowerCase()){
                "coupon_code" -> COUPON
                "home_tile" -> ITEM_TILE
                "group" -> ITEM_GROUP
                "message_full_page" -> MESSAGE_FULL_PAGE
                "message_webview" -> MESSAGE_WEB_VIEW
                "ad_banner" -> AD
                else -> NONE
            }
        }
    }
}
\`\`\`
{% endsubtab %}
{% subtab Java %}
**タイプの識別**<br>
`ContentCardClass` enum は、Braze ダッシュボードの`class_type`値を表し、SDK によって提供される文字列から enum を初期化するメソッドを提供します。

\`\`\`java
enum ContentCardClass {
    AD,
    COUPON,
    NONE,
    ITEM\_TILE,
    ITEM\_GROUP,
    MESSAGE\_FULL\_PAGE,
    MESSAGE\_WEB\_VIEW

    public static valueFrom(String val){
        switch(val.toLowerCase()){
            case "coupon_code":{
                return COUPON;
            }
            case "home_tile":{
                return ITEM_TILE;
            }
            case "group":{
                return ITEM_GROUP;
            }
            case "message_full_page":{
                return MESSAGE_FULL_PAGE;
            }
            case "message_webview":{
                return MESSAGE_WEB_VIEW;
            }
            case "ad_banner":{
                return AD;
            }
            default:{
                return NONE;
            }
        }
    }
}
\`\`\`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## カスタムカードレンダリング{#customizing-card-rendering-for-android}

{% tabs local %}
{% tab Android View System %}

次のリストは、`recyclerView`でカードをレンダリングする方法の変更について示しています。`IContentCardsViewBindingHandler`インターフェイスは、すべてのコンテンツカードのレンダリング方法を定義します。これをカスタマイズして、必要なものを変更することができます。

{% subtabs %}
{% subtab JAVA %}

\`\`\`java
public class DefaultContentCardsViewBindingHandler implements IContentCardsViewBindingHandler {
  // Interface that must be implemented and provided as a public CREATOR
// field that generates instances of your Parcelable class from a Parcel.
  public static final Parcelable.Creator<DefaultContentCardsViewBindingHandler> CREATOR = new Parcelable.Creator<DefaultContentCardsViewBindingHandler>() {
  public DefaultContentCardsViewBindingHandler createFromParcel(Parcel in) {
    return new DefaultContentCardsViewBindingHandler();
      }

    public DefaultContentCardsViewBindingHandler[] newArray(int size) {
      return new DefaultContentCardsViewBindingHandler[size];
    }
  };

  /**
* A cache for the views used in binding the items in the {@link android.support.v7.widget.RecyclerView}.
*/
   private final Map<CardType, BaseContentCardView> mContentCardViewCache = new HashMap<CardType, BaseContentCardView>();

  @Override
  public ContentCardViewHolder onCreateViewHolder(Context context, List<? extends Card> cards, ViewGroup viewGroup, int viewType) {
    CardType cardType = CardType.fromValue(viewType);
    return getContentCardsViewFromCache(context, cardType).createViewHolder(viewGroup);
  }

  @Override
  public void onBindViewHolder(Context context, List<? extends Card> cards, ContentCardViewHolder viewHolder, int adapterPosition) {
    Card cardAtPosition = cards.get(adapterPosition);
    BaseContentCardView contentCardView = getContentCardsViewFromCache(context, cardAtPosition.getCardType());
    contentCardView.bindViewHolder(viewHolder, cardAtPosition);
  }

  @Override
  public int getItemViewType(Context context, List<? extends Card> cards, int adapterPosition) {
    Card card = cards.get(adapterPosition);
    return card.getCardType().getValue();
  }

  /**
* Gets a cached instance of a {@link BaseContentCardView} for view creation/binding for a given {@link CardType}.
   \* {@link CardType} がキャッシュ内に見つからない場合、その {@link CardType} のビューバインディング実装
   \* が作成され、キャッシュに追加されます。
   */
@VisibleForTesting
BaseContentCardView getContentCardsViewFromCache(Context context, CardType cardType) {
if (!mContentCardViewCache.containsKey(cardType)) {
// Create the view here
   BaseContentCardView contentCardView;
  switch (cardType) {
case BANNER:
contentCardView = new BannerImageContentCardView(context);
break;
case CAPTIONED_IMAGE:
contentCardView = new CaptionedImageContentCardView(context);
break;
case SHORT_NEWS:
contentCardView = new ShortNewsContentCardView(context);
break;
case TEXT_ANNOUNCEMENT:
contentCardView = new TextAnnouncementContentCardView(context);
break;
default:
contentCardView = new DefaultContentCardView(context);
break;
}
  mContentCardViewCache.put(cardType, contentCardView);
    }
      return mContentCardViewCache.get(cardType);
      }

  // パーセル可能なインターフェイス方式
  @Override
  public int describeContents() {
    return 0;
  }

  // Parcelable interface method
@Override
public void writeToParcel(Parcel dest, int flags) {
// Retaining views across a transition could lead to a
  // リソースがリークするため、パーセルが変更されないままになります
  }
    }
    \`\`\`

{% endsubtab %}
{% subtab KOTLIN %}

\`\`\`kotlin
class DefaultContentCardsViewBindingHandler :IContentCardsViewBindingHandler {
  // Interface that must be implemented and provided as a public CREATOR
// field that generates instances of your Parcelable class from a Parcel.
  val CREATOR:Parcelable.Creator<DefaultContentCardsViewBindingHandler?> = object :Parcelable.Creator<DefaultContentCardsViewBindingHandler?> {
  override fun createFromParcel(`in`:Parcel):DefaultContentCardsViewBindingHandler? {
    return DefaultContentCardsViewBindingHandler()
      }

    override fun newArray(size: Int): Array<DefaultContentCardsViewBindingHandler?> {
      return arrayOfNulls(size)
    }
  }

  /\**
    \* [RecyclerView] 内の項目のバインドに使用されるビューのキャッシュ。
    */
  private val mContentCardViewCache:MutableMap<CardType, BaseContentCardView<*>?> = HashMap()

  override fun onCreateViewHolder(context:Context?, cards:List<Card?>?, viewGroup:ViewGroup?, viewType:Int):ContentCardViewHolder? {
    val cardType = CardType.fromValue(viewType)
    return getContentCardsViewFromCache(context, cardType)!!.createViewHolder(viewGroup)
  }

  override fun onBindViewHolder(context:Context?, cards:Context?, cards:ContentCardViewHolder?, adapterPosition:Int) {
    if (adapterPosition < 0 || adapterPosition >= cards.size) {
      return
    }
    val cardAtPosition = cards[adapterPosition]
    val contentCardView = getContentCardsViewFromCache(context, cardAtPosition.cardType)
    if (viewHolder != null) {
      contentCardView!!.bindViewHolder(viewHolder, cardAtPosition)
    }
  }

  override fun getItemViewType(context:Context?, cards:List<Card>, adapterPosition:Int):Int {
    if (adapterPosition < 0 || adapterPosition >= cards.size) {
      return -1
    }
    val card = cards[adapterPosition]
    return card.cardType.value
  }

  /**
* Gets a cached instance of a [BaseContentCardView] for view creation/binding for a given [CardType].
    \* [CardType] がキャッシュに見つからない場合、その [CardType] のビューバイディング実装
    \* が作成され、キャッシュに追加されます。
    */
    @VisibleForTesting
  fun getContentCardsViewFromCache(context:Context?, cardType:CardType):BaseContentCardView<Card>? {
  if (!mContentCardViewCache.containsKey(cardType)) {
    // ここでビューを作成します
      val contentCardView:BaseContentCardView<*> = when (cardType) {
      CardType.BANNER -> BannerImageContentCardView(context)
        CardType.CAPTIONED\_IMAGE -> CaptionedImageContentCardView(context)
        CardType.SHORT\_NEWS -> ShortNewsContentCardView(context)
        CardType.TEXT\_ANNOUNCEMENT -> TextAnnouncementContentCardView(context)
        else -> DefaultContentCardView(context)
        }
      mContentCardViewCache[cardType] = contentCardView
      }
    return mContentCardViewCache[cardType] as BaseContentCardView<Card>?
    }

  // パーセル可能なインターフェイス方式
  override fun describeContents():Int {
    return 0
  }

  // Parcelable interface method
override fun writeToParcel(dest: Parcel?, flags: Int) {
// Retaining views across a transition could lead to a
  // リソースがリークするため、パーセルが変更されないままになります
    }
    }
  \`\`\`

{% endsubtab %}
{% endsubtabs %}

このコードは [\`DefaultContentCardsViewBindingHandler\`][56] にもあります。

次に、このクラスの使用方法を示します。

{% subtabs %}
{% subtab JAVA %}

\`\`\`java
IContentCardsViewBindingHandler viewBindingHandler = new DefaultContentCardsViewBindingHandler();

ContentCardsFragment fragment = getMyCustomFragment();
fragment.setContentCardsViewBindingHandler(viewBindingHandler);
\`\`\`

{% endsubtab %}
{% subtab KOTLIN %}

\`\`\`kotlin
val viewBindingHandler = DefaultContentCardsViewBindingHandler()

val fragment = getMyCustomFragment()
fragment.setContentCardsViewBindingHandler(viewBindingHandler)
\`\`\`

{% endsubtab %}
{% endsubtabs %}

このトピックに関するその他の関連リソースは、[Android Data Binding](https://medium.com/google-developers/android-data-binding-recyclerview-db7c40d9f0e4) に関するこの記事で入手できます。

{% endtab %}
{% tab Jetpack Compose %}
Jetpack Compose でカードを完全にカスタマイズする場合、カスタムの Composable 関数を作成すると次のようになります。

1. Composable をレンダリングし、`true`を返します。
2. 何もレンダリングせず、`false`を返します。 `false`が返されると、Braze はカードをレンダリングします。

次の例では、Composable 関数は`TEXT_ANNOUNCEMENT`カードをレンダリングし、Braze は残りを自動的にレンダリングします。

\`\`\`kotlin
val myCustomCardRenderer: @Composable ((Card) -> Boolean) = { card ->
    if (card.cardType == CardType.TEXT\_ANNOUNCEMENT) {
        val textCard = card as TextAnnouncementCard
        Box(
            Modifier
                .padding(10.dp)
                .fillMaxWidth()
                .background(color = Color.Red)
        ) {
            Text(
                modifier = Modifier
                    .align(Alignment.Center)
                    .fillMaxWidth()
                    .basicMarquee(iterations = Int.MAX\_VALUE),
                fontSize = 35.sp,
                text = textCard.description
            )
        }
        true
    } else {
        false
    }
}

ContentCardsList(
    customCardComposer = myCustomCardRenderer
)
\`\`\`
{% endtab %}
{% endtabs %}

## カードの却下

スワイプして閉じる機能を無効にするには、[\`card.isDismissibleByUser()\`][9] メソッドを使用してカードごとに行います。[\`ContentCardsFragment.setContentCardUpdateHandler()\`][8] メソッドを使用して、表示前にカードをインターセプトできます。

## ダークテーマのカスタマイズ

デフォルトでは、コンテンツカードビューは、テーマカラーとレイアウト変更のセットでデバイスのダークテーマの変更に自動的に応答します。 

この動作をオーバーライドするには、`android-sdk-ui/src/main/res/values-night/colors.xml`および`android-sdk-ui/src/main/res/values-night/dimens.xml`の`values-night`の値をオーバーライドします。

## インプレッション、クリック、却下の記録

カスタムオブジェクトをコンテンツカードとして機能するように拡張した後、`BrazeManager`を参照してデータを提供する`ContentCardable`ベースクラスを使用して、インプレッション、クリック、および却下などの貴重なメトリクスをログに記録することができます。

#### **実装コンポーネント**<br><br>

{% tabs %}
{% tab Kotlin %}
**カスタムオブジェクトによるロギングメソッドの呼び出し**<br>
`ContentCardable` ベースクラス内で、必要に応じて`BrazeManager`を直接呼び出すことができます。この例では、オブジェクトがコンテンツカードから取得された場合、`cardData`プロパティは NULL 以外になります。 

```kotlin
override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val tile = currentTiles[position]
        tile.logContentCardImpression()
        ...
    }
```

**`ContentCardId`からコンテンツカードを取得する**<br>
`ContentCardable`ベースクラスは、`BrazeManager`を呼び出し、カスタムオブジェクトに関連付けられたコンテンツカードから一意の識別子を渡すという負荷の大きい処理を行います。

```kotlin
    fun logContentCardImpression() {
        cardData?.let { BrazeManager.getInstance().logContentCardImpression(it.contentCardId) }
    }
```

**`Card`関数を呼び出す**<br>
[`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt)は、コンテンツカードオブジェクト配列リストなどの Braze SDK 依存関係を参照して、`Card`にロギングメソッドを呼び出させることができます。

\`\`\`kotlin
    fun logContentCardClicked(idString:String?) {
        getContentCard(idString)?.logClick()
    }

    fun logContentCardImpression(idString: String?) {
        getContentCard(idString)?.logImpression()
    }

    private fun getContentCard(idString: String?): Card? {
        return cardList.find { it.id == idString }.takeIf { it != null }
    }
```
{% endtab %}
{% tab Java %}
**Custom objects call the logging methods**<br>
Within your `ContentCardable` base class, you can call the `BrazeManager` directly, if appropriate. Remember, in this example, the `cardData` property will be non-null if the object came from a Content Card. 
```java
@Override
public View getView(int position, View convertView, ViewGroup parent) {
        Tile tile = currentTiles.get(position);
        tile.logContentCardImpression();
        ...
    }
\`\`\`

**`ContentCardId`からコンテンツカードを取得する**<br>
`ContentCardable`ベースクラスは、`BrazeManager`を呼び出し、カスタムオブジェクトに関連付けられたコンテンツカードから一意の識別子を渡すという負荷の大きい処理を行います。

```java
    public void logContentCardImpression() {
        if (cardData != null){
            BrazeManager.getInstance().logContentCardImpression(cardData.getContentCardId());
        }
    }
```

**`Card`関数を呼び出す**<br>
[`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt)は、コンテンツカードオブジェクト配列リストなどの Braze SDK 依存関係を参照して、`Card`にロギングメソッドを呼び出させることができます。

\`\`\`java
    public void logContentCardClicked(String idString) {
getContentCard(idString).ifPresent(Card::logClick);
}

    public void logContentCardImpression(String idString) {
        getContentCard(idString).ifPresent(Card::logImpression);
    }

    private Optional<Card> getContentCard(String idString) {
        return cardList.filter(c -> c.id.equals(idString)).findAny();
    }
\`\`\`
{% endtab %}
{% endtabs %}

{% alert important %}
コントロールバリアントのコンテンツカードの場合、カスタムオブジェクトはインスタンス化されたままで、UI ロジックはオブジェクトの対応するビューを非表示に設定する必要があります。その後、オブジェクトはインプレッションをログに記録して、ユーザーがいつコントロールカードを表示したかを分析に知らせることができます。
{% endalert %}

## ヘルパーファイル

{% details ContentCardKey Helper File %}
{% tabs %}
{% tab Kotlin %}
```kotlin
companion object Keys{
        const val idString = "idString"
        const val created = "created"
        const val classType = "class_type"
        const val dismissable = "dismissable"
        //...
    }
```
{% endtab %}
{% tab Java %}
```java
public static final String IDSTRING = "idString";
public static final String CREATED = "created";
public static final String CLASSTYPE = "class_type";
public static final String DISMISSABLE = "dismissable";
...
```
{% endtab %}
{% endtabs %}
{% enddetails %}

[1]: {% image_buster /assets/img/cc_implementation/android_supplemental_content.png %}
[2]: {% image_buster /assets/img/cc_implementation/supplementary_content.png %}
[3]: {% image_buster /assets/img/cc_implementation/android_message_center.png %}
[4]: {% image_buster /assets/img/cc_implementation/full_page.png %}
[5]: {% image_buster /assets/img/cc_implementation/html_webview.png %}
[6]: {% image_buster /assets/img/cc_implementation/android_discount2.png %}
[7]: {% image_buster /assets/img/cc_implementation/discount.png %}
[8]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/set-content-card-update-handler.html
[9]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/is-dismissible-by-user.html
[36]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization
[42]: https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml
[44]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html
[45]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/set-content-card-update-handler.html
[46]: https://github.com/braze-inc/braze-android-sdk/blob/v11.0.0/android-sdk-ui/src/main/java/com/appboy/ui/contentcards/handlers/DefaultContentCardsUpdateHandler.java
[49]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html
[56]: https://github.com/braze-inc/braze-android-sdk/blob/v11.0.0/android-sdk-ui/src/main/java/com/appboy/ui/contentcards/handlers/DefaultContentCardsViewBindingHandler.java