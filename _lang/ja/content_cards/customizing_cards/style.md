---
nav_title: スタイル
article_title: コンテンツカードのスタイルのカスタマイズ
page_order: 1
description: "この記事では、コンテンツ カードのスタイルオプションについて説明します。"
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# コンテンツカードのスタイルのカスタマイズ

> Braze コンテンツ カードには、デフォルトのルック アンドフィールが含まれています。この記事では、ブランドアイデンティティに合わせるためのコンテンツ カードのスタイルオプションについて説明します。コンテンツカードタイプの完全なリストについては、[コンテンツカードについて]({{site.baseurl}}/developer_guide/content_cards/)を参照してください。

## カスタムスタイルの作成

デフォルトのコンテンツ カード UI は、Braze SDK の UI レイヤーからインポートされます。そこから、カードのスタイルの特定の部分、カードが表示される順序、フィードがユーザーに表示される方法を調整できます。

![2枚のコンテンツ・カード、1枚はデフォルトのフォントで角が四角いもの、もう1枚は角が丸くカーリーフォントのものである。]({% image_buster/assets/img/content_cards/content-card-customization-attributes.png %})

{% alert note %}
コンテンツ カードのプロパティ`title`、 `cardDescription`、`imageUrl`などは、[ダッシュボード]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details)から直接編集できます。これは、詳細を変更するための推奨される方法です。
{% endalert %}


{% tabs %}
{% tab web %}

Braze のデフォルトスタイルは、Braze SDK 内の CSS で定義されます。アプリケーションで選択したスタイルを上書きすることで、独自の背景画像、フォントファミリ、スタイル、サイズ、アニメーションなどを使用して標準フィードをカスタマイズできます。たとえば、次の例はコンテンツカードを幅800 ピクセルで表示する上書きを示しています。

``` css
body .ab-feed {
  width: 800px;
}
```

{% endtab %}
{% tab android %}

デフォルトでは、Android および FireOS SDK コンテンツカードは標準の Android UI ガイドラインに一致し、シームレスなエクスペリエンスを提供します。これらのデフォルトのスタイルは、Braze SDK ディストリビューション内の[`res/values/styles.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml)ファイルで確認できます。

```xml
  <style name="Braze.ContentCards.CaptionedImage.Description">
    <item name="android:textColor">@color/com_braze_description</item>
    <item name="android:textSize">15.0sp</item>
    <item name="android:includeFontPadding">false</item>
    <item name="android:paddingBottom">8.0dp</item>
    <item name="android:layout_marginLeft">10.0dp</item>
    <item name="android:layout_marginRight">10.0dp</item>
    <item name="android:layout_marginTop">8.0dp</item>
    <item name="android:layout_width">match_parent</item>
    <item name="android:layout_below">@id/com_braze_content_cards_captioned_image_card_title_container</item>
  </style>
```

コンテンツカードのスタイルをカスタマイズするには、このデフォルトのスタイルを上書きします。スタイルを上書きするには、スタイル全体をプロジェクトの`styles.xml`ファイルにコピーし、変更を加えます。すべての属性が正しく設定されるようにするには、スタイル全体をローカルの`styles.xml`にコピーする必要があります。

{% subtabs local %}
{% subtab Correct style override %}

```xml
<style name="Braze.ContentCardsDisplay">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
  <item name="android:divider">@android:color/transparent</item>
  <item name="android:dividerHeight">16.0dp</item>
  <item name="android:paddingLeft">12.5dp</item>
  <item name="android:paddingRight">5.0dp</item>
  <item name="android:scrollbarStyle">outsideInset</item>
</style>
```

{% endsubtab %}
{% subtab Incorrect style override %}

```xml
<style name="Braze.ContentCardsDisplay">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
</style>
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Jetpack Compose %}

デフォルトでは、Android および FireOS SDK コンテンツカードは標準の Android UI ガイドラインに一致し、シームレスなエクスペリエンスを提供します。

2つの方法のいずれかでスタイルを適用できます。まず、以下の例のように、[`ContentCardListStyling`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-list-styling/index.html) および[`ContentCardStyling`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html) を[`ContentCardsList`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards/-content-cards-list.html) に渡します。

```kotlin
ContentCardsList(
    style = ContentCardListStyling(listBackgroundColor = Color.Red),
    cardStyle = ContentCardStyling(
        titleTextStyle = TextStyle(
            fontFamily = fontFamily,
            fontSize = 25.sp
        ),
        shadowRadius = 10.dp,
        shortNewsContentCardStyle = BrazeShortNewsContentCardStyling(
            shadowRadius = 15.dp
        )
    )
)
```

