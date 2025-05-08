# ユースケース:予約通知メールシステム

> Braze は、プログラムで高度に制御できるように設計された包括的なカスタマーエンゲージメントプラットフォームです。このユースケースでは、予約システムなど、製品とマーケティングの交差点にあるユースケースに接続できる機能をBraze が提供するいくつかの方法を紹介します。

このユースケースでは、Braze 機能を使用して予約リマインダーメールメッセージングサービスを構築する方法を示します。このサービスにより、ユーザーは予定を予約することができ、次回の予定のリマインダーとともにユーザーにメッセージを送信します。このユースケースでは電子メールメッセージが使用されますが、ユーザープロファイルへの単一の更新に基づいて、任意のチャネルまたは複数のチャネルでメッセージを送信できます。

このサービスを作成するその他の利点は、次のとおりです。
- 送信されたメッセージは完全に追跡され、レポートされます。
- メッセージコンテンツは、技術的でないブレーズユーザーが更新することができます。
- メッセージは、キャンペーン設定ごとのユーザプロファイルのオプトインおよびオプトアウトのステータスに従います。
- 予約データとメッセージインタラクションデータの両方を使用して、追加のメッセージングのためにユーザをセグメント化およびターゲット化することができます。たとえば、最初のリマインダーメッセージを開かないユーザーに、予定の前に追加のリマインダーを付けてリターゲットできます。

このユースケースを実現するには、次の手順を実行します。
1. [次の予約データをブレーズユーザープロファイルに書き込む](#step-1)
2. [予約リマインダーメッセージを設定して起動する](#step-2)
3. [更新された予約とキャンセルの処理](#step-3)

## ステップ1:次の予約データをブレーズユーザープロファイルに書き込む {#step-1}

予約が行われるたびに、ブレーズ[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) エンドポイントを使用して、[ネストされたカスタム属性]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/) をユーザプロファイルに書き込みます。ネストされたカスタム属性に、リマインダメッセージの送信とカスタマイズに必要なすべての情報が含まれていることを確認します。この使用例では、ネストされたカスタム属性に「trips」という名前を付けます。

### 予約を追加する

ユーザが予約を作成する場合、オブジェクトの配列に次の構造を使用して、`/users/track` エンドポイントを介してデータをブレーズに送信します。

{% raw %}
```json
{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": [
               {"trip_id":"1","name":"London Trip","start_date"{$time:"2025-11-11"}},
               {"trip_id":"2","name":"Sydney Trip","start_date"{$time:"2025-11-11"}}
           ]
       }
   ]
}
```
{% endraw %}

ネストされたカスタム属性「trips」は、ユーザープロファイルに表示されます。

![ロンドン旅行とシドニー旅行の2つのネストされたカスタム属性。][1]{: style="max-width:70%;"}

### 予約更新
ユーザが予約を更新する場合、オブジェクトの配列に次の構造を使用して、`/users/track` エンドポイントを介してデータをBraze に送信します。

{% raw %}
```json
{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": {
               "$update:":[
                   {
                       "$identifier_key":"trip_id",
                       "$identifier_value":"1",
                       "$new_object":{"trip_id":"1","name":"London Trip","start_date":{"$time":"2025-11-11"}}
                   }
               ]
           }
       }
 ]
}
```
{% endraw %}

### 予約の削除

{% tabs %}
{% tab ユーザー/トラックエンドポイント %}
#### `/users/track` エンドポイント経由でデータを送信する
ユーザが予約を削除する場合、オブジェクトの配列に次の構造を使用して、`/users/track` エンドポイントを介してBraze にデータを送信します。

{% raw %}
```json

{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": {
               "$remove:":[
                   {
                       "$identifier_key":"trip_id",
                       "$identifier_value": "1"
                   }
               ]
           }
       }
   ]
}
```
{% endraw %}
{% endtab %}
{% tab SDK %}
#### ネストされた属性をSDK 経由でユーザープロファイルに書き込みます

アプリ、ウェブサイト、またはその両方で予約を収集し、そのデータをユーザープロファイルに直接書き込む場合は、Braze SDK を使用してこのデータを送信できます。Web SDK の使用例を次に示します。

{% raw %}
```json
const json = [{
  "id": 1,
  "name": "London Trip",
  "start_date": {"$time”: “2025-05-08”}
}, {
  "id": 1,
  "name": "Sydney Trip",
  "start_date": {"$time”: “2025-11-11”}
}];
braze.getUser().setCustomUserAttribute("trips", json);
```
{% endraw %}
{% endtab %}
{% endtabs %}

指定した予約は、ユーザプロファイルのネストされたカスタム属性から削除され、残りの予約が表示されます。

![London trip.]({% image_buster /assets/img/use_cases/1_nested_attribute.png %})のネストされたカスタム属性{: style="max-width:70%;"}

## ステップ2: 予約リマインダーメッセージを設定して起動する {#step-2}

### ステップ 2a: ターゲットオーディエンスを作成する
複数条件セグメンテーションを使用してリマインダーを受信するターゲットオーディエンスを作成します。たとえば、予約日の2 日前にリマインダーを送信する場合は、次のように選択します。

- 開始日**が1日以上**で
- 開始日**2日以内** 

![ネストされたカスタム属性"trips" 開始日が1 日以上2 日未満の条件付き。][3]

### ステップ 2b: メッセージを作成する

[カスタムHTML]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/)を使用したメールの作成の手順に従って、リマインダーメールメッセージを作成します。この例のように、Liquid を使用して、作成したカスタム顧客属性("trips") のデータでメッセージをパーソナライズします。

{% raw %}
```liquid
{% assign dates = {{custom_attribute.${trips}}} %}
{% assign today = "now" | date: "%s" %}
{% assign two_days = today | plus: 172800 | date: "%F" %}
You have the following booked in 2 days! Check the information below:
{% for date in dates %}
{% if date.start_date == two_days %}
{{date.trip_id}} 
{{date.name}}
{% endif %}
{% endfor %}
```
{% endraw %}

### ステップ 2c: キャンペーンを起動する

リマインダーメールメッセージのキャンペーンを起動します。これで、Brazeが「trips」カスタム属性を受信するたびに、各予約のオブジェクトに含まれるデータに従ってメッセージがスケジュールされます。

## ステップ 3:更新された予約更新とキャンセルの処理 {#step-3}

リマインダーメッセージを送信しているので、予約が更新またはキャンセルされたときに送信する確認メッセージを設定できます。

### ステップ 3a: 更新データの送信

{% tabs %}
{% tab /ユーザー/トラック %}

#### `/users/track` エンドポイント経由でデータを送信する
ユーザが予約を更新またはキャンセルしたときにカスタムイベントを送信するには、ブレーズ[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) エンドポイントを使用します。その場合は、必要なデータを変更を確認するイベント・プロパティーに入れます。 

このユースケースでは、ユーザーがシドニーへの旅行日を更新したとします。イベントは次のようになります。

{% raw %}
```json
{
  "events": [
    {
      "external_id": "user_id",
      "name": "trip_updated",
      "time": "2025-03-07T08:19:23+01:00",
      "properties": {
        "id": 2,
        "name": "Sydney Trip",
        "old_time": "2025-11-12"
        "new_time": "2026-01-21"
      }
    }
  ]
}
```
{% endraw %}
{% endtab %}
{% tab SDK %}

#### ネストされた属性をSDK 経由でユーザープロファイルに書き込みます

SDK を使用してカスタムイベントをユーザープロファイルに送信します。たとえば、Web SDK を使用している場合、以下を送信できます。

{% raw %}
```json
braze.logCustomEvent("trip_updated", { 
  id: 2,
  name: "Sydney Trip",
  old_time: "2025-11-12",
  new_time: "2026-01-21"
});
```
{% endraw %}
{% endtab %}
{% endtabs %}

### ステップ 3b： 更新を確認するメッセージを作成する

[action-based campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) を作成し、更新された予約の確認をユーザに送信します。[Liquidを使用して、予約の名前、古い時刻、新しい時刻(キャンセルの場合は名前のみ)をメッセージ自体に反映するイベントプロパティ]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)をテンプレート化することができます。

