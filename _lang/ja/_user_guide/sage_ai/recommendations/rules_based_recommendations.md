---
nav_title: ルールベースの推奨
article_title: ルールベースの推奨
page_type: tutorial
page_order: 16
alias: "/rules_based_recommendations/"
description: "この記事では、カタログまたはコネクテッドコンテンツを使用するルールベースのレコメンデーションエンジンの作成方法について説明します。"
tool:
  - Campaigns
  - Canvas

---

# ルールベースの推奨事項

> ルールベースのレコメンデーションエンジンは、ユーザーデータと製品情報を使用して、メッセージ内でユーザーに関連するアイテムを提案します。それは[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)とBraze [カタログ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/)または[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)のいずれかを使用して、ユーザーの行動と属性に基づいてコンテンツを動的にパーソナライズします。

Liquid、カタログ、コネクテッドコンテンツについて詳しく知るには、これらのBraze学習コースをチェックしてください:

- [パーソナライズされたおすすめとメール](https://learning.braze.com/personalized-recommendations-with-email)
- [Liquid によるダイナミックパーソナライゼーション](https://learning.braze.com/path/dynamic-personalization-with-liquid)
- [コネクテッドコンテンツの基礎](https://learning.braze.com/path/dynamic-personalization-with-liquid/connected-content-fundamentals)

{% alert important %}
ルールベースの推奨事項は、手動で設定する必要がある固定ロジックに基づいています。これは、ロジックを更新しない限り、あなたの推奨事項がユーザーの購入履歴や好みに調整されないことを意味します。<br><br>ユーザーの履歴に自動的にAdjustするパーソナライズされたAIレコメンデーションを作成するには、[AI item recommendations]({{site.baseurl}}/ai_item_recommendations)をチェックしてください。
{% endalert %}

## カタログのレコメンデーションエンジンを作成する

1. [製品のカタログを作成する]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/)
2. 各製品について、区切り文字（パイプ`|`など）で区切られた文字列として推奨製品のリストを「product_recommendations」という列に追加します。
3. 製品IDをカタログに渡して、推奨事項を見つけてください。
4. そのカタログアイテムの`product_recommendations`値を取得し、Liquid分割フィルターでデリミタで分割します。
5. それらのIDの1つ以上をカタログに戻して、他の製品の詳細を収集します。

### カタログのユースケース

たとえば、健康食品アプリを持っていて、ユーザーがアプリにサインアップしてからの期間に応じて異なるレシピを送信するコンテンツカードキャンペーンを作成したいとします。 

1. CSVを介して次の情報を含むカタログを作成してアップロードします:<br>- **id:**ユーザーがあなたのアプリにサインアップしてからの日数に相当するユニークな番号。例えば、`3`は3日間に相当します。<br>**タイプ:**レシピのカテゴリ、例えば`comfort`、`fresh`、その他。<br>**タイトル:**各IDに送信されるコンテンツカードのタイトルは、「今週のランチのために作り置き」や「タコスについて話そう」などです。<br>**リンク:**レシピ記事へのリンク。<br>**画像_url:**レシピに対応する画像。

{: start="2"}
2\.カタログがBrazeにアップロードされた後、カタログアイテムの一部のプレビューを確認して、情報が正確にインポートされたことを確認してください。アイテムはプレビューでランダム化される場合がありますが、レコメンデーションエンジンの出力には影響しません。

![][1]

{: start="3"}
3\.コンテンツカードキャンペーンを作成します。コンポーザーで、どのユーザーがキャンペーンを受け取るべきか、どのレシピと画像を表示するべきかを決定するためにLiquidロジックを入力します。このユースケースでは、Braze はユーザーの`start_date`（またはサインアップ日）を取得し、現在の日付と比較します。日数の違いによって、どのコンテンツカードが送信されるかが決まります。 

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
4\.「**クリック時の動作**」セクションで、iOS、Android、およびWebデバイスでコンテンツカードをクリックしたときにユーザーがリダイレクトされる場所のLiquidロジックを入力します。 

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
5\.**テスト** タブに移動し、**ユーザーとしてメッセージをプレビュー** の下の **カスタムユーザー** を選択します。日付を**カスタム属性**フィールドに入力して、その日にサインアップしたユーザーに送信されるコンテンツカードをプレビューします。<br><br>

![][4]

## コネクテッドコンテンツレコメンデーションエンジンの作成

1. 次のいずれかの方法でコネクテッドコンテンツエンドポイントを作成します:
- スプレッドシートをJSON APIエンドポイントに変換するには、SheetDPのようなサービスを使用し、生成されるAPI URLに注意してください。
- カスタムビルドの社内エンドポイントを構築、ホスト、および維持する
- サードパーティのパートナーを通じてレコメンデーションエンジンを購入します。例えば、[Alloyパートナー]({{site.baseurl}}/partners/message_personalization/dynamic_content)の1つである[Amazon Personalise]({{site.baseurl}}/partners/message_personalization/dynamic_content/amazon_personalize/)、[Certona]({{site.baseurl}}/partners/message_personalization/dynamic_content/certona/)、[ダイナミックなYield]({{site.baseurl}}/partners/message_personalization/dynamic_content/dynamic_yield/)などがあります。

2. メッセージ本文またはコンテンツブロックHTMLエディタにコネクテッドコンテンツLiquidを記述して、データベースを検索するエンドポイントを呼び出します。
3. 与えられたユーザーのプロファイルで見つけたカスタム属性の値にLiquidを合わせます。
4. 正しい推奨事項を結果として引き出します。

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
|`YOUR-API-URL` | APIの実際のURLに置き換えてください。 |
|`RECOMMENDED_ITEM_IDS` | 推奨アイテムのIDを含むカスタム属性の実際の名前に置き換えてください。この属性は、セミコロンで区切られたIDの文字列であることが期待されます。 |
|`ITEM_ID` | APIレスポンス内のアイテムIDに対応する属性の実際の名前に置き換えてください。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
これは基本的な例であり、特定のニーズやデータ構造に基づいてさらに修正する必要があるかもしれません。詳細なガイダンスについては、[Liquidドキュメント]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid)を参照するか、開発者に相談してください。
{% endalert %}

## コネクテッドコンテンツ ユースケース

レストランの推薦をZomatoレストランデータベースから引き出し、その結果を`restaurants`というローカル変数として保存したいとしましょう。次のコネクテッドコンテンツ呼び出しを行うことができます:

{% raw %}
```liquid

{% connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:“USER_KEY”} :save restaurants %}

{{city_food.restaurants[0]}}
```
{% endraw %}

次に、ユーザーの市区町村と食べ物の種類に基づいてレストランの推薦を引き出したいとしましょう。ユーザーの市区町村と食べ物の種類のカスタム属性を動的に挿入し、`restaurants`の値を変数`city_food.restaurants`に割り当てることで、これを行うことができます。

コネクテッドコンテンツの呼び出しは次のようになります:

{% raw %}
```liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}

{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:“USER_KEY”} :save restaurants %}

{% assign restaurants = city_food.restaurants %}

{{city_food.restaurants[0]}}
```
{% endraw %}

応答をレストランの名前と評価のみに絞りたい場合は、次のように呼び出しの最後にフィルターを追加できます:

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

最後に、レストランのおすすめを評価ごとにグループ化したいとしましょう。次のことを行ってください:

1. 「優秀」、「非常に良い」、「良い」の評価カテゴリの空の配列を作成するには`assign`を使用します。
2. リスト内の各レストランの評価を調べる`for`ループを追加します。 
- 評価が「優れている」場合は、レストラン名を`excellent_restaurants`文字列に追加し、各レストラン名を区切るために最後に*文字を追加します。 
- 評価が「非常に良い」の場合は、レストラン名を`very_good_restaurants`文字列に追加し、最後に*文字を追加します。
- 評価が「良い」の場合、レストラン名を`good_restaurants`文字列に追加し、最後に*文字を追加します。
3. カテゴリごとのレストランの推薦数を4つに制限する。

これは最終的な呼び出しがどのように見えるかです:

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

ユーザーのデバイスに応答が表示される例については、以下のスクリーンショットを参照してください。

![][5]{: style="max-width:30%;"}

## 考慮事項

どのレコメンデーションエンジンが利用可能なリソースとユースケースに適しているかを決定する際には、この考慮事項の表を参照してください。

| 考慮事項 | Liquid | カタログ CSV | カタログ API | コネクテッドコンテンツ |
| --- | --- | --- | --- | --- |
| データポイントを消費しません | サポートされていません | サポートされている | サポートされている | サポートされている |
| コードなしソリューション | サポートされていません | 事前生成されたLiquidがサポートされている場合 | サポートされていません | サポートされていません |
| 高度なLiquidが必要な場合が多い | サポートされている | サポートされていません | サポートされていません | サポートされている |
| 製品フィードのデータの更新 | サポートされていません | 推奨事項が頻繁に更新されない場合にサポートされます | 推奨事項が毎時更新される場合にサポートされます | サポートと推奨事項はリアルタイムまで更新されます |
| Braze UI内で推奨事項を生成する | サポートされている | サポートされている | サポートされている | Braze 以外で生成された場合はサポートされません |
| ホスティング、管理、トラブルシューティングの推奨データはありません | サポートされている | サポートされている | サポートされている | サポートされていません |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

[1]: {% image_buster /assets/img/recs/catalog_items.png %}
[2]: {% image_buster /assets/img/recs/content_card_preview.png %}
[3]: {% image_buster /assets/img/recs/on_click_behavior.png %}
[4]: {% image_buster /assets/img/recs/custom_attributes_test.png %}
[5]: {% image_buster /assets/img/recs/sample_response.png %}