---
nav_title: Dyspatch
article_title: Dyspatch
alias: /partners/dyspatch
description: "이 참고 문서에서는 코드를 작성할 필요 없이 아름답고 반응이 좋으며 매력적인 이메일을 만들 수 있는 드래그 앤 드롭 이메일 빌더인 Braze와 Dyspatch의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# Dyspatch

> [Dyspatch][1]는 코드를 작성할 필요 없이 아름답고 응답성이 뛰어난 매력적인 이메일을 생성하는 데 사용되는, 직관적인 끌어서 놓기 방식의 이메일 작성기를 제공합니다. 팀과 협업하여 Dyspatch 내에서 이메일을 작성하고 승인한 다음 Braze로 내보내는 과정을 몇 단계만 거치면 완료할 수 있습니다! 

_This integration is maintained by Dyspatch._

## 통합 정보

Dyspatch와 Braze의 통합을 통해 Dyspatch 이메일 템플릿을 Braze로 직접 내보내 이메일 생성 생애주기를 간소화할 수 있습니다.

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Dyspatch 계정 | 이 파트너십을 활용하려면 [소유자 또는 관리자 역할][4]이 있는 [Dyspatch 계정][3]이 필요합니다. |
| Braze REST API 키 | 전체 **템플릿** 권한이 있는 Braze REST API 키입니다. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 통합

Braze와 Dyspatch의 통합을 통해 Dyspatch 이메일 템플릿을 Braze 미디어 라이브러리로 직접 내보내거나 템플릿을 다운로드하여 수동으로 업로드할 수 있습니다. 

### 1단계: Braze 통합 만들기

Dyspatch 관리 포털에서 사용자 이름 드롭다운 메뉴를 열고 **Integrations**을 선택하십시오. 새 연동 기능을 생성하고 **Braze를** 선택한 다음 Braze API 키를 입력합니다.

**내보내기 기준 현지화** 필드에서 현지화를 관리할 방법을 선택할 수 있습니다. 이 필드에서는 [이메일 템플릿을 현지화][6]하고 Braze로 내보내어 언어 또는 로캘별로 개인화된 이메일을 쉽게 보낼 수 있습니다. 

![디스패치 내보내기 템플릿]({% image_buster /assets/img/dyspatch/dyspatch_integration_create.png %}){: style="max-width:50%;"}

### 2단계: Braze로 템플릿 내보내기

Dyspatch에서 이메일을 작성한 후 템플릿을 Braze로 보내려면 게시된 이메일 템플릿을 보고 **다운로드/내보내기**를 클릭한 다음, **통합으로 내보내기**를 클릭합니다.

템플릿을 수동으로 업로드하려면 게시된 이메일 템플릿을 보고 **다운로드/내보내기**를 클릭한 다음, **HTML 다운로드**를 클릭합니다. 그런 다음 Braze 계정의 **템플릿 및 미디어 > 이메일 템플릿** 섹션에서 **파일에서를** 선택하여 템플릿을 업로드합니다.

![디스패치 내보내기 템플릿]({% image_buster /assets/img/dyspatch/dyspatch_export.gif %})

{% alert important %}
Braze의 모든 다이스패치 이메일 템플릿의 **정보 보내기** 섹션에서 **인라인 CSS를** 선택하지 마세요. Dyspatch는 이메일의 강력한 기능과 뛰어난 응답성, 전송 준비 상태를 지원함으로써 이를 처리합니다.
{% endalert %}

### 사용량

Braze 계정의 **템플릿 및 미디어 > 이메일 템플릿** 섹션에서 업로드한 다이스패치 템플릿을 찾으세요. 이제 이 이메일 템플릿을 사용하여 고객에게 매력적인 이메일 메시지를 보낼 수 있습니다!


[1]: https://www.dyspatch.io
[2]: https://dashboard.braze.com/sign_in
[3]: https://www.dyspatch.io/login/
[4]: https://docs.dyspatch.io/administration/dyspatch_roles/
[5]: https://docs.dyspatch.io/exports/export_to_braze/#download-your-template
[6]: https://docs.dyspatch.io/localization/localizing_a_template/
