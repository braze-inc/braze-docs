---
nav_title: VWO
article_title: VWOとBrazeの統合
description: "VWO と Braze を統合する方法について説明します。"
alias: /partners/vwo/
page_type: partner
search_tag: Partner
---

# VWO

> [VWO](https://vwo.com/) は、顧客行動データに裏打ちされたコンバージョン最適化プログラムをチームが実行できるようにすることで、ブランドが主要なビジネス指標を強化するのを支援する強力な実験プラットフォームです。VWOを使えば、顧客データの一元化、顧客行動インサイトの獲得、仮説の構築、複数プラットフォーム（サーバー、Web、モバイル）でのABテストの実行、機能の展開、カスタマーエクスペリエンスのパーソナライズ、カスタマージャーニー全体の最適化が可能になる。

VWO と Braze を統合することで、VWO の実験データを活用してターゲットセグメントを作成し、パーソナライズされたキャンペーンを提供できます。

## 前提条件

| 必要条件     | 説明 |
|-----------------|-------------|
| VWO アカウント     | 実験データにアクセスできる VWO アカウント。 |
| Braze アカウント   | Web ページに [Braze Web SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) が統合されたアクティブな Braze アカウント。また、イベントプロパティのセグメンテーションを有効にする必要がある。リクエストするには、[考慮事項](#request-event-property-segmentation)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## VWOとBrazeの統合

### ステップ 1: VWO でBraze 統合を有効にする

1. VWO アカウントにログインします。
2. VWO ダッシュボードで、**[Configurations] > [Integrations]** と移動します。ここでは、ワークスペースレベルで統合を有効にできます。これにより、統合はデフォルトで今後のすべてのテストキャンペーンに適用されます。

   ![VWO 統合設定]({% image_buster /assets/img/vwo/vwo1_settings.png %})

4. 有効にするには、Braze 統合を選択します。
5. 必要に応じて、既存のあらゆるキャンペーンに対して Braze 統合を有効にできます。そのためには、キャンペーンを選択し、**[Configuration] > [Integrations]** と移動して、Braze を有効にします。

   ![Brazeインテグレーションを有効にする]({% image_buster /assets/img/vwo/vwo2_enable_braze.png %})

6. 統合を有効にすると、VWO はキャンペーンレベルで Braze への実験データの送信を開始します。

### ステップ2: VWO イベントプロパティを使用して、Braze でセグメントを作成する

1. Braze ダッシュボードで [**セグメント**] > [**セグメントを作成**] を選択します。
3. [**セグメントを作成**] ウィンドウで、セグメントの名前を入力し、**セグメントを作成**します。
4. 新しく作成したセグメントで、[**フィルター**] ＞ [**フィルターの追加**] を選択し、フィルターの種類として [**カスタムイベント**] を選します。
6. フィルターのドロップダウンで、**VWO** を検索します。
7. 関連する VWO プロパティを選択し、必要な値を指定します。
8. 必要であれば、訪問回数と時間枠を設定します。完了したら、[**保存**] を選択します。

   ![Braze区分の作成]({% image_buster /assets/img/vwo/vwo3_braze_segment.png %})

9. セグメント条件に一致するユーザー数を表示するには、[**正確な統計を計算する**] を選択します。

   ![Braze区分統計]({% image_buster /assets/img/vwo/vwo4_braze_segment_calculate_size.png %})

## データフロー

VWO は、キャンペーン実験データを、以下のフォーマットでカスタムイベントとして Braze に送信します。

- **イベント名:**VWO
- **イベントプロパティ:** `vwo_campaign_name`、 `vwo_variation_name`

{% alert tip %}
これらのカスタムイベントプロパティは、セグメンテーションおよびターゲティングにも使用できます。
{% endalert %}

## 考慮事項

### リクエストイベントプロパティのセグメンテーション

イベントプロパティセグメンテーションを使用するには、事前に Braze で有効にしておく必要があります。次のテンプレートを使用して、Braze CSM またはサポートチームに問い合わせてください。

   <table>
   <thead>
      <tr>
         <th>フィールド</th>
         <th>詳細</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td><strong>件名</strong></td>
         <td>VWO 統合のためのイベントプロパティセグメンテーション有効化のリクエスト</td>
      </tr>
      <tr>
         <td><strong>本文</strong></td>
         <td>
         Braze チームのみなさん、こんにちは。<br><br>
         VWO&lt;>Braze 統合から送信されるイベントのイベントプロパティセグメンテーションを有効にしたいと考えています。詳細は次のとおりです。<br><br>
         - <strong>イベント名:</strong>VWO<br>
         - <strong>イベントプロパティ:</strong> <code>vwo_campaign_name</code>,<code>vwo_variation_name</code><br><br>
         アカウントでプロパティが有効になったらご確認ください。<br><br>
         ありがとうございます。
         </td>
      </tr>
   </tbody>
   </table>
   {: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Braze データポイント

VWO からBraze に送信されるカスタムイベント(セグメンテーション で有効になっているすべてのイベントプロパティーを含む) は、Brazeインスタンスのデータポイントs を記録します。

### 制限事項

現在、この統合は、テストデータのリアルタイム同期をサポートしていません。テストデータが Braze に表示されるまで、最大 15 分ほど遅れる場合があります。

## トラブルシューティング

Braze で VWO のデータが表示されない場合:

1. テストキャンペーンが実行されているページを右クリックし、[**Inspect Element**] を選択します。
2. [**Network**] タブで、[**Braze**] を検索し、Braze のネットワークコールをフィルタリングします。
3. ネットワークコールは、ページのロード時に入力されます。ネットワークコールを表示するにはページをリロードします。
4. ネットワークコールを選択すると、詳細が表示されます。
5. **ペイロード]**タブの**[リクエストペイロード]**セクションに移動し、[カスタムイベント]を示す[**ce]**という名前のイベントを見つける。
6. 0: および data: を展開すると、n: が表示されます。"VWO" (Custom Event の名前) とp: {vwo_campaign_name: "<your vwo campaign name>"、vwo_variation_name: "<variation name>"}。これらは、値が VWO から Braze にプッシュされていることを示しています。

 ![Brazeのトラブルシューティング]({% image_buster /assets/img/vwo/vwo5_troubleshooting.png %})

その他のサポートについては、VWO カスタマーサクセスマネージャーにお問い合わせください。
