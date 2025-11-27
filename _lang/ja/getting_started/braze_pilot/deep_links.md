---
nav_title: ナビゲーションディープリンク
article_title: Braze操縦士におけるナビゲーションディープリンク
page_order: 4
page_type: reference
description: "この参考記事では、エンジニアや開発者に必要な統合ステップを簡単に説明します。"
---

# Braze水先人における航行の深度化

> Braze操縦士は、Braze メッセージングから操縦士アプリの特定の部分へのディープリンクを支援する。これにより、エンゲージメント ユースケースs を作成し、ユーザーs をパイロットアプリライケーションのさまざまな部分に駆動することができます。オプションのディープリンクパラメータを使用して、ユーザーのアプリの特定のページの内容をカスタマイズすることもできます。ディープリンクの詳細については、[アプリ内容へのディープリンク]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking)を参照してください。

## 全般的な質問

これらは、パイロットアプリのメインナビゲーションページのディープリンクです。 

| スクリーン | ディープリンク |
| --- | --- |
| プロジェクト | `braze-pilot://navigation/projects` |
| ログデータ | `braze-pilot://navigation/logdata` |
| 設定 | `braze-pilot://navigation/setup` |
| 言語の変更 | `braze-pilot://navigation/selectlanguage` |
| カメラ | `braze-pilot://navigation/camera` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Steppington:

これらは、パイロットにおけるSteppington架空のブランドアプリの深いつながりである。

### ディープリンクの例

`braze-pilot://navigation/steppington/workout?title=Running&icon=HEART_DETAILS&image=https://picsum.photos/400&info=This%20workout%20is%20awesome%21&workout=5k%20Run&calories=600&length=25&workout_info_left_text=Road%20Run&workout_info_left_icon=RUNNING_HOME&workout_info_center_text=120%20BPM&workout_info_center_icon=HEART_DETAILS&workout_info_right_text=25%3A00&workout_info_right_icon=TIMER_DETAILS`

### パラメータなしのディープリンク

| スクリーン | ディープリンク |
| --- | --- |
| スプラッシュスクリーン | `braze-pilot://navigation/steppington/splash` |
| ホーム | `braze-pilot://navigation/steppington/home` |
| Steppington+ページ | `braze-pilot://navigation/steppington/plus` |
| 目標画面 | `braze-pilot://navigation/steppington/goals` |
| 目標変更画面 | `braze-pilot://navigation/steppington/changegoals` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### パラメーターとのディープリンク

| スクリーン | ディープリンク |
| --- | --- |
| ワークアウト | `braze-pilot://navigation/steppington/workout` |
| アクティブワークアウト | `braze-pilot://navigation/steppington/activeworkout` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 使用可能なパラメータ

<style>
table td {
    word-break: break-word;
}
th:nth-child(1), td:nth-child(1) {
    width: 22%;
}
th:nth-child(2), td:nth-child(2) {
    width: 30%;
}
th:nth-child(3), td:nth-child(3) {
    width: 8%;
}
th:nth-child(4), td:nth-child(4) {
    width: 13%;
}
th:nth-child(5), td:nth-child(5) {
    width: 10%;
}
th:nth-child(6), td:nth-child(6) {
    width: 30%;
}
</style>

