---
nav_title: スタイリング例
article: Styling examples
description: "これは、ヘッダー、タブ、コードブロックなど、Braze Docs でページがスタイル設定される方法です。"
page_order: 8 
noindex: true
---

# スタイリング例

これは、ヘッダー、タブ、コードブロックなど、Braze Docs でページがスタイル設定される方法です。

## ヘッダーテスト

{% tabs %}
{% tab Styling %}

# H1バナー
H1テキスト

Lorem ipsum dolor sit amet, consectetur adipiscing elit.レクタステンポアのSedネクトトータ。Tellus diam, finibus eu dictum non, varius et ipsum をサスペンドします。

## H2バナー
H2テキスト

Lorem ipsum dolor sit amet, consectetur adipiscing elit.レクタステンポアのSedネクトトータ。Tellus diam, finibus eu dictum non, varius et ipsum をサスペンドします。

### H3バナー
H3テキスト

Lorem ipsum dolor sit amet, consectetur adipiscing elit.レクタステンポアのSedネクトトータ。Tellus diam, finibus eu dictum non, varius et ipsum をサスペンドします。

#### H4バナー
H4テキスト

Lorem ipsum dolor sit amet, consectetur adipiscing elit.レクタステンポアのSedネクトトータ。Tellus diam, finibus eu dictum non, varius et ipsum をサスペンドします。

##### H5バナー
H5テキスト

Lorem ipsum dolor sit amet, consectetur adipiscing elit.レクタステンポアのSedネクトトータ。Tellus diam, finibus eu dictum non, varius et ipsum をサスペンドします。

###### H6バナー
H6 テキスト

Lorem ipsum dolor sit amet, consectetur adipiscing elit.レクタステンポアのSedネクトトータ。Tellus diam, finibus eu dictum non, varius et ipsum をサスペンドします。

{% endtab %}
{% tab Markdown %}

\`\`\`
# H1バナー

## H2バナー

### H3バナー

#### H4バナー

##### H5バナー

###### H6バナー
\`\`\`
{% endtab %}
{% endtabs %}

## カスタムヘッダーアンカー

ヘッダーにアンカーを追加するには、ヘッダーがある行の末尾に次のコードを追加します。`anchor-text` をこの見出しのアンカーに置き換えます。小文字を使用し、単語間にハイフンを入れます。

\`\`\`
# 見出しテキスト {#anchor-text}
\`\`\`

番号記号`#` の後にカスタムアンカーが続く標準リンクを作成することで、カスタムアンカーを使用してヘッダーにリンクできます。

{% raw %}
```
Here is my [link](#anchor-text)
```
{% endraw %}

## フォントテスト

{% tabs %}
{% tab Styling %}

標準テキスト

*テキストを強調する*

**太字**

_**大胆な強調**_

～～打撃～～

