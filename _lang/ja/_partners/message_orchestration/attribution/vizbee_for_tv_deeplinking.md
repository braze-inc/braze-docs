---
nav_title: ヴィズビー
article_title: TVディープリンクのためのVizbee
alias: /partners/vizbee_for_tv_deeplinking/
page_type: partner
description: "この参考記事では、BrazeとVizbeeのパートナーシップと、TVディープリンクをサポートするための使用方法について説明している。"
search_tag: Partner

---
# Vizbee {#vizbee}

> [Vizbeeは][1]、家庭内のすべてのスマートフォンとスマートテレビを1つのシームレスなデバイスとして連携させ、優れたユーザー体験を可能にする。Vizbeeは、通知、ディープリンク、Eメールなどの既存のモバイルアプリ・マーケティング・チャネルを活用し、すべてのコネクテッドTV（CTV）デバイス（Roku、FireTV、Samsung TV、LG TVなど）で視聴者をシームレスに獲得し、エンゲージすることができる。

BrazeとVizbeeの統合により、単一のコンソールを使用して、モバイルとCTVデバイスの両方のストリーミングアプリで視聴者を獲得し、維持するためのマーケティングキャンペーンをスケジュールすることができる。この統合によって、あなたは次のことができる：
- ターゲットユーザーにモバイル通知をスケジュールし、タップすると、モバイルアプリの視聴につながったり、近くのストリーミングデバイスやテレビでの再生をシームレスに呼び出したりできる。
- ターゲットユーザーへのEメールマーケティングキャンペーンをスケジュールし、タップすると、CTVアプリの自動インストールや、RokuやFireTVなどのCTVデバイスへのサインインが可能になる。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Vizbeeアカウント | このパートナーシップを利用するには、[Vizbee][1]アカウントが必要である。Vizbeeにアプリを登録し、Vizbee IDを割り当てる必要がある。 |
| iOSまたはAndroidアプリ | この統合はiOSとAndroidアプリをサポートしている。プラットフォームによっては、アプリケーションにコード・スニペットが必要になるかもしれない。 |
| Vizbee SDK | 必要なBraze SDKに加えて、Vizbee SDKをインストールする必要がある。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

Vizbeeの[SDK統合ガイドに従って][2]、VizbeeとBrazeの統合を立ち上げ、実行する。ここでは、モバイルからテレビへのディープリンク、テレビアプリのインストール、視聴率アトリビューションに関するガイダンスを見ることができる。 

### インストール・レポートとアトリビューション・レポートを見る {#vizbee-tv-app-installs-viewership-attribution}

また、VizbeeとBrazeは、モバイルとCTVデバイスにまたがるキャンペーンの総合的なパフォーマンスを表示することもできる。Vizbee SDKはBraze SDKにカスタムイベントを送信し、Brazeダッシュボードからキャンペーンレポートで確認できる。

[1]: https://vizbee.tv/
[2]: https://console.vizbee.tv/app/vzb1765003429/develop/guides/ios-continuity
