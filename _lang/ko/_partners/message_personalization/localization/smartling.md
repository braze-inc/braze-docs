---
nav_title: Smartling
article_title: Smartling
description: "이 참고 문서에서는 Braze와 현지화를 위한 클라우드 기반 소프트웨어인 Smartling 간의 파트너십을 설명합니다. 브레이즈 커넥터는 HTML 이메일 템플릿, 콘텐츠 블록, 캔버스 및 캠페인 이메일 메시지의 번역을 지원합니다."
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> [Smartling][5]은 웹사이트, 애플리케이션 및 고객 경험의 번역을 자동화하려는 고객을 위한 종단 간 클라우드 번역 관리 소프트웨어입니다.

브레이즈 커넥터는 HTML 이메일 템플릿, 콘텐츠 블록, 캔버스 및 캠페인 이메일 메시지의 번역을 지원합니다. 번역은 Smartling에 요청되며, 번역된 콘텐츠는 자동으로 Braze로 전송됩니다.

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Smartling 계정 | 이 파트너십을 활용하려면 [Smartling 계정][2]이 필요합니다. |
| Smartling 번역 프로젝트 | Smartling과 Braze 계정을 연결하려면 먼저 가입하고 [번역 프로젝트를 생성해야 합니다][6]. |
| Braze REST API 키 | 모든 템플릿 및 콘텐츠 블록 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [당신의 REST 엔드포인트 URL][1]. 사용자의 엔드포인트는 인스턴스를 위한 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

스마트링 브레이즈 통합을 통해 HTML 이메일 템플릿, 콘텐츠 블록, 캔버스 및 캠페인 이메일 메시지를 번역할 수 있습니다. 다음 번역하는 내용에 따라 다음 세부 사항에 유의하십시오:

**이메일 템플릿**
* HTML 이메일 템플릿만 지원됩니다.
* 당신은 커넥터를 통해 Braze에 번역된 이메일이 어떻게 전달될지 결정해야 합니다.
  * **모든 언어를 위한 하나의 이메일:** 커넥터는 모든 언어를 소스와 동일한 이메일로 전달합니다.
  * **하나의 이메일당 언어:** 커넥터는 Braze에서 각 언어에 대한 새로운 이메일을 생성합니다.

**콘텐츠 블록**
* 모든 콘텐츠 블록이 지원됩니다.
* 콘텐츠 블록에는 원본과 번역된 버전이 모두 포함되어 있습니다.
* Liquid 스크립트는 수신자의 언어 환경설정에 따라 표시할 올바른 언어를 결정합니다.

**캠페인 및 캔버스**
* Braze에서 **다국어 지원** 설정 아래에 대상 언어를 추가했는지 확인하세요.
* 커넥터 구성에 대한 자세한 내용은 Smartling [설명서][3]를 참조하세요.

## 통합

### 1단계: Smartling TMS에서 Braze 프로젝트 설정

#### Braze를 Smartling에 연결

1. [Smartling][2]에서 Smartling 계정에 [Braze 커넥터][6] 프로젝트 유형을 만드세요.
  - 프로젝트에 필요한 모든 대상 언어가 추가되었는지 확인하십시오.
2. 이 프로젝트에서 **설정** > **브레이즈 설정** > **브레이즈에 연결**를 선택합니다.
3. Braze API URL과 Braze API 키를 입력하세요.
4. **저장**을 선택하십시오.

#### 완전한 Braze 커넥터 구성

커넥터 구성에 대한 자세한 내용은 Smartling [설명서][3]를 참조하세요.

1. 이전 번역 요청의 자동화를 선택합니다.
2. **언어 구성**에서 소스 및 대상 언어를 구성합니다. 커넥터는 Smartling TMS에 콘텐츠를 수집하고 Braze로 번역을 전달하는 데 사용할 것입니다.

![커넥터 언어 구성.][8]

### 2단계: Smartling으로 콘텐츠 전송

Braze 커넥터가 연결되고 설정되면 Smartling 프로젝트의 **Braze** 탭에서 Braze 콘텐츠를 찾을 수 있습니다. Smartling [설명서][7]를 참조하여 자세히 알아보세요.

Smartling은 다음과 같은 고급 기능을 제공하여 콘텐츠를 검색하고 선택합니다:

* 키워드 검색
* Braze 콘텐츠 유형
* Braze 태그 지정

![Content blocks list.][9]

### 3단계: Braze에 번역 추가

Smartling 플랫폼에서 번역이 완료되면 Braze로 자동 전송됩니다. Smartling과 Braze 간의 콘텐츠를 수동으로 동기화할 필요가 없습니다.

[1]: {{site.baseurl}}/api/basics/#endpoints
[2]: https://dashboard.smartling.com/
[3]: https://help.smartling.com/hc/en-us/articles/13248549217435
[4]: https://help.smartling.com/hc/article_attachments/13347533624347
[5]: https://www.smartling.com/
[6]: https://help.smartling.com/hc/en-us/articles/115003074093
[7]: https://help.smartling.com/hc/en-us/articles/13248577069979
[8]: {% image_buster /assets/img/smartling/smartling-braze-settings.png %}
[9]: {% image_buster /assets/img/smartling/smartling-content-blocks-list.png %}