---
nav_title: 高度な実装（オプション）
article_title: iOS 用アプリ内メッセージ実装ガイド (オプション)
platform: iOS
page_order: 6
description: "この高度な実装ガイドでは、iOS のアプリ内メッセージコードに関する考慮事項、私たちのチームが構築した3つのユースケース、および付属のコードスニペットについて説明しています。"
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

<br>
{% alert important %}
基本的なアプリ内メッセージ開発者統合ガイドをお探しですか?見つける [here]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/overview/).
{% endalert %}

# アプリ内メッセージング実装ガイド

> このオプションの高度な実装ガイドでは、アプリ内メッセージコードに関する考慮事項、当社のチームが構築した3つのカスタムユースケース、および付属のコードスニペットについて説明します。[こちらから](https://github.com/braze-inc/braze-growth-shares-ios-demo-app)Braze Demo リポジトリにアクセスしてください！この実装ガイドは Swift の実装を中心としていますが、興味のある人のために Objective-C のスニペットが提供されています。HTML の実装をお探しですか?Braze の[HTML テンプレートリポジトリ](https://github.com/braze-inc/in-app-message-templates)をご確認ください。

## コードに関する考慮事項

次のガイドでは、デフォルトのアプリ内メッセージに加えて使用する、オプションのカスタムデベロッパーインテグレーションについて説明します。各ユースケースにはカスタムビューコントローラーが含まれており、機能を拡張したり、アプリ内メッセージの外観をネイティブにカスタマイズしたりするためのサンプルが用意されています。

### ABKInAppMessage サブクラス

次のコードスニペットは Braze SDK の UI デリゲートメソッドで、アプリ内メッセージに入力するサブクラスビューを決定します。このガイドでは基本的な実装について説明し、フルサブクラス、スライドアップサブクラス、モーダルサブクラスを魅力的な方法で実装する方法を示します。カスタムビューコントローラーを設定する場合は、他のすべてのアプリ内メッセージサブクラスを設定する必要があることに注意してください。サブクラス化の背後にある概念をしっかりと理解したら、[ユースケース](#sample-use-cases)を確認してアプリ内メッセージングサブクラスの実装を開始してください。

{% tabs %}
{% tab Swift %}
**ABKInAppMessage サブクラス**<br>

```swift
extension AppboyManager: ABKInAppMessageUIDelegate {
  func inAppMessageViewControllerWith(_ inAppMessage: ABKInAppMessage) -> ABKInAppMessageViewController {
    switch inAppMessage {
    case is ABKInAppMessageSlideup:
      return slideupViewController(inAppMessage: inAppMessage) //Custom Method
    case is ABKInAppMessageModal: 
      return modalViewController(inAppMessage: inAppMessage) //Custom Method
    case is ABKInAppMessageFull:
      return fullViewController(inAppMessage: inAppMessage) //Custom Method
    case is ABKInAppMessageHTML:
      return ABKInAppMessageHTMLViewController(inAppMessage: inAppMessage)
    default:
      return ABKInAppMessageViewController(inAppMessage: inAppMessage)
    }
  }
}
```
{% endtab %}
{% tab Objective-C %}
**ABKInAppMessage サブクラス**<br> 

```objc
- (ABKInAppMessageViewController *)inAppMessageViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage {
  if ([inAppMessage isKindOfClass:[ABKInAppMessageSlideup class]]) {
    return [self slideupViewControllerWithInAppMessage:inAppMessage]; //Custom Method
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageModal class]]) {
    return [self modalViewControllerWithInAppMessage:inAppMessage]; //Custom Method
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageFull class]]) {
    return [self fullViewControllerWithInAppMessage:inAppMessage]; //Custom Method
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageHTML class]]) {
    return [[ABKInAppMessageHTMLViewController alloc] initWithInAppMessage:inAppMessage];
  } else {
    return [[ABKInAppMessageViewController alloc] initWithInAppMessage:inAppMessage];
  }
}
```
{% endtab %}
{% endtabs %}

## ユースケース

以下の3つのユースケースを提供しました。それぞれのユースケースには、詳細な説明、関連するコードスニペット、アプリ内メッセージが Braze ダッシュボードでどのように表示され、どのように使用されるかが記載されています。
- [カスタムスライドアップアプリ内メッセージ](#custom-slide-up-in-app-message)
- [カスタムモーダルアプリ内メッセージ](#custom-modal-in-app-message)
- [カスタムフルアプリ内メッセージ](#custom-full-in-app-message)

### カスタムスライドアップアプリ内メッセージ

![2台のiPhoneを並べて。最初の iPhone では、スライドアップメッセージが画面の下部に表示されます。2台目の iPhone では、スライドアップメッセージが画面の上方に表示され、アプリのナビゲーションボタンが表示されています。]({% image_buster /assets/img/iam_implementation/slideup.png %}){: style="float:right;max-width:45%;margin-left:15px;border:0;"}

スライドアップのアプリ内メッセージを作成しているときに、デフォルトの方法ではメッセージの配置を変更できないことに気付くかもしれません。このような変更は、`ABKInAppMessageSlideupViewController` をサブクラス化し、独自のカスタム変数で `offset` 変数をオーバーライドすることによって可能になります。右の画像は、これを使用してスライドアップアプリ内メッセージを調整する方法の例を示しています。 

開始するには、[`SlideFromBottomViewController`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/SlideFromBottomViewController.swift) にアクセスしてください。

#### デフォルト UI への動作の追加<br><br>

{% tabs %}
{% tab Swift %}
**`offset` 変数を更新**<br>
`offset` 変数を更新し、必要に応じて独自のオフセットを設定します。
```swift
func setSlideConstraint() {
  offset = 0
}
```

```swift
override var offset: CGFloat {
  get {
    return super.offset
  }
  set {
    super.offset = newValue + adjustedOffset
  }
}
```

{% details Version 3.34.0 or earlier  %}
**`slideConstraint` 変数を更新**<br>
`slideConstraint` パブリック変数はスーパークラス `ABKInAppMessageSlideupViewController` から取得されます。 

```swift
func setSlideConstraint() {
    slideConstraint?.constant = bottomSpacing
}
```

```swift
private var bottomSpacing: CGFloat {
    return AppboyManager.shared.activeApplicationViewController.topMostViewController().view.safeAreaInsets.bottom
}
``` 
[`topMostViewController()`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/Utils/UIViewController_Util.swift#L17) 機能については、Braze Demo リポジトリにアクセスしてください。
{% enddetails %}
{% endtab %}
{% tab Objective-C %}
**`offset` 変数を更新**<br>
`offset` 変数を更新し、必要に応じて独自のオフセットを設定します。
```objc
- (void)setOffset {
  self.offset = 0;
}
```

```objc
- (CGFloat)offset {
  return [super offset];
}
 
- (void)setOffset:(CGFloat)offset {
  [super setOffset:offset + [self adjustedOffset]];
}
```
{% details Version 3.34.0 or earlier  %}
**`slideConstraint` 変数を更新**<br>
`slideConstraint` パブリック変数はスーパークラス `ABKInAppMessageSlideupViewController` から取得されます。 

```objc
- (void)self.setSlideConstraint:(NSLayoutConstraint *)slideConstraint {
  slideConstraint.constant = bottomSpacing;
}
```

```objc
- (CGFloat)bottomSpacing {
  return [AppboyManager shared].activeApplicationViewController.topMostViewController.view.safeAreaInsets.bottom;
}
```
{% enddetails %}
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
**カスタム制約のオーバーライドと設定**<br>
`beforeMoveInAppMessageViewOnScreen()` をオーバーライドし、必要に応じて独自のカスタム制約値を設定します。元の値はスーパークラスに設定されます。

```swift
override func beforeMoveInAppMessageViewOnScreen() {
  super.beforeMoveInAppMessageViewOnScreen()
  setOffset()
}
```

{% details Version 3.34.0 or earlier %}
```swift
override func beforeMoveInAppMessageViewOnScreen() {
  setSlideConstraint()
}
```
{% enddetails %}

{% endtab %}
{% tab Objective-C %}
**カスタム制約のオーバーライドと設定**<br> 
`beforeMoveInAppMessageViewOnScreen()` をオーバーライドし、必要に応じて独自のカスタム制約値を設定します。元の値はスーパークラスに設定されます。

```objc
- (void)beforeMoveInAppMessageViewOnScreen {
  [super beforeMoveInAppMessageViewOnScreen];
  [self setOffset];
}
```

{% details Version 3.34.0 or earlier  %}
```objc
- (void)beforeMoveInAppMessageViewOnScreen {
  [self setSlideConstraint:self.slideConstraint];
}
```
{% enddetails %}
{% endtab %}
{% endtabs %}

**デバイスの向きの制約を調整**<br>
サブクラスはレイアウト変更中に制約の同期を維持する責任を負うため、`viewWillTransition()` 内のそれぞれの値を調整します。

### カスタムモーダルアプリ内メッセージ

![スポーツチームの一覧を循環させ、好きなチームを選択できるモーダル アプリ内メッセージが表示されたiPhone。このアプリ内メッセージの下部には、大きな青い送信ボタンがあります。]({% image_buster /assets/img/iam_implementation/modal.png %}){: style="float:right;max-width:23%;margin-left:15px;border:0;"}

`ABKInAppMessageModalViewController` をサブクラス化して、貴重なユーザー属性を収集する魅力的な方法を提供する `UIPickerView` を活用できます。カスタムモーダルアプリ内メッセージを使用すると、コネクテッドコンテンツまたは使用可能なリストを使用して、アイテムの動的なリストから属性を表示およびキャプチャできます。 

サブクラス化されたアプリ内メッセージに独自のビューを挿入できます。この例では、`UIPickerView` を使用して `ABKModalInAppMessageViewController` の機能を拡張する方法を示しています。

開始するには、[ModalPickerViewController](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/ModalPickerViewController/ModalPickerViewController.swift) にアクセスしてください。

#### ダッシュボード設定

ダッシュボードでモーダルアプリ内メッセージを設定するには、コンマ区切り文字列として書式設定された項目のリストを指定する必要があります。この例では、コネクテッドコンテンツを使用してチーム名の JSON リストを取得し、それに応じてフォーマットします。

![in-アプリ メッセージ作成画面には、アプリ内メッセージの外観のプレビューが表示されますが、代わりにBrazeに指定したアイテムの一覧が表示されます。スマートフォンに送信されない限り、Braze UI にはカスタムアプリ内メッセージ UI が表示されないため、プレビューではメッセージがどのように表示されるかを示すものではないので、送信前にテストすることをお勧めします。]({% image_buster /assets/img/iam_implementation/dashboard1.png %})

キーと値のペアに `attribute_key` を入力します。このキーは、ユーザーが選択した値とともに、カスタム属性としてユーザープロファイルに保存されます。カスタムビューロジックは、Braze に送信されたユーザー属性を処理する必要があります。

`ABKInAppMessage` オブジェクト内の `extras` ディクショナリを使用して、表示すべき正しいビューを示す `view_type` キー (存在する場合) をクエリできます。アプリ内メッセージはメッセージごとに設定されるため、カスタムとデフォルトのモーダルビューが調和して機能することに注意してください。

![メッセージ作成画面で検出された2 つのキーと値のペア。最初のキーと値のペアには、"attribute_key" "Favorite Team "が設定され、2番目には"view_type" "picker "が設定されている。]({% image_buster /assets/img/iam_implementation/dashboard2.png %}){: style="max-width:65%;"}

{% tabs %}
{% tab Swift %}
**UI 表示動作に `view_type` を使用**<br>
`view_type` に対して `extras` ディクショナリを照会して、目的のサブクラス化されたビューコントローラをロードします。

```swift
func modalViewController(inAppMessage: ABKInAppMessage) -> ABKInAppMessageModalViewController {
  switch inAppMessage.extras?[InAppMessageKey.viewType.rawValue] as? String {
  case InAppMessageViewType.picker.rawValue:
    return ModalPickerViewController(inAppMessage: inAppMessage)
  default:
    return ABKInAppMessageModalViewController(inAppMessage: inAppMessage)
  }
}
```
{% endtab %}
{% tab Objective-C %}
**UI 表示動作に `view_type` を使用**<br>
`view_type` に対して `extras` ディクショナリを照会して、目的のサブクラス化されたビューコントローラをロードします。

```objc
- (ABKInAppMessageModalViewController *)modalViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage {
  InAppMessageData *inAppMessageData = [[InAppMessageData alloc] init];
  NSString *key = [inAppMessageData rawValueForInAppMessageKey:InAppMessageKeyViewType];
  NSString *viewType = [inAppMessageData rawValueForInAppMessageViewType:InAppMessageViewTypePicker];
   
  if ([inAppMessage.extras objectForKey:key] && [inAppMessage.extras[key] isEqualToString:viewType]) {
    return [[ModalViewController alloc] initWithInAppMessage:inAppMessage];
  } else {
    return [[ABKInAppMessageModalViewController alloc] initWithInAppMessage:inAppMessage];
  }
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
**オーバーライドしてカスタムビューを提供する**<br>
`loadView()` をオーバーライドし、必要に応じて独自のカスタムビューを設定します。
```swift
override var nibname: String{
  return "ModalPickerViewController"
}

override func loadView() {
  Bundle.main.loadNibNamed(nibName, owner: self, options: nil)
}
```
{% endtab %}
{% tab Objective-C %}
**オーバーライドしてカスタムビューを提供する**<br>
`loadView()` をオーバーライドし、必要に応じて独自のカスタムビューを設定します。
```objc
- (void)loadView {
  NSString *nibName = @"ModalPickerViewController";
  [[NSBundle mainBundle] loadNibNamed:nibName owner:self options:nil];
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
**動的リストのフォーマット変数**<br>
`UIPickerView` コンポーネントをリロードする前に、`inAppMessage` メッセージ変数は_文字列_として出力されます。正しく表示するには、このメッセージを項目の配列としてフォーマットする必要があります。例として、これは [`components(separatedBy: ", ")`](https://developer.apple.com/documentation/foundation/nsstring/1413214-components) を使用して実現できます。
```swift
override func viewDidLoad() {
  super.viewDidLoad()
 
  items = inAppMessage.message.separatedByCommaSpaceValue
  pickerView.reloadAllComponents()
}
```
{% endtab %}
{% tab Objective-C %}
**PickerView の形式変数**<br>
`UIPickerView` コンポーネントをリロードする前に、`inAppMessage` メッセージ変数は_文字列_として出力されます。正しく表示するには、このメッセージを項目の配列としてフォーマットする必要があります。たとえば、[`componentsSeparatedByString`](https://developer.apple.com/documentation/foundation/nsstring/1413214-componentsseparatedbystring?language=objc) を使用してこれを実現できます。
```objc
- (void)viewDidLoad {
  [super viewDidLoad];
   
  self.items = [[NSArray alloc] initWithArray:[self.inAppMessage.message componentsSeparatedByString:@", "]];
  [self.pickerView reloadAllComponents];
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
**カスタム属性を割り当てる**<br>
サブクラスを使用して、ユーザーが [送信] を押した後に、属性とそれに対応する選択した値を Braze に渡します。
```swift
@IBAction func primaryButtonTapped(_ sender: Any) {
  guard let item = selectedItem, !item.isEmpty, let attributeKey = inAppMessage.extras?[InAppMessageKey.attributeKey.rawValue] as? String else { return }
     
  AppboyManager.shared.setCustomAttributeWithKey(attributeKey, andStringValue: item)
}
```
{% endtab %}
{% tab Objective-C %}
**カスタム属性を割り当てる**<br>
サブクラスを使用して、ユーザーが [送信] を押した後に、属性とそれに対応する選択した値を Braze に渡します。
```objc
- (IBAction)primaryButtonTapped:(id)sender {
  InAppMessageData *inAppMessageData = [[InAppMessageData alloc] init];
  NSString *key = [inAppMessageData rawValueForInAppMessageKey:InAppMessageKeyAttributeKey];
   
  if (self.selectedItem.length > 0 && [self.inAppMessage.extras objectForKey:key]) {
    [[AppboyManager shared] setCustomAttributeWithKey:self.inAppMessage.extras[key] andStringValue:self.selectedItem];
  }
}
```
{% endtab %}
{% endtabs %}

{% alert tip %}
カスタムモーダルアプリ内メッセージを活用して、FaceTime で動画を共有することに興味がありますか？SharePlay アプリ内メッセージ[実装ガイド]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/implementation_guide/shareplay/)をご覧ください。
{% endalert%}

### カスタムフルアプリ内メッセージ

![各オプションの横にトグルがある設定オプションの一覧を表示するアプリ内メッセージ。メッセージの一番下には、大きな青い送信ボタンがあります。]({% image_buster /assets/img/iam_implementation/fullscreen.png %}){: style="float:right;max-width:23%;margin-left:15px;border:0;"}

カスタムのフルアプリ内メッセージを使用して、インタラクティブで使いやすいプロンプトを作成し、貴重な顧客データを収集します。右の例は、通知設定を備えたインタラクティブなプッシュプライマーとして再構成されたカスタムフルアプリ内メッセージの実装を示しています。 

開始するには、[`FullListViewController`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/FullListViewController/FullListViewController.swift) にアクセスしてください。

#### ダッシュボード設定

ダッシュボードでカスタムアプリ内メッセージ全体を設定するには、コンマ区切り文字列形式のタグのリストを指定する必要があります。 

キーと値のペアに、`attribute_key` を入力します。このキーは、ユーザーが選択した値とともに、カスタム属性としてユーザープロファイルに保存されます。カスタムビューロジックは、Braze に送信されたユーザー属性を処理する必要があります。

![メッセージ作成画面で見つかった3 つのキーと値のペア。最初のキーと値のペア"attribute_key" は "プッシュタグ "として設定され、2番目の"subtitle_text" は "イネーブルメント通知も... "として設定され、3番目の"view_type" は"table_list".]({% image_buster /assets/img/iam_implementation/dashboard3.png %}として設定される){: style="max-width:65%;"}

#### アプリ内メッセージタッチのインターセプト
![設定とトグルの行を表示する Apple デバイス。カスタムビューはボタンを処理し、ボタンコントロールの外側でのタッチはアプリ内メッセージによって処理され、閉じられます。]({% image_buster /assets/img/iam_implementation_guide.png %}){: style="float:right;max-width:30%;margin-left:10px;border:0"}
カスタムフルアプリ内メッセージボタンを正しく機能させるには、アプリ内メッセージのタッチをインターセプトすることが重要です。デフォルトでは、`ABKInAppMessageImmersive` はメッセージにタップジェスチャ認識機能を追加するので、ユーザーはボタンなしでメッセージを閉じることができます。`UISwitch` またはボタンを `UITableViewCell` ビュー階層に追加すると、タッチはカスタムビューによって処理されるようになります。iOS 6 以降、ジェスチャー認識機能を使用する場合はボタンやその他のコントロールが優先され、カスタムのフルアプリ内メッセージが正常に機能するようになりました。 

