---
nav_title: 커넥티드 콘텐츠 통화하기
article_title: 커넥티드 콘텐츠 API 호출 만들기
page_order: 0
description: "이 참조 문서에서는 연결된 콘텐츠 API를 호출하는 방법과 유용한 예제 및 고급 연결된 콘텐츠 사용 사례를 다룹니다."
search_rank: 2
---

# [![Braze 학습 과정]](https://learning.braze.com/connected-content) ( [{% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"}커넥티드 콘텐츠 API 호출 만들기

> Use Connected Content to insert any information accessible by API directly into messages you send to users. 웹 서버에서 직접 콘텐츠를 가져오거나 공개적으로 액세스할 수 있는 API에서 콘텐츠를 가져올 수 있습니다.<br><br>This page covers how to make Connected Content API calls, advanced Connected Content use cases, error handling, and more.

## Sending a Connected Content call

{% raw %}

커넥티드 콘텐츠 호출을 보내려면 `{% connected_content %}` 태그를 사용합니다. 이 태그를 사용하면 `:save`를 사용하여 변수를 할당하거나 선언할 수 있습니다. 이러한 변수의 측면은 나중에 [Liquid][2]를 사용하여 메시지에서 참조할 수 있습니다.

예를 들어, 다음 메시지 본문은 URL `http://numbersapi.com/random/trivia`에 접속하여 재미있는 퀴즈 사실을 메시지에 포함시킵니다:

```
{% connected_content http://numbersapi.com/random/trivia :save result %}
Hi there, here is fun some trivia for you!: {{result.text}}
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

커넥티드 콘텐츠 요청은 GET 및 POST 요청만 지원합니다.

## 오류 처리

URL을 사용할 수 없고 404 페이지에 도달하면 Braze는 그 자리에 빈 문자열을 렌더링합니다. URL이 HTTP 500 또는 502 페이지에 도달하면 재시도 로직에서 실패합니다.

엔드포인트가 JSON을 반환하는 경우 `connected` 값이 null인지 확인하여 이를 감지한 다음 [조건부로 메시지를 중단][1]할 수 있습니다. Braze는 포트 80(HTTP) 및 443(HTTPS)을 통해 통신하는 URL만 허용합니다.

### 건강하지 않은 호스트 탐지

커넥티드 콘텐츠는 비정상 호스트 감지 메커니즘을 사용하여 대상 호스트가 심각한 속도 저하 또는 과부하를 경험하여 시간 초과, 너무 많은 요청 또는 기타 결과로 인해 Braze가 대상 엔드포인트와 성공적으로 통신할 수 없는 경우를 감지합니다. 이는 대상 호스트가 어려움을 겪을 수 있는 불필요한 부하를 줄이기 위한 안전장치 역할을 합니다. 또한 Braze 인프라를 안정화하고 빠른 메시징 속도를 유지하는 데도 도움이 됩니다.

대상 호스트에 심각한 속도 저하 또는 과부하가 발생하면 Braze는 대상 호스트에 대한 요청을 1분 동안 일시적으로 중단하고 대신 장애를 나타내는 응답을 시뮬레이션합니다. Braze는 1분 후 소수의 요청을 통해 호스트의 건강 상태를 검사한 후 호스트가 건강한 것으로 확인되면 최대 속도로 요청을 재개합니다. 호스트가 여전히 건강하지 않으면 Braze는 다시 시도하기 전에 1분을 더 기다립니다.

비정상 호스트 감지기에 의해 대상 호스트에 대한 요청이 중단되는 경우, Braze는 오류 응답 코드를 받은 것처럼 메시지를 계속 렌더링하고 Liquid 로직을 따릅니다. 이러한 커넥티드 콘텐츠 요청이 비정상 호스트 감지기에 의해 중단될 때 다시 시도되도록 하려면 `:retry` 옵션을 사용하세요. `:retry` 옵션에 대한 자세한 내용은 [연결된 콘텐츠 재시도를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries) 참조하세요.

건강하지 않은 호스트 감지로 인해 문제가 발생했다고 생각되면 [Braze 지원팀에]({{site.baseurl}}/support_contact/) 문의하세요.

{% alert tip %}
일반적인 오류 코드를 해결하는 방법에 대해 자세히 알아보려면 [웹훅 및 커넥티드 콘텐츠 요청 문제 해결을]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors#unhealthy-host-detection) 참조하세요.
{% endalert %}

## Allowing for efficient performance

Because Braze delivers messages at a very fast rate, be sure that your server can handle thousands of concurrent connections so the servers don't get overloaded when pulling down content. When using public APIs, confirm your usage won't violate any rate-limiting that the API provider may employ. Braze requires that server response time is less than two seconds for performance reasons; if the server takes longer than two seconds to respond, the content won't be inserted.

Braze 시스템은 수신자당 동일한 연결된 콘텐츠 API를 두 번 이상 호출할 수 있습니다. 이는 Braze가 메시지 페이로드를 렌더링하기 위해 연결된 콘텐츠 API 호출을 해야 할 수 있으며, 유효성 검사, 재시도 로직 또는 기타 내부 목적을 위해 수신자당 메시지 페이로드가 여러 번 렌더링될 수 있기 때문입니다. 시스템은 수신자당 동일한 연결된 콘텐츠 호출을 두 번 이상 허용할 수 있어야 합니다.

## 알아두어야 할 사항

* Braze는 API 호출에 대해 요금을 부과하지 않으며, 주어진 데이터 포인트 할당량에 포함되지 않습니다.
* There is a limit of one MB for Connected Content responses.
* 연결된 콘텐츠 호출은 메시지가 전송될 때 발생하지만, 인앱 메시지는 메시지를 볼 때 이 호출을 수행합니다.
* 커넥티드 콘텐츠 호출은 리디렉션을 따르지 않습니다.

## 인증 유형

### 기본 인증 사용

URL에 기본 인증이 필요한 경우, Braze는 API 호출에 사용할 수 있도록 기본 인증 자격 증명을 생성할 수 있습니다. **설정** > **연결된 콘텐츠**에서 기존의 기본 인증 자격 증명을 관리하고 새 인증 자격 증명을 추가할 수 있습니다.

![Braze 대시보드의 '연결된 콘텐츠' 설정.][34]

To add a new credential, select **Add Credential**. 자격 증명에 이름을 지정하고 사용자 아이디와 비밀번호를 입력합니다.

![이름, 사용자 아이디, 비밀번호를 입력하는 옵션이 있는 '새 자격증명 만들기' 창이 열립니다.][35]{: style="max-width:30%" }

그런 다음 토큰의 이름을 참조하여 API 호출에서 이 기본 인증 자격 증명을 사용할 수 있습니다:

{% raw %}
```
Hi there, here is fun some trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
자격 증명을 삭제하면 해당 자격 증명을 사용하려는 모든 연결된 콘텐츠 호출이 중단된다는 점에 유의하세요.
{% endalert %}

