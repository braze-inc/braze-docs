---
nav_title: カスタムメールフッター
article_title: カスタムメールフッター
page_order: 6.5
description: "この記事では、ワークスペース全体にカスタムEメールフッターを設定する方法を説明する。"
channel:
  - email

---

# カスタムEメールフッター

> ワークスペース全体のカスタムメールフッターを設定することができ、{% raw %}`{{${email_footer}}}`{% endraw %} Liquid属性を使ってすべてのメールにテンプレート化することができる。

カスタムメールフッターを使うことで、メールテンプレートやメールキャンペーンごとに新しいフッターを作成する必要がなくなる。カスタムフッターに加えた変更は、新規および既存のすべてのメールキャンペーンに反映される。[CAN-SPAM法（2003年）を](https://www.ftc.gov/tips-advice/business-center/guidance/can-spam-act-compliance-guide-business)遵守するためには、Eメールにあなたの会社の物理的な住所と配信停止リンクを含める必要があることを覚えておいてほしい。

{% alert warning %}
カスタムフッターが前述の要件を満たしていることを確認するのは、あなたの責任である。
{% endalert %}

## カスタムフッターを作成する

カスタムフッターを作成または編集するには、以下のようにする：

1. **設定**＞**Eメール設定に**進む。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合、このページは「**Eメール設定**」と呼ばれ、「**設定の管理**」の下にある。
{% endalert %}

{: start="2"}
2\.**カスタムフッターセクションに**行き、カスタムフッターをオンにする。
3\.**メール作成**セクションでフッターを編集し、テストメッセージを送信する。 

![][20]

デフォルトのフッターは、{% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} 属性と私たちの物理的な郵送先住所を使用している。CAN-SPAM規制に準拠するため、カスタムフッターには{% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} を含める必要がある。この属性がないと、カスタムフッターを保存することができない。

{% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} 属性を使用するデフォルトのフッターを使用する場合は、**プロトコルに** **<other>を**必ず選択すること。

![カスタムフッターに必要なプロトコルとURLの値。][24]{: style="max-width:50%;"}

## 配信停止リンクのないフッター

カスタムフッター{% raw %}`{{${email_footer}}}` 、`{{${set_user_to_unsubscribed_url}}}`{% endraw %} 配信停止リンクタグのないテンプレートを使用する場合は、十分に注意すること。警告が表示されるが、配信停止リンクのあるメールを送るか、ないメールを送るかはあなたの選択となる。

**メールコンポーザー内の警告：**<br>![フッターなしで構成された電子メールの例。][21]

**キャンペーンコンポーザー内での警告：**<br>![ノー・フッター・キャンペーンの構図。][22]

## ベストプラクティス

Brazeでは、カスタムフッターを作成・使用する際のベストプラクティスを以下のように提案している。

### 属性でパーソナライズする

カスタムフッターを作成する際、Brazeは[パーソナライゼーションのために属性を]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)使うことを提案している。デフォルト属性とカスタム属性のフルセットが利用可能だが、ここでは役に立つと思われるものをいくつか紹介しよう：

| 属性 | タグ |
| --------- | --- |
| ユーザーのメールアドレス | {% raw %}`{{${email_address}}}`{% endraw %} |
| ユーザーのカスタム配信停止URL | {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %}<br><br>このタグは、以前の{% raw %}`{{${unsubscribe_url}}}`{% endraw %} 。代わりに、より新しい{% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} タグを使用することをお勧めする。 |
| ユーザーのカスタムオプトインURL | {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} |
| ユーザーのカスタム購読URL | {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}|
| ユーザー独自のBrazeプリファレンスセンターURL | {% raw %}`{{${preference_center_url}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2}

### 配信停止リンクとオプトインリンクを含む

{% raw  %}
ベストプラクティスとして、Brazeはカスタムフッターに配信停止リンク（``{{${set_user_to_unsubscribed_url}}}`` など）とオプトインリンク（``{{${set_user_to_opted_in_url}}}`` など）の両方を含めることを推奨している。こうすることで、ユーザーは配信停止とオプトインの両方ができるようになり、一部のユーザーのオプトインデータを受動的に収集することができる。
{% endraw %}

### プレーンテキスト・メールにカスタム・フッターを設定する

また、**メール設定**ページの**購読ページとフッタータブから**、プレーンテキストメール用のカスタムフッターを設定することもできる。プレーンテキストのフッターを含めない場合、Brazeは自動的にHTMLフッターからフッターを作成する。カスタムフッターが好みのものになったら、ページ下部の**「保存**」をクリックする。

![Set Custom Plaintext Footerオプションを選択した電子メール。][23]{: style="max-width:70%" }

[20]: {% image_buster /assets/img_archive/custom_footer.png %}
[21]: {% image_buster /assets/img_archive/no_unsub_link_warning.png %}
[22]: {% image_buster /assets/img_archive/no_footer_test.png %}
[23]: {% image_buster /assets/img_archive/custom_footer_save_changes.png %}
[24]: {% image_buster /assets/img_archive/email_unsub_protocol.png %}
