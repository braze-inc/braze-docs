---
nav_title: スタックアダプト
article_title: スタックアダプト
description: "この参考記事では、BrazeとStackAdaptのパートナーシップについて概説している。"
alias: /partners/stackadapt/
page_type: partner
search_tag: Partner
---

# スタックアダプト

> [StackAdaptは](https://www.stackadapt.com/)、ターゲットを絞ったパフォーマンス重視の広告を配信するためにデジタルマーケターが使用する、AIを活用したマーケティングプラットフォームのリーディングカンパニーである。

_この統合はStackAdaptによって維持されている。_

BrazeとStackAdaptの統合により、ユーザープロファイルのデータをBrazeからStackAdapt Data Hubに同期することができる。2つのプラットフォームを接続することで、顧客の統一されたビューを作成し、広告パフォーマンスを向上させるためにカスタマーファーストデータを活性化することができる。

## ユースケース

- **離脱ユーザーを再びエンゲージメントする：**Brazeのメールマーケティングリストから配信停止したユーザーを識別子し、StackAdaptのプログラマティック広告でターゲットを絞り、別のチャネルを通じて再エンゲージメントを図る。
- **マルチチャネル体験を創造する：**ユーザーの旅をメールだけに終わらせない。例えば、ユーザーがBrazeのメールキャンペーンをクリックした場合、StackAdaptを使って補完的なプログラマティック広告を表示し、メッセージを強化してさらなるアクションを促すことができる。
- **規模に応じてパーソナライズされる：**市区町村」や「言語」といったBrazeの詳細なデータポイントを活用し、関連性の高い、ローカライズされた、言語固有の広告やメールを配信する。
- **オーディエンスへの理解を深める：**プロファイル属性を同期することで、StackAdaptでよりリッチなオーディエンスセグメントを作成し、より正確なターゲティングとパーソナライズされた広告体験を可能にする。

## 前提条件

| 必要条件 | 説明         |
| ----------- | ------------------- |
| **StackAdaptアカウント**  | データハブ統合を管理するには、権限を持つアクティブなStackAdaptアカウントが必要である。 |
| **Braze REST API キー**  | 以下の権限を持つBraze REST APIキー：<br>- users.export.ids<br>- users.export.segment<br>- email.unsubscribe<br>- email.hard_bounces<br>- messages.schedule_broadcasts<br>- campaigns.list<br>- campaigns.details<br>- canvas.list<br>- canvas.details<br>- segments.list<br>- segments.details<br>- purchases.product_list<br>- events.list<br>- feed.list<br>- feed.details<br>- templates.email.info<br>- templates.email.list<br>- subscription.status.get<br>- subscription.groups.get<br><br>これはダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| **Braze RESTエンドポイント** | [あなたのRESTエンドポイントURL](https://www.braze.com/docs/api/basics/#endpoints)。エンドポイントはインスタンスの Braze URL に応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 仕組み

StackAdaptデータハブは、ユーザープロファイル属性を引き出すために、Brazeアカウントに直接接続する。これにより、StackAdapt内で直接Braze顧客データを活用し、高度なオーディエンスのセグメンテーションと活性化を行うことができる。

### データフロー

1. StackAdaptは、提供されたAPI認証情報を使用してBrazeインスタンスへのセキュアな接続を開始する。
2. StackAdaptはユーザープロファイルのデータを取得し、特にあなたが選択してマッピングしたプロパティを取得する。
3. データは正規化され、StackAdapt Data Hubに取り込まれ、セグメンテーションやキャンペーンに利用できるようになる。
4. この統合により、スケジュールされたデータ同期（例えば毎日）が可能になり、StackAdaptのオーディエンスがBrazeからの最新のプロファイルデータを常に最新の状態に保つことができる。

## フィールドが同期される

StackAdaptはBrazeの様々なプロファイルフィールドを同期することができる：

{% tabs local %}
{% tab Standard attributes %}
- メール
- 生年月日
- 名
- 姓
- 電話
- 市区町村
- 国
- 性別
- タイムゾーン
- 作成日時:
- external ID
- 言語 

{% endtab %}
{% tab Custom attributes %}
アプリやビジネスに固有のアトリビューションで、特定のビジネスニーズに基づいて定義される。

{% endtab %}
{% tab Attribution data %}
- 紐づけられる広告
- 紐づけられる広告グループ
- 紐づけられるキャンペーン
- 紐づけられるソース

{% endtab %}
{% tab Subscription status %}
- メールサブスクリプションステータス
- プッシュ通知のサブスクリプションのステータス 

マーケティングコミュニケーションに対するユーザーの同意（例えば、メールのサブスクリプションステータス）を反映するBrazeのフィールドを正確にマッピングすることは、広告活動がユーザー嗜好やプライバシー規制に準拠したものとなるために極めて重要である。

{% endtab %}
{% endtabs %}

## 統合をセットアップする

以下のステップに従い、Brazeユーザープロファイルをインポートする：

1. StackAdaptアカウントにログインする。
2. ナビゲーション・メニューで、**データ・ハブを**選択する。
3. **プロファイルのインポートを**選択し、利用可能な統合のリストから**Brazeを**選択する。
4. プロンプトが表示されたら、Braze API認証情報を入力する。
- **REST APIキー：**Brazeの**設定**＞**APIキーに**ある。セキュリティのベストプラクティスとして、StackAdapt との統合用に専用の API キーを作成することを推奨する。
- **Brazeアプリのキー：**Brazeの「**設定**」>「**APIキー**」または「**アプリの管理**」にある。
- **Braze RESTエンドポイントURL：**BrazeインスタンスのベースURL（例：```https://rest.iad-01.braze.com``` ）。
5. **Connectを**選択して認証情報を確認する。

![StackAdaptのBraze接続。]({% image_buster /assets/img/stackadapt/stackadapt_braze_connection_settings.png %})

{: start="6"}
6. 接続を選択し、StackAdaptの広告主を選択する。
7. **プロパティ・マッピングを**設定する。StackAdaptが提案するデフォルトマッピングと事前に選択されたプロパティを確認する。
8. (オプション）追加のプロパティをインポートしたい場合は、それぞれのチェックボックスをチェックして選択し、PIIを含むかどうか、およびそのデータ型を指定する。

![StackAdaptのBraze接続。]({% image_buster /assets/img/stackadapt/stackadapt_mappings.png %})

{: start="9"}
9\.プロファイルを**リストに**追加、または新規作成し、プロファイルをグループ化、セグメンテーションできる。
10\.**Activate Integration（統合を有効にする**）を選択し、最初のデータ同期を開始する。

## 考慮事項

- **カスタムイベントとプロパティをインポートする：**この機能はまだサポートされていない。
- **データ遅延：**すべてのユーザープロファイルのデータをインポートするには、最大で24時間かかる。
- **同意のマネージャー：**Brazeにおけるデータ収集の慣行がプライバシー規制に合致していること、および顧客データを広告目的で使用するために必要な同意を得ていることを確認する。StackAdaptは、ソースシステムから渡される同意ステータスに依存している。
- **属性の一貫性：**データの有効性を最大化するために、StackAdaptに同期する前に、Brazeでのアトリビューションの名前と入力方法の一貫性を維持する。
