---
nav_title: "カタログセグメント"
article_title: カタログセグメント
page_order: 0
page_type: reference
alias: "/catalog_segments/"
description: "この記事では、SQL セグメントエクステンションでカタログデータを使用してユーザーのオーディエンスを構築するカタログセグメントを作成する方法について説明します。"
tool: Segments
---

# カタログセグメント

> カタログセグメントは、カタログデータとカスタムイベントまたは購入からのデータを組み合わせて作成される SQL セグメントエクステンションの一種です。セグメントで参照し、キャンペーンや Canvas でターゲットにすることができます。 

カタログセグメントは、SQL を使用して、カタログのデータとカスタムイベントまたは購入のデータを結合します。これを行うには、カタログとカスタムイベントまたは購入に共通の識別子フィールドが必要です。たとえば、カタログ内のアイテム ID の値は、カスタムイベントのプロパティの値と一致する必要があります。

## カタログセグメントの作成

1. [**セグメントエクステンション**] > [**エクステンションを新規作成**] > [**テンプレートで開始**] に移動し、テンプレートを選択します。<br>![イベント、購入、またはRFMセグメントのカタログセグメントを作成するためのオプションを持つモーダル。]({% image_buster /assets/img/catalog-segments-template.png %}){: style="max-width:80%" }

{: start="2"}
2. SQL エディターにテンプレートが自動的に入力されます。<br>![事前生成されたテンプレートを持つ SQL エディター。]({% image_buster /assets/img/catalog-segments-editor.png %}){: style="max-width:80%" }<br>このテンプレートでは、ユーザーイベントデータをカタログデータと結合して、特定のカタログアイテムにエンゲージしたユーザーをセグメント化します。

3. [**変数**] タブを使用して、セグメントを生成する前にテンプレートに必要なフィールドを指定します。<br>Braze がカタログアイテムへのエンゲージメントに基づいてユーザーを識別するには、次のことを行う必要があります。<br> - カタログフィールドを含むカタログを選択します <br> - イベントプロパティを含むカスタムイベントを選択します <br> - カタログフィールドとイベントプロパティの値を一致させます

変数を選択するためのガイドラインを次に示します。

| 変数フィールド | 説明 |
| --- | --- |
| `Catalog` | ユーザーのターゲット設定に使用しているカタログの名前です。 |
| `Catalog field`| `Custom event property` と同じ値を含むカタログ内のフィールドです。これは多くの場合、ID の一種です。e コマースのユースケースでは `shopify_id` になります。 |
| `Custom event` | カスタムイベントの名前です。これは、`Catalog field` と一致する値を持つプロパティを含む同じイベントです。e コマースのユースケースでは `Made Order` になります。 |
| `Custom event property` | カスタムイベントプロパティの名前です。値を `Catalog field` と一致させます。e コマースのサンプルユースケースでは、`Shopify_ID.` になります。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="4"}
4. 必要に応じて、ユースケースの追加のオプションフィールドに入力して、カタログ内の特定のフィールド値でセグメント化します。
- `Catalog field`:このカタログ内の特定のフィールド (列名)
- `Value`:そのフィールドまたは列内の特定の値 <br><br> ヘルスケアアプリを例にとると、予約できる各医師のカタログ内に、`vision` や `dental` などの値を含む `specialty` というフィールドがあるとします。値が `dental` の医師を受診したユーザーをセグメント化するには、`Catalog field` として `specialty` を選択し、`Value` として `dental` を選択します。

5. SQL セグメントを作成したら、[**プレビューの実行**] をクリックして、クエリがユーザーを返すかどうか、またはエラーがあるかどうかを確認することをお勧めします。[クエリ結果のプレビュー]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#previewing-results)、[SQL セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#managing-sql-segment-extensions)の管理などの詳細については、「[SQL セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/)」を参照してください。 

{% alert note %}
テーブル `CATALOGS_ITEMS_SHARED` を使用する SQL セグメントを作成する場合は、カタログ ID を指定する必要があります。以下に例を示します。

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

### SQL を反転する必要があるかどうかの判別

イベントが 0 件のユーザーを直接クエリすることはできませんが、**SQL の反転**を使用してこれらのユーザーをターゲットにすることができます。

