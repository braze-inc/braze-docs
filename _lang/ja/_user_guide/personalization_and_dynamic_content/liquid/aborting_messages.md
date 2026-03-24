---
nav_title: メッセージの中止
article_title: Liquidメッセージを中止する
page_order: 7
description: "このリファレンス記事では、リキッドメッセージの中止といくつかのサンプルユースケースs について説明します。"

---

# メッセージを中止する

> オプションで、条件内で`abort_message("optional reason for aborting")` Liquid メッセージタグを使用して、ユーザーへのメッセージ送信を中止できます。この記事では、この機能をマーケティングキャンペーンで使用する方法の例をいくつか紹介します。

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

![「language was nil」という中止メッセージのある開発者コンソールのメッセージエラーログ]({% image_buster /assets/img_archive/developer_console.png %})

## アボートメッセージのクエリ

Braze に接続されている場合は、[Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) または独自のデータウェアハウスを使用して、Liquid ロジックがメッセージをアボートさせたときにトリガーされる特定のアボートメッセージをクエリーできます。

## アボートロジックが評価される時

アボートロジックの評価タイミングはメッセージチャネルに依存する。

### プッシュ通知、メール、SMS、Webhook、コンテンツカード

アボートロジックは送信時に評価される。つまり、Brazeがメッセージを配信処理する際に評価される。

### アプリ内メッセージ

中止ロジックは、アプリ内メッセージがトリガーされた時点（例えば、ユーザーがトリガーイベントを実行した時やセッションを開始した時）に評価される。メッセージが最初にデバイスに送信された時点ではない。アプリ内メッセージはセッション開始時にSDKに配信され、ローカルにキャッシュされる。トリガー条件が満たされた時点で、Liquid（呼び出し`abort_message()`を含む）が実行される。

## 考慮事項

`abort_message()` Liquid メッセージタグは、ユーザーへのメッセージ送信を中止します。つまり、メッセージはユーザープロファイルに表示されず、配信やフリークエンシーキャップにカウントされません。
