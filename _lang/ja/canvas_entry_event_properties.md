キャンバスのユーザー・ジャーニーでは、キャンバス・エントリー・プロパティとイベント・プロパティを使用できる。

{% tabs local %}
{% tab Canvas Entry Properties %}

[キャンバスエントリのプロパティ]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)は、アクションベースまたは API でトリガーされるキャンバスにマップするプロパティです。`canvas_entry_properties` オブジェクトのサイズ上限は 50 KB であることに注意してください。

{% alert note %}
特にアプリ内メッセージチャネルでは、`canvas_entry_properties` はキャンバス内でのみ参照できます。
{% endalert %}

どのメッセージステップでも、このLiquidフォーマットで`canvas_entry_properties` を参照できる:``{% raw %} canvas_entry_properties.${property_name} {% endraw %}`` 。このように使用するには、イベントがカスタムイベントまたは購入イベントでなければならないことに注意してください。

#### ユースケース

{% raw %}
小売店である RetailApp に対してリクエスト `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}` があるとします。 

`{{canvas_entry_properties.${product_name}}}`RetailApp は、商品名(靴)をメッセージに取り込むことができる。
{% endraw %}

RetailApp は、ユーザーが購入イベントをトリガーした後に、キャンバス内の異なる `product_name` プロパティに対して特定のメッセージをトリガーして送信することもできます。たとえば、次の Liquid をメッセージステップに追加することで、靴を購入したユーザーと別のものを購入したユーザーに異なるメッセージを送ることができます。

{% raw %}
```markdown
{% if  {{canvas_entry_properties.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add more items to your cart for the same discounts.
{% endif %}

```
{% endraw %}

{% details Expand for original Canvas editor %}

元のエディターを使用したキャンバスの作成や複製はできなくなりました。このセクションは参照のみを目的としています。オリジナルのエディターで作られたキャンバスでは、キャンバスエントリープロパティはキャンバスの最初のステップでのみ参照できる。

{% enddetails %}
{% endtab %}

{% tab Event Properties %}

イベントプロパティとは、カスタムイベントと購入に設定したプロパティを指します。これらの `event_properties` は、アクションベースの配信やキャンバスを含むキャンペーンで使用できます。

{% alert important %}
キャンバスの最初のメッセージステップでは、`event_properties` 。代わりに、`canvas_entry_properties` を使用するか、`event_properties` を含むメッセージステップの**前に**、対応するイベントを持つアクションパスステップを追加する必要があります。
{% endalert %}

キャンバスでは、カスタムイベントと購入イベントのプロパティを、アクションパスステップに続く任意のメッセージステップで Liquid で使用できます。これらのイベント・プロパティを参照する場合は、必ず{% raw %} ``{{event_properties.${property_name}}}``{% endraw %} 。メッセージコンポーネントでこのように使用するには、これらのイベントがカスタムイベントまたは購入イベントである必要があります。

アクションパスに続く最初のメッセージステップでは、そのアクションパスで参照されているイベントに関連するイベントプロパティを使うことができる。しかし、これらのイベントプロパティは、ユーザーが実際にアクションを実行した（Everyone Elseグループにソートされなかった）場合にのみ使用できる。このアクションパスとメッセージステップの間に、他のステップ (別のアクションパスやメッセージステップではない) があってもかまいません。

{% details Expand for original Canvas editor %}

元のエディターを使用したキャンバスの作成や複製はできなくなりました。このセクションは参照のみを目的としています。オリジナルのキャンバス・エディターでは、イベント・プロパティはスケジュールされたフル・ステップでは使用できない。ただし、アクションベースのキャンバスの最初のフルステップでは、フルステップがスケジュールされていても、イベントプロパティを使用できる。

{% enddetails %}

{% endtab %}
{% endtabs %}

詳細と例については、[キャンバスのエントリプロパティとイベントプロパティ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/)を参照してください。