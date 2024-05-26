---
nav_title: 以前の世代
article_title: 以前のアプリ内メッセージ世代
page_order: 20
page_type: reference
description: "この記事では、Braze のアプリ内メッセージに関する以前の情報をレビューします。"
channel: in-app messages
noindex: true
hidden : true
---

# 以前のアプリ内メッセージ世代

{% alert important %}
このページでは、アプリ内メッセージに関する以前の情報を確認します。現在のアプリ内メッセージ生成に関する最新情報を確認するには、現在の [アプリ内メッセージの]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) ドキュメントをご覧ください。
{% endalert %}

## ユニバーサル

これにより、アプリ内メッセージに関する以前の情報が確認されます。現在のアプリ内メッセージ生成に関する最新情報を確認するには、 [アプリ内メッセージの概要ドキュメント]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/)をご覧ください。

{% details Fullscreen %}
これらは最も魅力的ですが、ユーザーの画面全体を覆うため、最も邪魔になります。大きくてリッチな画像を表示するのに最適で、重要な新機能や期限切れのプロモーションなど、非常に重要な情報を伝えるのに役立ちます。これらはユーザー エクスペリエンスを阻害する可能性があるため、最優先のコンテンツにのみ控えめに使用してください。

![Fullscreen Message]({% image_buster /assets/img_archive/braze_fullscreen.png %}){: style="max-width:80%;"}

**カスタマイズ可能な機能**

- ヘッダーと本文
- 大きな画像
- クリック時の挙動とディープリンクが異なる最大 2 つの CTA ボタン
- ヘッダーと本文、ボタンと背景に異なる色を使用する
- キーと値のペア

{% enddetails %}
{% details  Modal %}
これらのメッセージは、ユーザーがアプリの UI の一部を見ることができるため、全画面メッセージほど邪魔にはなりません。ボタンと画像が含まれているため、よりインタラクティブで視覚的なキャンペーンを希望する場合は、スライドアップよりもモーダル メッセージの方が適している可能性があります。これらは、アプリのアップデートや緊急ではない取引やイベントなど、優先度が中程度のコンテンツに最適です。

![Modal Message]({% image_buster /assets/img_archive/braze_modal.png %}){: style="max-width:80%;"}

**カスタマイズ可能な機能**

- ヘッダーと本文
- 画像またはカスタマイズ可能なバッジアイコン
- クリック時の挙動とディープリンクが異なる最大 2 つの CTA ボタン
- ヘッダーと本文、ボタンと背景に異なる色を使用する
- キーと値のペア

{% enddetails %}

{% details Traditional Slideup %}
これらは最も邪魔にならないメッセージ タイプですが、色やバッジ アイコンの使用方法によっては、注目を集める度合いが増したり減ったりすることがあります。これは、アプリのエクスペリエンスを一時停止せずに継続的に探索できるため、新しいユーザーをオンボーディングし、特定のアプリ内機能に誘導するときに使用するメッセージ形式である可能性があります。

![Slideup Message]({% image_buster /assets/img_archive/stopwatch_slideup_IAM.gif %}){: style="max-width:50%;"}

**カスタマイズ可能な機能**

- 本文
- 画像またはカスタマイズ可能なバッジアイコン
- スライドアップの背景、テキスト、アイコンに異なる色を使用する
- メッセージを閉じる動作
- スライドアップ位置（アプリ画面の上部または下部）
- キーと値のペア

{% enddetails %}

<br>

## Web

これにより、よりカスタマイズされたアプリ内メッセージに関する以前の情報が確認されます。現在のアプリ内メッセージ生成に関する最新情報を確認するには、 [カスタマイズに関するドキュメント]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/)をご覧ください。

{% details Email capture message %}
電子メール キャプチャ メッセージを使用すると、サイトのユーザーに電子メール アドレスの送信を簡単に促すことができます。送信された電子メール アドレスは、Braze システム内ですべてのメッセージング キャンペーンで使用できるようになります。

![Email capture message]({% image_buster /assets/img_archive/web-email-capture.png %}){: style="max-width:60%;"}

>  Web SDKを通じてアプリ内メッセージのメールキャプチャを有効にするには、 `allowUserSuppliedJavascript`Brazeの初期化オプションの例： `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`。これはセキュリティ上の理由です。HTML アプリ内メッセージは JavaScript を実行できるため、サイト管理者が JavaScript を有効にする必要があります。

**カスタマイズ可能な機能**

- ヘッダー、本文、送信ボタンのテキスト
- オプションの画像
- オプションの「利用規約」リンク
- ヘッダーと本文、ボタンと背景に異なる色を使用する
- キーと値のペア

{% enddetails %}

{% details Custom HTML Message %}

Braze のすぐに使用できるアプリ内メッセージはさまざまな方法でカスタマイズできますが、HTML、CSS、JavaScript を使用して設計および構築されたメッセージを使用すると、キャンペーンの外観と雰囲気をさらに細かく制御できます。簡単な構成で、あらゆるニーズに合わせてカスタム機能とブランディングを実現できます。HTML アプリ内メッセージを使用すると、メッセージの外観と操作性をより細かく制御できます。また、HTML5 でサポートされているものはすべて Braze でもサポートされています。

