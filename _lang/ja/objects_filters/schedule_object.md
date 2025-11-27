---
nav_title: "Scheduleオブジェクト"
article_title: APIスケジュールオブジェクト
page_order: 12
page_type: reference
description: "この参考記事では、Brazeで使用されているさまざまなスケジューリングオブジェクトをリストアップし、解説している。"

---

# Scheduleオブジェクト

> キャンペーンとキャンバスのスケジュール作成エンドポイントのパラメータは、送信エンドポイントのパラメータを反映し、ターゲットユーザーにいつメッセージを受信させたいかを指定できる`schedule` パラメータを追加する。`schedule` オブジェクトに`time` パラメータだけを含めると、Brazeはその時点ですべてのユーザーにメッセージングを行う。

`in_local_time` を`true` に設定した場合、すべてのタイムゾーンでtimeパラメータがパスした場合、エラー・レスポンスが返ってくる。`at_optimal_time` をtrueに設定すると、ユーザーは指定した日付の最適な時間にメッセージを受け取る（あなたが指定した時間に関係なく）。ローカル時間または最適時間送信を使用する場合、時間パラメータの値にタイムゾーン指定子を指定しない（例えば、`"2015-02-20T13:14:47-05:00"` の代わりに`"2015-02-20T13:14:47"` を使用する）。

この応答により `schedule_id` が提供されます。これは、後でスケジュールしたメッセージをキャンセルしたり更新したりする必要がある場合に備えて、保存しておく必要があります。

## オブジェクト本体

このオブジェクトを必要に応じて挿入し、メッセージのスケジューリングを行う。

```json
"schedule": {
  "time": (required, datetime as ISO 8601 string) time to send the message in UTC,
  "in_local_time": (optional, bool),
  "at_optimal_time": (optional, bool),
}
```

## スケジュール ID の応答

作成したスケジュール済みメッセージの `schedule_id` を受け取ります。

```json
{
  "schedule_id" : (required, string) identifier for the scheduled message you created
}
```

サーバー間の呼び出しに API を使用する場合、ファイアウォールの内側にある場合は、適切な API URL を許可リストに追加する必要が生じることがあります。

メッセージスケジューリングエンドポイント応答には、メッセージのディスパッチを参照できるように、メッセージの `dispatch_id` が含まれます。`dispatch_id` は、メッセージディスパッチの ID です (Braze から送信される「送信」ごとに固有の ID）。