2 つ目は、[`BrazeStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose/-braze-style.html) を使用して、次の例のようにBraze コンポーネントのグローバルスタイルを作成します。

```kotlin
BrazeStyle(
    contentCardStyle = ContentCardStyling(
        textAnnouncementContentCardStyle = BrazeTextAnnouncementContentCardStyling(
            cardBackgroundColor = Color.Red,
            descriptionTextStyle = TextStyle(
                fontFamily = fontFamily,
                fontSize = 25.sp,
            )
        ),
        titleTextColor = Color.Magenta
    )
) {
    // Your app here, including any ContentCardsList() in it
}
```

{% endtab %}
{% tab swift %}

コンテンツカードビューコントローラーを使用すると、[`BrazeContentCardUI.ViewController.Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct)構造体を介してすべてのセルの外観と動作をカスタマイズできます 。`Attributes`を使用したコンテンツカードの設定は簡単なオプションであり、最小限の設定でコンテンツカード UI を立ち上げることができます。 

{% alert important %}
`Attributes`によるカスタマイズは、Swift でのみ利用可能です。
{% endalert %}

{% subtabs %}
{% subtab Swift %}

**`Attributes.default`の変更**

静的[`Attributes.defaults`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults)変数を直接変更して、Braze コンテンツカード UI ビュー コントローラーのすべてのインスタンスのルックアンドフィールをカスタマイズします。 

たとえば、すべてのセルのデフォルトの画像サイズと角の半径を変更するには、次のようにします。

```swift
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.cornerRadius = 20
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.classicImageSize = CGSize(width: 65, height: 65)
```

**属性を使用してビューコントローラーを初期化する**

