---
title: "Movable Ink"
article_title: Movable Ink
alias: "/partners/movable_ink/"
description: "このリファレンス記事では、Braze と Movable Ink のパートナーシップについて説明します。Movable Ink は、顧客に印象づける説得力のある独特なビジュアルエクスペリエンスを作成できるデジタルマーケターに提供するクラウドベースのソフトウェアプラットフォームです。"
page_type: partner
search_tag: Partner

---

# Movable Ink

> [Movable Ink](https://www.movableink.com/) は、顧客に印象づける説得力のある独特なビジュアルエクスペリエンスを作成できる手段をデジタルマーケターに提供するクラウドベースのソフトウェアプラットフォームです。Movable Ink プラットフォームは、キャンペーンに簡単に挿入できる有用なカスタマイズオプションを提供します。 

_この統合は Movable Ink によって管理されます。_

## 統合について

ポーリング、カウントダウンタイマー、スクラッチオフなど、Movable Ink の Intelligent Creative 機能を利用して Braze のクリエイティブ機能を拡大します。Movable Ink と Braze の統合により、動的なデータドリブン型メッセージへのよりバランスの取れたアプローチを可能にし、重要な事柄に関するリアルタイムの要素をユーザーに提供します。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Movable Ink アカウント | このパートナーシップを活用するには、Movable Ink アカウントが必要です。 |
| データソース | データソースを Movable Ink に接続する必要があります。これは、CSV、Web サイトインポート、または API を使用して実行できます。Braze と Movable Ink の間で統一 ID (`external_id` など) を使用してデータを渡していることを確認します。
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

- パーソナライズされた月ごとの要約または年末の要約。
- 直近の既知の動作に基づいて、メール、プッシュ、またはリッチプッシュ通知に使用される画像をダイナミックにパーソナライズします。<br>
	以下に例を示します。 
	- リッチプッシュメッセージを使用して、API からデータを取得してイベントのスケジュールを動的に作成します。 
	- 大規模なセール (ブラックフライデー、バレンタインデー、祝日セールなど) が近づいているときに、カウントダウンタイマーを使用してユーザーに通知します。
	- プロモーションコードを配信する楽しくインタラクティブな方法として、Scratch Off 機能を使用します。

## サポートされている Movable Ink の機能

Intelligent Creative には、Braze のユーザーが利用できる多くのサービスがあります。次のリストに、サポートされている機能を示します。 

| Movable Ink の機能 | 機能 | リッチプッシュ通知 | アプリ内メッセージ/コンテンツカード/メール | 詳細 |
| ---------------------- |---| ---------------------- | -------------------------------- | ------- |
| クリエイティブ・オプティマイザー | A/B コンテンツの表示 | ✗ | ✔ | |
|| 最適化 | ✗ | ✔* | \* Branch のディープリンクソリューションを使用する必要がある |
| ターゲティングルール | 日付 | ✔* | ✔ | \* プッシュ通知は受信時にキャッシュされ、更新されないため、サポートされますが推奨されません |
|| 曜日 | ✔* | ✔ | \* プッシュ通知は受信時にキャッシュされ、更新されないため、サポートされますが推奨されません |
|| 時刻 | ✔* | ✔ | \* プッシュ通知は受信時にキャッシュされ、更新されないため、サポートされますが推奨されません |
| ストーリー/行動アクティビティ | | ✔* | ✔* | \* Brazeに使用される一意のユーザー識別子を、メールサービスプロバイダー (ESP) にリンクする必要がある |
| アプリ内のディープリンク | | ✔* | ✔* | \* 顧客に効率化されたエクスペリエンスを提供するには、Branch で確立されたディープリンクソリューションを使用するか、Movable Ink のクライアントエクスペリエンスチェンジチームによる検証済みソリューションを使用します。 |
| アプリ | カウントダウンタイマ | ✔* | ✔ | \* プッシュ通知は受信時にキャッシュされ、更新されないため、サポートされますが推奨されません |
|| ポーリング | ✗ | ✔* | \* 投票後、アプリを移動式ランディングページに残す |
|| スクラッチオフ | ✔* | ✔* | \* クリックすると、スクラッチオフエクスペリエンスのためにアプリが終了する |
|| 動画 | ✔* | ✔* | \* アニメーションGIF のみ。<br>Androidの場合、Brazeの実装には[GIFサポート]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs/)が必要です |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 統合

### ステップ1:Movable Inkのデータソースの作成

顧客は、CSV、Web サイトのインポート、または API統合である可能性のあるデータソースを作成する必要があります。

![表示されるさまざまなデータソースオプション:CSV アップ読み込む、Webサイト、またはAPI 統合。]({% image_buster /assets/img/movable_ink/movable_ink1.png %})

