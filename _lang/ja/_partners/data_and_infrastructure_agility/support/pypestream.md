---
nav_title: Pypestream
article_title:パイプストリーム
description:この記事では、BrazeとPypestreamの提携について説明します。Pypestreamは、ブランドとのデジタルエンゲージメントを強化することができるフルスタックの会話型AIプラットフォームです。
alias: /partners/pypestream/
page_type: partner
search_tag:Partner

---

# パイプストリーム

> [Pypestream](https://www.pypestream.com) は、特許取得済みのオールインワンクラウドメッセージングを提供するフルスタックの会話型AIプラットフォームで、ブランドを「常時稼働」のデジタルエンティティに変革します。Pypestreamを使用すると、ブランドは没入型のユーザーエクスペリエンス、高度なNLU機能、およびバックエンドシステムへのリアルタイム統合を活用しながら、すべての顧客と大規模なオムニチャネル会話を行うことができます。

BrazeとPypestreamの統合により、初期のアウトリーチから会話型の体験にルーティングされ、インテリジェントなリターゲティングを通じてオムニチャネルのフォローアップに至るまで、エンドツーエンドの顧客ライフサイクルをシームレスにオーケストレーションすることができます。 

## 前提条件

| 要件 | 説明 |
|---|---|
| Pypestreamアカウント | このパートナーシップを利用するには、[パイプストリームアカウント](https://www.pypestream.com/contact-us/)が必要です。<br><br>購読すると、Pypestreamチームが専用の環境を設定し、Brazeと統合するための会話型AIソリューションの構築を開始するのを支援します。 |
| Braze REST API キー | `users.track` の権限を持つBraze REST APIキー。<br><br> これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze REST エンドポイント  | あなたのRESTエンドポイントURL。エンドポイントは、お使いのインスタンスの[Braze URL]({{site.baseurl}}/api/basics/)に依存します。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

BrazeとPypestreamのパートナーシップは、次のような一般的なユースケースを達成するためにキャンバスで使用できます。
* **インテリジェントなリターゲティング**:Pypestreamを介して収集された豊富なデータポイントを活用して、ブランドとの会話型エンゲージメントの後にBraze Canvasでユーザーをリターゲティングします。
* **動的ターゲティング**:Pypestreamを通じて、特定のコホートやセグメントに基づいて既存および見込み顧客にアプローチし、カスタマイズされた会話体験を提供します。
* **コンテクスト顧客インサイト**:エンドユーザー（既存または見込み顧客）があなたのウェブサイトでエンゲージした後、Pypestream Event Listenerから取り込まれたウェブページタグとBraze内に保存された顧客データを組み合わせて、完全にパーソナライズされ、文脈に即した会話型インタラクションを提供します。

## 統合

Pypestreamは、サーバーレスの統合レイヤーを活用して、さまざまなプラットフォームへのカスタム統合を実行します。このレイヤーは、構築中の会話フローのデータ要件をサポートするために、サービスやシステムとインターフェースするために使用されます。これらの統合は、アクションノード統合と呼ばれ、通常はPythonで記述され、Pypestreamプラットフォームを使用して展開されます。アクションノードがインスタンス化された後、任意のBraze APIエンドポイントに統合する柔軟性を提供し、結果を多くの方法で評価することができます。 

{% alert note %}
この[ Pypestreamの記事](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070)を参照して、Pypestreamアクションノードの概要と構成手順を確認してください。このドキュメントにアクセスするには、Pypestreamの顧客である必要があります。
{% endalert %}

### ステップ1:エンドポイント構成を設定する

ソリューションの `app.py` ファイルに、Braze REST エンドポイント URL や Braze API キーなどの主要な構成値を設定する必要があります。 

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

### ステップ2:アクションノードテンプレートを開発する

アクションノードは、前のステップで設定されたそれぞれのBrazeエンドポイントと対話するために、ソリューションが展開される環境を活用します。このステップでは、特定のBrazeエンドポイントを統合するためのアクションノードを開発します。次のテンプレートをガイドとして使用して、統合を開発します: 

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
### ステップ3:ソリューション設計を更新する

Braze REST APIとの統合の最終ステップは、前のステップで開発されたアクションノードを使用するようにPypestreamの[Design Studio](https://platform.pypestream.com/design-studio/)内のフローを構成することです。 

{% alert note %}
この[Pypestreamの記事](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070)を訪れて、デザインスタジオ内でモードを構成する方法の概要をご覧ください。このドキュメントにアクセスするには、Pypestreamの顧客である必要があります。
{% endalert %}

## 統合ユースケース

前提条件が満たされ、アクションノード構造が作成されると、開発者はBraze APIエンドポイントと対話する際に作業するための空白のキャンバスを持つことになります。この例では、アクションノードをBraze [`/user/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)に統合するために必要な手順を示しています。具体的には、特定のユーザーがPypestreamの会話フローに入る際にそのユーザープロファイルを作成して追跡することです。

### ステップ1:会話でユーザーからデータを収集する

ユーザーがPypestreamセッションに入ると、収集されるデータの詳細は完全にその時の使用例に依存します。Braze内でユーザープロファイルを作成できるようにするには、会話で必要なフィールドを収集する必要があります。
必要なエンドポイントによって要求されます。

例えば、ソリューションが会話中にユーザーから次の情報を収集した場合、Braze `/user/track` エンドポイント用: 

* 名
* 姓
* メールアドレス
* 生年月日
* 居住都市
* オペレーティングシステム

このデータは、将来的に再ターゲットする可能性を持ちながら、このユーザーのエンゲージメントを追跡するためにBrazeプラットフォームに送信できるようになりました。ユースケースリストをチェックして、一般的なアプリケーションを確認してください。

### ステップ2:アクションノード構造にデータを入力する

同じ構造を活用してアクションノードを開発することで、ユーザーから収集されたデータをアクションノードに入力し、`/user/track`エンドポイントを介してBrazeに送信できます。

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

### ステップ3:ソリューションフローを更新して、アクションノードの成功/失敗時にリダイレクトする

最後に、各ソリューションの設計において、アクションノードのAPIコールが成功したかどうかに基づいてユーザーをノードにルーティングすることができます。アクションノードがエラーメッセージを受信した場合、エンドユーザーは注意して扱う必要があります。 