Braze コンテンツカード UI ビュー コントローラーの特定のインスタンスのみを変更する場合は、[`init(braze:attributes:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/init(braze:attributes:)/)初期化子を使用してカスタムの`Attributes`構造体をビューコントローラーに渡します。

たとえば、ビュー コントローラーの特定のインスタンスの画像サイズと角の半径を変更できます。

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.cornerRadius = 20
attributes.cellAttributes.classicImageSize = CGSize(width: 65, height: 65)

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

**サブクラス化によるセルのカスタマイズ**

また、必要なカードタイプごとにカスタムクラスを登録して、カスタムインターフェイスを作成することもできます。デフォルトのセルの代わりにサブクラスを使用するには、`Attributes`構造体の[`cells`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cells)プロパティを変更します。以下に例を示します。

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
// Register your own custom cell
attributes.cells[BrazeContentCardUI.ClassicImageCell.identifier] = CustomClassicImageCell.self

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

**プログラムによるコンテンツカードの変更**

コンテンツ カードは、`Attributes`構造体の[`transform`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/transform)クロージャを割り当てることで、プログラムにより変更できます。以下の例では、互換性のあるカードの`title`と`description`を変更しています。

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.transform = { cards in
  cards.map { card in
    var card = card
    if let title = card.title {
      card.title = "[modified] \(title)"
    }
    if let description = card.description {
      card.description = "[modified] \(description)"
    }
    return card
  }
}

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

完全な例については、[サンプルアプリの例](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift)を確認してください。

{% endsubtab %}
{% subtab Objective-C %}

`Attributes`によるコンテンツカードのカスタマイズは、OBJECTIVE-C ではサポートされていません。

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## カスタマイズの例

### カスタムフォント

コンテンツカードで使用されるフォントをカスタマイズすると、ブランドアイデンティティを維持し、ユーザーにとって視覚的に魅力的なエクスペリエンスを作成できます。これらのレシピを使用して、すべてのコンテンツカードのフォントをプログラムで設定します。 

{% tabs %}
{% tab web %}

他の Web 要素と同様に、CSS を使用してコンテンツカードの外観を簡単にカスタマイズできます。CSS ファイルまたはインラインスタイルで、`font-family`プロパティを使用して、希望のフォント名またはフォントスタックを指定します。

```css
/* CSS selector targeting the Content Card element */
.card-element {
  font-family: "Helvetica Neue", Arial, sans-serif;
}
```

{% endtab %}
{% tab android %}

デフォルトのフォントをプログラムで変更するには、カードのスタイルを設定し、`fontFamily`属性を使用して、カスタムフォントファミリを使用するように Braze に指示します。

たとえば、キャプション付き画像カードのすべてのタイトルのフォントを更新するには、`Braze.ContentCards.CaptionedImage.Title`スタイルを設定し、カスタムフォントファミリを参照します。属性値は、`res/font`ディレクトリのフォントファミリを指す必要があります。

以下は、最後の行でカスタムフォントファミリ `my_custom_font_family` が参照されている部分的なコード例です。

```xml
  <style name="Braze.ContentCards.CaptionedImage.Title">
    <item name="android:layout_width">wrap_content</item>
    ...
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

Android SDK でのフォントのカスタマイズの詳細については、[フォントファミリガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization)を参照してください。
{% endtab %}
{% tab Jetpack Compose %}
デフォルトのフォントをプログラムで変更するには、`ContentCardStyling` の[`titleTextStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#715371549%2FProperties%2F-1725759721) を設定します。

また、[`BrazeShortNewsContentCardStyling`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-braze-short-news-content-card-styling/index.html)に設定し、[](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#8580250%2FProperties%2F-1725759721)`shortNewsContentCardStyle`の[`shortNewsContentCardStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#8580250%2FProperties%2F-1725759721)に渡すことで、特定のカードタイプに`titleTextStyle`を設定することもできます。

```kotlin
val fontFamily = FontFamily(
    Font(R.font.sailec_bold)
)

ContentCardStyling(
    titleTextStyle = TextStyle(
        fontFamily = fontFamily
    )
)
```
{% endtab %}
{% tab swift %}
{% subtabs %}
{% subtab Swift %}

[`cellAttributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cellattributes/)インスタンスプロパティの`Attributes`をカスタマイズして、フォントをカスタマイズします。以下に例を示します。

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.titleFont = .preferredFont(textStyle: .callout, weight: .bold)
attributes.cellAttributes.descriptionFont = .preferredFont(textStyle: .footnote, weight: .regular)
attributes.cellAttributes.domainFont = .preferredFont(textStyle: .footnote, weight: .medium)

let viewController = BrazeContentCardUI.ViewController.init(braze: braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

`Attributes`によるフォントのカスタマイズは、OBJECTIVE-C ではサポートされていません。 

カスタムフォントを使用して独自の UI を構築する例については、[サンプルアプリの例](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/ObjC/Sources/ContentCards-Custom-UI/CardsInfoViewController.m#L97)を確認してください。

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### カスタムの固定アイコン

コンテンツカードの作成時、マーケターはカードを固定するオプションを選択できます。ピン留めされたカードはユーザーのフィードの上部に表示され、ユーザーが閉じることはできません。カードスタイルをカスタマイズすると、固定されたアイコンの外観を変更できます。

![Braze for MobileとBraze for Webのコンテンツカードプレビューを、「このカードをフィードの先頭にピン留めする」オプションを選択した状態で並べてみた。]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

{% tabs %}
{% tab web %}

コンテンツカードの固定アイコンの構造は次のとおりです。

```css
<div class="ab-pinned-indicator">
  <i class="fa fa-star"></i>
</div>
```

別の FontAwesome アイコンを使用する場合は、`i`要素のクラス名を目的のアイコンのクラス名に置き換えるだけです。  

アイコンを全体的に交換したい場合は、`i`要素を削除し、カスタムアイコンを`ab-pinned-indicator`の子として追加します。いくつかの方法がありますが、簡単な方法の1つは`ab-pinned-indicator`要素の`replaceChildren()`です。

以下に例を示します。

```javascript
// Get the parent element
const pinnedIndicator = document.querySelector('.ab-pinned-indicator');

// Create a new custom icon element
const customIcon = document.createElement('span');
customIcon.classList.add('customIcon');

// Replace the existing icon with the custom icon
pinnedIndicator.replaceChildren(customIcon);
```

{% endtab %}
{% tab android %}

カスタムの固定アイコンを設定するには、`Braze.ContentCards.PinnedIcon`スタイルを上書きします。カスタム画像アセットは、`android:src`要素で宣言される必要があります。以下に例を示します。

```xml
  <style name="Braze.ContentCards.PinnedIcon">
    <item name="android:src">@drawable/{my_custom_image_here}</item>

    <item name="android:layout_width">wrap_content</item>
    <item name="android:layout_height">wrap_content</item>
    <item name="android:layout_alignParentRight">true</item>
    <item name="android:layout_alignParentTop">true</item>
    <item name="android:contentDescription">@null</item>
    <item name="android:importantForAccessibility">no</item>
  </style>
```

{% endtab %}
{% tab Jetpack Compose %}

デフォルトの固定アイコンを変更するには、`ContentCardStyling`の[`pinnedResourceId`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#794044424%2FProperties%2F-1725759721)を設定します。 以下に例を示します。

```kotlin
ContentCardStyling(
    pinnedResourceId = R.drawable.pushpin,
    pinnedImageAlignment = Alignment.TopCenter
)
```

`ContentCardStyling`の[`pinnedComposable`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#1460938052%2FProperties%2F-1725759721)にComposableを指定することもできます。`pinnedComposable`が指定されている場合は、`pinnedResourceId`の値が上書きされます。

```kotlin
ContentCardStyling(
    pinnedComposable = {
        Box(Modifier.fillMaxWidth()) {
            Text(
                modifier = Modifier
                    .align(Alignment.Center)
                    .width(50.dp),
                text = "This message is not read. Please read it."
            )
        }
    }
)
```
{% endtab %}
{% tab swift %}
{% subtabs %}
{% subtab Swift %}

固定アイコンをカスタマイズするには、[`cellAttributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cellattributes/)インスタンスプロパティの`pinIndicatorColor`と`pinIndicatorImage`のプロパティを変更します。以下に例を示します。

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.pinIndicatorColor = .red
attributes.cellAttributes.pinIndicatorImage = UIImage(named: "my-image")

let viewController = BrazeContentCardUI.ViewController.init(braze: braze, attributes: attributes)
```

サブクラス化を使用して、`BrazeContentCardUI.Cell`のカスタムバージョンを独自に作成することもできます。 これにはピンインジケーターが含まれます。以下に例を示します。 

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cells[BrazeContentCardUI.ClassicImageCell.identifier] = CustomClassicImageCell.self

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

`Attributes`によるピンインジケーターのカスタマイズは、OBJECTIVE-C ではサポートされていません。

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### 未読インジケーターの色の変更

コンテンツカードの下部には、カードが閲覧されたかどうかを示す青い線が表示されます。 

![2枚のコンテンツ・カードが並んで表示される。最初のカードの下部には青い線があり、それがまだ見られていないことを示している。2番目のカードには青い線がなく、すでに見られたことを示している。]({% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %})

{% tabs %}
{% tab web %}

カードの未読インジケーターの色を変更するには、Web ページにカスタム CSS を追加します。たとえば、未表示のインジケーターの色を緑に設定するには、次のようにします。

```css
.ab-unread-indicator { background-color: green; }
```

{% endtab %}
{% tab android %}

未読インジケーターバーの色を変更するには、`colors.xml`ファイルの`com_braze_content_cards_unread_bar_color`の値を変更します。 

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <!-- The color used to highlight unread Content Cards at their bottom edge -->
  <color name="com_braze_content_cards_unread_bar_color">#1676d0</color>
</resources>
```

{% endtab %}
{% tab Jetpack Compose %}

未読インジケータバーの色を変更するには、`ContentCardStyling` の[`unreadIndicatorColor`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#-1669590042%2FProperties%2F-1725759721) の値を変更します。

```kotlin
ContentCardStyling(
    unreadIndicatorColor = Color.Red
)
```

{% endtab %}
{% tab swift %}

{% subtabs %}
{% subtab Swift %}

未読インジケーターバーの色を変更するには、`BrazeContentCardUI.ViewController`インスタンスの色合いに値を割り当てます。

```swift
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze)
viewController.view.tintColor = .systemGreen
```

ただし、未表示のインジケーターのみを変更したい場合は、`BrazeContentCardUI.ViewController.Attributes`構造体の`unviewedIndicatorColor`プロパティにアクセスします。Braze`UITableViewCell` の実装を使用する場合は、セルが描画される前にプロパティにアクセスする必要がある。

たとえば、未閲覧インジケーターの色を赤に設定するには、次のようにします。

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.unviewedIndicatorColor = .red

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

完全な例については、[サンプルアプリの例](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift)を確認してください。

{% endsubtab %}
{% subtab Objective-C %}

未読インジケーターバーの色を変更するには、`BRZContentCardUIViewController`の色合いに値を割り当てます。

```objc
BRZContentCardUIViewController *viewController = [[BRZContentCardUIViewController alloc] initWithBraze:AppDelegate.braze];
[viewController.view setTintColor:[UIColor systemGreenColor]];
```

`Attributes`による未表示インジケーターのみのカスタマイズは、OBJECTIVE-C ではサポートされていません。

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### 未読インジケーターを無効にする

{% tabs %}
{% tab web %}

未読インジケーターバーを非表示にするには、`css`に次のスタイルを追加します。

```css
.ab-unread-indicator { display: none; }
```

{% endtab %}

{% tab android %}

未読インジケーターバーを非表示にするには、`ContentCardViewHolder`の[`setUnreadBarVisible`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.view/-content-card-view-holder/set-unread-bar-visible.html?query=fun%20setUnreadBarVisible(isVisible:%20Boolean))を`false`に設定します。 

{% endtab %}

{% tab Jetpack Compose %}
未読インジケーターの無効化は、Jetpack Compose ではサポートされていません。
{% endtab %}
{% tab swift %}
{% subtabs %}
{% subtab Swift %}

未読インジケーターバーを非表示にするには、`Attributes`構造体の`attributes.cellAttributes.unviewedIndicatorColor`プロパティを`.clear`に設定します。 

{% endsubtab %}
{% subtab Objective-C %}

`Attributes`による未表示インジケーターのみのカスタマイズは、OBJECTIVE-C ではサポートされていません。

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}
