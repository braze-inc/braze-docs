---
nav_title: Currentsイベント変更履歴
page_order: 6
description: "このページには、各Currentsリリースのイベント変更点が含まれている。"
tool: Currents
---

# Currentsの変更履歴

## バージョン6の変更点（リリース日：2026年3月4日）

### 保管に関する変更

* フィールドがイベントタイプに変更される`agentconsole.AgentExecuted`：
    * 新しい`string`フィールド`error`を追加した：エラーの説明

* フィールドがイベントタイプに変更される`agentconsole.ToolInvocation`：
    * 新しい`string`フィールド`request_id`を追加した：このLLMリクエスト全体と完全な実行に対する一意のIDだ。

* フィールドがイベントタイプに変更される`users.messages.rcs.InboundReceive`：
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名

### データ共有の変更

* フィールドがイベントタイプに変更される`agentconsole.AgentExecuted`：
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前
    * 新しい`string`フィールド`error`を追加した：エラー名

* フィールドがイベントタイプに変更される`agentconsole.ToolInvocation`：
    * 新しい`string`フィールド`request_id`を追加した：このLLMリクエスト全体と完全な実行に対する一意のIDだ。

* フィールドがイベントタイプに変更される`users.behaviors.subscription.GlobalStateChange`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.behaviors.subscriptiongroup.StateChange`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.campaigns.Conversion`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`conversion_behavior`を追加した：コンバージョン動作を記述するJSONエンコードされた文字列

* フィールドがイベントタイプに変更される`users.campaigns.EnrollInControl`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名

* フィールドがイベントタイプに変更される`users.canvas.Conversion`：
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前
    * 新しい`string`フィールド`conversion_behavior`を追加した：コンバージョン動作を記述するJSONエンコードされた文字列

* フィールドがイベントタイプに変更される`users.canvas.Entry`：
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.canvas.exit.MatchedAudience`：
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.canvas.exit.PerformedEvent`：
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.canvas.experimentstep.Conversion`：
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前
    * 新しい`string`フィールド`experiment_split_name`を追加した：実験名分割
    * 新しい`string`フィールド`conversion_behavior`を追加した：コンバージョン動作を記述するJSONエンコードされた文字列

* フィールドがイベントタイプに変更される`users.canvas.experimentstep.SplitEntry`：
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前
    * 新しい`string`フィールド`experiment_split_name`を追加した：実験名分割

* フィールドがイベントタイプに変更される`users.canvasstep.Progression`：
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.banner.Abort`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名

* フィールドがイベントタイプに変更される`users.messages.banner.Click`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名

* フィールドがイベントタイプに変更される`users.messages.banner.Impression`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名

* フィールドがイベントタイプに変更される`users.messages.contentcard.Abort`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.contentcard.Click`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.contentcard.Dismiss`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.contentcard.Impression`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.contentcard.Send`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.email.Abort`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.email.Bounce`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.email.Click`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.email.Deferral`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.email.Delivery`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.email.MarkAsSpam`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.email.Open`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.email.Retry`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.email.Send`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.email.SoftBounce`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.email.Unsubscribe`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.featureflag.Impression`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名

* フィールドがイベントタイプに変更される`users.messages.inappmessage.Abort`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.inappmessage.Click`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.inappmessage.Impression`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.line.Retry`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.pushnotification.Abort`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.pushnotification.Bounce`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.pushnotification.InfluencedOpen`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.pushnotification.IosForeground`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.pushnotification.Open`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.pushnotification.Retry`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.pushnotification.Send`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.rcs.InboundReceive`：
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名

* フィールドがイベントタイプに変更される`users.messages.sms.Abort`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.sms.CarrierSend`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.sms.Delivery`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.sms.DeliveryFailure`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.sms.InboundReceive`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.sms.Rejection`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.sms.Retry`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.sms.Send`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.sms.ShortLinkClick`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.webhook.Abort`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.webhook.Failure`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名

* フィールドがイベントタイプに変更される`users.messages.webhook.Retry`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.webhook.Send`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.whatsapp.Abort`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.whatsapp.Click`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.whatsapp.Delivery`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.whatsapp.Failure`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.whatsapp.InboundReceive`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名

* フィールドがイベントタイプに変更される`users.messages.whatsapp.Read`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.whatsapp.Retry`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前

