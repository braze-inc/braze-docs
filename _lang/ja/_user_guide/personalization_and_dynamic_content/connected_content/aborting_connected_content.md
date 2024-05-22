---
nav_title: 接続コンテンツの中止
article_title: 接続コンテンツの中止
page_order: 2
description: "この参考記事では、コネクテッド・コンテンツのメッセージ中止のベスト・プラクティスをいくつか取り上げています。"

---

# 接続コンテンツの中止 {#aborting-connected-content}

> リキッドテンプレートを使用すると、条件付きロジックでメッセージを中止するオプションがあります。 

以下の例では、`connected.recommendations.size < 5` と`connected.foo.bar == nil` という条件式が、メッセージを中断させる状況を指定している。

{% raw %}
```
{% connected_content https://example.com/webservice.json :save connected %}
   {% if connected.recommendations.size < 5 or connected.foo.bar == nil %}
     {% abort_message() %}
   {% endif %}
```
{% endraw %}

中止の理由を指定することもでき、その理由は[メッセージ・アクティビティ・ログに]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)保存される。この中止理由は文字列でなければならず、リキッドを含むことはできない。

{% raw %}
`{% abort_message('Could not get enough recommendations') %}`
{% endraw %}

{% alert important %}
Brazeは、中断されたメッセージをBrazeアカウントやCurrentsの送信数にカウントしません。
{% endalert %}
