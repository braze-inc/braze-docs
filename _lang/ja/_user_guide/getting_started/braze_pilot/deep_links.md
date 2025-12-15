---
nav_title: ナビゲーションのディープリンク
article_title: Braze Pilotのナビゲーション・ディープリンク
page_order: 4
page_type: reference
description: "この参考記事では、エンジニアや開発者に必要な統合ステップを簡単に説明します。"
---

# Braze Pilotのナビゲーションディープリンク

> Braze Pilotは、BrazeメッセージングからPilotアプリの特定の部分へのディープリンクをサポートしている。これにより、エンゲージメントのユースケースを作成し、ユーザーをPilotアプリケーションのさまざまな部分に誘導することができる。また、オプションのディープリンクパラメータを使って、アプリ内の特定のページのコンテンツをユーザー向けにカスタマイズすることもできる。ディープリンクについては、[アプリ内コンテンツへのディープリンクを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking)参照のこと。

## 全般的な質問

これらは、パイロットアプリのメインナビゲーションページのディープリンクである。 

| スクリーン | ディープリンク |
| --- | --- |
| プロジェクト | `braze-pilot://navigation/projects` |
| ログデータ | `braze-pilot://navigation/logdata` |
| 設定 | `braze-pilot://navigation/setup` |
| 言語を変更する | `braze-pilot://navigation/selectlanguage` |
| カメラ | `braze-pilot://navigation/camera` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ステッピントン

これらはパイロットの架空ブランドアプリ「ステッピングトン」のディープリンクである。

### ディープリンクの例

`braze-pilot://navigation/steppington/workout?title=Running&icon=HEART_DETAILS&image=https://picsum.photos/400&info=This%20workout%20is%20awesome%21&workout=5k%20Run&calories=600&length=25&workout_info_left_text=Road%20Run&workout_info_left_icon=RUNNING_HOME&workout_info_center_text=120%20BPM&workout_info_center_icon=HEART_DETAILS&workout_info_right_text=25%3A00&workout_info_right_icon=TIMER_DETAILS`

### パラメータなしのディープリンク

| スクリーン | ディープリンク |
| --- | --- |
| スプラッシュスクリーン | `braze-pilot://navigation/steppington/splash` |
| ホーム | `braze-pilot://navigation/steppington/home` |
| ステッピングトン＋のページ | `braze-pilot://navigation/steppington/plus` |
| ゴール画面 | `braze-pilot://navigation/steppington/goals` |
| 目標変更画面 | `braze-pilot://navigation/steppington/changegoals` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### パラメータ付きディープリンク

