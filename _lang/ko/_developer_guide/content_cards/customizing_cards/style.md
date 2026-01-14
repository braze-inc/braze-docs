---
nav_title: 서식
article_title: 콘텐츠 카드 스타일 사용자 지정
page_order: 1
description: "이 문서에서는 콘텐츠 카드의 스타일 지정 옵션을 다룹니다."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# 콘텐츠 카드 스타일 사용자 지정

> Braze 콘텐츠 카드에는 기본 모양과 느낌이 제공됩니다. 이 문서에서는 브랜드 정체성에 맞는 콘텐츠 카드의 스타일 옵션을 다룹니다. 콘텐츠 카드 유형 전체 목록은 [콘텐츠 카드 정보를]({{site.baseurl}}/developer_guide/content_cards/) 참조하세요.

## 사용자 지정 스타일 만들기

기본 콘텐츠 카드 UI는 Braze SDK의 UI 레이어에서 가져옵니다. 여기에서 카드의 스타일, 카드가 표시되는 순서, 사용자에게 피드가 표시되는 방식 등 특정 부분을 조정할 수 있습니다.

![두 개의 콘텐츠 카드, 하나는 기본값 글꼴과 직각 모서리를 가지고 있고, 다른 하나는 둥근 모서리와 곱슬 글꼴을 가지고 있다]({% image_buster/assets/img/content_cards/content-card-customization-attributes.png %})

{% alert note %}
`title`, `cardDescription`, `imageUrl` 등과 같은 콘텐츠 카드 속성정보는 [대시보드]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details)를 통해 직접 편집할 수 있으며, 이러한 세부 정보를 변경하는 데 가장 선호되는 방법입니다.
{% endalert %}


{% tabs %}
{% tab Android %}

기본적으로 Android 및 FireOS SDK 콘텐츠 카드는 표준 Android UI 지침과 일치하여 원활한 경험을 제공합니다. 이러한 기본 스타일은 Braze SDK 배포의 [`res/values/styles.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml) 파일에서 확인할 수 있습니다:

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

콘텐츠 카드 스타일을 사용자 정의하려면 이 기본 스타일을 덮어씁니다. 스타일을 재정의하려면 프로젝트의 `styles.xml` 파일에 전체 스타일을 복사한 후 수정합니다. 모든 속성을 올바르게 설정하려면 전체 스타일을 로컬 `styles.xml` 파일에 복사해야 합니다.

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

기본적으로 Android 및 FireOS SDK 콘텐츠 카드는 표준 Android UI 지침과 일치하여 원활한 경험을 제공합니다.

두 가지 방법 중 하나로 스타일링을 적용할 수 있습니다. 첫 번째 방법은, 다음 예제와 같이 `ContentCardListStyling` 및 `ContentCardStyling`을 `ContentCardsList()`로 전달하는 것입니다.

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

두 번째는 다음 예시와 같이 BrazeStyle을 사용하여 Braze 컴포넌트에 대한 글로벌 스타일링을 만드는 것입니다:

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
{% tab iOS %}

콘텐츠 카드 보기 컨트롤러를 사용하면 [`BrazeContentCardUI.ViewController.Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct) 구조를 통해 모든 셀의 모양과 동작을 사용자 지정할 수 있습니다. `Attributes`를 사용하여 콘텐츠 카드를 구성하는 방법이 가장 쉽습니다. 이 경우 최소한의 설정으로 콘텐츠 카드 UI를 시작할 수 있습니다. 

{% alert important %}
`Attributes` 을 통한 사용자 지정은 Swift에서만 가능합니다.
{% endalert %}

{% subtabs %}
{% subtab Swift %}

**`Attributes.default` 수정**

정적 [`Attributes.defaults`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults) 변수를 직접 수정하여 Braze 콘텐츠 카드 UI 보기 컨트롤러에 대한 모든 인스턴스의 모양과 느낌을 사용자 지정합니다.

예를 들어 모든 셀의 기본 이미지 크기와 모서리 반경을 변경하려면 다음을 수행합니다.

```swift
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.cornerRadius = 20
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.classicImageSize = CGSize(width: 65, height: 65)
```

**속성을 사용하여 보기 컨트롤러 초기화**

