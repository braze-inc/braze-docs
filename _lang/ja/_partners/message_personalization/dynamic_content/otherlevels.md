---
nav_title: その他のレベル
article_title: その他のレベル
alias: /partners/otherlevels/
description: "この記事では、OtherLevels Experience PlatformとBrazeの統合について説明する。"
page_type: partner
search_tag: OtherLevels

---

# その他のレベル

> [OtherLevels](https://www.otherlevels.com/)エクスペリエンス・プラットフォームは、GenAIを使用して、従来のコンテンツをオンブランドのパーソナライズされた動画やリッチメディア体験に変換することで、スポーツブランド、パブリッシャー、オペレーターがカスタマーエクスペリエンスとつながる方法を変革する。

*この統合はOtherLevelsによって維持されている。*

## 概要

BrazeとOtherLevelsの統合により、OtherLevelsエクスペリエンスプラットフォームへのAPIコールを通じてカスタムGenAI動画を作成し、[Brazeコネクテッドコンテンツを通じて]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/)これらの動画をiOSプッシュ動画としてユーザーに送信することができる。

OtherLevelsのAIを駆使したエクスペリエンスで、ユーザーにより良い体験を与えよう。既存のコンテンツやサードパーティコンテンツを拡張性の高い動画やリッチメディアに変換し、すでに異なる方法でコンテンツを消費し、文脈に応じたパーソナライズされた体験に強く反応するオーディエンスに提供する。

## 前提条件

開始する前に、次のものが必要になります。

