---
nav_title: Eagle Eye
article_title: Eagle Eye
description: Braze と Eagle Eye を統合する方法を学びます。
alias: /partners/eagle_eye/
page_type: partner
search_tag: Partner
---

# Eagle Eye

> [Eagle Eye](https://eagleeye.com/) は SaaS と AI テクノロジーのリーディングカンパニーで、小売、旅行、ホスピタリティの各ブランドが、リアルタイム、オムニチャネル、パーソナライズされた消費者マーケティング活動をスケールアップすることで、エンドツーエンドの顧客のロイヤルティを獲得することを可能にしている。

_この統合は Eagle Eye によって管理されます。_

## 概要

Eagle Eye Connect は、Braze と AIR 間の双方向統合で、ブランドは Braze でロイヤルティや販促データを直接有効化できます。クライアントは、AIR 内でオーディエンスに参加した消費者に対して、AIR で報酬を発行することができます。 これによりマーケターは、ポイント残高、プロモーション、報酬アクティビティなどのリアルタイムデータを使用して、カスタマーエンゲージメントをパーソナライズできます。

## ユースケース

- ポイントのしきい値または獲得報酬などのロイヤルティイベントに基づいて、Braze キャンペーンをトリガーします。
- Braze ユーザープロファイルをリアルタイムのロイヤルティデータで充実させ、よりパーソナライズされたターゲティングを可能にします。
- 報酬の償還に関連するキャンペーンの有効性を追跡およびレポートします。
- ユーザーが Braze でキャンペーンに参加すると、AIR で報酬を発行します。

## 前提条件

| 必要条件              | 説明 |
|--------------------------|-------------|
| Eagle Eye AIR アカウント    | このパートナーシップを利用するには、アクティブな Eagle Eye AIR アカウントが必要です。まずは、イーグル・アイのパートナーシップ・チーム（[partnerships@eagleeye.com](mailto:partnerships@eagleeye.com) ）にご連絡を。 |
| Braze REST API キー       | `users.track` 権限を持つ Braze REST API キー。<br><br>これは、Braze ダッシュボードの**「設定」>「API キー」**から作成できます。 |
| Braze RESTエンドポイント      | [あなたのRESTエンドポイントURL](https://www.braze.com/docs/api/basics/#endpoints)。エンドポイントはインスタンスの Braze URL に応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## アウトバウンドとインバウンド

以下の表は、Braze と Eagle Eye AIR の間でサポートされる 2 種類の統合の概要を示しています。Eagle Eye Connect は、AIR と Braze のようなパートナーシステム間のデータ交換を可能にするミドルウェアである。詳しくは、[Eagle Eye の Brazeドキュメント](https://developer.eagleeye.com/docs/braze)を参照してください。

{% tabs local %}
{% tab outbound %}
<table>
  <thead>
    <tr>
      <th>方向</th>
      <th>開始者</th>
      <th>データフロー</th>
      <th>目的</th>
      <th>例</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Eagle Eye → Braze</td>
      <td>Eagle Eye</td>
      <td>Braze API へ</td>
      <td>
        ロイヤルティデータをカスタムイベント経由でカスタム属性としてBrazeユーザープロファイルに送信。Braze では、取り込んだデータを次のように使用できます。
        <ul>
          <li>ユーザーをセグメント化し、キャンペーンをトリガーする</li>
          <li>メッセージのパーソナライズ</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>ロイヤルティポイントやステータスを　Braze に送る(<code>ee_loyalty.points.current</code>,<code>ee_loyalty.tier.tierId</code>)</li>
          <li>ユーザーがクーポンを受け取ったり、クーポンを利用した際にユーザープロファイルを更新します。</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}
{% endtab %}

{% tab inbound %}
<table>
  <thead>
    <tr>
      <th>方向</th>
      <th>開始者</th>
      <th>データフロー</th>
      <th>目的</th>
      <th>例</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Braze → Eagle Eye</td>
      <td>Braze</td>
      <td>Webhook 経由で Eagle Eye API に</td>
      <td>
        消費者が何らかのソースから Braze のオーディエンスに入ると、Braze は EE Connect への Braze Webhook をトリガーし、EE が報酬 (クーポンまたはポイント) を発行できるようにします。<br><br>
        AIR でアクションが完了すると、Braze は AIR からアウトバウンドイベントを受け取ります。
      </td>
      <td>
        <ul>
          <li>ロイヤルティプログラムに参加することで、消費者に報酬 (クーポンまたはポイント) が発行されます。</li>
          <li>報酬は、配信が遅れた消費者に発行される。</li>
          <li>誕生日の報酬</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}
{% endtab %}
{% endtabs %}

{% alert tip %}
カスタム属性やカスタムイベントとしてBrazeに送信できるカスタムデータの詳細については、[Eagle EyeのBrazeドキュメントを](https://developer.eagleeye.com/docs/braze#data-model)参照。
{% endalert %}

## 統合の概要

現在、インバウンドとアウトバウンドのコネクターは、Eagle Eye チームが直接サポートする API 経由でしか設定できませんが、AIR ダッシュボード内のセルフサービスオプションが提供される予定です。

Eagle Eye のチームと協力する際には、以下を実行します:

### ステップ 1: 設定の詳細を提供する

まず、Eagle Eye のチームに次の詳細情報を提供します。

| 提供            | 説明 |
|------------------------|-------------|
| Braze API 認証情報  | Braze REST エンドポイント、アプリ識別子、API キーを Eagle Eye 担当者と安全に共有します。 |
| 識別子マッチング    | 外部 ID やメールなど、AIR と Braze で共通するプロファイル更新用の主要ユーザー識別子を決定し、共有します。 |
| 認証キー               | インバウンドおよびアウトバウンドコネクタごとに秘密認証キーを決定して共有します。 |
| 通貨コード          | 購入金額を表示するための 3 桁の通貨コードを共有します (e.g、米ドル)。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### ステップ2: Eagle Eye Connect を設定 

Eagle Eye チームは、提供された詳細情報、固有の AIR API 認証情報、およびコネクタ用の送信イベントを使用して Eagle Eye Connect を設定します。

### ステップ 3: AIR でソーシャル行動アクションを設定する

次に、ポイントまたはクーポンを発行するための一意のアクション参照を使用して、AIR で 1 つ以上のソーシャル行動アクションを設定します。

### ステップ 4: Braze の設定

Braze で、以下を実行します。

- Braze でキャンペーンを設定して AIR で報酬を発行する  
- AIR イベントを受信したときの消費者へのコミュニケーションを設定する

### ステップ 5: 連携のテスト

AIR で API 呼び出しを行い、AIR から受け取った Braze workspace.Validate データへのイベントデータフローを観察し、属性が期待どおりに更新されていることを確認します。  

また、ユーザーをオーディエンスに追加し、AIR で報酬が発行されることを確認します。

### ステップ 6: プロダクションにローンチ

テストが成功した後は、統合を本番環境で稼働させ、Braze にデータを継続的に送信できます。AIR と Braze の本番環境でも同じ設定ステップが必要です。

Eagle Eyeカスタマーサクセスマネージャーに連絡してリソースを割り当て、EE Connectの設定を依頼する。

## サポート

統合のサポートやトラブルシューティングについては、Eagle Eye のサポートチーム ([support@eagleeye.com](mailto:support@eagleeye.com)) までお問い合わせください。
