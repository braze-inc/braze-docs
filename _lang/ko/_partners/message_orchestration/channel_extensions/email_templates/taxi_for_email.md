---
nav_title: Taxi for Email
article_title: Taxi for Email
alias: /partners/taxi_for_email
description: "이 참고 문서에서는 드래그 앤 드롭 인터페이스와 간단하면서도 강력한 구문을 사용하여 지능형 이메일 템플릿을 만들 수 있는 온라인 이메일 마케팅 도구인 Braze와 Taxi for Email의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# Taxi for Email

> [Taxi for Email](http://taxiforemail.com/)은 직관적인 끌어서 놓기 방식의 시각적 이메일 편집기를 제공하는 온라인 이메일 마케팅 툴입니다. Taxi는 카피라이터와 편집자가 코드 없이도 이메일을 작성하는 데 필요한 액세스 권한과 리소스를 제공하여 팀이 이메일 캠페인에서 쉽게 협업할 수 있도록 지원합니다.

_This integration is maintained by Taxi for Email._

## 통합 정보

Braze와 Taxi의 통합을 통해 Taxi의 간단하면서도 강력한 구문을 활용하여 지능형 이메일 템플릿을 생성하고 Braze로 내보낼 수 있습니다. 

## 필수 조건

| 요구 사항 | 설명 |
| ------------| ----------- |
| Taxi for Email 계정 | 이 파트너십을 활용하려면 Taxi for Email 계정이 필요합니다. |
| Braze REST API 키 | 전체 **템플릿** 권한이 있는 Braze REST API 키입니다. <br><br> 이것은 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
| 브레이즈 엔드포인트 | [Braze 엔드포인트]({{site.baseurl}}/api/basics/#endpoints)는 Braze 대시보드 URL에 맞춰 조정됩니다.<br><br> 예를 들어 대시보드 URL이 `https://dashboard-03.braze.com`인 경우 엔드포인트는 `dashboard-03`입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 통합

### 1단계: 택시 이메일 템플릿 만들기

택시 플랫폼에서 택시 템플릿을 만듭니다. 템플릿을 만든 후 **조직 설정으로** 이동하여 **ESP 커넥터** 탭을 선택합니다.

### 2단계: Braze 커넥터 만들기

1. 대화 상자가 나타나면 **새로 추가** 버튼을 선택한 다음 드롭다운에서 **브레이즈를** 선택합니다. 
2. **브레이즈를** 선택하여 브레이즈 커넥터 설정을 편집합니다.
3. Braze 엔드포인트와 Braze API 키를 입력합니다.

올바른 권한이 있는 세부 정보가 제공되면 커넥터 필드의 색상이 변경됩니다. 이 필드가 변경되지 않으면 필드가 나열된 요구 사항에 맞게 조정되는지 확인합니다.

## 사용량

Braze 계정의 **템플릿 및 미디어 > 이메일 템플릿** 섹션에서 업로드한 택시 템플릿을 찾으세요. 이제 이 이메일 템플릿을 사용하여 고객에게 매력적인 이메일 메시지를 보낼 수 있습니다!


[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
