---
nav_title: メールリストのインポート
article_title: メールリストをBrazeにインポートする
page_order: 4
page_type: reference
description: "この参考記事では、メールリストをBrazeにインポートするためのベストプラクティスを解説している。"
channel: email

---

# メールリストを Braze にインポートする {#importing-email-lists}

> メール送信を成功させるための重要なステップとして、質の高いメールリストを確保することがあります。適切なメールリスト管理によって配信到達性が向上し、より正確でクリーンなキャンペーン成果を得ることができます。

## 輸入前の注意事項

{% multi_lang_include email-via-sms-warning.md %}

### Eメールリストを検証する

BrazeにEメールリストをインポートする前に、リストに本物のEメールアドレスだけが含まれていることを確認する。バウンス率が高いと、メール送信者の評判が下がる。 

Eメールリストのクリーニングサービスは、Eメールアドレスが正しい構文に従っているかどうか、Eメールアドレスの物理的な特性を持っているかどうかを判断し、Eメールのドメインを確認し、Eメールアドレスがそこに存在するかどうかを認証するためにEメールサーバーに接続することによって、あなたのためにこれを行うことができる。

### エンゲージメントの高いユーザーを特定する

最もエンゲージメントの高いユーザーを特定するためには、まず、長期間にわたって離脱しているユーザーを排除します。メール送信者としての評判が損なわれないよう、6 か月以上メールのエンゲージメントがないユーザーにはメールを送信しないのがベストプラクティスです。メールリストをインポートする際は、過去 6 か月以内にメールを開封したユーザーだけを含めるようにします。

長期的には、[サンセットポリシー][60]の導入も検討する必要があります。

### 抑制リストを避ける

既存のEメールプロバイダから移行する場合は、抑制リストからユーザーをインポートしないように注意すること。抑制リストは、配信停止、スパム扱い、あるいはハードバウンスされたメールアドレスがリストされています。

## インポート方法

メールリストの準備ができたら、Braze REST API や CSV ファイルなど、Braze にユーザーをインポートする方法がいくつかあります。詳細については、[ユーザーインポート]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/)の専用記事を参照してください。

[60]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/