{% tabs local %}
{% tab CSV Data Source %}
- **CSV データソース**:各行には、少なくとも1つのSegment列と1つの内容列が必要です。CSV がアップロードされた後、コンテンツのターゲットとして使用する列を選択します。[CSV ファイルの例]]({% image_buster /assets/download_file/movable_ink_CSV.csv %})

!["CSV"をデータソースとして選択したときに表示されるフィールドs。]({% image_buster /assets/img/movable_ink/movable_ink2.png %})
{% endtab %}
{% tab Website Data Source %}
- **Web サイトデータソース**:各行には、少なくとも1つのSegment列と1つの内容列が必要です。CSV がアップロードされたら、コンテンツのターゲットを設定するために使用する列を選択します。
  - このプロセスでは、以下をマップする必要があります。
    - セグメントとして使用されるフィールドs
    - クリエイティブで動的にパーソナライズできるデータフィールドとして使用する項目(たとえば、ユーザー属性や名、姓、市区町村などのカスタム属性)

![データソースとして" Web site" を選択すると表示されるフィールドs。]({% image_buster /assets/img/movable_ink/movable_ink3.png %})
{% endtab %}
{% tab API Integrations %}
- **API 統合**:自社の API を使用して、API レスポンスから直接ココンテンツを供給します。

!["API Integration"をデータソースとして選択すると表示されるフィールドs]({% image_buster /assets/img/movable_ink/movable_ink4.png %})
{% endtab %}
{% endtabs %}

### ステップ2:Movable Ink プラットフォームでのキャンペーンの作成

Movable Inkのホームスクリーンから、キャンペーンを作成します。HTML からのメールの開始、画像からのメールの開始、または任意のチャネルで使用できるブロックの作成 (プッシュ、アプリ内メッセージ、コンテンツカード(推奨) など) のいずれかを選択できます。

また、ブロックを通じて利用できるさまざまなコンテンツオプションを確認することもお勧めします。

