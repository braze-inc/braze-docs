---
nav_title: Simon Data
article_title: Simon Data
description: "Braze と Simon Data の統合を使用して、高度なオーディエンスを作成し、オーケストレーションのためにリアルタイムでコードを使用せずに Braze に同期します。"
alias: /partners/simon_data/
page_type: partner
search_tag: Partner
---

# Simon Data

> [Simon Data][1] は、マーケターにとって使いやすく、データチームの信頼を得ている顧客データプラットフォーム (ＣＤＰ) です。Simon は、データウェアハウスをマーケティングの強みに変えることで、ビジネスの実績を向上し、カスタマーエクスペリエンスを促進します。

Braze と Simon Data の統合を使用して、高度なオーディエンスを作成し、オーケストレーションのためにリアルタイムでコードを使用せずに Braze に同期します。この統合により、Simonのキャンペーン優先順位付け、Identityマッチング機能、複雑な集計サポートなどを最大限に活用し、Brazeのキャンペーンをダウンストリームで向上させることができる。

## 前提条件

開始するには、Simon Data アカウント内で Braze アカウントを認証する必要があります。

| 要件         | 説明                                                                                                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Simon Data          | Simon Data 内から Braze 統合を利用するには、既存の Simon Dataアカウントが必要です。                                                                    |
| Braze REST API キー  | `users.track`,`campaigns.trigger.schedule.create`,および `campaigns.trigger.send` の権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| BrazeダッシュボードURL | [RESTエンドポイントのURL][3]。お客様のエンドポイントは、お客様のインスタンスのBraze URLに依存します。                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

- Braze キャンバスまたはメールをトリガーする  
- セグメントプロパティを受け渡し、維持する
- 特性と連絡先プロパティを同期する

{% alert note %}  
SimonとBrazeの統合を使用する場合、Simonは各同期でBrazeにデルタのみを送信するため、無関係なデータのコストを避けることができる。詳しくは、「[特性とコンタクトプロパティを同期する](#sync-traits-and-contact-properties)」を参照してください。
{% endalert %}

## 統合

### SimonでBrazeアカウントを認証する

Brazeとの統合を使用するには、まずSimonでBrazeアカウントを認証する：

1. 左側のナビゲーションで [**Integrations**] をクリックし、[Braze] までスクロールします。
2. Braze の [REST API キー][2]と[ダッシュボードのURL][3] を入力します。
3. [**SAVE CHANGES**] クリックします。

接続に成功すると、ウィンドウに「**Connected**」と表示される。

![Simon Data の統合画面][8]{: style="max-width:70%"}

### Simon でフローまたはジャーニーに Braze アクションを追加する

Simon で Braze アカウントを認証したら、Braze のアクションを[フロー][4]と[ジャーニー][5]に追加できます。

3つのアクションがあります。

- **Sync Simon segment attribute**:セグメントの詳細をBrazeの新規または既存のカスタム属性と同期させる。
- **Trigger a Braze Canvas**:Simon のセグメントデータを利用する Braze キャンバスをトリガーします。
- **Send a Braze campaign**:Simon から Braze キャンペーン全体を開始します。

![Simon Data で利用可能な Braze アクションのリストを示すドロップダウン。][9]{: style="max-width:60%"}

一部のアクションは、特定のフロータイプまたはジャーニーでのみ利用できる。詳細は以下を参照のこと。 [docs.simondata.com][6].

### 特性と連絡先プロパティを同期する

データの消費を最小限に抑えるために、セグメント内のすべての顧客のすべてのフィールドを更新するのではなく、デフォルトで同期する特定の特性を選択できます。

{% alert note %}
特性の同期を開始するには、[Simon Support Center](https://docs.simondata.com/docs/support-center) でリクエストを送信します。次のステップに進めるようになったら、アカウント・マネージャーから連絡がある。
{% endalert %}

アカウントマネージャーによって連絡先特性がアクティブ化された後に、次の手順に沿って操作します。

1. Simon で、左側のナビゲーションの [**Admin Centerを**] を展開し、[**Sync Contact Traits**] を選択します。
2. [**Braze**] を選択します。連絡先プロパティはここに表示され、データセットごとにネストされます。
3. SimonとBrazeの統合を使用する際に同期させたいフィールドを選択する：
   1. [**Number of traits**] は、そのデータセットで選択可能な特性の数を示します。すべてを選択することも、行を展開して個々のフィールドを選択することもできる。
   2. フィールド名がBrazeに到着したときに異なる表示にしたい場合は、**Downstream nameを**編集する。
   3. Simon から Braze と初めて統合する場合は、[**Backfill all contacts**] をクリックします。フローまたはジャーニーで初めてアクションを使用するときに、すべてのデータが完全に同期されるようにするため、バックフィルにより Braze にすべてのデータポイントが送信されます。その後の同期では、この画面で選択した特性のみが Braze に送信されます。これにより、必要なデータに対してのみ課金されるようになります。

![Simon Dataでの同期する特性の選択。][10]




[1]: https://www.simondata.com
[2]: {{site.baseurl}}/api/basics/#creating-and-managing-rest-api-keys
[3]: {{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints
[4]: https://docs.simondata.com/docs/campaigns-flows
[5]: https://docs.simondata.com/docs/campaigns-journeys-two
[6]: https://docs.simondata.com
[7]: https://docs.simondata.com/docs/support-center

[8]: {% image_buster /assets/img/simon_data/ConnecttoBraze.png %}  
[9]: {% image_buster /assets/img/simon_data/BrazeActions.png %}  
[10]: {% image_buster /assets/img/simon_data/BrazeTraitSyncing.png %}
