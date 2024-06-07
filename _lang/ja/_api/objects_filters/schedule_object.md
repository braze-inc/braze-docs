---
nav_title: "スケジュール対象"
article_title: APIスケジュールオブジェクト
page_order: 12
page_type: reference
description: "このリファレンスでは、Brazeで使用されている様々なスケジューリングオブジェクトをリストアップし、解説しています。"

---

# スケジュールオブジェクト

> キャンペーンとキャンバスのスケジュール作成エンドポイントのパラメータは、送信エンドポイントのパラメータを反映し、ターゲットユーザーにいつメッセージを受信させたいかを指定できる`schedule` パラメータを追加します。`schedule` オブジェクトに`time` パラメータだけを含めると、その時点ですべてのユーザーにメッセージが送られます。

`in_local_time` を`true` に設定した場合、time パラメーターがすべてのタイムゾーンでパスした場合、エラー応答が返される。`at_optimal_time` 」を「true」に設定すると、ユーザーは指定された日付の[最適な][33]時間にメッセージを受け取ります（あなたが指定した時間に関係なく）。ローカル時間または最適時間送信を使用する場合、時間パラメータの値にタイムゾーン指定を指定しないでください（例えば、`"2015-02-20T13:14:47-05:00"` の代わりに`"2015-02-20T13:14:47"` を指定してください）。

この応答は`schedule_id` を提供します。後で予約したメッセージをキャンセルまたは更新する必要がある場合に備えて保存しておいてください：

## オブジェクト本体

このオブジェクトを必要に応じて挿入し、メッセージのスケジューリングを行います。

```json
"schedule": {
  "time": (required, datetime as ISO 8601 string) time to send the message,
  "in_local_time": (optional, bool),
  "at_optimal_time": (optional, bool),
}
```

## スケジュール ID レスポンス

作成したスケジュールメッセージの`schedule_id` 。

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "schedule_id" : (required, string) identifier for the scheduled message that was created
}
```

サーバー間の呼び出しにAPIを使用する場合、サーバーがファイアウォールの内側にある場合は、適切なAPI URLをallowlistする必要があるかもしれない。

メッセージ・スケジューリング・エンドポイントのレスポンスには、メッセージのディスパッチに参照できるように、メッセージの`dispatch_id` が含まれます。`dispatch_id` はメッセージ発信のID（Brazeから送信される「送信」ごとにユニークなID）。

[33]: {{site.baseurl}}/user_guide/sage_ai/intelligence/intelligent_timing/
