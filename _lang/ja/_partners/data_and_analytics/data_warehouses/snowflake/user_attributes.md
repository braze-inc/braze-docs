---
nav_title: "ユーザープロファイル属性"
article_title: Snowflakeのユーザー属性ビュー 
page_order: 10
page_type: partner
search_tag: Partner
---

# ユーザープロファイル属性

> このページは、Snowflakeのデフォルトおよびカスタム属性ビューの参照として機能します。デフォルト属性には3 つのビューがあり、カスタム属性には3 つのビューがあり、それぞれ独自のパフォーマンスを考慮して特定のユースケース用に設計されています。

{% alert important %}
ユーザープロファイル属性は現在、Snowflake Data Sharing の顧客向けにベータ版が提供されています。Snowflake Data Sharing を使用しており、このベータ版にアクセスしたい場合は、カスタマーサクセスマネージャまたは Braze サポートにお問い合わせください。
{% endalert %}

# 使用可能なビュー

<table>
  <thead>
    <tr>
      <th>タイプ</th>
      <th>ビュー</th>
      <th>説明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">デフォルト属性</td>
      <td><code>USER_DEFAULT_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>ユーザープロファイルスナップショット</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>リアルタイムユーザープロファイル</td>
    </tr>
    <tr>
      <td><code>USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>変更履歴ログ</td>
    </tr>
    <tr>
      <td rowspan="3">カスタム属性</td>
      <td><code>USER_CUSTOM_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>ユーザープロファイルスナップショット</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED</code></td>
      <td>リアルタイムユーザープロファイル</td>
    </tr>
    <tr>
      <td><code>USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>変更履歴ログ</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## ユーザープロファイルスナップショット

これらのビューは、ユーザープロファイル属性の定期的なスナップショットを提供します。データは最大 12 時間遅れており、リアルタイムの更新を必要としないクエリで役立ちます。 

 - `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`
 - `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`  

### `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`

#### スキーマ

| 列名     | データタイプ     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | 数値 |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE` | VARCHAR |
| `DOB` | VARCHAR |
| `TIME_ZONE` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}


### `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`

#### スキーマ

| 列名     | データタイプ     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | 数値 |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `CUSTOM_ATTRIBUTES` | VARIANT |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}  

### ユーザープロファイルスナップショット- 使用上の注意

* **12 時間の遅延** を持つユーザー属性のスナップショットを提供します。
* リアルタイムの正確さを必要としないクエリに適しています。
* 特に `USER_ID` 以外の属性でフィルタリングする場合は、クエリの実行が高速になります。
* **制限:**データがリアルタイムに更新されません。

## リアルタイムユーザープロファイルビュー

これらのビューは、ユーザプロファイル属性に関するほぼリアルタイムの更新を提供します。データは、Braze で更新が行われてから最大 10 分遅れます。

  - `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` 
  - `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` 

### `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`
#### スキーマ

| 列名     | データタイプ     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | 数値 |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_LTZ |
| `EXTERNAL_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE` | VARCHAR |
| `DOB` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
| `TIME_ZONE` | VARCHAR |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

### `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`
#### スキーマ

| 列名     | データタイプ     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | 数値 |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `APP_ID` | VARCHAR |
| `CUSTOM_ATTRIBUTES` | OBJECT |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}


### リアルタイムユーザープロファイルビュー- 使用上の注意

* 最小の遅延( ～10 分) で最新のユーザー属性を提供します。
* 最新のデータが必要なリアルタイム分析やシナリオに適しています。
* **パフォーマンスに関する考慮事項:**
    * 個々のユーザに対するクエリは高速です (大規模なウェアハウスを使用して1分以内)。
    * USER_ID フィルターを使用しないクエリーは、全ユーザーの集計を必要とするため、実行時間が大幅に長くなる。
    * 大型のデータセット (ユーザーが 1 億人以上など) のクエリには数分かかる場合があります。

## 変更履歴ログ

これらのビューには、ユーザー属性の変更履歴ログが保存され、12 時間単位で変更がキャプチャされます。

- `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` 
- `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED` 

### `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`
#### スキーマ

| 列名     | データタイプ     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `TIME` | 数値 |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE` | VARCHAR |
| `DOB` | VARCHAR |
| `TIME_ZONE` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
| `EFF_DT` | TIMESTAMP_NTZ |
| `END_DT` | TIMESTAMP_NTZ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

### `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`
#### スキーマ

| 列名     | データタイプ     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `TIME` | 数値 |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `CUSTOM_ATTRIBUTES` | VARIANT |
| `EFF_DT` | TIMESTAMP_NTZ |
| `END_DT` | TIMESTAMP_NTZ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

### 変更履歴ログ - 使用上の注意

* ユーザー属性の変更履歴の記録を提供します。
* データは12 時間ごとにスナップショットされます。つまり、このウィンドウの複数の更新が1 つのレコードに結合されます。この期間内の個々の変更は、別途保持されません。
* `EFF_DT` および `END_DT` は、ユーザー属性状態の開始と終了を示します。

# ベストプラクティス

## 推奨されるクエリの使用法

| ユースケース                                               | 推奨ビュー                                   | メモ                                                                 |
|--------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------|
| **最近の更新を必要としない一般的なクエリ** | `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` と `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`               | 高速な実行 (最大 12 時間前までのデータを使用)                          |
| **最新のユーザー属性を必要とするクエリ**       | `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` と `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` | ほぼリアルタイムの更新を提供しますが、大規模なデータセットでは低速になる場合があります。 |
| 属性変更の**履歴の追跡**           | `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` と `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`      | 属性の変更を 12 時間単位で保存します。                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation}

## パフォーマンスに関する考慮事項

* `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` または `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED` に対するクエリは、大規模なウェアハウスの大規模なデータセット (最大10億ユーザー) の場合、10 秒以内に返されます。
* 1 人のユーザーに対する `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` または `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED ` に対するクエリは 1 分以内に返されますが、`USER_ID` フィルター処理を行わないとスケーリングが不十分です。
* ユーザーごとの集計のため、`USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` または `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` の 1 億人を超えるユーザーに対するクエリには数分かかる場合があります。


