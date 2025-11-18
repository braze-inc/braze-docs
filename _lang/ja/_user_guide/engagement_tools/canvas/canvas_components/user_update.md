---
nav_title: ユーザ更新
article_title: ユーザーの更新 
alias: "/user_update/"
page_order: 6
page_type: reference
description: "この記事では、ユーザー更新コンポーネントの概要と、そのキャンバスでの使用方法を説明します。"
tool: Canvas
---

# ユーザーの更新 

> ユーザーの更新コンポーネントを使用すると、JSON コンポーザーでユーザーの属性、イベント、購入を更新できるため、API キーなどの機密情報を含める必要はありません。

## このコンポーネントの仕組み

<<<<<<< HEAD
![" 更新 ロイヤルティ" 更新は属性 " Is Premium Member" to " true" という名前のユーザ更新 ステップ。]({% image_buster /assets/img_archive/canvas_user_update_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}
=======
\![" 更新 ロイヤルティ" 更新は属性 " Is Premium Member" to " true" という名前のユーザ更新 ステップ。]({% image_buster /assets/img_archive/canvas_user_update_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}
>>>>>>> main

キャンバスでこのコンポーネントを使用する場合、更新は 1 分あたり`/users/track` 件のリクエストのレート制限にはカウントされません。代わりに、Braze ではこれらの更新がバッチ処理されるので、Braze-to-Braze の Webhook よりも効率的に処理することができます。このコンポーネントは、請求不可能なデータポイントs (サブスクリプショングループ s など) を更新するために使用されている場合、[データポイント s]({{site.baseurl}}/user_guide/data/data_points/) を記録しないことに注意してください。

ユーザーは、関連するユーザーの更新が完了した後でのみ、次のキャンバスステップに進みます。つまり、これらのユーザー更新に依存する後続のメッセージングは、次のステップが実行された時点で最新の状態になります。

## ユーザーアップデートを作成する

サイドバーからコンポーネントをドラッグ＆ドロップするか、バリアントまたはステップの一番下にある <i class="fas fa-plus-circle"></i> プラスのボタンをクリックし、[**ユーザーの更新**] を選択します。 

既存のユーザープロファイルの更新、新規追加、ユーザープロファイル情報の削除を行える 3 つのオプションがあります。ワークスペース内のユーザー更新ステップをすべて組み合わせると、1 分あたり最大 200,000 のユーザープロファイルを更新できます。

{% alert tip %}
このコンポーネントで行った変更をテストするには、ユーザーを検索し、その変更を適用します。するとユーザーが更新されます。
{% endalert %}

### カスタム属性を更新する

カスタム属性を追加や更新するには、属性のリストから属性名を選択し、キー値を入力します。

<<<<<<< HEAD
![2 つの属性s "ロイヤルティメンバー"および"ロイヤルティプログラム" to "true"を更新するユーザ更新 ステップ。]({% image_buster /assets/img_archive/canvas_user_update_update.png %}){: style="max-width:90%;"}
=======
\![2 つの属性s "ロイヤルティメンバー"および"ロイヤルティプログラム" to "true"を更新するユーザ更新 ステップ。]({% image_buster /assets/img_archive/canvas_user_update_update.png %}){: style="max-width:90%;"}
>>>>>>> main

### カスタム属性を削除する

カスタム属性を削除するには、ドロップダウンを使用して属性名を選択します。[高度な JSON コンポーザー](#advanced-json-composer)に切り替えて、さらに編集することができます。 

<<<<<<< HEAD
![属性 &クォートを削除するユーザアップデートステップ;ロイヤルティメンバー&クォート;。]({% image_buster /assets/img_archive/canvas_user_update_remove.png %}){: style="max-width:90%;"}
=======
\![属性 &クォートを削除するユーザアップデートステップ;ロイヤルティメンバー&クォート;。]({% image_buster /assets/img_archive/canvas_user_update_remove.png %}){: style="max-width:90%;"}
>>>>>>> main

### 増加値と減少値

ユーザー更新ステップによって属性値を増減させることが可能です。属性を選択し、[**増分**] または [**減分**] を選択して数値を入力します。 

#### 週次の進捗状況を追跡する

イベントを追跡するカスタム属性をインクリメントすることで、ユーザーが1週間に受講したクラス数を追跡することができる。このコンポーネントを使用すると、クラスカウントを週の始めにリセットして、再びトラッキングを開始できます。 

<<<<<<< HEAD
![属性"class_count" を1 つ増分するユーザアップデートステップ。]({% image_buster /assets/img_archive/canvas_user_update_increment.png %}){: style="max-width:90%;"}
=======
\![属性"class_count" を1 つ増分するユーザアップデートステップ。]({% image_buster /assets/img_archive/canvas_user_update_increment.png %}){: style="max-width:90%;"}
>>>>>>> main

### オブジェクトの配列を更新する

[オブジェクトの配列は]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/)、データ豊富なユーザープロファイルに保存されるカスタム属性である。これにより、ユーザーとあなたのブランドとのインタラクションの履歴を作成することができる。これにより、購入履歴やライフタイムバリューの合計など、計算フィールドであるカスタム属性に基づいてセグメントを作成することができる。

ユーザー更新ステップによって、このオブジェクトの配列に属性を追加したり削除したりすることが可能です。配列を更新するには、属性リストから配列属性名を選択し、キー値を入力する。

#### ユースケース:ユーザーのウィッシュリストを更新する

配列にアイテムを追加または削除すると、ユーザーのウィッシュリストが更新される。

<<<<<<< HEAD
![アイテム&クォート;sun ブロック" を属性"items_in_wishlist".]({% image_buster /assets/img_archive/canvas_user_update_wishlist.png %} に追加するユーザアップデートステップ]{: style="max-width:90%;"}
=======
\![アイテム&クォート;sun ブロック" を属性"items_in_wishlist".]({% image_buster /assets/img_archive/canvas_user_update_wishlist.png %} に追加するユーザアップデートステップ]{: style="max-width:90%;"}
>>>>>>> main

#### ユースケース:ショッピングカートの合計を計算する

ユーザーがいつショッピングカートに商品を入れたか、いつ新しい商品を入れたか、いつ商品を削除したか、ショッピングカートの合計金額はいくらかなどを追跡する。 

1. `shopping_cart` というオブジェクトのカスタム配列を作成する。次の例は、この属性がどのように見えるかを示している。各アイテムは、`price` を含むオブジェクトの独自の階層化配列に、より複雑なデータを持つユニークな `product_id` を持っています。

{% raw %}
```javascript
{
  "attributes": [
    {
      "shopping_cart": [
       {
         "total_cart_value": number,
         "shipping": number,
         "items_in_cart": number,
         "product_id": array,
         "gift": boolean,
         "discount_code": "enum",
         "timestamp": {"$time" : "{{$isoTimestamp}}"},
       }
      ]
    }
  ]
}
```
{% endraw %}

{:start="2"}
2\.ユーザーがバスケットに商品を追加したときに記録される`add_item_to_cart` という[カスタムイベントを]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)作成する。
3\.このカスタムイベントで、ターゲットとなるユーザーとキャンバスを作成します。さて、ユーザーが商品をカートに入れると、このキャンバスがトリガーされる。その後、そのユーザーを直接ターゲットにしたメッセージングを行い、一定の支出額に達したとき、一定の期間カートを放棄したとき、あるいはその他のユースケースに一致したときに、クーポンコードを提供することができます。 

`shopping_cart` 属性は、多くのカスタムイベントの合計を運ぶ：すべてのアイテムの合計金額、カート内のアイテムの合計数、ショッピングカートにギフトが含まれている場合など。例えば、次のようになります。

{% raw %}
```javascript
{
  "attributes": [
    {
      "shopping_cart": [
       {
         "total_cart_value": 22.99,
         "shipping": 4.99,
         "items_in_cart": 2,
         "product_id": ["1001", "1002"]
         "gift": yes,
         "discount_code": "flashsale1000",
         "timestamp": {"$time" : "{{$isoTimestamp}}"},
       }
      ]
    }
  ]
}
```
{% endraw %}

## キャンバス・エントリーのプロパティを属性として設定する

ユーザーの更新ステップを使用して、`canvas_entry_property` を永続的に保存できます。例えば、アイテムがカートに追加されたときにトリガーされるイベントがあるとします。カートに追加された最新のアイテムの ID を保存し、それをリマーケッティングキャンペーンに使用できます。パーソナライゼーション機能を使用して、キャンバスのエントリプロパティを取得し、属性に保存します。

<<<<<<< HEAD
![アイテムID で属性"most_recent_cart_item" を更新するユーザー更新 ステップ。]({% image_buster /assets/img_archive/canvas_user_update_cep.png %}){: style="max-width:90%;"}
=======
\![アイテムID で属性"most_recent_cart_item" を更新するユーザー更新 ステップ。]({% image_buster /assets/img_archive/canvas_user_update_cep.png %}){: style="max-width:90%;"}
>>>>>>> main

### パーソナライゼーション

キャンバスのトリガーイベントのプロパティを属性として保存するには、パーソナライゼーションモーダルを使ってキャンバスのエントリプロパティを抽出し、保存します。ユーザーの更新では、次のパーソナライゼーション機能もサポートされています。 
* [コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) 
* [コンテンツブロック]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)
* [エントリのプロパティ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/)
* Liquid ロジック ([メッセージの中止]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/)を含む)
* オブジェクトごとに複数の属性またはイベントを更新する

{% alert warning %}
ユーザーの更新ステップでは、コネクテッドコンテンツの Liquid パーソナライゼーションを慎重に使用することをお勧めします。このステップタイプのレート制限は 1 分あたり 200,000 件です。このレート制限は、キャンバスのレート制限をオーバーライドします。
{% endalert %}

## 高度な JSON コンポーザー

JSON コンポーザーには最大 65,536 文字の属性、イベント、または購入 JSON オブジェクトを追加できます。ユーザーの[グローバルサブスクリプション]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states)および[サブスクリプショングループ]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups)の状態も設定できます。

