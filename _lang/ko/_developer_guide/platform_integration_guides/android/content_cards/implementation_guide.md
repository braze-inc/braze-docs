---
nav_title: 고급 구현 가이드(선택 사항)
article_title: Android용 콘텐츠 카드 구현 가이드(선택 사항) 
platform: Android
page_order: 7
description: "이 고급 구현 가이드(선택 사항)에서는 Android 콘텐츠 카드 코드 고려사항, 저희 팀이 구축한 세 가지 사용 사례, 함께 제공되는 코드 스니펫, 노출 횟수, 클릭 및 해제 로깅에 대한 지침을 다룹니다."
channel:
  - content cards

---
# 고급 구현 가이드(선택 사항)

> 이 고급 구현 가이드(선택 사항)에서는 콘텐츠 카드 코드 고려사항, 저희 팀이 구축한 세 가지 커스텀 사용 사례, 함께 제공되는 코드 스니펫, 노출 횟수, 클릭 및 해제 로깅에 대한 지침을 다룹니다. [여기에서](https://github.com/braze-inc/braze-growth-shares-android-demo-app) Braze 데모 리포지토리를 방문하세요! 이 구현 가이드는 Kotlin 구현을 중심으로 하지만 관심 있는 사람을 위해 Java 스니펫도 제공됩니다.

{% alert important %}
기본 콘텐츠 카드 개발자 통합 가이드를 찾고 계신가요? [여기]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/integration/)에서 확인하세요.<br><br>콘텐츠 카드 사용자 지정에 대한 자세한 내용은 [사용자 지정 가이드]({{site.baseurl}}/developer_guide/customization_guides/content_cards)에서 확인할 수 있습니다.
{% endalert %}

## 코드 고려 사항

### 명령문 및 헬퍼 파일 가져오기

콘텐츠 카드를 빌드할 때는 단일 매니저 싱글톤을 통해 Braze SDK를 공개해야 합니다. 이 패턴은 사용 사례에 적합한 공유 추상화 이면의 Braze 구현 세부 정보으로부터 애플리케이션 코드를 보호합니다. 또한 이를 통해 코드를 더 쉽게 추적, 디버그 및 변경할 수 있습니다. 관리자 구현 예제는 [여기에서](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt) 확인할 수 있습니다.

### 사용자 지정 객체로서의 콘텐츠 카드

애플리케이션에서 이미 사용 중인 자체 커스텀 오브젝트를 확장하여 콘텐츠 카드 데이터를 전달함으로써 데이터 소스를 애플리케이션 코드에서 이미 이해하는 형식으로 추상화할 수 있습니다. 데이터 소스 추상화는 서로 다른 데이터 백엔드를 상호 호환적으로 함께 사용할 수 있는 유연성을 제공합니다. 이 예제에서는 `ContentCardable` 추상 기본 클래스를 정의하여 기존 데이터(이 예제에서는 로컬 JSON 파일에서 제공됨)와 Braze SDK에서 제공된 새 데이터를 모두 표시합니다. 기본 클래스는 원본 `Card` 구현에 액세스해야 하는 소비자를 위해 원시 콘텐츠 카드 데이터도 공개합니다.

Braze SDK에서 `ContentCardable` 인스턴스를 초기화할 때 `class_type` 추가 항목을 사용하여 콘텐츠 카드를 구체적인 서브클래스에 매핑합니다. 그런 다음, Braze 대시보드에 설정된 추가 키-값 페어를 사용하여 필요한 필드를 채웁니다.

