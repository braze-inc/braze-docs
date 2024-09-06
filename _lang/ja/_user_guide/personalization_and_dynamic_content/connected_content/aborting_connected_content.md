---
nav_title: 接続されたコンテンツを中止する
article_title: 接続されたコンテンツを中止する
page_order: 2
description: "この参考記事では、コネクテッド・コンテンツにおけるメッセージ中止のベスト・プラクティスをいくつか取り上げている。"

---

# 接続されたコンテンツを中止する {#aborting-connected-content}

> リキッドテンプレートを使えば、条件付きロジックでメッセージを中止するオプションがある。 

以下の例では、`connected.recommendations.size < 5` と`connected.foo.bar == nil` という条件式が、メッセージを中断させる状況を指定している。

{% raw %}
```
{% connected_content https://example.com/webservice.json :save connected %}
   {% if connected.recommendations.size < 5 or connected.foo.bar == nil %}
     {% abort_message() %}
   {% endif %}
```
{% endraw %}

中止の理由を指定することもでき、その理由は[メッセージアクティビティログに]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)保存される。この中止理由は文字列でなければならず、リキッドを含むことはできない。

{% raw %}
`{% abort_message('Could not get enough recommendations') %}`
{% endraw %}

{% alert important %}
Brazeは、中断されたメッセージをBrazeアカウントやCurrentsの送信数にカウントしない。
{% endalert %}