![新しいMovable Ink キャンペーンを作成するときのMovable Ink プラットフォームの外観の"画像。]({% image_buster /assets/img/movable_ink/movable_ink5.png %}){: style="max-width:70%"}

Movable Ink には、テキストまたは画像のような要素をドラッグアンドドロップできる簡単なエディターがあります。データソースを入力した場合は、データプロパティを使用して画像をダイナミックに生成できます。また、このフロー内に、ユーザーs のフォールバックs を作成することもできます。これは、キャンペーンが送信され、ユーザーがパーソナライゼーション基準内に収まらない場合です。

![Movable Ink ブロックエディタには、カスタマイズ可能なさまざまな要素が表示されます。]({% image_buster /assets/img/movable_ink/create_campaign2.png %})

キャンペーンを終了する前に、ダイナミックな画像をプレビューし、クエリパラメーターを試してビューで画像がどのように表示されるかを確認してください。完了すると、Braze に挿入できる動的なURL が生成されます。

Movable Ink プラットフォームの使用方法の詳細については、[Movable Ink サポートセンター](https://support.movableink.com/)を参照してください。

### ステップ 3: Movable Ink コンテンツ URL を取得する

Movable Ink のコンテンツを Braze メッセージに含めるには、Movable Ink から提供されたソース URL を確認する必要があります。 

ソース URL を取得するには、Movable Ink ダッシュボードでコンテンツを設定し、完了してコンテンツをエクスポートする必要があります。**Finish**ページで、ソースURL(`img src`)をクリエイティブタグからコピーします。

![Movable Ink キャンペーンを完了するとアプリが表示されるページで、ここにコンテンツURL が表示されます。]({% image_buster /assets/img/movable_ink/obtain_url.png %}){: style="max-width:80%;"}

次に Braze プラットフォームで、URL を該当するフィールドに貼り付けます。メッセージングチャネルに適したフィールドは、4ステップに記載されています。最後に、マージタグ ({% raw %}```&mi_u=%%email%%```{% endraw %} など) を対応するLiquid 変数 ({% raw %}```&mi_u={{${email_address}}}```{% endraw %} など) に置き換えます。

### ステップ4:Braze体験

{% tabs local %}
{% tab Email %}
Braze プラットフォームで、クリエイティブなタグをメール本文に貼り付けます。![]({% image_buster /assets/img/movable_ink/web2.png %}){: style="max-width:90%"}<br><br>

{% endtab %}
{% tab Push notification %}

1. Braze プラットフォームの場合:
	- Android プッシュ:**プッシュアイコン画像**と**拡張通知画像**フィールドにURLを貼り付けます。<br>![]({% image_buster /assets/img/movable_ink/android.png %}){: style="max-width:60%"}<br><br>
	- iOS プッシュ**Media**リンクフィールドにURLを貼り付け、使用しているファイル形式を示します。<br>![]({% image_buster /assets/img/movable_ink/ios.png %}){: style="max-width:60%"}<br><br>
	- Web プッシュURL を [**プッシュ通知アイコンの画像**] と [**大きな通知画像**] フィールドに貼り付けます。<br>![]({% image_buster /assets/img/movable_ink/web.png %}){: style="max-width:60%"}<br><br>
2. 画像がキャッシュされないようにするため、メッセージの URL の先頭に空の Liquid タグを追加します。<br>{% raw %}```{% if true %}{% endif %}https://movable-ink-image-url-goes-here```{% endraw %}

{% endtab %}
{% tab In-app message %}

1. Braze プラットフォームで、**リッチ通知メディア**フィールドにURLを貼り付けます。![]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. キャッシュの防止に役立つ一意のURL を指定します。Movable Ink のリアルタイム画像が機能し、キャッシュの影響を受けないようにするため、Liquid を使用して、Movable Ink 画像 URL の末尾にタイムスタンプを付加します。

これを行うには、次の構文を使用します。必要に応じて画像 URL を置き換えます。
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
このテンプレートは、現在の時刻 (秒単位) を取得し、それを Movable Ink 画像タブの終わりに (クエリパラメーターとして) 付加し、最終結果を出力します。**Test**タブでプレビューできます。これにより、コードが評価され、プレビューが表示されます。

**3\.**最後に、セグメントのメンバーシップを再評価します。これを行うには、キャンペーンの**Target Audiences**ステップにある`Re-evaluate audience membership and liquid at send-time`を有効にします。この項目を選択できない場合は、顧客サクセスマネージャーまたはBrazeサポートにお問い合わせください。このオプションは、アプリ内メッセージがトリガーされるたびに、一意の URL を指定してキャンペーンを再要求するように Braze SDK に指示します。

{% endtab %}
{% tab Content Card %}

1. Braze プラットフォームで、**リッチ通知メディア**フィールドにURLを貼り付けます。![]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. モバイル:iOS および Android のコンテンツカードの画像は、受信時にキャッシュされ、更新されません。 
  - 回避策として、キャンペーンを毎日、毎週、または毎月の定期的なメッセージとしてスケジュールし、対応する有効期限を設定します。これにより、コンテンツカードが再テンプレート化されます。たとえば、1日に1回更新する必要があるコンテンツカードは、有効期間が1日に設定された毎日のスケジュール送信として設定する必要があります。
3. コンテンツカードが再テンプレート化されたときに、Movable Ink のリアルタイム画像が機能し、キャッシュの影響を受けないようにするため、Liquid を使用して、Movable Ink 画像 URL の末尾にタイムスタンプを付加します。

これを行うには、次の構文を使用します。必要に応じて画像 URL を置き換えます。
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
このテンプレートは、現在の時刻 (秒単位) を取得し、それを Movable Ink 画像タブの終わりに (クエリパラメーターとして) 付加し、最終結果を出力します。**Test**タブでプレビューできます。これにより、コードが評価され、プレビューが表示されます。

{% endtab %}
{% endtabs %}

## トラブルシューティング

### 動的画像が正しく表示されませんか?どんなチャネルで苦労していますか？
- **プッシュ通知**Movable Ink 画像 URL の前に空のロジックがあることを確認します。<br>{% raw %}```{% if true %}{% endif %}https://movable-ink-image-url-goes-here```{% endraw %}
- **アプリ内メッセージとコンテンツカード**:画像 URL がインプレッションごとに一意であることを確認します。このためには、各URL が異なる URL になるように適切な Liquid を追加します。[アプリ内メッセージおよびコンテンツカードメッセージの手順]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/movable_ink/#step-4-braze-experience)を参照してください。 
- **画像が読み込まれない**:Braze ダッシュボードで、すべての「マージタグ」を対応する Liquid フィールドに必ず置き換えてください。たとえば、{% raw %}```https://mi-msg.com/p/rp/image.png?mi_u=%%email%%```{% endraw %} を {% raw %}```https://mi-msg.com/p/rp/image.png?mi_u={{${email_address}}}```{% endraw %} に置き換えます。

### Android で GIF を表示するときに問題がありますか?
- Androidには、実施にあたってGIFの支援が必要である。この設定がない場合は、Android の[アプリ内メッセージカスタマイズ]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs/)の記事に従います。


[1]: https://www.movableink.com/
[datasource]: ({% image_buster /assets/img/movable_ink/movable_ink1.png %})
[1]: ({% image_buster /assets/img/movable_ink/android.png %})
[2]: ({% image_buster /assets/img/movable_ink/ios.png %})
[3]: ({% image_buster /assets/img/movable_ink/web.png %})
