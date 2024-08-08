---
nav_title: ユーザープロファイルデータの取得
article_title: 接続されたコンテンツコールでのユーザプロファイルデータの取得
page_order: 5
description: "この記事では、Connected Content コールにユーザプロファイルをプルする方法、およびLiquid テンプレーティングに関するベストプラクティスについて説明します。"

---

# ユーザープロファイルデータの取得

> Connected Content レスポンスにユーザプロファイルフィールド(Liquid パーソナライゼーションタグ内)が含まれている場合、Liquid パスバックを適切にレンダリングするには、Connected Content コールの前に、Liquid 経由のメッセージでこれらの値を定義する必要があります。 

同様に、`:rerender` フラグもリクエストに含める必要があります。`:rerender` フラグは1 レベルの深さのみであることに注意してください。つまり、ネストされた接続コンテンツタグには適用されません。

パーソナライゼーションの場合、Brazeは、そのフィールドをLiquidに渡す前にユーザープロファイルフィールドをプルします。そのため、Connected Contentからの応答にユーザープロファイルフィールドがある場合は、事前に定義する必要があります。 

たとえば、これがConnected Content コールの場合は、次のようになります。
{% raw %}
```liquid
Hi ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}
そしてConnected Contentのレスポンスは{% raw %}`Your language is ${language}`{% endraw %}で、このシナリオで表示される内容は`Hi Jon, your language is`になります。言語自体はテンプレート化されません。これは、接続コンテンツ呼び出しを行う前に、ユーザから取得するフィールドをBraze が認識する必要があるためです。

Liquid パスバックを適切にレンダリングするには、以下のコードスニペットに示すように、{% raw %}`${language}`{%endraw%} タグをリクエストの任意の場所に配置する必要があります。リキッドプリプロセッサは、ユーザーから"language"属性を取得して、応答をテンプレート化する準備ができていることを認識します。
{%raw%}
```liquid
"Hi ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}
{% alert important %}
`:rerender` フラグオプションは、深さが1 レベルのみであることを覚えておいてください。Connected Content 応答自体にConnected Content タグが多い場合、Braze はこれらの追加タグを再レンダリングしません。
{% endalert %}
