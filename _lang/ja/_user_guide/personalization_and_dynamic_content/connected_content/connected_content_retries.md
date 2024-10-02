---
nav_title: 接続コンテンツの再試行
article_title: 接続コンテンツの再試行
page_order: 3
description: "この参考記事では、コネクテッド・コンテンツの再試行に対処する方法を取り上げている。"

---

# コネクテッド・コンテンツの再試行

> Connected ContentはAPIからのデータ受信に依存しているため、Brazeがコールしている間、APIが断続的に利用できない可能性がある。この場合、Brazeは指数バックオフを使用してリクエストを再試行するリトライロジッ クをサポートする。 

再試行を有効にするには、次のコード・スニペットに示すように、Connected Content呼び出しに`:retry` ：
{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

APIコールが失敗し、これが有効になっている場合、Brazeは、各再送に設定した[レート制限を][47]尊重しながら、コールを再試行する。Brazeは、失敗したメッセージをキューの最後尾に移動させ、必要であれば、メッセージ送信にかかる総時間をさらに数分追加する。

再試行が成功した場合、そのメッセージは送信され、以後そのメッセージの再試行は行われない。Connected Content呼び出しが5回エラーになった場合、メッセージは、[中止メッセージタグが][1]トリガーされた場合と同様に、中止される。

{% alert note %}
Connected Content`:retry` はアプリ内メッセージでは利用できない。
{% endalert %}


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[16]: [success@braze.com](mailto:success@braze.com)
[47]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-speed-rate-limiting