### 토큰 인증 사용

Braze 연결된 콘텐츠를 사용할 때 특정 API에 사용자 아이디와 비밀번호 대신 토큰이 필요할 수 있습니다. 다음 호출에는 메시지를 참조하고 모델링할 수 있는 코드 스니펫이 포함되어 있습니다.

{% raw %}
```
{% assign campaign_name="New Year Sale" %}
{% connected_content
     https://your_API_link_here/
     :method post
     :headers {
       "X-App-Id": "YOUR-APP-ID",
       "X-App-Token": "YOUR-APP-TOKEN"
     }
     :body campaign={{campaign_name}}&customer={{${user_id}}}&channel=Braze
     :content_type application/json
     :save publication
%}
```
{% endraw %}

### OAuth(공개 인증) 사용

일부 API 구성에서는 액세스하려는 API 엔드포인트를 인증하는 데 사용할 수 있는 액세스 토큰을 검색해야 합니다.

#### Step 1: 액세스 토큰 검색

다음 예는 액세스 토큰을 검색하여 로컬 변수에 저장한 다음 후속 API 호출을 인증하는 데 사용할 수 있는 예시입니다. `:cache_max_age` 매개변수를 추가하여 액세스 토큰의 유효 기간을 일치시키고 아웃바운드 연결된 콘텐츠 호출 수를 줄일 수 있습니다. 자세한 내용은 [구성 가능한 캐싱][36]을 참조하세요.

{% raw %}
```
{% connected_content
     https://your_API_access_token_endpoint_here/
     :method post
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE",
       "Authorization": "Bearer YOUR-APP-TOKEN"
     }
     :cache_max_age 900
     :save token_response
%}
```
{% endraw %}

