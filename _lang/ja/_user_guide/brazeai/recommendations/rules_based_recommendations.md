---
nav_title: ルールに基づく推薦
article_title: ルールに基づく推薦
page_type: tutorial
page_order: 16
alias: "/rules_based_recommendations/"
description: "この記事では、カタログやコネクテッドコンテンツを使用したルールベースのレコメンデーションエンジンの作成方法について概説する。"
tool:
  - Campaigns
  - Canvas

---

# ルールに基づく推奨

> ルールベースのレコメンデーションエンジンは、ユーザーデータと商品情報を使って、メッセージング内でユーザーに関連アイテムを提案する。[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) と、Braze の[カタログ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/)または[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)のいずれかを使用して、ユーザーの行動や属性に基づいてコンテンツをダイナミックにパーソナライズします。

Liquid、カタログ、コネクテッドコンテンツの詳細については、Brazeラーニングコースをチェック：

- [メールによるパーソナライズされたおすすめ](https://learning.braze.com/personalized-recommendations-with-email)
- [Liquid によるダイナミックパーソナライゼーション](https://learning.braze.com/path/dynamic-personalization-with-liquid)
- [コネクテッドコンテンツの基礎](https://learning.braze.com/path/dynamic-personalization-with-liquid/connected-content-fundamentals)

{% alert important %}
ルールベースの推奨事項は、手動で設定する必要がある固定ロジックに基づいています。つまり、ロジックを更新しない限り、ユーザーの購入履歴や嗜好に合わせてレコメンドが調整されないということだ。<br><br>AI によりパーソナライズされたおすすめ (ユーザーの履歴に合わせて自動的に調整される) を作成するには、「[AI によるアイテムのおすすめ]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/)」を参照してください。
{% endalert %}

## カタログ推奨エンジンの作成

1. 製品の[カタログを作成]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/)します。
2. 製品ごとに、推奨製品のリストを区切り記号 (パイプ `|` のようなもの) で区切った文字列として、「product_recommendations 」という名前の列に追加します。
3. カタログにおすすめを探したい製品IDを渡す。
4. そのカタログアイテムの `product_recommendations` 値を取得し、Liquid の分割フィルターを使用して区切り記号で区切ります。
5. それらの 1 つ以上の ID をカタログに渡して、他の製品の詳細を収集します。

### カタログのユースケース

例えば、あなたが健康食品のアプリを持っていて、ユーザーがアプリに登録した期間に応じて異なるレシピを送るコンテンツカードキャンペーンを作りたいとしよう。 

1. 以下の情報を含むカタログをCSVで作成し、アップロードする：<br>- **id:**ユーザーがアプリに登録してからの日数に関連する一意の数字。例えば、`3` は3日間に相当する。<br>**タイプ:** `comfort`、`fresh` などのレシピカテゴリーがあります。<br>**タイトル:** 各 ID に送信されるコンテンツカードのタイトル。「今週のランチ用の作り置き」や「タコスについて話そう」などです。<br>**リンク:** レシピ記事へのリンク。<br>- **image_url:** レシピに対応する画像, 写真。

{: start="2"}
2\.カタログが Braze にアップロードされた後、カタログアイテムの一部のプレビューを確認して、情報が正確にインポートされたことを確認してください。プレビューでは項目がランダムになっているかもしれないが、レコメンデーションエンジンの出力には影響しない。

![][1]

{: start="3"}
3\.コンテンツカードキャンペーンを作成する。作成画面で、キャンペーンの送信先のユーザー、および表示するレシピと画像を決定する Liquid ロジックを入力します。このユースケースで、Braze はユーザーの `start_date` (または登録日) を取得し、現在の日付と比較します。日数の違いによって、送信されるコンテンツカードが決まります。 

![][2]

**Title:**

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

**メッセージ:**

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

**画像：**

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

{: start="4"}
4\.**On click behavior**セクションで、iOS、Android、Webデバイスでユーザーがコンテンツカードをクリックしたときに、どこにリダイレクトされるべきかのLiquidロジックを入力する。 

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

![][3]{: style="max-width:60%;"}<br><br>

{: start="5"}
5\.**テスト」**タブに移動し、「**ユーザーとしてメッセージをプレビュー**」で**「カスタムユーザー**」を選択する。**カスタム属性**フィールドに日付を入力し、その日にサインアップしたユーザーに送信されるコンテンツカードをプレビューする。<br><br>

![][4]

## コネクテッド・コンテンツ・レコメンデーションエンジンの開発

1. 以下のいずれかの方法でコネクテッド・コンテンツ・エンドポイントを作成する：
- SheetDP のようなサービスを使って、スプレッドシートを JSON API エンドポイントに変換し、生成される API URL をメモします。
- カスタムビルドの社内エンドポイントを構築し、ホストおよびメンテナンスを行います。
- [Amazon Personalise]({{site.baseurl}}/partners/message_personalization/dynamic_content/amazon_personalize/)、[Certona]({{site.baseurl}}/partners/message_personalization/dynamic_content/certona/)、[Dynamic Yield]({{site.baseurl}}/partners/message_personalization/dynamic_content/dynamic_yield/) などの [Alloy パートナー]({{site.baseurl}}/partners/message_personalization/dynamic_content/)などのサードパーティパートナー経由で推奨エンジンを購入します。

2. コネクテッドコンテンツLiquidをメッセージボディまたはコンテンツブロックHTMLエディタに記述し、エンドポイントを呼び出してデータベースを検索する。
3. 指定したユーザープロファイルで見つけたカスタム属性の値で Liquid を整列させます。
4. 結果的に正しい推薦を引き出せた。

{% raw %}
```
{% connected_content YOUR-API-URL :save items %}

{% assign recommended_item_ids_from_user_profile = custom_attribute.${RECOMMENDED_ITEM_IDS} | split: ';' %}

{% for item_id in recommended_item_ids_from_user_profile %}
  {% assign recommended_item = items | where: "ITEM_ID", ITEM_ID | first %}
  recommended_item.item_name
{% endfor %}
```
{% endraw %}

| 属性 | 交換 |
| --- | --- |
|`YOUR-API-URL` | 実際のAPIのURLに置き換える。 |
|`RECOMMENDED_ITEM_IDS` | 推奨アイテムのIDを含むカスタム属性の実際の名前に置き換える。この属性は、セミコロンで区切られたIDの文字列であることが期待される。 |
|`ITEM_ID` | 項目 ID に対応する API 応答の実際の属性名に置き換えます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
これは基本的な例であり、特定のニーズやデータ構造に基づいてさらに修正する必要があるかもしれない。詳細なガイダンスについては、[Liquid のドキュメント]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)を参照するか、開発者に相談してください。
{% endalert %}