たとえば、購入数が 3 件未満のユーザーをターゲットにするには、まず購入数が 3 件以上のユーザーを選択するクエリを作成します。次に、**SQL の反転**を選択して、購入数が 3 件未満のユーザー (購入数が 0 件のユーザーを含む) をターゲットにします。

![「直近30日間で1～4件のメールをクリック」という名前のセグメントエクステンションで、SQL を反転するオプションが選択されています。]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:70%;"}

{% alert important %}
イベントが 0 件のユーザーを特にターゲットにする場合を除き、SQL を反転する必要はありません。**SQL の反転**が選択されている場合は、その機能が必要であり、セグメントが目的のオーディエンスと一致していることを確認してください。たとえば、クエリが少なくとも 1 件のイベントを持つユーザーをターゲットにしている場合、反転すると 0 件のイベントを持つユーザーのみがターゲットになります。
{% endalert %}

## セグメントメンバーシップの更新

カタログセグメントのセグメントメンバーシップを更新するには、カタログセグメントを開き、[**アクション**] > [**最新の情報に更新**] > [**はい、更新します**] を選択します。

{% alert tip %}
ユーザーが頻繁に出入りすることが予想されるセグメントを作成した場合は、キャンペーンまたはキャンバスでそのセグメントをターゲットにする前に、使用するカタログセグメントを手動で更新してください。
{% endalert %}

### 更新設定の指定

{% multi_lang_include segments.md section='Refresh settings' %}

## ユースケース

{% tabs local %}
{% tab Health %}

### ヘルスケアアプリ

ヘルスケアアプリを持っていて、歯科医の訪問を予約したユーザーをセグメント化したいとします。また、次のものもあります。

- 患者が予約できるさまざまな医師を含むカタログ `Doctors`。それぞれに `doctor ID` が割り当てられています。
- カタログの `doctor ID` フィールドと同じ値を共有する `doctor ID` プロパティを持つカスタムイベント `Booked Visit`
- `dental` 値を含むカタログ内の `speciality` フィールド

カタログセグメントは、次の変数を使用して設定します。

| 変数 | プロパティ |
| --- | --- |
| `Catalog`| Doctors |
| `Catalog field` | doctor ID |
| `Custom event`| Booked Visit|
| `Custom event property` | doctor ID |
| `(Under Filter SQL Results) Catalog field` | Specialty |
| `(Under Filter SQL Results) Value`| Dental |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab SaaS %}

### SaaS プラットフォーム

B2B SaaS プラットフォームがあり、既存の顧客の従業員であるユーザーをセグメント化したいとします。また、次のものもあります。

- 現在 SaaS プラットフォームを使用しているさまざまなアカウントを含むカタログ `Accounts`。それぞれに `account ID` が割り当てられています。
- カタログの「account ID」フィールドと同じ値を共有する「account ID」プロパティを持つカスタムイベント `Event Attendance`
- `enterprise` 値を含むカタログ内の `Classification` フィールド

カタログセグメントは、次の変数を使用して設定します。

| 変数 | プロパティ |
| --- | --- |
| `Catalog` | Accounts |
| `Catalog field `| account ID |
| `Custom event` | Event Attendance |
| `Custom event property` | account ID |
| `(Under Filter SQL Results) Catalog field` | Classification |
| `(Under Filter SQL Results) Value` | Enterprise |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## よくある質問

### カタログセグメントを実行すると、SQL セグメントエクステンションクレジットが消費されますか?

はい、カタログセグメントは SQL を利用しており、SQL セグメントエクステンションクレジットを消費します。詳細については、「[SQL セグメントの使用状況]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments#monitoring-your-sql-segments-usage)」を参照してください。

### カタログセグメントを作成すると、SQL セグメントエクステンションの割り当てが消費されますか?

はい。SQL セグメントエクステンションがセグメントエクステンションの割り当てにカウントされるのと同様に、カタログセグメントもその割り当てにカウントされます。

### カタログセグメントのユースケースがありますが、現在のテンプレートでは対応していません。どのように設定すればよいですか?

詳細については、顧客サポートマネージャーまたは [Braze サポート]({{site.baseurl}}/user_guide/administrative/access_braze/support/)にお問い合わせください。