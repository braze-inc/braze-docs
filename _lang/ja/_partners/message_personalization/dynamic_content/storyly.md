---
nav_title: Storyly
article_title:ストーリーリー
description:「この参考記事では、Brazeと軽量SDKであるStorylyのパートナーシップについて概説しています。これにより、アプリ所有者はセグメントをターゲットにして、より多くのファーストパーティデータをBrazeに提供できるようになります。「
alias: /partners/storyly/
page_type: partner
search_tag:Partner

---

# ストーリーリー

> [Storylyは](https://www.storyly.io/)、アプリやWeb サイトストーリーをもたらす軽量SDKです。直感的なデザインスタジオ、洞察力に富んだ分析、シームレスな接続性を備えたStorylyは、オーディエンス体験を豊かにするための強力なツールです。 

Braze と Storyly の統合により、Braze のセグメントを Storyly プラットフォームオーディエンスとして使用できます。この統合により、次のことが可能になります。
- 特定のストーリーでセグメントをターゲットにする
- ユーザー属性を使用してストーリーの内容をパーソナライズする

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| ストーリーアカウント | このパートナーシップを利用するには Storyly アカウントが必要です。 |
| ストーリーリー SDK | [Storyly SDK](https://integration.storyly.io/) をインストールする必要があります。 |
| Braze REST API キー | 以下の権限を持つ Braze REST API キー <br><br> `users.export.ids`<br> `users.export.segments`<br> `segments.list`<br> `segments.details`<br><br> これは Braze ダッシュボードの **\[設定] > \[**API キー**]** から作成できます。 |
| Braze REST エンドポイント | [あなたの REST エンドポイント URL][1]。エンドポイントは、インスタンスの Braze URL によって異なります。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

BrazeとStorylyの統合により、アプリ所有者はBrazeのすべてのセグメントにストーリーを表示し、ユーザー属性を使用してストーリーをパーソナライズできます。

一般的な使用例としては、次のようなものがあります。

__StorylyのターゲットBraze セグメント__<br>統合が完了したら、Braze セグメントに基づいて Storyly オーディエンス作成できます。これは、人口統計または行動Segment である可能性があります。たとえば、特定の地域に住んでいるユーザー、アプリに対して特定のアクションを実行するユーザー、特定のストーリーを持つ特定の製品に関心のあるユーザーをターゲットにして、コンバージョン増やします。<br>
__ユーザー属性によるパーソナライズされたストーリー__<br>Brazeのユーザー属性はStorylyでも使用でき、ダイナミックなストーリーを生成できます。これには、ユーザーの名前、カートに入っている商品、またはお気に入りの商品を含めることができ、ユーザーに独自のパーソナライズされたストーリーを提供できます。パーソナライズは、ストーリーのコンバージョン率とストーリー全体のエンゲージメント率を高めるのに役立ちます。

## データエクスポート統合

Braze Storylyの統合については、次の動画で説明されています。

{% multi_lang_include video.html id="3-OEqQs48Zw" source="youtube" %}

Storyly インテグレーションにカスタムパラメータが含まれていることを確認してください。これらのパラメーターは Braze `external id` ユーザープロパティと一致します。ここでは、[iOS](https://integration.storyly.io/ios/personalization-customaudience.html)、[Android](https://integration.storyly.io/android/personalization-customaudience.html)、[リアクトネイティブ](https://integration.storyly.io/react-native/personalization-customaudience.html)、[Flutter](https://integration.storyly.io/flutter/personalization-customaudience.html)、[Web](https://integration.storyly.io/web/personalization-customaudience.html) 向けのカスタムパラメーターの実装について説明します。

詳細については、[Storyly](https://docs.storyly.io/page/connect-your-braze-audiences-with-storyly) のドキュメントを参照することもできます。

### ステップ1:Storyly ダッシュボードでインテグレーションを設定します

インテグレーションは、**Storyly ダッシュボード > 設定 > インテグレーション > Braze との接続で作成できます**。ここでは、Braze REST API キーと Braze REST エンドポイントが必要になります。 

### ステップ2:セグメントを取得 

次に、Braze セグメントを使用して Storyly オーディエンススを作成できます。これは **Storyly ダッシュボード > 設定 > オーディエンス > 新規オーディエンス > Braze でオーディエンスを作成で作成できます**。

ここでは、2 つの同期オプションがあります。特定のキャンペーンストーリーには \[**1回限りの同期**] を、長期的なストーリーには \[**毎日同期**] を選択します。

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints