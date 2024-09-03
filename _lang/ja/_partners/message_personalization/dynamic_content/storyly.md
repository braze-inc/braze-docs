---
nav_title: ストーリー
article_title: ストーリー
description: "この参考記事では、Brazeと軽量SDKであるStorylyのパートナーシップについて概説しており、アプリ所有者はセグメントを絞り込み、より多くのファーストパーティデータをBrazeに供給することができる。"
alias: /partners/storyly/
page_type: partner
search_tag: Partner

---

# ストーリー

> [Storylyは](https://www.storyly.io/)、あなたのアプリやウェブサイトにストーリーをもたらす軽量SDKだ。直感的なデザインスタジオ、洞察に満ちた分析、シームレスな接続性を備えたStorylyは、視聴者の体験を豊かにする強力なツールだ。 

BrazeとStorylyの統合により、BrazeのセグメントをStorylyプラットフォームのオーディエンスとして使うことができる。この統合によって、あなたは次のことができる：
- 特定のストーリーを持つセグメントをターゲットにする
- ユーザー属性を使ってストーリー・コンテンツをパーソナライズする

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| ストーリーリー・アカウント | このパートナーシップを利用するには、Storylyのアカウントが必要である。 |
| ストーリーリーSDK | [Storyly SDKを](https://integration.storyly.io/)インストールする必要がある。 |
| Braze REST API キー | 以下の権限を持つBraze REST APIキー。 <br><br> `users.export.ids`<br> `users.export.segments`<br> `segments.list`<br> `segments.details`<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント | [RESTエンドポイントのURL][1]。エンドポイントは、インスタンスのBraze URLに依存する。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

BrazeとStorylyの統合により、アプリのオーナーはBrazeの全セグメントにストーリーを表示し、ユーザー属性でストーリーをパーソナライズすることができる。

一般的な使用例には以下のようなものがある：

__Storylyのターゲット・ブレイズ・セグメント__<br>統合が完了したら、Brazeセグメントに基づいてStorylyオーディエンスを作成できる。これは、人口統計学的または行動学的セグメントである可能性がある。例えば、特定の場所に住んでいるユーザー、アプリで特定のアクションを起こしたユーザー、特定のストーリーのある特定の商品に興味があるユーザーなどをターゲットにすることで、コンバージョンを高めることができる。<br>
__ユーザー属性でパーソナライズされたストーリー__<br>Brazeのユーザー属性はStorylyでも使用でき、動的なストーリーを生成することができる。これには、ユーザーの名前、バスケット内の商品、あるいはお気に入り商品などが含まれ、ユーザーにユニークなパーソナライズされたストーリーを提供することができる。パーソナライゼーションは、ストーリーのコンバージョン率とストーリー全体のエンゲージメント率を高めるのに役立つ。

## データ・エクスポートの統合

Braze Storylyの統合については、以下のビデオで説明されている：

{% multi_lang_include video.html id="3-OEqQs48Zw" source="youtube" %}

Storylyインテグレーションがカスタムパラメータを保持していることを確認する。これらのパラメータは、Braze`external id` のユーザー・プロパティと一致する。ここでは、[iOS](https://integration.storyly.io/ios/personalization-customaudience.html)、[Android](https://integration.storyly.io/android/personalization-customaudience.html)、[React Native](https://integration.storyly.io/react-native/personalization-customaudience.html)、[Flutter](https://integration.storyly.io/flutter/personalization-customaudience.html)、[Web](https://integration.storyly.io/web/personalization-customaudience.html)用のカスタム・パラメーターの実装について説明する。

詳細は[Storylyの](https://docs.storyly.io/page/connect-your-braze-audiences-with-storyly)ドキュメントを参照することもできる。

### ステップ1:Storylyダッシュボードで統合を設定する

**Storylyダッシュボード＞設定＞統合＞Brazeと接続で**統合を作成する。ここでは、Braze REST APIキーとBraze RESTエンドポイントが必要である。 

### ステップ2:セグメントを取得する 

次に、Brazeセグメントを使ってStorylyオーディエンスを作成する。これは、**Storylyダッシュボード＞設定＞オーディエンス＞新規オーディエンス＞Brazeでオーディエンスを作成で**作成できる。

ここには2つの同期オプションがある。特定のキャンペーン・ストーリーには**1回限りの同期を**、長期的なストーリーには**毎日の同期を**選択する。

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints