---
nav_title: ユーザー更新
article_title: ユーザーの更新 
alias: "/user_update/"
page_order: 12
page_type: reference
description: "この記事では、ユーザー更新コンポーネントの概要と、そのキャンバスでの使用方法を説明します。"
tool: Canvas
---

# ユーザーの更新 

> ユーザー更新コンポーネントでは、ユーザーの属性、イベント、購入履歴をJSONエディタで更新できる。そのため、API キーのような機密情報を記載する必要はない。

## このコンポーネントの仕組み

![「Updateロイヤルティ」という名前のユーザー更新ステップで、属性「Is Premium Member」を「true」に更新する。]({% image_buster /assets/img_archive/canvas_user_update_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

キャンバスでこのコンポーネントを使用する場合、更新は 1 分あたり`/users/track` 件のリクエストのレート制限にはカウントされません。代わりに、Braze ではこれらの更新がバッチ処理されるので、Braze-to-Braze の Webhook よりも効率的に処理することができます。このコンポーネントは、課金対象外のデータポイント（サブスクリプショングループなど）を更新する際に使用される場合[、データポイントを]({{site.baseurl}}/user_guide/data/data_points/)ログに記録しないことに注意せよ。

ユーザーがユーザー更新ステップに入り、処理が完了すると、次のステップに進む。これは、これらのユーザー更新に依存する後続のメッセージングは、次のステップが実行される時点で最新の状態であることを意味する。

## ユーザーアップデートを作成する

サイドバーからコンポーネントをドラッグ＆ドロップするか、バリアントまたはステップの下部にあるプラス<i class="fas fa-plus-circle"></i>ボタンを選択し、**「ユーザー更新」**を選ぶ。 

既存のユーザープロファイル情報を更新する、新しい情報を追加する、あるいはユーザープロファイル情報を削除する、という三つの選択肢がある。ワークスペース内のユーザー更新ステップをすべて組み合わせると、1 分あたり最大 200,000 のユーザープロファイルを更新できます。

{% alert tip %}
このコンポーネントで行った変更をテストするには、ユーザーを検索し、その変更を適用します。するとユーザーが更新されます。
{% endalert %}

## カスタム属性を更新する

カスタム属性を更新または削除するには、属性リストから属性名を選択し、値を入力する。

![ユーザー更新ステップは、「ロイヤルティ会員」と「ロイヤルティプログラム」の2つの属性を「true」に更新する。]({% image_buster /assets/img_archive/canvas_user_update_update.png %}){: style="max-width:90%;"}

## カスタム属性を削除する

カスタム属性を削除するには、ドロップダウンを使用して属性名を選択します。詳細な編集を行うには[、高度なJSONエディタ](#advanced-json-editor)に切り替えることができる。 

![ユーザー更新ステップで「ロイヤルティメンバー」属性を削除する。]({% image_buster /assets/img_archive/canvas_user_update_remove.png %}){: style="max-width:90%;"}

### 増加値と減少値

ユーザー更新ステップでは、属性値を増減させることができる。属性を選択し、[**増分**] または [**減分**] を選択して数値を入力します。 

#### 週次の進捗状況を追跡する

イベントを追跡するカスタム属性をインクリメントすることで、ユーザーが1週間に受講したクラス数を追跡することができる。このコンポーネントを使用すると、クラスカウントを週の始めにリセットして、再びトラッキングを開始できます。 

![属性を"class_count"１ずつ増加させるユーザー更新ステップ。]({% image_buster /assets/img_archive/canvas_user_update_increment.png %}){: style="max-width:90%;"}

### オブジェクトの配列を更新する

[オブジェクトの配列]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/)は、ユーザープロファイルに保存されるデータ豊富なカスタム属性である。これを使って、ユーザーが自社ブランドと行ったやり取りの履歴を作成できる。また、購入履歴や生涯価値総額といった計算フィールドに基づいてセグメントを作成することも可能だ。

**高度なJSONエディタ**オプションを使用すれば、このオブジェクト配列に項目を追加したり削除したりするためにJSONを挿入できる。

#### ユースケース:ユーザーのウィッシュリストを更新する

ユーザーのウィッシュリストをトラッキングし、保存されたアイテムに基づいてセグメンテーションやパーソナライゼーションを行う。

1. オブジェクトの配列であるカスタム属性を生成する。例えば`wishlist`。各オブジェクトは、フィールドやフィールド`product_name``product_id`などを含む`added_at`ことができる。
2. ユーザー更新ステップで、**高度なJSONエディター**を選択する。次に、**コンポーズ**セクションで、演算`$add`子 `append` を使って項目を追加するか、演算`$remove`子 \`remove\` を使って値で項目を削除する。

以下はウィッシュリストにアイテムを追加する例だ：

{% raw %}
```json
{
  "attributes": [
    {
      "wishlist": {
        "$add": [
          {
            "product_id": "SKU-123",
            "product_name": "Wireless Headphones",
            "added_at": "{{$isoTimestamp}}"
          }
        ]
      }
    }
  ]
}
```
{% endraw %}

アイテムを削除するには、同じオブジェクト構造で  `"wishlist": { "$remove": [ { "product_id": "SKU-123", ... } ] }`を使用する。そうすればBrazeが一致させて削除できる。

#### ユースケース:ショッピングカートの合計を計算する

ユーザーがいつショッピングカートに商品を入れたか、いつ新しい商品を入れたか、いつ商品を削除したか、ショッピングカートの合計金額はいくらかなどを追跡する。 

1. オブジェクトの配列をカスタムで作成する`shopping_cart`。次の例は、この属性がどのように見えるかを示している。各項目には固有の識別子`product_id`があり、その識別子には独自のオブジェクトのネストされた配列に追加データが含まれている。これには`price`...も含まれる。

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
3\.このカスタムイベントを実行するユーザーを対象とするキャンバスを作成する。さて、ユーザーが商品をカートに入れると、このキャンバスがトリガーされる。その後、そのユーザーを直接ターゲットにしたメッセージングを行い、一定の支出額に達したとき、一定の期間カートを放棄したとき、あるいはその他のユースケースに一致したときに、クーポンコードを提供することができます。 

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
         "product_id": ["1001", "1002"],
         "gift": true,
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

![ユーザー更新ステップは、属性にアイテム"most_recent_cart_item"IDを割り当てる。]({% image_buster /assets/img_archive/canvas_user_update_cep.png %}){: style="max-width:90%;"}

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

## 高度なJSONエディタ

JSONエディタに、最大65,536文字の属性、イベント、または購入JSONオブジェクトを追加する。ユーザーの[グローバルサブスクリプション]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states)および[サブスクリプショングループ]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups)の状態も設定できます。

![]({% image_buster /assets/img_archive/canvas_user_update_composer.png %}){: style="max-width:90%;"}

JSONエディタを使えば、**プレビューとテスト**タブでユーザープロファイルが変更内容で更新されることをプレビューしテストすることもできる。ランダムなユーザーを選択するか、特定のユーザーを検索できます。次に、テストをユーザーに送信した後、生成されたリンクを使用してユーザープロファイルを表示します。

![]({% image_buster /assets/img_archive/canvas_user_update_test_preview.png %}){: style="max-width:90%;"}

### 考慮事項

JSONエディタを使用する際、API キーのような機密データを含める必要はない。これはプラットフォームによって自動的に提供されるからだ。以下のフィールドはJSONエディタに含めるべきではない：
* 外部ユーザ ID
* APIキー
* BrazeクラスタURL
* プッシュトークンのインポートに関連するフィールド

{% alert important %}
キャンバスのプロパティ（例えば、`canvas_id`Liquidタグの```canvas_name`、\``canvas_variant_name``、``など）は、ユーザー更新ステップではサポートされていない。
{% endalert %}

{% raw %}
### カスタムイベントをログに記録する

JSONエディタを使えば、カスタムイベントも記録できる。注意せよ、これはISO形式のタイムスタンプを必要とする。したがって、最初にLiquidで日時を割り当てる必要がある。次の例は、イベントを時刻とともに記録します。

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

JSONエディタ内では、ユーザーのサブスクリプション状態も編集できる。次の例は、ユーザーのサブスクリプション状態を `opted_in` に更新しています。 

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

このキャンバスステップを使用して、サブスクリプショングループを更新することもできます。以下の例は、1つ以上のサブスクリプショングループを更新する方法を示す。

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

