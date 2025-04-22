---
nav_title: 不明な電話番号の処理
article_title: 不明なSMS電話番号の処理
page_order: 4
description: "このリファレンス記事では、新しいユーザーからの不明なSMS電話番号をBrazeがどのように処理するかについて説明します。"
page_type: reference
channel:
  - SMS
  
---

# 不明な電話番号の処理 - 新しいユーザー

> BrazeでSMSを設定して稼働させた後、見知らぬユーザーからメッセージを受け取ることがあるかもしれません。次の手順は、未確認のユーザーと番号がどのように処理されるかを説明しています。

{% alert important %}
現在、非ネイティブSMSクライアントですか？その場合は、[非ネイティブ SMS ドキュメント]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/)で、対応する不明な電話番号の処理の記事を参照してください。
{% endalert %}

## オプトイン/アウトおよび不明な番号のカスタムキーワードワークフロー

Brazeは、不明な番号を次の3つの方法のいずれかで自動的に処理します:

1. オプトインキーワードがテキスト送信された場合:
  * Brazeは匿名のプロファイルを作成します
  * 私たちのシステムは電話属性を設定します
  * Braze が受信したオプトインキーワードに基づいて、対応する購読グループにユーザーを登録します。<br><br>
2. オプトアウトのキーワードがテキスト送信された場合:
  * Brazeは匿名のプロファイルを作成します
  * 私たちのシステムは電話属性を設定します
  * Brazeによって受信されたオプトアウトキーワードに基づいて、対応するサブスクリプショングループからユーザーの登録を解除します。<br><br>
3. 他のカスタムキーワードがテキスト化されている場合:
  * Brazeはテキストメッセージを無視し、何もしません。

[ualink]: {{site.baseurl}}/api/objects_filters/user_alias_object/
[telink]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[uaolink]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[e.164]: https://en.wikipedia.org/wiki/E.164