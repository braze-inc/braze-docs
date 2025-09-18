---
nav_title: Stensul
article_title: Stensul
alias: /partners/stensul
description: "이 참고 문서에서는 Braze와 Stensul 간의 파트너십에 대해 설명합니다. Stensul은 여러 채널에서 모바일 반응형 이메일 템플릿을 쉽게 만들 수 있는 엔터프라이즈 이메일 플랫폼입니다."
page_type: partner
search_tag: Partner

---

# Stensul

> [Stensul](https://stensul.com/)을 통해 이메일 마케터가 Stensul에서 모바일 반응형 브랜드 이메일을 쉽게 구축한 후, 캠페인 생성을 위해 실시간으로 Braze로 전송할 수 있습니다.

_이 통합은 Stensul에서 유지 관리합니다._

## 통합 정보

Braze와 Stensul 통합을 통해 HTML 형식의 Stensul 이메일을 내보내고 Braze 내에서 템플릿으로 업로드할 수 있습니다.

## 전제 조건

| 요구 사항 | 설명 |
| ------------| ----------- |
| Stensul 계정 | 이 파트너십을 활용하려면 Stensul 계정이 필요합니다. |
| Braze REST API 키 | 전체 **템플릿** 권한이 있는 Braze REST API 키입니다. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| 클러스터 인스턴스 | 귀하의 Braze [클러스터 인스턴스]({{site.baseurl}}/api/basics/#endpoints)는 Braze 대시보드 및 REST 엔드포인트와 일치합니다.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 통합

Braze REST API 키와 클러스터 인스턴스를 Stensul 고객 성공 팀에 제공합니다. 팀에서 초기 통합을 설정합니다.

{% alert important %}
이 설정은 일회성 설정이며 향후 모든 내보내기에서는 이 API 키를 자동으로 활용합니다.
{% endalert %}

### 1단계: Stensul 이메일 생성

Stensul 플랫폼에서 Stensul 이메일을 생성하고 **완료**를 클릭하십시오.

![Stensul 저장 Options]({% image_buster /assets/img_archive/stensul_save_options.png %})

### 2단계: 템플릿을 Braze로 내보내기
새로운 대화 상자가 완료 페이지에 나타나면 **ESP에 업로드**를 선택합니다.

![Stensul 업로드 옵션]({% image_buster /assets/img_archive/stensul_upload_options.png %})

다음으로, **템플릿 이름**, **제목**, 그리고 **프리헤더**를 입력하고 이메일을 선택한 후 **업로드**를 선택합니다. 이후 업로드가 성공적으로 완료되었음을 알리는 확인과 해당되는 경우 파일의 과거 업로드 기록을 수신합니다.

![Stensul 업로드 성공]({% image_buster /assets/img_archive/stensul_upload_success.png %})

## 사용량

Braze 계정의 **템플릿 및 미디어 > 이메일 템플릿** 섹션에서 업로드한 Stensul 템플릿을 찾으십시오. 이제 이 이메일 템플릿을 사용하여 고객에게 매력적인 이메일 메시지를 보내기 시작할 수 있습니다!


[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
