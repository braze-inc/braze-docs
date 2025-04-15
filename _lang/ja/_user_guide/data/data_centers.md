---
nav_title: データセンター
article_title: データセンター
page_order: 0.1
page_type: reference
description: "この参照記事では、データセンターの場所や地域固有のデータセンターへの登録方法など、データセンターに関する情報について説明します。"
---

# データセンター

> Braze データ・センターは、ユーザーデータが処理および保管される場所に関するオプションを提供するように構築されています。これにより、データ主権、柔軟性、および管理に関連するリスクを効果的に管理できます。Braze データセンターを選択すると、当社のプラットフォームがデータ管理におけるすべてのローカル要件を満たしているか、それを超えていることを確認できます。

## CDI の仕組み

Brazeは、世界中の異なる地域にある複数のデータセンターを運営しています。これらのデータセンターは、当社のサービスの信頼性と拡張性を高めます。この地理的な分散は、データがサーバーとユーザーの間を移動するのにかかる時間であるレイテンシーを最小限に抑えるのに役立ちます。 

これは、ユーザーがアプリまたはウェブサイトとやり取りすると、そのリクエストが最も近いデータセンターに送信されるため、パフォーマンスが最適化され、ロード時間が短縮されることも意味します。最寄りのデータセンターに接続することで、ユーザーは高速のロード時間を体験できます。これは、リアルタイムのメッセージングとユーザーエンゲージメントに特に重要です。

ユーザにプッシュ通知を送信するモバイルアプリがあるとしましょう。メルボルンのユーザーが通知を受け取った場合、その通知の送信要求はオーストラリアの最も近いデータセンターにルーティングされます。モバイルアプリがプロモーションイベント中にユーザーの急増を経験した場合、Brazeには、増大する需要に対応できる複数のデータセンターを備えたスケーラブルなインフラがあります。

## データセンター一覧

利用可能なデータセンターのリストについては、次の表を参照してください。

<style>
table th:nth-child(1) {
    width: 10%;
}
table th:nth-child(2) {
    width: 33%;
}
table th:nth-child(3) {
    width: 33%;
}
table th:nth-child(4) {
    width: 24%;
}
table td {
    word-break: break-word;
}
</style>
<table>
  <thead>
    <tr>
      <th>データセンターのリージョン</th>
      <th>ダッシュボードURL</th>
      <th>REST エンドポイント</th>
      <th>SDKエンドポイント</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>オーストラリア</b></td>
      <td><code>https://dashboard.au-01.braze.com</code></td>
      <td><code>https://rest.au-01.braze.com</code></td>
      <td><code>sdk.au-01.braze.com</code></td>
    </tr>
    <tr>
      <td><b>ヨーロッパ</b></td>
      <td>
        <ul>
          <li><code>https://dashboard-01.braze.eu</code></li>
          <li><code>https://dashboard-02.braze.eu</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>https://rest.fra-01.braze.eu</code></li>
          <li><code>https://rest.fra-02.braze.eu</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>sdk.fra-01.braze.eu</code></li>
          <li><code>sdk.fra-02.braze.eu</code></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>米国</b></td>
      <td>
        <ul>
          <li><code>https://dashboard-01.braze.com</code></li>
          <li><code>https://dashboard-02.braze.com</code></li>
          <li><code>https://dashboard-03.braze.com</code></li>
          <li><code>https://dashboard-04.braze.com</code></li>
          <li><code>https://dashboard-05.braze.com</code></li>
          <li><code>https://dashboard-06.braze.com</code></li>
          <li><code>https://dashboard-07.braze.com</code></li>
          <li><code>https://dashboard-08.braze.com</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>https://rest.iad-01.braze.com</code></li>
          <li><code>https://rest.iad-02.braze.com</code></li>
          <li><code>https://rest.iad-03.braze.com</code></li>
          <li><code>https://rest.iad-04.braze.com</code></li>
          <li><code>https://rest.iad-05.braze.com</code></li>
          <li><code>https://rest.iad-06.braze.com</code></li>
          <li><code>https://rest.iad-07.braze.com</code></li>
          <li><code>https://rest.iad-08.braze.com</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>sdk.iad-01.braze.com</code></li>
          <li><code>sdk.iad-02.braze.com</code></li>
          <li><code>sdk.iad-03.braze.com</code></li>
          <li><code>sdk.iad-04.braze.com</code></li>
          <li><code>sdk.iad-05.braze.com</code></li>
          <li><code>sdk.iad-06.braze.com</code></li>
          <li><code>sdk.iad-07.braze.com</code></li>
          <li><code>sdk.iad-08.braze.com</code></li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## 地域固有のデータセンターへの登録

Braze アカウントを設定すると、リージョン固有のデータセンターにサインアップできます。ユーザーの地理的地域に基づいて最適なデータセンターの情報と推奨事項については、アカウントマネージャーにお問い合わせください。