* フィールドがイベントタイプに変更される`users.messages.whatsapp.Send`：
    * 新しい`string`フィールド`campaign_name`を追加した：キャンペーン名
    * 新しい`string`フィールド`canvas_name`を追加した：キャンバスの名前
    * 新しい`string`フィールド`canvas_step_name`を追加した：キャンバスステップの名前
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * 新しい`string`フィールド`message_variation_name`を追加した：メッセージのバリエーション名

## バージョン5の変更点（リリース日：2026年2月4日）

### 保管に関する変更

* 新しいイベントタイプ`agentconsole.AgentExecuted`を追加した。

* 新しいイベントタイプ`agentconsole.ToolInvocation`を追加した。

* 新しいイベントタイプ`users.messages.email.Retry`を追加した。

* 新しいイベントタイプ`users.messages.line.Retry`を追加した。

* 新しいイベントタイプ`users.messages.pushnotification.Retry`を追加した。

* 新しいイベントタイプ`users.messages.sms.Retry`を追加した。

* 新しいイベントタイプ`users.messages.webhook.Retry`を追加した。

* 新しいイベントタイプ`users.messages.whatsapp.Retry`を追加した。

* フィールドがイベントタイプに変更される`users.behaviors.pushnotification.TokenStateChange`：
    * 新しい`long`フィールド`time_ms`を追加した：イベントが発生した時刻（ミリ秒単位）

### データ共有の変更

* 新しいイベントタイプ`agentconsole.AgentExecuted`を追加した。

* 新しいイベントタイプ`agentconsole.ToolInvocation`を追加した。

* 新しいイベントタイプ`users.messages.email.Retry`を追加した。

* 新しいイベントタイプ`users.messages.line.Retry`を追加した。

* 新しいイベントタイプ`users.messages.pushnotification.Retry`を追加した。

* 新しいイベントタイプ`users.messages.sms.Retry`を追加した。

* 新しいイベントタイプ`users.messages.webhook.Retry`を追加した。

* 新しいイベントタイプ`users.messages.whatsapp.Retry`を追加した。

* フィールドがイベントタイプに変更される`users.behaviors.pushnotification.TokenStateChange`：
    * 新しい`long`フィールド`time_ms`を追加した：イベントが発生した時刻（ミリ秒単位）

## バージョン4の変更点（リリース日：2026年1月7日）

### 保管に関する変更

* フィールドがイベントタイプに変更される`users.behaviors.pushnotification.TokenStateChange`：
    * 新しい`string`フィールド`push_token`を追加した：イベントのプッシュトークン

* フィールドがイベントタイプに変更される`users.messages.pushnotification.Bounce`：
    * 新しい`string`フィールド`push_token`を追加した：イベントのプッシュトークン

* フィールドがイベントタイプに変更される`users.messages.pushnotification.Send`：
    * 新しい`string`フィールド`push_token`を追加した：イベントのプッシュトークン

* フィールドがイベントタイプに変更される`users.messages.rcs.Click`：
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * フィールドは現在、*任意*`user_phone_number`*項目*となった。

* フィールドがイベントタイプに変更される`users.messages.rcs.InboundReceive`：
    * フィールドは現在、*任意*`user_id`*項目*となった。

* フィールドがイベントタイプに変更される`users.messages.rcs.Rejection`：
    * 新しい`string`フィールド`canvas_step_message_variation_id`を追加した：このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID

### データ共有の変更

* フィールドがイベントタイプに変更される`users.messages.rcs.Click`：
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * フィールドは現在、*任意*`user_phone_number`*項目*となった。

* フィールドがイベントタイプに変更される`users.messages.rcs.InboundReceive`：
    * フィールドは現在、*任意*`user_id`*項目*となった。

