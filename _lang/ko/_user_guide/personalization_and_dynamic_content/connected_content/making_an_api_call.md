---
nav_title: Making a Connected Content call
article_title: 연결된 콘텐츠 API 호출 만들기
page_order: 0
description: "이 참조 문서에서는 연결된 콘텐츠 API를 호출하는 방법과 유용한 예제 및 고급 연결된 콘텐츠 사용 사례를 다룹니다."
search_rank: 2
---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"} 연결된 콘텐츠 API 호출 만들기

> 연결된 콘텐츠를 사용하면 API로 접근 가능한 모든 정보를 사용자에게 보내는 메시지에 직접 삽입할 수 있습니다. 웹 서버에서 직접 콘텐츠를 가져오거나 공개적으로 액세스할 수 있는 API에서 콘텐츠를 가져올 수 있습니다.<br><br>이 페이지에서는 연결된 콘텐츠 API 호출 방법, 고급 연결된 콘텐츠 사용 사례, 오류 처리 등을 다룹니다.

## 연결된 콘텐츠 호출 볼륨 이해하기

{% alert important %}
한 번의 발송이 한 번의 연결된 콘텐츠 호출과 같지 않습니다. Braze는 메시지 발송과 연결된 콘텐츠 요청 간의 1:1 비율을 보장하지 않습니다. 시스템은 호출 수를 최소화하는 것보다 올바른 메시지 렌더링과 전달을 우선시하도록 설계되어 있습니다. 엔드포인트는 수신자 수 또는 발송된 메시지 수보다 더 많은 요청을 처리할 수 있도록 구축되어야 합니다.
{% endalert %}

Braze는 수신자당 동일한 연결된 콘텐츠 API 호출을 두 번 이상 수행할 수 있습니다. 일반적인 이유는 다음과 같습니다:

- **여러 파트가 있는 이메일:** 단일 이메일은 HTML 본문, 일반 텍스트 본문, 가속 모바일 페이지(AMP) 버전(있는 경우)에 대해 별도의 렌더링 패스를 트리거할 수 있습니다. 각 패스는 해당 파트에서 연결된 콘텐츠를 트리거할 수 있으므로, 한 명의 수신자가 여러 개의 동일하거나 유사한 호출을 생성할 수 있습니다.
- **유효성 검사 및 재시도:** 메시지 페이로드는 유효성 검사, 재시도 로직 또는 기타 내부 목적을 위해 수신자당 여러 번 렌더링될 수 있습니다.
- **채널 동작:** 연결된 콘텐츠는 메시지가 렌더링될 때 실행됩니다. 인앱 메시지의 경우 메시지는 노출 시점에 렌더링됩니다.

로그에서 발송 수 또는 수신자 수보다 더 많은 연결된 콘텐츠 호출이 보인다면, 이는 예상되는 동작입니다. 부하를 줄이고 확장을 계획하는 방법에 대한 안내는 [대용량 엔드포인트 모범 사례](#best-practices-for-high-volume-endpoints)를 참조하세요.

## 연결된 콘텐츠 호출 보내기

{% raw %}

연결된 콘텐츠 호출을 보내려면 `{% connected_content %}` 태그를 사용합니다. 이 태그를 사용하면 `:save`를 사용하여 변수를 할당하거나 선언할 수 있습니다. 이러한 변수의 측면은 나중에 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid)를 사용하여 메시지에서 참조할 수 있습니다.

예를 들어, 다음 메시지 본문은 URL `http://numbersapi.com/random/trivia`에 접속하여 재미있는 퀴즈 사실을 메시지에 포함시킵니다:

```
{% connected_content http://numbersapi.com/random/trivia :save result %}
Hi there, here is some fun trivia for you!: {{result.text}}
```

### 변수 추가

연결된 콘텐츠를 요청할 때 고객 프로필 속성을 URL 문자열에 변수로 포함할 수도 있습니다. 

예를 들어 사용자의 이메일 주소와 ID를 기반으로 콘텐츠를 반환하는 웹 서비스가 있을 수 있습니다. 앳 기호(@)와 같은 특수 문자가 포함된 속성을 전달하는 경우 다음 이메일 주소 속성에 표시된 것처럼 Liquid 필터 `url_param_escape`를 사용하여 URL에 허용되지 않는 문자를 URL 친화적인 이스케이프 버전으로 바꾸어야 합니다.

```
Hi, here are some articles that you might find interesting:

{% connected_content http://www.yourwebsite.com/articles?email={{${email_address} | url_param_escape}}&user_id={{${user_id}}} %}
```
{% endraw %}
{% alert note %}
속성 값은 `${}`로 묶어야 Liquid 구문 버전에서 제대로 작동합니다.
{% endalert %}

