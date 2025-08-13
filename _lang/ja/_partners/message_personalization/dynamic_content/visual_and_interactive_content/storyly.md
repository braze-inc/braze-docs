---
nav_title: Storyly
article_title: Storyly
description: "このリファレンス記事では、Braze と Storyly のパートナーシップについて説明します。Storyly は、アプリオーナーがセグメントを絞り込み、より多くのファーストパーティデータを Braze にフィードできるようにする軽量 SDK です。"
alias: /partners/storyly/
page_type: partner
search_tag: Partner

---

# Storyly

> [Storyly](https://www.storyly.io/) は、アプリや Web サイトにストーリーをもたらす軽量 SDK です。直感的なデザインスタジオ、洞察に満ちた分析、シームレスな接続性を備えたStorylyは、視聴者の体験を豊かにする強力なツールだ。 

_この統合は Storyly によって管理されます。_

## 統合について

Braze と Storyly の統合により、Braze のセグメントを Storyly プラットフォームでオーディエンスとして使用できます。この統合により、次のことが可能になります。
- 特定のストーリーを持つセグメントをターゲットにする
- ユーザー属性を使ってストーリー・コンテンツをパーソナライズする

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Storyly アカウント | このパートナーシップを活用するには、Storyly アカウントが必要です。 |
| Storyly SDK | [Storyly SDK](https://integration.storyly.io/)をインストールする必要があります。 |
| Braze REST API キー | 以下の権限を持つBraze REST APIキー。 <br><br> `users.export.ids`<br> `users.export.segments`<br> `segments.list`<br> `segments.details`<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze REST エンドポイント | [あなたのRESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。お客様のエンドポイントは、お客様のインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

BrazeとStorylyの統合により、アプリのオーナーはBrazeの全セグメントにストーリーを表示し、ユーザー属性でストーリーをパーソナライズすることができる。

一般的な使用例には以下のようなものがある：

__Storyly で Braze セグメントをターゲットにする__<br>統合が完了したら、Brazeセグメントに基づいてStorylyオーディエンスを作成できる。これは、デモグラフィックセグメントまたは行動セグメントです。例えば、特定の場所に住んでいるユーザー、アプリで特定のアクションを起こしたユーザー、特定のストーリーのある特定の商品に興味があるユーザーなどをターゲットにすることで、コンバージョンを高めることができる。<br>
__ユーザー属性でパーソナライズされたストーリー__<br>Brazeのユーザー属性はStorylyでも使用でき、動的なストーリーを生成することができる。これには、ユーザーの名前、買い物かごに入っている製品、お気に入りの製品などを含めることができ、独自のパーソナライズされたストーリーをユーザーに提供できます。パーソナライゼーションは、ストーリーのコンバージョン率とストーリー全体のエンゲージメント率を高めるのに役立つ。

## データ・エクスポートの統合

Braze Storylyの統合については、以下のビデオで説明されている：

{% multi_lang_include video.html id="3-OEqQs48Zw" source="youtube" %}

Storylyインテグレーションがカスタムパラメータを保持していることを確認する。これらのパラメーターは、Braze `external id` ユーザープロパティに対応します。ここでは、[iOS](https://integration.storyly.io/ios/personalization-customaudience.html)、[Android](https://integration.storyly.io/android/personalization-customaudience.html)、[React Native](https://integration.storyly.io/react-native/personalization-customaudience.html)、[Flutter](https://integration.storyly.io/flutter/personalization-customaudience.html)、[Web](https://integration.storyly.io/web/personalization-customaudience.html)用のカスタム・パラメーターの実装について説明する。

詳細については、[Storyly](https://docs.storyly.io/page/connect-your-braze-audiences-with-storyly) のドキュメントを参照してください。

### ステップ1:Storylyダッシュボードで統合を設定する

**Storylyダッシュボード > [Settings] > [Integrations] > [Connect with Braze]** で統合が作成されます。ここでは、Braze REST APIキーとBraze RESTエンドポイントが必要である。 

### ステップ2:セグメントを取得する 

次に、Braze セグメントを使用して Storyly オーディエンスを作成できます。これは、**Storylyダッシュボード > [Settings] > [Audiences] > [New Audience] > [Create Audience with Braze]** で作成できます。

ここには2つの同期オプションがあります。特定のキャンペーン・ストーリーには**1回限りの同期を**、長期的なストーリーには**毎日の同期を**選択する。


