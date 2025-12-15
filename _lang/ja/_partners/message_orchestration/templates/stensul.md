---
nav_title: Stensul
article_title: Stensul
alias: /partners/stensul
description: "この参考記事では、Brazeと、チャネルを横断してモバイルレスポンシブなメールテンプレートを作成するためのエンタープライズメールプラットフォームStensulのパートナーシップについて概説している。"
page_type: partner
search_tag: Partner

---

# Stensul

> [Stensulは](https://stensul.com/)、モバイルマーケティング担当者に、キャンペーン作成のためにリアルタイムでBrazeに送信する前に、Stensulでモバイルレスポンシブでオンブランドのメールを作成するためのツールを提供する。

_この統合は Stensul によって管理されます。_

## 統合について

Braze と Stensul の統合により、HTML 形式の Stensul メールをエクスポートし、Braze 内でテンプレートとしてアップロードできます。

## 前提条件

| 必要条件 | 説明 |
| ------------| ----------- |
| Stensul アカウント | このパートナーシップを活用するには、Stensul アカウントが必要です。 |
| Braze REST API キー | 完全な**テンプレート**権限を持つBraze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| クラスタインスタンス | Braze [クラスターインスタンス]({{site.baseurl}}/api/basics/#endpoints)は、Braze ダッシュボードと REST エンドポイントに対応しています。  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 統合

Braze REST API キーとクラスターインスタンスをStensul カスタマーサクセスチームに提供します。その後、このチームが初期統合を設定できます。

{% alert important %}
これは1 回限りの設定であり、今後のエクスポートではこのAPI キーが自動的に使用されます。
{% endalert %}

### ステップ1:Stensul メールを作成する

Stensul プラットフォームで Stensul メールを作成し、[**Complete**] をクリックします。

![Stensul 保存オプション]({% image_buster /assets/img_archive/stensul_save_options.png %})

### ステップ 2:Brazeへのテンプレートのエクスポート
完了ページに表示される新しいダイアログで、[**Upload to ESP**] を選択します。

![アップロードオプション]({% image_buster /assets/img_archive/stensul_upload_options.png %})

次に、メールの ** テンプレート name**、**subject**、および **preヘッダー** を入力し、**Up読み込む** を選択します。アップロードが成功したことを示す確認と、該当する場合はファイルの過去のアップロード履歴が表示されます。

![Stensulアップロードの成功]({% image_buster /assets/img_archive/stensul_upload_success.png %})

## 使用

アップロードしたStensulテンプレートを、Brazeアカウントの**テンプレート& メディア > メールテンプレートセクションで**探す。これで、このメールテンプレートを使用して、顧客に魅力的なメールメッセージを送信できます。


