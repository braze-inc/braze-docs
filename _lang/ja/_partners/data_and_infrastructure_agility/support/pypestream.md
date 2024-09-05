---
nav_title: パイプストリーム
article_title: パイプストリーム
description: "この参考記事では、ブランドとのデジタル・エンゲージメントを強化できるフルスタックの会話AIプラットフォームであるBrazeとPypestreamのパートナーシップについて概説している。"
alias: /partners/pypestream/
page_type: partner
search_tag: Partner

---

# パイプストリーム

> [Pypestreamは](https://www.pypestream.com)フルスタックの会話AIプラットフォームで、特許を取得したオールインワンのクラウド・メッセージングを提供し、ブランドを「常時オン」のデジタル・エンティティに変える。Pypestreamを利用することで、ブランドは、没入感のあるユーザー体験、高度なNLU機能、バックエンドシステムとのリアルタイム統合を活用しながら、すべての顧客とオムニチャネルの会話を大規模に行うことができる。

BrazeとPypestreamの統合により、最初のアウトリーチから、会話体験へのルーティング、インテリジェントなリターゲティングによるオムニチャネルのフォローアップまで、エンドツーエンドの顧客ライフサイクルをシームレスに編成することができる。 

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Pypestreamアカウント | このパートナーシップを利用するには、[Pypestreamのアカウントが](https://www.pypestream.com/contact-us/)必要である。<br><br>契約後は、Pypestreamチームが専用環境のセットアップを支援し、Brazeと統合する会話AIソリューションの構築を開始する。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント  | RESTエンドポイントのURL。エンドポイントは、[インスタンスのBraze URLに]({{site.baseurl}}/api/basics/)依存する。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

BrazeとPypestreamのパートナーシップは、Canvasesで以下のような一般的なユースケースを実現するために使用することができる：
* **インテリジェントなリターゲティング**：Pypestreamを通じて収集された豊富なデータポイントを活用することで、ブランドとの会話エンゲージメントの後にBraze Canvasでユーザーをリターゲティングしよう。
* **ダイナミック・ターゲティング**だ：特定のコホートやセグメントに基づいて既存顧客や見込み客にアプローチし、Pypestreamを通じてカスタマイズされた会話体験を提供する。
* **コンテクスチュアルな顧客インサイト**：エンドユーザー（既存または見込み客）がウェブサイトにアクセスした後、Pypestream Event Listenerから取り込んだウェブページタグと、Brazeに保存されている顧客データを組み合わせることで、完全にパーソナライズされた、文脈に沿った会話型インタラクションを提供することができる。

## 統合

Pypestreamはサーバーレスの統合レイヤーを活用し、様々なプラットフォームへのカスタム統合を行う。このレイヤーは、構築される会話フローのデータ要件をサポートするために、サービスやシステムとのインターフェースに使用される。アクション・ノード統合と呼ばれるこれらの統合は、通常Pythonで書かれ、Pypestreamプラットフォームを使ってデプロイされる。アクションノードがインスタンス化されると、Braze APIのどのエンドポイントにも柔軟に統合できるようになり、結果をさまざまな方法で評価できるようになる。 

{% alert note %}
Pypestreamアクションノードの概要と設定手順については、こちらの[Pypestreamの記事を](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070)参照のこと。このドキュメントにアクセスするには、Pypestreamの顧客である必要がある。
{% endalert %}

### ステップ1:エンドポイントの設定を行う

Braze RESTエンドポイントURLやBraze APIキーなどの主要な設定値は、ソリューションの`app.py` ファイルに設定する： 

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
Design Studioでモードを設定する方法の概要については、[Pypestreamの記事を](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070)参照のこと。このドキュメントにアクセスするには、Pypestreamの顧客である必要がある。
{% endalert %}

## 統合のユースケース

前提条件が満たされ、アクションノード構造が作成されると、開発者は、Braze APIエンドポイントと対話する際に、空白のキャンバスで作業できるようになる。この例では、アクションノードをBraze[`/user/track` のエンドポイントに]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)統合するために必要な手順を示す[。具体的には]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)、Pypestreamの会話フローに入る特定のユーザーを追跡するためのユーザープロファイルを作成する。

### ステップ1:会話の中でユーザーからデータを収集する

ユーザーがPypestreamのセッションに入ると、収集されるデータの詳細は、その時点でのユースケースに完全に依存する。Brazeでユーザープロフィールを作成するには、会話で必要なフィールドを収集する必要がある。
目的のエンドポイントが必要とするものである。

例えば、Braze`/user/track` エンドポイントの会話中に、ソリューションがユーザーから以下の情報を収集したとする： 

* 名
* 姓
* メールアドレス
* 生年月日
* 居住都市
* オペレーティング・システム

このデータはBrazeプラットフォームに送られ、このユーザーのエンゲージメントを追跡し、将来的にリターゲティングできる可能性がある。一般的なアプリケーションを見るには、[ユースケース・リストを](#use-cases)チェックしよう。

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

最後に、各ソリューションの設計では、アクション・ノードAPI呼び出しが成功したかどうかに基づいて、ユーザーをノードにルーティングすることができる。アクションノードがエラーメッセージを受け取った場合、エンドユーザーは注意深く対処しなければならない。 
