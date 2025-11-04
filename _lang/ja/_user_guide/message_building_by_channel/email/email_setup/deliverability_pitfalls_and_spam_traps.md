---
nav_title: 配信の落とし穴とスパムの罠
article_title: 配信の落とし穴とスパムの罠
page_order: 7
page_type: reference
description: "この参考記事では、潜在的なメール配信の落とし穴、スパムの罠、そしてそれらを回避する方法について取り上げている。"
channel: email

---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability){: style="float:right;width:120px;border:0;" class="noimgborder"} 配信の落とし穴とスパムの罠

以下のスパムトラップは、メール配信に影響を与える可能性がある：

| トラップタイプ | 説明 |
|---|---|
| プリスティントラップ | 一度も使用されたことのないメールアドレスとドメイン。 |
| リサイクルトラップ | 元々は実在のユーザーであったが、現在は休止しているメールアドレス。 |
| タイポの罠 | よくあるタイプミスを含むメールアドレス。 |
| スパムの苦情 | あなたのメールが顧客によってスパムとしてマークされた場合。 |
| 高い直帰率 | 受信者のアドレスが無効であるために、メールが常に配信できない場合。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## スパムの罠を回避する方法

このような罠は、確認オプトイン・プロセスを設定すれば回避できる。最初のオプトインメールを送信し、メッセージを希望するかどうかを顧客に確認することで、受信者があなたからの返信を求めているか、そして実際の有効なアドレスに送信しているかどうかを確認できます。スパムの罠を回避するその他の方法を紹介しよう：

1. ダブルオプトインメールを送信します。これは、ユーザーがリンクをクリックして購読の選択を確認することを要求するメールです。
2. ベストプラクティスとして、[サンセットポリシー]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/)を導入します。
3. **メールリストは決して購入しないようにします。** 

{% alert tip %}
Brazeのカスタマーサクセスチームとデリバビリティチームは、お客様がベストプラクティスに従って世界中でデリバビリティを最大化できるようにサポートする。
{% endalert %}

## バウンスリストやスパムリストからメールアドレスを削除する

バウンスメールやBrazeスパムリストのメールは、以下のエンドポイントで削除できる：
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam)