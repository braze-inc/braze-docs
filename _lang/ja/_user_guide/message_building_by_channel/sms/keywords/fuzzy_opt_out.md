---
nav_title: あいまいなオプトアウト
article_title: あいまいなオプトアウト
description: "この参考記事では、ファジーオプトアウトの設定方法について説明します。ファジーオプトアウトとは、受信メッセージがオプトアウトキーワードと一致しない場合にそれを認識しようとする設定です。"
page_type: reference
channel:
  - SMS
page_order: 1

---

# あいまいなオプトアウト

![][1]{: style="float:right;max-width:30%;margin-left:15px;"}

> Braze で SMS を送信するユーザーは、定められている適用法、規制、および業界標準を遵守する必要があります。オプトアウトについては、ユーザーが「STOP」とテキストメッセージを送信すると、そのメッセージングプログラムに関連するその後のすべてのメッセージングが停止されることが法律で定められています。Braze はこれらのメッセージを自動的に処理し、ユーザーの登録を解除します。<br><br>ファジーオプトアウトは、受信メッセージがオプトアウトキーワードと一致しない場合にそれを認識しようとしますが、[オプトアウトの意図を示します]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/optin_optout/)。ファジーオプトアウトが有効になっていて、インバウンドキーワードの応答が「あいまい」と見なされた場合、Brazeは自動的に応答し、ユーザーに意図の確認を求めます。 

現在、[英語を現地の言語として使用して作成されたオプトアウトキーワードのみがサポートされています]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#multi-language-support)。

## ファジーと見なされるのは何ですか？

インバウンド回答が「あいまい」と見なされる基準は次のとおりです。
-QWERTY キーワードで 1 の文字を左または右に切り替えると、一致するオプトアウトキーワードが生成されます。
-メッセージのサブストリングがオプトアウトキーワードと一致する。

たとえば、「Stop」や「Please stopppp」はあいまいと見なされ、あいまいなオプトアウト応答が送信されます。

## ファジーオプトアウトの設定

ファジーオプトアウトを設定するには、サブスクリプショングループのキーワード管理ページに移動します。

1. [**オーディエンス**] > [**サブスクリプション**] に移動し、SMS サブスクリプショングループを選択します。
{% alert note %}
[古いナビゲーションを使用している場合は]({{site.baseurl}}/navigation)、「**ユーザー**」**の下にサブスクリプショングループが表示されます**。
{% endalert %}

{:start="2"}
2\.**SMSグローバルキーワードで**、**オプトアウトカテゴリを見つけて鉛筆アイコンを選択します**。
3\.**ファジーオプトアウトをオンに切り替えて有効にします**。
4\.必要に応じてファジーオプトアウトレスポンスを変更します。 

![][2]{: style="max-width:70%;"}

[1]: {% image_buster /assets/img/sms/fuzzy1.jpg %}
[2]: {% image_buster /assets/img/sms/fuzzy2.png %}