{% endtab %}
{% tab Markdown %}
\`\`\`
標準テキスト

*テキストを強調する*

**太字**

_**大胆な強調**_

～～打撃～～
\`\`\`
{% endtab %}
{% endtabs %}

## 見積テスト

{% tabs %}
{% tab Styling %}
> 引用文

#### インラインクォート
Lorem ipsum dolor ``sit amet, consectetur adipiscing elit``.レクタステンポアのSedネクトトータ。

#### チャンクを引用
```
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor.
```
{% endtab %}
{% tab Markdown %}
\`\`\`
> 引用文

Lorem ipsum dolor ``sit amet, consectetur adipiscing elit``.レクタステンポアのSedネクトトータ。

``` Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. ```
\`\`\`
{% endtab %}
{% endtabs %}

## テーブルテスト

{% tabs %}
{% tab Styling %}
インスタンス| ダッシュボードURL | REST エンドポイント
----------- |---------------- | --------------------
US-01 | `https://dashboard.braze.com`または<br> `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com`
米国
米国
米国
米国
米国
米国
米国
EU-01 | `https://dashboard.braze.eu`または<br> `https://dashboard-01.braze.eu` | `https://rest.fra-01.braze.eu`
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
{% endtab %}
{% tab Markdown %}
```
Instance    | Dashboard URL   | REST Endpoint
----------- |---------------- | --------------------
US-01 | `https://dashboard.braze.com` or<br> `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com`
US-02 | `https://dashboard-02.braze.com` | `https://rest.iad-02.braze.com`
US-03 | `https://dashboard-03.braze.com` | `https://rest.iad-03.braze.com`
US-04 | `https://dashboard-04.braze.com` | `https://rest.iad-04.braze.com`
US-05 | `https://dashboard-05.braze.com` | `https://rest.iad-05.braze.com`
US-06 | `https://dashboard-06.braze.com` | `https://rest.iad-06.braze.com`
US-07 | `https://dashboard-07.braze.com` | `https://rest.iad-07.braze.com`
US-08 | `https://dashboard-08.braze.com` | `https://rest.iad-08.braze.com`
EU-01 | `https://dashboard.braze.eu` or<br> `https://dashboard-01.braze.eu` | `https://rest.fra-01.braze.eu`
EU-02 | `https://dashboard-02.braze.eu` | `https://rest.fra-02.braze.eu`
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
```
{% endtab %}
{% endtabs %}

#### 列ごとのテーブルのワードブレークのリセット
word-break をデフォルトスタイルにリセットする必要があるテーブル列の場合、Markdown オプションを使用して、`.reset-td-br-1`、`.reset-td-br-2`、`.reset-td-br-3`、`.reset-td-br-4`、`.reset-td-br-4` を使用してテーブルにクラスを追加し、列に対応する`#` を最大4 にします。

#### 使用
\`\`\`
| イベント名| フィードタイプ| 説明| カスタム属性
| ------------------------------------ | ---------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG | Unbound Feed | メールがユーザのメールサーバに正常に配信されました。| `campaign_id`、`canvas_step_id`、`canvas_id`、`canvas_variation_id` |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG` | Unbound Feed | ユーザーがメールを開きました。| `campaign_id`、`canvas_step_id`、`canvas_id`、`canvas_variation_id` |
| アプリ内メッセージ印象| プラットフォーム固有のフィード| アプリ内メッセージを表示したユーザ。| `app_id`、`campaign_id`、`canvas_step_id`、`canvas_id`、`canvas_variation_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

\`\`\`
{% tabs local %}
{% tab Before %}

| イベント名| フィードタイプ| 説明| カスタム属性|
|------------------------------------------------------------------|------------------------|--------------------------------------------------------------|-------------------------------------------------------------------------------|
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG | Unbound Feed | メールがユーザのメールサーバに正常に配信されました。| `campaign_id`、`canvas_step_id`、`canvas_id`、`canvas_variation_id` |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG` | Unbound Feed | ユーザーがメールを開きました。| `campaign_id`、`canvas_step_id`、`canvas_id`、`canvas_variation_id` |
| アプリ内メッセージ印象| プラットフォーム固有のフィード| アプリ内メッセージを表示したユーザ。| `app_id`、`campaign_id`、`canvas_step_id`、`canvas_id`、`canvas_variation_id` |

{% endtab %}
{% tab After %}

| イベント名| フィードタイプ| 説明| カスタム属性|
|------------------------------------------------------------------|------------------------|--------------------------------------------------------------|-------------------------------------------------------------------------------|
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG | Unbound Feed | メールがユーザのメールサーバに正常に配信されました。| `campaign_id`、`canvas_step_id`、`canvas_id`、`canvas_variation_id` |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG` | Unbound Feed | ユーザーがメールを開きました。| `campaign_id`、`canvas_step_id`、`canvas_id`、`canvas_variation_id` |
| アプリ内メッセージ印象| プラットフォーム固有のフィード| アプリ内メッセージを表示したユーザ。| `app_id`、`campaign_id`、`canvas_step_id`、`canvas_id`、`canvas_variation_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}
{% endtab %}
{% endtabs %}

