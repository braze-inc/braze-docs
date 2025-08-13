---
nav_title: ルールに基づくレコメンデーション
article_title: ルールベースのアイテムレコメンドの作成
description: "この記事では、カタログに掲載されているアイテムについて、AI によるアイテムのおすすめを作成する方法を説明します。"
page_order: 2
---

# ルールに基づく項目のレコメンデーションの作成

> カタログ内のアイテムからルールベースのレコメンドエンジンを作成する方法について説明します。

## ルールベースの項目の推奨事項について

ルールベースのレコメンデーションエンジンは、ユーザーデータと商品情報を使って、メッセージング内でユーザーに関連アイテムを提案する。これは、[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)を使用し、Braze [catalogs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/)または[Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)を使用して、ユーザーの動作と属性に基づいてコンテンツを動的にパーソナライズします。

{% alert important %}
ルールベースの推奨事項は、手動で設定する必要がある固定ロジックに基づいています。つまり、ロジックを更新しない限り、ユーザーの購入履歴や嗜好に合わせてレコメンドが調整されないということだ。<br><br>AI によりパーソナライズされたおすすめ (ユーザーの履歴に合わせて自動的に調整される) を作成するには、「[AI によるアイテムのおすすめ]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/)」を参照してください。
{% endalert %}

## 推奨エンジンオプション

どの推奨エンジンが、利用可能なリソースやユースケースに適しているかを判断する際には、この検討事項表を参考にしてください。

<table style="text-align: center;">
  <thead>
    <tr>
      <th>レコメンデーションエンジン</th>
      <th>データポイントは消費されません</th>
      <th>ノーコードソリューション</th>
      <th>高度な Liquid がない</th>
      <th>製品フィードを自動的に更新する</th>
      <th>Braze UI で生成</th>
      <th>データホスティングまたはトラブルシューティングなし</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>カタログCSV</strong></td>
      <td>✔</td>
      <td>はい (事前に生成されｔげいる Liquid を使用する場合)</td>
      <td>✔</td>
      <td>はい (レコメンデ―ションが頻繁に更新<strong>されない</strong>場合)</td>
      <td>✔</td>
      <td>✔</td>
    </tr>
    <tr>
      <td><strong>カタログ API</strong></td>
      <td>✔</td>
      <td></td>
      <td>✔</td>
      <td>はい (レコメンデーションが1時間ごとに更新される場合)</td>
      <td>✔</td>
      <td>✔</td>
    </tr>
    <tr>
      <td><strong>コネクテッドコンテンツ</strong></td>
      <td>✔</td>
      <td></td>
      <td></td>
      <td>✔<br>(レコメンデーションはリアルタイムで更新される)</td>
      <td>はい (Braze の外部で生成された場合)</td>
      <td></td>
    </tr>
    <tr>
      <td><strong>Liquid</strong></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>✔</td>
      <td>✔</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 .reset-td-br-7 role="presentation" }

## 推奨エンジンの作成

カタログまたは接続コンテンツのいずれかを使用して、推奨エンジンを作成します。

{% tabs local %}
{% tab カタログを使用 %}
カタログを使用してレコメンドエンジンを作成するには

1. 製品の[カタログを作成]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/)します。
2. 製品ごとに、推奨製品のリストを区切り記号 (パイプ `|` のようなもの) で区切った文字列として、「product_recommendations 」という名前の列に追加します。
3. カタログにおすすめを探したい製品IDを渡す。
4. そのカタログアイテムの `product_recommendations` 値を取得し、Liquid の分割フィルターを使用して区切り記号で区切ります。
5. それらの 1 つ以上の ID をカタログに渡して、他の製品の詳細を収集します。

### 例

例えば、あなたが健康食品のアプリを持っていて、ユーザーがアプリに登録した期間に応じて異なるレシピを送るコンテンツカードキャンペーンを作りたいとしよう。まず、以下の情報を含むCSV ファイルを使用してカタログを作成してアップロードします。

