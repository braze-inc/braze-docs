---
nav_title: 最大限にプッシュ通知
article_title: 最大限にプッシュ通知
page_type: reference
description: "[最大限にプッシュ通知] は、失敗したプッシュ通知をトラッキングし、ユーザーがプッシュ通知を受信する可能性が高いときにプッシュ通知を再送信することで、Android プッシュ通知を強化します。"

permalink: /user_guide/message_building_by_channel/push/android/push_max/
platform: Android
channel:
  - Push

---

# 最大限にプッシュ通知

> Push Max について、およびこの機能を使用して、[中国のOEM デバイス]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/chinese_push_deliverability/) へのAndroid プッシュ通知の配信性を向上させる方法について説明します。

## 最大限にプッシュ通知

[最大限にプッシュ通知] は、失敗したプッシュ通知をトラッキングし、ユーザーがプッシュ通知を受信する可能性が高いときにプッシュ通知を再送信することで、Android プッシュ通知を強化します。

Xiaomi、OPPO、およびVivoのような中国のOrigin al Equipment Manufacturers(OEM)によって製造されたいくつかのAndroid装置は、バッテリ寿命を延ばすためにロバストなバッテリ最適化方式を採用している。この動作は、バックグラウンドのアプリ処理をシャットダウンするという意図しない結果をもたらす可能性があります。これにより、アプリがフォアグラウンドにない場合、これらのデバイスでプッシュ通知の配信性が低下します。この状況は、アジア太平洋 (APAC) 市場で最も頻繁に発生します。

## 可用性

- Android のプッシュ通知にのみ使用できます
- アクション ベースまたはAPI トリガーメッセージではサポートされません
- [ユーザーの最後に使用したデバイス]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#device-options)にのみ送信するオプションが選択されている場合はサポートされません

## 前提条件

最大限にプッシュ通知の機能を使用して送信されたプッシュ通知は、次の[SDK の最小バージョン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions)以降を持つデバイスにのみ配信されます。

{% sdk_min_versions android:29.0.1 %}

## プッシュ最大値の使用

{% tabs %}
{% tab キャンペーン %}

キャンペーンでプッシュマックスを使用するには:

1. プッシュキャンペーンを作成します。
2. ** Android Push** をプラットフォームとして選択します。
3. **Schedule Delivery**ステップに移動します。
4. **Send using Push Max**を選択します。

![スケジュール配信ステップの [最大限にプッシュ通知] を使用して送信] オプションを持つ [Android プッシュ通知配信] セクション。]({% image_buster /assets/img_archive/push_max_campaigns.png %}

{% endtab %}
{% tab キャンバス %}

キャンバスで最大限にプッシュ通知の機能を使用するには、次の手順に従います。

1. キャンバスにメッセージステップを追加します。
2. ** Android Push** をプラットフォームとして選択します。
3. [**配信設定**] タブに移動します。
4. **Send using Push Max**を選択します。

![Android プッシュ通知メッセージステップの [最大限にプッシュ通知] を使用して送信] オプションを持つ [配信設定] タブ。]({% image_buster /assets/img_archive/push_max_canvas.png %}

{% endtab %}
{% endtabs %}

インテリジェントタイミングと有効時間の 2 つの機能を最大限にプッシュ通知の機能と組み合わせて使用すると、Android プッシュ通知の配信性が向上する可能性があります。

### インテリジェントタイミング

[[インテリジェントタイミング]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/)] がオンのときに、最大限にプッシュ通知の効果が最大に発揮されます。インテリジェントタイミングでは、ユーザーがアプリを使用している可能性が最も高く、プッシュが配信される可能性が最も高い時点で、プッシュ通知を計算して送信できます。

### 有効時間 (TTL) 

有効時間 (TTL) を使用すると、失敗したプッシュ通知を Firebase Cloud Messaging (FCM) まで追跡し、ユーザーが受信する可能性があるときに通知を再試行できます。

デフォルトで、[有効時間] は最長の 28 日に設定されています。すべての新しいAndroidプッシュメッセージのデフォルト TTL を**設定**> **ワークスペース設定**> **存続期間へのプッシュ時間(TTL)**から減らすことができます。または、Android プッシュ通知を作成するときに**設定**タブでメッセージごとの日数を設定することができます。

![28 日に設定されている [有効時間] フィールド。]({% image_buster /assets/img_archive/time_to_live.png %}){: style="max-width:60%"}

## 知っておくべきこと

### プロモーションコード

Braze [プロモーションコードs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/)は、プッシュマックスが有効になっているメッセージでは使用しないことをお勧めします。

これは、プロモーションコードsが一意であるためです。プロモーションコードを含むプッシュ通知が配信に失敗した場合、プッシュマックスによりその通知が再送されると、新しいプロモーションコードが送信されます。これにより、プロモーションコードの消費が予想以上に速くなる可能性があります。

### キャンバスイベントのプロパティとエントリのプロパティ

メッセージに[キャンバスのエントリプロパティーまたはイベントプロパティー]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) へのLiquid 参照を含めると、Push Max が期待どおりに機能しない場合があります。これは、最大限にプッシュ通知の機能がメッセージの再送信を試行しているときに、エントリおよびイベントのプロパティが使用できないためです。
