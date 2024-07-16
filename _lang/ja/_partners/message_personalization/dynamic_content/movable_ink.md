---
title: "Movable Ink"
article_title:Movable Ink
alias: 「/partners/movable_ink/"
description:「この参考記事では、BrazeとMovable Inkのパートナーシップについて概説しています。Movable Inkは、デジタルマーケティング担当者に、顧客を感動させる魅力的でユニークなビジュアル体験を生み出す方法を提供するクラウドベースのソフトウェアプラットフォームです。「
page_type: partner
search_tag:Partner

---

# Movable Ink

> [Movable Inkはクラウドベースのソフトウェアプラットフォームで](https://www.movableink.com/)、デジタルマーケティング担当者が顧客を感動させる魅力的でユニークなビジュアル体験を作成する方法を提供します。Movable Inkプラットフォームには、キャンペーンに簡単に挿入できる貴重なカスタマイズオプションが用意されています。 

ポーリング、カウントダウンタイマー、スクラッチオフなどのMovable Inkのインテリジェントクリエイティブ機能を活用して、クリエイティブ機能を拡張してください。Movable InkとBrazeの統合により、データドリブン型のダイナミックなメッセージへのより包括的なアプローチが強化され、重要なことに関するリアルタイムの要素をユーザーに提供できます。

## 前提条件

| 必要条件 | 説明 |
|---|---|
|  | このパートナーシップを利用するには、Movable Inkアカウントが必要です。 |
| データソース | データソースを Movable Ink に接続する必要があります。これは、CSV、Web サイトインポート、またはAPIを使用して実行できます。Braze と Movable Ink 間の統一識別子 (例:) を使用してデータを渡すようにしてください。`external_id`
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース
- パーソナライズされた月次または年末のまとめ。
- 前回の既知の動作に基づいて、電子メール、プッシュ、またはリッチ通知用の画像を動的にパーソナライズします。<br>
	例えば: 
	- リッチプッシュメッセージを使用して、API からデータを取得してイベントスケジュールを動的に作成します。 
	- カウントダウンタイマー機能を使用して、大きなセール（ブラックフライデー、バレンタインデー、ホリデーセールなど）が近づいたときにユーザーに通知します。
	- スクラッチオフ機能を楽しくインタラクティブな方法でプロモコードをお支払いください。

## 対応しているムーバブルインク機能

インテリジェントクリエイティブには、Brazeユーザーが利用できる多くのサービスがあります。次のリストは、サポートされている機能を示しています。 

|  | 機能 | リッチプッシュ通知 | アプリ内メッセージング / Content Cards / Email | 詳細 |
| ---------------------- |---| ---------------------- | -------------------------------- | ------- |
| クリエイティブオプティマイザー | A/B コンテンツを表示 | ✗ | ✔ | |
|| 最適化 | ✗ | ✔ \* | \* Branchのディープリンクソリューションを使用する必要があります |
| ターゲットルール | 日付 | ✔ \* | ✔ | \* プッシュ通知は受信時にキャッシュされ、更新されないため、サポートされていますが、推奨されません |
|| 曜日・オブ・ウィーク | ✔ \* | ✔ | \* プッシュ通知は受信時にキャッシュされ、更新されないため、サポートされていますが、推奨されません |
|| 時間帯 | ✔ \* | ✔ | \* プッシュ通知は受信時にキャッシュされ、更新されないため、サポートされていますが、推奨されません |
| ストーリー/行動活動 | | ✔ \* | ✔ \* | \* Brazeに使用する固有のユーザー識別子は、ESPの識別子にリンクする必要があります |
| アプリ内のディープリンク | | ✔ \* | ✔ \* | \* 顧客に効率的なエクスペリエンスを提供するには、Branch経由で確立されたディープリンクソリューションを使用するか、Movable Inkのクライアントエクスペリエンスチームによる検証済みのソリューションを使用してください。 |
| アプリ | カウントダウンタイマー | ✔ \* | ✔ | \* プッシュ通知は受信時にキャッシュされ、更新されないため、サポートされていますが、推奨されません |
|| ポーリング | ✗ | ✔ \* | \*投票後、アプリモバイルランディングページのままになります |
|| スクラッチオフ | ✔ \* | ✔ \* | \*クリックすると、アプリが終了してスクラッチオフエクスペリエンスに移行します |
|| 動画 | ✔ \* | ✔ \* | \* アニメーション GIF のみ<br>Android版の場合、Brazeの実装には \[GIFサポート] \[GIFサポート] が必要です |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 統合

### ステップ1:ムーバブルインクのデータソースを作成する

お客様は、CSV、Web サイトインポート、またはAPI統合のいずれかのデータソースを作成する必要があります。

![Different data source options that will appear: CSV Upload, Website, or API Integration.]({% image_buster /assets/img/movable_ink/movable_ink1.png %})

{% tabs local %}
{% tab CSV Data Source %}
- **CSV データソース**:各行には、少なくとも 1 つのSegment 列と 1 つのコンテンツ列が必要です。CSV をアップロードしたら、コンテンツのターゲットとして使用する列を選択します。\[CSV ファイルの例] ({% image_buster /assets/download_file/movable_ink_CSV.csv %})

![The fields that will show up when selecting "CSV" as your data source.]({% image_buster /assets/img/movable_ink/movable_ink2.png %})
{% endtab %}
{% tab Website Data Source %}
- **Web サイトデータソース**:各行には、少なくとも 1 つのSegment 列と 1 つのコンテンツ列が必要です。CSV をアップロードしたら、コンテンツのターゲットとして使用する列を選択します。
  - このプロセスでは、以下をマッピングする必要があります。
    - どのフィールドをセグメントとして使用するのか
    - クリエイティブで動的にパーソナライズされたできるデータフィールドとしてどのフィールドが必要か（例：ユーザー属性または名前、姓、都市などのカスタム属性）

![The fields that will show up when selecting "Website" as your data source.]({% image_buster /assets/img/movable_ink/movable_ink3.png %})
{% endtab %}
{% tab API Integrations %}
- **API インテグレーション**:会社の API を使用して、API レスポンスからコンテンツを直接生成します。

![The fields that will show up when selecting "API Integration" as your data source]({% image_buster /assets/img/movable_ink/movable_ink4.png %})
{% endtab %}
{% endtabs %}

### ステップ2:Movable Ink プラットフォームキャンペーンを作成する

Movable Ink のホーム画面から、キャンペーンを作成します。HTMLからのメール、画像, 写真からのメール、またはプッシュ、アプリ内メッセージ、コンテンツカード（推奨）を含む任意のチャネルで使用できるブロックから選択できます。
また、ブロックを通じて利用できるさまざまなコンテンツオプションを確認することをお勧めします。

![An image of what the Movable Ink platform looks like when creating a new Movable Ink campaign.]({% image_buster /assets/img/movable_ink/movable_ink5.png %}){: style="max-width:70%"}

Movable Inkには、テキストや画像, 写真などの要素をドラッグアンドドロップできる簡単なエディターがあります。データソースにデータを入力したら、データプロパティを使用して画像, 写真動的に生成できます。さらに、キャンペーンが送信されたのにユーザーがパーソナライゼーション基準に合わない場合に、このフロー内でユーザー用のフォールバックを作成することもできます。

![The Movable Ink block editor showing the different customizable elements.]({% image_buster /assets/img/movable_ink/create_campaign2.png %})

キャンペーンを終了する前に、必ずダイナミックな画像をプレビューし、クエリパラメータをテストして、画像が表示されたときにどのように表示されるかを確認してください。完了すると、ダイナミックな URLが生成され、Braze! に挿入できます。

Movable Ink Platformの使用方法の詳細については、\[Movable Inkサポートセンター] \[support] をご覧ください。

### ステップ3:ムーバブルインクのコンテンツ URL を取得

Movable InkのコンテンツをBrazeメッセージに含めるには、Movable Inkから提供されたソースURLを見つける必要があります。 

ソース URL を取得するには、Movable Ink ダッシュボードでコンテンツを設定し、そこからコンテンツを完成させてエクスポートする必要があります。「**完了**」ページで、クリエイティブタグからソース URL (`img src`) をコピーします。

![The page that appears after you have completed your Movable Ink campaign, here you find your content URL.]({% image_buster /assets/img/movable_ink/obtain_url.png %}){: style="max-width:80%;"}

次に、Braze プラットフォームで、適切なフィールドに URL を貼り付けます。メッセージングチャネルに適したフィールドは、ステップ 4 にあります。最後に、マージタグ (など {% raw %} ```&mi_u=%%email%%```{% endraw %}) を対応するLiquid変数 (など {% raw %} ```&mi_u={{${email_address}}}```{% endraw %}) に置き換えます。

### ステップ 4:Braze エクスペリエンス

{% tabs local %}
{% tab Email %}
Braze プラットフォームで、クリエイティブタグをメール本文に貼り付けます。![] ({% image_buster /assets/img/movable_ink/web2.png %}){: style="max-width:90%"}<br><br>

{% endtab %}
{% tab Push notification %}

1. Braze プラットフォームでは:
	- Android プッシュ:URL を **\[プッシュアイコンイメージ]** フィールドと \[**拡張通知イメージ**] フィールドに貼り付けます。<br>![] ({% image_buster /assets/img/movable_ink/android.png %}){: style="max-width:60%"}<br><br>
	- iOS プッシュ:**メディアリンクフィールド** URLを貼り付け、使用しているファイル形式を指定します。<br>![] ({% image_buster /assets/img/movable_ink/ios.png %}){: style="max-width:60%"}<br><br>
	- Web プッシュ:URL を **\[プッシュアイコンイメージ]** フィールドと \[**大きい通知イメージ**] フィールドに貼り付けます。<br>![] ({% image_buster /assets/img/movable_ink/web.png %}){: style="max-width:60%"}<br><br>
2. 画像がキャッシュされないようにするには、メッセージ内の URL に空の Liquid タグを付けてください。<br>{% raw %}```{% if true %}{% endif %}https://movable-ink-image-url-goes-here```{% endraw %}

{% endtab %}
{% tab In-app message %}

1. Braze プラットフォームで、URL **をリッチ通知メディアフィールド**貼り付けます。![] ({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. キャッシュを防ぐのに役立つ一意の URL を指定してください。Movable Ink のリアルタイム画像, 写真が機能し、キャッシュの影響を受けないことを確認するには、Liquid を使用して Movable Ink 画像 URL の末尾にタイムスタンプを追加します。

これを行うには、次の構文を使用し、必要に応じて画像, 写真の URL を置き換えます。
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
このテンプレートは現在の時間 (秒単位) を取得し、それをMovable Ink画像, 写真タブの末尾に (クエリパラメータとして) 追加し、最終結果を出力します。**テストタブでプレビューできます**。これによりコードが評価され、プレビューが表示されます。

**3\.**最後に、Segment メンバーシップを再評価してください。これを行うには、キャンペーンの「**ターゲットオーディエンス**」`Re-evaluate audience membership and liquid at send-time` ステップにあるオプションを有効にします。このオプションが利用できない場合は、顧客サクセスマネージャーまたは Braze サポートに連絡してください。このオプションは、アプリ内メッセージトリガーされるたびに固有のURLを指定してキャンペーンを再リクエストするようにBraze SDKに指示します。

{% endtab %}
{% tab Content Card %}

1. Braze プラットフォームで、URL **をリッチ通知メディアフィールド**貼り付けます。![] ({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. モバイル用:iOS と Android のコンテンツカード画像は受信時にキャッシュされ、更新されません。 
  - 回避策として、キャンペーンを毎日、毎週、または毎月の定期的なメッセージとしてスケジュールし、対応する有効期限を設定して、コンテンツカードを再テンプレート化します。たとえば、1 日に 1 回更新する必要があるコンテンツカードは、有効期限が 1 日の日次スケジュールされた送信として設定する必要があります。
3. Movable Inkのリアルタイム画像, 写真が機能し、コンテンツカードを再テンプレート化してもキャッシュの影響を受けないようにするには、Liquidを使用してMovable Ink画像URLの末尾にタイムスタンプを追加します。

これを行うには、次の構文を使用し、必要に応じて画像, 写真の URL を置き換えます。
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
このテンプレートは現在の時間 (秒単位) を取得し、それをMovable Ink画像, 写真タブの末尾に (クエリパラメータとして) 追加し、最終結果を出力します。テストタブでコードをプレビューできます。**テストタブではコード**評価してプレビューを表示します。

{% endtab %}
{% endtabs %}

## トラブルシューティング

#### ダイナミック画像が正しく表示されない?どのチャネルで問題が発生していますか？
- **プッシュ**:Movable Ink 画像, 写真の URL の前に空のロジックがあることを確認してください。<br>{% raw %}```{% if true %}{% endif %}https://movable-ink-image-url-goes-here```{% endraw %}
- **アプリ内メッセージとコンテンツカード**:画像, 写真の URL はインプレッションごとに異なるようにしてください。これは、それぞれの URL が異なるように適切な Liquid を追加することで実現できます。\[アプリ内メッセージとコンテンツカードメッセージの説明] \[手順] を参照してください。 
- **画像が読み込まれません**:必ず「マージタグ」をBrazeダッシュボードの対応するLiquidフィールドに置き換えてください。例:{% raw %}```https://mi-msg.com/p/rp/image.png?mi_u=%%email%%```{% endraw %}と {% raw %} ```https://mi-msg.com/p/rp/image.png?mi_u={{${email_address}}}```{% endraw %}.

#### Android でGIFを表示するのに問題がありますか？
- Android の実装には GIF サポートが必要です。この設定がない場合は、Android \[アプリ内メッセージカスタマイズ] \[GIFSupport] の記事に従ってください。

[1]: https://www.movableink.com/
\[datasource]: ({% image_buster /assets/img/movable_ink/movable_ink1.png %})
\[support]: https://support.movableink.com/
\[GIFsupport]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs/
\[Instructions]: {{site.baseurl}}/partners/message_personalization/dynamic_content/movable_ink/#step-4-braze-experience
[1]: ({% image_buster /assets/img/movable_ink/android.png %})
[2]: ({% image_buster /assets/img/movable_ink/ios.png %})
[3]: ({% image_buster /assets/img/movable_ink/web.png %})