Braze 콘텐츠 카드 UI 뷰 컨트롤러의 특정 인스턴스만 수정하려는 경우에는 [`init(braze:attributes:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/init(braze:attributes:)/) 이니셜라이저를 사용하여 사용자 정의 `Attributes` 구조체를 뷰 컨트롤러에 전달하세요.

예를 들어 뷰 컨트롤러의 특정 인스턴스에 대한 이미지 크기와 모서리 반경을 변경할 수 있습니다:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.cornerRadius = 20
attributes.cellAttributes.classicImageSize = CGSize(width: 65, height: 65)

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

**서브클래스로 설정하여 셀 사용자 지정**

또는 원하는 각 카드 유형에 대한 사용자 지정 클래스를 등록하여 사용자 지정 인터페이스를 만들 수도 있습니다. 기본 셀 대신 서브클래스를 사용하려면 `Attributes` 구조의 [`cells`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cells) 속성정보를 수정합니다. 예를 들어, 다음과 같습니다.

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
// Register your own custom cell
attributes.cells[BrazeContentCardUI.ClassicImageCell.identifier] = CustomClassicImageCell.self

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

**프로그래밍 방식으로 콘텐츠 카드 수정하기**

콘텐츠 카드는 프로그래밍 방식으로 [`transform`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/transform) 클로저를 `Attributes` 구조에 할당하여 변경할 수 있습니다. 아래 예제에서는 호환되는 카드의 `title` 및 `description`을 수정합니다.

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

전체 예제는 [예제 샘플 앱에서](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift) 확인하세요.

{% endsubtab %}
{% subtab Objective-C %}

`Attributes`를 통한 콘텐츠 카드 사용자 지정은 Objective-C에서 지원되지 않습니다.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab 웹 %}

Braze의 기본 스타일은 Braze SDK 내 CSS에서 정의됩니다. 애플리케이션에서 선택한 스타일을 재정의하여 나만의 배경 이미지, 글꼴 모음, 스타일, 크기, 애니메이션 등으로 표준 피드를 맞춤 설정할 수 있습니다. 예를 들어, 다음은 콘텐츠 카드를 800px 너비로 표시하는 재정의 예제입니다.

``` css
body .ab-feed {
  width: 800px;
}
```

{% endtab %}
{% endtabs %}

## 사용자 지정 예제

### 사용자 지정 글꼴

콘텐츠 카드에 사용되는 글꼴을 사용자 지정하면 브랜드 아이덴티티를 유지하고 사용자에게 시각적으로 매력적인 경험을 제공할 수 있습니다. 이 레시피를 사용하여 모든 콘텐츠 카드의 글꼴을 프로그래밍 방식으로 설정할 수 있습니다. 

{% tabs %}
{% tab Android %}

프로그래밍 방식으로 기본 글꼴을 변경하려면 카드의 스타일을 설정하고 `fontFamily` 속성을 사용하여 사용자 지정 글꼴 패밀리를 사용하도록 Braze에 지시하세요.

예를 들어 자막 이미지 카드의 모든 제목에서 글꼴을 업데이트하려면 `Braze.ContentCards.CaptionedImage.Title` 스타일을 재정의하고 커스텀 글꼴 패밀리를 참조합니다. 속성 값은 `res/font` 디렉터리에 있는 글꼴 패밀리를 가리켜야 합니다.

다음은 마지막 줄에 참조된 사용자 정의 글꼴 모음( `my_custom_font_family`)을 사용한 잘린 예제입니다:

```xml
  <style name="Braze.ContentCards.CaptionedImage.Title">
    <item name="android:layout_width">wrap_content</item>
    ...
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

Android SDK의 글꼴 사용자 지정에 대한 자세한 내용은 [글꼴 패밀리 가이드]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization)를 참조하세요.
{% endtab %}
{% tab Jetpack Compose %}
기본 글꼴을 프로그래밍 방식으로 변경하려면 `ContentCardStyling`의 `titleTextStyle`을 설정하면 됩니다.

특정 카드 유형에 대해 `BrazeShortNewsContentCardStyling`에서 설정하고 `ContentCardStyling`의 `shortNewsContentCardStyle`에 전달함으로써 `titleTextStyle`을 설정할 수도 있습니다.

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
{% tab iOS %}
{% subtabs %}
{% subtab Swift %}

