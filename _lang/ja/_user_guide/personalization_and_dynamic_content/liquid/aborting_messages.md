---
nav_title: メッセージの中止
article_title: Liquid メッセージの中止
page_order: 7
description: "このリファレンス記事では、リキッドメッセージの中止といくつかのサンプルユースケースs について説明します。"

---

# メッセージの中止

> 必要に応じて、条件内のリキッドメッセージを中止できます。このリファレンス記事では、この機能をマーケティング キャンペーン s で使用する方法をいくつか例示します。

{% alert note %}
キャンバスでメッセージステップが中止された場合、ユーザー**はキャンバスを終了せず、**は次回のステップに進みます。
{% endalert %}

## "Number Games Attended" = 0の場合、メッセージを中止します

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

このメッセージは、試合に出席したことがわかっている顧客にのみ送信されます。

## 英語圏顧客のみ

英語圏の顧客にメッセージを送るには、"if"文を作成します。顧客の言語が英語で"else"文は、英語を話さない人やプロファイルに言語がない人のメッセージを中止します。

{% raw %}
```liquid

{% if ${language} == 'en' %}
Send this message in English!
{% else %}
{% abort_message() %}
{% endif %}
```

デフォルト Brazeでは、一般的なエラーメッセージがメッセージアクティビティログに記録されます。

```text
{% abort_message %} called
```

また、かっこs 内に文字列を含めることで、メッセージアクティビティログに何かを記録することもできます。

```liquid
{% abort_message('language was nil') %}
```
{% endraw %}

![メッセージエラーは、"language がnil"のアボートメッセージで開発者コンソールにログインします。][26]

[15]: {% image_buster /assets/img_archive/liquid_abort.png %}
[26]: {% image_buster /assets/img_archive/developer_console.png %}
[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[37]:\#accounting-for-null-属性-values
