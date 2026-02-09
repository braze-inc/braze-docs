---
nav_title: Vizbee
article_title: Vizbee (TV ディープリンク)
alias: /partners/vizbee/
page_type: partner
description: "このリファレンス記事では、Braze と Vizbee のパートナーシップと、これを利用して TV ディープリンクをサポートする方法について説明します。"
search_tag: Partner

---
# Vizbee {#vizbee}

> [Vizbee](https://vizbee.tv/) は、ご家庭のすべてのスマートフォンとスマートテレビを1つのシームレスなデバイスとして連携させ、優れたユーザーエクスペリエンスを実現します。Vizbeeは、通知、ディープリンク、メールなどの既存のモバイルアプリマーケティングチャネルを使用して、すべてのコネクテッドTV（CTV）デバイス（Roku、FireTV、Samsung TV、LG TVなど）で視聴者をシームレスに獲得し、エンゲージメントすることができる。

_この統合はVizbeeによって維持されています。_

## 統合について

Braze と Vizbee の統合により、モバイルデバイスと CTV デバイスの両方でストリーミングアプリの視聴者を獲得、維持するためのマーケティングキャンペーンを、1つのコンソールでスケジュールできます。この統合により、次のことが可能になります。
- ターゲットユーザーへのモバイル通知をスケジュールする。このモバイル通知では、タップ操作でモバイルアプリで視聴できたり、近くにあるストリーミングデバイスやテレビでの再生をシームレスに実行できたりします。
- ターゲットユーザーへのEメールマーケティングキャンペーンをスケジュールし、タップすると、CTVアプリの自動インストールや、RokuやFireTVなどのCTVデバイスへのサインインが可能になる。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Vizbeeアカウント | このパートナーシップを利用するには、[Vizbee](https://vizbee.tv/)アカウントが必要である。Vizbee でアプリを登録し、Vizbee ID を割り当てる必要があります。 |
| iOSまたはAndroidアプリ | この統合では、iOS アプリと Android アプリがサポートされています。プラットフォームによっては、アプリケーションにコード・スニペットが必要になるかもしれない。 |
| Vizbee SDK | 必要な Braze SDK に加えて、Vizbee SDK をインストールする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

Vizbee の [SDK 統合ガイド](https://console.vizbee.tv/app/vzb1765003429/develop/guides/ios-continuity)に従って、Vizbee と Braze の統合を稼働させます。ここでは、モバイルからテレビへのディープリンク、テレビアプリのインストール、視聴率アトリビューションに関するガイダンスを見ることができる。 

### インストールおよびアトリビューションレポートの表示 {#vizbee-tv-app-installs-viewership-attribution}

また、VizbeeとBrazeは、モバイルとCTVデバイスにまたがるキャンペーンの総合的なパフォーマンスを表示することもできる。Vizbee SDK はカスタムイベントを Braze SDK に送信します。カスタムイベントは、Braze ダッシュボードからキャンペーンレポートで確認できます。


