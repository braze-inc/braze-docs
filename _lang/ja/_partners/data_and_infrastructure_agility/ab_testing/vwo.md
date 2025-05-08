---
nav_title: VWO
article_title: VWOとブレーズの統合
description: "VWO とBraze を統合する方法について説明します。"
alias: /partners/vwo/
page_type: partner
search_tag: Partner
---

# VWO

> [VWO](https://vwo.com/)は、顧客行動データに裏付けされた変換最適化プログラムをチームが実行できるようにすることで、ブランドが主要なビジネスメトリクスを強化するのに役立つ強力な実験プラットフォームです。VWOでは、顧客データの統一、行動的洞察の獲得、仮説の構築、複数のプラットフォーム(サーバー、ウェブ、モバイル)にわたるA/Bテストの実行、機能の展開、経験のパーソナライズ、顧客ジャーニー全体の最適化が可能です。

VWOとBrazeを統合することで、VWO実験データを活用してターゲットセグメントを作成し、パーソナライズされたキャンペーンを提供することができます。

## 前提条件

| 必要条件     | 説明 |
|-----------------|-------------|
| VWOアカウント     | 実験データへのアクセス権を持つVWO アカウント。 |
| Braze アカウント   | Web ページに統合された[Braze Web SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) を持つアクティブなBraze アカウント。イベントプロパティのセグメンテーションも有効にする必要があります。これを要求するには、[考慮事項](#request-event-property-segmentation)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## VWOとブレーズの統合

### ステップ1:VWO でのブレーズ統合の有効化

1. VWO アカウントにログインします。
2. VWO ダッシュボードで、**Configurations > Integrations** に移動します。ここでは、ワークスペースレベルで統合を有効にすることができます。この統合は、デフォルトで将来のすべてのテストキャンペーンに適用されます。

   ![VWO 統合設定]({% image_buster /assets/img/vwo/vwo1_settings.png %})

4. ろう付け統合を選択して有効にします。
5. オプションで、既存のキャンペーンに対してブレーズ統合を有効にすることができます。そのためには、キャンペーンを選択し、**Configuration > Integrations** に移動して、Braze を有効にします。

   ![ブレーズ統合を有効にする]({% image_buster /assets/img/vwo/vwo2_enable_braze.png %})

6. 統合を有効にすると、VWO はキャンペーンレベルでBraze に実験データの送信を開始します。

### ステップ2:VWO イベントプロパティを使用して、Braze でセグメントを作成する

1. Braze ダッシュボードで、**Segments** > **\+ Create Segment** を選択します。
3. **Create Segment**ウィンドウで、セグメントの名前を入力し、**Create Segment**と入力します。
4. 新しく作成したセグメントで、**Filters** > **Add Filter**を選択し、フィルタタイプとして**Custom Event**を選択します。
6. フィルタドロップダウンで、**VWO** を検索します。
7. 関連するVWO プロパティを選択し、必要な値を指定します。
8. 必要に応じて、訪問回数と時間枠を設定します。完了したら、[**保存**] を選択します。

   ![ろう付けセグメント作成]({% image_buster /assets/img/vwo/vwo3_braze_segment.png %})

9. セグメント条件に一致するユーザー数を表示するには、**Calculate Exact Statistics**を選択します。

   ![ブレーズセグメント統計]({% image_buster /assets/img/vwo/vwo4_braze_segment_calculate_size.png %})

## データフロー

VWO は、以下の形式を使用して、キャンペーン実験データをカスタムイベントとしてBraze に送信します。

- **イベント名:**VWO
- **イベントプロパティ:** `vwo_campaign_name`、 `vwo_variation_name`

{% alert tip %}
これらのカスタムイベントプロパティは、セグメンテーションおよびターゲティングにも使用できます。
{% endalert %}

## 考慮事項

### リクエストイベントプロパティのセグメンテーション

イベント・プロパティ・セグメンテーションを使用する前に、Braze で有効にする必要があります。次のテンプレートを使用して、Braze CSM またはサポートチームにアクセスしてください。

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
         <td>VWO統合のためのイベントプロパティセグメンテーションを有効にするリクエスト</td>
      </tr>
      <tr>
         <td><strong>本文</strong></td>
         <td>
         こんにちは、ろうろうチーム、<br><br>
         VWO&lt;>Braze統合から送信されるイベントのイベントプロパティセグメンテーションを有効にしたいと考えています。詳細は次のとおりです。<br><br>
         - <strong>イベント名:</strong>VWO<br>
         - <strong>イベントプロパティ:</strong> <code>vwo_campaign_name</code>,<code>vwo_variation_name</code><br><br>
         アカウントでプロパティが有効になったらご確認ください。<br><br>
         ありがとうございます。
         </td>
      </tr>
   </tbody>
   </table>
   {: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### ろう付けデータ点

VWO からブレーズに送信されるカスタムイベント(セグメンテーションで有効になっているイベントプロパティを含む) は、ブレーズインスタンスのデータポイントを消費します。

### 制限事項

現在、この統合は、テストデータのリアルタイム同期をサポートしていません。試験データがブレーズに表示されるまで、最大15 分の遅延がある場合があります。

## トラブルシューティング

Braze でVWO データが表示されない場合:

1. テストキャンペーンが実行されているページを右クリックし、**Inspect Element** を選択します。
2. **Network** タブで、**Braze** を検索し、Braze のネットワークコールをフィルタリングします。
3. ネットワークコールは、ページのロード時に入力されます。ページをリロードして、ネットワークコールを表示できます。
4. ネットワークコールを選択すると、詳細が表示されます。
5. **Request Payload** セクションの**Payload** タブに移動します。ここには、**ce** という名前のイベントがあり、カスタムイベントを示しています。
6. 0: とdata: を展開してn: を表示します。"VWO" (Custom Event の名前) およびp: {vwo_campaign_name: "<your vwo campaign name>", vwo_variation_name: "<variation name>"}.これらは、値がVWOによってブレーズにプッシュされていることを示します。

 ![ブレーズのトラブルシューティング]({% image_buster /assets/img/vwo/vwo5_troubleshooting.png %})

追加のサポートについては、VWOカスタマーサクセスマネージャーにお問い合わせください。
