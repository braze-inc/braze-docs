---
nav_title: 永続的なエントリプロパティ
article_title: 永続的なエントリプロパティ
alias: "/persistent_entry/"
page_type: reference
description: "この記事では、キャンバスで永続的なエントリプロパティを使用して、よりキュレートされたメッセージを送信し、高度に洗練されたエンドユーザーエクスペリエンスを作成する方法について説明します。"
tool: Canvas
page_order: 5
---

# 永続的なエントリプロパティ

> キャンバスがカスタムイベント、購入、または API 呼び出しによってトリガーされる際、キャンバスワークフローの各ステップでのパーソナライゼーションに、API 呼び出し、カスタムイベント、購入イベントからのメタデータを使用することができます。 

この機能がリリースされる前は、キャンバスの最初のステップでのみエントリプロパティを使用できました。キャンバスジャーニー全体でエントリープロパティを使用できるようになり、よりキュレートされたメッセージを顧客に送信し、高度に洗練されたエンドユーザーエクスペリエンスを作成することが可能になりました。

## エントリプロパティを使用する

エントリプロパティは、アクションベースおよび API トリガーのキャンバスで使用できます。これらのエントリプロパティは、キャンバスがカスタムイベント、購入、または API 呼び出しによってトリガーされた時点で定義されます。詳細については、次の記事を参照してください。

- [キャンバスエントリのプロパティオブジェクト]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)
- [イベントのプロパティオブジェクト]({{site.baseurl}}/api/objects_filters/event_object/)
- [購入対象]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-product_id)

これらのオブジェクトから渡されるプロパティは、Liquid タグ `canvas_entry_properties` を使用して参照できます。例えば、`\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}` を使ったリクエストの場合、{% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %} という Liquid を追加して、メッセージに「shoes」という単語を追加できます。

キャンバスに Liquid タグ `canvas_entry_properties` を持つメッセージが含まれている場合、これらのプロパティに関連付けられている値は、ユーザーのジャーニーの間保持され、ユーザーがキャンバスを退出したときに削除されます。キャンバスエントリのプロパティは、Liquid で参照用にのみ使用できる点に注意してください。キャンバス内のプロパティをフィルタリングするには、代わりに[イベントプロパティのセグメンテーション]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/)を使用します。

{% alert note %}
キャンバスエントリのプロパティオブジェクトの最大サイズは 50 KB に制限されています。
{% endalert %}

## エントリプロパティを使用するようにキャンバスを更新する

`canvas_entry_properties` を使用するメッセージを含まないアクティブなキャンバスを編集して `canvas_entry_properties` を含めた場合、`canvas_entry_properties` がキャンバスに追加される前にキャンバスに入ったユーザーは、そのプロパティに対応する値を使用できません。変更後にキャンバスに入ったユーザーのみ、これらの値が保存されます。

例えば、11 月 3 日にエントリプロパティを使用しなかったキャンバスを最初に開始した後で 11 月 11 日に新しいプロパティ `product_name` をキャンバスに追加した場合、`product_name` の値は、11 月 11 日以降にキャンバスに入ったユーザーにのみ保存されます。

キャンバスエントリのプロパティが null または空白の場合、条件を使用してメッセージを中止することができます。次のコードスニペットは、Liquid を使用してメッセージを中止する方法の例を示します。
{%raw%}
```
{% if canvas_entry_properties.${product_name} == blank %}
{% abort_message() %}
{% endif %}
```
{%endraw%}

Liquid を使用したメッセージの中止の詳細については、[Liquid のドキュメント]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages)を参照してください。

## グローバルキャンバスのエントリのプロパティ

`canvas_entry_properties` では、すべてのユーザーに適用されるグローバルプロパティを設定するか、指定のユーザーのみに適用されるユーザー固有のプロパティを設定することができます。ユーザー固有のプロパティは、そのユーザーのグローバルプロパティより優先されます。

### リクエスト例

```
url -X POST \
-H 'Content-Type:application/json' \
-d '{
      "api_key": "a valid rest api key",
      "canvas_id": "the ID of your Canvas",
         "canvas_entry_properties": {
            "food_allergies": "none"
          },
      "recipients": [
        {
          "external_user_id": Customer_123,
          "canvas_entry_properties": {
            "food_allergies": ["dairy", "soy"],
            "nutrition": {
              "calories_per_serving": 200,
              "serving_size_in_ounces": 4
            }
          }
        }
      ]
    }' \
```
 
このリクエストでは、「food allergies」のグローバル値は「none」です。Customer_123 の場合、値は「dairy」です。Liquid スニペットの {%raw%}`{{canvas_entry_properties.${food_allergies}}}`{%endraw%} を含むこのキャンバスのメッセージでは、「Customer_123」に「dairy」、他のすべてのユーザーには「none」がテンプレート化されます。 

## ユースケース

ユーザーが e コマースサイトでアイテムをブラウズした後に、そのアイテムをカートに追加しないときにトリガーされるキャンバスがある場合、キャンバスの最初のステップを、アイテムの購入に興味があるかどうかを尋ねるプッシュ通知にすることができます。製品名は、{% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %} を使用して参照できます。

![]({% image_buster /assets/img/persistent_entry_properties/PEP1.png %}){: style="border:0;margin-left:15px;"}

2 番目のステップでは、ユーザーがカートにアイテムを追加したにもかかわらず、まだ購入していない場合、別のプッシュ通知を送信してチェックアウトするように促すことができます。`product_name` エントリプロパティは、引き続き {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %} を使用して参照できます。

![]({% image_buster /assets/img/persistent_entry_properties/PEP12.png %}){: style="border:0;margin-left:15px;"}