|フィールド|説明|
|-----|-----------|
| **id** | ユーザーがアプリに登録してからの日数に関連する一意の数字。例えば、`3` は3日間に相当する。 |
| **タイプ** | `comfort`、`fresh` などのレシピカテゴリーがあります。 |
| **名称** | 各 ID に送信されるコンテンツカードのタイトル。「今週のランチ用の作り置き」や「タコスについて話そう」などです。 |
| **リンク** | レシピ記事へのリンク。 |
| **image_url** | レシピに対応する画像, 写真。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

カタログが Braze にアップロードされた後、カタログアイテムの一部のプレビューを確認して、情報が正確にインポートされたことを確認してください。プレビューでは項目がランダムになっているかもしれないが、レコメンデーションエンジンの出力には影響しない。

![Braze のカタログの例。]({% image_buster /assets/img/recs/catalog_items.png %})

コンテンツカードキャンペーンを作成する。作成画面で、キャンペーンの送信先のユーザー、および表示するレシピと画像を決定する Liquid ロジックを入力します。このユースケースで、Braze はユーザーの `start_date` (または登録日) を取得し、現在の日付と比較します。日数の違いによって、送信されるコンテンツカードが決まります。

{% subtabs local %}
{% subtab title %}
{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{{ items[0].title }}
```
{% endraw %}
{% endsubtab %}

{% subtab message %}
{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{% if items[0].title != blank %}
{{ items[0].body }}
{% else %}
{% abort_message('no card for today') %}
{% endif %}
```
{% endraw %}
{% endsubtab %}

{% subtab image %}
{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{{ items[0].image_url }}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}

以下に例を示します。

![コンテンツカードキャンペーンのメッセージコンポーザーの例。]({% image_buster /assets/img/recs/content_card_preview.png %})

**On click behavior**セクションで、iOS、Android、Webデバイスでユーザーがコンテンツカードをクリックしたときに、どこにリダイレクトされるべきかのLiquidロジックを入力する。 

{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{{ items[0].link }}
```
{% endraw %}

以下に例を示します。

![作成画面でのクリック時動作ブロックの例。]({% image_buster /assets/img/recs/on_click_behavior.png %}){: style="max-width:60%;"}<br><br>

**テスト」**タブに移動し、「**ユーザーとしてメッセージをプレビュー**」で**「カスタムユーザー**」を選択する。**カスタム属性**フィールドに日付を入力し、その日にサインアップしたユーザーに送信されるコンテンツカードをプレビューする。<br><br>

!['start_date'.]({% image_buster /assets/img/recs/custom_attributes_test.png %})という名前のカスタム属性の例
{% endtab %}

{% tab Connected Content を使用 %}
Connected Content を使用してレコメンドエンジンを作成するには、まず次のいずれかの方法を使用して新しいエンドポイントを作成します。

|オプション|説明|
|------|-----------|
|**スプレッドシートの変換**|スプレッドシートをSheetDP のようなサービスを使用してJSON API エンドポイントに変換し、この生成されるAPI URL に注意してください。|
|**カスタムエンドポイントの作成**|カスタムビルドの社内エンドポイントを作成し、ホストおよびメンテナンスを行います。|
|**サードパーティエンジンの使用** |サードパーティの推奨エンジン([Alloy partners]({{site.baseurl}}/partners/message_personalization/)など)を使用します。これには、[Amazon Personalise]({{site.baseurl}}/partners/amazon_personalize/)、[Certona]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalized_recommendations/certona/)、[Dynamic Yield]({{site.baseurl}}/partners/dynamic_yield/)などが含まれます。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

次に、エンドポイントを呼び出すメッセージで Liquid を使用して、カスタム属性値をユーザーのプロファイルに一致させ、対応する推奨事項をプルします。

{% raw %}
```liquid
{% connected_content YOUR_API_URL :save items %}

{% assign recommended_item_ids_from_user_profile = custom_attribute.${RECOMMENDED_ITEM_IDS} | split: ';' %}

{% for item_id in recommended_item_ids_from_user_profile %}
  {% assign recommended_item = items | where: "ITEM_ID", ITEM_ID | first %}
  recommended_item.item_name
{% endfor %}
```
{% endraw %}

以下を置き換えます。

| 属性 | 交換 |
| --- | --- |
|`YOUR_API_URL` | 実際のAPIのURLに置き換える。 |
|`RECOMMENDED_ITEM_IDS` | 推奨アイテムのIDを含むカスタム属性の実際の名前に置き換える。この属性は、セミコロンで区切られたIDの文字列であることが期待される。 |
|`ITEM_ID` | 項目 ID に対応する API 応答の実際の属性名に置き換えます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
これは基本的な例であり、特定のニーズやデータ構造に基づいてさらに修正する必要があるかもしれない。詳細なガイダンスについては、[Liquid のドキュメント]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)を参照するか、開発者に相談してください。
{% endalert %}

### 例

例えば、Zomato Restaurantsデータベースからお勧めのレストランを取得し、その結果を`restaurants` という内部変数として保存したいとしよう。次のコネクテッドコンテンツの呼び出しができます。

{% raw %}
```liquid

{% connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:“USER_KEY”} :save restaurants %}

{{city_food.restaurants[0]}}
```
{% endraw %}

次に、ユーザーの市区町村と食べ物の種類に基づいて、お勧めのレストランを引き出したいとしよう。ユーザーの市区町村と料理の種類のカスタム属性を呼び出しの冒頭にダイナミックに挿入し、`restaurants` の値を変数 `city_food.restaurants` に代入することで、これを行うことができます。

コネクテッドコンテンツの呼び出しは次のようになります。

{% raw %}
```liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}

