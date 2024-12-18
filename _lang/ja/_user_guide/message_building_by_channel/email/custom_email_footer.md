---
nav_title: メールのカスタムフッター
article_title: メールのカスタムフッター
page_order: 6.5
description: "この記事では、ワークスペース全体にカスタムEメールフッターを設定する方法を説明する。"
channel:
  - email

---

# メールのカスタムフッター

> Liquid 属性 {% raw %}`{{${email_footer}}}`{% endraw %} を使用して個々のメールにテンプレート化できるカスタムメールフッターを、ワークスペース全体で設定できます。

カスタムメールフッターを使うことで、メールテンプレートやメールキャンペーンごとに新しいフッターを作成する必要がなくなる。カスタムフッターに加えた変更は、新規および既存のすべてのメールキャンペーンに反映される。[CAN-SPAM法（2003年）を](https://www.ftc.gov/tips-advice/business-center/guidance/can-spam-act-compliance-guide-business)遵守するためには、Eメールにあなたの会社の物理的な住所と配信停止リンクを含める必要があることを覚えておいてほしい。

{% alert warning %}
前述の要件を満たすカスタムフッターにすることは、お客様の責任です。
{% endalert %}

## カスタムフッターを作成する

カスタムフッターを作成または編集するには、以下のようにする：

1. [**設定**] > [**メール設定**] に移動します。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation) を使用している場合、このページは**Email Settings** と呼ばれ、**Manage Settings** の下にあります。
{% endalert %}

{: start="2"}
2\.**カスタムフッターセクションに**行き、カスタムフッターをオンにする。
3\.**Compose**セクションでフッタを編集します。
4. テストメッセージを送信します。 

![カスタムフッタの例。][20]

デフォルトのフッターでは、属性 {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} と物理的な住所を使用しています。このデフォルトを使用する場合は、必ず**<other>**を**Protocol**に選択してください。

{% alert important %}
CAN-SPAM規制に準拠するため、カスタムフッターには{% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} を含める必要がある。この属性がないと、カスタムフッターを保存することができない。
{% endalert %}

![カスタムフッターに必要なプロトコルとURLの値。][24]{: style="max-width:50%;"}

## 配信停止リンクのないフッター

カスタムフッター {% raw %}`{{${email_footer}}}` を含むが `{{${set_user_to_unsubscribed_url}}}`{% endraw %} の購読解除リンクがないテンプレートを使用するときには、十分に注意してください。警告が表示されるが、配信停止リンクのあるメールを送るか、ないメールを送るかはあなたの選択となる。

メール作成者の警告は次のとおりです。

![フッターなしで構成された電子メールの例。][21]

キャンペーンコンポーザーの警告は次のとおりです。

![フッターなしで作成されたキャンペーン。][22]

### カスタム配信停止リンクの作成

カスタム配信停止リンクを追加するには、カスタムフッターの配信停止リンクを、{% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} から、クエリパラメーターにユーザー ID を含む自社の Web サイトへのリンクに変更することができます。例は次のとおりです。
{% raw %} 
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

次に、[`/email/status` endpoint]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) を呼び出して、ユーザーのサブスクリプションステータスを更新します。詳細については、「[メールサブスクリプションステータスの変更]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions)」のドキュメントを参照してください。。

次に、この新しいリンクを保存します。Braze のデフォルトの配信停止タグ {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} をフッターに含める必要があります。つまり、デフォルトのリンクを"hiding" に含める必要があります。これは、タグをコメントに配置するか、非表示の`<div>` タグに配置することによって行います。

## ベストプラクティス

カスタムフッタを作成および使用する際には、以下のベストプラクティスを推奨します。

### 属性でパーソナライズする

カスタムフッターを作成するときに、Braze では[パーソナライゼーション用の属性]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)を使用することをお勧めしています。デフォルト属性とカスタム属性のフルセットが利用可能だが、ここでは役に立つと思われるものをいくつか紹介しよう：

| 属性 | タグ |
| --------- | --- |
| ユーザーのメールアドレス | {% raw %}`{{${email_address}}}`{% endraw %} |
| ユーザーのカスタム配信停止URL | {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %}<br><br>このタグは、以前の {% raw %}`{{${unsubscribe_url}}}`{% endraw %} タグを置き換えるものです。代わりに、より新しい{% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} タグを使用することをお勧めする。 |
| ユーザーのカスタムオプトインURL | {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} |
| ユーザーのカスタム購読 URL | {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}|
| ユーザーのカスタム Braze ユーザー設定センターの URL | {% raw %}`{{${preference_center_url}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 配信停止リンクとオプトインリンクを含む

{% raw  %}
ベストプラクティスとして、Braze はカスタムフッターに購読解除リンク (``{{${set_user_to_unsubscribed_url}}}`` など) とオプトインリンク (``{{${set_user_to_opted_in_url}}}`` など) の両方を含めることをお勧めしています。これにより、ユーザーは購読解除とオプトインの両方を行うことができ、お客様は一部のユーザーのオプトインデータを受動的に収集できます。
{% endraw %}

### プレーンテキスト・メールにカスタム・フッターを設定する

また、[**メール設定**] ページの [**購読ページおよびフッター**] タブからも、プレーンテキストメール用のカスタムフッターを設定できます。これは、HTML メールのカスタムフッターと同じルールに従います。 

プレーンテキストのフッターを含めない場合、Brazeは自動的にHTMLフッターからフッターを作成する。カスタムフッターの作成が完了したら、[**保存**] をクリックする。

![[カスタムプレーンテキストフッターを設定] オプションを選択したメール。][23]{: style="max-width:70%" }

[20]: {% image_buster /assets/img_archive/custom_footer.png %}
[21]: {% image_buster /assets/img_archive/no_unsub_link_warning.png %}
[22]: {% image_buster /assets/img_archive/no_footer_test.png %}
[23]: {% image_buster /assets/img_archive/custom_footer_save_changes.png %}
[24]: {% image_buster /assets/img_archive/email_unsub_protocol.png %}
