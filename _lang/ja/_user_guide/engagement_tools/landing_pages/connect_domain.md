---
nav_title: ドメインの接続
article_title: ドメインの接続
description: "この記事では、独自のカスタムドメインをBraze ランディングページに接続する方法について説明します。"
page_order: 1
alias: /landing_pages/connect_domain/
---

# ドメインの接続

> ブランドのランディングページURL をカスタマイズするには、独自のドメインをBraze ワークスペースに接続します。

ドメインまたはサブドメインをBraze アカウントに接続するには、管理者に次の手順を実行してもらいます。

1. **Settings**> **Landing Page Settings**に進みます。
2. 接続するドメインまたはサブドメインを入力し、**Submit** を選択します。たとえば `forms.example.com` です。
3. **TXT** および**CNAME** レコードをコピーして、ドメインプロバイダーのDNS 設定に貼り付けます。
4. Braze ダッシュボードに戻り、接続を確認します。

![ランディングページ設定ページには、1 つのTXT レコードと2 つのCNAME レコードがそれぞれの名前と値とともにリストされています。][1]

{% alert note %}
ドメインプロバイダーによっては、接続に最大48 時間かかる場合があります。プロセスが完了したら、Braze ダッシュボードのランディングページでカスタムドメインの使用を開始します。
{% endalert %}

## ブレーズでのドメインの使用

ドメインの検証が完了すると、デフォルトではブレーズで使用されます。たとえば、サブドメイン`forms.example.com` を接続すると、ランディングページURL は`forms.example.com/holiday-sale` のように更新されます。

{% alert note %}
カスタムドメインの削除がまもなく行われます。サブドメインを削除する必要がある場合は、カスタマーサクセスマネージャーに連絡してください。
{% endalert %}

## ドメインプロバイダからのリソース

以下に、一般的に使用されるドメインプロバイダでDNS レコードを作成および管理するためのリソースを示します。別のプロバイダを使用している場合は、そのプロバイダのマニュアルを参照するか、サポートチームにお問い合わせください。

| ドメインプロバイダー | リソース |
| --- | --- |
| ブルーホスト | [DNSレコードの説明](https://my.bluehost.com/hosting/help/508)<br> [DNS 管理DNS エントリの追加編集または削除](https://my.bluehost.com/hosting/help/559) |
| ドリームホスト | [カスタムDNS レコードを追加するには?](https://help.dreamhost.com/hc/en-us/articles/360035516812) |
| ゴダディー | [CNAME レコードの追加](https://www.godaddy.com/help/add-a-cname-record-19236?) |
| クラウドフレア | [DNS レコードの管理](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) |
| スクエアスペース | [カスタムDNS 設定の追加](https://support.squarespace.com/hc/en-us/articles/360002101888-Adding-custom-DNS-records-to-your-Squarespace-managed-domain) |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## トラブルシューティング 

### ドメイン接続に失敗しました

ドメインが正しく入力され、ドメインプロバイダアカウントからBraze に送信したものと一致していることを確認します。正しく一致する場合は、Braze が提供するTXT およびCNAME レコードを確認します。これらは、ドメインプロバイダアカウントに入力したレコードと一致する必要があります。

## よくある質問

### 複数のサブドメインをワークスペースに接続することも、1 つのサブドメインを複数のワークスペースに接続することもできますか?

いいえ。現在、1 つのサブドメインのみをワークスペースに接続できます。

[1]: {% image_buster /assets/img/landing_pages/connect_subdomain.png %}
