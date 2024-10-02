---
nav_title: Wyng
article_title: Wyng
description: "このレファレンス記事では、BrazeとWyngの提携、ゼロパーティデータプラットフォームの概要を説明します。これにより、マイクロエクスペリエンス、顧客プリファレンスポータル、API プラットフォームを介して、顧客のプリファレンスと属性を簡単に収集、使用、統合できます。"
alias: /partners/wyng/
page_type: partner
search_tag: Partner
---

# Wyng

> [Wyng][0]は、適切な瞬間に消費者を巻き込み、好みや他のゼロパーティデータを収集し、リアルタイムでパーソナライズする対話型デジタルエクスペリエンスs(すなわちクイズ、ユーザー設定センターs、プロモーション)を容易に構築できるようにします。

BrazeとWyngインテグレーションでは、BrazeキャンペーンとBrazeキャンバスでWyngエクスペリエンスで得たゼロパーティデータを活用して、インターアクションをパーソナライズできます。Wyngはユーザー設定センターを動かすこともできるので、消費者sは自分のブランドと共有するデータや好み(通信の好みを含む)をコントロールすることができる。

## 前提条件

| 要件 | 説明 |
| ----------- | ----------- |
| Wyng勘定 | この提携の前進タグeを考慮するには、Wyngな考慮が必要である。 |
| Braze REST API キー | `users.track` 権限を持つBraze REST API キー。<br><br> これは、**Settings** > **API Keys** のBraze ダッシュボードで作成できます。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:Brazeインテグレーションを接続する

Wyngで、[**Integrations**][1]に移動し、**Add**タブを選択します。次に、**Braze**にマウスを合わせ、**Connect**をクリックして統合します。

![Wyng プラットフォームのBrazeパートナタイル。][2]{: style="max-width:80%;"}

### ステップ2:Braze コネクターを設定する

1. s を開封する設定ウィンドウで、Braze REST API キーを指定します。
![認証情報のプロンプトの"画像。][4]{: style="max-width:80%;"}<br><br>
2. 次に、ドロップダウンを使用して、Brazeと共有するWyng キャンペーンを選択します。![Braze コネクターの"画像で、Braze と共有する既存のWyng キャンペーンを選択します。][5]{: style="max-width:80%;"}<br><br>
3. 次に、サブスクリプションs、属性およびイベントオブジェクト、およびカスタムイベントs を設定する必要があります。<br><br>
- **サブスクリプションの設定(必須)**<br>
ユーザー s をサブスクリプショングループ s にサブスクライブするには、**サブスクリプション** を追加し、サブスクリプショングループの名前とID を追加します。複数のグループ名とID を追加するには、**Add Subscription** ボタンを再度クリックします。<br>![サブスクリプショングループの名前とID の入力を求める"画像。][8]{: style="max-width:80%;"}<br><br>
- **ユーザートラックの設定**<br>
**カスタムプロパティ**を追加をクリックして、`/users/track`エンドポイントに送信する属性とイベントオブジェクトペアを追加します。これを使用して、インテグレーション用に送信されたデータトランスアクションごとにハードコードd 属性を追加します。複数のプロパティーを追加するには、**カスタムプロパティ** ボタンを再度クリックします。<br>![属性のカスタムプロパティを追加するように求める"画像。][9]{: style="max-width:80%;"}<br><br>
- **送信カスタムイベント**<br>
オプションで、**送信カスタムイベント**を有効にすることができます。有効になっている場合、イベント名と対応するアプリ ID を含める必要があります。<br>![必要に応じて、カスタムイベントs を送信するように促す"画像。][10]{: style="max-width:80%;"}<br><br>
4. 最後に、Wyng フィールドs をユースケースに基づいてBraze API フィールドs にマップする必要があります。**フィールド**を選択してマップするsを選択し、その後、**統合を保存します。保存すると、これらのm アプリ ed フィールド s は**Integrations > Manage** にあります。
![さまざまなWyng フィールドs を特定のBraze フィールドs にマップできます。][11]{: style="max-width:80%;"}
![使用可能なシンクフィールドの一覧。][12]{: style="max-width:80%;margin-top:2px"}

### ステップ3:連携のテスト

Wyng で、Wyng キャンペーンでフォームを送信するかどうかを確認します。主な本番キャンペーンにレコードを追加しない場合は、プレビュー キャンペーンで送信することもできます。**Integration** ダッシュボードに、正常なトランスアクションが表示されます。

## この統合の使用

データコネクターが配置されると、他のデータフィールドと同様に、Wyng で作成され、Braze に追加されたすべてのフィールドを使用して、s、Segment オーディエンスs、またはフィード パーソナライズされたの内容をトリガー キャンペーンできます。

アプリケーションは幅広く、具体的な質問は\[contact@wyng.com][13]または独自のアカウントマネージャーに対応できます。

## トラブルシューティング

### 送信失敗

送信に失敗した場合、Brazeにデータを送信するときに、**View Log**リンクをクリックして、失敗した送信と関連するエラーメッセージを確認します。

!["View Log"アクション s ヘッダーにあるリンク。][14]{: style="max-width:80%;"}

ログページには、失敗した送信、再試行回数、送信、エラー、および送信を再プッシュするためのリンクが表示されます。

![失敗した送信が表示される例。][15]{: style="max-width:80%;"}

**View エラー**セクションには、エラーのエラー コードとその要因に関する追加情報が表示されます。その後、Brazeを使用してエラー コードを相互参照し、原因を特定できます。

![Wyng プラットフォームに表示されるサンプルエラーログです。][16]{: style="max-width:80%;"}

ご不明な点がございましたら、Wyngサポートまでお問い合わせください(\[support@wyng.com][13])。

[0]: https://wyng.com/
[1]: https://wyng.com/dashboard/integrations/
[2]: {% image_buster /assets/img/wyng/2.png %}
[3]: {% image_buster /assets/img/wyng/3.png %}
[4]: {% image_buster /assets/img/wyng/4.png %}
[5]: {% image_buster /assets/img/wyng/5.png %}
[6]: {% image_buster /assets/img/wyng/6.png %}
[7]: {{site.baseurl}}/api/basics/
[8]: {% image_buster /assets/img/wyng/8.png %}
[9]: {% image_buster /assets/img/wyng/9.png %}
[10]: {% image_buster /assets/img/wyng/10.png %}
[11]: {% image_buster /assets/img/wyng/11.png %}
[12]: {% image_buster /assets/img/wyng/12.png %}
[13]: mailto:contact@wyng.com
[14]: {% image_buster /assets/img/wyng/14.png %}
[15]: {% image_buster /assets/img/wyng/15.jpg %}
[16]: {% image_buster /assets/img/wyng/16.jpg %}