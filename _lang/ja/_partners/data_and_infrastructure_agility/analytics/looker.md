---
nav_title: ルッカー
article_title: ルッカー
alias: /partners/looker/
description: "この参考記事では、Brazeとビジネス・インテリジェンスおよびビッグデータ分析プラットフォームであるLookerのパートナーシップについて概説している。"
page_type: partner
search_tag: Partner

---

# [![Braze Learning course]](https://learning.braze.com/looker-integration-with-braze/)([{% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/looker-integration-with-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Looker

> ビジネスインテリジェンスとビッグデータ分析プラットフォームである[Lookerは](https://looker.com/)、リアルタイムのビジネス分析をシームレスに探索、分析、共有することを可能にする。

BrazeとLookerの統合により、BrazeユーザーはREST APIを介してファーストパーティの[Looker Blocksと](#looker-blocks) [Looker Actionsの](#looker-actions)ユーザーフラグを活用することができる。これらのフラグを立てたユーザーをセグメントに追加し、将来のBrazeキャンペーンやCanvasの[ターゲットにする](#segment-users)ことができる。BrazeでLookerを使用するには、Braze[カレントを使用して][6]Brazeデータを[データウェアハウスに][6]送信し、BrazeのLooker Blocksを使用してLookerでBrazeデータを素早くモデル化、視覚化することを推奨する。

## 前提条件

| 必要条件 | 説明 |
|---|---|
|ルッカーアカウント | このパートナーシップを利用するには、[Lookerアカウントが](https://looker.com/)必要である。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント  | RESTエンドポイントのURL。エンドポイントは、[インスタンスのBraze URLに][1]依存する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### 制限事項

- このプロセスは、ピボットされていないデータに対してのみ機能する。
- APIは一度に最大100,000行を処理する。
- 重複や非ユーザーのため、最終的なユーザーフラグのカウントは低くなる可能性がある。

## 統合

### ルッカーブロック

当社のLooker Blocksは、Brazeの顧客が[Currentsを通じて][5]提供する詳細なデータのビューに素早くアクセスするのに役立つ。Brazeのブロックは、Currentsデータ用にあらかじめ作成されたビジュアライゼーションとモデリングを提供するため、Brazeの顧客は、リテンションなどの分析パターンの実装、メッセージ配信性の評価、ユーザー行動のより詳細な調査などを簡単に行うことができる。

Looker Blocksを実装するには、GitHubコードのREADMEファイルの指示に従う。
- [メッセージ・エンゲージメント分析ブロック README][2]
- [ユーザー行動分析ブロック README][3]

どちらの統合も、[最初のBrazeとの統合][4]、およびBrazeとLooker互換の[データウェアハウスとの][7]統合が、必要なデータを取り込み、送信するように適切に設定されていることを前提としている。


{% alert important %}
Brazeは[Snowflakeを](https://www.snowflake.com/)データウェアハウスとして使用してLooker Blocksを構築した。ブロックはできるだけ多くのデータウェアハウスで動作することを目指しているが、SQL関数の中には方言によって利用可能なもの、構文、動作が異なるものがある。
{% endalert %}

{% alert warning %}
さまざまな命名規則に注意すること！カスタム名は、対応する名前をすべて変更しない限り、データの不整合を引き起こす可能性がある。ビュー名、テーブル名、モデル名をカスタマイズしている場合は、LookML 内のそれぞれの名前を、選択した名前に変更する。
{% endalert %}

#### 利用可能なブロック

| ブロック | 説明 |
|---|---|
| メッセージ・エンゲージメント分析ブロック | このブロックには、プッシュ、Eメール、アプリ内メッセージ、ウェブフック、ニュースフィード、コンバージョン、キャンバスエントリー、キャンペーンコントロールグループの登録イベントに関するデータが含まれる。<br><br>この[Looker Blockの](https://looker.com/platform/blocks/source/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)詳細については、[GitHubのコードを](https://github.com/llooker/braze_message_engagement_block)チェックしてほしい。 |
| ユーザー行動分析ブロック | このブロックには、カスタムイベント、購入、セッション、ロケーションイベント、アンインストールに関するデータが含まれる。<br><br>この[Looker Blockの](https://looker.com/platform/blocks/source/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)詳細については、[GitHubのコードを](https://github.com/llooker/braze_retention_block)チェックしてほしい。 |
{: .reset-td-br-1 .reset-td-br-2}

### ルッカーのアクション

Looker Actionsを使用すると、Looker LookからREST APIエンドポイント経由でBraze内のユーザーにフラグを立てることができる。アクションでは、ディメンジョンに`braze_id` というタグが付けられる必要がある。アクションは、フラグを立てた値をユーザーのカスタム属性（`looker_export` ）に追加する。

{% alert important %}
フラグが立つのは既存のユーザーだけだ。Brazeでデータにフラグを立てる場合、ピボット・ルックは使用できない。
{% endalert %}

#### ステップ1:ブレイズ・ルッカーのアクションをセットする

Braze REST APIキーとRESTエンドポイントを使用して、Braze Looker Actionを設定する。

![Looker Brazeの設定ページ。ここには、Braze APIキーとBraze REST APIエンドポイントのフィールドがある。][12]

#### ステップ2:Looker Developをセットアップする

Looker Develop 内で、適切なビューを選択する。dimensionsタグに`braze_id` 、変更をコミットする。
この`braze_id` タグは、どのフィールドがユニークキーであるかを決定するために使用される。

```json
dimension: external_id {
    type: string
    primary_key: yes
    sql: ${TABLE}.external_id ;;
    tags: ["braze_id"]
}
```

**必ず変更をコミットすること。Looker Actionはプロダクションの設定でのみ機能する。**

#### ステップ3:タグにユーザー属性を設定する

オプションで、`braze[]` タグを使って、属性名を括弧で囲んで設定することもできる。例えば、カスタム属性`user_segment` を送信したい場合、タグは`braze[user_segment]` となる。

以下の制限に注意：
- 属性は、**ルック内のフィールドとして含まれている**場合にのみ送信される。
- サポートされるタイプは`Strings` 、`Boolean` 、`Numbers` 、`Dates` である。
- 属性名は大文字と小文字を区別する。
- 標準[ユーザープロファイル]({{site.baseurl}}/api/endpoints/user_data/#braze-user-profile-fields)名と完全に一致する限り、標準属性も設定できる。
- 完全なタグは引用符で囲む。例えば、`tags: ["braze[first_name]"]` 。他のタグを割り当てることもできるが、無視される。
- 追加情報は[GitHubで](https://github.com/looker/actions/tree/master/src/actions/braze)見ることができる。

#### ステップ 4:ルッカーのアクションを送信する

1. `braze_id` ディメンジョンを選択したルック内で、右上の設定ギア (<i class="fas fa-cog"></i> ) をクリックし、**Send.**.. を選択する**。**
2. カスタムブレイズアクションを選択する。
3. **Unique Keyの**下に、Brazeアカウントのプライマリユーザーマッピングキー（`external_id` または`braze_id` ）を入力する。
4. エクスポートに名前をつける。指定がない場合は、`LOOKER_EXPORT` 。
5. **Advanced Options（詳細オプション）**」で、**「Results in Table（テーブル内の結果**）」または「**All Results（すべての結果）**」を選択し、「**Send（送信）**」を選択する。<br><br>![][13]<br><br>エクスポートが正しく送信されていれば、`LOOKER_EXPORT` 、アクションで入力した値がカスタム属性としてユーザーのプロファイルに表示されるはずだ。<br><br>![][14]

##### 送信APIの例

以下は発信APIコールの例で、[`/users/track/` エンドポイントに][10]送られる。

###### ヘッダー
```
Authorization: Bearer [API_KEY]
```

###### ボディ
```json
{
   "attributes" : [
      {
        "external_id" : "user_01",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      {
        "external_id" : "user_02",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      {
        "external_id" : "user_03",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      .....
   ]
}
```

### Brazeのセグメントユーザー {#segment-users}

Brazeで、これらのフラグを付けたユーザーのセグメントを作成するには、**Engagementの** **Segmentsに**移動し、セグメントに名前を付け、フィルターとして**Looker_Exportを**選択する。次に、"includes value "オプションを使い、Lookerで割り当てたカスタム属性フラグを指定する。

![Brazeセグメントビルダーで、フィルター "looker_export "を "includes_value "と "Looker "に設定する。][15]

一度保存すれば、キャンバスやキャンペーン作成時に、ユーザーをターゲティングするステップでこのセグメントを参照することができる。

## トラブルシューティング
Lookerアクションに問題がある場合、テストユーザーを\[internal groups][16] ] に追加し、以下を確認する：

* APIキーには`users.track` の権限がある。
* 正しいRESTエンドポイントは、`https://rest.iad-01.braze.com` のように入力する。
* `braze_id` タグがディメンジョン・ビューに設定される。
* クエリには、Id ディメンジョンまたは属性が列として含まれている。
* ルッカーの結果はピボットされない。
* ユニークキーは正しく選択されている。通常、`external_id` 。
* `braze_id` `braze_id` ディメンジョン内の`braze_id` は、Braze APIの`id` フィールドであることを示すために使用される。ほとんどの場合、送信時`external_id` が主キーとなる。
* `external_id` ユーザーはBrazeプラットフォームに存在する。
* `looker_export` フィールドは`Braze Platform > Settings > Manage Settings > Custom Attributes` の下に`Automatically Detect` として設定されている。
* 変更はプロダクションにコミットされる。Looker Actionは本番環境でも機能する。

[1]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/advanced_topics/how_braze_uses_currents/
[2]: https://github.com/llooker/braze_message_engagement_block/blob/master/README.md
[3]: https://github.com/llooker/braze_retention_block/blob/master/README.md
[4]: {{site.baseurl}}//user_guide/onboarding_with_braze/integration/
[5]: {{site.baseurl}}/partners/braze_currents/about/
[6]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/
[7]: https://looker.com/solutions/other-databases?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct
[8]: https://dashboard.braze.com/app_settings/developer_console/
[9]: {{site.baseurl}}/api/basics/#endpoints
[10]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[11]: {% image_buster /assets/img/user_track_api.png %}
[12]: {% image_buster /assets/img/braze-looker-action.png %}
[13]: {% image_buster /assets/img/send-looker-action.png %}
[14]: {% image_buster /assets/img/custom-attributes-looker.png %}
[15]: {% image_buster /assets/img/braze_segments.png %}
[16]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/
