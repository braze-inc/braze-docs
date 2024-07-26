---
nav_title: スタイリング例
article: Styling examples
description: "ヘッダー、タブ、コードブロックなど、Braze Docsでページがどのようにスタイリングされるかを示す。"
page_order: 8 
noindex: true
---

# スタイリング例

ヘッダー、タブ、コードブロックなど、Braze Docsでページがどのようにスタイリングされるかを示す。

## ヘッダーテスト

{% tabs %}
{% tab スタイリング %}

# H1バナー
H1テキスト

Lorem ipsum dolor sit amet, consectetur adipiscing elit.Sed nec tortor at lectus tempus tempor.Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

## H2バナー
H2テキスト

Lorem ipsum dolor sit amet, consectetur adipiscing elit.Sed nec tortor at lectus tempus tempor.Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

### H3バナー
H3テキスト

Lorem ipsum dolor sit amet, consectetur adipiscing elit.Sed nec tortor at lectus tempus tempor.Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

#### H4バナー
H4テキスト

Lorem ipsum dolor sit amet, consectetur adipiscing elit.Sed nec tortor at lectus tempus tempor.Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

##### H5バナー
H5テキスト

Lorem ipsum dolor sit amet, consectetur adipiscing elit.Sed nec tortor at lectus tempus tempor.Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

###### H6バナー
H6テキスト

Lorem ipsum dolor sit amet, consectetur adipiscing elit.Sed nec tortor at lectus tempus tempor.Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

{% endtab %}
{% tab マークダウン %}

```
# H1 Banner

## H2 Banner

### H3 Banner

#### H4 Banner

##### H5 Banner

###### H6 Banner
```
{% endtab %}
{% endtabs %}

## カスタムヘッダーアンカー

見出しにアンカーを追加するには、見出しのある行のエンドツーエンドの部分に以下のコードを追加する。`anchor-text` をこの見出しのアンカーに置き換える。小文字を使い、単語と単語の間にはハイフンを入れる。

```
# Heading Text {#anchor-text}
```

`#` 、その後にカスタム・アンカーが続く標準リンクを作成することで、カスタム・アンカーを持つ見出しにリンクすることができる。

{% raw %}
```
Here is my [link](#anchor-text)
```
{% endraw %}

## フォントテスト

{% tabs %}
{% tab スタイリング %}

通常のテキスト

*テキストを強調する*

**太字**

_**太字で強調する**_

~~取り消し線~~

{% endtab %}
{% tab マークダウン %}
```
Normal Text

*Emphasize Text*

**Bold**

_**Bold Emphasize**_

~~Strikethrough~~
```
{% endtab %}
{% endtabs %}

## 引用テスト

{% tabs %}
{% tab スタイリング %}
> 引用テキスト

#### インライン見積もり
Lorem ipsum dolor ``sit amet, consectetur adipiscing elit``.Sed nec tortor at lectus tempus tempor.

#### 引用 チャンク
```
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor.
```
{% endtab %}
{% tab マークダウン %}
```
> Quoted Text

Lorem ipsum dolor ``sit amet, consectetur adipiscing elit``. Sed nec tortor at lectus tempus tempor.

``` Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. ```
```
{% endtab %}
{% endtabs %}

## テーブルテスト

