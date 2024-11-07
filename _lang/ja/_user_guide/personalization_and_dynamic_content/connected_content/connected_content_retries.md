---
nav_title: コネクテッドコンテンツの再試行
article_title: コネクテッドコンテンツの再試行
page_order: 3
description: "この記事では、コネクテッドコンテンツの再試行に対処する方法を説明します。"

---

# コネクテッドコンテンツの再試行

> コネクテッドコンテンツは API からのデータ受信に依存するため、Braze が呼び出しを処理する間、API が断続的に利用できなくなる可能性があります。その場合、Braze は指数バックオフを使用してリクエストを再試行する、再試行ロジックをサポートしています。 

再試行を有効にするには、次のコードスニペットにあるように、コネクテッドコンテンツ呼び出しに `:retry` を追加します。
{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

APIコールが失敗し、これが有効になっている場合、Brazeは、各再送に設定した[レート制限を][47]尊重しながら、コールを再試行する。Brazeは、失敗したメッセージをキューの最後尾に移動させ、必要であれば、メッセージ送信にかかる総時間をさらに数分追加する。

再試行が成功した場合、そのメッセージは送信され、以後そのメッセージの再試行は行われない。コネクテッドコンテンツ呼び出しが 5 回エラーになった場合、メッセージは、[メッセージ中止タグ][1]がトリガーされた場合と同様に中止されます。

{% alert note %}
コネクテッドコンテンツ `:retry` は、アプリ内メッセージでは利用できません。
{% endalert %}


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[16]: [success@braze.com](mailto:success@braze.com)
[47]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-speed-rate-limiting
