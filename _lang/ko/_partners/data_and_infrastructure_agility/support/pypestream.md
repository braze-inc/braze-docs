---
nav_title: Pypestream
article_title: Pypestream
description: "이 참조 문서에서는 브랜드와의 디지털 인게이지먼트를 강화할 수 있는 풀스택 대화형 인공지능 플랫폼인 Pypestream과 Braze 간의 파트너십을 간략히 설명합니다."
alias: /partners/pypestream/
page_type: partner
search_tag: Partner

---

# Pypestream

> [Pypestream](https://www.pypestream.com)은 브랜드를 '상시 가동' 디지털 엔티티로 변환하기 위해 특허받은 올인원 클라우드 메시징을 제공하는 풀스택 대화형 인공지능 플랫폼입니다. 이제 브랜드는 Pypestream을 통해 몰입형 사용자 경험, 고급 NLU 기능, 백엔드 시스템과의 실시간 통합을 활용하면서 모든 고객과 대규모로 옴니채널 대화에 참여할 수 있습니다.

_This integration is maintained by Pypestream._

## 통합 정보

Braze와 Pypestream의 통합을 통해 초기 아웃리치부터 대화 경험으로 연결되는 경로, 지능형 리타겟팅을 통한 옴니채널 후속 조치에 이르기까지 포괄적인 고객 생애주기를 원활하게 오케스트레이션할 수 있습니다. 

## 전제 조건

| 요구 사항 | 설명 |
|---|---|
| Pypestream 계정 | 이 파트너십을 이용하려면 [Pypestream 계정이](https://www.pypestream.com/contact-us/) 필요합니다.<br><br>가입하면 Pypestream 팀이 전용 환경을 설정하여 Braze와 통합할 수 있는 대화형 인공지능 솔루션 구축을 시작할 수 있도록 도와드립니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> 이는 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
| Braze REST 엔드포인트  | REST 엔드포인트 URL. 엔드포인트는 [인스턴스의 Braze URL에]({{site.baseurl}}/api/basics/) 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용 사례

Braze와 Pypestream의 파트너십은 캔버스에서 다음과 같은 일반적인 사용 사례를 달성하는 데 사용할 수 있습니다.
* **지능형 리타겟팅**: Pypestream을 통해 수집된 모든 리치 데이터 포인트를 활용하여 브랜드와 대화형 인게이지먼트에 참여한 후 Braze 캔버스로 사용자를 리타겟팅합니다.
* **동적 타겟팅**: 특정 코호트 및 세그먼트를 기반으로 기존 고객과 잠재 고객에게 다가가 Pypestream을 통해 맞춤형 대화 경험을 제공합니다.
* **상황에 맞는 고객 인사이트**: 최종사용자(기존 고객 또는 잠재 고객)가 웹사이트에 참여한 후, Pypestream 이벤트 리스너에서 수집한 웹페이지 태그를 Braze에 저장된 고객 데이터와 결합하여 완전히 개인화된 상황별 대화형 상호 작용을 제공합니다.

## 통합

Pypestream은 서버리스 통합 계층을 활용하여 다양한 플랫폼에 맞는 커스텀 통합을 수행합니다. 이 계층은 구축하는 대화형 흐름의 데이터 요구 사항을 지원하기 위해 서비스 또는 시스템과 인터페이스하는 데 사용됩니다. 작업 노드 통합이라고 하는 이러한 통합은 일반적으로 Python으로 작성되고 Pypestream 플랫폼을 사용하여 배포됩니다. 작업 노드가 인스턴스화된 후에는 모든 Braze API 엔드포인트에 통합할 수 있는 유연성을 제공하며 다양한 방식으로 결과를 평가할 수 있습니다. 

{% alert note %}
Pypestream 작업 노드에 대한 개요와 구성 단계는 이 [Pypestream 문서](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070)를 참조하세요. 이 설명서에 액세스하려면 Pypestream 고객이어야 합니다.
{% endalert %}

### 1단계: 엔드포인트 구성 설정

솔루션의 `app.py` 파일에서 Braze REST 엔드포인트 URL 및 Braze API 키와 같은 기본 구성 값을 설정해야 합니다. 

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

### 2단계: 액션 노드 템플릿 개발

작업 노드는 솔루션이 배포된 환경을 활용하여 이전 단계에서 설정한 각 Braze 엔드포인트와 상호 작용합니다. 이 단계에서는 특정 Braze 엔드포인트를 통합하기 위한 액션 노드를 개발합니다. 통합을 개발할 때 다음 템플릿을 가이드로 사용하세요: 

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
### 3단계: 솔루션 설계 업데이트

Braze REST API와 통합의 마지막 단계는 이전 단계에서 개발한 작업 노드를 사용하도록 Pypestream의 [Design Studio](https://platform.pypestream.com/design-studio/) 내에서 흐름을 구성하는 것입니다. 

{% alert note %}
Design Studio 내에서 모드를 구성하는 방법에 대한 개요를 보려면 이 [Pypestream 문서](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070)를 참조하세요. 이 설명서에 액세스하려면 Pypestream 고객이어야 합니다.
{% endalert %}

## 통합 사용 사례

전제 조건이 충족되고 작업 노드 구조가 생성되면, 개발자는 Braze API 엔드포인트와 상호 작용할 때 작업할 빈 캔버스를 갖게 됩니다. 이 예제는 작업 노드를 Braze [`/user/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)에 통합하는 데 필요한 단계, 특히 Pypestream 대화 흐름에 들어오는 특정 사용자를 추적하기 위한 고객 프로필을 생성하는 데 필요한 단계를 보여줍니다.

### 1단계: 대화 중 사용자로부터 데이터 수집

사용자가 Pypestream 세션에진입할 때 수집되는 데이터의 세부 사항은 전적으로 해당 사용 사례에 따라 달라집니다. Braze 내에서 고객 프로필을 생성하려면 대화에서 필수 필드를 수집해야 합니다.
이 필드는 원하는 엔드포인트에 필요합니다.

예를 들어, 솔루션이 Braze `/user/track` 엔드포인트에 대한 대화 중에 사용자로부터 다음 정보를 수집한 경우를 고려합니다. 

* 이름
* 성
* 이메일 주소
* 생년월일
* 거주 도시
* 운영 체제

이제 이 데이터를 Braze 플랫폼으로 전송하여 해당 사용자의 참여를 추적하고 향후 잠재적으로 리타겟팅할 수 있는 기능을 사용할 수 있습니다. [사용 사례 목록](#use-cases)을 확인하여 일반적인 애플리케이션을 살펴보세요.

### 2단계: 액션 노드 구조에서 데이터 채우기

작업 노드 개발에 동일한 구조를 활용하여 사용자로부터 수집한 데이터를 작업 노드에 채우고 `/user/track` 엔드포인트를 통해 Braze로 전송할 수 있습니다.

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

### 3단계: 액션 노드의 성공/실패 시 리디렉션되도록 솔루션 흐름 업데이트

마지막으로, 각 솔루션의 디자인에서 작업 노드 API 호출이 성공했는지 여부에 따라 사용자를 노드로 라우팅할 수 있습니다. 작업 노드에 오류 메시지가 수신되면 최종사용자는 주의해서 이 오류를 처리해야 합니다. 