{% tabs %}
{% tab スタイリング %}
| Instance | Dashboard URL                                                         | REST Endpoint                   |
| -------- | --------------------------------------------------------------------- | ------------------------------- |
| US-01｜`https://dashboard.braze.com` または<br> `https://dashboard-01.braze.com` |`https://rest.iad-01.braze.com` |
| US-02 |`https://dashboard-02.braze.com` |`https://rest.iad-02.braze.com` |
| US-03 |`https://dashboard-03.braze.com` |`https://rest.iad-03.braze.com` |
｜US-04｜`https://dashboard-04.braze.com` ｜`https://rest.iad-04.braze.com` ｜｜。
| US-05 |`https://dashboard-05.braze.com` |`https://rest.iad-05.braze.com` |
| US-06 |`https://dashboard-06.braze.com` |`https://rest.iad-06.braze.com` |
｜US-07｜`https://dashboard-07.braze.com` ｜`https://rest.iad-07.braze.com` ｜｜。
| US-08｜`https://dashboard-08.braze.com` ｜`https://rest.iad-08.braze.com` ｜。
| EU-01｜`https://dashboard.braze.eu` または<br> `https://dashboard-01.braze.eu`   |`https://rest.fra-01.braze.eu` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
{% endtab %}
{% tab マークダウン %}
```
| Instance | Dashboard URL                                                         | REST Endpoint                   |
| -------- | --------------------------------------------------------------------- | ------------------------------- |
| US-01    | `https://dashboard.braze.com` or<br> `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` |
| US-02    | `https://dashboard-02.braze.com`                                      | `https://rest.iad-02.braze.com` |
| US-03    | `https://dashboard-03.braze.com`                                      | `https://rest.iad-03.braze.com` |
| US-04    | `https://dashboard-04.braze.com`                                      | `https://rest.iad-04.braze.com` |
| US-05    | `https://dashboard-05.braze.com`                                      | `https://rest.iad-05.braze.com` |
| US-06    | `https://dashboard-06.braze.com`                                      | `https://rest.iad-06.braze.com` |
| US-07    | `https://dashboard-07.braze.com`                                      | `https://rest.iad-07.braze.com` |
| US-08    | `https://dashboard-08.braze.com`                                      | `https://rest.iad-08.braze.com` |
| EU-01    | `https://dashboard.braze.eu` or<br> `https://dashboard-01.braze.eu`   | `https://rest.fra-01.braze.eu`  |
| EU-02    | `https://dashboard-02.braze.eu`                                       | `https://rest.fra-02.braze.eu`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
```
{% endtab %}
{% endtabs %}

#### テーブルの改行を列ごとにリセットする
改行がデフォルトのスタイルにリセットされるべきテーブルの列については、Markdownオプションを使用して、`.reset-td-br-1`,`.reset-td-br-2`,`.reset-td-br-3`,`.reset-td-br-4` を使用してテーブルにクラスを追加し、`#` は4までの列に対応する。

#### 使用
```
| Event Name                                                       | Feed Type              | Description                                                  | Custom Attributes                                                             |
| ---------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG             | Unbound Feed           | An email was successfully delivered to a User's mail server. | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG` | Unbound Feed           | User opened an email.                                        | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| In-App Message Impression                                        | Platform-specific Feed | User viewed an In-App Message.                               | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

```
{% tabs ローカル %}
{% tab 前 %}

| イベント名                                                       | フィードタイプ              | 説明                                                  | カスタム属性                                                             |
| ---------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG             | アンバインド・フィード           | ユーザーのメールサーバーにメールが正常に配信された。 | `campaign_id``canvas_step_id`,`canvas_id` 、 `canvas_variation_id`           |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG` | アンバインド・フィード           | ユーザーがメールを開封した。                                        | `campaign_id``canvas_step_id`,`canvas_id` 、 `canvas_variation_id`           |
| アプリ内メッセージ-インプレッション                                        | プラットフォーム別フィード | ユーザーがアプリ内メッセージを閲覧した。                               | `app_id``campaign_id`,`canvas_step_id`,`canvas_id` 、 `canvas_variation_id` |

{% endtab %}
{% tab その後 %}

| イベント名                                                       | フィードタイプ              | 説明                                                  | カスタム属性                                                             |
| ---------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG             | アンバインド・フィード           | ユーザーのメールサーバーにメールが正常に配信された。 | `campaign_id``canvas_step_id`,`canvas_id` 、 `canvas_variation_id`           |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG` | アンバインド・フィード           | ユーザーがメールを開封した。                                        | `campaign_id``canvas_step_id`,`canvas_id` 、 `canvas_variation_id`           |
| アプリ内メッセージ-インプレッション                                        | プラットフォーム別フィード | ユーザーがアプリ内メッセージを閲覧した。                               | `app_id``campaign_id`,`canvas_step_id`,`canvas_id` 、 `canvas_variation_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}
{% endtab %}
{% endtabs %}

## リンクテスト
{% tabs %}
{% tab スタイリング %}
リンクはこちら：[Braze.com](https://www.braze.com){: height="36px" width="36px"}
{% endtab %}
{% tab マークダウン %}
```
[Braze.com](https://www.braze.com)
```
{% endtab %}
{% endtabs %}

## 画像, 写真
{% tabs %}
{% tab スタイリング %}
画像：![ロゴ]({% image_buster /assets/img/braze-logo-mark.png %}){: style="max-width:30%;"}

#### リンク画像、写真テスト

リンク画像、写真：[![Braze]({% image_buster /assets/img/braze-logo-mark.png %}){: style="max-width:30%;"}](https://www.braze.com)

#### 画像, 写真

![テキスト]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="max-width:30%; color: green" }

#### 画像、写真を固定する

![テキスト]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="float:right;max-width:30%; color: green" }
<br><br><br><br><br>
{% endtab %}
{% tab マークダウン %}

