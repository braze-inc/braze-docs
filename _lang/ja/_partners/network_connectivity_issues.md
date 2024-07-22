---
nav_title: API ネットワーク接続の問題
article_title: API ネットワーク接続の問題
page_order: 4
description: "この参考記事では、API 接続の問題とそのトラブルシューティング方法について説明しています。"
page_type: reference

---

# API ネットワーク接続の問題

> この参考記事では、API 接続の問題とそのトラブルシューティング方法について説明しています。

Braze API エンドポイントは CDN を使用し、DNS 情報に基づいてトラフィックを最も近い POP にルーティングします。 接続に問題がある場合や、効率的でないPOPに接続していることに気付いた場合は、プロバイダーのDNSサーバーまたはサーバーと同じデータセンターに設置され、適切なIPロケーションのメタ情報が関連付けられているDNSサーバーを使用してください。

一部のファイアウォールが、Braze API エンドポイントへの接続を妨害する HTTPS/TLS トラフィックを変更または保護しようとしていることがわかりました。サーバーが何らかの物理ファイアウォールの背後にある場合は、ファイアウォールまたはルーターが実行しているHTTPS/TLSアクセラレーションまたは変更をすべて無効にしてください。さらに、CDN プロバイダー (Fastly.com) へのアウトバウンドトラフィックを許可リストに登録して、問題が解決するかどうかを確認できます。

場合によっては、iptables セットアップが SYN でフィルタリングされることがあります/ACK/RST packets can also cause issues, so if you are using iptables on your host you could also allowlist outbound traffic to our CDN providers (Fastly.com) to see if that resolves the issue.

Braze API エンドポイントへの接続でネットワークの問題が解決しない場合は、問題が発生している間に [MTR テストと][1] [Fastly Debug][2] の結果を提供して、サポートリクエストとともに送信してください。テスト結果は、開発マシンからではなく、Braze API エンドポイントへの接続に問題があるサーバーから取得する必要があることに注意してください。ネットワークキャプチャ (tcpdump または.pcap ファイル) も入手できれば役に立ちます。

MTR の詳細については、ご使用のオペレーティングシステムに応じた以下のリソースをご覧ください。

- [GNU/Linux][4]
- [MacOSの][5]

## Braze API エンドポイントの IP 範囲を許可リストに登録する

ファイアウォールを通じて Braze API エンドポイントを許可リストに追加するために、CDN は JSON ダンプを通じて割り当てられた IP 範囲のリストへのアクセスを提供します。Braze API IP範囲のリストについては、[[FastlyのパブリックIPリストとCloudflareのパブリックIPリストの両方を参照してください][6]][3]。これらの IP は変更される可能性があることに注意してください。

[1]: https://www.privateinternetaccess.com/helpdesk/kb/articles/what-is-an-mtr-test-and-how-do-i-run-one-2
[2]: http://www.fastly-debug.com/
[3]: https://api.fastly.com/public-ip-list
[4]: https://www.digitalocean.com/community/tutorials/how-to-use-traceroute-and-mtr-to-diagnose-network-issues
[5]: https://formulae.brew.sh/formula/mtr
[6]: https://api.cloudflare.com/client/v4/ips
