---
nav_title: Looker
article_title:Looker
alias: /partners/looker/
description:「この参考記事では、Brazeとビジネスインテリジェンスおよびビッグデータ分析プラットフォームであるLookerのパートナーシップについて概説しています。「
page_type: partner
search_tag:Partner

---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/looker-integration-with-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Looker

> ビジネスインテリジェンス[およびビッグデータ分析プラットフォームであるLookerを使用すると](https://looker.com/)、リアルタイムのビジネス分析をシームレスに探索、分析、共有できます。

BrazeとLookerの統合により、BrazeユーザーはREST [APIを介してファーストパーティのLLooker Blocks](#looker-blocks) [とLookerアクションのユーザーフラグ機能を活用できます](#looker-actions)。これらのフラグを付けたユーザーをセグメントに追加して、[今後のBrazeキャンペーンやキャンバスをターゲットにすることができます](#segment-users)。BrazeでLookerを使用するには、[BrazeデータをBraze電流を使用してデータウェアハウスに送信し、BrazeのLooker Blocks を使用してBrazeデータをLookerですばやくモデル化して視覚化することをお勧めします][6]。

## 前提条件

| 必要条件 | 説明 |
|---|---|
|Lookerアカウント | このパートナーシップを利用するには、[Lookerアカウントが必要です](https://looker.com/)。 |
| Braze REST API キー | `users.track`権限のあるBraze REST APIキー。<br><br> これは Braze ダッシュボードの **\[設定] > \[**API キー**]** から作成できます。 |
| Braze REST エンドポイント  | あなたの REST エンドポイント URL。エンドポイントは、[インスタンスの Braze URL][1] によって異なります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### 制限事項

- このプロセスは、ピボットされていないデータでのみ機能します。
- API は一度に最大 100,000 行を処理します。
- ユーザーフラグの最終カウントは、重複している場合や非ユーザーである場合に、これより少なくなる場合があります。

## 統合

### Looker Blocks

[Looker Blocks を使うと、Brazeのお客様はCurrentsを通じて提供する詳細なデータにすばやくアクセスできます。][5]当社のブロックでは、Currents データを事前に視覚化およびモデル化できるため、Braze のお客様はリテンションなどの分析パターンを簡単に実装したり、メッセージの配信可能性を評価したり、ユーザー行動の詳細を確認したりできます。

Looker Blocks を実装するには、GitHubコード READMEファイルの指示に従ってください。
- [メッセージエンゲージメント分析ブロック README][2]
- [ユーザー行動分析ブロック README][3]

どちらの統合も、[最初のBraze統合とLooker互換データウェアハウスとのBraze統合が][4][、必要なデータをキャプチャして送信するように適切に設定されていることを前提としています][7]。


{% alert important %}
Brazeは、[Snowflakeをデータウェアハウスとして使用してLooker](https://www.snowflake.com/) Blocks を構築しました。Blocksはできるだけ多くのデータウェアハウスで動作することを目指していますが、一部のSQL関数は方言によって可用性、構文、動作が異なる場合があります。
{% endalert %}

{% alert warning %}
さまざまな命名規則に注意してください。カスタム名は、対応する名前をすべて変更しない限り、データに不一致が生じる可能性があります。've customized any View/table or model names, rename each in the LookML to the name you'選ばれたら.
{% endalert %}

#### 使用可能なブロック

| \[ブロック] | 説明 |
|---|---|
| メッセージエンゲージメント分析ブロック | このブロックには、プッシュ、メール、アプリ内メッセージ、Webhook、ニュースフィード、コンバージョン、キャンバスエントリ、キャンペーンコントロールグループ登録イベントに関するデータが含まれます。<br><br>[このLookerブロックの詳細を確認するか](https://looker.com/platform/blocks/source/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)、[GitHubコードを確認してください](https://github.com/llooker/braze_message_engagement_block)。 |
| ユーザー行動分析ブロック | このブロックには、カスタムイベント、購入、セッション、ロケーションイベント、アンインストールに関するデータが含まれます。<br><br>[このLookerブロックの詳細を確認するか](https://looker.com/platform/blocks/source/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)、[GitHubコードを確認してください](https://github.com/llooker/braze_retention_block)。 |
{: .reset-td-br-1 .reset-td-br-2}

### Looker Actions

Looker Actions を使用すると、Looker LookからREST APIエンドポイントを介してBraze内のユーザーにフラグを立てることができます。アクションには、`braze_id`ディメンションにタグを付ける必要があります。アクションは、`looker_export`フラグ付きの値をユーザーのカスタム属性に追加します。

{% alert important %}
既存のユーザーのみにフラグが付けられます。Braze でデータにフラグを設定する場合、ピボットルックを使用することはできません。
{% endalert %}

#### ステップ1:Braze Looker のアクションをセットアップ

Braze REST API キーと REST エンドポイントを使用して Braze Looker アクションを設定します。

![Looker Brazeの設定ページここでは、Braze API キーと Braze REST API エンドポイントのフィールドを見つけることができます。][12]

#### ステップ2:Looker Developをセットアップ

Looker Develop内で、適切なビューを選択します。`braze_id`ディメンションタグに追加し、変更を確定します。
`braze_id`このタグは、どのフィールドがユニークキーであるかを判断するために使用されます。

```json
dimension: external_id {
    type: string
    primary_key: yes
    sql: ${TABLE}.external_id ;;
    tags: ["braze_id"]
}
```

**必ず変更をコミットしてください。Lookerアクションはプロダクション設定でのみ機能します。**

#### ステップ3:タグにユーザー属性を設定

オプションで、`braze[]`角括弧内に属性名を含むタグを使用して任意の属性を設定できます。たとえば、カスタム属性`user_segment`送信したい場合、タグはになります`braze[user_segment]`。

以下の制限に注意してください。
- 属性は、**ルック内のフィールドとして含まれている場合にのみ送信されます**。
- サポートされるタイプは`Strings`、、`Boolean``Numbers`、`Dates`およびです。
- 属性名は大文字と小文字が区別されます。
- 標準属性は、[標準ユーザープロファイル名と完全に一致していれば設定することもできます]({{site.baseurl}}/api/endpoints/user_data/#braze-user-profile-fields)。
- タグ全体は引用符で囲む必要があります。たとえば、`tags: ["braze[first_name]"]`。他のタグも割り当てることができますが、無視されます。
- 追加情報は [GitHub](https://github.com/looker/actions/tree/master/src/actions/braze) にあります。

#### ステップ 4:Lookerアクションを送信

1. `braze_id`ディメンションを選択したLook内で、右上の設定ギア (<i class="fas fa-cog"></i>) をクリックし、[**送信...**] を選択します。。
2. カスタムBraze アクションを選択します。
3. \[**ユニークキー**] で、Braze アカウントのプライマリユーザーマッピングキーを入力します (`external_id`または`braze_id`)。
4. エクスポートに名前を付けます。何も指定されていない場合は、`LOOKER_EXPORT`が使用されます。
5. 「**詳細オプション**」で、「**表内の結果**」または「**すべての結果**」を選択し、「**送信**」を選択します。<br><br>![][13]<br><br>エクスポートが正しく送信された場合は、`LOOKER_EXPORT`アクションで入力した値を持つカスタム属性としてユーザーのプロファイルに表示されるはずです。<br><br>![][14]

##### アウトゴーイングAPIの例

以下は、[`/users/track/`エンドポイント][10]に送信される発信 API 呼び出しの例です。

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

### Braze のセグメントユーザー {#segment-users}

Brazeで、これらのフラグ付きユーザーのセグメントを作成するには、「**エンゲージメント**」の下の「Segment」に移動し、**Segment** に名前を付け、フィルターとして「**Looker_Export**」を選択します。次に、「値を含む」オプションを使用して、Lookerで割り当てたカスタム属性フラグを指定します。

![Braze Segment ビルダーでは、フィルター「looker_export」が「includes_value」と「Looker」に設定されています。][15]

保存したら、キャンバスまたはキャンペーン作成時に「ユーザーをターゲットにする」ステップでこのSegment を参照できます。

## トラブルシューティング
Looker Actionに問題がある場合は、テストユーザーを \[内部] ][16] グループに追加して、次の点を確認してください。

* API `users.track` キーには権限があります。
* 正しい REST エンドポイント (など) `https://rest.iad-01.braze.com` が入力されています。
* `braze_id`ディメンションビューにタグが設定されます。
* クエリには、Id ディメンションまたは属性列として含まれています。
* Lookerの結果はピボットされません。
* ユニークキーは正しく選択されています。通常は`external_id`.
* `braze_id` `braze_id`のディメンションはAPIのディメンションとは異なります。`braze_id`ディメンション内は、Braze API `id` のフィールドであることを示すために使用されます。ほとんどの場合、`external_id`送信時がプライマリキーです。
* `external_id`ユーザー Braze プラットフォームに存在します。
* `looker_export``Automatically Detect`フィールドは以下に設定されています`Braze Platform > Settings > Manage Settings > Custom Attributes`。
* 変更は本番環境に反映されます。Lookerアクションはプロダクション設定で機能します。

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
