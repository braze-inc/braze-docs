---
nav_title: フィーチャーフラグの実験
article_title: フィーチャーフラグの実験
page_order: 40
description: "機能フラグのテストでは、アプリケーションへの変更を A/B テストしてコンバージョン率を最適化できます。"
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web

---

# 機能フラグの実験の作成

> 機能フラグのテストでは、アプリケーションへの変更を A/B テストしてコンバージョン率を最適化できます。マーケターは、機能フラグを使用して、新機能がコンバージョン率にプラスまたはマイナスの影響を与えるかどうか、またはどの機能フラグプロパティのセットが最も最適かを判断できます。

## 前提条件

テストでユーザーデータをトラッキングする前に、ユーザーが機能フラグを操作したタイミングをアプリで記録する必要があります。これは、機能フラグのインプレッションと呼ばれます。ユーザーがコントロール グループに属している場合でも、テストしている機能を表示した、または表示した可能性がある場合は、必ず機能フラグのインプレッションを記録してください。

機能フラグのインプレッションのログ記録の詳細については、「 [機能フラグの作成][6]」を参照してください。

\`\`\`javascript
const featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag?.enabled) {
   return <NewFeature />
} else {
   return <ExistingFeature />
()

\`\`\`

## ステップ 1:実験を作成する

1. **「メッセージング**>**キャンペーン**」に移動し、「**+キャンペーンを作成**」をクリックします。
2. [ **Feature Flag Experiment**] を選択します。
3. キャンペーンには、明確で意味のある名前を付けます。

## ステップ 2: テストのパターンを追加する

次に、バリエーションを作成します。バリアントごとに、オンまたはオフにする機能フラグを選択し、割り当てられたプロパティを確認します。

機能の影響をテストするには、パターンを使用してトラフィックを 2 つ以上のグループに分割します。1 つのバリアントをコントロール グループと見なす必要があり、このバリアントでは機能フラグをオフにする必要があります。

### プロパティの上書き

機能フラグを最初に設定したときにデフォルトのプロパティを指定しましたが、特定のキャンペーン バリアントを受け取るユーザーの値を上書きすることもできます。

![][画像1]{: style="max-width:80%"}

追加の既定のプロパティを編集、追加、または削除するには、[ **メッセージング** ] > **[機能フラグ**] から機能フラグ自体を編集します。

## ステップ 3: ターゲットとするユーザーを選択する

次に、セグメントまたはフィルターを選択して [ユーザーをターゲティング][4] し、オーディエンスを絞り込む必要があります。セグメント メンバーシップは、特定のユーザーの機能フラグが更新されたときに計算されます。

{% alert note %}
ターゲットオーディエンスは、0%を超えるロールアウトを保存するとすぐに機能フラグの対象となります。変更は、アプリが機能フラグを更新するか、新しいセッションが開始されたときに利用可能になります。
{% endalert %}

## ステップ 4: バリアントの配布

テストのパーセント分布を選択します。ベスト プラクティスとして、テストの開始後にディストリビューションを変更しないでください。

## ステップ 5: コンバージョンを割り当てる

Brazeを使用すると、ユーザーがキャンペーンを受け取った後、特定のアクション( [コンバージョンイベント][5])を実行する頻度を追跡できます。最大 30 日間の期間を指定して、ユーザーが指定したアクションを実行した場合にコンバージョンがカウントされるようにします。

## ステップ 6:レビューと開始

最後の実験の作成が完了したら、その詳細を確認し、[ **実験を開始**] をクリックします。


[1]: {{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/
[3]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/
[4]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/
[5]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/
[6]: {{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#impressions

[画像1]: {% image_buster /assets/img/feature_flags/feature_flag_experiment_override.png %} 
