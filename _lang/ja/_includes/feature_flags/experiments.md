# 特集フラッグ実験

> 機能フラグ実験では、コンバージョン率を最適化するためにアプリケーションの変更をA/Bテストできる。マーケティング担当者は、機能フラグを使って、新機能がコンバージョン率にプラスに影響するかマイナスに影響するか、あるいはどの機能フラグのプロパティセットが最も最適かを判断することができる。

## 前提条件

実験でユーザーデータを追跡する前に、ユーザーがフィーチャーフラグを操作したタイミングをアプリで記録する必要があります。これをフィーチャーフラグインプレッションと呼びます。ユーザーがテスト中の機能を見たとき、あるいは見た可能性があるときは、コントロールグループであっても、必ず機能フラグのインプレッションを記録すること。

フィーチャーフラグのインプレッションを記録する方法については、[フィーチャーフラグを作成する]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#impressions)を参照してください。

{% tabs %}
{% tab Web %}

```javascript
const featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag?.enabled) {
   return <NewFeature />
} else {
   return <ExistingFeature />
}
```

{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

```java
FeatureFlag featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag != null && featureFlag.getEnabled()) {
  return new NewFeature();
} else {
  return new ExistingFeature();
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("my-new-feature")
braze.logFeatureFlagImpression("my-new-feature")
if (featureFlag?.enabled == true) {
  return NewFeature()
} else {
  return ExistingFeature()
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## フィーチャー・フラッグ実験を行う

### ステップ 1: 実験を行う

1. [**メッセージング**] > [**キャンペーン**] に進み、[**+キャンペーンの作成**] を選択します。
2. [**フィーチャーフラグの実験**] を選択します。
3. キャンペーンに明確で意味のある名前をつける。

### ステップ 2:実験のバリエーションを追加する

次に、バリエーションを作ります。それぞれのバリアントについて、オンまたはオフにしたいフィーチャーフラグを選択し、割り当てられたプロパティを確認します。

機能のインパクトをテストするには、バリアントを使ってトラフィックを2つ以上のグループに分けます。1つのグループを "My control group "と名付け、その機能フラグをオフにする。

### ステップ3: プロパティを上書きする（オプション）

特定のキャンペーンバリアントを受け取るユーザーに対して最初に設定した既定のプロパティを上書きすることを選択できます。

追加のデフォルトプロパティを編集、追加、削除するには、[**メッセージング**] > [**フィーチャーフラグ**] からフィーチャーフラグ自体を編集します。バリアントが無効になっている場合、SDKは指定された機能フラグの空のプロパティオブジェクトを返します。

![「Experiment Variants」セクションの「link」変数キーは「/sales」で上書きされます。]({% image_buster /assets/img/feature_flags/feature_flag_experiment_override.png %}){: style="max-width:80%"}

### ステップ 4: ターゲットとするユーザーを選択する

セグメントまたはフィルターのいずれかを使用して、[ターゲットユーザー]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/)を選択します。例えば、**Received Feature Flag Variant**フィルターを使用して、すでにA/Bテストを受けたユーザーをリターゲティングすることができる。

![フィルターグループサーチバーで「受信フィーチャーフラグバリアント」がハイライトされたフィーチャーフラグ実験の「ターゲット」ページ。]({% image_buster /assets/img/feature_flags/variant-filter-dropdown.png %}){: style="max-width:70%"}

{% alert note %}
セグメントメンバーシップは、指定されたユーザーのフィーチャーフラグが更新されたときに計算されます。変更は、アプリがフィーチャーフラグをリフレッシュした後、または新しいセッションが開始されたときに利用可能になります。
{% endalert %}

### ステップ 5: バリアントを配布する

実験に使用するパーセンテージ分布を選ぶ。ベストプラクティスとして、実験開始後に配布を変更すべきではありません。

### ステップ 6: コンバージョンを割り当てる

Brazeを使えば、キャンペーンを受け取った後、ユーザーがどれくらいの頻度で特定のアクション（[コンバージョンイベント]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/)）を実行するかを追跡することができる。ユーザーが指定されたアクションを取った場合、コンバージョンがカウントされる最大30日間のウィンドウを指定する。

### ステップ 7:レビューと開始

最後の実験の構築が完了したら、その詳細を確認し、[**実験を開始**] を選択します。

## 結果を見直す

フィーチャーフラグの実験が終わったら、実験のインプレッションデータを見直すことができます。[**メッセージング**] > [**キャンペーン**] に移動し、フィーチャーフラグ実験を含むキャンペーンを選択します。

### キャンペーン分析

**キャンペーン分析**は、次のような実験のパフォーマンスの大まかな概要を提供します。

- インプレッションの総数
- ユニークインプレッション数
- 1次コンバージョン率
- メッセージングが生み出す総収入
- 推定オーディエンス

また、配信、オーディエンス、およびコンバージョンに関する実験の設定を表示することもできます。

### フィーチャーフラグ実験のパフォーマンス

**フィーチャーフラグ エクスペリメント パフォーマンスは**、あなたのメッセージが様々な次元でどの程度のパフォーマンスを示したかを示す。表示される具体的な指標は、選択したメッセージングチャネルや、多変量テストを実施しているかどうかによって異なる。各バリアントに関連するフィーチャーフラグの値を見るには、**プレビュー**を選択します。
