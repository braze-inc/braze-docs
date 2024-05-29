---
nav_title: ルールベースの推奨事項
article_title: ルールベースの推奨事項
page_type: tutorial
page_order: 16
alias: "/rules_based_recommendations/"
description: "この記事では、カタログまたは接続コンテンツを使用するルールベースのレコメンドエンジンを作成する方法について説明します。"
tool:
  - Campaigns
  - Canvas

---

# ルールに基づく推奨事項

> ルールベースのレコメンドエンジンは、ユーザデータと製品情報を使用して、メッセージ内の関連する項目をユーザに提案します。これは、[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)を使用し、Braze [catalogs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/)または[Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)を使用して、ユーザーの動作と属性に基づいてコンテンツを動的にパーソナライズします。

Liquid、カタログ、およびConnected Content の詳細については、以下のBraze Learning コースを参照してください。

- [メールを使用したカスタマイズされた推奨事項](https://learning.braze.com/personalized-recommendations-with-email)
- [液体を使用したダイナミックパーソナライズ](https://learning.braze.com/path/dynamic-personalization-with-liquid)
- [接続コンテンツの基礎](https://learning.braze.com/path/dynamic-personalization-with-liquid/connected-content-fundamentals)

{% alert important %}
ルールベースの推奨事項は、手動で設定する必要がある固定ロジックに基づいています。つまり、ロジックを更新しない限り、おすすめはユーザの購入履歴や嗜好に合わせて調整されません。<br><br>ユーザの履歴に自動的に調整されるパーソナライズされたAI 推奨事項を作成するには、[AI 項目の推奨事項]({{site.baseurl}}/ai_item_recommendations) をチェックアウトします。
{% endalert %}

## カタログレコメンドエンジンの作成

1. [製品のカタログ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/)を作成します。
2. 製品ごとに、「product\_recommendations」という名前の列に、区切り文字で区切られた文字列(パイプ`|` など) として推奨製品のリストを追加します。
3. 推奨事項を見つける製品ID をカタログに渡します。
4. そのカタログアイテムの`product_recommendations` 値を取得し、Liquid split フィルタを使用して区切り文字で分割します。
5. 1 つ以上のID をカタログに戻して、他の製品の詳細を収集します。

### カタログのユースケース

ヘルスフードアプリがあり、ユーザーがアプリに登録されている期間に基づいて異なるレシピを送信するコンテンツカードキャンペーンを作成するとします。 

1. 以下の情報を含む、CSV を使用したカタログの作成とアップロード:<br>- **id:**ユーザーがアプリにサインアップしてからの日数に相関する一意の番号。たとえば、`3` は3 日間に相関します。<br>- **type:**レシピカテゴリ(`comfort`、`fresh`、その他)。<br>- **title:** IDごとに送信されるコンテンツカードのタイトル。「今週のランチを先にする」や「それについてタコをしよう」など。<br>- **link:** レシピ記事へのリンク。<br>- **image_url:**レシピに対応するイメージ。

{: start="2"}
2\.カタログがBrazeにアップロードされたら、選択した数のカタログアイテムのプレビューをチェックして、正確にインポートされた情報を確認します。アイテムはプレビューでランダム化される場合がありますが、これはレコメンドエンジンの出力には影響しません。

![][1]

{: start="3"}
3\.コンテンツカードキャンペーンを登録します。コンポーザーで、Liquid ロジックを入力して、キャンペーンを受信するユーザと表示するレシピおよびイメージを決定します。この使用例では、Braze はユーザの`start_date` (またはサインアップ) をプルし、現在の日付と比較します。日付の違いによって、送信されるコンテンツカードが決まります。 

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
4\.**クリック動作**セクションで、ユーザがiOS、Android、およびWebデバイスのコンテンツカードをクリックしたときにリダイレクトする場所の液体ロジックを入力します。 

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
5\.**Test**タブに進み、**カスタムユーザ**を**ユーザ**としてプレビューメッセージを選択します。**Custom attribute**フィールドに日付を入力して、その日付にサインアップしたユーザに送信されるコンテンツカードをプレビューします。<br><br>

![][4]

## 接続コンテンツレコメンドエンジンの作成

1. 次のいずれかの方法で、接続されたコンテンツエンドポイントを作成します。
- スプレッドシートをSheetDP のようなサービスを使用してJSON API エンドポイントに変換し、生成されるAPI URL に注意してください
- カスタム・ビルトイン・ハウス・エンドポイントのビルド、ホスト、および保守
- 弊社の[Alloy partners]({{site.baseurl}}/partners/message_personalization/dynamic_content) などのサードパーティパートナー経由で推奨エンジンを購入します。[Amazon Personalise]({{site.baseurl}}/partners/message_personalization/dynamic_content/amazon_personalize/)、[Certona]({{site.baseurl}}/partners/message_personalization/dynamic_content/certona/)、[Dynamic Yield]({{site.baseurl}}/partners/message_personalization/dynamic_content/dynamic_yield/) などが含まれます

2. Connected Content Liquid をメッセージ本文またはContent Block HTML エディタに書き込んで、エンドポイントを呼び出してデータベースを検索します。
3. 特定のユーザーのプロファイルで見つかったカスタム属性値に合わせて、リキッドを調整します。
4. その結果、正しい推奨事項を引き出します。

{% raw %}
\`\`\`
{% connected_content YOUR-API-URL :save items %}

{% assign recommended\_item\_ids\_from\_user\_profile = custom\_attribute.${RECOMMENDED\_ITEM\_IDS} | split: ';' %}

{% for item_id in recommended_item_ids_from_user_profile %}
  {% assign recommended_item = items | where: "ITEM_ID", ITEM_ID | first %}
  recommended\_item.item\_name
{% endfor %}
\`\`\`
{% endraw %}

| 属性| 置換|
| --- | --- |
|`YOUR-API-URL` | API の実際のURL で置き換えます。|
|`RECOMMENDED_ITEM_IDS` | 推奨アイテムのID を含むカスタム属性の実際の名前で置き換えます。この属性は、セミコロンで区切られたID の文字列であることが期待されます。|
|`ITEM_ID` | 項目ID に対応するAPI レスポンスの属性の実際の名前で置き換えます。|
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
これは基本的な例であり、特定のニーズとデータ構造に基づいてさらに変更する必要がある場合があります。詳細なガイダンスについては、[液体文書]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid)を参照するか、開発者にご相談ください。
{% endalert %}

## 接続コンテンツのユースケース

Zomato Restaurants データベースからレストランの推奨を引き出し、その結果を`restaurants` というローカル変数として保存するとします。次の接続コンテンツコールを発信できます。

{% raw %}
\`\`\`liquid

{% connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity\_type=city&count=20&cuisines={{food\_type}}&sort=rating:headers{“user-key”:“USER_KEY”} :save restaurants %}

{{city\_food.restaurants[0]}}
\`\`\`
{% endraw %}

次に、ユーザーの都市と食べ物のタイプに基づいてレストランのおすすめを引きたいとしましょう。これを行うには、コールの先頭にユーザの市区町村およびフードタイプのカスタム属性を動的に挿入し、`restaurants` の値を変数`city_food.restaurants` に割り当てます。

接続されたコンテンツコールは次のようになります。

{% raw %}
\`\`\`liquid
{% assign city\_id = {{custom\_attribute.${city\_id} | default:‘306’}} %}
{% assign food\_type = {{custom\_attribute.${food\_type} | default:‘471’}} %}

{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity\_type=city&count=20&cuisines={{food\_type}}&sort=rating:headers{“user-key”:“USER_KEY”} :save restaurants %}

{% assign restaurants = city_food.restaurants %}

{{city\_food.restaurants[0]}}
\`\`\`
{% endraw %}

レストランの名前と評価のみを取得するように応答を調整する場合は、以下のように、コールの最後にフィルタを追加できます。

{% raw %}
\`\`\`liquid
{% assign city\_id = {{custom\_attribute.${city\_id} | default:‘306’}} %}
{% assign food\_type = {{custom\_attribute.${food\_type} | default:‘471’}} %}

{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity\_type=city&count=20&cuisines={{food\_type}}&sort=rating:headers{“user-key”:”USER_KEY”} :save restaurants %}
{% assign restaurants = city_food.restaurants %}

{{city\_food.restaurants[0].restaurant.name}}
{{city\_food.restaurants[0].restaurant.user\_rating.rating\_text}}
\`\`\`
{% endraw %}

最後に、レストランのおすすめを評価別にグループ化したいとしましょう。次の手順を実行します。

1. `assign` を使用して、"excellent"、"very good"、および"good" のカテゴリを評価するための空白配列を作成します。
2. リスト内の各レストランの評価を調べる`for` ループを追加します。 
- 評価が"Excellent" の場合は、`excellent_restaurants` 文字列にレストラン名を追加し、最後に* 文字を追加して各レストラン名を区切ります。 
- 評価が「Very Good」の場合は、`very_good_restaurants` 文字列にレストラン名を追加し、最後に* 文字を追加します。
- 評価が"Good" の場合は、`good_restaurants` 文字列にレストラン名を追加し、最後に* を追加します。
3. レストランのおすすめの返却数は、カテゴリごとに4つに制限してください。

最後の呼び出しは次のようになります。

{% raw %}
\`\`\`liquid
{% assign city\_id = {{custom\_attribute.${city\_id} | default:‘306’}} %}
{% assign food\_type = {{custom\_attribute.${food\_type} | default:‘471’}} %}
{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity\_type=city&count=20&cuisines={{food\_type}}&sort=rating:headers{“user-key”:”USER_KEY”} :save restaurants %}
{% assign restaurants = city_food.restaurants %}
{% assign excellent_restaurants = “” %}
{% assign very_good_resturants = “” %}
{% assign good_restaurants = “” %}
{% for list in restaurants %}
{% if {{list.restaurant.user\_rating.rating\_text}} == `Excellent` %}
{% assign excellent\_restaurants = excellent\_restaurants | append: list.restaurant.name | append: `*` %}
{% elseif {{list.restaurant.user\_rating.rating\_text}} == `Very Good` %}
{% assign very\_good\_restaurants = very\_good\_restaurants | append: list.restaurant.name | append: `*` %}
{% elseif {{list.restaurant.user\_rating.rating\_text}} == `Good` %}
{% assign good\_restaurants = good\_restaurants | append: list.restaurant.name | append: `*` %}
{% endif %}
{% endfor %}
{% assign excellent\_array = excellent\_restaurants | split: `*` %}
{% assign very\_good\_array = very\_good\_restaurants | split: `*` %}
{% assign good\_array = good\_restaurants | split: `*` %}

すばらしい場所
{% for list in excellent_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}

とても良い場所
{% for list in very_good_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}

良い場所
{% for list in good_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}
\`\`\`
{% endraw %}

ユーザーのデバイスに応答がどのように表示されるかの例については、以下のスクリーンショットを参照してください。

![][5]{: style="max-width:30%;"}

## 考慮事項

使用可能なリソースおよびユースケースに適した推奨エンジンを決定する場合は、次の考慮事項の表を参照してください。

| 考慮事項| Liquid | Catalogs CSV | Catalogs API | 接続コンテンツ|
| --- | --- | --- | --- | --- |
| データポイントを消費しない| サポートされない| サポートされる|
| No code solution | Not supported | 事前に生成された液体の場合はSupported | Not supported | Not supported |
| 頻繁に必要な高度な液体| サポート| サポートされない| サポートされない| サポートされない| サポートされる|
| 製品フィードのデータへの更新| サポートなし| 推奨が頻繁に更新されない場合はサポート| 推奨が1 時間ごとに更新され、推奨がリアルタイムに更新される場合はサポート|
| Braze UI で推奨事項を生成| Supported | Supported | Supported | Braze の外部で生成された場合、サポートなし|
| ホストなし、管理、トラブルシューティングの推奨データ| Supported | Supported | Supported | 非サポート|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

[1]: {% image_buster /assets/img/recs/catalog_items.png %}
[2]: {% image_buster /assets/img/recs/content_card_preview.png %}
[3]: {% image_buster /assets/img/recs/on_click_behavior.png %}
[4]: {% image_buster /assets/img/recs/custom_attributes_test.png %}
[5]: {% image_buster /assets/img/recs/sample_response.png %}