---
nav_title: 不明な電話番号の処理
article_title: 不明なSMS電話番号の処理
page_order: 4
description: "このリファレンス記事では、Brazeが新規ユーザーからの不明なSMS電話番号を処理する方法について説明します。"
page_type: reference
channel:
  - SMS
  
---

# 不明な電話番号の処理 - 新規ユーザー

> BrazeでSMSを起動して実行した後、不明なユーザーからメッセージを受信することがあります。次の手順では、識別できないユーザーと番号がどのように処理されるかについて説明します。

{% alert important %}
現在、非ネイティブのSMSクライアントですか?その場合は、非 [ネイティブ SMS のドキュメント](/docs/user_guide/message_building_by_channel/sms/non_native/) で、対応する不明な電話番号の処理に関する記事を参照してください。
{% endalert %}

## 不明な番号のオプトイン/アウトとカスタムキーワードワークフロー

Brazeは、次の3つの方法のいずれかで未知の番号に自動的に対処します。

1. オプトインキーワードがテキストで送信される場合:
  * Brazeは匿名プロファイルを作成します
  * システムは phone 属性を設定します
  * Brazeが受信したオプトインキーワードに基づいて、対応するサブスクリプショングループにユーザーをサブスクライブします。<br><br>
2. オプトアウトキーワードがテキストで送信される場合:
  * Brazeは匿名プロファイルを作成します
  * システムは phone 属性を設定します
  * Brazeが受信したオプトアウトキーワードに基づいて、対応するサブスクリプショングループからユーザーの登録を解除します。<br><br>
3. 他のカスタムキーワードがテキストで送信される場合:
  * Brazeはテキストメッセージを無視し、何もしません。

[ualink]: {{site.baseurl}}/api/objects_filters/user_alias_object/
[telink]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[uaolink]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[e.164]: https://en.wikipedia.org/wiki/E.164