[`cellAttributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cellattributes/) 인스턴스 속성정보의 `Attributes`를 사용자 지정하여 글꼴을 사용자 지정합니다. 예를 들어, 다음과 같습니다.

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.titleFont = .preferredFont(textStyle: .callout, weight: .bold)
attributes.cellAttributes.descriptionFont = .preferredFont(textStyle: .footnote, weight: .regular)
attributes.cellAttributes.domainFont = .preferredFont(textStyle: .footnote, weight: .medium)

let viewController = BrazeContentCardUI.ViewController.init(braze: braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

`Attributes` 을 통한 글꼴 사용자 지정은 Objective-C에서 지원되지 않습니다. 

[예제 샘플 앱](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/ObjC/Sources/ContentCards-Custom-UI/CardsInfoViewController.m#L97)에서 사용자 지정 글꼴로 나만의 UI를 빌드하는 예제를 확인하세요.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab 웹 %}

다른 웹 요소와 마찬가지로 CSS를 통해 콘텐츠 카드의 모양을 쉽게 사용자 지정할 수 있습니다. CSS 파일 또는 인라인 스타일에서 `font-family` 속성을 사용하여 원하는 글꼴 이름 또는 글꼴 스택을 지정합니다.

```css
/* CSS selector targeting the Content Card element */
.card-element {
  font-family: "Helvetica Neue", Arial, sans-serif;
}
```

{% endtab %}
{% endtabs %}

### 사용자 지정 고정 아이콘

콘텐츠 카드를 만들 때 마케팅 담당자는 카드를 고정할 수 있습니다. 고정 카드는 사용자의 피드 상단에 표시되며 사용자가 지울 수 없습니다. 카드 스타일을 사용자 지정할 때 고정된 아이콘의 모양을 변경할 수 있습니다.

![모바일 및 웹용 Braze의 콘텐츠 카드 미리보기 나란히, "이 카드를 피드 상단에 고정" 옵션이 선택되었습니다.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

{% tabs %}
{% tab Android %}

커스텀 고정 아이콘을 설정하려면 `Braze.ContentCards.PinnedIcon` 스타일을 재정의합니다. 사용자 정의 이미지 자산은 `android:src` 요소에 선언해야 합니다. 예를 들어, 다음과 같습니다.

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

기본 고정 아이콘을 변경하려면 `ContentCardStyling`의 `pinnedResourceId`를 설정하면 됩니다.  예를 들어, 다음과 같습니다.

```kotlin
ContentCardStyling(
    pinnedResourceId = R.drawable.pushpin,
    pinnedImageAlignment = Alignment.TopCenter
)
```

`ContentCardStyling`의 `pinnedComposable`에서 Composable을 지정할 수도 있습니다. `pinnedComposable`을 지정하면 `pinnedResourceId` 값을 재정의합니다.

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
{% tab iOS %}
{% subtabs %}
{% subtab Swift %}

[`cellAttributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cellattributes/) 인스턴스 속성정보의 `pinIndicatorColor` 및 `pinIndicatorImage` 속성정보를 수정하여 고정 아이콘을 사용자 지정합니다. 예를 들어, 다음과 같습니다.

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.pinIndicatorColor = .red
attributes.cellAttributes.pinIndicatorImage = UIImage(named: "my-image")

let viewController = BrazeContentCardUI.ViewController.init(braze: braze, attributes: attributes)
```

하위 클래싱을 사용하여 핀 표시기가 포함된 `BrazeContentCardUI.Cell` 의 사용자 지정 버전을 만들 수도 있습니다. 예를 들어, 다음과 같습니다. 

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cells[BrazeContentCardUI.ClassicImageCell.identifier] = CustomClassicImageCell.self

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

`Attributes` 을 통한 핀 표시기 사용자 지정은 Objective-C에서 지원되지 않습니다.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab 웹 %}

콘텐츠 카드 고정 아이콘의 구조는 다음과 같습니다:

```css
<div class="ab-pinned-indicator">
  <i class="fa fa-star"></i>