## コネクテッドコンテンツのユースケース

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

![][5]{: style="max-width:30%;"}

## 考慮事項

どの推奨エンジンが、利用可能なリソースやユースケースに適しているかを判断する際には、この検討事項表を参考にしてください。

| 考慮事項 | Liquid | カタログCSV | カタログ API | コネクテッドコンテンツ |
| --- | --- | --- | --- | --- |
| データポイントを消費しない | サポートされていない | 対応 | 対応 | 対応 |
| コードソリューションなし | サポートされていない | Liquid 事前生成されている場合にサポートされる | サポートされていない | サポートされていない |
| 多くの場合、高度な Liquid が必要 | 対応 | サポートされていない | サポートされていない | 対応 |
| 製品フィードのデータ更新 | サポートされていない | 推奨事項が頻繁に更新されない場合はサポートされる | 推奨事項が1時間ごとに更新される場合はサポートされる | サポートされており、おすすめがリアルタイムまで更新される |
| Braze UI内で推薦文を生成する | 対応 | 対応 | 対応 | Braze以外で生成された場合はサポートされない。 |
| 推奨データのホスティング、マネージャー、トラブルシューティングがない | 対応 | 対応 | 対応 | サポートされていない |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

[1]: {% image_buster /assets/img/recs/catalog_items.png %}
[2]: {% image_buster /assets/img/recs/content_card_preview.png %}
[3]: {% image_buster /assets/img/recs/on_click_behavior.png %}
[4]: {% image_buster /assets/img/recs/custom_attributes_test.png %}
[5]: {% image_buster /assets/img/recs/sample_response.png %}