#### Step 2: 검색된 액세스 토큰을 사용하여 API를 승인합니다.

토큰이 저장된 후에는 후속 커넥티드 콘텐츠 호출에 토큰을 동적으로 템플릿화하여 요청을 승인할 수 있습니다:

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

## 커넥티드 콘텐츠 IP 허용 목록

Braze에서 연결된 콘텐츠를 사용한 메시지가 전송되면, Braze 서버는 자동으로 고객 또는 타사 서버에 네트워크 요청을 보내 데이터를 가져옵니다. IP 허용 목록을 사용하면 연결된 콘텐츠 요청이 실제로 Braze에서 오는지 확인할 수 있어 보안이 한층 더 강화됩니다.

Braze는 다음 IP 범위에서 커넥티드 콘텐츠 요청을 보냅니다. 나열된 범위는 허용 목록에 옵트인한 모든 API 키에 자동으로 동적으로 추가됩니다. 

Braze에는 모든 서비스에 사용되는 예약된 IP 집합이 있으며, 모든 IP가 특정 시간에 활성화되는 것은 아닙니다. 이는 고객에게 영향을 주지 않고 필요한 경우 Braze가 다른 데이터 센터에서 전송하거나 유지보수를 수행할 수 있도록 설계되었습니다. Braze는 연결된 콘텐츠를 요청할 때 다음 IP 중 하나, 일부 또는 전부를 사용할 수 있습니다.

{% multi_lang_include data_centers.md datacenters='ips' %}

## 문제 해결

[Webhook.site](https://webhook.site/)를 사용하여 연결된 콘텐츠 호출 문제를 해결하세요. 

1. 연결된 콘텐츠 호출의 URL을 사이트에서 생성된 고유 URL로 전환합니다.
2. 캠페인 또는 캔버스 단계를 미리 보고 테스트하여 이 웹사이트로 들어오는 요청을 확인합니다.

이 도구를 사용하면 요청 헤더, 요청 본문 및 통화에서 전송되는 기타 정보와 관련된 문제를 진단할 수 있습니다.

## Frequently asked questions

### 커넥티드 콘텐츠 호출이 사용자 또는 전송 수보다 많은 이유는 무엇인가요? 

메시지 페이로드를 렌더링하기 위해 커넥티드 콘텐츠 API 호출을 해야 할 수 있기 때문에 Braze는 수신자당 동일한 커넥티드 콘텐츠 API 호출을 두 번 이상 수행할 수 있습니다. 메시지 페이로드는 유효성 검사, 재시도 로직 또는 기타 내부 목적을 위해 수신자별로 여러 번 렌더링할 수 있습니다.

재시도 로직이 호출에 사용되지 않더라도 수신자당 커넥티드 콘텐츠 API 호출을 두 번 이상 수행할 수 있을 것으로 예상됩니다. 연결된 콘텐츠가 포함된 메시지의 전송 속도 제한을 설정하거나 예상되는 볼륨을 더 잘 처리할 수 있도록 서버를 구성하는 것이 좋습니다.

### 커넥티드 콘텐츠에서 속도 제한은 어떻게 작동하나요?

커넥티드 콘텐츠에는 자체 요금 제한이 없습니다. 대신 속도 제한은 메시지 전송 속도를 기준으로 합니다. 전송되는 메시지 수보다 연결된 콘텐츠 호출 수가 많은 경우 메시징 속도 제한을 의도한 커넥티드 콘텐츠 속도 제한보다 낮게 설정하는 것이 좋습니다.  

### 캐싱 동작이란 무엇인가요?

기본적으로 POST 요청은 캐시되지 않습니다. 그러나 `:cache_max_age` 매개 변수를 추가하여 POST 호출을 강제로 캐시하도록 할 수 있습니다.
캐싱은 중복된 커넥티드 콘텐츠 호출을 줄이는 데 도움이 됩니다. 그러나 사용자당 항상 하나의 커넥티드 콘텐츠 호출이 발생한다는 보장은 없습니다.


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[2]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#liquid-usage-use-cases--overview
[16]: [success@braze.com](mailto:success@braze.com)
[34]: {% image_buster /assets/img_archive/basic_auth_mgmt.png %}
[35]: {% image_buster /assets/img_archive/basic_auth_token.png %}
[36]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/local_connected_content_variables/#configurable-caching