</div>
```

다른 FontAwesome 아이콘을 사용하려면 `i` 요소의 클래스 이름을 원하는 아이콘의 클래스 이름으로 바꾸면 됩니다. 

아이콘을 완전히 바꾸려면 `i` 요소를 제거하고 커스텀 아이콘을 `ab-pinned-indicator`의 하위 항목으로 추가합니다. 몇 가지 방법이 있지만 간단한 한 가지 방법은 `ab-pinned-indicator` 요소에서 `replaceChildren()`을 사용하는 것입니다.

예를 들어, 다음과 같습니다.

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
{% endtabs %}

### 읽지 않은 표시기 색상 변경하기

콘텐츠 카드에서 카드 하단에는 카드 열람 여부를 나타내는 파란색 선이 표시됩니다. 

![두 개의 콘텐츠 카드가 나란히 표시됩니다. 첫 번째 카드에서 하단에 파란색 선이 있고 이는 열람하지 않았음을 나타냅니다. 두 번째 카드는 파란색 선이 없으며, 이미 보았음을 나타냅니다.]({% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %})

{% tabs %}
{% tab Android %}

`colors.xml` 파일의 `com_braze_content_cards_unread_bar_color` 값을 변경하여 읽지 않은 표시줄의 색상을 변경합니다:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <!-- The color used to highlight unread Content Cards at their bottom edge -->
  <color name="com_braze_content_cards_unread_bar_color">#1676d0</color>
</resources>
```

{% endtab %}
{% tab Jetpack Compose %}

읽지 않음 표시줄의 색상을 변경하려면 `ContentCardStyling` 에서 `unreadIndicatorColor` 의 값을 수정합니다:

```kotlin
ContentCardStyling(
    unreadIndicatorColor = Color.Red
)
```

{% endtab %}
{% tab iOS %}

{% subtabs %}
{% subtab Swift %}

`BrazeContentCardUI.ViewController` 인스턴스의 색조 색상에 값을 지정하여 읽지 않은 표시줄의 색상을 변경합니다:

```swift
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze)
viewController.view.tintColor = .systemGreen
```

그러나 미열람 표시기만 수정하려면 `BrazeContentCardUI.ViewController.Attributes` 구조의 `unviewedIndicatorColor` 속성정보에 액세스하면 됩니다. Braze `UITableViewCell` 구현을 사용하는 경우 셀을 그리기 전에 속성정보에 액세스해야 합니다.

예를 들어, 보지 않은 표시기의 색상을 빨간색으로 설정합니다:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.unviewedIndicatorColor = .red

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

전체 예제는 [예제 샘플 앱에서](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift) 확인하세요.

{% endsubtab %}
{% subtab Objective-C %}

`BRZContentCardUIViewController` 의 색조 색상에 값을 지정하여 읽지 않은 표시줄의 색상을 변경합니다:

```objc
BRZContentCardUIViewController *viewController = [[BRZContentCardUIViewController alloc] initWithBraze:AppDelegate.braze];
[viewController.view setTintColor:[UIColor systemGreenColor]];
```

`Attributes`를 통해 미열람 표시기만 사용자 지정하는 기능은 Objective-C에서 지원되지 않습니다.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab 웹 %}

카드의 읽지 않음 표시기의 색상을 변경하려면 웹 페이지에 사용자 지정 CSS를 추가하세요. 예를 들어, 보지 않은 표시기의 색상을 녹색으로 설정합니다:

```css
.ab-unread-indicator { background-color: green; }
```

{% endtab %}
{% endtabs %}

### 읽지 않은 표시기 비활성화하기

{% tabs %}
{% tab Android %}

`ContentCardViewHolder`에서 [`setUnreadBarVisible`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.view/-content-card-view-holder/set-unread-bar-visible.html?query=fun%20setUnreadBarVisible(isVisible:%20Boolean))을 `false`로 설정하여 미열람 표시기를 숨깁니다. 

{% endtab %}

{% tab Jetpack Compose %}
미열람 표시기를 비활성화하는 기능은 Jetpack Compose에서 지원되지 않습니다.
{% endtab %}

{% tab iOS %}
{% subtabs %}
{% subtab Swift %}

`Attributes` 구조의 `attributes.cellAttributes.unviewedIndicatorColor` 속성을 `.clear` 로 설정하여 읽지 않은 표시줄을 숨깁니다. 

{% endsubtab %}
{% subtab Objective-C %}

`Attributes`를 통해 미열람 표시기만 사용자 지정하는 기능은 Objective-C에서 지원되지 않습니다.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab 웹 %}

`css` 에 다음 스타일을 추가하여 읽지 않은 표시줄을 숨기면 됩니다:

```css
.ab-unread-indicator { display: none; }
```

{% endtab %}
{% endtabs %}
