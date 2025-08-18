---
nav_title: タグ
article_title: タグ
page_order: 12
page_type: reference
description: "このリファレンス記事では、エンゲージメントの細かな整理と並べ替えに使用できる Braze ダッシュボードのタグについて説明します。"

---
# タグ

> Braze では、セグメント、キャンペーン、キャンバスの作成者、編集者、日付、およびステータスの情報を追跡します。ユーザーはタグを作成して、エンゲージメントの細かな整理と並べ替えができます。

## キャンペーン、キャンバス、およびセグメントのタグ

キャンペーン、キャンバス、セグメントの作成または編集時にタグを追加できます。エンゲージメント名の下にある <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span> [**タグ**] をクリックして、既存のタグを選択するか、新規のタグを追加するための入力を開始します。

![キャンペーン作成時にタグを追加する]({% image_buster /assets/img_archive/tags_add_tag.png %}){: style="max-width:60%;" }

{% alert important %}
キャンペーン、キャンバス、またはセグメントに最大 175 個のタグを追加できます。
{% endalert %}

### 一括タグ付け

複数のエンゲージメントを選択し、<span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tag Asを**選択することで、複数のキャンペーン、キャンバス、セグメントにタグを追加することもできる。

![複数のキャンペーンに同時にタグを追加する]({% image_buster /assets/img_archive/tags_apply_multiple.gif %})

{% alert important %}
一括タグ付けを使用して、すでに異なるタグが設定されている複数のキャンペーンに新しいタグを適用すると、選択された各キャンペーンに新しいタグが適用され、あるキャンペーンに設定されているタグは、そのタグが元々キャンペーンに関連付けられていなかったとしても、選択された他のすべてのキャンペーンに適用される。
{% endalert %}

### タグを見る

キャンペーン、キャンバス、セグメンテーションに設定されたタグは、詳細ページのエンゲージメント名の近くに表示される。タグはキャンペーン分析にも表示されます。

![キャンペーン分析ページに表示されるタグ]({% image_buster /assets/img_archive/tag_details_page.png %}){: style="max-width:60%;" }

### タグでフィルターをかける

また、キャンペーン、キャンバス、またはセグメントのリストにも、[**アーカイブ済み**] や [**下書き**] などの追加のステータスラベルのタグとともにタグが表示されます。タグでフィルターをかけるには、タグのリストからタグ名を選択する。

![キャンペーン一覧のタグ。]({% image_buster /assets/img_archive/tags_grid.png %})

## カスタムデータタグ

また、[カスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes)および[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#managing-custom-events)を管理するときに、タグをカスタムデータに追加することもできます。 

{% alert important %}
この機能は現在早期アクセス段階です。この早期アクセスへ参加することに興味がある場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

## タグの管理

キャンペーン、キャンバス、セグメントにわたって同じタグを使用できます。ダッシュボード全体でタグの名前の変更、削除、または追加を効率的に行うには、[**設定**] > [**タグ管理**] に移動します。

![[設定の管理] ページの [タグ] タブ。]({% image_buster /assets/img_archive/tags_view.png %})

タグをさらに整理するには、親タグの下にタグをネストします。例えば、すべての祝日タグを親の `Holidays` タグの下にネストしたり、マーケティングの目標到達段階に関連するすべてのタグを親の `Funnel` タグの下にネストしたりできます。 

そのためには、新しいタグを作成し、[**次のタグの下にネスト**] を選択して、新しいタグを下にネストする既存のタグを選択します。また、[**タグ管理**] ページから既存のタグをネストすることもできます。このページで、タグのある行にカーソルを合わせて、[**<i class="fas fa-pencil-alt"></i> 編集**]をクリックします。次に、前述の手順に従います。

![ネストされたタグを作成する]({% image_buster /assets/img_archive/tag_nested.png %}){: style="max-width:70%;" }

## ベストプラクティス {#tags-best-practices}

タグは、エンゲージメント作戦を追跡するための便利な整理ツールです。セグメントやキャンペーンをビジネス目標や目標到達段階などにリンクできます。

以下に、e コマースアプリで有用なタグの例を示します。

<style>
table td {
    word-break: break-word;
}
</style>


<table>
<thead>
  <tr>
    <th>重点項目</th>
    <th>ビジネス対象</th>
    <th>地域</th>
    <th>キャンペーン</th>
    <th>祝日</th>
    <th>トランザクション</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>オンボーディング<br>再エンゲージメント<br>忠実<br>パワーユーザー<br>解約<br>喪失</td>
    <td>上顧客<br>アクティブなユーザー<br>新規ユーザー<br>FacebookAttribution<br>最初のアクション</td>
    <td>米国<br>北東部<br>中西部<br>南部<br>西部<br>南米<br>アジア太平洋<br>西ヨーロッパ<br>中東</td>
    <td>販売<br>クーポン<br>イベント</td>
    <td>Martin Luther King Jr. 牧師の日<br>SuperBowl<br>πの日<br>聖パトリックデー<br>NCAA バスケットボールトーナメント<br>イースター<br>過ぎ越し<br>母の日<br>戦没将兵追悼記念日<br>父の日<br>独立記念日<br>労働者の日<br>復員軍人の日<br>コロンブスデー<br>大統領の日<br>ハロウィーン<br>ロシュハシャナ<br>感謝祭<br>クリスマス<br>ハヌカー<br>正月</td>
    <td>トランザクション<br>通知<br>接続アクション実行</td>
  </tr>
</tbody>
</table>

## ユースケース

タグを活用してメッセージングのライフサイクルを管理する方法を探しているユーザー向けに、一般的なユースケースをいくつか紹介します。

### スロットリング

顧客が特定タイプのキャンペーンを受け取る頻度を制限します。例えば、以下のようなフィルターを設定して、販売促進キャンペーンの頻度を制限できます。

`Last received campaign` 次のタグを持つ `Promo` 5 日超前
<br>`OR`<br>
`Has not received campaign` 次のタグを持つ `Promo`

### レポート

特定のタグを持つすべてのキャンペーンの量を監視するには、エンゲージメントレポートを設定します。例えば、すべてのプッシュキャンペーンを監視する場合は、それらのキャンペーンに `Push Reporting` のようなタグを追加し、それらのタグが付いたキャンペーンのレポートを毎日送信するように、[エンゲージメントレポート]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#automatically-select-campaigns-or-canvases)を設定できます。