| 前提条件          | 説明                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| OtherLevelsアカウント   | このパートナーシップを利用するには、OtherLevelsアカウントが必要である。                                                                     |
| Braze REST API キー  | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント | [RESTエンドポイントのURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。お客様のエンドポイントは、お客様のインスタンスのBraze URLに依存します。                                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

このインテグレーションでは、ユーザーにメッセージを送信する前に、動画生成プロセスの一部としてOtherLevels Experience Platform APIを呼び出す必要がある。このドキュメントの一部としてcURLの例が提供されているが、APIコールを自動化するためにPostmanのようなAPIクライアントを使用することを推奨する。

## ユースケース

OtherLevelsエクスペリエンス・プラットフォームで作成されたGenAIの動画を使用する：
- スポーツのオーナーやリーグ、ファンのエンゲージメント、スポーツブック、iGaming、宝くじのために、より良い体験を創造する。
- テキストベースのコンテンツをリッチメディアや動画に変換し、人間的で魅力的なカスタマーエクスペリエンスを創造することで、カスタマーマーケティングを強化する。
- 既存のBraze統合を再構築するのではなく、拡張することで、獲得からリテンションまでの成果を高める。

## OtherLevels Experienceプラットフォームの統合

### ステップ 1: OtherLevels Experience Platform APIを呼び出して動画を生成する。 {#step-1}

統合の最初のステップでは、OtherLevels Experience Platform APIを呼び出して新しい動画を生成する。動画の生成は瞬間的なものではないことに注意してほしい。動画の長さや複雑さにもよるが、コンテンツの生成には30分ほどかかることもある。メッセージングのスケジュールとAPIコールをそれに合わせて計画し、動画を生成するためのAPIコールが、Brazeメッセージの送信スケジュールされたタイミングより十分に前に行われるようにする。

{% alert important %}
以下のリクエストはcURLを使用している。APIリクエストをより効率的に管理するには、PostmanのようなAPIクライアントを使うことをお勧めする。
{% endalert %}

APIコールをどのように構成するかについては、以下の例を参照のこと。動画仕様のカスタマイズやAPIコールの構造についての詳細は、[GenAIの動画をカスタマイズするを](#customizing-the-genai-video)参照のこと。

{% raw %}
```bash
curl --request POST \
  --url 'https://exp-platform-api.prod.awsotherlevels.com/v1/app/OTHERLEVELS_PROJECT_KEY/media?=' \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/10.3.0' \
  --data '{
    "task": {
        "type": "tasks",
        "tasks": {
            "image_video_overlay": {
                "width": "= .orientation == '\''portrait'\'' ? '\''1080'\'' : .orientation == '\''landscape'\'' ? '\''1920'\''",
                "height": "= .orientation == '\''portrait'\'' ? '\''1920'\'' : .orientation == '\''landscape'\'' ? '\''1080'\''",
                "color": "255,255,255,0",
                "y_pos": "0",
                "x_pos": "0",
                "image_input": "= tasks.resize_image.jpg ?? tasks.resize_image.png",
                "video_input": "= tasks.talking_talent_replace_bg.mp4",
                "type": "compose.ImageVideoOverlay"
            },
            "resize_image": {
                "media_input": "= tasks.bg_image.jpg ?? tasks.bg_image.png",
                "type": "compose.MediaResize",
                "width": "= .orientation == '\''portrait'\'' ? '\''1080'\'' : .orientation == '\''landscape'\'' ? '\''1920'\''",
                "height": "= .orientation == '\''portrait'\'' ? '\''1920'\'' : .orientation == '\''landscape'\'' ? '\''1080'\''"
            },
            "bg_image": {
                "type": "load",
                "url": "BACKGROUND_IMAGE_URL",
                "refresh_interval": "12h"
            },
            "talking_head": {
                "test": false,
                "title": "INSERT_TITLE",
                "caption": false,
                "templateId": "TALENT_TEMPLATE",
                "type": "TALENT_MODEL",
                "variables": {
                    "script": {
                        "name": "script",
                        "properties": {
                            "content": "= tasks.translate_text.text"
                        },
                        "type": "text"
                    }
                }
            },
            "translate_text": {
                "type": "translate_text",
                "source": "en",
                "target": "en",
                "text": "INSERT_SCRIPT"
            },
            "talking_talent_speed": {
                "type": "compose.VideoSetSpeed",
                "speed": "1.0",
                "video_input": "= tasks.talking_head.mp4"
            },
            "talking_talent_replace_bg": {
                "type": "compose.VideoReplaceBg",
                "video_background": "= tasks.resize_image.jpg ?? tasks.resize_image.png",
                "video_input": "= tasks.talking_talent_speed.mp4"
            }
        },
        "output": "image_video_overlay"
    }
}'
```
{% endraw %}

次のように置き換えます。

| placeholder          | 説明                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `OTHERLEVELS_PROJECT_KEY`   | OtherLevelsプロジェクト・キーは、OtherLevelsアカウントのプロビジョニング時に提供される。                                                                     |
| `BACKGROUND_IMAGE_URL`  | 動画のバックグラウンド用の HTTPS URL。 |
| `INSERT_TITLE` | 動画のタイトル。これは内部参照であり、動画には表示されない。                                                 |
| `TALENT_TEMPLATE` | タレントテンプレートID。OtherLevelsは、アカウントのプロビジョニング中にあなたと協力してタレント（アバター）を作成する。使用可能な1つまたは複数のタレントIDが提供される。                                                 |
| `TALENT_MODEL` | タレント・モデルID。OtherLevelsは、アカウントのプロビジョニング中にあなたと協力してタレント（アバター）を作成する。使用可能なタレント・モデルが1つまたは複数提供される。                                                 |
| `INSERT_SCRIPT` | 動画の中でタレントに言わせたい正確な台本。                                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

APIレスポンスの一部として、OtherLevelsはAPIコールが成功したことを示すJSONペイロードを返す。JSONには、生成された動画を識別するための一意な`recipe_id` 。`recipe_id` 、次のステップで必要となる。

以下はAPIからのレスポンシブの例である：

{% raw %}
```bash
{"$schema":"https://exp-platform-api.prod.awsotherlevels.com/schemas/GenerateMediaResBody.json","message":"success","recipe_id":"LMINHWXV2BBD6JGV5VF3ZNZV7BDDRR7FH5FJH6MMX4BVLTPRKTWQ","media_short_id":"LMINHWX","status":"triggered"}
```
{% endraw %}

### ステップ 2:`recipe_id` をカスタム属性として設定する。

[ステップ](#step-1)1で受け取った`recipe_id` 、動画を送信したいユーザーのBrazeカスタム属性として設定する。

ユースケースによっては、多くのオーディエンスに向けた1本の動画を作成することもあるだろう。その場合、この同じ`recipe_id` を複数のユーザーに設定することができる。あるいは、それぞれ異なるユーザーをターゲットに複数のユニークな動画を生成している場合もあり、その場合は、各ユーザーにカスタム属性として`recipe_id` を設定する必要がある。

{% alert important %}
以下のリクエストはcURLを使用している。APIリクエストをより効率的に管理するには、PostmanのようなAPIクライアントを使うことをお勧めする。
{% endalert %}

{% raw %}
```bash
curl --location --request POST 'BRAZE_API_ENDPOINT/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer BRAZE_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "USER_ID",
      "olxpmedia": "RECIPE_ID"
    }
  ]
}'
```
{% endraw %}

次のように置き換えます。

| placeholder             | 説明                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_ENDPOINT`    | 現在の Braze インスタンスの Braze REST エンドポイント URL。詳細については、[REST APIキーを]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys)参照のこと。 |
| `BRAZE_API_KEY`         | `users.track` 権限を持つBraze REST API キー。                                                                                                                                      |
| `USER_ID`              | この動画を受信するユーザーID。使用できる識別子の例については、[/users/trackを]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users)参照のこと。                                                                                                                                                  |
| `RECIPE_ID`       | [ステップ](#step-1)1でOtherLevels APIレスポンスから受け取った`recipe_id` 。                                                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### ステップ 3:Brazeコネクテッドコンテンツで送信する

GenAIの動画をiOSのプッシュメッセージとしてユーザーに送信するには、以下のステップに従う：

1. Braze iOSプッシュ通知キャンペーンを作成する。
2. キャンペーンを作成中に、**アセットセクションに**行き、以下のコネクテッドコンテンツ構文を**URLから追加**フィールドに貼り付ける。

{% raw %}
```
{% connected_content https://exp-platform-api-external.prod.awsotherlevels.com/v1/app/OTHERLEVELS_PROJECT_KEY/media/{{custom_attribute.${olxpmedia}}} %}
```
{% endraw %}

次に、`OTHERLEVELS_PROJECT_KEY` をOtherLevelsが提供するプロジェクト・キーに置き換える。

{: start="3"}
3\.**URLファイル形式の**ドロップダウンで、**MP**4を選択する。
4. キャンペーンの残りの部分（メッセージ内容、送信スケジュール、ターゲットオーディエンスなど）を、希望する設定に基づいて設定する。

![コネクテッドコンテンツのアセットフィールド例。]({% image_buster /assets/img/otherlevels/1.png %})

## GenAIの動画をカスタマイズする

### 動画サイズと属性

動画のバックグラウンドは、`bg_image` キー内部で指定できる。

| パラメーター             | 説明                  |
|-------------------------|----------------------------|
| `url`    | バックグラウンド画像のHTTPS URL。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

動画バックグラウンドのサイズは、`resize_image` キー内部で指定できる。バックグラウンド画像は、ここで設定したものと同じサイズにすることを推奨する。

| パラメーター             | 説明                  |
|-------------------------|----------------------------|
| `width`    | 背景画像の幅で、縦向きと横向きのオプションがある。 |
| `height`     | 背景画像の高さ。縦向きと横向きの両方のオプションがある。                              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

動画オーバーレイオプションは、`image_video_overlay` キー内部で指定できる。

| パラメーター             | 説明                  |
|-------------------------|----------------------------|
| `width`    | オーバーレイの幅。縦向きと横向きのオプションがある。 |
| `height`         | オーバーレイの高さ。縦向きと横向きの両方のオプションがある。                                              |
| `color`              | RGBで指定されたオーバーレイの色と透明度動画。                                                                   |
| `y_pos`       | 中心からのY軸オフセット。                                                              |
| `x_pos`    | 中心からのX軸オフセット。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### 才能と脚本

プロビジョニングの一環として、OtherLevelsはあなたの動画で使用する1人または複数のタレント（アバターと呼ばれることもある）を生成するためにあなたと協力する。ユースケースやブランドにもよるが、既存のブランド・アンバサダーを起用することもできるし、ユニークな作品を作ることもできる。

これらが作成されると、当社のAPIで使用可能な`TALENT_TEMPLATE` 、`TALENT_MODEL` IDが提供される。 

入力スクリプトを処理するために使用される音声モデルは、人間が読むような自然なスクリプトを提供するときに最もうまく機能する。ほとんどの場合、手動でスクリプトを誘導するために余分な句読点は必要ない。しかし、実際のオーディエンスに送信する前に、すべてのスクリプトをテストすることをお勧めする。タレントが台本を読む速度は、`talking_talent_speed` キー内部で指定できる。

| パラメーター             | 説明                  |
|-------------------------|----------------------------|
| `speed`    | タレントが台本を読むスピードを指定する。たとえば `1.5` です。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## その他の考慮事項

- iOSのプッシュ通知プラットフォームだけが動画メディアにネイティブ対応している。Androidのプッシュ通知はネイティブで動画をサポートしていないため、この統合はiOSオーディエンスにのみ使用できる。
- iOSデバイスで動画のプッシュ通知を受け取る場合、ユーザーは動画を読み込んで再生するためにプッシュ通知を長押しする必要がある。これはiOSプラットフォームの標準的な動作であり、カスタマイズすることはできない。