たとえば、次のメッセージを作成できます。

{% raw %}
```liquid
Hi {{${first_name}}}, you have successfully updated the date of your trip, {{event_properties.${name}}}, from {{event_properties.${old_time}}} to {{event_properties.${new_time}}}
```
{% endraw %}

### ステップ 3c: 更新を反映するようにユーザープロファイルを変更します

最後に、最新のデータに基づいてステップ1および2から予約リマインダーを送信するには、ネストされたカスタム属性を更新して、予約の変更またはキャンセルを反映します。

#### 予約更新

このユースケースのユーザがシドニー旅行を更新した場合、`/users/track` エンドポイントを使用して、以下のようなコールで日付を変更します。

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "trips": {
	  "$update": [
	    {
            "$identifier_key": "id",
            "$identifier_value": 2,
            "$new_object": {
              "start_date": "2026-01-21"
            }
          }
        ]
      }
    }
  ]
}
```
{% endraw %}

#### 予約取消

このユースケースのユーザがSyndey トリップをキャンセルした場合、`/users/track` エンドポイントに次のコールを送信します。

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "trips": {
	  "$remove": [
	   {
            "$identifier_key": "id",
            "$identifier_value": 2
          }
         ]
      }
    }
  ]
}
```
{% endraw %}

これらのコールが送信され、ユーザプロファイルが更新された後、予約リマインダメッセージには、ユーザの予約日に関する最新のデータが反映されます。

[1]: {% image_buster /assets/img/use_cases/2_nested_attributes.png %}
[3]: {% image_buster /assets/img/use_cases/custom_nested_attribute.png %}