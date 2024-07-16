---
nav_title: Simon Data
article_title:サイモン・データ
description:「BrazeとSimon Dataの統合を利用して、リアルタイムで、コードなしで、洗練されたオーディエンスを作成し、オーケストレーションのためにBrazeに同期する。
alias: /partners/simon_data/
page_type: partner
search_tag:Partner
---

# サイモン・データ

> [サイモン・][1]データは、マーケターに親しみやすく、データチームから信頼されている顧客データプラットフォーム（CDP）である。サイモンは、データウェアハウスをマーケティングの強みに変えることで、ビジネスの成果と優れたカスタマーエクスペリエンスを実現する。

BrazeとSimon Dataの統合を使用して、オーケストレーション用の洗練されたオーディエンスを作成し、Brazeに同期させる。この統合により、Simonのキャンペーン優先順位付け、Identityマッチング機能、複雑な集計サポートなどを最大限に活用し、Brazeのキャンペーンをダウンストリームで向上させることができる。

## 前提条件

開始するには、Simon Dataアカウント内でBrazeアカウントを認証する必要がある。

| 必要条件         | 説明                                                                                                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| サイモン・データ          | Simon DataからBraze統合を利用するには、既存のSimon Dataアカウントが必要である。                                                                    |
| Braze REST API キー  | `users.track`,`campaigns.trigger.schedule.create`,`campaigns.trigger.send` の権限を持つREST APIキー。<br><br> これはダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| ダッシュボードURL | [RESTエンドポイントのURL][3]。エンドポイントはインスタンスのBraze URLに依存する。                                                                                |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

- Brazeキャンバスまたはメールのトリガー  
- セグメンテーション・プロパティの受け渡しと管理
- シンク特性とコンタクトプロパティ

{% alert note %}  
SimonとBrazeの統合を使用する場合、SimonはBrazeに各同期のデルタのみを送信し、無関係なデータのコストを回避する。詳しくは[Sync TraitsとContact Propertiesを](#sync-traits-and-contact-properties)参照のこと。
{% endalert %}

## 統合

### SimonでBrazeアカウントを認証する

Braze統合を使用するには、まずSimonでBrazeアカウントを認証する：

1. 左のナビゲーションから**Integrationsを**クリックし、Brazeまでスクロールする。
2. Braze[REST APIキーと][2] [ダッシュボードURLを][3]入力する。
3. **Save Changesを**クリックする。

接続に成功すると、ウィンドウに「**Connected**」と表示される。

![サイモンデータの統合画面][8]{: style="max-width:70%"}

### サイモンのフローやジャーニーにBrazeアクションを追加する

SimonでBrazeアカウントを認証した後、Brazeアクションを[Flowsと][4] [Journeysに][5]追加できる。

3つのアクションが用意されている：

- **サイモンのセグメンテーション属性を同期さ**せる：セグメントの詳細をBrazeの新規または既存のカスタム属性と同期させる。
- **Brazeキャンバスをトリガーする**：サイモンのセグメンテーションデータを活用したBrazeキャンバスをトリガーする。
- **Brazeキャンペーンを送る**：サイモンからBrazeキャンペーン全体を立ち上げる。

![サイモンデータで利用可能なBrazeアクションのリストをドロップダウンで表示する。][9]{: style="max-width:60%"}

一部のアクションは、特定のフロータイプまたはジャーニーでのみ利用できる。詳しくは[docs.simondata.com][6]で学習しよう。

### 特性とコンタクトプロパティを同期させる

データ消費を最小限に抑えるために、セグメンテーション内のすべての顧客のすべてのフィールドを更新するのではなく、デフォルトで同期する特定の特徴を選択することができる。

{% alert note %}
取引同期を開始するには、[サイモン・サポート・センターで](https://docs.simondata.com/docs/support-center)リクエストを送信する。次のステップに進めるようになったら、アカウントマネージャーがお知らせする。
{% endalert %}

アカウントマネージャーがContact Traitsを有効にした後：

1. Simonで、左ナビゲーションの**Admin Centerを**展開し、**Sync Contact Traitsを**選択する。
2. **Brazeを**選ぶ。コンタクト・プロパティは、データセットごとにネストされてここに表示される。
3. SimonとBrazeの統合を使用する際に同期させたいフィールドを選択する：
   1. **形質の数は**、そのデータセットで選択可能な形質の数を示す。すべてを選択することも、行を展開して個々のフィールドを選択することもできる。
   2. フィールド名がBrazeに到着したときに異なる表示にしたい場合は、**Downstream nameを**編集する。
   3. サイモンから初めてBrazeと統合する場合は、「**Backfill all contacts**」をクリックする。バックフィルは、フローやジャーニーでアクションを初めて使用する際に、すべてのデータポイントをBrazeに送信し、すべてのデータが完全に同期されていることを確認する。その後の同期では、この画面で選んだ形質だけがBrazeに送られる。これにより、必要なデータに対してのみ課金されるようになる。

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