이러한 코드 고려사항을 확실히 이해했다면 [사용 사례](#sample-use-cases)를 참조하여 자체 커스텀 오브젝트 구현을 시작합니다.

{% tabs local %}
{% tab 카드 종속성 없음 %}
{% subtabs global %}
{% subtab Kotlin %}
**`Card` 종속성 없음**<br>
`ContentCardData`는 `Card`의 구문 분석된 일반 값을 나타냅니다.

```kotlin
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

data class ContentCardData (var contentCardId: String,
                            var contentCardClassType: ContentCardClass,
                            var createdAt: Long,
                            var dismissable: Boolean)
```
{% endsubtab %}
{% subtab Java %}
**`Card` 종속성 없음**<br>
`ContentCardData`는 `Card`의 구문 분석된 일반 값을 나타냅니다.

```java
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
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab 사용자 지정 개체 %}
{% subtabs global %}
{% subtab Kotlin %}
**사용자 지정 객체 초기화 프로그램**<br>
`Card`의 메타데이터는 구체적인 서브클래스 변수를 채우는 데 사용됩니다. 하위 클래스에 따라 초기화 중에 다른 값을 추출해야 할 수도 있습니다. Braze 대시보드에 설정된 키-값 페어는 '추가 항목' 사전에 표시됩니다.

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
**사용자 지정 객체 초기화 프로그램**<br>
`Card`의 메타데이터는 구체적인 서브클래스 변수를 채우는 데 사용됩니다. 하위 클래스에 따라 초기화 중에 다른 값을 추출해야 할 수도 있습니다. Braze 대시보드에 설정된 키-값 페어는 '추가 항목' 사전에 표시됩니다.

```java
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
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab 유형 식별 %}
{% subtabs global %}
{% subtab Kotlin %}
**유형 식별**<br>
`ContentCardClass` 열거형은 Braze 대시보드에서 `class_type` 값을 표시하며, SDK에서 제공하는 문자열에서 열거형을 초기화하는 방법을 제공합니다.

```kotlin
enum class ContentCardClass{
    AD,
    COUPON,
    NONE,
    ITEM_TILE,
    ITEM_GROUP,
    MESSAGE_FULL_PAGE,
    MESSAGE_WEB_VIEW;

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
```
{% endsubtab %}
{% subtab Java %}
**유형 식별**<br>
`ContentCardClass` 열거형은 Braze 대시보드에서 `class_type` 값을 표시하며, SDK에서 제공하는 문자열에서 열거형을 초기화하는 방법을 제공합니다.

```java
enum ContentCardClass {
    AD,
    COUPON,
    NONE,
    ITEM_TILE,
    ITEM_GROUP,
    MESSAGE_FULL_PAGE,
    MESSAGE_WEB_VIEW

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
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 사용자 지정 카드 렌더링 {#customizing-card-rendering-for-android}

{% tabs local %}
{% tab Android 보기 시스템 %}

다음에는 `recyclerView`에서 카드가 렌더링되는 방식을 변경하는 방법에 대한 정보가 나와 있습니다. `IContentCardsViewBindingHandler` 인터페이스는 모든 콘텐츠 카드가 렌더링되는 방식을 정의합니다. 원하는 대로 변경하도록 사용자 지정할 수 있습니다:

{% subtabs %}
{% subtab JAVA %}

```java
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
   * If the {@link CardType} is not found in the cache, then a view binding implementation for that {@link CardType}
   * is created and added to the cache.
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

  // Parcelable interface method
  @Override
  public int describeContents() {
    return 0;
  }

  // Parcelable interface method
  @Override
  public void writeToParcel(Parcel dest, int flags) {
    // Retaining views across a transition could lead to a
    // resource leak so the parcel is left unmodified
  }
}
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
class DefaultContentCardsViewBindingHandler : IContentCardsViewBindingHandler {
  // Interface that must be implemented and provided as a public CREATOR
  // field that generates instances of your Parcelable class from a Parcel.
  val CREATOR: Parcelable.Creator<DefaultContentCardsViewBindingHandler?> = object : Parcelable.Creator<DefaultContentCardsViewBindingHandler?> {
    override fun createFromParcel(`in`: Parcel): DefaultContentCardsViewBindingHandler? {
      return DefaultContentCardsViewBindingHandler()
    }

    override fun newArray(size: Int): Array<DefaultContentCardsViewBindingHandler?> {
      return arrayOfNulls(size)
    }
  }

  /**
    * A cache for the views used in binding the items in the [RecyclerView].
    */
  private val mContentCardViewCache: MutableMap<CardType, BaseContentCardView<*>?> = HashMap()

  override fun onCreateViewHolder(context: Context?, cards: List<Card?>?, viewGroup: ViewGroup?, viewType: Int): ContentCardViewHolder? {
    val cardType = CardType.fromValue(viewType)
    return getContentCardsViewFromCache(context, cardType)!!.createViewHolder(viewGroup)
  }

  override fun onBindViewHolder(context: Context?, cards: List<Card>, viewHolder: ContentCardViewHolder?, adapterPosition: Int) {
    if (adapterPosition < 0 || adapterPosition >= cards.size) {
      return
    }
    val cardAtPosition = cards[adapterPosition]
    val contentCardView = getContentCardsViewFromCache(context, cardAtPosition.cardType)
    if (viewHolder != null) {
      contentCardView!!.bindViewHolder(viewHolder, cardAtPosition)
    }
  }

