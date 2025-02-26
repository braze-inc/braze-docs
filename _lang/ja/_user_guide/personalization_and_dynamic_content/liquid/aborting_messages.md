---
nav_title: メッセージの中止
article_title: Liquid メッセージの中止
page_order: 7
description: "このリファレンス記事では、リキッドメッセージの中止といくつかのサンプルユースケースs について説明します。"

---

# メッセージの中止

> 必要に応じて、条件内のリキッドメッセージを中止できます。この記事では、この機能をマーケティングキャンペーンで使用する方法の例をいくつか紹介します。

{% alert note %}
キャンバスでメッセージステップが中止された場合、ユーザーはキャンバスを**終了せず**、**次のステップに進みます**。
{% endalert %}

## "Number Games Attended" = 0 の場合、メッセージを中止する

たとえば、ゲームに参加していない顧客にメッセージを送信したくなかったとします。

{% raw %}
```liquid
{% if custom_attribute.${Number_Game_Attended} == 1 %}
Loved the game? Get 10% off your second one with code SAVE10.
{% elsif custom_attribute.${Number_Game Attended} > 1 %}
Love the games? Get 10% off your next one with code SAVE10.
{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

このメッセージは、ゲームに参加したことがわかっている顧客にのみ送信されます。

## 英語圏の顧客専用のメッセージング

英語圏の顧客にメッセージを送るには、顧客の言語が英語の場合に一致する「if」ステートメントを使い、英語を話さない顧客やプロファイルに言語がない顧客の場合は「else」ステートメントを使用してメッセージを中止します。

{% raw %}
```liquid

{% if ${language} == 'en' %}
Send this message in English!
{% else %}
{% abort_message() %}
{% endif %}
```

デフォルトでは、Braze はメッセージアクティビティログに一般的なエラーメッセージを記録します。

```text
{% abort_message %} called
```

また、かっこ内に文字列を含めることで、メッセージアクティビティログに何らかの中止メッセージログを記録することもできます。

```liquid
{% abort_message('language was nil') %}
```
{% endraw %}

![「language was nil」という中止メッセージのある開発者コンソールのメッセージエラーログ][26]

## アボートメッセージのクエリ

Braze に接続されている場合は、[Query Builder]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/) または独自のデータウェアハウスを使用して、Liquid ロジックがメッセージをアボートさせたときにトリガーされる特定のアボートメッセージをクエリーできます。

[15]: {% image_buster /assets/img_archive/liquid_abort.png %}
[26]: {% image_buster /assets/img_archive/developer_console.png %}
[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[37]:\#accounting-for-null-attribute-values