연결된 콘텐츠 요청은 GET 및 POST 요청만 지원합니다.

## 오류 처리

URL을 사용할 수 없고 404 페이지에 도달하면 Braze는 그 자리에 빈 문자열을 렌더링합니다. URL이 HTTP 500 또는 502 페이지에 도달하면 재시도 로직에서 실패합니다.

엔드포인트가 JSON을 반환하는 경우 `connected` 값이 null인지 확인하여 이를 감지한 다음 [조건부로 메시지를 중단]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/)할 수 있습니다. Braze는 포트 80(HTTP) 및 443(HTTPS)을 통해 통신하는 URL만 허용합니다.

### 비정상 호스트 감지

연결된 콘텐츠는 대상 호스트에 심각한 속도 저하 또는 과부하가 발생하여 시간 초과, 과도한 요청 또는 Braze가 대상 엔드포인트와 성공적으로 통신하지 못하는 기타 결과가 발생하는 경우를 감지하는 비정상 호스트 감지 메커니즘을 사용합니다. 이는 대상 호스트가 어려움을 겪을 수 있는 불필요한 부하를 줄이기 위한 안전장치 역할을 합니다. 또한 Braze 인프라를 안정화하고 빠른 메시징 속도를 유지하는 데도 도움이 됩니다.

대상 호스트에 심각한 속도 저하 또는 과부하가 발생하면 Braze는 1분 동안 대상 호스트에 대한 요청을 일시적으로 중단하고 대신 장애를 나타내는 응답을 시뮬레이션합니다. 1분 후 Braze는 소수의 요청을 통해 호스트의 상태를 검사한 후 호스트가 정상인 것으로 확인되면 최대 속도로 요청을 재개합니다. 호스트가 여전히 비정상이면 Braze는 다시 시도하기 전에 1분을 더 기다립니다.

비정상 호스트 감지기에 의해 대상 호스트에 대한 요청이 중단되는 경우, Braze는 오류 응답 코드를 받은 것처럼 메시지를 계속 렌더링하고 Liquid 로직을 따릅니다. 이러한 연결된 콘텐츠 요청이 비정상 호스트 감지기에 의해 중단될 때 다시 시도되도록 하려면 `:retry` 옵션을 사용하세요. `:retry` 옵션에 대한 자세한 내용은 [연결된 콘텐츠 재시도]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries)를 참조하세요.

비정상 호스트 감지로 인해 문제가 발생했다고 생각되면 [Braze 고객지원]({{site.baseurl}}/support_contact/)에 문의하세요.

{% alert note %}
연결된 콘텐츠에 사용할 특정 URL을 허용 목록에 추가할 수 있습니다. 이 기능을 이용하려면 고객 성공 매니저에게 문의하세요.
{% endalert %}

{% alert tip %}
일반적인 오류 코드를 해결하는 방법에 대해 자세히 알아보려면 [웹훅 및 연결된 콘텐츠 요청 문제 해결]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors#unhealthy-host-detection)을 참조하세요.
{% endalert %}

### 사용량 제한(429)과 비정상 호스트 감지 비교

다음은 서로 다른 메커니즘입니다:

- **429 Too Many Requests:** 엔드포인트(또는 업스트림 서비스)가 이 응답을 반환하고 있습니다. 이는 서버 또는 미들웨어가 트래픽을 거부하고 있음을 의미하며, 자체 사용량 제한이 있기 때문인 경우가 많습니다. Braze는 연결된 콘텐츠에 별도의 사용량 제한을 적용하지 않습니다. 연결된 콘텐츠 요청 볼륨은 [메시지 전달 속도 사용량 제한]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting)에 따라 직접 확장됩니다. 메시지는 수신자당 여러 번 렌더링될 수 있으므로(예: 이메일 HTML, 일반 텍스트, AMP) 연결된 콘텐츠 요청 수가 해당 사용량 제한을 초과할 수 있습니다. 설정한 분당 메시지 수 이하가 될 것이라고 가정하지 마세요. 429 오류가 발생하면 예상 요청 볼륨을 처리할 수 있도록 엔드포인트 또는 미들웨어를 확장하거나, 캠페인 또는 캔버스 단계의 사용량 제한을 낮추어 분당 더 적은 메시지(따라서 더 적은 연결된 콘텐츠 호출)가 발송되도록 하세요.
- **비정상 호스트 감지:** 1분 기간 내에 높은 비율과 볼륨의 *실패*가 발생한 후 트리거되는 Braze 측 안전장치입니다. 실패 횟수에는 `408`, `429`, `502`, `503`, `504`, `529` 상태 코드가 포함됩니다. 트리거되면 Braze는 해당 호스트에 대한 요청을 일시적으로 중단하고 실패 응답을 시뮬레이션합니다. 이는 자체 사용량 제한과 독립적입니다. 감지 임계값 및 자세한 내용은 [웹훅 및 연결된 콘텐츠 요청 문제 해결]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors/#unhealthy-host-detection)을 참조하세요. 비정상 호스트 감지를 방지하려면 [연결된 콘텐츠 호출 볼륨 이해하기](#understanding-connected-content-call-volume) 및 [대용량 엔드포인트 모범 사례](#best-practices-for-high-volume-endpoints)에 설명된 호출 볼륨을 엔드포인트가 처리할 수 있는지 확인하세요.

