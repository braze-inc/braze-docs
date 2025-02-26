---
nav_title: "カタログセグメント"
article_title: カタログセグメント
page_order: 1
page_type: reference
alias: "/catalog_segments/"
description: "この記事では、SQL セグメントエクステンションでカタログデータを使用してユーザーのオーディエンスを構築するカタログセグメントを作成する方法について説明します。"
tool: Segments
---

# カタログセグメント

> カタログセグメントは、カタログデータとカスタムイベントまたは購入からのデータを組み合わせて作成される SQL セグメントエクステンションの一種です。セグメントで参照し、キャンペーンやキャンバスでターゲットにすることができます。 

{% alert important %}
カタログセグメントは現在、早期アクセス中です。この早期アクセスへ参加することに興味がある場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

カタログセグメントは、SQL を使用して、カタログのデータとカスタムイベントまたは購入のデータとを結合します。これを行うには、カタログとカスタムイベントまたは購入に共通の識別子フィールドが必要です。たとえば、カタログ内のアイテム ID の値は、カスタム イベントのプロパティの値と一致する必要があります。

## カタログセグメントの作成

1. [**セグメントエクステンション**] > [**エクステンションを新規作成**] > [**テンプレートで開始**] に移動し、テンプレート [**カタログセグメント**] を選択します。<br>![作成するテンプレートとして「カタログセグメント」を選択したモーダル。][1]{: style="max-width:70%" }

{: start="2"}
2\.SQL エディターにテンプレートが自動的に入力されます。<br>![事前生成されたテンプレートを持つSQL エディタ。][2]{: style="max-width:70%" }<br>このテンプレートでは、ユーザーイベントデータをカタログデータと結合して、特定のカタログ項目を使用したユーザーをセグメント化します。

3. [**変数**] タブを使用して、セグメントを生成する前にテンプレートに必要なフィールドを指定します。<br>Braze がカタログアイテムへのエンゲージメントに基づいてユーザーを識別するには、次のことを行う必要があります。<br> \- カタログフィールドを含むカタログを選択します <br> \- イベントプロパティを含むカスタムイベントを選択します <br> \- カタログフィールドとイベントプロパティの値を一致させる

変数を選択するためのガイドラインを次に示します。

| 可変フィールド | 説明 |
| --- | --- |
| `Catalog` | ユーザーのターゲット設定に使用しているカタログの名前。 |
| `Catalog field`| `Custom event property` と同じ値を含むカタログ内のフィールド。これは多くの場合、ID の一種です。e コマースのユースケースでは `shopify_id` になります。 |
| `Custom event` | カスタムイベントの名前。これは、`Catalog field` と一致する値を持つプロパティを含む同じイベントです。e コマースのユースケースでは `Made Order` になります。 |
| `Custom event property` | カスタムイベントプロパティの名前。値を `Catalog field` と一致させます。e コマースのサンプルユースケースでは、`Shopify_ID.` になります。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="4"}
4\.必要に応じて、ユースケースの追加のオプションフィールドに入力して、カタログ内の特定のフィールド値でセグメント化します。
- `Catalog field`:このカタログ内の特定のフィールド (列名)
- `Value`:そのフィールドまたは列内の特定の値 <br><br> ヘルスケアアプリを例にとると、予約できる各医師のカタログ内に、`vision` や `dental` などの値を含む `specialty` というフィールドがあるとします。値が `dental` の医師を受診したユーザーをセグメント化するには、`Catalog field` として `specialty` を選択し、`Value` として `dental` を選択します。

5. SQL セグメントを作成したら、[**プレビューの実行**] をクリックして、クエリがユーザーを返すかどうか、またはエラーがあるかどうかを確認することをお勧めします。[クエリ結果のプレビュー]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#previewing-results)、[SQL セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#managing-sql-segment-extensions)の管理などの詳細については、「[SQL セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/)」を参照してください。 

## ユースケース

### ヘルスケアアプリ

医療アプリを持っていて、歯科医のために訪問を予約した人をSegment ユーザーしたいとしましょう。また、次のものもあります。

- 患者が予約できるさまざまな医師を含むカタログ `Doctors`。それぞれに `doctor ID` が割り当てられています。
- カタログの `doctor ID` フィールドと同じ値を共有する `doctor ID` プロパティを持つカスタムイベント `Booked Visit`
- `dental` 値を含むカタログ内の`speciality` フィールド

カタログセグメントは、次の変数を使用して設定します。

| 変数 | プロパティ |
| --- | --- |
| `Catalog`| 医師 |
| `Catalog field` | 医師 ID |
| `Custom event`| 予約訪問|
| `Custom event property` | 医師 ID |
| `(Under Filter SQL Results) Catalog field` | スペシャリティ |
| `(Under Filter SQL Results) Value`| 歯科 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### SaaS プラットフォーム

たとえば、B2B SaaSプラットフォームがあり、既存の顧客の従業員であるユーザーをセグメント化したいとします。また、次のものもあります。

- 現在SaaS プラットフォームを使用しているさまざまなアカウントを含むカタログ`Accounts`。それぞれに次のように割り当てられます `account ID`
- カタログの "アカウント ID" フィールドと同じ値を共有する "アカウント ID" プロパティを持つカスタムイベント `Event Attendance`
- `enterprise` 値を含むカタログ内の`Classification` フィールド

カタログセグメントは、次の変数を使用して設定します。

| 変数 | プロパティ |
| --- | --- |
| `Catalog` | アカウント |
| `Catalog field `| アカウントID |
| `Custom event` | イベント参加 |
| `Custom event property` | アカウントID |
| `(Under Filter SQL Results) Catalog field` | 分類 (Classification) |
| `(Under Filter SQL Results) Value` | 企業 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## よくある質問

### カタログセグメントを実行すると、SQL セグメントエクステンションクレジットが消費されますか。

はい、カタログ セグメントは SQL を利用しており、SQL セグメントエクステンションクレジットを消費します。詳細については、「[SQL セグメントの使用方法]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments#monitoring-your-sql-segments-usage)」を参照してください。

### カタログセグメントを作成すると、SQL セグメントエクステンションの割り当てが消費されますか?

はい。SQL セグメントエクステンションがセグメントエクステンションの割り当てにカウントされるのと同様に、カタログセグメントもその割り当てにカウントされます。

### カタログセグメントのユースケースがありますが、現在のテンプレートには対応していません。どのように設定すればよいですか?

追加のガイダンスについては、カスタマーサポートマネージャーまたは [Brazeサポート]({{site.baseurl}}/help/support/)にお問い合わせください。

[1]: {% image_buster /assets/img/catalog-segments-template.png %}
[2]: {% image_buster /assets/img/catalog-segments-editor.png %}
