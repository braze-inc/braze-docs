---
nav_title: メッセージの中止
article_title: リキッドメッセージの中止
page_order: 7
description: "このリファレンス記事では、液体メッセージの中止といくつかの使用例について説明します。"

---

# メッセージの中止

> 必要に応じて、条件内のリキッドメッセージを中止できます。このリファレンス記事では、この機能をマーケティングキャンペーンで使用する方法の例をいくつか紹介します。

{% alert note %}
キャンバスでメッセージステップが中止された場合、ユーザ**はキャンバスを終了せず、**は次のステップに進みます。
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

このメッセージは、ゲームに参加したことがわかっている顧客にのみ送信されます。

## 英語を話すメッセージ顧客のみ

英語を話す顧客にメッセージを送るには、"if"顧客の言語が英語で"else"のときに一致するステートメントを作成します。英語を話さない人や、プロフィールに言語がない人のメッセージを中止するステートメントです。

{% raw %}
\`\`\`liquid

{% if ${language} == 'en' %}
このメッセージを英語で送ろう！
{% else %}
{% abort_message() %}
{% endif %}
\`\`\`

デフォルトでは、Braze はメッセージアクティビティログに一般的なエラーメッセージを記録します。

```text
{% abort_message %} called
```

また、括弧内に文字列を含めることで、メッセージアクティビティログに何らかのアボートメッセージログを記録することもできます。

```liquid
{% abort_message('language was nil') %}
```
{% endraw %}

!["language was nil".][26] のアボートメッセージを含む開発者コンソールのメッセージエラーログ。

[15]: {% image_buster /assets/img_archive/liquid_abort.png %}
[26]: {% image_buster /assets/img_archive/developer_console.png %}
[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[37]:#accounting-for-null-attribute-values