{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:“USER_KEY”} :save restaurants %}

{% assign restaurants = city_food.restaurants %}

{{city_food.restaurants[0]}}
```
{% endraw %}

レストラン名と評価だけを取得するようにレスポンスを調整したい場合は、次のようにフィルターを呼び出しの最後に追加することができる：

{% raw %}
```liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}

{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:”USER_KEY”} :save restaurants %}
{% assign restaurants = city_food.restaurants %}

{{city_food.restaurants[0].restaurant.name}}
{{city_food.restaurants[0].restaurant.user_rating.rating_text}}
```
{% endraw %}

最後に、お勧めのレストランを評価別にまとめたいとしよう。次の手順を実行します。

1. `assign` 、「素晴らしい」、「非常に良い」、「良い」の評価カテゴリー用の空白の配列を作成する。
2. リスト内の各レストランの評価を調べる `for` ループを追加します。 
- 評価が「優れている」場合は、レストラン名を `excellent_restaurants` 文字列の後に追加し、各レストラン名を区切る * 文字を最後に追加します。 
- 評価が "Very Good "の場合、`very_good_restaurants` の文字列にレストラン名を追加し、最後に*を追加する。
- 評価が "Good "の場合、`good_restaurants` の文字列にレストラン名を追加し、最後に*を追加する。
3. 返されるおすすめレストランの数を各カテゴリで 4 店に制限します。

最終的な呼び出しは次のようになります。

{% raw %}
```liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}
{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:”USER_KEY”} :save restaurants %}
{% assign restaurants = city_food.restaurants %}
{% assign excellent_restaurants = “” %}
{% assign very_good_resturants = “” %}
{% assign good_restaurants = “” %}
{% for list in restaurants %}
{% if {{list.restaurant.user_rating.rating_text}} == `Excellent` %}
{% assign excellent_restaurants = excellent_restaurants | append: list.restaurant.name | append: `*` %}
{% elseif {{list.restaurant.user_rating.rating_text}} == `Very Good` %}
{% assign very_good_restaurants = very_good_restaurants | append: list.restaurant.name | append: `*` %}
{% elseif {{list.restaurant.user_rating.rating_text}} == `Good` %}
{% assign good_restaurants = good_restaurants | append: list.restaurant.name | append: `*` %}
{% endif %}
{% endfor %}
{% assign excellent_array = excellent_restaurants | split: `*` %}
{% assign very_good_array = very_good_restaurants | split: `*` %}
{% assign good_array = good_restaurants | split: `*` %}

Excellent places
{% for list in excellent_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}

Very good places
{% for list in very_good_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}

Good places
{% for list in good_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}
```
{% endraw %}

ユーザー端末でのレスポンシブの表示例については、以下のスクリーンショットを参照のこと。

![例の最終呼び出しで生成されたレストランリストのレンダリング。]({% image_buster /assets/img/recs/sample_response.png %}){: style="max-width:30%;"}
{% endtab %}
{% endtabs %}
