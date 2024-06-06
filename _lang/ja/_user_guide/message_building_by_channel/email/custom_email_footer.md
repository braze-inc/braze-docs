---
nav_title: カスタムメールフッター
article_title: カスタムメールフッター
page_order: 6.5
description: "この記事では、ワークスペース全体のカスタムメールフッターを設定する方法について説明します。"
channel:
  - email

---

# カスタムメールフッター

> ワークスペース全体のカスタムメールフッターを設定し、Liquid属性を使用して {% raw %}`{{${email_footer}}}`{% endraw %} すべてのメールにテンプレート化できます。

カスタムメールフッターを使用すると、使用するメールテンプレートやメールキャンペーンごとに新しいフッターを作成する必要がなくなります。カスタムフッターに加えた変更は、新規および既存のすべてのメールキャンペーンに反映されます。[2003年のCAN-SPAM法](https://www.ftc.gov/tips-advice/business-center/guidance/can-spam-act-compliance-guide-business)に準拠するには、会社の住所と登録解除リンクをメールに含める必要があります。

{% alert warning %}
カスタムフッターが前述の要件を満たしていることを確認するのは、お客様の責任です。
{% endalert %}

## カスタムフッターの作成

カスタムフッターを作成または編集するには、次の操作を行います。

1. [ **設定** ] > **[メール設定**] に移動します。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、このページは **[電子メールの設定**] と呼ばれ、[**設定の管理**] の下にあります。
{% endalert %}

{: start="2"}
2\.**[カスタムフッター**]セクションに移動し、[カスタムフッター]をオンにします。
3\.[ **作成** ] セクションでフッターを編集し、テスト メッセージを送信します。 

![][20]

デフォルトのフッターは、 {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} 属性と物理的な郵送先住所を使用します。CAN-SPAM規制に準拠するには、カスタムフッター {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %}に.この属性がないとカスタムフッターを保存できません。

属性を使用する{% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %}デフォルトのフッターを使用する場合は、必ず **[プロトコル**] で **<other>** を選択してください。

![カスタム フッターに必要なプロトコルと URL の値。[24]{: style="max-width:50%;"}

## 登録解除リンクのないフッター

カスタムフッター {% raw %}`{{${email_footer}}}` でテンプレートを使用し、登録解除リンクタグを使用しない場合は `{{${set_user_to_unsubscribed_url}}}`{% endraw %} 、十分に注意してください。警告が表示されますが、登録解除リンクの有無にかかわらずメールを送信するかどうかは、お客様の選択次第です。

**メールコンポーザー内の警告:**<br>![フッターなしで作成されたメールの例][21]

**キャンペーンコンポーザー内の警告:**<br>![フッターなしのキャンペーン構成][22]

## おすすめの方法

Brazeは、カスタムフッターを作成および使用する際の次のベストプラクティスを提案しています。

### 属性によるパーソナライゼーション

カスタムフッターを作成する際、Brazeは [パーソナライゼーションに属性]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)を使用することを提案しています。デフォルト属性とカスタム属性の完全なセットを使用できますが、ここでは役立つものをいくつか紹介します。

|属性 |タグ |
| --------- | --- |
|ユーザーのメールアドレス | {% raw %}`{{${email_address}}}`{% endraw %} |
|ユーザーのカスタム登録解除 URL | {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %}<br><br>このタグは、前の {% raw %}`{{${unsubscribe_url}}}`{% endraw %} タグを置き換えます。代わりに新しい {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} タグを使用することをおすすめします。 |
|ユーザーのカスタムオプトイン URL | {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} |
|ユーザーのカスタム購読 URL | {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}|
|ユーザーカスタムBrazeプリファレンスセンターURL | {% raw %}`{{${preference_center_url}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2}

### 登録解除リンクとオプトインリンクを含める

{% raw  %}
ベストプラクティスとして、Brazeでは、カスタムフッターに登録解除リンク( など ``{{${set_user_to_unsubscribed_url}}}``)とオプトインリンク( など ``{{${set_user_to_opted_in_url}}}``)の両方を含めることをお勧めします。これにより、ユーザーは登録解除またはオプトインの両方を行うことができ、一部のユーザーのオプトインデータを受動的に収集できます。
{% endraw %}

### プレーンテキストメールのカスタムフッターの設定

また、HTMLメールのカスタムフッターと同じルールに従って、[**メール設定**]ページの[**購読ページとフッター**]タブから、プレーンテキストメールのカスタムフッターを設定することもできます。プレーンテキストのフッターを含めない場合、BrazeはHTMLフッターから自動的にフッターを作成します。カスタムフッターが気に入ったら、ページ下部の [ **保存** ] をクリックします。

![カスタムプレーンテキストフッターの設定オプションが選択されたメール][23]{: style="max-width:70%" }

[20]: {% image_buster /assets/img_archive/custom_footer.png %}
[21]: {% image_buster /assets/img_archive/no_unsub_link_warning.png %}
[22]: {% image_buster /assets/img_archive/no_footer_test.png %}
[23]: {% image_buster /assets/img_archive/custom_footer_save_changes.png %}
[24]: {% image_buster /assets/img_archive/email_unsub_protocol.png %}
