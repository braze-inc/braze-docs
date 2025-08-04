---
nav_title: Zoom 등록 자동화
article_title: Zoom 등록 자동화
page_order: 1
page_type: tutorial
description: "이 문서에서는 이메일, 푸시 및 인앱 메시지 캠페인에서 Zoom 참석자 등록을 자동화하는 방법을 설명합니다."
channel: 
  - email
  - push
  - in-app messages

---

# Zoom 등록 자동화

> 지난 몇 년 동안 Braze 고객들이 웨비나를 주최하는 것이 일반화되었습니다. Zoom 웹 세미나를 호스팅할 때 사용자는 Zoom 랜딩 페이지에 자신의 정보를 입력하여 가입해야 합니다. 

권장되는 사용자 흐름은 다음과 같습니다:
1. Zoom에서 웹 세미나를 예약하고 `webinarId`를 생성합니다.
2. Braze를 사용하여 이메일, 푸시, 인앱 메시지 채널을 통해 Zoom 웹 세미나를 홍보할 수 있습니다. 
3. 이러한 커뮤니케이션에 사용자를 웨비나에 자동으로 추가하는 클릭유도 실행 버튼을 포함하세요.

이메일, 푸시 또는 인앱 메시지 내의 버튼 클릭을 통해 사용자를 웹 세미나에 자동으로 추가하는 [Zoom API를](https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/meetingRegistrantCreate) 사용하면 이 작업을 수행할 수 있습니다. 다음 엔드포인트를 사용하여 API 요청에서 웨비나 ID를 대체하세요. 

POST: `/meetings/{webinarId}/registrants`

자세한 내용은 Zoom [웹 세미나 등록자 추가 엔드포인트](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarRegistrantCreate)를 참조하세요.<br><br>

{% tabs %}
{% tab 이메일 %}

메시지 본문 내에 클릭 유도 문안 버튼이 포함된 이메일 캠페인을 만듭니다. 사용자가 버튼을 클릭하면 웨비나 랜딩 페이지로 리디렉션합니다(리디렉션 링크에 적절한 매개변수 포함). 

URL의 매개변수를 사용하여 사용자 데이터를 전달하고, 페이지가 로드될 때 실행할 API 호출을 작성하여 사용자를 웨비나에 추가합니다.

![이름, 성, 이메일 주소, 도시를 포함하는 Liquid 템플릿을 사용한 이메일 메시지.]({% image_buster /assets/img/zoom/zoom1.png %})

이제 사용자는 자신의 Braze 프로필에 이미 존재하는 세부 정보로 웨비나에 등록됩니다.

{% endtab %}
{% tab 푸시 %}

1. 푸시 캠페인 만들기<br><br>

	버튼의 클릭 시 동작을 설정하여 웨비나 랜딩 페이지로 연결되도록 합니다.<br>

	![버튼을 클릭하면 웨비나로 연결됩니다.]({% image_buster /assets/img/zoom/zoom2.png %})<br><br>

	푸시에서 버튼 클릭을 통해 가입하는 사용자를 위한 랜딩 페이지의 간단한 예시입니다. 사용자에게 가입한 항목을 알리고 등록을 확인합니다.<br>

	![]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>


2. 인앱 메시지 또는 버튼 클릭으로 트리거되는 웹훅 캠페인을 생성합니다.<br><br>
 	Braze 프로필의 기존 사용자 데이터를 사용하여 해당 사용자를 웨비나에 등록합니다.<br>

	![특정 캠페인의 버튼을 클릭한 사용자에게 전송되는 액션 기반 캠페인입니다.]({% image_buster /assets/img/zoom/zoom6.png %})<br><br>

	Zoom 엔드포인트에 대한 웹훅 호출 예시.<br>
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

3. 이제 사용자는 자신의 Braze 프로필에 이미 존재하는 세부 정보로 웨비나에 등록됩니다.

{% endtab %}
{% tab 인앱 메시지 %}

1. 인앱 메시지 캠페인 만들기<br><br>

	웨비나 랜딩 페이지로 연결되는 버튼의 클릭 시 동작을 설정합니다.<br>

	![버튼을 클릭하면 웨비나로 연결됩니다.]({% image_buster /assets/img/zoom/zoom3.png %})<br><br>

	인앱 메시지에서 버튼 클릭을 통해 가입하는 사용자를 위한 랜딩 페이지의 간단한 예시입니다. 사용자에게 가입한 항목을 알리고 등록을 확인합니다.<br>

	![]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>

2. 인앱 메시지 또는 버튼 클릭으로 트리거되는 웹훅 캠페인을 생성합니다.<br><br>
	Braze 프로필의 기존 사용자 데이터를 사용하여 해당 사용자를 웨비나에 등록합니다.<br>

	![특정 캠페인의 버튼을 클릭한 사용자에게 전송되는 액션 기반 캠페인입니다.]({% image_buster /assets/img/zoom/zoom5.png %})<br><br>

	Zoom 엔드포인트에 대한 웹훅 호출 예시.<br>
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
3. 이제 사용자는 자신의 Braze 프로필에 이미 존재하는 세부 정보로 웨비나에 등록됩니다.

{% endtab %}
{% endtabs %}