**JavaScript ブリッジ (appboyBridge)**

HTML アプリ内メッセージは、Braze Web SDK への JavaScript「ブリッジ」インターフェースをサポートしているため、ユーザーがリンクのある要素をクリックしたり、コンテンツに関与したりしたときに、カスタム Braze アクションをトリガーできます。Braze の HTML アプリ内メッセージでは、次の JavaScript メソッドがサポートされています。

{% multi_lang_include archive/appboyBridge.md platform="web" %}

さらに、分析トラッキングのために、 `<a>` または `<button>` HTML 内の要素により、アプリ内メッセージに関連付けられたキャンペーンへの「クリック」アクションが自動的に記録されます。「本体クリック」ではなく「ボタンクリック」を記録するには、リンクのhrefにabButtonIdのクエリ文字列値を指定します（例： `<a href="http://mysite.com?abButtonId=0">click me</a>`）、またはHTML要素にIDを指定します（例： `<a id="0" href="http://mysite.com">click me</a>`）。現在受け入れられるボタン ID は「0」と「1」のみであることに注意してください。 ボタン ID が 0 のリンクはダッシュボード上で「ボタン 1」として表され、ボタン ID が 1 のリンクは「ボタン 2」として表されます。

>  Web SDKを通じてHTMLアプリ内メッセージを有効にするには、 `allowUserSuppliedJavascript`Brazeの初期化オプション: 例えば `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`。これはセキュリティ上の理由です。HTML アプリ内メッセージは JavaScript を実行できるため、サイト管理者が JavaScript を有効にする必要があります。

{% enddetails %}

{% details HTML In App-Message Templates %}

すぐに使い始められるように、HTML5 アプリ内メッセージ テンプレートのセットを設計しました。これらのテンプレートの使用方法とニーズに合わせたカスタマイズ方法の詳細な手順が記載されている [GitHub リポジトリ](https://github.com/braze-inc/in-app-message-templates) をご覧ください。

**カスタマイズ可能な機能**

- フォント
- スタイル
- 画像 + 動画
- クリック時動作
- インタラクティブコンポーネント

{% enddetails %}

<br>

## 仕様

ここでは、アプリ内メッセージのクリエイティブ仕様に関する以前の情報を確認します。現在のアプリ内メッセージ生成に関する最新情報を確認するには、 [クリエイティブ仕様のドキュメント]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/)を参照してください。

### 文字数と画像の制限

次の表に記載されているすべてのアプリ内メッセージ タイプには、次の追加ガイドラインが適用されます。

- **推奨画像サイズ:**500 KB 
- **最大画像サイズ:** MB
- **サポートされているファイルの種類:**JPEG、GIF、JPEG形式

| タイプ | アスペクト比 | 最大文字数 |

| ポートレート全画面（画像のみ） | 10:16 | 240 |
| ポートレート全画面（テキストあり） | 5:4 | 240 |
| 横長全画面（テキストあり） | 16:5 | 240 |
| 横長全画面（画像のみ） | 16:10 | 240 |
| スライドアップ | 1:1 | 140 |
| モーダル (画像のみ) | 1:1 | 140 |
| モーダル (テキスト付き) | 29:10 | 140 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### アプリ内メッセージのファイルサイズを小さく保つ

Braze では、次のような理由から、画像と HTML アセットの zip ファイルをできるだけ小さく保つことを推奨しています。

- HTML および画像メッセージのペイロードが小さくなると、ダウンロードが高速化され、顧客にとってより迅速かつ確実に表示されます。
- HTML および画像メッセージのペイロードが小さくなると、顧客のデータ コストも削減されます。Braze アプリ内メッセージはセッション開始時にバックグラウンドでダウンロードされるため、選択した基準に基づいてリアルタイムでトリガーできます。その結果、1 MB の HTML アプリ内メッセージが 10 個ある場合、顧客がそれらのメッセージをすべてトリガーしなかったとしても、全員に 10 MB のデータ料金が発生します。アプリ内メッセージはキャッシュされ、セッションごとに再ダウンロードされない場合でも、時間の経過とともに急速に蓄積される可能性があります。

ファイル サイズを小さく保つには、次の戦略が役立ちます。

- HTML アセットの ZIP フォルダーにフォント ファイルを含めるのではなく、アプリケーションまたは Web サイトに埋め込まれたフォントを参照して、HTML アプリ内メッセージをカスタマイズします。
- HTML アセット ZIP に、無関係または重複した CSS や JavaScript が含まれていないことを確認します。
- すべての画像に [ImageOptim][25] を使用すると、品質を低下させることなく、画像を可能な限り最小のサイズに圧縮できます。

### iPhone 5の仕様

![iPhone 5の仕様][18]

### iPhone 6の仕様

![iPhone 6の仕様][19]


[18]: {% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_05.png %}

[19]: {% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_06.png %}

[25]: https://imageoptim.com/
