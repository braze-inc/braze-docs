---
nav_title: Wyng
article_title: Wyng
description: "この参考記事では、マイクロエクスペリエンス、顧客嗜好ポータル、APIプラットフォームを通じて顧客の嗜好や属性を収集、利用、統合するために使用されるゼロパーティデータプラットフォームであるBrazeとWyngのパートナーシップについて概説している。"
alias: /partners/wyng/
page_type: partner
search_tag: Partner
---

# Wyng

> [Wyngは](https://wyng.com/)、インタラクティブなデジタルエクスペリエンス（クイズ、ユーザー設定センター、プロモーション）を構築するツールを提供し、重要な瞬間に消費者をエンゲージメントし、嗜好やその他のゼロパーティデータを収集し、リアルタイムでパーソナライズされる。

_この統合は Wyng によって管理されます。_

## 統合について

Braze と Wyng の統合により、Wyng のエクスペリエンスから取得したゼロパーティデータを利用して、Braze キャンペーンと Braze キャンバスでインタラクションをパーソナライズできます。また、Wyng ではユーザー設定センターにより、消費者がブランドと共有するデータや好み (好みのコミュニケーション方法など) をコントロールできます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Wyng アカウント | このパートナーシップを活用するには、Wyng アカウントが必要です。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:Brazeインテグレーションを接続する

Wyngで、[**Integrations**](https://wyng.com/dashboard/integrations/)に移動し、**Add**タブを選択します。次に、**Braze**にマウスを合わせ、**Connect**をクリックして統合します。

![Wyng プラットフォームの Braze パートナータイル。]({% image_buster /assets/img/wyng/2.png %}){: style="max-width:80%;"}

### ステップ2:Braze コネクターを設定する

1. 表示される設定ウィンドウで、Braze REST API キーを指定します。
![認証情報プロンプト。]({% image_buster /assets/img/wyng/4.png %}){: style="max-width:80%;"}<br><br>
2. 次にドロップダウンを使用して、Braze と共有する Wyng キャンペーンを選択します。![Braze と共有する既存の Wyng キャンペーンを選択するように求める Braze コネクター。]({% image_buster /assets/img/wyng/5.png %}){: style="max-width:80%;"}<br><br>
3. 次に、サブスクリプション、属性オブジェクトとイベントオブジェクト、およびカスタムイベントを設定する必要があります。<br><br>
- **サブスクリプションの設定(必須)**<br>
ユーザーをサブスクリプショングループに登録するには、[**Add Subscription**] をクリックし、サブスクリプショングループの名前と ID を追加します。複数のグループ名とID を追加するには、**Add Subscription** ボタンを再度クリックします。<br>![サブスクリプショングループの名前と ID の入力を促す画面。]({% image_buster /assets/img/wyng/8.png %}){: style="max-width:80%;"}<br><br>
- **User track setup**<br>
**カスタムプロパティ**を追加をクリックして、`/users/track`エンドポイントに送信する属性とイベントオブジェクトペアを追加します。これを使用して、統合のために送信された各データトランザクションのハードコーディングされた属性値を追加します。複数のプロパティーを追加するには、**カスタムプロパティ** ボタンを再度クリックします。<br>![属性のカスタムプロパティの追加を促す画面。]({% image_buster /assets/img/wyng/9.png %}){: style="max-width:80%;"}<br><br>
- **Send custom event**<br>
オプションで、**送信カスタムイベント**を有効にすることができます。有効になっている場合、イベント名と対応するアプリ ID を含める必要があります。<br>![必要に応じてカスタムイベントの送信を促す画面。]({% image_buster /assets/img/wyng/10.png %}){: style="max-width:80%;"}<br><br>
4. 最後に、ユースケースに基づいて Wyng のフィールドを Braze API のフィールドにマッピングする必要があります。[**Select a field**] を選択してマップピングするフィールドを選択し、その後、統合を**保存**します。保存すると、これらのマッピングされたフィールドは**[Integrations] > [Manage]** の下で確認できます。
![特定の Braze フィールドにマッピングできるさまざまな Wyng フィールドの例。]({% image_buster /assets/img/wyng/11.png %}){: style="max-width:80%;"}
![使用可能なシンクフィールドの一覧。]({% image_buster /assets/img/wyng/12.png %}){: style="max-width:80%;margin-top:2px"}

### ステップ3:連携のテスト

Wyng で、Wyng キャンペーンでフォームを送信するかどうかを確認します。メインの本番キャンペーンにレコードを追加したくない場合は、プレビューキャンペーンでフォームを送信することもできます。[**Integration**] ダッシュボードに、正常に完了したトランザクションが表示されます。

## この統合を使う

データコネクターが配置されると、Wyng で作成され、Braze に追加されたフィールドを、他のデータフィールドのように使用して、キャンペーンのトリガー、オーディエンスのセグメンテーション、パーソナライズされたコンテンツのフィードを行うことができます。

用途が幅広いため、具体的なご質問がある場合には、[contact@wyng.com](mailto:contact@wyng.com) または担当のアカウントマネージャーにお問い合わせください。

## トラブルシューティング

### 失敗した送信

送信に失敗した場合、Brazeにデータを送信するときに、**View Log**リンクをクリックして、失敗した送信と関連するエラーメッセージを確認します。

![アクションヘッダーの下にある「View Log」リンク。]({% image_buster /assets/img/wyng/14.png %}){: style="max-width:80%;"}

ログページには、失敗した送信、再試行回数、送信されたデータ、エラー、および送信を再プッシュするためのリンクが表示されます。

![失敗した送信が表示される例。]({% image_buster /assets/img/wyng/15.jpg %}){: style="max-width:80%;"}

**View エラー**セクションには、エラーのエラー コードとその要因に関する追加情報が表示されます。その後、Brazeを使用してエラー コードを相互参照し、原因を特定できます。

![Wyng プラットフォームに表示されるサンプルエラーログです。]({% image_buster /assets/img/wyng/16.jpg %}){: style="max-width:80%;"}

他に質問がある場合は、Wyngサポート[（support@wyng.com](mailto:contact@wyng.com) ）に問い合わせること。


