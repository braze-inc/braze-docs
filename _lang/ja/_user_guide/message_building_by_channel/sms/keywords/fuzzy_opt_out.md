---
nav_title: あいまいなオプトアウト
article_title: あいまいなオプトアウト
description: "このリファレンス記事では、受信メッセージがオプトアウトキーワードと一致しない場合に認識しようとする設定であるファジィオプトアウトを設定する方法について説明します。"
page_type: reference
channel:
  - SMS
page_order: 1

---

# あいまいなオプトアウト

![][1]{: style="float:right;max-width:30%;margin-left:15px;"}

> Braze を使用して SMS を送信するユーザーは、定義されているアプリのライセンス適用法令、規則、および業界標準に従う必要があります。オプトアウトでは、ユーザーのテキストが「STOP」の場合、そのメッセージングプログラムに関連する後続のすべてのメッセージングを停止することが法で定められています。Braze はこれらのメッセージを自動的に処理し、ユーザーへの配信を停止します。<br><br>[あいまいなオプトアウト]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/optin_optout/)は、インバウンドメッセージがオプトアウトキーワードと一致しなくても、オプトアウトのインテントを示している場合に、それを認識しようとします。あいまいなオプトアウトが有効で、受信キーワードの応答が「あいまい」であると見なされた場合、Braze は自動的に応答し、ユーザーにそのインテントを確認するように求めます。 

現在、[ローカル言語]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#multi-language-support)として英語を使用して作成されたオプトアウトキーワードのみがサポートされています。

## 「あいまい」の基準

インバウンド応答が「あいまい」と見なされる基準は次のとおりです。
- QWERTY キーボードで左右隣にある文字に置き換えると一致するオプトアウトキーワードが生成される場合
- メッセージの部分文字列は、オプトアウトキーワードと一致します。

たとえば、「Stpo」や「Please stopppp」はあいまいと見なされ、あいまいなオプトアウト応答が送信されます。

## ファジィオプトアウトの設定

ファジィオプトアウトを設定するには、サブスクリプショングループ キーワードマネジメントページに移動します。

1. [**オーディエンス**] > [**購読**] に移動して、SMS 購読グループを選択します。
{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation) を使用している場合、**Subscription Groups** は**Users** にあります。
{% endalert %}

{:start="2"}
2\.**SMS Global Keywords**で、**opt-out**カテゴリを見つけ、鉛筆アイコンを選択します。
3\.[**あいまいなオプトアウト**] をオンに切り替えて有効にします。
4\.必要に応じて、ファジィオプトアウト応答を変更します。 

![][2]{: style="max-width:70%;"}

[1]: {% image_buster /assets/img/sms/fuzzy1.jpg %}
[2]: {% image_buster /assets/img/sms/fuzzy2.png %}