## リンクテスト
{% tabs %}
{% tab Styling %}
リンク先:[Braze.com](https://www.braze.com){: height="36px" width="36px"}
{% endtab %}
{% tab Markdown %}
```
[Braze.com](https://www.braze.com)
```
{% endtab %}
{% endtabs %}

## 画像テスト
{% tabs %}
{% tab Styling %}
画像

#### リンク画像テスト

リンクされた画像: [![Braze]({% image_buster /assets/img/braze-logo-mark.png %}){: style="max-width:30%;"}](https://www.braze.com)

#### イメージスタイリング

![Text]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="max-width:30%; color: green" }

#### イメージのアンカー

![Text]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="float:right;max-width:30%; color: green" }
<br><br><br><br><br>
{% endtab %}
{% tab Markdown %}

\`\`\`
![Logo]({% image_buster /assets/img/braze-logo-mark.png %}){: style="max-width:30%;"}

[![Braze]({% image_buster /assets/img/braze-logo-mark.png %})](https://www.braze.com)

![Text]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="max-width:30%; color: green" }

![Text]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="float:right;max-width:30%;" }
\`\`\`
{% endtab %}
{% endtabs %}

## ギャラリー試験
{% tabs %}
{% tab Styling %}
{% gallery %}
{{site.baseurl}}/assets/img_archive/EBTH_Email.png?bf892368baf287cba5ab9a6e3b09431d <br> これは[リンク](https://www.braze.com)です。
{{site.baseurl}}/assets/img_archive/iHeartRadio_Email.png?ecd2c8fe148939b7de957fe85cd6317e <br> これは別の`comment` です。
{{site.baseurl}}/assets/img_archive/Saucey_Email.png?b9768937a1cc12d4c08e55a52e700d68 <br> これは、さらに別の**comment** です。
{{site.baseurl}}/assets/img/schellman_iso27001_seal_grey_CMYK_300dpi_jpg.png?1b1fb9dbb80b0332c62512dcf9c83258 <br> **画像のタイトル**<br> これは改行するかどうかを調べるテストです。
{{site.baseurl}}/assets/img/SOC2.png?6338040be8e98c4c9abe1f35b3e43e3a <br> これは通常のコメントです。
{% endgallery %}
{% endtab %}
{% tab Markdown %}
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

## 対話型画像テスト
{% tabs %}
{% tab Styling %}
<div class="iactiveImg" data-ii="6967"></div><script src="https://interactive-img.com/js/include.js"></script>
{% endtab %}
{% tab Markdown %}
```
<div class="iactiveImg" data-ii="6967"></div><script src="https://interactive-img.com/js/include.js"></script>
```
{% endtab %}
{% endtabs %}
<!--- Leaving formatting here just in case it's important...
<div style="position: relative; padding-bottom: 83%; padding-top: 0; height: 0;"><iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border-width:0px; max-width:100%; overflow-y:auto;" width="100%" height="100%" src="https://interactive-img.com/view?id=6967&iframe=true"></iframe></div>
-->

## コードスニペットテスト

{% tabs %}
{% tab Styling %}
#### コードテスト目標C
```objc
- (void)submitFeedback:(ABKFeedback * )feedback
 withCompletionHandler:(nullable void (^)(ABKFeedbackSentResult feedbackSentResult))completionHandler;
```

#### コードテストスイフト
```swift
Appboy.sharedInstance()?.submitFeedback(feedback) { (feedbackSentResult) in
      print("Feedback sent: (feedbackSentResult)")
    }
