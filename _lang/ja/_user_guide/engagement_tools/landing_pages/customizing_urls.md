---
nav_title: URLをカスタマイズする
article_title: ランディングページのURLをカスタマイズする
description: "ドメインをBrazeワークスペースに接続することで、ランディングページのURLを企業ブランドに合わせてカスタマイズする方法を学習。"
page_order: 1
---

# ランディングページのURLをカスタマイズする

> ドメインをBrazeワークスペースに接続することで、ランディングページのURLを企業ブランドに合わせてカスタマイズする方法を学習。

## CDI の仕組み

[Brazeにドメインを接続](#connecting-your-domain-to-braze)すると、そのドメインがすべてのランディングページのデフォルトドメインとして使用される。例えばサブドメイン `forms.example.com` を接続すると、ランディングページ URL は `forms.example.com/holiday-sale` のようになります。

Braze アカウントに接続できるカスタムドメインの数は、[プランティア]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/#plan-tiers) によって異なります。制限を増やすには、Braze アカウントマネージャにお問い合わせください。

## ドメインをBrazeに接続する

ドメインを Braze アカウントに接続するには、管理者に次の手順を実行してもらいます。

1. [**設定**] > [**ランディングページの設定**] に移動します。
2. 接続するドメインを入力し、**Submit** を選択します。たとえば `forms.example.com` です。
3. **TXT** および**CNAME** レコードをコピーして、ドメインプロバイダーのDNS 設定に貼り付けます。
4. Braze ダッシュボードに戻り、接続を確認します。

![ランディングページ設定ページで、1 つのTXT と2 つのCNAME レコードがそれぞれの名前と値とともにリストされています。]({% image_buster /assets/img/landing_pages/connect_subdomain.png %})

{% alert note %}
ドメインプロバイダーによっては、接続に最大48時間かかることがあります。プロセスが完了したら、Braze ダッシュボードのランディングページでカスタムドメインの使用を開始します。
{% endalert %}

## ドメインの削除

Braze 管理者は、次の手順で以前に設定したドメインを削除できます。

1. [**設定**] > [**ランディングページの設定**] に移動します。
2. [**カスタムドメインを削除**] を選択します。
3. ドメインの削除を確認します。
4. 表示されているDNS レコードをドメイン設定から削除します。

{% alert important %}
カスタムドメインを削除すると、そのURL は無効になります。このドメインを使用していたランディングページは、自動的にBraze で設定されたデフォルトドメインに戻ります。
{% endalert %}


## DNSリソース

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

### 現在メインサイトで使用しているサブドメインや送信ドメインと同じものを使用できるか？

いや、すでに使われているサブドメインを使うことはできない。これらのサブドメインは有効だが、すでに他の目的に割り当てられていたり、必要なCNAMEレコードと競合するDNSレコードを持っている場合は、ランディングページに使用することはできない。

