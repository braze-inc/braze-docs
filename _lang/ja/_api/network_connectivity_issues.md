---
nav_title: APIネットワーク接続の問題
article_title: APIネットワーク接続の問題
page_order: 4
description: "この参考記事では、API接続の問題とそのトラブルシューティング方法について触れています。"
page_type: reference

---

# APIネットワーク接続の問題

> この参考記事では、API接続の問題とそのトラブルシューティング方法について触れています。

Braze APIエンドポイントは、DNS情報に基づいて最も近いPOPにトラフィックをルーティングするCDNを使用します。 接続に問題がある場合、または効率的でないPOPに接続していることに気づいた場合は、プロバイダーのDNSサーバー、またはサーバーと同じデータセンターに設置され、適切なIPロケーションメタ情報が関連付けられているDNSサーバーを使用するようにしてください。

我々は、Braze APIエンドポイントへの接続を妨害するHTTPS/TLSトラフィックを変更または保護しようとする一握りのファイアウォールがあることに気づきました。サーバーが何らかの物理的なファイアウォールの背後にある場合、ファイアウォールやルーターが実行しているHTTPS/TLSのアクセラレーションや変更を無効にしてください。さらに、当社の CDN プロバイダー (Fastly.com) へのアウトバウンドトラフィックを許可して、問題が解決されるかを確認することもできます。

SYN/ACK/RST パケットにフィルターするiptables の設定によっても問題が発生することがあります。そのため、ホストでiptables を使用している場合は、CDN プロバイダへのアウトバウンドトラフィック(Fastly.com) を許可して問題が解決するかどうかを確認することもできます。

それでもBraze APIエンドポイントへの接続にネットワークの問題がある場合は、問題が発生している間の[MTRテストと](https://www.privateinternetaccess.com/helpdesk/kb/articles/what-is-an-mtr-test-and-how-do-i-run-one-2) [Fastly Debugの](http://www.fastly-debug.com/)結果を提供し、それをサポートリクエストと一緒に提出してください。テスト結果は、開発マシンからではなく、Braze API エンドポイントへの接続に問題があるサーバーから取得しなければならないことに注意してください。ネットワークキャプチャ（tcpdumpまたは.pcapファイル）も入手できれば役に立ちます。

MTRの詳細については、お使いのオペレーティング・システムに応じて、以下のリソースをチェックしてください：

- [GNU/Linux](https://www.digitalocean.com/community/tutorials/how-to-use-traceroute-and-mtr-to-diagnose-network-issues)
- [macOS](https://formulae.brew.sh/formula/mtr)

## Braze API エンドポイントの IP 範囲の許可リスト登録

ファイアウォールを通して Braze API エンドポイントを許可リストに登録するために、当社の CDN は、JSON ダンプを介して割り当てられた IP 範囲のリストへのアクセスを提供しています。Braze API の IP範囲のリストについては、[Fastly の公開 IP リスト](https://api.fastly.com/public-ip-list)と [Cloudflare の公開 IP リスト](https://api.cloudflare.com/client/v4/ips)の両方を参照してください。これらのIPは変更される可能性があります。