```

#### コードテストJava
```java
@Override
public void onResume() {
  super.onResume();
  // Registers the BrazeInAppMessageManager for the current Activity. This Activity will now listen for
  // in-app messages from Braze.
  BrazeInAppMessageManager.getInstance().registerInAppMessageManager(activity);
}
```

#### コードテストjson
```json
{
   "attributes" : "Attributes" ,
   "events" : ["Array", "Of", "Object"],
   "purchases" : ["Array" ,"Of" ,"Purchase" ,"Object"]
}
```

#### コードテストJavaScript
```javascript
braze.subscribeToFeedUpdates(function(feed) {
  var cards = feed.cards;
  braze.showFeed(undefined, cards);
});
braze.requestFeedRefresh();
```

#### ピグメント試験
\`\`\`python
/usr/bin/python3

RunForrestRunのインポートエンジンから

"""構文ハイライト用のテストコード!""""

Fooクラス:
	def __init__(self, var):
		self.var = var
		self.run()

	def run(self):
		RunForrestRun()  # run along!

\`\`\`
{% endtab %}
{% tab Markdown %}
![Markdown Example]({% image_buster /assets/img_archive/code_snippet.png %})
{% endtab %}
{% endtabs %}

## アラートテスト

{% tabs %}
{% tab Styling %}

{% alert tip %}これはヒントです{% endalert %}

{% alert note %}これは注記です{% endalert %}

{% alert important %}これは重要な警告です{% endalert %}

{% alert warning %}これは警告です{% endalert %}

{% alert update %}アップデートです{% endalert %}

{% endtab %}
{% tab Markdown %}
{% raw %}
\`\`\`
{% alert tip %}
これはヒントです
{% endalert %}

{% alert note %}
これは注記です
{% endalert %}

{% alert important %}
これは重要な警告です
{% endalert %}

{% alert warning %}
これは警告です
{% endalert %}

{% alert update %}
これはアップデートです
{% endalert %}
\`\`\`
{% endraw %}
{% endtab %}
{% endtabs %}

## 内蔵ビデオテスト
{% tabs %}
{% tab Styling %}
#### 内蔵ビデオ/YouTube
デフォルトはYouTube 組み込みです。
{% multi_lang_include video.html id="XY5vFY" source="youtube" %}

#### 埋め込みビデオの右揃え
{% multi_lang_include video.html id="XYuXoKIvFY" align="right" source="youtube" %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit.Sed nec tortor at lectus tempus tempor.Tellus diam, finibus eu dictum non, varius et ipsum をサスペンドします。Lorem ipsum dolor sit amet, consectetur adipiscing elit.Sed nec tortor at lectus tempus tempor.Tellus diam, finibus eu dictum non, varius et ipsum をサスペンドします。Lorem ipsum dolor sit amet, consectetur adipiscing elit.Sed nec tortor at lectus tempus tempor.Tellus diam, finibus eu dictum non, varius et ipsum をサスペンドします。

#### 内蔵ビデオの左揃え
{% multi_lang_include video.html id="XY5uXvFY" align="left" source="youtube" %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit.Sed nec tortor at lectus tempus tempor.Tellus diam, finibus eu dictum non, varius et ipsum をサスペンドします。Lorem ipsum dolor sit amet, consectetur adipiscing elit.Sed nec tortor at lectus tempus tempor.Tellus diam, finibus eu dictum non, varius et ipsum をサスペンドします。Lorem ipsum dolor sit amet, consectetur adipiscing elit.Sed nec tortor at lectus tempus tempor.Tellus diam, finibus eu dictum non, varius et ipsum をサスペンドします。
<br /><br />

#### 織機の例
* 使用 `source="loom"`
{% multi_lang_include video.html id="c1d3199463c448e8918f046265b54eb2" source="loom" %}

{% endtab %}
{% tab Markdown %}

{% raw %}
```html
{% multi_lang_include video.html id="[youte_id]" source="youtube" %}
```
{% endraw %}

右または左に揃え、最大幅を50% に制限するには、`align` パラメータ= `left` または`right` を使用します。
{% raw %}
\`\`\`html
{% multi_lang_include video.html id="[ytube_id]" align="left" source="youtube" %}

{% multi_lang_include video.html id="[youe_id]" align="right" source="youtube" %}
\`\`\`
{% endraw %}

織機の例:
{% raw %}
```html
{% multi_lang_include video.html id="[lid]" source="loom" %}
```
{% endraw %}

{% endtab %}
{% endtabs %}

#### 高解像度のためのステータス配置を備えた特徴的なビデオレイアウト

高解像度表示のためにスタティックビデオを左側に配置する機能付きビデオレイアウトを使用するには、ページのyaml ヘッダに`video_id` と`video_type` (`youtube` など) を追加します。デフォルトでは、`video_source` は`youtube` に設定されます。

{% raw %}
```yaml
layout: featured_video
video_id: [video_id]
video_source: youtube
```
{% endraw %}

## リストテスト
{% tabs %}
{% tab Styling %}
#### ビュレット

- リスト1
  - サブリスト1
- リスト2
  - サブリスト2a
    - サブサブリスト2
- リスト3

#### 番号

1. リスト1
   - サブリスト1
2. リスト2
3. リスト3
   - サブリスト3a
   - サブリスト3b
     - サブサブリスト3
4. リスト4
    1. サブリスト4a
        1. サブサブリスト4
    2. サブリスト4b
        1. サブリスト4

{% endtab %}
{% tab Markdown %}
\`\`\`
#### ビュレット

- リスト1
  - サブリスト1
- リスト2
  - サブリスト2a
    - サブサブリスト2
- リスト3

#### 番号

1. リスト1
   - サブリスト1
2. リスト2
3. リスト3
   - サブリスト3a
   - サブリスト3b
     - サブサブリスト3
4. リスト4
    1. サブリスト4a
        1. サブサブリスト4
    2. サブリスト4b
        1. サブリスト4
\`\`\`
{% endtab %}
{% endtabs %}

## 折りたたみ式コンテンツテスト
{% tabs %}
{% tab Styling %}
{% details Click me to Expand %}
#### 見てください!隠されたコードブロック!

```python
print("hello world!")
```
{% enddetails %}
{% endtab %}
{% tab Markdown %}
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

{% tabs local %}
{% tab OBJECTIVE-C %}

以下のコード行を`AppDelegate.m` ファイルに追加します。

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
{% tab swift %}

Braze SDK をCocoaPods またはCarthage と統合する場合は、`AppDelegate.swift` ファイルに次のコード行を追加します。

```swift
{% if include.platform == 'iOS' %}#import Appboy_iOS_SDK{% else %}#import AppboyTVOSKit{% endif %}
```

Swift プロジェクトでObjective-C コードを使用する方法の詳細については、[Apple Developer Docs][apple\_initial\_setup\_19] を参照してください。

`AppDelegate.swift` で、`application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` に次のスニペットを追加します。

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```
{% endtab %}
{% endtabs %}