* フィールドがイベントタイプに変更される`users.messages.rcs.Rejection`：
    * 新しい`string`フィールド`canvas_step_message_variation_api_id`を追加した：このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID

## バージョン3の変更点（リリース日：2025年10月8日）

### 保管に関する変更

* 新しいイベントタイプ`users.messages.line.Abort`を追加した。

* 新しいイベントタイプ`users.messages.line.Click`を追加した。

* 新しいイベントタイプ`users.messages.line.InboundReceive`を追加した。

* 新しいイベントタイプ`users.messages.line.Send`を追加した。

* 新しいイベントタイプ`users.messages.rcs.Abort`を追加した。

* 新しいイベントタイプ`users.messages.rcs.Click`を追加した。

* 新しいイベントタイプ`users.messages.rcs.Delivery`を追加した。

* 新しいイベントタイプ`users.messages.rcs.InboundReceive`を追加した。

* 新しいイベントタイプ`users.messages.rcs.Read`を追加した。

* 新しいイベントタイプ`users.messages.rcs.Rejection`を追加した。

* 新しいイベントタイプ`users.messages.rcs.Send`を追加した。

* フィールドがイベントタイプに変更される`users.messages.sms.Delivery`：
    * 新しい`boolean`フィールド`is_sms_fallback`を追加した：RCSメッセージが拒否されたため、SMSフォールバックメッセージが送信されたことを示す。このメッセージは、配信、配信の失敗、または拒否の原因となる場合があります。送信IDとディスパッチIDを介して、RCS拒否イベントにリンクできる。

* フィールドがイベントタイプに変更される`users.messages.sms.DeliveryFailure`：
    * 新しい`boolean`フィールド`is_sms_fallback`を追加した：RCSメッセージが拒否されたため、SMSフォールバックメッセージが送信されたことを示す。このメッセージは、配信、配信の失敗、または拒否の原因となる場合があります。送信IDとディスパッチIDを介して、RCS拒否イベントにリンクできる。

* フィールドがイベントタイプに変更される`users.messages.sms.Rejection`：
    * 新しい`boolean`フィールド`is_sms_fallback`を追加した：RCSメッセージが拒否されたため、SMSフォールバックメッセージが送信されたことを示す。このメッセージは、配信、配信の失敗、または拒否の原因となる場合があります。送信IDと配信IDを介してRCS拒否イベントにリンクできる。(イベントプロパティ)

* フィールドがイベントタイプに変更される`users.messages.whatsapp.Delivery`：
    * 新しい`string`フィールド`flow_id`を追加した：WhatsAppマネージャーにおけるフローの固有ID。メッセージにWhatsApp Flowへの応答を求めるCTAが含まれている場合、表示する。
    * 新しい`string`フィールド`template_name`を追加した：[PII] WhatsAppマネージャー内のテンプレートの名前。テンプレートメッセージを送信する場合に存在させる
    * 新しい`string`フィールド`message_id`を追加した：このメッセージに対してMetaが生成した固有ID

* フィールドがイベントタイプに変更される`users.messages.whatsapp.Failure`：
    * 新しい`string`フィールド`message_id`を追加した：このメッセージに対してMetaが生成した固有ID
    * 新しい`string`フィールド`template_name`を追加した：[PII] WhatsAppマネージャー内のテンプレートの名前。テンプレートメッセージを送信する場合に存在させる
    * 新しい`string`フィールド`flow_id`を追加した：WhatsAppマネージャーにおけるフローの固有ID。メッセージにWhatsApp Flowへの応答を求めるCTAが含まれている場合、表示する。

