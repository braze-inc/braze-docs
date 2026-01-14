---
nav_title: 接続されたコンテンツを中止する
article_title: 接続されたコンテンツを中止する
page_order: 2
description: "この参考記事では、コネクテッド・コンテンツにおけるメッセージ中止のベスト・プラクティスをいくつか取り上げている。"
---

# コネクテッドコンテンツの中止{#aborting-connected-content}

> Liquid テンプレートを使用する場合、条件付きロジックでメッセージを中止できます。このページでは、ベストプラクティスについて説明します。

次の例では、条件 `connected.recommendations.size < 5` および `connected.foo.bar == nil` でメッセージを中止する状況を指定します。

{% raw %}
```
{% connected_content https://example.com/webservice.json :save connected %}
   {% if connected.recommendations.size < 5 or connected.foo.bar == nil %}
     {% abort_message() %}
   {% endif %}
```
{% endraw %}

## 中止理由の指定

中止の理由も指定することができ、その理由は[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)に保存されます。この中止理由は文字列でなければならず、リキッドを含むことはできない。

{% raw %}
`{% abort_message('Could not get enough recommendations') %}`
{% endraw %}

{% alert important %}
Braze は、中断されたメッセージを Braze アカウントや Currents の送信数にカウントしません。
{% endalert %}
