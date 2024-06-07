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

> Push Maxと、この機能を使用して[中国OEMデバイスへの]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/chinese_push_deliverability/)Androidプッシュ通知の配信性を向上させる方法について説明します。


## プッシュ・マックスとは？

[最大限にプッシュ通知] は、失敗したプッシュ通知をトラッキングし、ユーザーがプッシュ通知を受信する可能性が高いときにプッシュ通知を再送信することで、Android プッシュ通知を強化します。

Xiaomi、OPPO、Vivoなど、中国のOEM（相手先ブランド製造）メーカーが製造するAndroid端末の中には、バッテリーを長持ちさせるために、バッテリーの最適化をしっかり行う方式を採用しているものがある。この動作は、アプリがフォアグラウンドにない場合、バックグラウンドのアプリ処理をシャットダウンし、これらのデバイス上でプッシュ通知の配信可能性を低下させるという意図しない結果をもたらす可能性がある。このような状況は、アジア太平洋（APAC）市場で最も多く見られる。

## 空室状況

- Androidのプッシュ通知でのみ利用可能
- アクションベースまたはAPIトリガーメッセージには対応していません。
- [最後に使用したデバイスにのみ送信]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message#device-options)するオプションが選択されている場合はサポートされません。

## 前提条件

Push Maxを使用して送信されたPush通知は、少なくとも以下の[最小SDKバージョンを]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions)持つデバイスにのみ配信されます：

{% sdk_min_versions android:29.0.1 %}

## プッシュ・マックスの使用

{% tabs %}
{% tab Campaigns %}

キャンペーンでPush Maxを使用するには

1. プッシュキャンペーンを作成する。
2. プラットフォームとして**Android Pushを**選択します。
3. **スケジュール配信の**ステップに進みます。
4. **プッシュ・マックスを使用して送信を**選択します。

![Android Push Deliverability section of the Schedule Delivery step with the option to "Send using Push Max".]({% image_buster /assets/img_archive/push_max_campaigns.png %})

{% endtab %}
{% tab Canvas %}

キャンバスでプッシュ・マックスを使うには

1. キャンバスにメッセージステップを追加する。
2. プラットフォームとして**Android Pushを**選択します。
3. **配信設定**タブに移動します。
4. **プッシュ・マックスを使用して送信を**選択します。

![Delivery Settings tab of an Android Push Message step with the option to "Send using Push Max".]({% image_buster /assets/img_archive/push_max_canvas.png %})

{% endtab %}
{% endtabs %}

以下の2つの機能、Intelligent TimingとTime to LiveをPush Maxと併用することで、Androidのプッシュ通知の配信性を高めることができます。

### インテリジェントタイミング

プッシュ・マックスは、[インテリジェント・タイミングが]({{site.baseurl}}/user_guide/sage_ai/intelligence/intelligent_timing/)オンになっているときに最もよく機能する。インテリジェント・タイミングは、ユーザーがアプリを使用している可能性が最も高く、プッシュが配信される可能性が最も高い時間帯を計算し、プッシュ通知を送信することができます。

### 生存時間（TTL）

Time to Live (TTL)は、Firebase Cloud Messaging (FCM)へのプッシュ通知の失敗を追跡し、ユーザが通知を受け取る可能性があるときに再試行することができます。

デフォルトでは、生存期間は最大28日に設定されている。**設定**＞**ワークスペース設定**＞**Push Time to Live (TTL**)から、すべての新しいAndroidプッシュメッセージのデフォルトのTTLを減少させるか、Androidプッシュ通知を作成する際に**設定**タブでメッセージごとに日数を構成することができます。

![Time to Live field set to 28 days.]({% image_buster /assets/img_archive/time_to_live.png %}){: style="max-width:70%"}

## 知っておくべきこと

### プロモーションコード

プッシュマックスがオンになっているメッセージでは、Braze[プロモーション]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/)コードを使用しないことをお勧めします。

これは、プロモーションコードがユニークだからだ。プロモーションコードを含むプッシュ通知が配信に失敗した場合、Push Maxによってその通知が再送信されると、新しいプロモーションコードが送信されます。その結果、プロモーションコードを予想以上に早く消費してしまうことになりかねない。

### キャンバス・イベント・プロパティとエントリー・プロパティ

[Canvas エントリ・プロパティやイベント・プロパティへの]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)リキッド参照をメッセージに含めると、Push Max は期待通りに動作しないかもしれません。これは、Push Max がメッセージを再送しようとしているときには、エントリとイベントのプロパティが利用できないためです。