* フィールドがイベントタイプに変更される`users.messages.whatsapp.InboundReceive`：
    * 新しい`string`フィールド`catalog_id`を追加した：製品がインバウンドメッセージで参照されている場合の製品のカタログ ID。それ以外の場合は、空です。
    * 新しい`string`フィールド`product_id`を追加した：製品がインバウンドメッセージで参照されている場合の製品 SKU。それ以外の場合は、空です。
    * 新しい`string`フィールド`flow_id`を追加した：WhatsAppマネージャーにおけるフローの固有ID。ユーザーがWhatsApp Flowに応答している場合、この条件が成立する。
    * 新しい`string`フィールド`flow_response_json`を追加した：[PII] ユーザーが入力したフォームの値。ユーザーがWhatsApp Flowに応答している場合、この条件が成立する。
    * 新しい`string`フィールド`message_id`を追加した：このメッセージに対してMetaが生成した固有ID
    * 新しい`string`フィールド`in_reply_to`を追加した：このメッセージが返信した返信message_id先のメッセージの件名

* フィールドがイベントタイプに変更される`users.messages.whatsapp.Read`：
    * 新しい`string`フィールド`template_name`を追加した：[PII] WhatsAppマネージャー内のテンプレートの名前。テンプレートメッセージを送信する場合に存在させる
    * 新しい`string`フィールド`message_id`を追加した：このメッセージに対してMetaが生成した固有ID
    * 新しい`string`フィールド`flow_id`を追加した：WhatsAppマネージャーにおけるフローの固有ID。メッセージにWhatsApp Flowへの応答を求めるCTAが含まれている場合、表示する。

* フィールドがイベントタイプに変更される`users.messages.whatsapp.Send`：
    * 新しい`string`フィールド`flow_id`を追加した：WhatsAppマネージャーにおけるフローの固有ID。メッセージにWhatsApp Flowへの応答を求めるCTAが含まれている場合、表示する。
    * 新しい`string`フィールド`template_name`を追加した：[PII] WhatsApp Manager内のテンプレートの名前。テンプレートメッセージを送信する場合に存在させる
    * 新しい`string`フィールド`message_id`を追加した：このメッセージに対してMetaが生成した固有ID

### データ共有の変更

* 新しいイベントタイプ`users.messages.line.Abort`を追加した。

* 新しいイベントタイプ`users.messages.line.Click`を追加した。

* 新しいイベントタイプ`users.messages.line.InboundReceive`を追加した。

* 新しいイベントタイプ`users.messages.line.Send`を追加した。

* 新しいイベントタイプ`users.messages.rcs.Abort`を追加した。

* 新しいイベントタイプ`users.messages.rcs.Click`を追加した。

* 新しいイベントタイプ`users.messages.rcs.Delivery`を追加した。

* 新しいイベントタイプ`users.messages.rcs.InboundReceive`を追加した。

* 新しいイベントタイプ`users.messages.rcs.Read`を追加した。

* 新しいイベントタイプ`users.messages.rcs.Rejection`を追加した。

* 新しいイベントタイプ`users.messages.rcs.Send`を追加した。

* フィールドがイベントタイプに変更される`users.messages.sms.Delivery`：
    * 新しい`boolean`フィールド`is_sms_fallback`を追加した：この拒否されたRCSメッセージに対してSMSフォールバックが試行されたかどうかを示す。SMS配信イベントと連動している。

* フィールドがイベントタイプに変更される`users.messages.sms.DeliveryFailure`：
    * 新しい`boolean`フィールド`is_sms_fallback`を追加した：この拒否されたRCSメッセージに対してSMSフォールバックが試行されたかどうかを示す。SMS配信イベントと連動している。

* フィールドがイベントタイプに変更される`users.messages.sms.Rejection`：
    * 新しい`boolean`フィールド`is_sms_fallback`を追加した：この拒否されたRCSメッセージに対してSMSフォールバックが試行されたかどうかを示す。SMS配信イベントと連動している。

* フィールドがイベントタイプに変更される`users.messages.whatsapp.Delivery`：
    * 新しい`string`フィールド`flow_id`を追加した：WhatsAppマネージャーにおけるフローの固有ID。ユーザーがWhatsApp Flowに応答している場合、この条件が成立する。
    * 新しい`string`フィールド`template_name`を追加した：[PII] WhatsAppマネージャー内のテンプレートの名前。テンプレートメッセージを送信する場合に存在させる
    * 新しい`string`フィールド`message_id`を追加した：このメッセージに対してMetaが生成した固有ID

