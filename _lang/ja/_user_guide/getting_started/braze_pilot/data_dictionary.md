---
nav_title: データ辞書
article_title: Braze操縦士用データディクショナリ
page_order: 3
page_type: reference
description: "この参考記事では、エンジニアや開発者に必要な統合ステップを簡単に説明します。"
---

# データ辞書

> アプリのBraze試験機では、各種の事象や属性sを、アプリのユーザー活動に基づいて収集するために、それぞれの試験機が設置されている。 

## アプリはデーターに侵入する

このアプリは、架空のブランドに代表される業界に典型的なカスタム属性や出来事を記録している。これらの属性s を使用して、さまざまな一般的なユースケースのデモをパワーアップできます。
一般的に、すべての事象および属性には、データーを担当するアプリ・シミュレーションに対応する短いコードがプレフィックスとして付けられます。以下に例を示します。

- Steppington アプリシミュレーションでログに記録されるすべてのデータには、接頭辞が付きます `st_`
- PantsLabyrinth アプリ シミュレーションによってログに記録されるすべてのデータには、プレフィックスが付きます `pl_`
- MovieCanon アプリシミュレーションでログに記録されるすべてのデータには、プレフィックスが付きます `mc_`

## ログされたイベントと属性の一覧

下表は、Braze操縦士が記録した事象と属性の一覧です。

<style>
table td {
    word-break: break-word;
}
th:nth-child(1), td:nth-child(1) {
    width: 32%;
}
th:nth-child(2), td:nth-child(2) {
    width: 15%;
}
th:nth-child(3), td:nth-child(3) {
    width: 10%;
}
th:nth-child(4), td:nth-child(4) {
    width: 20%;
}
th:nth-child(5), td:nth-child(5) {
    width: 28%;
}
</style>

<table>
    <thead>
        <tr>
            <th>名前</th>
            <th>アプリ</th>
            <th>タイプ</th>
            <th>プロパティ</th>
            <th>ログに記録されたとき</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>mc_entered_app</code></td>
            <td>ムービーキャノン</td>
            <td>イベント</td>
            <td></td>
            <td>ユーザーがムービーキャノンアプリに入るとき</td>
        </tr>
        <tr>
            <td><code>mc_watched_movie</code></td>
            <td>ムービーキャノン</td>
            <td>イベント</td>
            <td><code>title:文字列</code></td>
            <td>ユーザーが動画を見終わったら</td>
        </tr>
        <tr>
            <td><code>mc_viewed_movie_page</code></td>
            <td>ムービーキャノン</td>
            <td>イベント</td>
            <td><code>title:文字列</code></td>
            <td>ユーザーが動画を表示しているとき</td>
        </tr>
        <tr>
            <td><code>pl_viewed_item</code></td>
            <td>PantsLabyrinth</td>
            <td>イベント</td>
            <td><code>item_name: 文字列</code></td>
            <td>ユーザーがプロダクトページを表示する場合</td>
        </tr>
        <tr>
            <td><code>pl_entered_app</code></td>
            <td>PantsLabyrinth</td>
            <td>イベント</td>
            <td></td>
            <td>ユーザーがパンツラビリンスアプリに入るとき</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_wishlist</code></td>
            <td>PantsLabyrinth</td>
            <td>イベント</td>
            <td><code>item_name: 文字列</code></td>
            <td>ユーザーが希望する一覧に項目を追加したとき</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_cart</code></td>
            <td>PantsLabyrinth</td>
            <td>イベント</td>
            <td><code>item_name: 文字列</code></td>
            <td>ユーザーが台車にアイテムを追加したとき</td>
        </tr>
        <tr>
            <td><code>&lt;purchase_event></code></td>
            <td>PantsLabyrinth</td>
            <td>イベント</td>
            <td><code>name: string</code><br><code>価格:個数</code></td>
            <td>ユーザーが購入を完了したとき</td>
        </tr>
        <tr>
            <td><code>st_entered_app</code></td>
            <td>ステッピントン</td>
            <td>イベント</td>
            <td></td>
            <td>ユーザーがSteppington アプリに入ったとき</td>
        </tr>
        <tr>
            <td><code>st_completed_class</code></td>
            <td>ステッピントン</td>
            <td>イベント</td>
            <td><code>class_type: 文字列</code><br><code>calories_burned: 番号</code><br><code>workout_length: 番号</code></td>
            <td>ユーザーがワークアウトを完了したとき</td>
        </tr>
        <tr>
            <td><code>st_viewed_premium_benefit</code></td>
            <td>ステッピントン</td>
            <td>イベント</td>
            <td><code>benefit_type: 文字列</code></td>
            <td>ユーザーがSteppington+タブにアクセスしたとき(フィーチャーフラグで有効になっている場合)</td>
        </tr>
        <tr>
            <td><code>st_viewed_class</code></td>
            <td>ステッピントン</td>
            <td>イベント</td>
            <td><code>class_type: 文字列</code></td>
            <td>ユーザーがワークアウトページを表示したとき</td>
        </tr>
        <tr>
            <td><code>st_completed_class</code></td>
            <td>ステッピントン</td>
            <td>イベント</td>
            <td><code>class_type: 文字列</code><br><code>calories_burned: 番号</code><br><code>workout_length: 番号</code></td>
            <td>ユーザーがワークアウトを完了したとき</td>
        </tr>
        <tr>
            <td><code>st_most_recent_completed_class</code></td>
            <td>ステッピントン</td>
            <td>属性</td>
            <td><code>ストリング</code></td>
            <td>ユーザーがワークアウトを完了したとき</td>
        </tr>
        <tr>
            <td><code>st_favorited_class</code></td>
            <td>ステッピントン</td>
            <td>イベント</td>
            <td><code>class_type: 文字列</code></td>
            <td>ユーザーが授業を好きなとき</td>
        </tr>
        <tr>
            <td><code>st_unfavorited_class</code></td>
            <td>ステッピントン</td>
            <td>イベント</td>
            <td><code>class_type: 文字列</code></td>
            <td>ユーザーが授業にお気に入りでない場合</td>
        </tr>
        <tr>
            <td><code>st_started_free_trial</code></td>
            <td>ステッピントン</td>
            <td>イベント</td>
            <td></td>
            <td>ユーザーが<strong>無料トライアル開始</strong>ボタンを選択した場合</td>
        </tr>
        <tr>
            <td><code>st_set_goal</code></td>
            <td>ステッピントン</td>
            <td>イベント</td>
            <td><code>goal_name: 文字列</code><br><code>目標数</code><br><code>単位: string</code></td>
            <td>ユーザーが<strong>無料トライアル</strong>スタートボタンを選択した場合。</td>
        </tr>
    </tbody>
</table>
