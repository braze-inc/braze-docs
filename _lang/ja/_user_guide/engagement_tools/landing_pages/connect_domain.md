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

1. [**設定**] > [**ランディングページの設定**] に移動します。
2. 接続するドメインまたはサブドメインを入力し、**Submit** を選択します。たとえば `forms.example.com` です。
3. **TXT** および**CNAME** レコードをコピーして、ドメインプロバイダーのDNS 設定に貼り付けます。
4. Braze ダッシュボードに戻り、接続を確認します。

![ランディングページ設定ページには、1 つのTXT レコードと2 つのCNAME レコードがそれぞれの名前と値とともにリストされています。][1]

{% alert note %}
ドメインプロバイダーによっては、接続に最大48時間かかることがあります。プロセスが完了したら、Braze ダッシュボードのランディングページでカスタムドメインの使用を開始します。
{% endalert %}

## Braze でのドメインの使用

ドメインの検証が完了すると、デフォルトではドメインは Braze で使用されます。たとえば、サブドメイン`forms.example.com` を接続すると、ランディングページURL は`forms.example.com/holiday-sale` のように更新されます。

{% alert note %}
カスタムドメインの削除がまもなく行われます。サブドメインを削除する必要がある場合は、カスタマーサクセスマネージャーに連絡してください。
{% endalert %}

## ドメインプロバイダーのリソース

以下に、一般的に使用されるドメインプロバイダでDNS レコードを作成および管理するためのリソースを示します。別のプロバイダーを使用している場合は、そのプロバイダーのドキュメントを参照するか、サポートチームにお問い合わせください。

| ドメインプロバイダー | リソース |
| --- | --- |
| Bluehost | [DNS レコードの説明](https://my.bluehost.com/hosting/help/508)<br> [DNS 管理DNS エントリの追加編集または削除](https://my.bluehost.com/hosting/help/559) |
| Dreamhost | [カスタム DNS レコードを追加する方法](https://help.dreamhost.com/hc/en-us/articles/360035516812) |
| GoDaddy | [CNAME レコードの追加](https://www.godaddy.com/help/add-a-cname-record-19236?) |
| Cloudflare | [DNS レコードの管理](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) |
| Squarespace | [カスタムDNS 設定の追加](https://support.squarespace.com/hc/en-us/articles/360002101888-Adding-custom-DNS-records-to-your-Squarespace-managed-domain) |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## トラブルシューティング 

### ドメイン接続に失敗しました

ドメインが正しく入力され、ドメインプロバイダアカウントからBraze に送信したものと一致していることを確認します。正しく一致する場合は、Braze が提供するTXT およびCNAME レコードを確認します。これらのレコードは、ドメインプロバイダーアカウントに入力したレコードと一致している必要があります。

## よくある質問

### 複数のサブドメインをワークスペースに接続することも、1 つのサブドメインを複数のワークスペースに接続することもできますか?

いいえ。現在、1 つのサブドメインのみをワークスペースに接続できます。

[1]: {% image_buster /assets/img/landing_pages/connect_subdomain.png %}
