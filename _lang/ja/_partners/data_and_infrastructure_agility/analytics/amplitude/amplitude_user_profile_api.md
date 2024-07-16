---
nav_title: Amplitude and Connected Content
article_title:振幅と接続されたコンテンツ
page_order:0
alias: /partners/amplitude_api_endpoints/
page_type: partner
description:AmplitudeのユーザープロファイルAPIはAmplitudeユーザープロファイルを提供します。これには、ユーザーのプロパティ、計算されたユーザーのプロパティ、ユーザーを含むコホートのコホートIDのリスト、および推奨事項が含まれます。
search_tag:Partner

---

# 振幅と接続されたコンテンツ

> AmplitudeのユーザープロファイルAPIはAmplitudeユーザープロファイルを提供します。これには、ユーザーのプロパティ、計算されたユーザーのプロパティ、ユーザーを含むコホートのコホートIDのリスト、および推奨事項が含まれます。以下は、Connected Contentで使用できる一般的なAmplitude APIエンドポイントのリストです。

## エンドポイントパラメータ

次の表は、ユーザープロファイルAPIへの呼び出しで使用できるパラメータを示しています。

| パラメータ | 必須 | 説明 |
| --------- | -------- | ----------- |
| `user_id` | オプショナル | クエリを実行するユーザーID（外部データベースID）、`device_id`が設定されていない限り必須です。 |
| `device_id` | オプショナル | 照会するデバイスID（匿名ID）、`user_id`が設定されていない限り必須。 |
| `get_recs` | オプショナル<br>（デフォルトはfalse） | このユーザーに推奨結果を返します。 |
| `rec_id` | オプショナル | <b><i><u>}推奨事項{</u></i></b>を取得する必要があります。`get_recs`が真である場合に必要です。複数の推奨事項は、`rec_ids`をコンマで区切ることで取得できます。 |
| `rec_type` | オプショナル | デフォルトの実験的な制御設定を上書きし、`rec_type=model`はモデル化された推奨を返し、`rec_type=random`はランダムな推奨を返します。将来的には他のオプションが存在するかもしれません。 |
| `get_amp_props` | オプショナル<br>（デフォルトはfalse） | このユーザーの計算を含まない完全なユーザー プロパティ セットを返します。 |
| `get_cohort_ids` | オプショナル<br>（デフォルトはfalse） | このユーザーが所属しているコホートIDのうち、追跡するように設定されているもののリストを返します。デフォルトでは、任意のコホートのユーザーのコホートメンバーシップは追跡されません。 |
| `get_computations` | オプショナル<br>（デフォルトはfalse） | このユーザーに対して有効になっているすべての計算のリストを返します。 |
| `comp_id` | オプショナル | このユーザーに対して有効にできる単一の計算を返します。存在しない場合はnull値を返します。`get_computations` が真である場合、すべての値が取得されます（アーカイブまたは削除されていない限り）。|
{: .reset-td-br-1 .reset-td-br-2}

Amplitudeの応答で最も一般的に見られるパラメータを以下の表に示します。

| 応答パラメータ | 説明 |
| ------------------ | ----------- |
| `rec_id` | 要求された推奨ID。 |
| `child_rec_id` | モデルのパフォーマンスを向上させるための内部実験の一環として、Amplitudeがバックエンドで使用する可能性がある、より詳細な推奨ID。ほとんどの場合、これは`rec_id`と同じになります。 |
| `items` | このユーザーへの推奨事項のリスト。 |
| `is_control` | このユーザーがコントロールグループの一員である場合はtrue。 |
| `recommendation_source` | この推奨を生成するために使用されたモデルの名前 |
| `last_updated` | この推奨事項が最後に生成および同期された時刻。 |
{: .reset-td-br-1 .reset-td-br-2}

## 一般的な振幅エンドポイント

### おすすめを取得する

#### エンドポイント
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_recs=true&rec_id=testRecId`
{% endraw %}
#### 例の応答
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

### 複数の推奨事項を取得する

#### エンドポイント
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_recs=true&rec_id=testRecId,testRecId2`
{% endraw %}
#### 例の応答
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

### ユーザーのプロパティを取得

#### エンドポイント
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_amp_props=true`
{% endraw %}
#### 例の応答
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

### コホートIDを取得

#### エンドポイント
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_cohort_ids=true`
{% endraw %}
#### 例の応答
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

### 単一の計算を取得

#### エンドポイント
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&comp_id=testCompId`
{% endraw %}
#### 例の応答
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
#### 例の応答
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