\![]({% image_buster /assets/img_archive/canvas_user_update_composer.png %}){: style="max-width:90%;"}

高度なコンポーザーでは、[**プレビュー後にテスト**] タブを使用してユーザープロファイルの変更をプレビューしてテストすることもできます。ランダムなユーザーを選択するか、特定のユーザーを検索できます。次に、テストをユーザーに送信した後、生成されたリンクを使用してユーザープロファイルを表示します。

\![]({% image_buster /assets/img_archive/canvas_user_update_test_preview.png %}){: style="max-width:90%;"}

### 考慮事項

JSON コンポーザーの使用中に API キーのような機密データを含める必要はありません。これはプラットフォームによって自動的に提供されます。そのため、以下のフィールドは不要です。JSON コンポーザーでは使用しないでください。
* 外部ユーザ ID
* APIキー
* BrazeクラスタURL
* プッシュトークンのインポートに関連するフィールド

{% raw %}
### カスタムイベントをログに記録する

JSON コンポーザーを使用して、カスタムイベントを記録することもできます。これには ISO 形式のタイムスタンプが必要なので、最初に Liquid で日付と時刻を割り当てる必要があります。次の例は、イベントを時刻とともに記録します。

```
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
  "events": [
    {
      "name": "logged_user_event",
      "time": "{{timestamp}}"
    }
  ]
}
```

