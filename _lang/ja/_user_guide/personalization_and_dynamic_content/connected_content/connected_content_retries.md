---
nav_title: コネクテッドコンテンツの再試行
article_title: コネクテッドコンテンツの再試行
page_order: 5
description: "この記事では、コネクテッドコンテンツの再試行に対処する方法を説明します。"

---

# 

> このページでは、コネクテッドコンテンツの呼び出しに再試行を追加する方法について説明します。

##  

その場合、Braze は指数バックオフを使用してリクエストを再試行する、再試行ロジックをサポートしています。

{% alert note %}
コネクテッドコンテンツ `:retry` は、アプリ内メッセージでは利用できません。
{% endalert %}

## 




```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}



### 再試行の結果

#### 再試行が成功した場合



#### API  コールが失敗し、再試行が有効になっている場合

Brazeは、失敗したメッセージをキューの最後尾に移動させ、必要であれば、メッセージ送信にかかる総時間をさらに数分追加する。

