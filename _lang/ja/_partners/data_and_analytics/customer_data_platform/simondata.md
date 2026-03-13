---
nav_title: サイモンAI
article_title: サイモンAI
description: "BrazeとSimonAIの統合を使用して、オーケストレーションのために洗練されたオーディエンスをリアルタイムでコードなしで作成し、Brazeに同期する。"
alias: /partners/simon_data/
page_type: partner
search_tag: Partner
---

# サイモンAI

> [サイモンAI][1]エージェンティック・マーケティング・プラットフォームは、マーケティングチームが真のOne to Oneパーソナライゼーションを実現できるよう支援する。これは、コンポーザブルCDPと、Snowflake AIデータクラウドで直接動作するAIエージェントを組み合わせたもので、マーケターのデータと実行チームとして機能する。

BrazeとSimonのAI統合を利用して、高度なオーディエンスを構築し、Brazeと同期させることで、リアルタイムでコード不要のオーケストレーションが可能になる。この統合により、Simon AIのパーソナライズされたセグメンテーション、顧客データの一元化、AI主導型のセグメンテーションを活用し、よりパーソナライズされたインパクトのあるBrazeキャンペーンを下流で展開することができる。

## 前提条件

開始するには、Simon AIアカウント内でBrazeアカウントを認証する必要がある。

| 必要条件         | 説明                                                                                                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| サイモンAI          | Simon AIからBrazeインテグレーションを利用するには、既存のSimon AIアカウントが必要である。                                                                    |
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

### Simon AIでBrazeアカウントを認証する

Brazeとの統合を使用するには、まずSimonでBrazeアカウントを認証する：

1. 左側のナビゲーションで [**Integrations**] をクリックし、[Braze] までスクロールします。
2. Braze の [REST API キー][2]と[ダッシュボードのURL][3] を入力します。
3. [**SAVE CHANGES**] クリックします。

接続に成功すると、ウィンドウに「**Connected**」と表示される。

![サイモンAI][8]の統合画面{: style="max-width:70%"}

### Simon AIのフローやジャーニーにBrazeアクションを追加する

Simon AIでBrazeアカウントを認証した後、Brazeアクションを[Flowsと][4] [Journeysに][5]追加できる。

3つのアクションがあります。

- **Sync Simon segment attribute**:セグメントの詳細をBrazeの新規または既存のカスタム属性と同期させる。
- **Trigger a Braze Canvas**:Simon のセグメントデータを利用する Braze キャンバスをトリガーします。
- **Send a Braze campaign**:Simon から Braze キャンペーン全体を開始します。

![サイモンAIで利用可能なBrazeアクションのリストを示すドロップダウン][9]。{: style="max-width:60%"}

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

![サイモンAIのシンク特性を選択する][10]。

[1]: https://www.simondata.com




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

