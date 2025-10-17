---
nav_title: コネクテッドコンテンツの再試行
article_title: コネクテッドコンテンツの再試行
page_order: 5
description: "この記事では、コネクテッドコンテンツの再試行に対処する方法を説明します。"

---

# コネクテッドコンテンツに再試行ロジックを使用する

> このページでは、コネクテッドコンテンツの呼び出しに再試行を追加する方法について説明します。

## リトライの仕組み 

コネクテッドコンテンツは API からのデータ受信に依存しているため、Braze が呼び出しを実行している間は API が断続的に使用できなくなることがあります。その場合、Braze は指数バックオフを使用してリクエストを再試行する、再試行ロジックをサポートしています。

{% alert note %}
コネクテッドコンテンツ `:retry` は、アプリ内メッセージでは利用できません。
{% endalert %}

## リトライ・ロジックを使う

再試行ロジックを使用するには、以下のコードスニペットに示すように、コネクテッドコンテンツ呼び出しに`:retry` タグを追加します。

{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

コネクテッドコンテンツの呼び出しに`:retry` タグが含まれている場合、Brazeは最大5回まで再試行を試みる。

### 再試行の結果

#### 再試行が成功した場合

再試行が成功した場合、そのメッセージは送信され、以後そのメッセージの再試行は行われない。

#### API  コールが失敗し、再試行が有効になっている場合

APIコールが失敗し、これが有効になっている場合、Brazeは、各再送に設定した[レート制限を]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-speed-rate-limiting)尊重しながら、コールを再試行する。Brazeは、失敗したメッセージをキューの最後尾に移動させ、必要であれば、メッセージ送信にかかる総時間をさらに数分追加する。

コネクテッドコンテンツ呼び出しが5回エラーになった場合、メッセージは、[メッセージ中止タグ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/)がトリガーされた場合と同様に中止されます。