---
nav_title: Looker
article_title: Looker
alias: /partners/looker/
description: "この参考記事では、Brazeとビジネス・インテリジェンスおよびビッグデータ分析プラットフォームであるLookerのパートナーシップについて概説している。"
page_type: partner
search_tag: Partner

---

# [![Braze ラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/looker-integration-with-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Looker

> ビジネスインテリジェンスとビッグデータ分析のプラットフォームである [Looker](https://looker.com/) は、リアルタイムのビジネス分析の探索、分析、共有をシームレスに行えるようにしています。

Braze と Looker の統合により、Braze をご利用のお客様は REST API を介してファーストパーティの [Looker Blocks](#looker-blocks) と [Looker Actions](#looker-actions) ユーザーフラグを利用できます。これらのフラグを立てたユーザーをセグメントに追加し、将来のBrazeキャンペーンやCanvasの[ターゲットにする](#segment-users)ことができる。Braze と Looker を使用するには、[Braze Currents を使用してデータウェアハウス][6]に Braze データを送信してから、Braze の Looker Blocks を使用して Looker で Braze データをスピーディーにモデル化および視覚化することをお勧めします。

## 前提条件

| 必要条件 | 説明 |
|---|---|
|Looker アカウント | このパートナーシップを活用するには、[Looker アカウント](https://looker.com/)が必要です。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント  | REST エンドポイントのURL。エンドポイントはインスタンスの [Braze URL][1] に応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### 制限事項

- このプロセスは、ピボットされていないデータに対してのみ機能する。
- APIは一度に最大100,000行を処理する。
- ユーザーの最終的なフラグの数は、重複や非ユーザーが原因で少なくなる可能性があります。

## 統合

### Looker Blocks

Looker Blocks により、Braze のお客様は [Currents][5] で当社から提供される詳細なデータのビューに素早くアクセスできるようになります。Braze のブロックは、Currents データ用に事前に作成されている視覚化とモデリング機能を提供します。これにより、Braze のお客様は、リテンションなどの分析パターンを容易に実装し、メッセージの配信可能性を評価し、ユーザーの行動をより細かく確認することなどができるようになります。

Looker Blocksを実装するには、GitHubコードのREADMEファイルの指示に従う。
- [メッセージ・エンゲージメント分析ブロック README][2]
- [ユーザー行動分析ブロック README][3]

どちらの統合も、[初回の Braze 統合][4]と、Looker 互換の[データウェアハウス][7]と Braze の統合が、必要なデータを取り込んで送信するように適切に設定されていることを前提としています。


{% alert important %}
Brazeは[Snowflakeを](https://www.snowflake.com/)データウェアハウスとして使用してLooker Blocksを構築した。ブロックはできるだけ多くのデータウェアハウスで動作することを目指しているが、SQL関数の中には方言によって利用可能なもの、構文、動作が異なるものがある。
{% endalert %}

{% alert warning %}
さまざまな命名規則に注意すること！カスタム名は、対応する名前をすべて変更しない限り、データの不整合を引き起こす可能性がある。ビュー名、テーブル名、モデル名をカスタマイズしている場合は、LookML 内のそれぞれの名前を、選択した名前に変更する。
{% endalert %}

#### 利用可能なブロック

| ブロック | 説明 |
|---|---|
| メッセージ・エンゲージメント分析ブロック | このブロックには、プッシュ、Eメール、アプリ内メッセージ、ウェブフック、ニュースフィード、コンバージョン、キャンバスエントリー、キャンペーンコントロールグループの登録イベントに関するデータが含まれる。<br><br>この [Looker ブロック](https://looker.com/platform/blocks/source/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)の詳細については、[GitHub のコード](https://github.com/llooker/braze_message_engagement_block)をご確認ください。 |
| ユーザー行動分析ブロック | このブロックには、カスタムイベント、購入、セッション、ロケーションイベント、アンインストールに関するデータが含まれる。<br><br>この [Looker ブロック](https://looker.com/platform/blocks/source/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)の詳細については、[GitHub のコード](https://github.com/llooker/braze_retention_block)をご確認ください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Looker Actions

Looker Actions を使用すると、Looker Look から REST API エンドポイントを介して Braze 内のユーザーにフラグを設定することができます。アクションを使用するには、ディメンションに `braze_id` というタグが付けられている必要があります。アクションは、フラグを立てた値をユーザーのカスタム属性（`looker_export` ）に追加する。

{% alert important %}
フラグが立つのは既存のユーザーだけだ。Brazeでデータにフラグを立てる場合、ピボット・ルックは使用できない。
{% endalert %}

#### ステップ1:Braze Looker アクションを設定する

Braze REST API キーと REST エンドポイントを使用して、Braze Looker アクションを設定します。

![Looker Brazeの設定ページ。Braze API キーと Braze REST API エンドポイントのフィールドがある。][12]

#### ステップ2:Looker Developをセットアップする

Looker Develop 内で、適切なビューを選択する。ディメンションタグに `braze_id` を追加し、変更をコミットします。
この`braze_id` タグは、どのフィールドがユニークキーであるかを決定するために使用される。

```json
dimension: external_id {
    type: string
    primary_key: yes
    sql: ${TABLE}.external_id ;;
    tags: ["braze_id"]
}
```

**必ず変更をコミットすること。Looker アクションは本番環境の設定でのみ機能します。**

#### ステップ3:タグにユーザー属性を設定する

オプションで、`braze[]` タグを使用し、属性名を括弧で囲んで属性を設定することもできます。たとえば、カスタム属性 `user_segment` を送信する場合、タグは `braze[user_segment]` になります。

以下の制限に注意：
- 属性は、**Look 内のフィールドとして含まれている**場合にのみ送信されます。
- サポートされているタイプは`Strings`、`Boolean`、`Numbers`、`Dates` です。
- 属性名は大文字と小文字を区別する。
- 標準[ユーザープロファイル]({{site.baseurl}}/api/endpoints/user_data/#braze-user-profile-fields)名と完全に一致する限り、標準属性も設定できる。
- 完全なタグは引用符で囲む。例: `tags: ["braze[first_name]"]`。他のタグを割り当てることもできるが、無視される。
- 追加情報は [GitHub](https://github.com/looker/actions/tree/master/src/actions/braze) で確認できます。

#### ステップ4:Looker アクションを送信する

1. `braze_id` ディメンションが選択されている Look 内で、右上の設定の歯車 (<i class="fas fa-cog"></i>) をクリックし、[**Send...**] を選択します。
2. カスタム Braze アクションを選択します。
3. [**Unique Keｙ**] で Braze アカウントのプライマリユーザーマッピングキー (`external_id` または`braze_id`) を入力します。
4. エクスポートに名前をつける。指定されない場合は `LOOKER_EXPORT` が使用されます。
5. **Advanced Options（詳細オプション）**」で、**「Results in Table（テーブル内の結果**）」または「**All Results（すべての結果）**」を選択し、「**Send（送信）**」を選択する。<br><br>![][13]<br><br>エクスポートが正しく送信された場合、`LOOKER_EXPORT` は、アクションに入力された値を含むカスタム属性としてユーザーのプロファイルに表示されます。<br><br>![][14]

##### 送信 API の例

以下に、[`/users/track/` エンドポイント][10]に送信される送信 API 呼び出しの例を示します。

###### ヘッダー
```
Authorization: Bearer [API_KEY]
```

###### 本文
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

### Braze でユーザーをセグメント化する {#segment-users}

Braze で、これらのフラグが設定されたユーザーのセグメントを作成するには、[**エンゲージメント**] の下の [**セグメント**] に移動し、セグメントに名前を付け、フィルターとして [**Looker_Export**] を選択します。次に、"includes value "オプションを使い、Lookerで割り当てたカスタム属性フラグを指定する。

![Braze セグメントビルダーで、フィルター [looker_export] に [includes_value] と [Looker] が設定されている。][15]

一度保存すれば、キャンバスやキャンペーン作成時に、ユーザーをターゲティングするステップでこのセグメントを参照することができる。

## トラブルシューティング
Looker アクションに問題がある場合、テストユーザーを[内部グループ][16]に追加し、以下を確認します。

* APIキーには`users.track` の権限がある。
* 正しい REST エンドポイントが入力されている (例: `https://rest.iad-01.braze.com`)。
* ディメンションビューで `braze_id` タグが設定されている。
* クエリには、Id ディメンションまたは属性が列として含まれている。
* ルッカーの結果はピボットされない。
* ユニークキーは正しく選択されている。通常は `external_id` です。
* ディメンションの `braze_id` は API の `braze_id` とは異なる。ディメンションの `braze_id` は、Braze API の `id` フィールドであることを示すために使用されます。ほとんどの場合、送信時には `external_id` がプライマリキーとなります。
* `external_id` ユーザーはBrazeプラットフォームに存在する。
* `looker_export` フィールドは`Braze Platform > Settings > Manage Settings > Custom Attributes` の下に`Automatically Detect` として設定されている。
* 変更はプロダクションにコミットされる。Looker Actionは本番環境でも機能する。

[1]: {{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/
[2]: https://github.com/llooker/braze_message_engagement_block/blob/master/README.md
[3]: https://github.com/llooker/braze_retention_block/blob/master/README.md
[4]: {{site.baseurl}}/user_guide/onboarding_with_braze/integration/
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
