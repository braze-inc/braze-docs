キャンバス ユーザー ジャーニーでは、キャンバス エントリ プロパティとイベント プロパティを使用できる。

{% tabs local %}
{% tab Canvas Entry Properties %}

[キャンバスエントリのプロパティ]({{site.baseurl}}/api/objects_filters/context_object/)は、アクションベースまたは API でトリガーされるキャンバスにマップするプロパティです。`canvas_entry_properties` オブジェクトのサイズ上限は 50 KB であることに注意してください。

{% alert note %}
特にアプリ内メッセージチャネルでは、`context` はキャンバス内でのみ参照できます。
{% endalert %}

このLiquidフォーマットで、どのメッセージステップ``{% raw %} context.${property_name} {% endraw %}``でも`context`参照できる：このように使用するには、イベントがカスタムイベントまたは購入イベントでなければならないことに注意してください。

#### ユースケース

{% raw %}
小売店である RetailApp に対してリクエスト `\"context\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}` があるとします。 

RetailAppはこのLiquidで商品名（靴）をメッセージに挿入できる：`{{context.${product_name}}}`
{% endraw %}

RetailApp は、ユーザーが購入イベントをトリガーした後に、キャンバス内の異なる `product_name` プロパティに対して特定のメッセージをトリガーして送信することもできます。たとえば、次の Liquid をメッセージステップに追加することで、靴を購入したユーザーと別のものを購入したユーザーに異なるメッセージを送ることができます。

{% raw %}
```markdown
{% if  {{context.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add more items to your cart for the same discounts.
{% endif %}

```
{% endraw %}

{% details Expand for original Canvas editor %}

元のエディターを使用したキャンバスの作成や複製はできなくなりました。このセクションは参照のみを目的としています。オリジナルのエディターで構築されたキャンバスの場合、キャンバスエントリのプロパティはキャンバスの最初の完全なステップでのみ参照できる。

{% enddetails %}
{% endtab %}

{% tab Event Properties %}

イベントプロパティとは、カスタムイベントと購入に設定したプロパティを指します。これらの `event_properties` は、アクションベースの配信やキャンバスを含むキャンペーンで使用できます。

{% alert important %}
キャンバスの最初のメッセージステップでは、`event_properties`を使用できない。代わりに、`context` を使用するか、`event_properties` を含むメッセージステップの**前に**、対応するイベントを持つアクションパスステップを追加する必要があります。
{% endalert %}

キャンバスでは、カスタムイベントと購入イベントのプロパティは、アクションパスステップに続く任意のメッセージステップにおいてLiquidで使用できる。これらのイベントプロパティを参照する場合は、必ず {% raw %}``{{event_properties.${property_name}}}``{% endraw %}`` を使用すること。メッセージコンポーネントでこのように使用するには、これらのイベントがカスタムイベントまたは購入イベントである必要があります。

アクションパスに続く最初のメッセージステップでは、そのアクションパスで参照されたイベントに関連するイベントプロパティを使用できる。ただし、これらのイベントプロパティは、ユーザーが実際にそのアクションを実行した場合（つまり「その他全員」グループに分類されなかった場合）にのみ使用できる。このアクションパスとメッセージステップの間に、他のステップ (別のアクションパスやメッセージステップではない) があってもかまいません。

{% details Expand for original Canvas editor %}

元のエディターを使用したキャンバスの作成や複製はできなくなりました。このセクションは参照のみを目的としています。オリジナルのCanvasエディターでは、スケジュールされた完全ステップにおいてイベントプロパティは使用できない。ただし、アクションベースのキャンバスの最初の完全ステップでは、そのステップがスケジュールされていても、イベントプロパティを使用できる。

{% enddetails %}

{% endtab %}
{% endtabs %}

詳細と例については、[キャンバスのエントリプロパティとイベントプロパティ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/)を参照してください。