<table>
    <thead>
        <tr>
            <th>パラメーター</th>
            <th>説明</th>
            <th>required</th>
            <th>デフォルト(指定しない場合)</th>
            <th>タイプ</th>
            <th>例</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>名称</code></td>
            <td>画面の上部で使用されるタイトル。</td>
            <td>はい</td>
            <td></td>
            <td>string</td>
            <td>実行中</td>
        </tr>
        <tr>
            <td>アイコン</td>
            <td>使用するアイコンを表す文字列。</td>
            <td>いいえ</td>
            <td><code>RUNNING_HOME</code></td>
            <td>string</td>
            <td>HEART_DETAILS</td>
        </tr>
        <tr>
            <td>画像</td>
            <td>アイテムの"画像のURL。</td>
            <td>はい</td>
            <td></td>
            <td>string</td>
            <td>https://<code>/200</td>
        </tr>
        <tr>
            <td><code>info</code></td>
            <td>ワークアウト開始ボタンの上に配置するワークアウトに関する情報。</td>
            <td>はい</td>
            <td></td>
            <td>string</td>
            <td>この%20 ワークアウト%20 は%20 素晴らしい%21</td>
        </tr>
        <tr>
            <td><code>ワークアウト</code></td>
            <td>ワークアウトの名前。<code>st_completed_class</code> イベントで送信されました。</td>
            <td>はい</td>
            <td></td>
            <td>数値</td>
            <td>5k%20Run</td>
        </tr>
        <tr>
            <td><code>カロリー</code></td>
            <td>アクティブなワークアウト画面に表示されるカロリーの数。<code>st_completed_class</code> イベントで送信されました。</td>
            <td>いいえ</td>
            <td>500から1250までの乱数</td>
            <td>数値</td>
            <td>4.</td>
        </tr>
        <tr>
            <td>長さ</td>
            <td>ワークアウトの長さ。<code>st_completed_class</code> イベントで送信されました。</td>
            <td>いいえ</td>
            <td></td>
            <td>数値</td>
            <td>25</td>
        </tr>
        <tr>
            <td><code>workout_info_left_text</code></td>
            <td>ワークアウト画面の左側のカードで使用する文字。</td>
            <td>いいえ</td>
            <td></td>
            <td>string</td>
            <td>Road%20Run</td>
        </tr>
        <tr>
            <td><code>workout_info_left_icon</code></td>
            <td>ワークアウト画面の左側のカードで使用するアイコン。</td>
            <td>いいえ</td>
            <td></td>
            <td>string</td>
            <td>RUNNING_HOME</td>
        </tr>
        <tr>
            <td><code>workout_info_center_text</code></td>
            <td>ワークアウトスクリーンの中央のカードで使用する文字。</td>
            <td>いいえ</td>
            <td></td>
            <td>string</td>
            <td>120%20BPM</td>
        </tr>
        <tr>
            <td><code>workout_info_center_icon</code></td>
            <td>ワークアウト画面の中央カードで使用するアイコン。</td>
            <td>いいえ</td>
            <td></td>
            <td>string</td>
            <td>HEART_DETAILS</td>
        </tr>
        <tr>
            <td><code>workout_info_right_text</code></td>
            <td>ワークアウトスクリーンの右側のカードで使用する文字。</td>
            <td>いいえ</td>
            <td></td>
            <td>string</td>
            <td>25%3A00</td>
        </tr>
        <tr>
            <td><code>workout_info_right_icon</code></td>
            <td>ワークアウト画面の右側のカードで使用するアイコン。</td>
            <td>いいえ</td>
            <td></td>
            <td>string</td>
            <td>TIMER_DETAILS</td>
        </tr>
    </tbody>
</table>

##### アイコンオプション

| アイコン | 画像 |
| --- | --- |
| `RUNNING_HOME` | ![走っている靴のアイコン。]({% image_buster /assets/img/braze_pilot/running_home_icon.png %}){:style="max-width:30%"} |
| `HEART_DETAILS` | ![ハートアイコン。]({% image_buster /assets/img/braze_pilot/heart_details_icon.png %}){:style="max-width:30%"} |
| `TIMER_DETAILS` | ![ストップウォッチアイコン。]({% image_buster /assets/img/braze_pilot/timer_details_icon.png %}){:style="max-width:30%"} |
| `YOGA_HOME` | ![ヨガポーズの人物の象徴。]({% image_buster /assets/img/braze_pilot/yoga_home_icon.png %}){:style="max-width:30%"} |
| `BICYCLE_HOME` | ![自転車のアイコン。]({% image_buster /assets/img/braze_pilot/bicycle_home_icon.png %}){:style="max-width:30%"} |
| `DUMBBELL_HOME` | ![ダンベルアイコン。]({% image_buster /assets/img/braze_pilot/dumbbell_home_icon.png %}){:style="max-width:30%"} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## PantsLabyrinth

これらは、パイロットにおけるパンツラビリンスの架空のブランドアプリの深いつながりである。

### ディープリンクの例

`braze-pilot://navigation/pantslabyrinth/itemdetails?name=Jeans&price=85&image=https://picsum.photos/400&description=This%20item%20is%20awesome%21&quantity=2&size=Large&colors=%230000FF,%23FF0000&color_strings=White,Blue&selected_color=1`

### パラメータなしのディープリンク

| スクリーン | ディープリンク |
| --- | --- |
| スプラッシュスクリーン | `braze-pilot://navigation/pantslabyrinth/splash` |
| ようこそ画面 | `braze-pilot://navigation/pantslabyrinth/welcome` |
| リスト画面 | `braze-pilot://navigation/pantslabyrinth/listing` |
| カートページ | `braze-pilot://navigation/pantslabyrinth/cart` |
| ウィッシュリストページ | `braze-pilot://navigation/pantslabyrinth/wishlist` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### パラメーターとのディープリンク

