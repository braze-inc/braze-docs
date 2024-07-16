---
nav_title: Vizbee
article_title:TVディープリンクのためのVizbee
alias: /partners/vizbee_for_tv_deeplinking/
page_type: partner
description:"この参考記事では、BrazeとVizbeeのパートナーシップと、TVディープリンクをサポートするための使用方法について説明している。"
search_tag:Partner

---
# Vizbee {#vizbee}

> [Vizbeeは][1]、家庭内のすべてのスマートフォンとスマートテレビを1つのシームレスなデバイスとして連携させ、優れたユーザー体験を可能にする。Vizbeeは、通知、ディープリンク、メールなどの既存のモバイルアプリマーケティングチャネルを活用し、すべてのコネクテッドTV（CTV）デバイス（Roku、FireTV、Samsung TV、LG TVなど）で視聴者をシームレスに獲得し、エンゲージメントすることができる。

BrazeとVizbeeの統合により、単一のコンソールを使用して、モバイルとCTVデバイスの両方のストリーミングアプリで視聴者を獲得し、維持するためのマーケティングキャンペーンをスケジュールさせることができる。この統合によって、あなたは次のことができる：
- ターゲットユーザーへのモバイル通知をスケジュールされ、タップすると、モバイルアプリの視聴につながったり、近くのストリーミングデバイスやテレビでの再生をシームレスに呼び出したりできる。
- ターゲットユーザーへのメールマーケティングキャンペーンをスケジュールさせ、タップすると、CTVアプリの自動インストールや、RokuやFireTVなどのCTVデバイスへのユーザーのサインインが可能になる。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Vizbeeアカウント | このパートナーシップを利用するには、[Vizbee][1]アカウントが必要である。アプリをVizbeeに登録し、Vizbee IDを割り当てる必要がある。 |
| iOSまたはAndroidアプリ | この統合はiOSとAndroidアプリをサポートしている。プラットフォームによっては、アプリケーションにコード・スニペットが必要な場合がある。 |
| Vizbee SDK | 必要なBraze SDKに加えて、Vizbee SDKをインストールする必要がある。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

Vizbeeの[SDK統合ガイドに従って][2]、VizbeeとBrazeの統合を立ち上げ、実行する。ここでは、モバイルからテレビへのディープリンク、テレビアプリのインストール、視聴率アトリビューションに関するガイダンスを見ることができる。 

### インストールとアトリビューションレポートを見る {#vizbee-tv-app-installs-viewership-attribution}

また、Vizbeeとイネーブルメントは、モバイルとCTVデバイスを横断して、キャンペーンの全体的なパフォーマンスを表示することができる。Vizbee SDKはBraze SDKにカスタムイベントを送信し、Brazeダッシュボードからキャンペーンレポートで確認できる。

[1]: https://vizbee.tv/
[2]: https://console.vizbee.tv/app/vzb1765003429/develop/guides/ios-continuity
