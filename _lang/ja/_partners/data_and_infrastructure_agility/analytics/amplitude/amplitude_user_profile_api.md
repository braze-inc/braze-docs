---
nav_title: 振幅とコネクテッド・コンテンツ
article_title: 振幅とコネクテッド・コンテンツ
page_order: 0
alias: /partners/amplitude_api_endpoints/
page_type: partner
description: "AmplitudeのUser Profile APIは、Amplitudeのユーザープロファイルを提供する。これには、ユーザー・プロパティ、計算されたユーザー・プロパティ、ユーザーを含むコホートのコホートIDのリスト、および推奨事項が含まれる。"
search_tag: Partner

---

# 振幅とコネクテッド・コンテンツ

> AmplitudeのユーザープロファイルAPIは、Amplitudeのユーザープロファイルを提供する。これには、ユーザー・プロパティ、計算されたユーザー・プロパティ、ユーザーを含むコホートのコホートIDのリスト、および推奨事項が含まれる。以下は、Connected Contentで使用できる一般的なAmplitude APIエンドポイントのリストである。

## エンドポイントパラメーター

以下の表は、ユーザープロファイルAPIの呼び出しで使用できるパラメータを示したものである。

| パラメーター | 必須 | 説明 |
| --------- | -------- | ----------- |
| `user_id` | オプション | 問い合わせるユーザーID（外部データベースID）。`device_id` が設定されていない場合は必須。 |
| `device_id` | オプション | 問い合わせるデバイスID（匿名ID）。`user_id` が設定されていない場合は必須。 |
| `get_recs` | オプション<br>(デフォルトはfalse）。 | このユーザーの推薦結果を返す。 |
| `rec_id` | オプション | `get_recs` が true の場合は必須。`rec_ids` 、カンマで区切ることで複数の推薦文を取得することができる。 |
| `rec_type` | オプション | デフォルトの実験的コントロール設定を上書きし、`rec_type=model` はモデル化された推奨を返し、`rec_type=random` はランダムな推奨を返す。将来的には他の選択肢も存在するかもしれない。 |
| `get_amp_props` | オプション<br>(デフォルトはfalse）。 | このユーザーの、計算を含まないユーザー・プロパティの完全なセットを返す。 |
| `get_cohort_ids` | オプション<br>(デフォルトはfalse）。 | このユーザーが所属するコホートIDのうち、追跡するよう設定されているすべてのコホートIDのリストを返す。デフォルトでは、どのコホートのユーザーについても、コホート・メンバーシップは追跡されない。 |
| `get_computations` | オプション<br>(デフォルトはfalse）。 | このユーザーに対して有効になっているすべての計算のリストを返す。 |
| `comp_id` | オプション | このユーザーで有効になっている可能性のある計算を1つ返す。存在しない場合はヌル値を返す。`get_computations` がtrueの場合、この値を含むすべての値がフェッチされる（アーカイブまたは削除されていない限り）。|
{: .reset-td-br-1 .reset-td-br-2}

以下の表は、アンプリチュードのレスポンスで最も一般的に期待されるパラメータを網羅している。

| 応答パラメーター | 説明 |
| ------------------ | ----------- |
| `rec_id` | という推薦状が要求された。 |
| `child_rec_id` | より詳細なレコメンデーションIDは、モデルのパフォーマンスを向上させるための内部実験の一環として、アンプリチュードがバックエンドで使用する可能性がある。ほとんどの場合、これは`rec_id` と同じである。 |
| `items` | このユーザーへの推薦リスト。 |
| `is_control` | このユーザーがコントロール・グループの一員であればtrue。 |
| `recommendation_source` | この推薦文を作成するために使用されたモデルの名前 |
| `last_updated` | この推薦文が最後に生成され、同期されたときのタイムスタンプ。 |
{: .reset-td-br-1 .reset-td-br-2}

## 共通の振幅エンドポイント

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

