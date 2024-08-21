---
nav_title: Stensul
article_title: Stensul
alias: /partners/stensul
description: "このリファレンス記事では、Braze とStensul の連携について概説します。これは、チャネル s 間でモバイルレスポンシブ メール テンプレートを簡単に作成できるエンタープライズメール プラットフォームです。"
page_type: partner
search_tag: Partner

---

# Stensul

> [Stensul](https://stensul.com/) は、メール マーケター s がStensul で簡単にモバイルレスポンシブのオンブランドメールを構築できるようにします。その後、リアルタイムでBraze に送信し、キャンペーンを作成します。

BrazeとStensulインテグレーションを使用すると、Braze内でHTML形式のStensul メールsをエクスポートし、テンプレートsとしてアップロードできます。

## 前提条件

| 要件 | 説明 |
| ------------| ----------- |
| Stensul勘定 | この提携の前進タグeを考慮するには、Stensulな考慮が必要である。 |
| Braze REST API キー | 完全な**テンプレート**権限を持つBraze REST API キー。<br><br> これは、**Settings** > **API Keys** のBraze ダッシュボードで作成できます。 |
| クラスタインスタンス | Braze[cluster instance]({{site.baseurl}}/api/basics/#endpoints) は、Braze ダッシュボードとREST エンドポイントに合わせます。  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 統合

Braze REST API キーとクラスターインスタンスをStensul カスタマーサクセスチームに提供します。チームは、最初の統合を設定します。

{% alert important %}
これは1 回限りの設定であり、今後のエクスポートではこのAPI キーが自動的に使用されます。
{% endalert %}

### ステップ1:Stensul メールの作成

Stensul プラットフォームにStensul メールを作成し、**Complete**を押します。

![Stensul保存オプション]({% image_buster /assets/img_archive/stensul_save_options.png %})

### ステップ2:Brazeへのテンプレートのエクスポート
アプリが完了ページで耳にする新しいダイアログで、<サービスプロバイダー an id="1">Up 読み込む to メールサービスプロバイダー (ESP)</サービスプロバイダー an> を選択します。

![Stensulアップ読み込むオプション]({% image_buster /assets/img_archive/stensul_upload_options.png %})

次に、メールの ** テンプレート name**、**subject**、および **preヘッダー** を入力し、**Up読み込む** を選択します。アプリに応じて、アップロードが成功したかどうかの確認と、以前のアップロードの履歴が表示されます。

![Stensulアップ読み込む成功]({% image_buster /assets/img_archive/stensul_upload_success.png %})

## 使用

Braze アカウントの ** テンプレート s& Media > E メールテンプレート s** セクションで、アップロードのStensul テンプレートを見つけます。これで、このメール テンプレートを使用してメールを顧客 s に送信できるようになりました。

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
