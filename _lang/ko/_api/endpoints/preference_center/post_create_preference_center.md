---
nav_title: "POST: 환경설정 센터 만들기"
article_title: "POST: 환경설정 센터 만들기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 환경설정 센터 Braze 엔드포인트 만들기에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 환경설정 센터 생성
{% apimethod post %}
/preference_center/v1
{% endapimethod %}

> 이 엔드포인트를 사용하여 사용자가 이메일 캠페인에 대한 알림 기본 설정을 관리할 수 있는 기본 설정 센터를 만들 수 있습니다. API로 생성된 환경설정 센터를 구축하는 방법에 대한 단계는 [API를 통한 환경설정 센터 만들기]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/#create-a-preference-center-via-api)를 참조하세요.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e15d7065-2cbc-4eb3-ae16-32efe43357a6 {% endapiref %}

## 전제 조건

이 엔드포인트를 사용하려면 `preference_center.update` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 요금 제한

이 엔드포인트는 워크스페이스당 분당 10건의 요청으로 사용량 제한이 있습니다.

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "name": "string",
  "preference_center_title": "string",
  "preference_center_page_html": "string",
  "confirmation_page_html": "string",
  "state": (optional) Choose `active` or `draft`. Defaults to `active` if not specified,
  "options": {
    "meta-viewport-content": "string", (optional) Only the `content` value of the meta tag
  }
}
```

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 | 설명
| --------- | ---------| --------- | ----------- |
|`name`| 필수 | 문자열 | 다음 요구 사항을 충족하는 기본 설정 센터의 이름입니다: <br>\- 문자, 숫자, 하이픈, 밑줄만 포함합니다. <br>\- 공백이 없습니다 |
|`preference_center_title`| 선택 사항 | 문자열 | 환경설정 센터 및 확인 페이지의 제목입니다. 제목을 지정하지 않으면 페이지의 제목은 기본적으로 "환경설정 센터"로 설정됩니다. |
|`preference_center_page_html`| 필수 | 문자열 | 환경 설정 센터 페이지의 HTML입니다. |
|`confirmation_page_html`| 필수 | 문자열 | 확인 페이지의 HTML입니다. |
|`state` | 선택 사항 | 문자열 | `active` 또는 `draft` 를 선택합니다. 지정하지 않으면 기본값은 `active` 입니다. |
|`options` | 선택 사항 | 개체 | 속성: `meta-viewport-content`. 존재하는 경우 `viewport` 메타 태그가 페이지에 `content= <value of attribute>`로 추가됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
환경설정 센터 이름은 생성한 후에는 편집할 수 없습니다.
{% endalert %}

### 리퀴드 태그

환경설정 센터 페이지에서 사용자의 구독 상태를 생성하기 위해 HTML에 포함할 수 있는 다음 Liquid 태그를 참조하세요.

{% raw %}

#### 사용자 구독 상태

| 액체 | 설명 | 설명
| --------- | ---------|
|`{{subscribed_state.${email_global}}}`| 사용자의 글로벌 이메일 구독 상태(예: '옵트인', '구독' 또는 '구독 취소')를 가져옵니다. |
|`{{subscribed_state.${<subscription_group_id>}}}`| 사용자에 대해 지정된 구독 그룹의 구독 상태(예: "구독됨" 또는 "구독 취소됨"을 표시)를 가져옵니다. |
{: .reset-td-br-1 .reset-td-br-2}

#### 양식 입력 및 작업

| 액체 | 설명 | 설명
| --------- | ---------|
|`{% form_field_name :email_global_state %}`| 특정 양식 입력 요소가 사용자의 글로벌 이메일 구독 상태에 해당함을 나타냅니다. 글로벌 이메일 구독 상태에 대한 선택 데이터와 함께 양식을 제출할 때 사용자의 선택 상태는 '옵트인', '구독' 또는 '구독 취소'여야 합니다. 체크박스인 경우 사용자는 '옵트인' 또는 '구독 취소' 상태가 됩니다. 숨겨진 입력의 경우 '구독' 상태도 유효합니다. |
|`{% form_field_name :subscription_group <subscription_group_id> %}`| 특정 양식 입력 요소가 지정된 구독 그룹에 해당함을 나타냅니다. 특정 구독 그룹에 대한 선택 데이터와 함께 양식을 제출할 때 사용자의 선택 상태는 "구독 중" 또는 "구독 취소" 중 하나여야 합니다. |
|`{{preference_center_submit_url}}`| 양식 제출용 URL을 생성합니다. |
{: .reset-td-br-1 .reset-td-br-2}

{% endraw %}

## 응답 예시

### 환경설정 센터 생성

{% raw %}
```
{
  "preference_center_api_id": "preference_center_api_id_example",
  "liquid_tag": "{{preference_center.${MyPreferenceCenter2022-09-22}}}",
  "created_at": "2022-09-22T18:28:07+00:00",
  "message": "success"
}
```
{% endraw %}

### 양식 입력이 있는 HTML 

{% raw %}
\`\`\`
<!doctype html>
<html lang="en">
  <head>
    <meta name="robots" content="noindex" />
    <title>이메일 환경설정</title>
    <script type="text/javascript">
      window.onload = () => {
        const globalUnsubscribed = '{{subscribed_state.${email_global}}}' == "unsubscribed";
        const globalSubscribedValue = '{{subscribed_state.${email_global}}}' == "opted_in" ? "opted_in" : "subscribed";
        const idStates = [
          // input format: [API_ID, '{{subscribed_state.${API_ID}}}' == "subscribed"][]
          ['3d2ae07a-f2ff-4318-bdff-e394f2d3a4ec', '{{subscribed_state.${3d2ae07a-f2ff-4318-bdff-e394f2d3a4ec}}}' == 'subscribed'],['7d89bdc3-4aa1-4592-8b8a-4c8b7161c875', '{{subscribed_state.${7d89bdc3-4aa1-4592-8b8a-4c8b7161c875}}}' == 'subscribed'],['5444d32e-2815-4258-964c-b9690d4ccb94', '{{subscribed_state.${5444d32e-2815-4258-964c-b9690d4ccb94}}}' == 'subscribed']
        ];

        const setState = (id, subscribed) => {
          document.querySelector(`#checkbox-${id}`).checked = subscribed;
          document.querySelector(`#value-${id}`).value = subscribed ? "subscribed" : "unsubscribed";
        };
        const setGlobal = (unsubscribed) => {
          document.querySelector(`#checkbox-global`).checked = unsubscribed;
          document.querySelector(`#value-global`).value = unsubscribed ? "unsubscribed" : globalSubscribedValue;
          idStates.forEach(([id]) => {
            document.querySelector(`#checkbox-${id}`).disabled = unsubscribed;
          });
        };

        idStates.forEach(([id, state]) => {
          setState(id, state);
          document.querySelector(`#checkbox-${id}`).onchange = ((e) => {
            setState(id, e.target.checked);
          });
        });
        setGlobal(globalUnsubscribed);
        document.querySelector(`#checkbox-global`).onchange = ((e) => {
          setGlobal(e.target.checked);
        });
      };
    </script>
    <style>
      body {
        background: #fff;
        margin: 0;
      }
      @media (max-width: 600px) {
        .main-container {
          margin-top: 0;
          width: 100%;
        }
        .main-container .content .email-input {
          width: 100%;
        }
      }
    </style>
  </head>
  <body class="vsc-initialized" style="margin: 0" bgcolor="#fff">
    <div
      class="main-container"
      style="
        background-color: #fff;
        color: #333335;
        font-family:
          Sailec W00 Medium,
          helvetica,
          arial,
          sans-serif;
        margin-left: auto;
        margin-right: auto;
        margin-top: 30px;
        width: 600px;
        padding: 15px 0 5px;
      "
    >
      <div class="content" style="margin-left: 20px; margin-right: 20px">
        
        <div>
          <h1
            style="color: #3accdd; font-size: 27px; font-weight: 400; margin-bottom: 40px; margin-top: 0"
            align="center"
          >
            이메일 환경설정 관리
          </h1>
          <p class="intro-text" style="font-size: 14px; margin-bottom: 20px" align="center">
            수신할 이메일을 선택합니다.
          </p>
        </div>

        <form action="{{ preference_center_submit_url }}" method="post" accept-charset="UTF-8">
          <div>
            <h3 style="font-size: 15px; margin-bottom: 15px; margin-left: 5px; margin-top: 40px">
              이메일 주소: <span class="displayed-email" style="font-weight: 400">{{${email_address}}}</span>
            </h3>
          </div>
          <div class="subscription-groups-holder" style="margin-bottom: 20px"><div class="row" style="border-top-width: 1px; border-top-color: #dddde2; border-top-style: solid; background-color: #fff; padding: 15px 10px 14px;border-bottom: 1px solid rgb(221, 221, 226);">
  <label style="color: #27368f; cursor: pointer; font-size: 15px; font-weight: 700;">
    <input type="checkbox" id="checkbox-3d2ae07a-f2ff-4318-bdff-e394f2d3a4ec" class="sub_group" style="margin-right: 4px;">
    <input type="hidden" name="{% form_field_name :subscription_group 3d2ae07a-f2ff-4318-bdff-e394f2d3a4ec %}" id="value-3d2ae07a-f2ff-4318-bdff-e394f2d3a4ec" />
    하위 그룹 1
  </label>
  <p class="subscription-group" style="font-size: 13px; line-height: 1.4em; min-height: 20px; padding-right: 20px; margin: 0 0 3px 23px;">
    
  </p>
