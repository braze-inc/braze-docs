---
nav_title: ユーザープロファイルデータの取得
article_title: 接続されたコンテンツコールでのユーザプロファイルデータの取得
page_order: 5
description: "この記事では、ユーザープロファイル をConnected Content コールにプルする方法、およびリキッドテンプレーティングに関するベストプラクティスについて説明します。"

---

# ユーザープロファイル情報の取得

> 連結内容レスポンスがユーザープロファイル フィールドs(液体パーソナライゼーション タグ内)を含む場合、液体パスバックを適切にレンダリングするためには、連結内容呼び出しの前に、これらの値を液体を介したメッセージの前に定義する必要があります。 

同様に、`:rerender` フラグもリクエストに含める必要があります。`:rerender`フラグは、1レベルの深さのみであることに注意してください。つまり、ネストされた接続内容タグsにはアプリしません。

パーソナライゼーションの場合、Braze はユーザープロファイル フィールドs をプルしてから、そのフィールドをLiquid に渡します。そのため、Connected Content からのレスポンスにユーザープロファイル フィールド s がある場合は、事前に定義する必要があります。 

たとえば、これがConnected Content コールの場合は、次のようになります。
{% raw %}
```liquid
Hi ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}
そしてConnected Contentのレスポンスは{% raw %}`Your language is ${language}`{% endraw %}で、このシナリオで表示される内容は`Hi Jon, your language is`になります。言語そのものはテンプレートd にはなりません。これは、Brazeが接続コンテンツ呼び出しを行う前に、ユーザーからどのフィールドを取得するかを知る必要があるためです。

リキッドパスバックを適切にレンダリングするには、次のコードスニペットに示すように、{% raw %}`${language}`{%endraw%} タグをリクエストの任意の場所に配置する必要があります。リキッドプリプロセッサは、"language"属性をユーザーから取得して、レスポンスをテンプレート化する準備を整えることができます。
{%raw%}
```liquid
"Hi ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}
{% alert important %}
`:rerender` フラグオプションは深さが1 レベルのみであることを覚えておいてください。接続コンテンツレスポンス自身がより多くの接続コンテンツタグを持っている場合、Brazeはこれらの追加タグを再レンダリングしません。
{% endalert %}
