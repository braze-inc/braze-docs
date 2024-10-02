---
nav_title: サイモン・データ
article_title: サイモン・データ
description: "BrazeとSimon Dataの統合を利用して、洗練されたオーディエンスを作成し、オーケストレーションのためにBrazeに同期させる。"
alias: /partners/simon_data/
page_type: partner
search_tag: Partner
---

# サイモン・データ

> [サイモン・][1]データは、マーケティング担当者に親しみやすく、データチームから信頼されている顧客データプラットフォーム（CDP）である。サイモンは、データウェアハウスをマーケティングの強みに変えることで、ビジネス成果と優れた顧客体験を促進する。

BrazeとSimon Dataの統合を利用して、洗練されたオーディエンスを作成し、オーケストレーションのためにBrazeに同期させる。この統合により、Simonのキャンペーン優先順位付け、Identityマッチング機能、複雑な集計サポートなどを最大限に活用し、Brazeのキャンペーンをダウンストリームで向上させることができる。

## 前提条件

開始するには、Simon Dataアカウント内でBrazeアカウントを認証する必要がある。

| 必要条件         | 説明                                                                                                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| サイモン・データ          | Simon DataからBraze統合を利用するには、既存のSimon Dataアカウントが必要である。                                                                    |
| Braze REST API キー  | `users.track`,`campaigns.trigger.schedule.create`,`campaigns.trigger.send` のパーミッションを持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| BrazeダッシュボードURL | [RESTエンドポイントのURL][3]。エンドポイントは、インスタンスのBraze URLに依存する。                                                                                |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

- ブレイズ・キャンバスまたはEメールをトリガーする  
- セグメント・プロパティを渡し、維持する
- シンク特性とコンタクト・プロパティ

{% alert note %}  
SimonとBrazeの統合を使用する場合、Simonは各同期でBrazeにデルタのみを送信するため、無関係なデータのコストを避けることができる。詳しくは[Sync TraitsとContact Propertiesを](#sync-traits-and-contact-properties)参照のこと。
{% endalert %}

## 統合

### SimonでBrazeアカウントを認証する

Brazeとの統合を使用するには、まずSimonでBrazeアカウントを認証する：

1. 左のナビゲーションから**Integrationsを**クリックし、Brazeまでスクロールする。
2. Braze[REST APIキーと][2] [ダッシュボードのURLを][3]入力する。
3. **Save Changesを**クリックする。

接続に成功すると、ウィンドウに「**Connected**」と表示される。

![サイモンデータの統合画面][8]{: style="max-width:70%"}

### サイモンのフローやジャーニーにブレイズのアクションを追加する

SimonでBrazeアカウントを認証した後、Brazeのアクションを[Flowsと][4] [Journeysに][5]追加できる。

つのアクションが用意されている：

- **サイモンのセグメント属性を同期させる**：セグメントの詳細をBrazeの新規または既存のカスタム属性と同期させる。
- **ブレイズ・キャンバスを発動させる**：サイモンのセグメントデータを活用したBraze Canvasをトリガーする。
- **ブレイズのキャンペーンを送る**：サイモンからBrazeキャンペーン全体を立ち上げる。

![サイモンデータで利用可能なBrazeアクションのリストをドロップダウンで表示する。][9]{: style="max-width:60%"}

一部のアクションは、特定のフロータイプまたはジャーニーでのみ利用できる。詳細は以下を参照のこと。 [docs.simondata.com][6].

### 特性とコンタクトのプロパティを同期する

データ消費を最小限に抑えるために、セグメント内のすべての顧客のすべてのフィールドを更新するのではなく、デフォルトで同期する特定の特徴を選択することができる。

{% alert note %}
取引同期を開始するには、[サイモン・サポート・センターで](https://docs.simondata.com/docs/support-center)リクエストを送信する。次のステップに進めるようになったら、アカウント・マネージャーから連絡がある。
{% endalert %}

アカウント・マネージャーによってContact Traitsが有効化された後：

1. Simonで、左ナビゲーションの**Admin Centerを**展開し、**Sync Contact Traitsを**選択する。
2. **ブレイズを**選ぶ。コンタクト・プロパティはここに表示され、データセットごとにネストされている。
3. SimonとBrazeの統合を使用する際に同期させたいフィールドを選択する：
   1. **形質の数は**、そのデータセットで選択可能な形質の数を示す。すべてを選択することも、行を展開して個々のフィールドを選択することもできる。
   2. フィールド名がBrazeに到着したときに異なる表示にしたい場合は、**Downstream nameを**編集する。
   3. サイモンから初めてBrazeと統合する場合は、「**Backfill all contacts**」をクリックする。すべてのデータが完全に同期していることを確認するために、フローやジャーニーで初めてアクションを使用するときに、Brazeにすべてのデータポイントを送信する。その後の同期では、この画面で選んだ特徴だけがBrazeに送られる。これにより、必要なデータに対してのみ課金されるようになる。

![サイモン・データで同期特性を選択する。][10]




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