  override fun getItemViewType(context: Context?, cards: List<Card>, adapterPosition: Int): Int {
    if (adapterPosition < 0 || adapterPosition >= cards.size) {
      return -1
    }
    val card = cards[adapterPosition]
    return card.cardType.value
  }

  /**
    * Gets a cached instance of a [BaseContentCardView] for view creation/binding for a given [CardType].
    * If the [CardType] is not found in the cache, then a view binding implementation for that [CardType]
    * is created and added to the cache.
    */
  @VisibleForTesting
  fun getContentCardsViewFromCache(context: Context?, cardType: CardType): BaseContentCardView<Card>? {
    if (!mContentCardViewCache.containsKey(cardType)) {
      // Create the view here
      val contentCardView: BaseContentCardView<*> = when (cardType) {
        CardType.BANNER -> BannerImageContentCardView(context)
        CardType.CAPTIONED_IMAGE -> CaptionedImageContentCardView(context)
        CardType.SHORT_NEWS -> ShortNewsContentCardView(context)
        CardType.TEXT_ANNOUNCEMENT -> TextAnnouncementContentCardView(context)
        else -> DefaultContentCardView(context)
      }
      mContentCardViewCache[cardType] = contentCardView
    }
    return mContentCardViewCache[cardType] as BaseContentCardView<Card>?
  }

  // Parcelable interface method
  override fun describeContents(): Int {
    return 0
  }

  // Parcelable interface method
  override fun writeToParcel(dest: Parcel?, flags: Int) {
    // Retaining views across a transition could lead to a
    // resource leak so the parcel is left unmodified
  }
}
```

{% endsubtab %}
{% endsubtabs %}

이 코드는 여기에서도 찾을 수 있습니다. [`DefaultContentCardsViewBindingHandler`](https://github.com/braze-inc/braze-android-sdk/blob/v11.0.0/android-sdk-ui/src/main/java/com/appboy/ui/contentcards/handlers/DefaultContentCardsViewBindingHandler.java).

이 클래스를 사용하는 방법은 다음과 같습니다:

{% subtabs %}
{% subtab JAVA %}

```java
IContentCardsViewBindingHandler viewBindingHandler = new DefaultContentCardsViewBindingHandler();

ContentCardsFragment fragment = getMyCustomFragment();
fragment.setContentCardsViewBindingHandler(viewBindingHandler);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
val viewBindingHandler = DefaultContentCardsViewBindingHandler()

