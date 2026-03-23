---
nav_title: データ辞書
article_title: Braze Pilot用データディクショナリ
page_order: 3
page_type: reference
description: "この参考記事では、エンジニアや開発者に必要な統合ステップを簡単に説明します。"
---

# データ辞書

> Braze Pilot内の各アプリシミュレーションは、アプリ内でのユーザー行動に基づいて様々なイベントや属性を収集するよう設計されている。 

## データへのアプローチ

このアプリは、架空のブランドが代表する業界で典型的なカスタム属性とイベントを記録する。これらの属性を使えば、様々な一般的なユースケースのデモを動かすことができる。
一般的に、すべてのイベントと属性には、そのデータを担当するアプリシミュレーションに対応する短いコードが接頭辞として付く。以下に例を示します。

- Steppingtonアプリのシミュレーションで記録された全データには、 `st_`
- パンツラビリンスアプリのシミュレーションで記録された全データには、 `pl_`
- MovieCanonアプリのシミュレーションで記録された全データには、 `mc_`

## 記録されたイベントと属性のリスト

以下の表は、Braze Pilotによって記録されるイベントと属性を一覧表示している。

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
            <th>記録された時</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>mc_entered_app</code></td>
            <td>映画カノン</td>
            <td>イベント</td>
            <td></td>
            <td>ユーザーがMovieCanonアプリに入ると</td>
        </tr>
        <tr>
            <td><code>mc_watched_movie</code></td>
            <td>映画カノン</td>
            <td>イベント</td>
            <td><code>title: string</code></td>
            <td>ユーザーが動画の視聴を終えた時</td>
        </tr>
        <tr>
            <td><code>mc_viewed_movie_page</code></td>
            <td>映画カノン</td>
            <td>イベント</td>
            <td><code>title: string</code></td>
            <td>ユーザーが映画ページを見たとき</td>
        </tr>
        <tr>
            <td><code>pl_viewed_item</code></td>
            <td>PantsLabyrinth</td>
            <td>イベント</td>
            <td><code>item_name: string</code></td>
            <td>ユーザーが商品ページを見た時</td>
        </tr>
        <tr>
            <td><code>pl_entered_app</code></td>
            <td>PantsLabyrinth</td>
            <td>イベント</td>
            <td></td>
            <td>ユーザーがパンツラビリンスアプリに入ると</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_wishlist</code></td>
            <td>PantsLabyrinth</td>
            <td>イベント</td>
            <td><code>item_name: string</code></td>
            <td>ユーザーがウィッシュリストにアイテムを追加するとき</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_cart</code></td>
            <td>PantsLabyrinth</td>
            <td>イベント</td>
            <td><code>item_name: string</code></td>
            <td>ユーザーがカートに商品を追加するとき</td>
        </tr>
        <tr>
            <td><code>&lt;purchase_event&gt;</code></td>
            <td>PantsLabyrinth</td>
            <td>イベント</td>
            <td><code>name: string</code><br><code>price: number</code></td>
            <td>ユーザーが購入を完了した時</td>
        </tr>
        <tr>
            <td><code>st_entered_app</code></td>
            <td>ステッピントン</td>
            <td>イベント</td>
            <td></td>
            <td>ユーザーがステッピングトンアプリに入ると</td>
        </tr>
        <tr>
            <td><code>st_completed_class</code></td>
            <td>ステッピントン</td>
            <td>イベント</td>
            <td><code>class_type: string</code><br><code>calories_burned: number</code><br><code>workout_length: number</code></td>
            <td>ユーザーがワークアウトを終えた時</td>
        </tr>
        <tr>
            <td><code>st_viewed_premium_benefit</code></td>
            <td>ステッピントン</td>
            <td>イベント</td>
            <td><code>benefit_type: string</code></td>
            <td>ユーザーがSteppington+タブにアクセスした時（フィーチャーフラグが有効化されている場合）</td>
        </tr>
        <tr>
            <td><code>st_viewed_class</code></td>
            <td>ステッピントン</td>
            <td>イベント</td>
            <td><code>class_type: string</code></td>
            <td>ユーザーがワークアウトページにアクセスした時</td>
        </tr>
        <tr>
            <td><code>st_completed_class</code></td>
            <td>ステッピントン</td>
            <td>イベント</td>
            <td><code>class_type: string</code><br><code>calories_burned: number</code><br><code>workout_length: number</code></td>
            <td>ユーザーがワークアウトを終えた時</td>
        </tr>
        <tr>
            <td><code>st_most_recent_completed_class</code></td>
            <td>ステッピントン</td>
            <td>属性</td>
            <td><code>string</code></td>
            <td>ユーザーがワークアウトを終えた時</td>
        </tr>
        <tr>
            <td><code>st_favorited_class</code></td>
            <td>ステッピントン</td>
            <td>イベント</td>
            <td><code>class_type: string</code></td>
            <td>ユーザーがクラスをお気に入りに追加したとき</td>
        </tr>
        <tr>
            <td><code>st_unfavorited_class</code></td>
            <td>ステッピントン</td>
            <td>イベント</td>
            <td><code>class_type: string</code></td>
            <td>ユーザーがクラスのお気に入り登録を解除した時</td>
        </tr>
        <tr>
            <td><code>st_started_free_trial</code></td>
            <td>ステッピントン</td>
            <td>イベント</td>
            <td></td>
            <td>ユーザーが<strong>「無料トライアルを開始」</strong>ボタンを選択したとき</td>
        </tr>
        <tr>
            <td><code>st_set_goal</code></td>
            <td>ステッピントン</td>
            <td>イベント</td>
            <td><code>goal_name: string</code><br><code>goal: number</code><br><code>units: string</code></td>
            <td>ユーザーが<strong>「無料トライアルを開始」</strong>ボタンを選択したとき。</td>
        </tr>
    </tbody>
</table>