</div>
<div class="row" style="border-top-width: 1px; border-top-color: #dddde2; border-top-style: solid; background-color: #fff; padding: 15px 10px 14px;border-bottom: 1px solid rgb(221, 221, 226);">
  <label style="color: #27368f; cursor: pointer; font-size: 15px; font-weight: 700;">
    <input type="checkbox" id="checkbox-7d89bdc3-4aa1-4592-8b8a-4c8b7161c875" class="sub_group" style="margin-right: 4px;">
    <input type="hidden" name="{% form_field_name :subscription_group 7d89bdc3-4aa1-4592-8b8a-4c8b7161c875 %}" id="value-7d89bdc3-4aa1-4592-8b8a-4c8b7161c875" />
    하위 그룹 2
  </label>
  <p class="subscription-group" style="font-size: 13px; line-height: 1.4em; min-height: 20px; padding-right: 20px; margin: 0 0 3px 23px;">
    
  </p>
</div>
<div class="row" style="border-top-width: 1px; border-top-color: #dddde2; border-top-style: solid; background-color: #fff; padding: 15px 10px 14px;border-bottom: 1px solid rgb(221, 221, 226);">
  <label style="color: #27368f; cursor: pointer; font-size: 15px; font-weight: 700;">
    <input type="checkbox" id="checkbox-5444d32e-2815-4258-964c-b9690d4ccb94" class="sub_group" style="margin-right: 4px;">
    <input type="hidden" name="{% form_field_name :subscription_group 5444d32e-2815-4258-964c-b9690d4ccb94 %}" id="value-5444d32e-2815-4258-964c-b9690d4ccb94" />
    하위 그룹 3
  </label>
  <p class="subscription-group" style="font-size: 13px; line-height: 1.4em; min-height: 20px; padding-right: 20px; margin: 0 0 3px 23px;">
    
  </p>
</div>
</div>

          <div class="unsub-all" style="cursor: pointer; font-size: 13px; margin-bottom: 20px" align="center">
            <label>
              <input type="checkbox" id="checkbox-global" />
              <input
                type="hidden"
                id="value-global"
                name="{% form_field_name :email_global_state %}"
              />
              <i> 위의 모든 유형의 이메일 수신 거부하기 </i>
            </label>
          </div>

          <div>
            <input
              class="save"
              type="submit"
              value="저장"
              style="
                background-color: rgb(71, 204, 163);
                color: #fff;
                cursor: pointer;
                display: block;
                font-size: 16px;
                text-align: center;
                text-decoration: none;
                width: 200px;
                margin: 0 auto 20px;
                padding: 12px;
                border-style: none;
              "
            />
          </div>
        </form>
      </div>
    </div>
  </body>
</html>
```
{% endraw %}

{% endapi %}
