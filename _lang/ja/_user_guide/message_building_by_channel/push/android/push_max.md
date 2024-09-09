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


## プッシュマックスとは。

\[最大限にプッシュ通知] は、失敗したプッシュ通知をトラッキングし、ユーザーがプッシュ通知を受信する可能性が高いときにプッシュ通知を再送信することで、Android プッシュ通知を強化します。

Xiaomi、OPPO、およびVivoのような中国のOrigin al Equipment Manufacturers(OEM)によって製造されたいくつかのAndroid装置は、バッテリ寿命を延ばすためにロバストなバッテリ最適化方式を採用している。この振る舞いは、バックグラウンド アプリプロセッシングをシャットダウンする意図しない結果をもたらす可能性があり、アプリがフォアグラウンドにない場合、これらの装置上のプッシュ通知sの配信可能性を低下させる。この状況は、アジア太平洋(APAC)市場で最も頻繁に発生する。

## 可用性

- Android プッシュ通知 sのみ使用可能
- アクション ベースまたはAPI トリガーメッセージではサポートされません
- [ユーザーの最後に使用したデバイス]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message#device-options)にのみ送信するオプションが選択されている場合はサポートされません

## 前提条件

プッシュマックスを使用して送信されたプッシュ通知は、少なくとも次の[最小SDKバージョン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions)を持つ機器にのみ配信されます。

{% sdk_min_versions android:29.0.1 %}

## プッシュ最大値の使用

{% tabs %}
{% tab キャンペーン %}

キャンペーンでプッシュマックスを使用するには:

1. 押しキャンペーンを作成します。
2. ** Android Push** をプラットフォームとして選択します。
3. **Schedule Delivery**ステップに移動します。
4. **Send using Push Max**を選択します。

![スケジュール配信ステップのAndroidプッシュ配信セクションで、"Send using Push Max".]({% image_buster /assets/img_archive/push_max_campaigns.png %})を選択します。

{% endtab %}
{% tab キャンバス %}

キャンバスで最大プッシュを使用するには:

1. キャンバスにメッセージステップを追加します。
2. ** Android Push** をプラットフォームとして選択します。
3. **Delivery Settings**タブに移動します。
4. **Send using Push Max**を選択します。

![Android プッシュメッセージステップの配信設定タブで、"Send using Push Max".]({% image_buster /assets/img_archive/push_max_canvas.png %})オプションを使用します。

{% endtab %}
{% endtabs %}

以下の2 つの機能(インテリジェントタイミングと生存時間)は、プッシュマックスと同時に使用することで、Android プッシュ通知s の配信機能を向上させることができます。

### インテリジェントタイミング

Max を押してください。[インテリジェントタイミング]({{site.baseurl}}/user_guide/sage_ai/intelligence/intelligent_timing/) がオンのときに最適です。インテリジェントタイミングでは、ユーザーがアプリを使用している可能性が最も高く、プッシュが配信される可能性が最も高い時点で、プッシュ通知を計算して送信できます。

### 生存時間(TTL)

Time to Live (TTL) は、障害が発生したプッシュ通知をFirebase Cloud Messaging (FCM) に追跡し、ユーザーが受信する可能性があるときに通知を再試行できます。

デフォルトでは、Time to Live(生存期間)は最長である28日に設定されています。すべての新しいAndroidプッシュメッセージのデフォルト TTL を**設定**> **ワークスペース設定**> **存続期間へのプッシュ時間(TTL)**から減らすことができます。または、Android プッシュ通知を作成するときに**設定**タブでメッセージごとの日数を設定することができます。

![生存フィールド期間が28 日に設定されます。]({% image_buster /assets/img_archive/time_to_live.png %}){: style="max-width:70%"}

## 知っておくべきこと

### 推進コード

Braze [プロモーションコードs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/)は、プッシュマックスが有効になっているメッセージでは使用しないことをお勧めします。

これは、プロモーションコードsが一意であるためです。プロモーションコードを含むプッシュ通知が配信に失敗した場合、プッシュマックスによりその通知が再送されると、新しいプロモーションコードが送信されます。これにより、プロモーションコードの消費が予想以上に速くなる可能性があります。

### キャンバスイベントのプロパティとエントリのプロパティ

メッセージに[キャンバスのエントリプロパティーまたはイベントプロパティー]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) へのLiquid 参照を含めると、Push Max が期待どおりに機能しない場合があります。これは、プッシュマックスがメッセージを再送信しようとしているときに、エントリおよびイベントプロパティーが使用できないためです。