| スクリーン | ディープリンク |
| --- | --- |
| ワークアウト | `braze-pilot://navigation/steppington/workout` |
| アクティブ・ワークアウト | `braze-pilot://navigation/steppington/activeworkout` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 許容されるパラメーター

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
            <th>デフォルト（指定がない場合）</th>
            <th>タイプ</th>
            <th>例</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>title</code></td>
            <td>画面上部に表示されるタイトル。</td>
            <td>はい</td>
            <td></td>
            <td>string</td>
            <td>実行中</td>
        </tr>
        <tr>
            <td><code>icon</code></td>
            <td>どのアイコンを使うかを表す文字列。</td>
            <td>いいえ</td>
            <td><code>RUNNING_HOME</code></td>
            <td>string</td>
            <td>HEART_DETAILS</td>
        </tr>
        <tr>
            <td><code>image</code></td>
            <td>画像, 写真のURL。</td>
            <td>はい</td>
            <td></td>
            <td>string</td>
            <td><code>https://picsum.photos/400</code></td>
        </tr>
        <tr>
            <td><code>info</code></td>
            <td>ワークアウトスタートボタンの上に配置されるワークアウトに関する情報。</td>
            <td>はい</td>
            <td></td>
            <td>string</td>
            <td>This%20workout%20is%20awesome%21</td>
        </tr>
        <tr>
            <td><code>workout</code></td>
            <td>ワークアウトの名前だ。で送られた。 <code>st_completed_class</code> イベントを開催した。</td>
            <td>はい</td>
            <td></td>
            <td>数値</td>
            <td>5キロマラソン</td>
        </tr>
        <tr>
            <td><code>calories</code></td>
            <td>アクティブ・ワークアウト画面に表示するカロリー数。で送られた。 <code>st_completed_class</code> イベントを開催した。</td>
            <td>いいえ</td>
            <td>500～1,250の乱数</td>
            <td>数値</td>
            <td>600</td>
        </tr>
        <tr>
            <td><code>length</code></td>
            <td>ワークアウトの長さ。で送られた。 <code>st_completed_class</code> イベントを開催した。</td>
            <td>いいえ</td>
            <td></td>
            <td>数値</td>
            <td>25</td>
        </tr>
        <tr>
            <td><code>workout_info_left_text</code></td>
            <td>アクティブなワークアウト画面の左カードに使用されるテキスト。</td>
            <td>いいえ</td>
            <td></td>
            <td>string</td>
            <td>ロード</td>
        </tr>
        <tr>
            <td><code>workout_info_left_icon</code></td>
            <td>アクティブなワークアウト画面の左カードで使用するアイコンである。</td>
            <td>いいえ</td>
            <td></td>
            <td>string</td>
            <td>RUNNING_HOME</td>
        </tr>
        <tr>
            <td><code>workout_info_center_text</code></td>
            <td>アクティブなワークアウト画面のセンターカードで使用されるテキスト。</td>
            <td>いいえ</td>
            <td></td>
            <td>string</td>
            <td>120%20BPM</td>
        </tr>
        <tr>
            <td><code>workout_info_center_icon</code></td>
            <td>アクティブなワークアウト画面のセンターカードに使用されるアイコンである。</td>
            <td>いいえ</td>
            <td></td>
            <td>string</td>
            <td>HEART_DETAILS</td>
        </tr>
        <tr>
            <td><code>workout_info_right_text</code></td>
            <td>アクティブなワークアウト画面の右カードに使用されるテキスト。</td>
            <td>いいえ</td>
            <td></td>
            <td>string</td>
            <td>25%3A00</td>
        </tr>
        <tr>
            <td><code>workout_info_right_icon</code></td>
            <td>アクティブなワークアウト画面の右カードで使用するアイコンである。</td>
            <td>いいえ</td>
            <td></td>
            <td>string</td>
            <td>TIMER_DETAILS</td>
        </tr>
    </tbody>
</table>

##### アイコンのオプション

| アイコン | 画像 |
| --- | --- |
| `RUNNING_HOME` | ![ランニングシューズのアイコンだ。]({% image_buster /assets/img/braze_pilot/running_home_icon.png %}){:style="max-width:30%"} |
| `HEART_DETAILS` | ![ハートのアイコンだ。]({% image_buster /assets/img/braze_pilot/heart_details_icon.png %}){:style="max-width:30%"} |
| `TIMER_DETAILS` | ![ストップウォッチのアイコン。]({% image_buster /assets/img/braze_pilot/timer_details_icon.png %}){:style="max-width:30%"} |
| `YOGA_HOME` | ![ヨガのポーズをとる人のアイコン。]({% image_buster /assets/img/braze_pilot/yoga_home_icon.png %}){:style="max-width:30%"} |
| `BICYCLE_HOME` | ![自転車のアイコンだ。]({% image_buster /assets/img/braze_pilot/bicycle_home_icon.png %}){:style="max-width:30%"} |
| `DUMBBELL_HOME` | ![ダンベルのアイコンだ。]({% image_buster /assets/img/braze_pilot/dumbbell_home_icon.png %}){:style="max-width:30%"} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## PantsLabyrinth

これらはPilotの架空ブランドアプリ「PantsLabyrinth」のディープリンクである。

### ディープリンクの例

`braze-pilot://navigation/pantslabyrinth/itemdetails?name=Jeans&price=85&image=https://picsum.photos/400&description=This%20item%20is%20awesome%21&quantity=2&size=Large&colors=%230000FF,%23FF0000&color_strings=White,Blue&selected_color=1`

### パラメータなしのディープリンク

| スクリーン | ディープリンク |
| --- | --- |
| スプラッシュスクリーン | `braze-pilot://navigation/pantslabyrinth/splash` |
| ようこそ画面 | `braze-pilot://navigation/pantslabyrinth/welcome` |
| リスト画面 | `braze-pilot://navigation/pantslabyrinth/listing` |
| カートページ | `braze-pilot://navigation/pantslabyrinth/cart` |
| ウィッシュリスト | `braze-pilot://navigation/pantslabyrinth/wishlist` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### パラメータ付きディープリンク