* フィールドがイベントタイプに変更される`users.messages.whatsapp.Failure`：
    * 新しい`string`フィールド`message_id`を追加した：このメッセージに対してMetaが生成した固有ID
    * 新しい`string`フィールド`template_name`を追加した：[PII] WhatsAppマネージャー内のテンプレートの名前。テンプレートメッセージを送信する場合に存在させる
    * 新しい`string`フィールド`flow_id`を追加した：WhatsAppマネージャーにおけるフローの固有ID。ユーザーがWhatsApp Flowに応答している場合、この条件が成立する。

* フィールドがイベントタイプに変更される`users.messages.whatsapp.InboundReceive`：
    * 新しい`string`フィールド`catalog_id`を追加した：製品がインバウンドメッセージで参照されている場合の製品のカタログ ID。それ以外の場合は、空です。
    * 新しい`string`フィールド`product_id`を追加した：購入した製品のID
    * 新しい`string`フィールド`flow_id`を追加した：WhatsAppマネージャーにおけるフローの固有ID。ユーザーがWhatsApp Flowに応答している場合、この条件が成立する。
    * 新しい`string`フィールド`flow_response_json`を追加した：[PII] ユーザーが入力したフォームの値。ユーザーがWhatsApp Flowに応答している場合、この条件が成立する。
    * 新しい`string`フィールド`message_id`を追加した：このメッセージに対してMetaが生成した固有ID
    * 新しい`string`フィールド`in_reply_to`を追加した：このメッセージが返信した返信message_id先のメッセージの件名

* フィールドがイベントタイプに変更される`users.messages.whatsapp.Read`：
    * 新しい`string`フィールド`template_name`を追加した：[PII] WhatsAppマネージャー内のテンプレートの名前。テンプレートメッセージを送信する場合に存在させる
    * 新しい`string`フィールド`message_id`を追加した：このメッセージに対してMetaが生成した固有ID
    * 新しい`string`フィールド`flow_id`を追加した：WhatsAppマネージャーにおけるフローの固有ID。ユーザーがWhatsApp Flowに応答している場合、この条件が成立する。

* フィールドがイベントタイプに変更される`users.messages.whatsapp.Send`：
    * 新しい`string`フィールド`flow_id`を追加した：WhatsAppマネージャーにおけるフローの固有ID。ユーザーがWhatsApp Flowに応答している場合、この条件が成立する。
    * 新しい`string`フィールド`template_name`を追加した：[PII] WhatsAppマネージャー内のテンプレートの名前。テンプレートメッセージを送信する場合に存在させる
    * 新しい`string`フィールド`message_id`を追加した：このメッセージに対してMetaが生成した固有ID

## バージョン2の変更点（リリース日なし）

### 保管に関する変更

* 新しいイベントタイプ`users.behaviors.app.FirstSession`を追加した。

* 新しいイベントタイプ`users.behaviors.app.SessionEnd`を追加した。

* 新しいイベントタイプ`users.behaviors.app.SessionStart`を追加した。

* 新しいイベントタイプ`users.behaviors.CustomEvent`を追加した。

* 新しいイベントタイプ`users.behaviors.InstallAttribution`を追加した。

* 新しいイベントタイプ`users.behaviors.liveactivity.PushToStartTokenChange`を追加した。

* 新しいイベントタイプ`users.behaviors.liveactivity.UpdateTokenChange`を追加した。

* 新しいイベントタイプ`users.behaviors.Location`を追加した。

* 新しいイベントタイプ`users.behaviors.Purchase`を追加した。

* 新しいイベントタイプ`users.behaviors.pushnotification.TokenStateChange`を追加した。

* 新しいイベントタイプ`users.behaviors.subscription.GlobalStateChange`を追加した。

* 新しいイベントタイプ`users.behaviors.subscriptiongroup.StateChange`を追加した。