| スクリーン | ディープリンク |
| --- | --- |
| 項目詳細ページ | `braze-pilot://navigation/pantslabyrinth/itemdetails` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 使用可能なパラメータ

<style>
table td {
    word-break: break-word;
}
th:nth-child(1), td:nth-child(1) {
    width: 20%;
}
th:nth-child(2), td:nth-child(2) {
    width: 30%;
}
th:nth-child(3), td:nth-child(3) {
    width: 8%;
}
th:nth-child(4), td:nth-child(4) {
    width: 13%;
}
th:nth-child(5), td:nth-child(5) {
    width: 10%;
}
th:nth-child(6), td:nth-child(6) {
    width: 30%;
}
</style>

<table>
    <thead>
        <tr>
            <th>パラメーター</th>
            <th>説明</th>
            <th>required</th>
            <th>デフォルト(指定しない場合)</th>
            <th>タイプ</th>
            <th>例</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>名前</code></td>
            <td>アイテムの名前。</td>
            <td>はい</td>
            <td></td>
            <td>string</td>
            <td>ジーンズ</td>
        </tr>
        <tr>
            <td><code>価格</code></td>
            <td>商品の価格。</td>
            <td>はい</td>
            <td></td>
            <td>string</td>
            <td>85</td>
        </tr>
        <tr>
            <td>画像</td>
            <td>アイテムの"画像のURL。</td>
            <td>はい</td>
            <td></td>
            <td>string</td>
            <td>https://<code>/200</td>
        </tr>
        <tr>
            <td><code>記述</code></td>
            <td>項目の説明。</td>
            <td>はい</td>
            <td></td>
            <td>string</td>
            <td>この%20item%20is%20awesome%21</td>
        </tr>
        <tr>
            <td>数量</td>
            <td>アイテムの数量。</td>
            <td>いいえ</td>
            <td>1</td>
            <td>数値</td>
            <td>2</td>
        </tr>
        <tr>
            <td><code>size</code></td>
            <td>項目のサイズを表す文字列。</td>
            <td>いいえ</td>
            <td>M</td>
            <td>string</td>
            <td>大:</td>
        </tr>
        <tr>
            <td><code>色</code></td>
            <td>カンマで区切られた16 進数の色のリスト。これらは、アイテムで使用可能な色です。</td>
            <td>いいえ</td>
            <td>4.</td>
            <td>string</td>
            <td>230000%FF,%23FF0000</td>
        </tr>
        <tr>
            <td><code>color_strings</code></td>
            <td>カンマで区切られたカラー文字列のリスト。テキストの色を表します。</td>
            <td>いいえ</td>
            <td>黒</td>
            <td>string</td>
            <td>青、赤</td>
        </tr>
        <tr>
            <td><code>selected_color</code></td>
            <td>ユーザーがスクリーンに到着したときに、カラーセレクターで選択するカラーの選択された索引。値が使用されていない場合は、最初の色が選択されます。</td>
            <td>いいえ</td>
            <td>0</td>
            <td>数値</td>
            <td>1</td>
        </tr>
    </tbody>
</table>

## ムービーキャノン

これらは、パイロットにおけるSteppington架空のブランドアプリの深いつながりである。

### ディープリンクの例

`braze-pilot://navigation/moviecannon/moviedetails?id=1&title=Jaws&thumbnail=https://picsum.photos/400&video=0&description=This%20video%20is%20awesome%21`

### パラメータなしのディープリンク

| スクリーン | ディープリンク |
| --- | --- |
| スプラッシュスクリーン | `braze-pilot://navigation/moviecannon/splash` |
| ようこそ画面 | `braze-pilot://navigation/moviecannon/welcome` |
| 動画一覧画面 | `braze-pilot://navigation/moviecannon/moviecannon` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### パラメーターとのディープリンク

| スクリーン | ディープリンク |
| --- | --- |
| 動画詳細画面 | `braze-pilot://navigation/moviecannon/moviedetails` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 使用可能なパラメータ

| パラメーター | 説明 | required | タイプ | 例 |
| --- | --- | --- | --- | --- |
| `id` | ムービーのID。 | はい | 数値 | 1 |
| `title` | ムービーのタイトル。 | はい | string | ジョー |
| `thumbnail` | ムービーの前に表示されるサムネイルのWeb URL。 | はい | string | `https://picsum.photos/400` |
| `video` | 表示される動画s の一覧の索引。 | いいえ | 数値 | 0 |
| `description` | 動画の記述。 | はい | string | `This%20video%20is%20awesome%21` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation" }
