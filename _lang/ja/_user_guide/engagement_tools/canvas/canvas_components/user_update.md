---
nav_title: ユーザーの更新 
article_title: ユーザーの更新 
alias: "/user_update/"
page_order: 6
page_type: reference
description: "この記事では、ユーザー更新コンポーネントの概要と、そのキャンバスでの使用方法を説明します。"
tool: Canvas
---

# ユーザーの更新 

![][1]{: style="float:right;max-width:45%;margin-left:15px;"}

> ユーザーの更新コンポーネントを使用すると、JSON コンポーザーでユーザーの属性、イベント、購入を更新できるため、API キーなどの機密情報を含める必要はありません。

ユーザーの更新では、更新はユーザーごとにカウントされません。1 分あたりのレート制限を追跡してください。代わりに、Braze ではこれらの更新がバッチ処理されるので、Braze-to-Braze の Webhook よりも効率的に処理することができます。このコンポーネントは、請求対象外のデータポイント (サブスクリプショングループなど) の更新に使用される場合、[データポイント]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/)を消費しないことに注意してください。

ユーザーは、関連するユーザーの更新が完了した後でのみ、次のキャンバスステップに進みます。後続のメッセージングが作成中のユーザー更新に依存している場合は、メッセージが送信される前にこれらの更新が完了していることを確認できます。

## ユーザーの更新を作成する

サイドバーからコンポーネントをドラッグ＆ドロップするか、バリアントまたはステップの一番下にある <i class="fas fa-plus-circle"></i> プラスのボタンをクリックし、[**ユーザーの更新**] を選択します。 

既存のユーザープロファイルの更新、新規追加、ユーザープロファイル情報の削除を行える 3 つのオプションがあります。ワークスペース内のユーザー更新ステップをすべて組み合わせると、1 分あたり最大 200,000 のユーザープロファイルを更新できます。

{% alert tip %}
このコンポーネントで行った変更をテストするには、ユーザーを検索し、その変更を適用します。するとユーザーが更新されます。
{% endalert %}

### カスタム属性を更新する

カスタム属性を追加や更新するには、属性のリストから属性名を選択し、キー値を入力します。

![][4]{: style="max-width:90%;"}

### カスタム属性を削除する

カスタム属性を削除するには、ドロップダウンを使用して属性名を選択します。高度な JSON コンポーザーに切り替えて、さらに編集することができます。 

![][5]{: style="max-width:90%;"}

### 高度な JSON コンポーザー

JSON コンポーザーには最大 65,536 文字の属性、イベント、または購入 JSON オブジェクトを追加できます。ユーザーの[グローバルサブスクリプション]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states)および[サブスクリプショングループ]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups)の状態も設定できます。

![][2]{: style="max-width:90%;"}

高度なコンポーザーでは、[**プレビュー後にテスト**] タブを使用してユーザープロファイルの変更をプレビューしてテストすることもできます。ランダムなユーザーを選択するか、特定のユーザーを検索できます。次に、テストをユーザーに送信した後、生成されたリンクを使用してユーザープロファイルを表示します。

![][6]{: style="max-width:90%;"}

#### 制限事項

JSON コンポーザーの使用中に API キーのような機密データを含める必要はありません。これはプラットフォームによって自動的に提供されます。そのため、以下のフィールドは不要です。JSON コンポーザーでは使用しないでください。
\* 外部ユーザー ID
\* API キー
\* Braze クラスターの URL
\* プッシュトークンのインポートに関連するフィールド

{% raw %}
#### カスタムイベントをログに記録する

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

#### サブスクリプションの状態を編集する

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

#### サブスクリプショングループを更新する 

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

## ユースケース

### キャンバスのエントリプロパティを属性として設定する

ユーザーの更新ステップを使用して、`canvas_entry_property` を永続的に保存できます。 例えば、アイテムがカートに追加されたときにトリガーされるイベントがあるとします。カートに追加された最新のアイテムの ID を保存し、それをリマーケッティングキャンペーンに使用できます。パーソナライゼーション機能を使用して、キャンバスのエントリプロパティを取得し、属性に保存します。

![][8]{: style="max-width:90%;"}

#### パーソナライゼーション

キャンバスのトリガーイベントのプロパティを属性として保存するには、パーソナライゼーションモーダルを使ってキャンバスのエントリプロパティを抽出し、保存します。ユーザーの更新では、次のパーソナライゼーション機能もサポートされています。
* [コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)
* [コンテンツブロック]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)
* [エントリのプロパティ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/)
\* Liquid ロジック ([メッセージの中止]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/)を含む)
\* オブジェクトごとに複数の属性またはイベントの更新

{% alert warning %}
ユーザーの更新ステップでは、コネクテッドコンテンツの Liquid パーソナライゼーションを慎重に使用することをお勧めします。このステップタイプのレート制限は 1 分あたり 200,000 件です。このレート制限は、キャンバスのレート制限をオーバーライドします。
{% endalert %}

### 増分数

このコンポーネントを使用して、ユーザーがイベントを実行した回数を増減数で追跡することもできます。例えば、ユーザーが 1 週間に受講したクラスの数を追跡できます。このコンポーネントを使用すると、クラスカウントを週の始めにリセットして、再びトラッキングを開始できます。 

![][7]{: style="max-width:90%;"}

### 配列に追加する

配列の項目を追加や削除したり、項目を削除したりできます。例えば、このステップを使用してウィッシュリストに項目を追加したり削除したりできます。

![][9]{: style="max-width:90%;"}

[1]: {% image_buster /assets/img_archive/canvas_user_update_step.png %}
[2]: {% image_buster /assets/img_archive/canvas_user_update_composer.png %}
[3]: {% image_buster /assets/img_archive/canvas_user_update_example.png %}
[4]: {% image_buster /assets/img_archive/canvas_user_update_update.png %}
[5]: {% image_buster /assets/img_archive/canvas_user_update_remove.png %}
[6]: {% image_buster /assets/img_archive/canvas_user_update_test_preview.png %}
[7]: {% image_buster /assets/img_archive/canvas_user_update_increment.png %}
[8]: {% image_buster /assets/img_archive/canvas_user_update_cep.png %}
[9]: {% image_buster /assets/img_archive/canvas_user_update_wishlist.png %} 