## 효율적인 성능 보장

Braze는 매우 빠른 속도로 메시지를 전달하므로, 콘텐츠를 가져올 때 서버가 과부하되지 않도록 수천 개의 동시 연결을 처리할 수 있는지 확인하세요. 공개 API를 사용할 때는 API 제공업체가 적용할 수 있는 사용량 제한을 위반하지 않는지 확인하세요. Braze는 성능상의 이유로 서버 응답 시간이 2초 미만이어야 합니다. 서버가 응답하는 데 2초 이상 걸리면 콘텐츠가 삽입되지 않습니다.

엔드포인트 용량 계획 및 호출 볼륨 줄이기에 대한 자세한 내용은 [대용량 엔드포인트 모범 사례](#best-practices-for-high-volume-endpoints)를 참조하세요.

## 알아두어야 할 사항

* Braze는 API 호출에 대해 요금을 부과하지 않으며 주어진 데이터 포인트 사용량에 포함되지 않습니다.
* 연결된 콘텐츠 응답에는 1MB 제한이 있습니다.
* 연결된 콘텐츠는 메시지가 렌더링될 때 실행됩니다. 인앱 메시지의 경우 메시지는 노출 시점에 렌더링됩니다.
* 연결된 콘텐츠 호출은 리디렉션을 따르지 않습니다.

## 대용량 엔드포인트 모범 사례

메시지에서 연결된 콘텐츠를 사용하고 대용량으로 발송하는 경우, 수신자 수 또는 발송 수보다 더 많은 요청을 계획하세요:

1. **피크 부하 추정:** 엔드포인트 또는 미들웨어의 크기를 산정할 때 보수적인 배수를 사용하세요. 연결된 콘텐츠 요청은 수신자 수 또는 발송된 메시지 수를 초과할 수 있습니다. 예를 들어, 이메일의 경우 단일 수신자가 여러 호출(HTML, 일반 텍스트, AMP)을 생성할 수 있으므로, 수신자 × 2 또는 × 3이 보수적인 추정치로 자주 사용됩니다.
2. **적절한 경우 캐싱 사용:** GET 요청은 기본적으로 캐시됩니다. POST 요청의 경우 응답을 일정 기간 재사용할 수 있을 때(예: 요청별로 변경되지 않는 토큰 또는 콘텐츠) `:cache_max_age`를 추가하세요. [응답 캐싱]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/caching_responses/) 및 아래의 [POST 캐싱 FAQ](#what-is-caching-behavior)를 참조하세요.
3. **전달 속도 사용량 제한 설정:** 캠페인 또는 캔버스 단계의 [전달 속도 사용량 제한]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting)은 연결된 콘텐츠 요청 볼륨을 간접적으로 제한하는 유일한 수단입니다. Braze는 연결된 콘텐츠 자체에 사용량 제한을 적용하지 않습니다. 이는 프록시일 뿐이며 완벽하지 않습니다. 연결된 콘텐츠 요청은 메시지와 1:1이 아니기 때문입니다. 메시지(따라서 연결된 콘텐츠) 볼륨을 엔드포인트가 처리할 수 있는 범위 내로 유지하는 데 사용하세요.
4. **멱등성 및 재시도를 고려한 설계:** Braze는 수신자당 엔드포인트를 두 번 이상 호출할 수 있습니다. 엔드포인트가 잘못된 부작용 없이 중복 요청을 허용할 수 있는지 확인하세요.

## 인증 유형

### 기본 인증 사용

URL에 기본 인증이 필요한 경우 Braze는 API 호출에 사용할 수 있도록 기본 인증 자격 증명을 저장할 수 있습니다. **설정** > **연결된 콘텐츠**에서 기존의 기본 인증 자격 증명을 관리하고 새 인증 자격 증명을 추가할 수 있습니다.

