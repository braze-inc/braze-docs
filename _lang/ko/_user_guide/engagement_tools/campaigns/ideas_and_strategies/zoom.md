---
nav_title: 줌 등록 자동화
article_title: 줌 등록 자동화
page_order: 1
page_type: tutorial
description: "이 문서에서는 이메일, 푸시 및 앱 내 메시지 캠페인에서 Zoom 참석자 등록을 자동화하는 방법을 설명합니다."
channel: 
  - email
  - push
  - in-app messages

---

# 줌 등록 자동화

> 웹 세미나는 지난 몇 년 동안 Braze 고객이 주최하는 일반적인 방법이 되었습니다. 줌 웹 세미나를 주최할 때 사용자는 등록하기 위해 줌 랜딩 페이지에 정보를 입력해야 합니다. 

추천 사용자 흐름은 아래에 설명되어 있습니다:
1. 줌에서 웹 세미나를 예약하고 `webinarId`을 생성합니다.
2. Braze를 사용하여 이메일, 푸시 및 앱 내 메시지 채널을 통해 Zoom 웹 세미나를 홍보합니다. 
3. 이러한 커뮤니케이션에 사용자를 웹 세미나에 자동으로 추가하는 클릭 유도 버튼을 포함합니다.

이것은 이메일, 푸시 또는 앱 내 메시지 내에서 버튼 클릭을 통해 사용자를 웹 세미나에 자동으로 추가하기 위해 [Zoom API](https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/meetingRegistrantCreate)를 사용하여 수행할 수 있습니다. API 요청에서 웹 세미나 ID를 교체하여 다음 엔드포인트를 사용하십시오. 

POST: `/meetings/{webinarId}/registrants`

자세한 내용은 Zoom [웹 세미나 등록자 추가 엔드포인트](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarRegistrantCreate)를 참조하십시오.<br><br>

{% tabs %}
{% tab Email %}

메시지 본문 내에 클릭 유도 버튼이 있는 이메일 캠페인을 만듭니다. 사용자가 버튼을 클릭하면 적절한 매개변수가 포함된 리디렉션 링크로 웹 세미나 랜딩 페이지로 리디렉션합니다. 

URL의 매개변수를 사용하여 사용자 데이터를 전달하고 페이지가 로드될 때 사용자를 웹 세미나에 추가하기 위해 API 호출을 실행합니다.

\![이메일 메시지에는 이름, 성, 이메일 주소 및 도시를 포함하기 위해 Liquid 템플릿이 사용되었습니다.]({% image_buster /assets/img/zoom/zoom1.png %})

사용자는 이제 Braze 프로필에 이미 존재하는 세부정보로 웹 세미나에 등록되었습니다.

{% endtab %}
{% tab Push %}

1. 푸시 캠페인 만들기<br><br>

	버튼의 클릭 동작을 설정하여 웨비나 랜딩 페이지로 연결합니다.<br>

	\![버튼 클릭 시 웨비나로 연결하기.]({% image_buster /assets/img/zoom/zoom2.png %})<br><br>

	푸시에서 버튼 클릭을 통해 가입한 사용자들을 위한 랜딩 페이지의 간단한 예시입니다. 사용자에게 그들이 무엇에 가입했는지 알려주고 등록을 확인합니다:<br>

	\![]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>


2. 인앱 메시지 또는 버튼 클릭으로 트리거되는 웹훅 캠페인 만들기.<br><br>
 	Braze 프로필의 기존 사용자 데이터를 사용하여 사용자를 웨비나에 등록합니다.<br>

	\![특정 캠페인을 위해 버튼을 클릭한 사용자에게 전송될 행동 기반 캠페인입니다.]({% image_buster /assets/img/zoom/zoom6.png %})<br><br>

	Zoom 엔드포인트에 대한 웹훅 호출 예시입니다.<br>
	{% raw %}
	```json
	POST https://api.zoom.com/meetings/{webinarId}/registrants

	{
		"email": "{{${email_addresses}}}",
		"first_name": "{{${first_name}}}",
		"last_name": "{{${last_name}}}",
		"city": "{{${city}}}",
		"country": "{{${country}}}",
		"phone": "{{${phone_number}}}"
	}
	```
	{% endraw %}

3. 사용자는 이제 Braze 프로필에 이미 존재하는 세부정보로 웹 세미나에 등록되었습니다.

{% endtab %}
{% tab In-app message %}

1. 인앱 메시지 캠페인 만들기<br><br>

	버튼의 클릭 동작을 설정하여 웨비나 랜딩 페이지로 연결합니다.<br>

	\![버튼 클릭 시 웨비나로 연결하기.]({% image_buster /assets/img/zoom/zoom3.png %})<br><br>

	인앱 메시지에서 버튼 클릭을 통해 가입한 사용자들을 위한 랜딩 페이지의 간단한 예시입니다. 사용자에게 그들이 무엇에 가입했는지 알려주고 등록을 확인합니다:<br>

	\![]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>

2. 인앱 메시지 또는 버튼 클릭으로 트리거되는 웹훅 캠페인 만들기.<br><br>
	Braze 프로필의 기존 사용자 데이터를 사용하여 사용자를 웨비나에 등록합니다.<br>

	\![특정 캠페인을 위해 버튼을 클릭한 사용자에게 전송될 행동 기반 캠페인입니다.]({% image_buster /assets/img/zoom/zoom5.png %})<br><br>

	Zoom 엔드포인트에 대한 웹훅 호출 예시입니다.<br>
	{% raw %}
	```json
	POST https://api.zoom.com/meetings/{webinarId}/registrants

	{
		"email": "{{${email_addresses}}}",
		"first_name": "{{${first_name}}}",
		"last_name": "{{${last_name}}}",
		"city": "{{${city}}}",
		"country": "{{${country}}}",
		"phone": "{{${phone_number}}}"
	}
	```
	{% endraw %}
3. 사용자는 이제 Braze 프로필에 이미 존재하는 세부정보로 웹 세미나에 등록되었습니다.

{% endtab %}
{% endtabs %}