* 新しいイベントタイプ`users.behaviors.Uninstall`を追加した。

* 新しいイベントタイプ`users.campaigns.Conversion`を追加した。

* 新しいイベントタイプ`users.campaigns.EnrollInControl`を追加した。

* 新しいイベントタイプ`users.canvas.Conversion`を追加した。

* 新しいイベントタイプ`users.canvas.Entry`を追加した。

* 新しいイベントタイプ`users.canvas.exit.MatchedAudience`を追加した。

* 新しいイベントタイプ`users.canvas.exit.PerformedEvent`を追加した。

* 新しいイベントタイプ`users.canvas.experimentstep.Conversion`を追加した。

* 新しいイベントタイプ`users.canvas.experimentstep.SplitEntry`を追加した。

* 新しいイベントタイプ`users.canvasstep.Progression`を追加した。

* 新しいイベントタイプ`users.messages.banner.Abort`を追加した。

* 新しいイベントタイプ`users.messages.banner.Click`を追加した。

* 新しいイベントタイプ`users.messages.banner.Impression`を追加した。

* 新しいイベントタイプ`users.messages.contentcard.Abort`を追加した。

* 新しいイベントタイプ`users.messages.contentcard.Click`を追加した。

* 新しいイベントタイプ`users.messages.contentcard.Dismiss`を追加した。

* 新しいイベントタイプ`users.messages.contentcard.Impression`を追加した。

* 新しいイベントタイプ`users.messages.contentcard.Send`を追加した。

* 新しいイベントタイプ`users.messages.email.Abort`を追加した。

* 新しいイベントタイプ`users.messages.email.Bounce`を追加した。

* 新しいイベントタイプ`users.messages.email.Click`を追加した。

* 新しいイベントタイプ`users.messages.email.Deferral`を追加した。

* 新しいイベントタイプ`users.messages.email.Delivery`を追加した。

* 新しいイベントタイプ`users.messages.email.MarkAsSpam`を追加した。

* 新しいイベントタイプ`users.messages.email.Open`を追加した。

* 新しいイベントタイプ`users.messages.email.Send`を追加した。

* 新しいイベントタイプ`users.messages.email.SoftBounce`を追加した。

* 新しいイベントタイプ`users.messages.email.Unsubscribe`を追加した。

* 新しいイベントタイプ`users.messages.featureflag.Impression`を追加した。

* 新しいイベントタイプ`users.messages.inappmessage.Abort`を追加した。

* 新しいイベントタイプ`users.messages.inappmessage.Click`を追加した。

* 新しいイベントタイプ`users.messages.inappmessage.Impression`を追加した。

* 新しいイベントタイプ`users.messages.liveactivity.Outcome`を追加した。

* 新しいイベントタイプ`users.messages.liveactivity.Send`を追加した。

* 新しいイベントタイプ`users.messages.pushnotification.Abort`を追加した。

* 新しいイベントタイプ`users.messages.pushnotification.Bounce`を追加した。

* 新しいイベントタイプ`users.messages.pushnotification.IosForeground`を追加した。

* 新しいイベントタイプ`users.messages.pushnotification.Open`を追加した。

* 新しいイベントタイプ`users.messages.pushnotification.Send`を追加した。

* 新しいイベントタイプ`users.messages.sms.Abort`を追加した。

* 新しいイベントタイプ`users.messages.sms.CarrierSend`を追加した。

* 新しいイベントタイプ`users.messages.sms.Delivery`を追加した。

* 新しいイベントタイプ`users.messages.sms.DeliveryFailure`を追加した。

* 新しいイベントタイプ`users.messages.sms.InboundReceive`を追加した。

* 新しいイベントタイプ`users.messages.sms.Rejection`を追加した。

* 新しいイベントタイプ`users.messages.sms.Send`を追加した。

* 新しいイベントタイプ`users.messages.sms.ShortLinkClick`を追加した。

* 新しいイベントタイプ`users.messages.webhook.Abort`を追加した。

* 新しいイベントタイプ`users.messages.webhook.Failure`を追加した。