![Braze 대시보드의 연결된 콘텐츠 설정입니다.]({% image_buster /assets/img/connected_content/basic_auth_mgmt.png %})

새 자격 증명을 추가하려면 **자격 증명 추가** > **기본 인증**을 선택합니다. 

![기본 인증 또는 토큰 인증을 사용할 수 있는 옵션이 있는 '자격 증명 추가' 드롭다운입니다.]({% image_buster /assets/img/connected_content/add_credential_button.png %}){: style="max-width:60%"}

자격 증명에 이름을 지정하고 사용자 아이디와 비밀번호를 입력합니다.

![이름, 사용자 아이디, 비밀번호를 입력하는 옵션이 있는 '새 자격 증명 만들기' 창입니다.]({% image_buster /assets/img/connected_content/basic_auth_token.png %}){: style="max-width:60%"}

그런 다음 토큰의 이름을 참조하여 API 호출에서 이 기본 인증 자격 증명을 사용할 수 있습니다:

{% raw %}
```
Hi there, here is some fun trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
자격 증명을 삭제하면 해당 자격 증명을 사용하려는 모든 연결된 콘텐츠 호출이 중단된다는 점에 유의하세요.
{% endalert %}

### 토큰 인증 사용

Braze 연결된 콘텐츠를 사용할 때 특정 API에 사용자 아이디와 비밀번호 대신 토큰이 필요할 수 있습니다. Braze는 토큰 인증 헤더 값을 포함하는 자격 증명도 저장할 수 있습니다.

토큰 값을 보관하는 자격 증명을 추가하려면 **자격 증명 추가** > **토큰 인증**을 선택합니다. 그런 다음 API 호출 헤더와 허용된 도메인에 대한 키-값 페어를 추가합니다.

![토큰 인증 세부 정보가 포함된 토큰 예시("token_credential_abc").]({% image_buster /assets/img/connected_content/token_auth.png %}){: style="max-width:60%"}

그런 다음 자격 증명 이름을 참조하여 API 호출에서 이 자격 증명을 사용할 수 있습니다:

{% raw %}
```
{% assign campaign_name="New Year Sale" %}
{% connected_content
     https://api.endpoint.com/your_path
     :method post
     :auth_credentials token_credential_abc
     :body campaign={{campaign_name}}&customer={{${user_id}}}&channel=Braze
     :content_type application/json
     :save publication
%}
```
{% endraw %}

### OAuth(공개 인증) 사용

일부 API 구성에서는 액세스하려는 API 엔드포인트를 인증하는 데 사용할 수 있는 액세스 토큰을 검색해야 합니다.

#### 1단계: 액세스 토큰 검색

다음 예시는 액세스 토큰을 검색하여 로컬 변수에 저장하는 방법을 보여줍니다. 이 변수는 이후 API 호출을 인증하는 데 사용할 수 있습니다. `:cache_max_age` 매개변수를 추가하여 액세스 토큰의 유효 기간과 일치시키고 아웃바운드 연결된 콘텐츠 호출 수를 줄일 수 있습니다. 자세한 내용은 [구성 가능한 캐싱]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/local_connected_content_variables/#configurable-caching)을 참조하세요.

{% raw %}
```
{% connected_content
     https://your_API_access_token_endpoint_here/
     :method post
     :auth_credentials access_token_credential_abc
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE"
     }
     :cache_max_age 900
     :save token_response
%}
```
{% endraw %}

#### 2단계: 검색된 액세스 토큰을 사용하여 API 승인

토큰이 저장된 후에는 후속 연결된 콘텐츠 호출에 토큰을 동적으로 템플릿화하여 요청을 승인할 수 있습니다:

{% raw %}
```
{% connected_content
     https://your_API_endpoint_here/
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE",
       "Authorization": "{{token_response}}"
     }
     :body key1=value1&key2=value2
     :save response
