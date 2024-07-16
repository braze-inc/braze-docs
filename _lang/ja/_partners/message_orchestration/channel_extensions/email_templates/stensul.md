---
nav_title: Stensul
article_title:Stensul
alias: /partners/stensul
description:"この参考記事では、BrazeとStensulのパートナーシップについて概説している。"Stensulは、チャネル間でモバイルレスポンシブなメールテンプレートを簡単に作成できるエンタープライズメールプラットフォームである。
page_type: partner
search_tag:Partner

---

# Stensul

> [Stensulは](https://stensul.com/)、モバイルマーケティングのマーケターが、Stensulで簡単にモバイルにレスポンシブでオンブランドのメールを作成し、それをリアルタイムでBrazeに送信してキャンペーンを作成できるようにする。

BrazeとStensulの統合により、HTMLフォーマットのStensulメールをエクスポートし、Braze内でテンプレートとしてアップロードできる。

## 前提条件

| 必要条件 | 説明 |
| ------------| ----------- |
| Stensulアカウント | このパートナーシップを利用するにはStensulアカウントが必要である。 |
| Braze REST API キー | 完全な**テンプレート**権限を持つBraze REST APIキー。<br><br> これはダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| クラスターインスタンス | Braze[クラスターインスタンスは]({{site.baseurl}}/api/basics/#endpoints)、BrazeダッシュボードおよびRESTエンドポイントと一致する。  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 統合

お客様のBraze REST APIキーとクラスターインスタンスをStensulカスタマーサクセスチームに提供する。その後、チームが初期統合を設定する。

{% alert important %}
これは1回限りのセットアップであり、今後のエクスポートは自動的にこのAPIキーを利用することになる。
{% endalert %}

### ステップ1:Stensulメールを作成する

StensulプラットフォームでStensulメールを作成し、**完了を**クリックする。

![Stensul Save Options]({% image_buster /assets/img_archive/stensul_save_options.png %})

### ステップ2:Brazeにテンプレートをエクスポートする
完了ページに表示される新しいダイアログで、メールサービスプロバイダー（E**SP）へのアップロードを**選択する。

![Stensul Upload Options]({% image_buster /assets/img_archive/stensul_upload_options.png %})

次に、メールの**テンプレート名**、**件名**、**プレヘッダーを**入力し、**アップロードを**選択する。その後、アップロードが成功したことの確認と、該当する場合はそのファイルの過去のアップロード履歴が表示される。

![Stensul Upload Success]({% image_buster /assets/img_archive/stensul_upload_success.png %})

## 使用

アップロードしたStensulテンプレートを、Brazeアカウントの「**テンプレート＆メディア」>「メールテンプレート**」から探す。このテンプレートを使って、カスタマーにエンゲージメントメッセージを送ることができる！

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
