---
title: "Movable Ink"
article_title: Movable Ink
alias: "/partners/movable_ink/"
description: "このリファレンス記事は、BrazeとMovable Inkのパートナーシップについて概説しています。これは、デジタルマーケティング担当者に顧客を動かす魅力的でユニークなビジュアル体験を作成する方法を提供するクラウドベースのソフトウェアプラットフォームです。"
page_type: partner
search_tag: Partner

---

# Movable Ink

> [Movable Ink](https://www.movableink.com/) は、デジタルマーケティング担当者に顧客を動かす魅力的でユニークなビジュアル体験を作成する方法を提供するクラウドベースのソフトウェアプラットフォームです。Movable Inkプラットフォームは、キャンペーンに簡単に挿入できる貴重なカスタマイズオプションを提供します。 

Movable Ink のインテリジェントクリエイティブ機能（投票、カウントダウンタイマー、スクラッチオフなど）を活用して、私たちのクリエイティブ能力を拡大します。Movable InkとBrazeの統合により、ダイナミックなデータドリブン型のメッセージに対するより包括的なアプローチが可能になり、ユーザーにとって重要な事柄に関するリアルタイムの要素が提供されます。

## 前提条件

| 要件 | 説明 |
|---|---|
| Movable Inkアカウント | このパートナーシップを利用するには、Movable Inkアカウントが必要です。 |
| データソース | データソースをMovable Inkに接続する必要があります。これは、CSV、Web サイトのインポート、またはAPIを通じて行うことができます。BrazeとMovable Inkの間でデータを統一する識別子（例えば、`external_id`）を渡すようにしてください。
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース
- パーソナライズされた月次または年末のまとめ。
- 最後に知られている行動に基づいて、メール、プッシュ、またはリッチ通知の画像を動的にパーソナライズします。<br>
	例えば： 
	- APIからデータを取得してイベントのスケジュールを動的に作成するためにリッチプッシュメッセージを使用します。 
	- カウントダウンタイマー機能を使用して、大規模なセールが近づいていることをユーザーに通知します（例えば、ブラックフライデー、バレンタインデー、ホリデーセールなど）。
	- プロモコードを配布する楽しくインタラクティブな方法としてスクラッチオフ機能を使用してください。

## サポートされているMovable Ink機能

インテリジェントクリエイティブには、Brazeユーザーが活用できる多くの提供があります。次のリストは、サポートされている機能を示しています。 

| Movable Ink機能 | 特徴 | リッチプッシュ通知 | アプリ内メッセージング / コンテンツカード / メール | 詳細 |
| ---------------------- |---| ---------------------- | -------------------------------- | ------- |
| クリエイティブオプティマイザー | A/Bコンテンツを表示 | ✗ | ✔ | |
|| 最適化する | ✗ | ✔* | \* Branchのディープリンクソリューションを使用する必要があります |
| ターゲティングルール | 日付 | ✔* | ✔ | サポートされていますが、推奨されません。プッシュ通知は受信時にキャッシュされ、更新されません。 |
|| 曜日 | ✔* | ✔ | サポートされていますが、推奨されません。プッシュ通知は受信時にキャッシュされ、更新されません。 |
|| 時刻 | ✔* | ✔ | サポートされていますが、推奨されません。プッシュ通知は受信時にキャッシュされ、更新されません。 |
| ストーリー/行動活動 | | ✔* | ✔* | \* Braze に使用される一意のユーザー識別子は、メールサービスプロバイダー (ESP) の識別子にリンクされている必要があります |
| アプリ内のディープリンク | | ✔* | ✔* | \* お客様にスムーズな体験を提供するために、確立されたディープリンクソリューションをBranch経由で使用するか、Movable Inkのクライアントエクスペリエンスチームによる検証済みのソリューションを使用してください。 |
| アプリ | カウントダウンタイマー | ✔* | ✔ | サポートされていますが、推奨されません。プッシュ通知は受信時にキャッシュされ、更新されません。 |
|| 世論調査 | ✗ | ✔* | \* 投票後、アプリをモバイルランディングページにします |
|| スクラッチオフ | ✔* | ✔* | クリックすると、スクラッチオフ体験のためにアプリを離れます |
|| 動画 | ✔* | ✔* | アニメーションGIFのみ,<br>Androidの場合、Brazeは実装において\[GIFサポート]\[GIFサポート]を必要とします。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 統合

### ステップ1:Movable Inkのデータソースを作成する

顧客は、CSV、Web サイトインポート、またはAPI統合のいずれかであるデータソースを作成する必要があります。

![表示されるさまざまなデータソースオプション:CSV アップロード、Web サイト、または API 統合。]({% image_buster /assets/img/movable_ink/movable_ink1.png %})

{% tabs ローカル %}
{% tab CSVデータソース %}
- **CSVデータソース**:各行には少なくとも1つのSegment列と1つのコンテンツ列が必要です。CSVファイルがアップロードされたら、どの列をコンテンツのターゲットに使用するかを選択します。 \[例のCSVファイル]({% image_buster /assets/download_file/movable_ink_CSV.csv %})

![「CSV」をデータソースとして選択する際に表示されるフィールド。]({% image_buster /assets/img/movable_ink/movable_ink2.png %})
{% endtab %}
{% tab Web サイト データソース %}
- **Web サイト データソース**:各行には少なくとも1つのSegment列と1つのコンテンツ列が必要です。CSVをアップロードした後、どの列をコンテンツのターゲットに使用するかを選択します。
  - このプロセスの中で、次のことをマッピングする必要があります:
    - どのフィールドがセグメントとして使用されますか
    - クリエイティブ内で動的にパーソナライズされたデータフィールドとして使用したいフィールドはどれですか（例：ユーザー属性や名、姓、市区町村など）。

![「データソース」として「Web サイト」を選択したときに表示されるフィールド。]({% image_buster /assets/img/movable_ink/movable_ink3.png %})
{% endtab %}
{% tab API統合 %}
- **API統合**:会社のAPIを使用して、API応答から直接コンテンツを提供します。

![データソースとして「API統合」を選択したときに表示されるフィールド]({% image_buster /assets/img/movable_ink/movable_ink4.png %})
{% endtab %}
{% endtabs %}

### ステップ2:Movable Inkプラットフォームでキャンペーンを作成する

Movable Inkのホーム画面から、キャンペーンを作成します。HTML、画像からのメール、またはプッシュ、アプリ内メッセージ、コンテンツカード（推奨）を含む任意のチャネルで使用できるブロックから選択できます。
また、ブロックを通じて利用できるさまざまなコンテンツオプションを確認することをお勧めします。

![新しいMovable Inkキャンペーンを作成する際のMovable Inkプラットフォームの{画像}です。]({% image_buster /assets/img/movable_ink/movable_ink5.png %}){: style="max-width:70%"}

Movable Inkには、テキスト、画像などの要素をドラッグ＆ドロップできる簡単なエディターがあります。データソースを入力した場合、データプロパティを使用して動的に画像を生成できます。さらに、キャンペーンが送信され、ユーザーがパーソナライゼーションの基準に合わない場合、このフロー内でユーザーのためにフォールバックを作成することもできます。

![Movable Inkブロックエディタは、さまざまなカスタマイズ可能な要素を表示します。]({% image_buster /assets/img/movable_ink/create_campaign2.png %})

キャンペーンを終了する前に、ダイナミックな画像をプレビューし、クエリパラメータをテストして、画像が表示されるときの見た目を確認してください。完了すると、ダイナミックなURLが生成され、それをBrazeに挿入できます！

Movable Inkプラットフォームの使用方法の詳細については、\[Movable Inkサポートセンター]\[サポート]を参照してください。

### ステップ 3:Movable Ink コンテンツ URL を取得

BrazeメッセージにMovable Inkコンテンツを含めるには、Movable Inkが提供したソースURLを見つける必要があります。 

ソースURLを取得するには、Movable Inkダッシュボードでコンテンツを設定し、そこからコンテンツを完成させてエクスポートする必要があります。「完了」ページで、クリエイティブタグからソースURL（`img src`）をコピーします。

![Movable Inkキャンペーンを完了した後に表示されるページで、ここにコンテンツURLが表示されます。]({% image_buster /assets/img/movable_ink/obtain_url.png %}){: style="max-width:80%;"}

次に、Brazeプラットフォームで、適切なフィールドにURLを貼り付けます。ステップ4に、メッセージングチャネルに適したフィールドが見つかります。最後に、マージタグ（{% raw %}```&mi_u=%%email%%```{% endraw %}など）を対応するLiquid変数（{% raw %}```&mi_u={{${email_address}}}```{% endraw %}など）に置き換えます。

### ステップ4:Brazeエクスペリエンス

{% tabs ローカル %}
{% tab メール %}
Brazeプラットフォームで、クリエイティブタグをメール本文に貼り付けます。![]({% image_buster /assets/img/movable_ink/web2.png %}){: style="max-width:90%"}<br><br>

{% endtab %}
{% tab プッシュ通知 %}

1. Brazeプラットフォーム内で:
	- Androidプッシュ:**プッシュアイコン画像**と**拡張通知画像**フィールドにURLを貼り付けます。<br>![]({% image_buster /assets/img/movable_ink/android.png %}){: style="max-width:60%"}<br><br>
	- iOSプッシュ:**メディア**リンクフィールドにURLを貼り付け、使用しているファイル形式を示します。<br>![]({% image_buster /assets/img/movable_ink/ios.png %}){: style="max-width:60%"}<br><br>
	- Web プッシュ:URLを**プッシュアイコン画像**および**大きな通知画像**フィールドに貼り付けます。<br>![]({% image_buster /assets/img/movable_ink/web.png %}){: style="max-width:60%"}<br><br>
2. 画像がキャッシュされないようにするには、メッセージ内のURLの前に空のLiquidタグを付けます:<br>{% raw %}```{% if true %}{% endif %}https://movable-ink-image-url-goes-here```{% endraw %}

{% endtab %}
{% tab アプリ内メッセージ %}

1. Brazeプラットフォームで、URLを**リッチプッシュ通知メディア**フィールドに貼り付けます。![]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. キャッシュを防ぐためにユニークなURLを提供してください。Movable Ink のリアルタイム画像が機能し、キャッシュの影響を受けないことを確認するには、Liquid を使用して Movable Ink 画像 URL の末尾にタイムスタンプを追加します。

これを行うには、必要に応じて画像URLを置き換えて、次の構文を使用します:
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
このテンプレートは現在の時間（秒単位）を取得し、それをMovable Ink画像タブの末尾に（クエリパラメータとして）追加して、最終結果を出力します。**テスト** タブでプレビューできます - これによりコードが評価され、プレビューが表示されます。

**3\.**最後に、Segmentのメンバーシップを再評価します。これを行うには、`Re-evaluate audience membership and liquid at send-time`オプションを**ターゲットオーディエンス**ステップのキャンペーンで有効にします。このオプションが利用できない場合は、顧客成功マネージャーまたはBrazeサポートに連絡してください。このオプションは、アプリ内メッセージがトリガーされるたびに一意のURLを提供するキャンペーンを再リクエストするようにBraze SDKに指示します。

{% endtab %}
{% tab コンテンツカード %}

1. Brazeプラットフォームで、URLを**リッチプッシュ通知メディア**フィールドに貼り付けます。![]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. モバイルの場合:iOSおよびAndroidのコンテンツカード画像は受信時にキャッシュされ、更新されません。 
  - 回避策として、キャンペーンを毎日、毎週、または毎月の定期的なメッセージとしてスケジュールし、対応する有効期限を設定してコンテンツカードを再テンプレート化します。例えば、コンテンツカードは1日に1回更新する必要がある場合、1日の有効期限で毎日スケジュールされた送信として設定する必要があります。
3. Movable Ink のリアルタイム画像が機能し、コンテンツカードが再テンプレート化されたときにキャッシュの影響を受けないようにするために、Liquid を使用して Movable Ink 画像 URL の末尾にタイムスタンプを追加します。

これを行うには、必要に応じて画像URLを置き換えて、次の構文を使用します:
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
このテンプレートは現在の時間（秒単位）を取得し、それをMovable Ink画像タブの末尾に（クエリパラメータとして）追加して、最終結果を出力します。**テスト** タブでプレビューでき、コードを評価してプレビューを表示します。

{% endtab %}
{% endtabs %}

## トラブルシューティング

#### ダイナミックな画像が正しく表示されない？どのチャネルに問題がありますか？
- **押す**:Movable Ink 画像 URL の前に空のロジックがあることを確認してください。<br>{% raw %}```{% if true %}{% endif %}https://movable-ink-image-url-goes-here```{% endraw %}
- **アプリ内メッセージとコンテンツカード**:各インプレッションの画像URLが一意であることを確認してください。これは、各URLが異なるように適切なLiquidを追加することで実行できます。\[アプリ内およびコンテンツカードメッセージの指示]\[指示]をご覧ください。 
- **画像 not loading**:必ずすべての「マージタグ」をBrazeダッシュボードの対応するLiquidフィールドに置き換えてください。例えば: {% raw %}```https://mi-msg.com/p/rp/image.png?mi_u=%%email%%```{% endraw %} と {% raw %}```https://mi-msg.com/p/rp/image.png?mi_u={{${email_address}}}```{% endraw %}。

#### AndroidでGIFを表示するのに問題がありますか？
- Androidは実装にGIFサポートを必要とします。Androidの\[アプリ内メッセージカスタマイズ]\[GIFサポート]記事に従って、この設定がない場合は設定してください。

[1]: https://www.movableink.com/
\[データソース]: ({% image_buster /assets/img/movable_ink/movable_ink1.png %})
サポート]: https://support.movableink.com/
\[GIFsupport]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs/
\[指示]: {{site.baseurl}}/partners/message_personalization/dynamic_content/movable_ink/#step-4-braze-experience
[1]: ({% image_buster /assets/img/movable_ink/android.png %})
[2]: ({% image_buster /assets/img/movable_ink/ios.png %})
[3]: ({% image_buster /assets/img/movable_ink/web.png %})