%}
```
{% endraw %}

### 자격 증명 편집

인증 유형에 대한 자격 증명 이름을 편집할 수 있습니다.

- 기본 인증의 경우 사용자 아이디와 비밀번호를 업데이트할 수 있습니다. 이전에 입력한 비밀번호는 표시되지 않습니다.
- 토큰 인증의 경우 헤더 키-값 페어와 허용 도메인을 업데이트할 수 있습니다. 이전에 설정한 헤더 값은 표시되지 않습니다.

![자격 증명을 편집하는 옵션입니다.]({% image_buster /assets/img/connected_content/edit_credentials.png %}){: style="max-width:60%"}

## 연결된 콘텐츠 IP 허용 목록

Braze에서 연결된 콘텐츠를 사용한 메시지가 전송되면, Braze 서버는 자동으로 고객 또는 타사 서버에 네트워크 요청을 보내 데이터를 가져옵니다. IP 허용 목록을 사용하면 연결된 콘텐츠 요청이 실제로 Braze에서 오는지 확인할 수 있어 보안이 한층 강화됩니다.

Braze는 다음 IP 범위에서 연결된 콘텐츠 요청을 보냅니다. 나열된 범위는 허용 목록에 옵트인된 모든 API 키에 자동으로 동적 추가됩니다. 

Braze에는 모든 서비스에 사용되는 예약된 IP 집합이 있으며, 모든 IP가 특정 시간에 활성화되는 것은 아닙니다. 이는 필요한 경우 고객에게 영향을 주지 않고 Braze가 다른 데이터 센터에서 전송하거나 유지보수를 수행할 수 있도록 설계되었습니다. Braze는 연결된 콘텐츠를 요청할 때 다음 IP 중 하나, 일부 또는 전부를 사용할 수 있습니다.

{% multi_lang_include data_centers.md datacenters='ips' %}

### `User-Agent` 헤더

Braze는 모든 연결된 콘텐츠 및 웹훅 요청에 다음과 유사한 `User-Agent` 헤더를 포함합니다:

```text
Braze Sender 75e404755ae1270441f07eb238f0faf25e44dfdc
```

{% alert tip %}
해시 값은 정기적으로 변경된다는 점에 유의하세요. `User-Agent`로 트래픽을 필터링하는 경우 `Braze Sender`로 시작하는 모든 값을 허용하세요.
{% endalert %}

## 문제 해결

[Webhook.site](https://webhook.site/)를 사용하여 연결된 콘텐츠 호출 문제를 해결하세요. 

1. 연결된 콘텐츠 호출의 URL을 사이트에서 생성된 고유 URL로 전환합니다.
2. 캠페인 또는 캔버스 단계를 미리 보고 테스트하여 이 웹사이트로 들어오는 요청을 확인합니다.

이 도구를 사용하면 요청 헤더, 요청 본문 및 호출에서 전송되는 기타 정보와 관련된 문제를 진단할 수 있습니다.

## 자주 묻는 질문

### 연결된 콘텐츠 호출이 사용자 또는 발송 수보다 많은 이유는 무엇인가요? 

이는 예상되는 동작입니다. Braze는 메시지 페이로드가 여러 번 렌더링될 수 있으므로(예: 이메일 HTML, 일반 텍스트, AMP; 유효성 검사 또는 재시도 로직; 기타 내부 목적) 수신자당 동일한 연결된 콘텐츠 API 호출을 두 번 이상 수행할 수 있습니다. 발송과 연결된 콘텐츠 호출 간에 보장된 1:1 비율은 없습니다. 자세한 내용 및 완화 방법은 [연결된 콘텐츠 호출 볼륨 이해하기](#understanding-connected-content-call-volume) 및 [대용량 엔드포인트 모범 사례](#best-practices-for-high-volume-endpoints)를 참조하세요.

### 연결된 콘텐츠에서 사용량 제한은 어떻게 작동하나요?

연결된 콘텐츠에는 자체 사용량 제한이 없습니다. 대신 사용량 제한은 메시지 전송 속도를 기준으로 합니다. 전송되는 메시지 수보다 연결된 콘텐츠 호출 수가 많은 경우 메시징 속도 제한을 의도한 연결된 콘텐츠 사용량 제한보다 낮게 설정하는 것이 좋습니다.  

### 캐싱 동작이란 무엇인가요?

GET 요청은 기본적으로 캐시됩니다([응답 캐싱]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/caching_responses/) 참조). **POST 요청은 기본적으로 캐시되지 않지만**, 연결된 콘텐츠 호출에 `:cache_max_age`를 추가하여 캐싱을 활성화할 수 있습니다. 이는 동일한 POST(예: 토큰 또는 콘텐츠 요청)가 캐시 기간 내에 반복적으로 수행될 때 엔드포인트 부하를 줄일 수 있습니다.

{% raw %}
```liquid
{% connected_content https://api.example.com/token :method post :body grant_type=client_credentials :cache_max_age 900 :save token %}
```
{% endraw %}

캐싱은 중복된 연결된 콘텐츠 호출을 줄이는 데 도움이 되지만 사용자당 단일 호출을 보장하지는 않습니다. 캐시 지속 시간은 5분에서 4시간 사이입니다. 자세한 내용은 [응답 캐싱]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/caching_responses/)을 참조하세요.

### 연결된 콘텐츠 HTTP 기본 동작은 무엇인가요? 

{% multi_lang_include connected_content.md section='default behavior' %}

{% multi_lang_include connected_content.md section='http post' %}