| スクリーン | ディープリンク |
| --- | --- |
| アイテム詳細ページ | `braze-pilot://navigation/pantslabyrinth/itemdetails` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 許容されるパラメーター

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
            <th>デフォルト（指定がない場合）</th>
            <th>タイプ</th>
            <th>例</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>name</code></td>
            <td>アイテムの名前。</td>
            <td>はい</td>
            <td></td>
            <td>string</td>
            <td>ジーンズ</td>
        </tr>
        <tr>
            <td><code>price</code></td>
            <td>商品の価格。</td>
            <td>はい</td>
            <td></td>
            <td>string</td>
            <td>85</td>
        </tr>
        <tr>
            <td><code>image</code></td>
            <td>画像, 写真のURL。</td>
            <td>はい</td>
            <td></td>
            <td>string</td>
            <td><code>https://picsum.photos/400</code></td>
        </tr>
        <tr>
            <td><code>description</code></td>
            <td>商品の説明。</td>
            <td>はい</td>
            <td></td>
            <td>string</td>
            <td>This%20item%20is%20awesome%21</td>
        </tr>
        <tr>
            <td><code>quantity</code></td>
            <td>商品の数量。</td>
            <td>いいえ</td>
            <td>1</td>
            <td>数値</td>
            <td>2</td>
        </tr>
        <tr>
            <td><code>size</code></td>
            <td>アイテムのサイズを表す文字列。</td>
            <td>いいえ</td>
            <td>M</td>
            <td>string</td>
            <td>大型</td>
        </tr>
        <tr>
            <td><code>colors</code></td>
            <td>コンマで区切られた16進数の色のリスト。これらはこのアイテムで利用可能な色である。</td>
            <td>いいえ</td>
            <td>%23000000</td>
            <td>string</td>
            <td>230000FF,%23FF0000</td>
        </tr>
        <tr>
            <td><code>color_strings</code></td>
            <td>カンマで区切られた色文字列のリスト。テキストの色を表す。</td>
            <td>いいえ</td>
            <td>ブラック</td>
            <td>string</td>
            <td>青、赤</td>
        </tr>
        <tr>
            <td><code>selected_color</code></td>
            <td>ユーザーが画面に到着したときに、カラーセレクターで選択される色のセレクテッドインデックス。値が使われていない場合は、最初に選択された色が使われる。</td>
            <td>いいえ</td>
            <td>0</td>
            <td>数値</td>
            <td>1</td>
        </tr>
    </tbody>
</table>

## ムービーキャノン

これらはパイロットの架空ブランドアプリ「ステッピングトン」のディープリンクである。

### ディープリンクの例

`braze-pilot://navigation/moviecannon/moviedetails?id=1&title=Jaws&thumbnail=https://picsum.photos/400&video=0&description=This%20video%20is%20awesome%21`

### パラメータなしのディープリンク

| スクリーン | ディープリンク |
| --- | --- |
| スプラッシュスクリーン | `braze-pilot://navigation/moviecannon/splash` |
| ようこそ画面 | `braze-pilot://navigation/moviecannon/welcome` |
| 映画一覧ページ | `braze-pilot://navigation/moviecannon/moviecannon` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### パラメータ付きディープリンク

| スクリーン | ディープリンク |
| --- | --- |
| 映画詳細ページ | `braze-pilot://navigation/moviecannon/moviedetails` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 許容されるパラメーター

| パラメーター | 説明 | required | タイプ | 例 |
| --- | --- | --- | --- | --- |
| `id` | 映画のIDだ。 | はい | 数値 | 1 |
| `title` | 映画のタイトルだ。 | はい | string | ジョーズ |
| `thumbnail` | ムービーの前に表示するサムネイルのWeb URL。 | はい | string | `https://picsum.photos/400` |
| `video` | 表示する動画リストのインデックス。 | いいえ | 数値 | 0 |
| `description` | 動画の説明である。 | はい | string | `This%20video%20is%20awesome%21` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation" }
