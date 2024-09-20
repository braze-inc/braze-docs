---
nav_title: ファジィオプトアウト
article_title: ファジィオプトアウト
description: "このリファレンス記事では、受信メッセージがオプトアウトキーワードと一致しない場合に認識しようとする設定であるファジィオプトアウトを設定する方法について説明します。"
page_type: reference
channel:
  - SMS
page_order: 1

---

# ファジィオプトアウト

![][1]{: style="float:right;max-width:30%;margin-left:15px;"}

> Braze を使用してSMS を送信するユーザは、定義されているアプリのライセンス適用法令、規則、および業界標準に準拠している必要があります。オプトアウトの場合、ユーザーのテキストが"STOP"のとき、そのメッセージング番組に関連した後続のすべてのメッセージングが停止されることが法則で定められています。Braze はこれらのメッセージを自動的に処理し、ユーザーを配信停止します。<br><br>ファジィオプトアウトは、受信メッセージが[opt-out キーワード]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/optin_optout/)と一致しないときを認識しようとしますが、オプトアウトインテントを示します。fuzzy opt-out が有効で、受信キーワードレスポンスが"fuzzy," Braze が自動的に応答し、ユーザーにそのインテントを確認するように求めます。 

現在、[ローカル言語]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#multi-language-support)として英語を使用して作成されたオプトアウトキーワードのみがサポートされています。

## ファジィとは何か?

インバウンド応答が"fuzzy&quot とみなされる基準は次のとおりです。
- 切り替えるに、文字がQWERTY キーワードの左右に1 つある文字を指定すると、一致するオプトアウトキーワードが生成されます。
- メッセージの部分文字列は、オプトアウトキーワードと一致します。

たとえば、"Stpo"または"Please stopppp"はファジーと見なされ、ファジーオプトアウト応答が送信されます。

## ファジィオプトアウトの設定

ファジィオプトアウトを設定するには、サブスクリプショングループ キーワードマネジメントページに移動します。

1. **Audience**> **サブスクリプション s** に進み、SMS サブスクリプショングループを選択します。
{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation) を使用している場合、**Subscription Groups** は**Users** にあります。
{% endalert %}

{:start="2"}
2\.**SMS Global Keywords**で、**opt-out**カテゴリを見つけ、鉛筆アイコンを選択します。
3\.**Fuzzy Opt-Out**をオンに切り替えて有効にします。
4\.必要に応じて、ファジィオプトアウト応答を変更します。 

![][2]{: style="max-width:70%;"}

[1]: {% image_buster /assets/img/sms/fuzzy1.jpg %}
[2]: {% image_buster /assets/img/sms/fuzzy2.png %}

