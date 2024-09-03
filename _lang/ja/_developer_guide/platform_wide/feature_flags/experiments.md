---
nav_title: フィーチャー・フラッグの実験
article_title: フィーチャー・フラッグの実験
page_order: 40
description: "機能フラグ実験では、コンバージョン率を最適化するためにアプリケーションの変更をA/Bテストできる。"
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web

---

# フィーチャー・フラッグ実験を行う

> 機能フラグ実験では、コンバージョン率を最適化するためにアプリケーションの変更をA/Bテストできる。マーケティング担当者は、機能フラグを使って、新機能がコンバージョン率にプラスに影響するかマイナスに影響するか、あるいはどの機能フラグのプロパティセットが最も最適かを判断することができる。

## 前提条件

実験でユーザーデータを追跡する前に、アプリはユーザーが機能フラグと相互作用した時を記録する必要がある。これをフィーチャー・フラッグ・インプレッションと呼ぶ。ユーザーがテスト中の機能を見たとき、あるいは見た可能性があるときは、コントロールグループであっても、必ず機能フラグのインプレッションを記録すること。

機能フラグのインプレッションを記録する方法については、[機能フラグを作成するを][6]参照のこと。

```javascript
const featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag?.enabled) {
   return <NewFeature />
} else {
   return <ExistingFeature />
}

```

## ステップ 1:実験を行う

1. **Messaging**>**Campaignsに**進み、**\+ Create Campaignを**クリックする。
2. **Feature Flag Experimentを**選択する。
3. キャンペーンに、明確で意味のある名前を付けます。

## ステップ2:実験のバリエーションを追加する

次に、バリエーションを作る。各バリアントについて、オンまたはオフにしたい機能フラグを選択し、割り当てられたプロパティを確認する。

機能のインパクトをテストするには、バリアントを使ってトラフィックを2つ以上のグループに分ける。1つのグループを "My control group "と名付け、その機能フラグをオフにする。

### プロパティの上書き

機能フラグを最初に設定したときにデフォルトのプロパティを指定したが、特定のキャンペーンバリアントを受け取るユーザーに対して、それらの値を上書きすることを選択できる。

![]\[画像1]{: style="max-width:80%"}

追加のデフォルトプロパティを編集、追加、削除するには、**Messaging**>**Feature Flagsから**機能フラグ自体を編集する。

## ステップ 3:ターゲットとするユーザーを選択する

次に、セグメントやフィルターを選択することで、[ユーザーを絞り込む][4]必要がある。セグメント・メンバーシップは、指定されたユーザーのフィーチャー・フラグが更新されたときに計算される。

{% alert note %}
変更は、アプリが機能フラグをリフレッシュした後、または新しいセッションが開始されたときに利用可能になる。
{% endalert %}

## ステップ 4:バリアントを配布する

実験に使用するパーセンテージ分布を選ぶ。ベストプラクティスとして、実験開始後に配布を変更すべきではない。

## ステップ 5: コンバージョンを割り当てる

Brazeを使えば、キャンペーンを受け取った後、ユーザーがどれくらいの頻度で特定のアクション（[コンバージョンイベント][5]）を実行するかを追跡することができる。ユーザーが指定されたアクションを取った場合、コンバージョンがカウントされる最大30日間のウィンドウを指定する。

## ステップ 6: レビューと開始

実験の最後を構築し終えたら、その詳細を確認し、**Launch Experimentを**クリックする。


[1]: {{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/
[3]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/
[4]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/
[5]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/
[6]: {{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#impressions

\[image1] ： {% image_buster /assets/img/feature_flags/feature_flag_experiment_override.png %} 
