---
nav_title: Amplitude とコネクテッドコンテンツ
article_title: Amplitude とコネクテッドコンテンツ
page_order: 0
alias: /partners/amplitude_api_endpoints/
page_type: partner
description: "Amplitude の User Profile API は、Amplitude ユーザープロファイルを提供します。これには、ユーザー・プロパティ、計算されたユーザー・プロパティ、ユーザーを含むコホートのコホートIDのリスト、および推奨事項が含まれる。"
search_tag: Partner

---

# Amplitude とコネクテッドコンテンツ

> AmplitudeのユーザープロファイルAPIは、Amplitudeのユーザープロファイルを提供する。これには、ユーザー・プロパティ、計算されたユーザー・プロパティ、ユーザーを含むコホートのコホートIDのリスト、および推奨事項が含まれる。コネクテッドコンテンツで使用できる一般的なAmplitude API エンドポイントのリストを以下に示します。

## エンドポイントパラメーター

以下の表は、ユーザープロファイルAPIの呼び出しで使用できるパラメータを示したものである。

| パラメーター | 必須 | 説明 |
| --------- | -------- | ----------- |
| `user_id` | オプション | 問い合わせるユーザーID（外部データベースID）。`device_id` が設定されていない場合は必須。 |
| `device_id` | オプション | 問い合わせるデバイスID（匿名ID）。`user_id` が設定されていない場合は必須。 |
| `get_recs` | オプション<br>(デフォルトは false)。 | このユーザーの推薦結果を返す。 |
| `rec_id` | オプション | 取得するレコメンデーション。`get_recs`が true の場合は必須です。複数のレコメンデーションを取得するには、`rec_ids` をカンマで区切って指定します。 |
| `rec_type` | オプション | デフォルトの実験的コントロール設定を上書きします。`rec_type=model` はモデル化されたレコメンデーションを返し、`rec_type=random` はランダムなレコメンデーションを返します。将来的にはその他のオプションが導入される可能性があります。 |
| `get_amp_props` | オプション<br>(デフォルトは false)。 | このユーザーの、計算を含まないユーザー・プロパティの完全なセットを返す。 |
| `get_cohort_ids` | オプション<br>(デフォルトは false)。 | このユーザーが所属するコホートIDのうち、追跡するよう設定されているすべてのコホートIDのリストを返す。デフォルトでは、すべてのコホートのユーザーのコホートメンバーシップが追跡されません。 |
| `get_computations` | オプション<br>(デフォルトは false)。 | このユーザーに対して有効になっているすべての計算のリストを返す。 |
| `comp_id` | オプション | このユーザーで有効になっている可能性のある計算を1つ返す。存在しない場合はヌル値を返す。`get_computations` がtrueの場合、この値を含むすべての値がフェッチされる（アーカイブまたは削除されていない限り）。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Amplitude の応答で最もよく使用される可能性があるパラメーターを次の表に示します。

| 応答パラメーター | 説明 |
| ------------------ | ----------- |
| `rec_id` | 要求されたレコメンデーション ID。 |
| `child_rec_id` | Amplitude がモデルパフォーマンス向上のための内部実験の一部としてバックエンドで使用する可能性がある、より詳細なレコメンデーション ID。ほとんどの場合、これは `rec_id` と同じです。 |
| `items` | このユーザーへの推薦リスト。 |
| `is_control` | このユーザーがコントロールグループに属している場合は true。 |
| `recommendation_source` | この推薦文を作成するために使用されたモデルの名前 |
| `last_updated` | この推薦文が最後に生成され、同期されたときのタイムスタンプ。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 一般的な Amplitude エンドポイント

### 推薦してもらう

#### エンドポイント
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_recs=true&rec_id=testRecId`
{% endraw %}
#### 回答例
```json
{
  "userData": {
    "recommendations": [
      {
        "rec_id": "testRecId",
        "child_rec_id": "testRecId",
        "items": [
          "cookie",
          "cracker",
          "chocolate milk",
          "donut",
          "croissant"
        ],
        "is_control": false,
        "recommendation_source": "model",
        "last_updated": 1608670720
      }
    ],
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": null,
    "cohort_ids": null
  }
}
```

### 複数の推薦を得る

#### エンドポイント
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_recs=true&rec_id=testRecId,testRecId2`
{% endraw %}
#### 回答例
```json
{
  "userData": {
    "recommendations": [
      {
        "rec_id": "testRecId",
        "child_rec_id": "testRecId",
        "items": [
          "cookie",
          "cracker",
          "chocolate milk",
          "donut",
          "croissant"
        ],
        "is_control": false,
        "recommendation_source": "model",
        "last_updated": 1608670720
      },
            {
        "rec_id": "testRecId2",
        "child_rec_id": "testRecId2",
        "items": [
          "bulgogi",
          "bibimbap",
          "kimchi",
          "croffles",
          "samgyeopsal"
        ],
        "is_control": false,
        "recommendation_source": "model2",
        "last_updated": 1608670658
      }
    ],
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": null,
    "cohort_ids": null
  }
}
```

### ユーザーのプロパティを取得する

#### エンドポイント
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_amp_props=true`
{% endraw %}
#### 回答例
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "library": "http/1.0",
      "first_used": "2020-01-13",
      "last_used": "2021-03-24",
      "number_property": 12,
      "boolean_property": true
    },
    "cohort_ids": null
  }
}
```

### コホートIDを取得する

#### エンドポイント
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_cohort_ids=true`
{% endraw %}
#### 回答例
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": null,
    "cohort_ids": ["cohort1", "cohort3", "cohort7"]
  }
}
```

### 単一の計算を取得する

#### エンドポイント
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&comp_id=testCompId`
{% endraw %}
#### 回答例
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "computed-prop-2": "3"
    },
    "cohort_ids": null
  }
}
```

### すべての計算を取得する

#### エンドポイント
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_computations=true`
{% endraw %}
#### 回答例
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "computed-prop-1": "5000000.0",
      "computed-prop-2": "3"
    },
    "cohort_ids": null
  }
}
```

