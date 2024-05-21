---
nav_title: コネクテッドコンテンツの再試行
article_title: コネクテッドコンテンツの再試行
page_order: 3
description: "この参考記事では、コネクテッド・コンテンツの再試行に対処する方法について説明します。"

---

# コネクテッドコンテンツの再試行

> Connected ContentはAPIからのデータ受信に依存しているため、Brazeがコールしている間、APIが断続的に利用できない可能性があります。この場合、Brazeは指数関数的バックオフを使ってリクエストを再試行するリトライロジックをサポートします。 

再試行を有効にするには、次のコード・スニペットに示すように、Connected Content呼び出しに`:retry` ：
{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

APIコールに失敗し、これが有効になっている場合、Brazeは再送ごとに設定した[レート制限を][47]尊重しながらコールを再試行します。Brazeは、失敗したメッセージをキューの最後尾に移動し、必要であれば、メッセージ送信にかかる総時間をさらに数分追加します。

再試行が成功した場合、そのメッセージは送信され、以後そのメッセージの再試行は行われない。Connected Content呼び出しが5回エラーになった場合、メッセージは[アボート][1]される。

{% alert note %}
Connected Content`:retry` はアプリ内メッセージではご利用いただけません。
{% endalert %}


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[16]: [success@braze.com](mailto:success@braze.com)
[47]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-speed-rate-limiting
