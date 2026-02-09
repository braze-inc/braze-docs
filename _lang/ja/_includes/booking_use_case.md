# ユースケース:予約リマインダーメールシステム

> Braze は、プログラムで高度に制御できるように設計された包括的なカスタマーエンゲージメントプラットフォームです。このユースケースでは、予約システムなど、製品とマーケティングが交わる地点のユースケースに適用可能な、Braze が提供する機能の使用方法をいくつかご紹介します。

このユースケースでは、Braze の機能を使用して予約リマインダーメールメッセージングサービスを構築する方法をご紹介します。このサービスを使用すると、ユーザーは予定を予約することができます。また、次回の予定のリマインダーが記載されたメッセージがユーザーに送信されます。このユースケースではメールメッセージが使用されますが、ユーザープロファイルを一度更新すれば、任意のチャネルまたは複数のチャネルでメッセージを送信できます。

このサービスを作成するその他の利点は次のとおりです。
- 送信されたメッセージは完全に追跡され、レポートに含まれます。
- 技術者でないBrazeユーザーでもメッセージ内容を更新できる。
- メッセージは、キャンペーン設定ごとのユーザープロファイルのオプトインおよびオプトアウトステータスに従います。
- 予約データとメッセージ・インタラクション・データの両方を使用して、ユーザーをセグメンテーションし、ターゲットを絞って追加メッセージを送ることができる。例えば、最初のリマインダーメッセージを開封しなかった人に、アポイントメントの前に追加のリマインダーでリターゲティングすることができる。

このユースケースを実現するには、次のステップを実行します。
1. [次の予約データを Braze ユーザープロファイルに書き込む](#step-1)
2. [予約リマインダーメッセージを設定して開始する](#step-2)
3. [更新された予約とキャンセルを処理する](#step-3)

## ステップ1:次の予約データを Braze ユーザープロファイルに書き込む {#step-1}

予約が行われるたびに、Braze [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) エンドポイントを使用して、[階層化カスタム属性]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/)をユーザープロファイルに書き込みます。階層化されたカスタム属性に、リマインダーメッセージの送信とパーソナライゼーションに必要なすべての情報が含まれていることを確認する。このユースケースでは、階層化カスタム属性に「trips」という名前を付けます。

### 予約の追加

ユーザーが予約を作成する場合、オブジェクトの配列に次の構造を使用して、`/users/track` エンドポイントを介してデータを Braze に送信します。

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

階層化カスタム属性「trips」は、ユーザープロファイルに表示されます。

![ロンドン旅行とシドニー旅行の2つの階層化カスタム属性。]({% image_buster /assets/img/use_cases/2_nested_attributes.png %}){: style="max-width:70%;"}

### 予約の更新
ユーザーが予約を更新する場合、オブジェクトの配列に次の構造を使用して、`/users/track` エンドポイントを介してデータを Braze に送信します。

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
{% tab /users/track endpoint %}
#### `/users/track` エンドポイント経由でデータを送信する
ユーザーが予約を削除する場合、オブジェクトの配列に次の構造を使用して、`/users/track` エンドポイントを介して Braze にデータを送信します。

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
#### 階層化された属性を SDK 経由でユーザープロファイルに書き込む

アプリ、Web サイト、またはその両方で予約を収集し、そのデータをユーザープロファイルに直接書き込む場合は、Braze SDK を使用してこのデータを送信できます。Web SDK の使用例を次に示します。

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

Brazeは、ユーザープロファイルの階層化カスタム属性から指定された予約を削除し、残りの予約を表示する。

![ロンドン旅行の階層化カスタム属性。]({% image_buster /assets/img/use_cases/1_nested_attribute.png %}){: style="max-width:70%;"}

## ステップ 2:予約リマインダーメッセージを設定して開始する {#step-2}

### ステップ 2a: ターゲットオーディエンスを作成する
複数条件のセグメンテーションを使用してリマインダーを受信するターゲットオーディエンスを作成します。例えば、予約日の2日前にリマインダーを送信する場合は、次のように選択します。

- 開始日まで**1日超**かつ
- 開始日まで**2日以内** 

![階層化されたカスタム属性 "trips "は、開始日が1日以上2日未満であることを条件とする。]({% image_buster /assets/img/use_cases/custom_nested_attribute.png %})

### ステップ 2b: メッセージを作成する

[カスタム HTML]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/) を使用したメール作成のステップに従って、リマインダーメールメッセージを作成します。この例のように、Liquid を使用して、作成したカスタム顧客属性 (「trips」) のデータでメッセージをパーソナライズします。

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

### ステップ 2c: キャンペーンを開始する

リマインダーメールメッセージのキャンペーンを開始します。これで、Brazeが "trips "カスタム属性を受信するたびに、Brazeはそれぞれの予約のオブジェクトに含まれるデータに従ってメッセージをスケジュールされる。

## ステップ 3:更新された予約とキャンセルを処理する {#step-3}

リマインダーメッセージを送信しているため、予約が更新またはキャンセルされたときに送信する確認メッセージを設定できます。

### ステップ 3a: 更新データの送信

{% tabs %}
{% tab /users/track %}

#### `/users/track` エンドポイント経由でデータを送信する
ユーザーが予約を更新またはキャンセルしたときにカスタムイベントを送信するには、Braze [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) エンドポイントを使用します。このイベントには、変更を確認するイベントプロパティーに必要なデータを含めます。 

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

#### 階層化された属性を SDK 経由でユーザープロファイルに書き込む

SDK を使用してカスタムイベントをユーザープロファイルに送信します。例えば、Web SDK を使用している場合、以下を送信できます。

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

[アクションベースのキャンペーン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/)を作成し、更新された予約の確認をユーザーに送信します。[Liquid を使用してイベントプロパティをテンプレート化することができます]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)。これを使用すると、予約の名前、以前の時刻、新しい時刻 (キャンセルの場合は名前のみ) をメッセージ自体に反映できます。

例えば、次のメッセージを作成できます。

{% raw %}
```liquid
Hi {{${first_name}}}, you have successfully updated the date of your trip, {{event_properties.${name}}}, from {{event_properties.${old_time}}} to {{event_properties.${new_time}}}
```
{% endraw %}

### ステップ 3c: 更新を反映するようにユーザープロファイルを変更する

最後に、最新のデータに基づいてステップ1および2から予約リマインダーを送信するために、階層化カスタム属性を更新して、予約の変更またはキャンセルを反映します。

#### 予約の更新

このユースケースのユーザーがシドニー旅行を更新した場合、`/users/track` エンドポイントを使用して、以下のようなコールで日付を変更します。

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

#### 予約のキャンセル

このユースケースのユーザーがシドニー旅行をキャンセルした場合、`/users/track` エンドポイントに次のようなコールを送ることになる：

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

これらのコールが送信され、ユーザープロファイルが更新されると、予約リマインダメッセージにユーザーの予約日に関する最新のデータが反映されます。