```
![Logo]({% image_buster /assets/img/braze-logo-mark.png %}){: style="max-width:30%;"}

[![Braze]({% image_buster /assets/img/braze-logo-mark.png %})](https://www.braze.com)

![Text]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="max-width:30%; color: green" }

![Text]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="float:right;max-width:30%;" }
```
{% endtab %}
{% endtabs %}

## ギャラリーテスト
{% tabs %}
{% tab スタイリング %}
{% gallery %}
{{site.baseurl}}/assets/img_archive/EBTH_Email.png?bf892368baf287cba5ab9a6e3b09431d<br> これは[リンク](https://www.braze.com)だ。
{{site.baseurl}}/assets/img_archive/iHeartRadio_Email.png?ecd2c8fe148939b7de957fe85cd6317e<br> これも`comment` だ。
{{site.baseurl}}/assets/img_archive/Saucey_Email.png?b9768937a1cc12d4c08e55a52e700d68<br> これはまた別の**コメント**だ。
{{site.baseurl}}/assets/img/schellman_iso27001_seal_grey_CMYK_300dpi_jpg.png?1b1fb9dbb80b0332c62512dcf9c83258<br> **画像、写真タイトル**<br> これはラインブレイクするかどうかのテストだ。
{{site.baseurl}}/assets/img/SOC2.png?6338040be8e98c4c9abe1f35b3e43e3a<br> これはいつものコメントだ。
{% endgallery %}
{% endtab %}
{% tab マークダウン %}
{% raw %}
```
{% gallery %}
{{site.baseurl}}/assets/img_archive/EBTH_Email.png?bf892368baf287cba5ab9a6e3b09431d  <br> This is a [link](https://www.braze.com).
{{site.baseurl}}/assets/img_archive/iHeartRadio_Email.png?ecd2c8fe148939b7de957fe85cd6317e  <br> This is another `comment`.
{{site.baseurl}}/assets/img_archive/Saucey_Email.png?b9768937a1cc12d4c08e55a52e700d68  <br> This is yet another **comment**.
{{site.baseurl}}/assets/img/schellman_iso27001_seal_grey_CMYK_300dpi_jpg.png?1b1fb9dbb80b0332c62512dcf9c83258 <br> **IMAGE TITLE** <br> This is a test to see if it will line break.
{{site.baseurl}}/assets/img/SOC2.png?6338040be8e98c4c9abe1f35b3e43e3a  <br> This is a regular comment.
{% endgallery %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## インタラクティブ画像, 写真
{% tabs %}
{% tab スタイリング %}
<div class="iactiveImg" data-ii="6967"></div><script src="https://interactive-img.com/js/include.js"></script>
{% endtab %}
{% tab マークダウン %}
```
<div class="iactiveImg" data-ii="6967"></div><script src="https://interactive-img.com/js/include.js"></script>
```
{% endtab %}
{% endtabs %}
<!--- Leaving formatting here just in case it's important...
<div style="position: relative; padding-bottom: 83%; padding-top: 0; height: 0;"><iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border-width:0px; max-width:100%; overflow-y:auto;" width="100%" height="100%" src="https://interactive-img.com/view?id=6967&iframe=true"></iframe></div>
-->

## コード・スニペット・テスト

{% tabs %}
{% tab スタイリング %}
#### コードテスト Objective C
```objc
- (void)submitFeedback:(ABKFeedback * )feedback
 withCompletionHandler:(nullable void (^)(ABKFeedbackSentResult feedbackSentResult))completionHandler;
```

#### コードテスト SWIFT
```swift
Appboy.sharedInstance()?.submitFeedback(feedback) { (feedbackSentResult) in
      print("Feedback sent: (feedbackSentResult)")
    }
```

#### コードテスト Java
```java
@Override
public void onResume() {
  super.onResume();
  // Registers the BrazeInAppMessageManager for the current Activity. This Activity will now listen for
  // in-app messages from Braze.
  BrazeInAppMessageManager.getInstance().registerInAppMessageManager(activity);
}
```

#### コードテスト json
```json
{
   "attributes" : "Attributes" ,
   "events" : ["Array", "Of", "Object"],
   "purchases" : ["Array" ,"Of" ,"Purchase" ,"Object"]
}
```

#### コードテスト JavaScript
```javascript
braze.subscribeToFeedUpdates(function(feed) {
  var cards = feed.cards;
  braze.showFeed(undefined, cards);
});
braze.requestFeedRefresh();
```

#### パイグメンテスト
```python
#!/usr/bin/python3

from engine import RunForrestRun

"""Test code for syntax highlighting!"""

class Foo:
	def __init__(self, var):
		self.var = var
		self.run()

	def run(self):
		RunForrestRun()  # run along!

```
{% endtab %}
{% tab マークダウン %}
![マークダウンの例]({% image_buster /assets/img_archive/code_snippet.png %})
{% endtab %}
{% endtabs %}

## アラートテスト

{% tabs %}
{% tab スタイリング %}

{% alert tip %}これがヒントだ。{% endalert %}

{% alert note %}これは注釈である。{% endalert %}

{% alert important %}これは重要な警告である。{% endalert %}

{% alert warning %}これは警告である。{% endalert %}

{% alert update %}これは更新である。{% endalert %}

{% endtab %}
{% tab マークダウン %}
{% raw %}
```
{% alert tip %}
This is a tip
{% endalert %}

{% alert note %}
This is a note
{% endalert %}

{% alert important %}
This is a important alert
{% endalert %}

{% alert warning %}
This is a warning
{% endalert %}

{% alert update %}
This is a update
{% endalert %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## 埋め込み動画テスト
{% tabs %}
{% tab スタイリング %}
#### 埋め込み動画/YouTube
デフォルトはYouTube embeddedである。
{% multi_lang_include video.html id="9SrKbY4BV2E" source="youtube" %}

#### 埋め込み動画の右揃え
{% multi_lang_include video.html id="9SrKbY4BV2E" align="right" source="youtube" %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit.Sed nec tortor at lectus tempus tempor.Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.Lorem ipsum dolor sit amet, consectetur adipiscing elit.Sed nec tortor at lectus tempus tempor.Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.Lorem ipsum dolor sit amet, consectetur adipiscing elit.Sed nec tortor at lectus tempus tempor.Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

#### 埋め込み動画の左揃え
{% multi_lang_include video.html id="9SrKbY4BV2E" align="left" source="youtube" %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit.Sed nec tortor at lectus tempus tempor.Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.Lorem ipsum dolor sit amet, consectetur adipiscing elit.Sed nec tortor at lectus tempus tempor.Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.Lorem ipsum dolor sit amet, consectetur adipiscing elit.Sed nec tortor at lectus tempus tempor.Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.
<br /><br />

#### 織機の例
* 使用 `source="loom"`
{% multi_lang_include video.html id="c1d3199463c448e8918f046265b54eb2" source="loom" %}

{% endtab %}
{% tab マークダウン %}

YouTube動画を埋め込むにはYouTube IDが必要だ。URLの`v=` の後に表示される。例えば、`https://www.youtube.com/watch?v=VR1qn1OBP7k` のIDは`VR1qn1OBP7k` である。

{% raw %}
```html
{% multi_lang_include video.html id="[youtube_id]" source="youtube" %}
```
{% endraw %}

右寄せまたは左寄せにし、最大幅を50%に制限するには、`align` パラメータ =`left` または`right` を使用する：
{% raw %}
```html
{% multi_lang_include video.html id="[youtube_id]" align="left" source="youtube" %}

{% multi_lang_include video.html id="[youtube_id]" align="right" source="youtube" %}
```
{% endraw %}

織機の例：
{% raw %}
```html
{% multi_lang_include video.html id="[lid]" source="loom" %}
```
{% endraw %}

{% endtab %}
{% endtabs %}

#### 高解像度のためにステータスを配置した注目の動画レイアウト

高解像度表示のために左側に静的動画を配置する特集動画レイアウトを使用するには、ページのYAMLヘッダーに`video_id` と`video_type` (`youtube` など) を追加する。デフォルトでは、`video_source` は`youtube` に設定されている。

{% raw %}
```yaml
layout: featured_video
video_id: [video_id]
video_source: youtube
```
{% endraw %}

## リストテスト
{% tabs %}
{% tab スタイリング %}
#### 弾丸

- リスト1
  - サブリスト1
- リスト2
  - サブリスト2a
    - サブ・サブ・リスト2
- リスト3

#### 番号付き

1. リスト1
   - サブリスト1
2. リスト2
3. リスト3
   - サブリスト3a
   - サブリスト3b
     - サブ・サブ・リスト3
4. リスト4
    1. サブリスト4a
        1. サブ・サブ・リスト 4
    2. サブリスト4b
        1. サブ・サブ・リスト 4

{% endtab %}
{% tab マークダウン %}
```
#### Bullet

- List 1
  - Sub List 1
- List 2
  - Sub List 2a
    - Sub Sub List 2
- List 3

#### Numbered

1. List 1
   - Sub List 1
2. List 2
3. List 3
   - Sub List 3a
   - Sub List 3b
     - Sub Sub List 3
4. List 4
    1. Sub list 4a
        1. Sub Sub List 4
    2. Sub list 4b
        1. sub sub list 4
```
{% endtab %}
{% endtabs %}

## 折りたたみ式コンテンツ・テスト {#collapsible-content}
{% tabs %}
{% tab スタイリング %}
{% details クリックして拡大する %}
#### 見てごらん！隠されたコードブロック！

```python
print("hello world!")
```
{% enddetails %}
{% endtab %}
{% tab マークダウン %}
{% raw %}
```liquid
{% details Click me to Expand %}
...
{% enddetails %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## タブテスト

#### カスタムタブ

{% tabs ローカル %}
{% tab OBJECTIVE-C %}

次のコード行を `AppDelegate.m` ファイルに追加します。

```objc
{% if include.platform == 'iOS' %}#import "Appboy-iOS-SDK/AppboyKit.h"{% else %}#import <AppboyTVOSKit/AppboyKit.h>{% endif %}
```

`AppDelegate.m` ファイル内で、`application:didFinishLaunchingWithOptions` メソッド内に次のスニペットを追加します。

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

{% endtab %}
{% tab 速い %}

Braze SDK を CocoaPods または Carthage と統合する場合は、次のコード行を `AppDelegate.swift` ファイルに追加します。

```swift
{% if include.platform == 'iOS' %}#import Appboy_iOS_SDK{% else %}#import AppboyTVOSKit{% endif %}
```

Swift プロジェクトで ObJECTIVE-C コードを使用することについての詳細な情報は、\[Apple Developer Docs]\[apple_initial_setup_19].

`AppDelegate.swift` で、次のスニペットを `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` に追加します。

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```
{% endtab %}
{% endtabs %}

#### 使用
{% raw %}
`{% tabs %}` 、**タブを**内部で囲む。 `{% endtabs %}`
個々の**タブを**Liquidコードとタブ名で囲む`{% tab [Tab name] %}` および `{% endtab %}`
{% endraw %}

{% alert important %}
 ページ上のタブの数は一定であるべきで、そうでないとタブの内容が隠れてしまう可能性がある。
 例えば、あるタブの設定に`C++` 、`C-Sharp` 、`JS` があり、別のタブの設定に`C-Sharp` 、`JS` があるとする、
誰かが`C++` をクリックすると、他のセクションには何も表示されない。回避策としては、以下のローカルタブのオプションを参照のこと。
{% endalert %}

{% raw %}
```liquid
{% tabs %}
{% tab objective-c %}
Content of objective-c
{% endtab %}
{% tab swift %}
Content of swift
{% endtab %}
{% endtabs %}
```
{% endraw %}

#### ローカルタブ
特定のセクションのタブコンテンツだけを変更するタブなど、自己完結型のタブの場合は、親タブブロックのローカライゼーションパラメータを使用する。

{% raw %}
```liquid
{% tabs local %}
...
{% endtabs %}
```
{% endraw %}

#### サブタブ
タブ内のタブには、`subtabs` と`subtab` が使える。デフォルト設定は`local` である。
グローバルな`subtabs` 、`global` オプションを使用する： {% raw %}`{% subtabs global %}`{% endraw %}

{% tabs ローカル %}
{% tab タブ1 %}
タブ・コンテンツ 1
{% subtabs %}
{% subtab Subtab 1a %}
サブタブ1aの内容
{% endsubtab %}
{% subtab Subtab 2a %}
サブタブ2aの内容
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab タブ2 %}
タブ・コンテンツ 2
{% subtabs %}
{% subtab Subtab 1b %}
サブタブ1aの内容
{% endsubtab %}
{% subtab Subtab 2b %}
サブタブ2aの内容
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

##### マークダウン
{% raw %}
```
{% tabs local %}
{% tab Tab 1 %}
tab content 1
{% subtabs %}
{% subtab Subtab 1a %}
Subtab 1a content
{% endsubtab %}
{% subtab Subtab 2a %}
Subtab 2a content
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Tab 2 %}
tab content 2
{% subtabs %}
{% subtab Subtab 1b %}
Subtab 1a content
{% endsubtab %}
{% subtab Subtab 2b %}
Subtab 2a content
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}
```
{% endraw %}

[1]: {% image_buster /assets/img_archive/code_snippet.png %}
