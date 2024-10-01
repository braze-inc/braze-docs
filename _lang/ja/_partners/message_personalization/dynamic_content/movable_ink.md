---
title: "Movable Ink"
article_title: Movable Ink
alias: "/partners/movable_ink/"
description: "このレファレンス記事では、顧客を動かす説得力のある独特な視覚体験を生み出す方法をデジタルマーケターに提供するクラウドベースのソフトウェアプラットフォームであるBrazeとMovable Inkの提携について概説します。"
page_type: partner
search_tag: Partner

---

# Movable Ink

> [Movable Ink](https://www.movableink.com/) は、デジタルマーケターを提供するクラウドベースのソフトウェアプラットフォームで、顧客を動かす説得力のある独特な視覚体験を創り出す方法を提供します。Movable Ink プラットフォームには、キャンペーンsに簡単に挿入できる貴重なカスタマイズ機能が用意されています。 

ポーリング、カウントダウンタイマー、スクラッチオフなど、Movable Inkのインテリジェント・クリエイティブ機能を活用して、当社のクリエイティブ能力を拡大します。Movable InkとBrazeインテグレーションは、より丸みのあるアプリを駆使して、ダイナミックな データドリブン型のな情報を提供し、問題の内容に関するリアルタイムの要素をユーザーに提供します。

## 前提条件

| 要件 | 説明 |
|---|---|
| Movable Ink勘定 | この提携の前進タグeを考慮するには、Movable Inkな考慮が必要である。 |
| データソース | データソースをMovable Inkに接続する必要があります。これは、CSV、Web サイト読み込み、またはAPI を使用して実行できます。Braze とMovable Ink の間で統一識別子を使用してデータを渡していることを確認します(たとえば、`external_id`)。
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

- 月ごとまたは年末の個別の再利用。
- 最新の既知の動作に基づいて、メール、プッシュ、またはリッチプッシュ通知s の"画像を動的にパーソナライズします。<br>
	以下に例を示します。 
	- リッチプッシュ メッセージを使用してダイナミックなall は、API からデータをプルすることでイベントのスケジュールを作成します。 
	- カウントダウンタイマーを使用して、大規模なセールがアプリ侵入したときにユーザーs に通知する(たとえば、ブラックフライデー、バレンタインデー、またはホリデーの案件)
	- スクラッチオフ機能は、プロモーションコードを支払うための楽しくインタラクティブな方法として使用します。

## サポートされるMovable Ink機能

インテリジェント・クリエイティブには、Braze ユーザーsがeのタグを進めることができる多くの提供物があります。次のリストは、サポートされる機能を示しています。 

| Movable Ink機能 | 機能 | リッチプッシュ通知 | アプリ内メッセージ/コンテンツカード/メール | 詳細 |
| ---------------------- |---| ---------------------- | -------------------------------- | ------- |
| クリエイティブ・オプティマイザー | ディスプレイA/B の内容 | ✗ | ✔ | |
|| 最適化 | ✗ | ✔* | \* Branchのディープリンクソリューションを使用する必要がある |
| ターゲティングルール | 日付 | ✔* | ✔ | \* プッシュ通知は受信時にキャッシュされ、更新されないため、サポートされますが推奨されません |
|| 曜日 | ✔* | ✔ | \* プッシュ通知は受信時にキャッシュされ、更新されないため、サポートされますが推奨されません |
|| 時刻 | ✔* | ✔ | \* プッシュ通知は受信時にキャッシュされ、更新されないため、サポートされますが推奨されません |
| ストーリー/ビヘイビア活動 | | ✔* | ✔* | \* Brazeに使用する一意のユーザー 識別子は、メールサービスプロバイダー (ESP)の識別子にリンクする必要があります |
| アプリ内のディープリンク | | ✔* | ✔* | \* 顧客 s に効率的なエクスペリエンスを提供するには、Branch で確立されたディープリンク ソリューションを使用するか、Movable Ink のクライアントエクスペリエンスチェンジチームとの検証済みソリューションを使用します。 |
| アプリ | カウントダウンタイマ | ✔* | ✔ | \* プッシュ通知は受信時にキャッシュされ、更新されないため、サポートされますが推奨されません |
|| ポーリング | ✗ | ✔* | \* 投票後、アプリを移動式ランディングページに残す |
|| スクラッチオフ | ✔* | ✔* | \* クリックすると、スクラッチオフエクスペリエンスのアプリが終了します |
|| 動画 | ✔* | ✔* | \* アニメーションGIFのみ、<br>Android の場合、Braze はインプリメンテーションで\[GIF support]\[GIF support] を必要とします |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 統合

### ステップ1:Movable Inkのデータソースの作成

顧客は、CSV、Web サイトインポート、またはAPI インテグレーションのいずれかになるデータソースを作成する必要があります。

![耳にアプリを与えるさまざまなデータソース方法:CSV アップ読み込む、Web サイト、またはAPI 統合。]({% image_buster /assets/img/movable_ink/movable_ink1.png %})

{% tabs ローカル %}
{% tab CSVデータソース %}
- **CSV データソース**:各行には、少なくとも1つのSegment列と1つの内容列が必要です。CSV がアップロードされたら、コンテンツをターゲットにする列を選択します。\[例: CSV ファイル]({% image_buster /assets/download_file/movable_ink_CSV.csv %})

!["CSV" を選択したときに表示されるフィールドs。データソースとして使用します。]({% image_buster /assets/img/movable_ink/movable_ink2.png %})
{% endtab %}
{% tab Web拠点データソース %}
- **Webサイトデータソース**:各行には、少なくとも1つのSegment列と1つの内容列が必要です。CSV がアップロードされたら、内容を対象とする列を選択します。
  - このプロセスでは、以下をマップする必要があります。
    - セグメントとして使用されるフィールドs
    - クリエイティブ(例:名、姓、都市などのユーザー 属性 s またはカスタム属性 s)でダイナミックな的にパーソナライズされた可能なデータフィールドs として使用するフィールド

![" Web site" を選択すると表示されるフィールドs は、データソースとして表示されます。]({% image_buster /assets/img/movable_ink/movable_ink3.png %})
{% endtab %}
{% tab API 統合 %}
- **API 統合**:API レスポンスから直接コンテンツに電力を供給するには、会社のAPI を使用します。

!["API Integration" を選択すると、データソース] ({% image_buster /assets/img/movable_ink/movable_ink4.png %}) として表示されるフィールドs
{% endtab %}
{% endtabs %}

### ステップ2:Movable Ink プラットフォームでのキャンペーンの作成

Movable Inkのホームスクリーンから、キャンペーンを作成します。HTMLからのメール、"画像からのメール、またはプッシュ、アプリ内メッセージ、コンテンツカード(推奨)など、任意のチャネルで使用できるブロックから選択できます。
また、ブロック s で利用可能なさまざまなコンテンツオプションを確認することもお勧めします。

![新しいMovable Ink キャンペーン.]({% image_buster /assets/img/movable_ink/movable_ink5.png %})を作成したときのMovable Ink プラットフォームの"画像{: style="max-width:70%"}

Movable Ink には、文字や"画像などの要素をドラッグ＆ドロップするためのエディタが用意されています。データソースを入力した場合は、データプロパティを使用して"画像をダイナミックな生成できます。また、このフロー内に、ユーザーs のフォールバックs を作成することもできます。これは、キャンペーンが送信され、ユーザーがパーソナライゼーション基準内に収まらない場合です。

![さまざまなカスタマイズ可能な要素を表示するMovable Ink ブロックエディタ。]({% image_buster /assets/img/movable_ink/create_campaign2.png %})

キャンペーンを終了する前に、ダイナミックな "画像s をプレビューし、クエリーパラメータをテストして、"画像s がビューでどのように表示されるかを確認してください。完了すると、ダイナミックな URLが生成され、Brazeに挿入できるようになります。

Movable Ink プラットフォームの使用方法の詳細については、\[Movable Ink サポートセンター][サポートを参照してください]

### ステップ 3:Movable InkコンテンツURLを取得する

Movable Inkの内容をBrazeメッセージに含めるには、入力した送信元URL Movable Inkを見つける必要があります。 

ソースURL を取得するには、Movable Ink ダッシュボードでコンテンツを設定し、そこからコンテンツを終了してエクスポートする必要があります。**Finish**ページで、ソースURL(`img src`)をクリエイティブタグからコピーします。

![Movable Ink キャンペーンを完了した後にアプリが表示されるページは、コンテンツURL.]({% image_buster /assets/img/movable_ink/obtain_url.png %})が表示されます。{: style="max-width:80%;"}

次に、Braze プラットフォームで、アプリの適切なフィールドにURL を貼り付けます。メッセージング チャネルに適したフィールドは、第4ステップに記載されています。最後に、マージタグs ({% raw %}```&mi_u=%%email%%```{% endraw %} など) を対応するLiquid 変数({% raw %}```&mi_u={{${email_address}}}```{% endraw %} など) に置き換えます。

### ステップ4:Braze体験

{% tabs ローカル %}
{% tab メール %}
Braze プラットフォームで、クリエイティブなタグをメール本文に貼り付けます。![]({% image_buster /assets/img/movable_ink/web2.png %}){: style="max-width:90%"}<br><br>

{% endtab %}
プッシュ通知

1. Braze プラットフォームの場合:
	- Androidプッシュ:**プッシュアイコン画像**と**拡張通知画像**フィールドにURLを貼り付けます。<br>![]({% image_buster /assets/img/movable_ink/android.png %}){: style="max-width:60%"}<br><br>
	- iOS プッシュ**Media**リンクフィールドにURLを貼り付け、使用しているファイル形式を示します。<br>![]({% image_buster /assets/img/movable_ink/ios.png %}){: style="max-width:60%"}<br><br>
	- Web プッシュURL を** Push Icon Image** と** Large Notification Image** フィールドに貼り付けます。<br>![]({% image_buster /assets/img/movable_ink/web.png %}){: style="max-width:60%"}<br><br>
2. "画像がキャッシュされないようにするには、メッセージの先頭に空のリキッドタグs を追加します。<br>{% raw %}```{% if true %}{% endif %}https://movable-ink-image-url-goes-here```{% endraw %}

{% endtab %}
{% tab アプリ中電文 %}

1. Braze プラットフォームで、**リッチ通知メディア**フィールド.![]({% image_buster /assets/img/movable_ink/image.png %})にURLを貼り付けます。{: style="max-width:60%"}<br><br>
2. キャッシュの防止に役立つ一意のURL を指定します。Movable Ink のリアルタイム"画像が機能し、キャッシュの影響を受けないことを確認するには、リキッドを使用して、Movable Ink "画像 URL の最後までタイムスタンプをアプリ終了します。

これを行うには、次のシンタックスを使用し、必要に応じて"画像のURL を置き換えます。
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
このテンプレートは、現在の時刻(秒単位)を取得し、それをMovable Ink "画像タブの最後までアプリし(クエリーパラメータとして)、最後の結果を出力します。**Test**タブでプレビューできます。これにより、コードが評価され、プレビューが表示されます。

**3\.**最後に、Segmentメンバーシップを再評価します。これを行うには、キャンペーンの**Target Audiences**ステップにある`Re-evaluate audience membership and liquid at send-time`を有効にします。この項目を選択できない場合は、顧客のサクセスマネージャーまたはBrazeサポートに連絡してください。アプリ内メッセージがトリガーされるたびに一意のURLを提供するキャンペーンを再要求するようにBraze SDKsに指示します。

{% endtab %}
{% tab Content Card %}

1. Braze プラットフォームで、**リッチ通知メディア**フィールド.![]({% image_buster /assets/img/movable_ink/image.png %})にURLを貼り付けます。{: style="max-width:60%"}<br><br>
2. モバイル:iOSおよびAndroidのコンテンツカード"画像は、受信時にキャッシュされ、更新されません。 
  - 回避策として、キャンペーンを毎日、毎週、または毎月の定期的なメッセージとしてスケジュールし、対応する有効期限を設定すると、コンテンツカードが再テンプレートされます。たとえば、1 日に1 回更新するコンテンツカードは、1 日の有効期限を持つ1 日のスケジュールされた送信として設定する必要があります。
3. Movable Ink のリアルタイム"画像が機能し、コンテンツカードが再テンプレートされたときにキャッシュの影響を受けないようにするには、リキッドを使用してMovable Ink "画像 URL の最後までタイムスタンプをアプリ終了します。

これを行うには、次のシンタックスを使用し、必要に応じて"画像のURL を置き換えます。
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
このテンプレートは、現在の時刻(秒単位)を取得し、それをMovable Ink "画像タブの最後までアプリし(クエリーパラメータとして)、最後の結果を出力します。**Test**タブでプレビューできます。これにより、コードが評価され、プレビューが表示されます。

{% endtab %}
{% endtabs %}

## トラブルシューティング

### ダイナミック"画像が正しく表示されない。どんなチャネルで苦労していますか？
- **プッシュ通知**Movable Ink "画像 URL の前に、空のロジックがあることを確認します。<br>{% raw %}```{% if true %}{% endif %}https://movable-ink-image-url-goes-here```{% endraw %}
- **In-アプリとコンテンツカード**:"画像 URL がインプレッションごとに一意であることを確認します。これは、それぞれのURL が違うように、アプリの適切なリキッドを終了することによって行うことができます。\[in-アプリ and コンテンツカード messages instructions]\[instructions]]を参照してください。 
- **イメージが読み込むしない**:"merge タグ s"は、必ずBraze ダッシュボードの対応するLiquid フィールドs に置き換えてください。例: {% raw %}```https://mi-msg.com/p/rp/image.png?mi_u=%%email%%```{% endraw %} {% raw %}```https://mi-msg.com/p/rp/image.png?mi_u={{${email_address}}}```{% endraw %}。

### AndroidでGIFを表示するのに問題がありますか?
- Androidには、実施にあたってGIFの支援が必要である。この設定がない場合は、Android[アプリ内メッセージ customization][GIFsupport] 記事に従ってください。

[1]: https://www.movableink.com/
[datasource]: ({% image_buster /assets/img/movable_ink/movable_ink1.png %})
[support]: https://support.movableink.com/
[GIFsupport]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs/
[Instructions]: {{site.baseurl}}/partners/message_personalization/dynamic_content/movable_ink/#step-4-braze-experience
[1]: ({% image_buster /assets/img/movable_ink/android.png %})
[2]: ({% image_buster /assets/img/movable_ink/ios.png %})
[3]: ({% image_buster /assets/img/movable_ink/web.png %})