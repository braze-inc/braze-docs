---
nav_title: 우편 배달원 및 샘플 요청
article_title: 우편 배달원 및 샘플 요청
page_order: 3
description: "이 참조 문서에서는 Braze Postman Collection, 그것이 무엇인지, 컬렉션을 설정하고 사용하는 메서드, 요청을 편집하고 보내는 방법을 다룹니다."
page_type: reference

---

# Postman 및 샘플 요청

> Braze를 사용하면 Postman 컬렉션을 통해 모든 엔드포인트에 대한 샘플 API 요청을 생성할 수 있습니다. 이 참조 문서에서는 Braze Postman Collection, 그것이 무엇인지, 컬렉션을 설정하고 사용하는 메서드, 요청을 편집하고 보내는 방법을 다룹니다.

## 포스트맨이란 무엇인가요?

Postman은 API 요청을 작성하고 테스트하는 데 무료로 사용할 수 있는 시각적 편집 도구입니다. API와 상호 작용하는 다른 방법(예: cURL 사용)과 달리 Postman을 사용하면 API 요청을 쉽게 편집하고 헤더 정보를 보는 등의 작업을 할 수 있습니다. Postman에는 미리 만들어진 샘플 API 요청의 컬렉션 또는 라이브러리를 저장할 수 있는 기능이 있습니다. 고객이 REST API를 쉽게 시작하고 실행할 수 있도록 모든 API 엔드포인트에 대해 미리 만들어진 예제가 포함된 컬렉션을 만들었습니다.

시작하려면 게시자 [문서에서](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro) 게시자에서 **실행을** 클릭하여 게시자 컬렉션을 보거나 다운로드하세요.

## 브레이즈 우체부 컬렉션 사용

Postman 계정이 있는 경우(MacOS, Windows 및 Linux 버전은 [Postman 웹사이트](https://www.getpostman.com)에서 다운로드할 수 있음) 주황색 **Postman에서 실행** 버튼을 클릭하여 자신의 Postman 앱에서 Postman 설명서를 열 수 있습니다. 그런 다음 [환경을 만들거나](#setting-up-your-postman-environment) Braze REST API 환경을 템플릿으로 사용하여 사용 가능한 `POST` 및 `GET` 요청을 필요에 맞게 편집할 수 있습니다.

### Postman 환경 설정하기

{% raw %}
Braze 포스트맨 컬렉션은 템플릿 변수 `{{instance_url}}` 를 사용하여 Braze 인스턴스의 REST API URL을 미리 빌드된 요청으로 대체하고, `{{api_key}}` 변수를 API 키로 대체합니다. 컬렉션의 모든 요청을 수동으로 편집할 필요 없이 Postman 환경에서 이 변수를 설정할 수 있습니다. 드롭다운에서 템플릿 환경(Braze REST API 환경 템플릿)을 선택하고 변수 값을 사용자 환경으로 바꾸거나 사용자 환경을 직접 설정할 수 있습니다.
{% endraw %}

나만의 환경을 설정하려면 다음 단계를 수행하세요:

1. **작업 공간** 탭에서 **환경을** 선택합니다.
2. 더하기 버튼을 클릭하여 새 환경을 만듭니다.
3. 이 환경에 이름을 지정하고(예: "Braze API 요청"), [Braze 인스턴스]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) 및 [Braze REST API 키에]({{site.baseurl}}/api/api_key/) 해당하는 값으로 `instance_url` 및 `api_key` 키를 추가합니다.
4. **저장**을 클릭합니다.

{% alert note %}
`POST` 요청 본문에서 `api_key` 은 따옴표로 묶어야 합니다: `"MY-API-KEY-EXAMPLE"`. `GET` URL에서는 그렇지 않아야 합니다. 이 문서의 `POST` 요청 본문, `GET` URL, `YOUR-API-KEY-HERE` 환경 템플릿에서 이미 이 형식을 제공했습니다.
{% endalert %}

![Postman의 Braze REST API 환경에 API 키 및 인스턴스 URL에 대한 변수를 추가합니다.]({% image_buster /assets/img_archive/postman_variable.png %})

### 컬렉션에서 미리 작성된 요청 사용

환경을 구성한 후에는 컬렉션에 미리 작성된 요청 중 하나를 새 API 요청을 작성하기 위한 템플릿으로 사용할 수 있습니다. 미리 작성된 요청 중 하나를 사용하려면 Postman의 **컬렉션** 메뉴에서 해당 요청을 클릭하세요. 그러면 요청이 Postman 앱의 기본 창에 새 탭으로 열립니다.

일반적으로 Braze API 엔드포인트가 수락하는 요청 유형은 `GET` 와 `POST` 의 두 가지입니다. 엔드포인트가 사용하는 `HTTP` 메서드에 따라 미리 빌드된 요청을 다르게 편집해야 합니다.

#### POST 요청 편집

`POST` 요청을 편집할 때는 요청을 열고 요청 편집기에서 **본문** 섹션으로 이동합니다. 가독성을 위해 **원시** 라디오 버튼을 선택하여 `JSON` 요청 본문의 형식을 지정합니다.

![Postman에서 POST 사용자 추적 요청을 편집할 때 본문 탭]({% image_buster /assets/img_archive/postman_post.png %})

#### GET 요청 편집

`GET` 요청을 편집할 때는 요청 URL에 전달된 매개변수를 편집합니다. 이렇게 하려면 **매개변수** 탭을 선택하고 표시되는 필드에서 키-값 쌍을 편집합니다.

![매개변수 탭에서 수신 거부된 이메일 주소의 쿼리 목록 가져오기 요청을 편집할 때]({% image_buster /assets/img_archive/postman_get.png %})

### 요청 보내기

API 요청이 준비되면 **보내기를** 클릭합니다. 요청이 전송되고 응답 데이터가 요청 편집기 아래의 섹션에 채워집니다. 여기에서 Braze API에서 반환된 원시 데이터를 보고, HTTP 응답 코드를 보고, 요청을 처리하는 데 걸린 시간을 확인하고, 헤더 정보를 볼 수 있습니다.

![상태가 201 생성됨이고 응답 시간이 269밀리초인 POST 요청의 본문 응답 데이터 예시]({% image_buster /assets/img_archive/postman_response.png %})

