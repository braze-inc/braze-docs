---
nav_title: "ユーザープロファイル属性"
article_title: Snowflakeのユーザー属性ビュー 
page_order: 10
page_type: partner
search_tag: Partner
---

# デフォルトのユーザープロファイル属性

> このページは、Snowflake のデフォルト属性ビューの参照として機能します。3 つのビューがあり、それぞれ独自のパフォーマンスを考慮した特定のユースケース用に設計されています。

{% alert important %}
ユーザープロファイル属性は現在、Snowflake Data Sharing の顧客のベータ版にあります。Snowflake Data Sharing を使用しており、このベータにアクセスしたい場合は、カスタマーサクセスマネージャまたはブレーズサポートにお問い合わせください。
{% endalert %}

## 使用可能なビュー

- `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`  
- `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` 
- `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` 

### `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`

このビューは、ユーザープロファイルのデフォルト属性の定期的なスナップショットを提供します。データは最大8時間遅れており、リアルタイムの更新を必要としないクエリで役立ちます。

#### スキーマ

| 列名     | データタイプ     |
|-----------------|---------------|
| `APP_GROUP_ID`  | バーチャ       |
| `USER_ID`       | バーチャ       |
| `TIME`          | 数値        |
| `UPDATE_SOURCE` | バーチャ       |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID`   | バーチャ       |
| `FIRST_NAME`    | バーチャ       |
| `LAST_NAME`     | バーチャ       |
| `EMAIL`         | バーチャ       |
| `GENDER`        | バーチャ       |
| `PHONE`         | バーチャ       |
| `DOB`           | バーチャ       |
| `TIME_ZONE`     | バーチャ       |
| `HOME_CITY`     | バーチャ       |
| `COUNTRY`       | バーチャ       |
| `LANGUAGE`      | バーチャ       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

#### 使用上の注意

* **8 時間の遅延** を持つユーザー属性のスナップショットを提供します。
* リアルタイムの正確さを必要としないクエリに対して適切に実行されます。
* 特に`USER_ID` 以外の属性でフィルタリングする場合は、クエリの実行が高速になります。
* **制限:**データがリアルタイムに更新されない。

### `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`

このビューでは、ユーザプロファイル属性に関するほぼリアルタイムの更新が提供され、データはブレーズで更新が行われてから最大10 分遅れます。

#### スキーマ

| 列名     | データタイプ     |
|-----------------|---------------|
| `APP_GROUP_ID`  | バーチャ       |
| `USER_ID`       | バーチャ       |
| `TIME`          | 数値        |
| `UPDATE_SOURCE` | バーチャ       |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID`   | バーチャ       |
| `FIRST_NAME`    | バーチャ       |
| `LAST_NAME`     | バーチャ       |
| `EMAIL`         | バーチャ       |
| `GENDER`        | バーチャ       |
| `PHONE`         | バーチャ       |
| `DOB`           | バーチャ       |
| `TIME_ZONE`     | バーチャ       |
| `HOME_CITY`     | バーチャ       |
| `COUNTRY`       | バーチャ       |
| `LANGUAGE`      | バーチャ       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

#### 使用上の注意

* 最小の遅延(～10 分)で最新のユーザー属性を提供します。
* 最新のデータが必要なリアルタイム分析やシナリオに役立ちます。
* **パフォーマンスに関する考慮事項:**
    * 個々のユーザに対するクエリは高速です(大規模なウェアハウスを使用して1分以内)。
    * USER_ID フィルタを使用しないクエリは、すべてのユーザーに集約する必要があるため、実行時間が大幅に長くなります。
    * 大規模なデータセット(1億 人以上のユーザーなど) のクエリには数分かかる場合があります。

### `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`

このビューには、ユーザー属性の履歴変更ログが保存され、8 時間単位で変更がキャプチャされます。

#### スキーマ

| 列名     | データタイプ     |
|-----------------|---------------|
| `APP_GROUP_ID`  | バーチャ       |
| `USER_ID`       | バーチャ       |
| `TIME`          | 数値        |
| `UPDATE_SOURCE` | バーチャ       |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_ID`   | バーチャ       |
| `FIRST_NAME`    | バーチャ       |
| `LAST_NAME`     | バーチャ       |
| `EMAIL`         | バーチャ       |
| `GENDER`        | バーチャ       |
| `PHONE`         | バーチャ       |
| `DOB`           | バーチャ       |
| `TIME_ZONE`     | バーチャ       |
| `HOME_CITY`     | バーチャ       |
| `COUNTRY`       | バーチャ       |
| `LANGUAGE`      | バーチャ       |
| `EFF_DT`        | TIMESTAMP_NTZ |
| `END_DT`        | TIMESTAMP_NTZ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

#### 使用上の注意

* ユーザー属性の履歴変更の記録を提供します。
* データは8 時間ごとにスナップショットされます。つまり、このウィンドウの複数の更新が1 つのレコードに結合されます。この期間内の個々の変更は、別途保持されません。
* `EFF_DT` `END_DT` は、ユーザの属性状態の開始と終了を示します。

## ベストプラクティス

### 推奨されるクエリの使用法

| ユースケース                                               | 推奨ビュー                                   | メモ                                                                 |
|--------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------|
| **最近の更新を必要としない一般的なクエリ** | `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`              | 高速実行、最大8 時間前までのデータあり。                          |
| **最新のユーザー属性を必要とするクエリ**       | `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` | リアルタイムに近い更新を提供しますが、大規模なデータセットでは低速になる場合があります。 |
| **属性変更の履歴追跡**           | `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`      | 属性の変更を8 時間単位で保存します。                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation}

### パフォーマンスに関する考慮事項

* 大規模なウェアハウスの大規模なデータセット(約10億 ユーザー) の場合、`USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` のクエリは10 秒未満で返されます。
* `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` に対するクエリは、1 分以内に1 人のユーザーが返すものですが、`USER_ID` フィルタリングなしでは、ほとんどスケールされません。
* `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` の1億 人以上のユーザーに対するクエリは、ユーザーごとの集計のために数分かかる場合があります。