#### 使用
{% raw %}
**tabs**を`{% tabs %}`で囲み `{% endtabs %}`
個々の**tab**を`{% tab [Tab name] %}`タブのリキッドコードと名前で囲み `{% endtab %}`
{% endraw %}

{% alert important %}
 ページ上のタブの数は一貫している必要があります。一貫していない場合は、タブの内容が非表示になっている可能性があります。
 たとえば、あるタブセットに`C++`、`C-Sharp`および`JS`があり、別のタブセットに`C-Sharp`および`JS`がある場合、
誰かが`C++` をクリックすると、他のセクションには何も表示されません。回避策については、次のローカルタブオプションを参照してください。
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
特定のセクションのタブコンテンツのみを変更するタブなど、自己完結型のタブの場合は、親タブブロックでローカルパラメータを使用します。

{% raw %}
```liquid
{% tabs local %}
...
{% endtabs %}
```
{% endraw %}

#### サブタブ
タブ内のタブの場合は、`subtabs` と`subtab` を使用できます。デフォルト設定は`local`です。
グローバル`subtabs` の場合は、`global` オプションを使用します。 {% raw %}`{% subtabs global %}`{% endraw %}

{% tabs local %}
{% tab Tab 1 %}
タブ内容1
{% subtabs %}
{% subtab Subtab 1a %}
サブタブ1aの内容
{% endsubtab %}
{% subtab Subtab 2a %}
サブタブ2aの内容
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Tab 2 %}
タブ内容2
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

##### 値下げ
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
