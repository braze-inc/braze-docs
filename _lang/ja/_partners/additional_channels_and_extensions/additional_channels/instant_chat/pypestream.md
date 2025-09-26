---
nav_title: Pypestream
article_title: Pypestream
description: "この参考記事では、ブランドとのデジタル・エンゲージメントを強化できるフルスタックの会話AIプラットフォームであるBrazeとPypestreamのパートナーシップについて概説している。"
alias: /partners/pypestream/
page_type: partner
search_tag: Partner

---

# Pypestream

> [Pypestream](https://www.pypestream.com) はフルスタックの会話型 AI プラットフォームであり、特許取得済みのオールインワン型のクラウドメッセージングを提供し、ブランドを「常時稼働」状態のデジタルエンティティに変換します。Pypestream によりブランドは、没入型のユーザーエクスペリエンス、高度な NLU 機能、バックエンドシステムへのリアルタイム統合を利用し、大規模なオムニチャネルの会話に参加できるようになります。

_この統合は Pypestream によって管理されます。_

## 統合について

Braze と Pypestream の統合により、最初のアウトリーチから、会話エクスぺリエンスへのルーティング、インテリジェントなリターゲティングによるオムニチャネルのフォローアップまで、エンドツーエンドのカスタマーライフサイクルをシームレスに調整できます。 

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Pypestreamアカウント | このパートナーシップを活用するには、[Pypestream アカウント](https://www.pypestream.com/contact-us/)が必要です。<br><br>サブスクライブ後は、Pypestream チームが、Braze と統合する会話型 AI ソリューションの構築を開始するための専用の環境の設定を支援します。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント  | REST エンドポイントのURL。エンドポイントはインスタンスの [Braze URL]({{site.baseurl}}/api/basics/) に応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

Braze と Pypestream の連携により、キャンバスで以下のような一般的なユースケースを実現できます。
* **インテリジェントなリターゲティング**：Pypestream で収集されたリッチなデータポイントをすべて活用して、ユーザーがブランドとの会話を終えた後に Braze キャンバスでユーザーをリターゲティングします。
* **ダイナミックターゲット設定**：特定のコホートやセグメントに基づいて既存の顧客や見込み客にアプローチし、Pypestream でカスタマイズされた会話エクスペリエンスを提供します。
* **状況に即した顧客インサイト**:エンドユーザー (既存の顧客または見込み客) が Web サイトでやり取りをした後で、Pypestream Event Listener から取り込んだ Web ページタグと、Braze に保存されている顧客データを組み合わせることで、完全にパーソナライズされ、コンテキストに即した会話型インタラクションを提供できます。

## 統合

Pypestreamはサーバーレスの統合レイヤーを活用し、様々なプラットフォームへのカスタム統合を行う。このレイヤーは、構築される会話フローのデータ要件をサポートするために、サービスやシステムとのインターフェースに使用される。これらの統合は、アクションノード統合と呼ばれ、通常、Python で記述され、Pypestream プラットフォームを使用してデプロイされます。アクションノードがインスタンス化されると、Braze APIのどのエンドポイントにも柔軟に統合できるようになり、結果をさまざまな方法で評価できるようになる。 

{% alert note %}
Pypestream アクションノードの概要と設定手順については、この [Pypestream の記事](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070)を参照してください。このドキュメントにアクセスするには、Pypestream の顧客である必要があります。
{% endalert %}

### ステップ1:エンドポイントの設定を行う

Raze REST エンドポイント URL や Braze API キーなどの主要な設定値は、ソリューションの `app.py` ファイルで設定する必要があります。 

```
import os

NAME = '{ CUSTOMER NAME }'
BOTS = []
CSV_BOTS = ['{ SOLUTION NAME }']
PATH = os.path.dirname(__file__)

PARAMS = {
    'sandbox': {
        #Braze
        'braze_url': '{ BRAZE ENDPOINT URL }',
        'braze_api_key': '{ BRAZE API KEY }',
        'braze_user_track': 'users/track'
    },
    'prod': {

        #Braze
        'braze_url': '{ BRAZE ENDPOINT URL }',
        'braze_api_key': '{ BRAZE API KEY }',
        'braze_user_track': 'users/track'
    },
}
```

### ステップ2:アクション・ノード・テンプレートを開発する

アクションノードは、前のステップで設定されたそれぞれのBrazeエンドポイントを使用して、ソリューションが相互作用するように展開された環境を活用する。このステップでは、特定のBrazeエンドポイントを統合するためのアクションノードを開発する。統合を開発する際のガイドとして、以下のテンプレートを使用する： 

```
# -*- coding: utf-8 -*-
r'''
    ______  ______  _____________________  _________    __  ___
   / __ \ \/ / __ \/ ____/ ___/_  __/ __ \/ ____/   |  /  |/  /
  / /_/ /\  / /_/ / __/  \__ \ / / / /_/ / __/ / /| | / /|_/ /
 / ____/ / / ____/ /___ ___/ // / / _, _/ /___/ ___ |/ /  / /
/_/     /_/_/   /_____//____//_/ /_/ |_/_____/_/  |_/_/  /_/
Action Node Script for Braze Integration

Parameters
----------
POST Request to the User Track Braze Endpoint (users/track)

{
  "api_base_url": "{env.braze_url}",
  "req_endpoint_path": "users/track",
  "req_method": "POST",
  "req_headers": {
    "Authorization": "{YOUR-REST-API-KEY}"
    "Content-Type": "application/json"
  },
  "req_body": {
        "api_key": "{env.braze_api_key}",
        "attributes": [{
                "external_id": "{HOLDER_EMAIL}",
                ...
        }],
        "events": [
            ...
        ]
}

Returns
-------
Creates and/or Updates User Details within Braze dashboard

'''
import requests
from .. import app

class BrazeExample:
    def execute(self, log, payload=None, context=None):
        try:
            # initialize payload variables
            app_params = app.PARAMS[context['env']]
            req_params = {
                "attributes": [{
                    "external_id": "{ USER_ID }",
                    # include add'tl user details in this section
                    # refer to the Braze API Documentation for User Track REST API Endpoint for more details
                }],
                "events": [],
                "partner" : 'pypestream'
            }
            req_url = '{}/{}'.format(
                app_params['braze_url'],
                app_params['braze_user_track']
            )
            req_headers = {
                "Authorization": app_params['braze_api_key']
                "Content-Type": "application/json"
            }

            resp = requests.post(req_url,
                                params=req_params,
                                headers=req_headers)
            
            log('BrazeExample API response: {}'.format(resp.text))

            if resp.status_code == 400:
                return {'success': 'error'}

            return {'success': 'true'}

        except Exception as err:
            log('BrazeExample Exception error: {}'.format(err))

        return {'success': 'error'}
```
### ステップ3:ソリューション・デザインを更新する

Braze REST APIと統合する最後のステップでは、前のステップで開発したアクションノードを使用するように、Pypestreamの[Design Studio](https://platform.pypestream.com/design-studio/)内でフローを設定する。 

{% alert note %}
Design Studio でモードを設定する方法の概要については、[Pypestream の記事](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070)を参照してください。このドキュメントにアクセスするには、Pypestream の顧客である必要があります。
{% endalert %}

## 統合のユースケース

前提条件が満たされ、アクションノード構造が作成されると、開発者はブランクのキャンバスを使用して、Braze API エンドポイントとのインタラクションを開始します。この例は、アクションノードを Braze [`/user/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)に統合するために必要な手順を示します。具体的には、Pypestream 会話フローに入る特定のユーザーを追跡するためにユーザープロファイルを作成します。

### ステップ1:会話の中でユーザーからデータを収集する

ユーザーが Pypestream セッションに入ると、収集されるデータの詳細は、その時点でのユースケースに完全に依存します。Brazeでユーザープロフィールを作成するには、会話で必要なフィールドを収集する必要がある。
目的のエンドポイントに必要な

たとえば、ソリューションが Braze `/user/track` エンドポイントの会話中にユーザーから次の情報を収集するとします。 

* 名
* 姓
* メールアドレス
* 生年月日
* 居住地の市町村
* オペレーティング・システム

将来的にこのユーザーをリターゲティングできる機能により、このユーザーのエンゲージメントを追跡するために、このデータを Braze プラットフォームに送信できます。一般的なアプリケーションを見るには、[ユースケース・リストを](#use-cases)チェックしよう。

### ステップ2:アクションノード構造体にデータを入力する

アクションノードを開発するための同じ構造を活用することで、ユーザーから収集したデータをアクションノードに入力し、当社の`/user/track` エンドポイントを経由してBrazeに送信することができる。

```
# -*- coding: utf-8 -*-
r'''
    ______  ______  _____________________  _________    __  ___
   / __ \ \/ / __ \/ ____/ ___/_  __/ __ \/ ____/   |  /  |/  /
  / /_/ /\  / /_/ / __/  \__ \ / / / /_/ / __/ / /| | / /|_/ /
 / ____/ / / ____/ /___ ___/ // / / _, _/ /___/ ___ |/ /  / /
/_/     /_/_/   /_____//____//_/ /_/ |_/_____/_/  |_/_/  /_/
Action Node Script for Braze Integration

Parameters
----------
POST Request to the User Track Braze Endpoint (users/track)

{
  "api_base_url": "{env.braze_url}",
  "req_endpoint_path": "users/track",
  "req_method": "POST",
  "req_headers": {
    "Content-Type": "application/json"
  },
  "req_body": {
        "api_key": "{env.braze_api_key}",
        "attributes": [{
                "external_id": "{HOLDER_EMAIL}",
                ...
        }],
        "events": [
            ...
        ],
        "partner" : 'pypestream'
}

Returns
-------
Creates and/or Updates User Details within Braze dashboard

'''
import requests
from .. import app

class BrazeExample:
    def execute(self, log, payload=None, context=None):
        try:
            # initialize payload variables
            app_params = app.PARAMS[context['env']]
            req_params = {
                "attributes": [{
                    "external_id": "{ USER_ID }",
                    "first_name": "{ FIRST_NAME }",
                    "last_name": "{ LAST_NAME }",
                    "email": "{ EMAIL_ADDRESS }",
                    "dob": "{ DATE_OF_BIRTH }",
                    "home_city": "{ CITY_OF_RESIDENCE }",
                    "operating_system": "{ OPERATING_SYSTEM }" #custom attributes can be added here as well
                    # include add'tl user details in this section
                    # refer to the Braze API Documentation for User Track REST API Endpoint for more details
                }],
                "events": [{
                    "external_id": "{ USER_ID }",
                    "name": "{ NAME_OF_EVENT }",
                    "time": "{ EVENT_TIME }"
                }],
                "partner" : 'pypestream'
            }
            req_url = '{}/{}'.format(
                app_params['braze_url'],
                app_params['braze_user_track']
            )
            req_headers = {
                "Authorization": app_params['braze_api_key']
                "Content-Type": "application/json"
            }

            resp = requests.post(req_url,
                                params=req_params,
                                headers=req_headers)
            
            log('BrazeExample API response: {}'.format(resp.text))

            if resp.status_code == 400:
                return {'success': 'error'}

            return {'success': 'true'}

        except Exception as err:
            log('BrazeExample Exception error: {}'.format(err))

        return {'success': 'error'}
```

### ステップ3:アクションノードの成功/失敗時にリダイレクトするようにソリューションフローを更新する。

最後に、各ソリューションの設計では、アクション・ノードAPI呼び出しが成功したかどうかに基づいて、ユーザーをノードにルーティングすることができる。アクションノードがエラーメッセージを受信した場合、エンドユーザーを慎重に処理する必要があります。 