val fragment = getMyCustomFragment()
fragment.setContentCardsViewBindingHandler(viewBindingHandler)
```

{% endsubtab %}
{% endsubtabs %}

이 주제에 대한 추가 관련 리소스는 이 문서의 [Android 데이터 바인딩](https://medium.com/google-developers/android-data-binding-recyclerview-db7c40d9f0e4)에서 확인할 수 있습니다.

{% endtab %}
{% tab Jetpack Compose %}
Jetpack Compose에서 카드를 완전히 사용자 지정하려면 사용자 지정 Composable 함수를 생성하여 다음을 수행합니다.

1. Composable을 렌더링하고 `true`를 반환합니다.
2. 아무것도 렌더링하지 않고 `false` 을 반환합니다.  `false` 이 반환되면 Braze가 카드를 렌더링합니다.

다음 예제에서 Composable 함수는 `TEXT_ANNOUNCEMENT` 카드를 렌더링하고 나머지는 Braze에서 자동으로 렌더링합니다.

```kotlin
val myCustomCardRenderer: @Composable ((Card) -> Boolean) = { card ->
    if (card.cardType == CardType.TEXT_ANNOUNCEMENT) {
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
                    .basicMarquee(iterations = Int.MAX_VALUE),
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
```
{% endtab %}
{% endtabs %}

## 카드 해지

스와이프하여 해제 기능을 비활성화하는 방법은 카드별로 [`card.isDismissibleByUser()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/is-dismissible-by-user.html) 메서드를 통해 카드별로 수행됩니다. 메서드를 사용하여 표시하기 전에 카드를 가로챌 수 있습니다. [`ContentCardsFragment.setContentCardUpdateHandler()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/set-content-card-update-handler.html) 메서드를 사용하여 카드를 가로챌 수 있습니다.

## 다크 테마 사용자 지정

기본적으로 콘텐츠 카드 보기는 테마 색상 및 레이아웃 변경 집합을 통해 기기의 다크 테마 변경에 자동으로 대응합니다. 

이 동작을 재정의하려면 `android-sdk-ui/src/main/res/values-night/colors.xml` 및 `android-sdk-ui/src/main/res/values-night/dimens.xml`에서 `values-night` 값을 재정의합니다.

## 노출 횟수, 클릭, 해제 기록

사용자 지정 개체를 콘텐츠 카드로 작동하도록 확장한 후 노출 수, 클릭 수, 해지 수와 같은 중요한 지표를 기록하는 것은 `BrazeManager` 에 데이터를 참조하고 제공하는 `ContentCardable` 베이스 클래스를 사용하여 수행할 수 있습니다.

#### **구현 구성요소**<br><br>

{% tabs %}
{% tab Kotlin %}
**사용자 정의 객체는 로깅 메서드를 호출합니다.**<br>
`ContentCardable` 기본 클래스 내에서 해당되는 경우 `BrazeManager`를 직접 호출할 수 있습니다. 이 예제에서 오브젝트를 콘텐츠 카드에서 가져온 경우 `cardData` 속성정보는 null이 아닙니다. 

```kotlin
override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val tile = currentTiles[position]
        tile.logContentCardImpression()
        ...
    }
```

**`ContentCardId`에서 콘텐츠 카드 검색**<br>
`ContentCardable` 기본 클래스는 `BrazeManager`를 호출하고 커스텀 오브젝트와 연결된 콘텐츠 카드의 고유 식별자를 전달하는 복잡한 작업을 처리합니다.

```kotlin
    fun logContentCardImpression() {
        cardData?.let { BrazeManager.getInstance().logContentCardImpression(it.contentCardId) }
    }
```

**`Card` 함수 호출**<br>
[`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt)는 Braze SDK 종속성(예: 콘텐츠 카드 오브젝트 배열 목록)을 참조하여 `Card`를 가져와 로깅 메서드를 호출할 수 있습니다.

```kotlin
    fun logContentCardClicked(idString: String?) {
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
**사용자 정의 객체는 로깅 메서드를 호출합니다.**<br>
`ContentCardable` 기본 클래스 내에서 해당되는 경우 `BrazeManager`를 직접 호출할 수 있습니다. 이 예제에서 오브젝트를 콘텐츠 카드에서 가져온 경우 `cardData` 속성정보는 null이 아닙니다. 
```java
@Override
public View getView(int position, View convertView, ViewGroup parent) {
        Tile tile = currentTiles.get(position);
        tile.logContentCardImpression();
        ...
    }
```

**`ContentCardId`에서 콘텐츠 카드 검색**<br>
`ContentCardable` 기본 클래스는 `BrazeManager`를 호출하고 커스텀 오브젝트와 연결된 콘텐츠 카드의 고유 식별자를 전달하는 복잡한 작업을 처리합니다.

```java
    public void logContentCardImpression() {
        if (cardData != null){
            BrazeManager.getInstance().logContentCardImpression(cardData.getContentCardId());
        }
    }
```

**`Card` 함수 호출**<br>
[`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt)는 Braze SDK 종속성(예: 콘텐츠 카드 오브젝트 배열 목록)을 참조하여 `Card`를 가져와 로깅 메서드를 호출할 수 있습니다.

```java
    public void logContentCardClicked(String idString) {
        getContentCard(idString).ifPresent(Card::logClick);
    }

    public void logContentCardImpression(String idString) {
        getContentCard(idString).ifPresent(Card::logImpression);
    }

    private Optional<Card> getContentCard(String idString) {
        return cardList.filter(c -> c.id.equals(idString)).findAny();
    }
```
{% endtab %}
{% endtabs %}

{% alert important %}
제어 배리언트 콘텐츠 카드의 경우 커스텀 오브젝트는 여전히 인스턴스화되어야 하며 UI 로직은 오브젝트의 해당 보기를 숨김으로 설정해야 합니다. 그런 다음, 오브젝트는 사용자가 제어 카드를 보았을 때를 분석 팀에 알릴 노출 횟수를 기록할 수 있습니다.
{% endalert %}

## 도우미 파일

{% details ContentCardKey 헬퍼 파일 %}
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

