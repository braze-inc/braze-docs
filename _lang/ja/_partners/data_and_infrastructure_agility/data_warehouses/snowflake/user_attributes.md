---
nav_title: "ユーザープロファイル属性"
article_title: Snowflake のユーザー属性ビュー 
page_order: 10
page_type: partner
search_tag: Partner
---

# デフォルトのユーザープロファイル属性

> このページは、Snowflake のデフォルト属性ビューのリファレンスとして機能します。それぞれが特定のユースケース用に設計された 3 つのビューがあり、ビューごとに固有のパフォーマンスが考慮されています。

{% alert important %}
現在、ユーザープロファイル属性は Snowflake Data Sharing の顧客にベータ版として提供されています。Snowflake Data Sharing を使用しており、このベータ版の利用をご希望の場合は、カスタマーサクセスマネージャーまたは Braze のサポートにお問い合わせください。
{% endalert %}

## 使用可能なビュー

- `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`  
- `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` 
- `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` 

### `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`

このビューは、ユーザープロファイルのデフォルト属性の定期的なスナップショットを提供します。データの遅延は最大 8 時間であり、リアルタイムの更新を必要後しないクエリに利用できます。

#### スキーマ

| 列名     | データタイプ     |
|-----------------|---------------|
| `APP_GROUP_ID`  | VARCHAR       |
| `USER_ID`       | VARCHAR       |
| `TIME`          | 数値        |
| `UPDATE_SOURCE` | VARCHAR       |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID`   | VARCHAR       |
| `FIRST_NAME`    | VARCHAR       |
| `LAST_NAME`     | VARCHAR       |
| `EMAIL`         | VARCHAR       |
| `GENDER`        | VARCHAR       |
| `PHONE`         | VARCHAR       |
| `DOB`           | VARCHAR       |
| `TIME_ZONE`     | VARCHAR       |
| `HOME_CITY`     | VARCHAR       |
| `COUNTRY`       | VARCHAR       |
| `LANGUAGE`      | VARCHAR       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

#### 使用上の注意

* **8 時間の遅延** を持つユーザー属性のスナップショットを提供します。
* リアルタイムの正確さを必要としないクエリに適しています。
* 特に `USER_ID` 以外の属性でフィルタリングする場合は、クエリの実行が高速になります。
* **制約事項:** リアルタイムのデータ更新は行われません。

### `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`

このビューでは、ユーザープロファイル属性に関するほぼリアルタイムの最新情報が提供され、データ遅延は Braze での更新後、最大で 10 分です。

#### スキーマ

| 列名     | データタイプ     |
|-----------------|---------------|
| `APP_GROUP_ID`  | VARCHAR       |
| `USER_ID`       | VARCHAR       |
| `TIME`          | 数値        |
| `UPDATE_SOURCE` | VARCHAR       |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID`   | VARCHAR       |
| `FIRST_NAME`    | VARCHAR       |
| `LAST_NAME`     | VARCHAR       |
| `EMAIL`         | VARCHAR       |
| `GENDER`        | VARCHAR       |
| `PHONE`         | VARCHAR       |
| `DOB`           | VARCHAR       |
| `TIME_ZONE`     | VARCHAR       |
| `HOME_CITY`     | VARCHAR       |
| `COUNTRY`       | VARCHAR       |
| `LANGUAGE`      | VARCHAR       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

#### 使用上の注意

* 最小の遅延 (～10 分) で最新のユーザー属性を提供します。
* 最新のデータが必要なリアルタイム分析やシナリオに適しています。
* **パフォーマンスに関する考慮事項:**
    * 個々のユーザーに対するクエリは高速です (大規模なウェアハウスを使用して 1 分以内)。
    * USER_ID フィルタを使用しないクエリは、すべてのユーザーに集約する必要があるため、実行時間が大幅に長くなります。
    * 大型のデータセット (ユーザーが 1 億人以上など) のクエリには数分かかる場合があります。

### `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`

このビューには、ユーザー属性の変更履歴ログが保存され、8 時間単位で変更がキャプチャーされます。

#### スキーマ

| 列名     | データタイプ     |
|-----------------|---------------|
| `APP_GROUP_ID`  | VARCHAR       |
| `USER_ID`       | VARCHAR       |
| `TIME`          | 数値        |
| `UPDATE_SOURCE` | VARCHAR       |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID`   | VARCHAR       |
| `FIRST_NAME`    | VARCHAR       |
| `LAST_NAME`     | VARCHAR       |
| `EMAIL`         | VARCHAR       |
| `GENDER`        | VARCHAR       |
| `PHONE`         | VARCHAR       |
| `DOB`           | VARCHAR       |
| `TIME_ZONE`     | VARCHAR       |
| `HOME_CITY`     | VARCHAR       |
| `COUNTRY`       | VARCHAR       |
| `LANGUAGE`      | VARCHAR       |
| `EFF_DT`        | TIMESTAMP_NTZ |
| `END_DT`        | TIMESTAMP_NTZ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

#### 使用上の注意

* ユーザー属性の履歴変更の記録を提供します。
* データは 8 時間ごとにスナップショットされます。つまり、このウィンドウの複数の更新が1 つのレコードに結合されます。この期間内の各変更の個別保存は行われません。
* `EFF_DT` と `END_DT` は、ユーザの属性状態の開始と終了を示します。

## ベストプラクティス

### 推奨されるクエリの使用法

| ユースケース                                               | 推奨ビュー                                   | メモ                                                                 |
|--------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------|
| 最近の更新を必要としない**一般的なクエリ** | `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`              | 高速実行、最大8 時間前までのデータを使用。                          |
| **最新のユーザー属性**を必要とするクエリ       | `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` | ほぼリアルタイムの更新を提供しますが、大規模なデータセットでは低速になる場合があります。 |
| 属性変更の**履歴追跡**           | `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`      | 属性の変更を 8 時間単位で保存します。                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation}

### パフォーマンスに関する考慮事項

* 大規模なウェアハウスの大型のデータセット (ユーザー数約 10 億) の場合、`USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` に対するクエリは 10 秒以内に返されます。
* `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` に対するクエリは、1 人のユーザーの場合は 1 分以内に返されますが、`USER_ID` フィルタリングがない場合は、スケーリング機能が低下します。
* `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` の 1 億人以上のユーザーに対するクエリは、ユーザーごとの集計があるため、数分かかる場合があります。