* 新しいイベントタイプ`users.messages.webhook.Send`を追加した。

* 新しいイベントタイプ`users.messages.whatsapp.Abort`を追加した。

* 新しいイベントタイプ`users.messages.whatsapp.Click`を追加した。

* 新しいイベントタイプ`users.messages.whatsapp.Delivery`を追加した。

* 新しいイベントタイプ`users.messages.whatsapp.Failure`を追加した。

* 新しいイベントタイプ`users.messages.whatsapp.InboundReceive`を追加した。

* 新しいイベントタイプ`users.messages.whatsapp.Read`を追加した。

* 新しいイベントタイプ`users.messages.whatsapp.Send`を追加した。

* 新しいイベントタイプ`users.RandomBucketNumberUpdate`を追加した。

### データ共有の変更

* 新しいイベントタイプ`changelogs.GlobalControlGroup`を追加した。

* 新しいイベントタイプ`users.behaviors.app.FirstSession`を追加した。

* 新しいイベントタイプ`users.behaviors.app.NewsFeedImpression`を追加した。

* 新しいイベントタイプ`users.behaviors.app.SessionEnd`を追加した。

* 新しいイベントタイプ`users.behaviors.app.SessionStart`を追加した。

* 新しいイベントタイプ`users.behaviors.CustomEvent`を追加した。

* 新しいイベントタイプ`users.behaviors.geofence.DataEvent`を追加した。

* 新しいイベントタイプ`users.behaviors.geofence.RecordEvent`を追加した。

* 新しいイベントタイプ`users.behaviors.InstallAttribution`を追加した。

* 新しいイベントタイプ`users.behaviors.liveactivity.PushToStartTokenChange`を追加した。

* 新しいイベントタイプ`users.behaviors.liveactivity.UpdateTokenChange`を追加した。

* 新しいイベントタイプ`users.behaviors.Location`を追加した。

* 新しいイベントタイプ`users.behaviors.Purchase`を追加した。

* 新しいイベントタイプ`users.behaviors.pushnotification.TokenStateChange`を追加した。

* 新しいイベントタイプ`users.behaviors.subscription.GlobalStateChange`を追加した。

* 新しいイベントタイプ`users.behaviors.subscriptiongroup.StateChange`を追加した。

* 新しいイベントタイプ`users.behaviors.Uninstall`を追加した。

* 新しいイベントタイプ`users.behaviors.UpgradedApp`を追加した。

* 新しいイベントタイプ`users.campaigns.Conversion`を追加した。

* 新しいイベントタイプ`users.campaigns.EnrollInControl`を追加した。

* 新しいイベントタイプ`users.campaigns.FrequencyCap`を追加した。

* 新しいイベントタイプ`users.campaigns.Revenue`を追加した。

* 新しいイベントタイプ`users.canvas.Conversion`を追加した。

* 新しいイベントタイプ`users.canvas.Entry`を追加した。

* 新しいイベントタイプ`users.canvas.exit.MatchedAudience`を追加した。

* 新しいイベントタイプ`users.canvas.exit.PerformedEvent`を追加した。

* 新しいイベントタイプ`users.canvas.experimentstep.Conversion`を追加した。

* 新しいイベントタイプ`users.canvas.experimentstep.SplitEntry`を追加した。

* 新しいイベントタイプ`users.canvas.FrequencyCap`を追加した。

* 新しいイベントタイプ`users.canvas.Revenue`を追加した。

* 新しいイベントタイプ`users.canvasstep.Progression`を追加した。

* 新しいイベントタイプ`users.messages.banner.Abort`を追加した。

* 新しいイベントタイプ`users.messages.banner.Click`を追加した。

* 新しいイベントタイプ`users.messages.banner.Impression`を追加した。

* 新しいイベントタイプ`users.messages.contentcard.Abort`を追加した。

* 新しいイベントタイプ`users.messages.contentcard.Click`を追加した。

* 新しいイベントタイプ`users.messages.contentcard.Dismiss`を追加した。