次の例は、オプションのプロパティと `app_id` を持つカスタムイベントを使用して、イベントを特定のアプリにリンクします。

```
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
  "events": [
    {
      "app_id": "insert_app_id",
      "name": "rented_movie",
      "time": "{{timestamp}}",
      "properties": {
        "release": {
          "studio": "FilmStudio",
          "year": "2022"
        },
        "cast": [
          {
            "name": "Actor1"
          },
          {
            "name": "Actor2"
          }
        ]
      }
    }
  ]
}
```

### サブスクリプションの状態を編集する

JSON コンポーザー内で、ユーザーのサブスクリプションの状態を編集することもできます。次の例は、ユーザーのサブスクリプション状態を `opted_in` に更新しています。 

```
{
  "attributes": [
    {
      "email_subscribe": "opted_in"
    }
  ]
}
```

### サブスクリプショングループを更新する 

このキャンバスステップを使用して、サブスクリプショングループを更新することもできます。次の例は、サブスクリプショングループへの更新を示しています。1 つまたは複数のサブスクリプショングループ更新を実行できます。

```
{
  "attributes": [
    {
      "subscription_groups": [
        {
          "subscription_group_id": "subscription_group_identifier_1",
          "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_2",
          "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_3",
          "subscription_state": "subscribed"
        }
      ]
    }
  ]
}
```
{% endraw %}

