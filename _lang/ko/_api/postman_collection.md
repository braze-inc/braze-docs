---
nav_title: Postman 및 샘플 요청
article_title: Postman 및 샘플 요청
page_order: 3
description: "이 참조 문서에서는 Braze Postman Collection, 그것이 무엇인지, 컬렉션을 설정하고 사용하는 메서드, 요청을 편집하고 보내는 방법을 다룹니다."
page_type: reference

---

# Postman 및 샘플 요청

> Braze를 사용하면 Postman Collection을 통해 모든 엔드포인트에 대한 샘플 API 요청을 생성할 수 있습니다. 이 참조 문서에서는 Braze Postman Collection, 그것이 무엇인지, 컬렉션을 설정하고 사용하는 메서드, 요청을 편집하고 보내는 방법을 다룹니다.

## Postman이란?

Postman은 API 요청을 빌드하고 테스트하기 위한 무료 시각적 편집 툴입니다. API와 상호 작용하는 다른 방법(예: cURL 사용)과 달리 Postman을 사용하면 API 요청을 쉽게 편집하고 헤더 정보를 보는 등의 작업을 수행할 수 있습니다. Postman에는 미리 만들어진 샘플 API 요청의 컬렉션 또는 라이브러리를 저장할 수 있는 기능이 있습니다. 고객이 REST API를 쉽게 시작하고 실행할 수 있도록 모든 API 엔드포인트에 대해 미리 만들어진 예제가 포함된 컬렉션을 만들었습니다.

시작하려면 [Postman 기술문서](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro)에서 **Postman에서 실행을** 클릭하여 Postman 컬렉션을 보거나 다운로드하세요.

## Braze Postman 컬렉션 사용

Postman 계정이 있는 경우( [Postman 웹 사이트에서][1] macOS, Windows 및 Linux 버전을 다운로드할 수 있음) 주황색 **Postman에서 실행** 버튼을 클릭하여 자신의 Postman 앱에서 Postman 설명서를 열 수 있습니다. 그런 다음 [환경을 만들거나](#setting-up-your-postman-environment) Braze REST API 환경을 템플릿으로 사용하고 필요에 맞게 사용 가능한 `POST` 요청과 `GET` 요청을 편집할 수 있습니다.

### Postman 환경 설정

{% raw %}
Braze Postman Collection은 템플릿 변수 `{{instance_url}}`을 사용하여 Braze 인스턴스의 REST API URL을 사전 빌드된 요청으로 대체하고 API 키의 `{{api_key}}` 변수를 대체합니다. 컬렉션의 모든 요청을 수동으로 편집하는 대신 Postman 환경에서 이 변수를 설정할 수 있습니다. 드롭다운에서 템플릿 기반 환경(Braze REST API 환경 템플릿)을 선택하고 변수 값을 자신의 값으로 바꾸거나 고유한 환경을 설정할 수 있습니다.
{% endraw %}

사용자 고유의 환경을 설정하려면 다음 단계를 수행합니다.

1. **Workspaces(작업 영역)** 탭에서 **Environments(환경**)를 선택합니다.
2. **+** 더하기 버튼을 클릭하여 새 환경을 만듭니다.
3. 이 환경에 이름을 지정하고(예: "Braze API 요청") [Braze 인스턴스][7] 및 [Braze REST API 키][8]에 해당하는 값과 함께 키를 `instance_url` 및 `api_key`에 대해 추가합니다.
4. **저장**을 클릭합니다.

{% alert note %}
`POST` 요청 본문에서는 `api_key`는 따옴표로 캡슐화되어야 합니다(`"MY-API-KEY-EXAMPLE"`). `GET` URL에서는 그렇지 않아야 합니다. 이 설명서의 `POST` 요청 본문, `GET` URL 및 `YOUR-API-KEY-HERE`에 대한 환경 템플릿에 이미 이 형식을 제공했습니다.
{% endalert %}

![Postman의 Braze REST API 환경에 API 키 및 인스턴스 URL에 대한 변수 추가.][3]

### 컬렉션에서 미리 빌드된 요청 사용

환경을 구성한 후. 컬렉션에서 미리 빌드된 요청을 새 API 요청을 빌드하기 위한 템플릿으로 사용할 수 있습니다. 미리 빌드된 요청 중 하나를 사용하려면 Postman의 **컬렉션** 메뉴에서 해당 요청을 클릭합니다. 그러면 Postman 앱의 기본 창에서 요청이 새 탭으로 열립니다.

일반적으로 Braze API 엔드포인트가 수락하는 요청에는 두 가지 유형인 `GET` 및 `POST`가 있습니다. 엔드포인트에서 사용하는 `HTTP` 메서드에 따라 미리 빌드된 요청을 다르게 편집해야 합니다.

#### POST 요청 편집

`POST` 요청을 편집할 때 요청을 열고 요청 편집기의 **본문** 섹션으로 이동합니다. 가독성을 위해 **원시** 라디오 버튼을 선택하여 `JSON` 요청 본문의 형식을 지정합니다.

![Postman에서 POST 사용자 추적 요청을 편집할 때 본문 탭] [4]

#### GET 요청 편집

`GET` 요청을 편집할 때 요청 URL에 전달된 매개변수를 편집합니다. 이렇게 하려면 **Params(매개 변수** ) 탭을 선택하고 표시되는 필드에서 키-값 쌍을 편집합니다.

![Postman에서 구독 취소한 이메일 주소의 GET 쿼리 목록 요청을 편집할 때 매개 변수 탭.] [5]

### 문의 보내기

API 요청이 준비되면 **보내기**를 클릭합니다. 요청이 전송되고 응답 데이터가 요청 편집기 아래의 섹션에 채워집니다. 여기에서 Braze API에서 반환된 원시 데이터를 보고, HTTP 응답 코드를 보고, 요청을 처리하는 데 걸린 시간을 확인하고, 헤더 정보를 볼 수 있습니다.

![상태가 201 생성됨이고 응답 시간이 269밀리초인 POST 요청의 본문 응답 데이터 예입니다.] [6]

[1]: https://www.getpostman.com
[3]: {% image_buster /assets/img_archive/postman_variable.png %}
[4]: {% image_buster /assets/img_archive/postman_post.png %}
[5]: {% image_buster /assets/img_archive/postman_get.png %}
[6]: {% image_buster /assets/img_archive/postman_response.png %}
[7]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[8]: {{site.baseurl}}/api/api_key/