* 新しいイベントタイプ`users.messages.contentcard.Impression`を追加した。

* 新しいイベントタイプ`users.messages.contentcard.Send`を追加した。

* 新しいイベントタイプ`users.messages.email.Abort`を追加した。

* 新しいイベントタイプ`users.messages.email.Bounce`を追加した。

* 新しいイベントタイプ`users.messages.email.Click`を追加した。

* 新しいイベントタイプ`users.messages.email.Deferral`を追加した。

* 新しいイベントタイプ`users.messages.email.Delivery`を追加した。

* 新しいイベントタイプ`users.messages.email.MarkAsSpam`を追加した。

* 新しいイベントタイプ`users.messages.email.Open`を追加した。

* 新しいイベントタイプ`users.messages.email.Send`を追加した。

* 新しいイベントタイプ`users.messages.email.SoftBounce`を追加した。

* 新しいイベントタイプ`users.messages.email.Unsubscribe`を追加した。

* 新しいイベントタイプ`users.messages.featureflag.Impression`を追加した。

* 新しいイベントタイプ`users.messages.inappmessage.Abort`を追加した。

* 新しいイベントタイプ`users.messages.inappmessage.Click`を追加した。

* 新しいイベントタイプ`users.messages.inappmessage.Impression`を追加した。

* 新しいイベントタイプ`users.messages.liveactivity.Outcome`を追加した。

* 新しいイベントタイプ`users.messages.liveactivity.Send`を追加した。

* 新しいイベントタイプ`users.messages.newsfeedcard.Abort`を追加した。

* 新しいイベントタイプ`users.messages.newsfeedcard.Click`を追加した。

* 新しいイベントタイプ`users.messages.newsfeedcard.Impression`を追加した。

* 新しいイベントタイプ`users.messages.pushnotification.Abort`を追加した。

* 新しいイベントタイプ`users.messages.pushnotification.Bounce`を追加した。

* 新しいイベントタイプ`users.messages.pushnotification.InfluencedOpen`を追加した。

* 新しいイベントタイプ`users.messages.pushnotification.IosForeground`を追加した。

* 新しいイベントタイプ`users.messages.pushnotification.Open`を追加した。

* 新しいイベントタイプ`users.messages.pushnotification.Send`を追加した。

* 新しいイベントタイプ`users.messages.sms.Abort`を追加した。

* 新しいイベントタイプ`users.messages.sms.CarrierSend`を追加した。

* 新しいイベントタイプ`users.messages.sms.Delivery`を追加した。

* 新しいイベントタイプ`users.messages.sms.DeliveryFailure`を追加した。

* 新しいイベントタイプ`users.messages.sms.InboundReceive`を追加した。

* 新しいイベントタイプ`users.messages.sms.Rejection`を追加した。

* 新しいイベントタイプ`users.messages.sms.Send`を追加した。

* 新しいイベントタイプ`users.messages.sms.ShortLinkClick`を追加した。

* 新しいイベントタイプ`users.messages.webhook.Abort`を追加した。

* 新しいイベントタイプ`users.messages.webhook.Failure`を追加した。

* 新しいイベントタイプ`users.messages.webhook.Send`を追加した。

* 新しいイベントタイプ`users.messages.whatsapp.Abort`を追加した。

* 新しいイベントタイプ`users.messages.whatsapp.Click`を追加した。

* 新しいイベントタイプ`users.messages.whatsapp.Delivery`を追加した。

* 新しいイベントタイプ`users.messages.whatsapp.Failure`を追加した。

* 新しいイベントタイプ`users.messages.whatsapp.InboundReceive`を追加した。

* 新しいイベントタイプ`users.messages.whatsapp.Read`を追加した。

* 新しいイベントタイプ`users.messages.whatsapp.Send`を追加した。

* 新しいイベントタイプ`users.RandomBucketNumberUpdate`を追加した。

* 新しいイベントタイプ`users.UserDeleteRequest`を追加した。

* 新しいイベントタイプ`users.UserOrphan`を追加した。
