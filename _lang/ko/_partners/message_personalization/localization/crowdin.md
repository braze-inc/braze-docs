---
nav_title: Crowdin
article_title: Crowdin
description: "이 참조 문서에서는 Braze의 이메일 템플릿 및 콘텐츠 블록 번역을 자동화할 수 있는 클라우드 기반 소프트웨어 플랫폼인 Crowdin과 Braze 간의 파트너십에 대해 간략하게 설명합니다."
alias: /partners/crowdin/
page_type: partner
search_tag: Partner

---

# Crowdin

> Crowdin은 로컬라이제이션 관리를 위한 클라우드 기반 소프트웨어입니다. Crowdin을 사용하면 Android 및 iOS 앱, 웹사이트, 스토어 스크린샷 및 기타 콘텐츠를 번역할 수 있습니다. 번역은 사내 팀, 번역 에이전시 또는 기계 번역 엔진을 통해 수행할 수 있습니다.

_This integration is maintained by Crowdin._

## 통합 정보

Braze와 Crowdin의 통합을 통해 이메일 템플릿과 콘텐츠 블록을 번역할 수 있습니다. 또한 Braze 계정의 콘텐츠를 Crowdin 프로젝트에 동기화하고 번역을 다시 Braze에 추가할 수 있습니다.

## 필수 조건

| 요구 사항| 설명|
| ---| ---|
| Crowdin 계정 | 이 파트너십을 활용하려면 [Crowdin 계정](https://accounts.crowdin.com/register)이 필요합니다. |
| 크라우딩 번역 프로젝트 | Braze 계정을 Crowdin 또는 Crowdin Enterprise에 연결하려면 먼저 가입하고 번역 프로젝트를 생성해야 합니다. |
| Braze REST API 키 | 모든 템플릿 및 콘텐츠 블록 권한이 있는 Braze REST API 키. <br><br> 이것은 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
| Braze SDK 엔드포인트 | SDK 엔드포인트 URL은 [인스턴스]({{site.baseurl}}/api/basics/#endpoints)의 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 통합

### 1단계: Crowdin/Crowdin Enterprise에서 Braze 앱 설정

#### Crowdin
Crowdin에서 Braze 앱을 설정하려면 다음 단계를 따르세요:

1. [마켓플레이스에서 Braze 앱으로](https://store.crowdin.com/braze-app) 이동합니다.
2. **설치**를 클릭하여 계정에 추가합니다.
3. Braze 콘텐츠 현지화를 위해 생성한 프로젝트를 엽니다.
4. **설정 > 연동** 탭으로 이동합니다.
5. **애플리케이션** 섹션에서 Braze 앱을 클릭합니다.
6. 대화 상자에서 Braze 자격 증명(Braze REST API 키 및 Braze SDK 엔드포인트)을 제공합니다.
7. **Braze 커넥터로 로그인**을 클릭합니다. 

#### Crowdin Enterprise
Crowdin Enterprise에서 Braze 앱을 설정하려면 다음 단계를 따르세요:

1. **Workspace** 홈 페이지 > **마켓플레이스로** 이동합니다.
2. Braze 앱에서 **설치를** 클릭하여 조직에 추가합니다.
3. Braze 콘텐츠 현지화를 위해 생성한 프로젝트를 엽니다.
4. **애플리케이션 > 커스텀**으로 이동합니다.
5. Braze 앱을 클릭합니다.
6. 대화 상자에서 Braze 자격 증명(Braze REST API 키 및 Braze SDK 엔드포인트)을 제공합니다.
7. **Braze 커넥터로 로그인**을 클릭합니다.

### 2단계: Crowdin/Crowdin Enterprise에 콘텐츠 추가

Braze 자격 증명을 제공하면 두 개의 패널이 표시됩니다. Braze 계정에서 번역할 파일을 동기화할 콘텐츠를 선택하고 **Crowdin에 동기화**를 클릭합니다.

Crowdin의 편집기 모드로 설정하고 Braze 계정에서 동기화된 콘텐츠를 번역자에게 문자열 목록 또는 파일 미리 보기로 표시할 수 있습니다.

![An image of what the Crowdin Editor email composer looks like with some basic translations added.]({% image_buster /assets/img/crowdin/crowdin_editor_email_preview.png %})

### 3단계: Braze에 번역 추가하기

번역이 완료되면 Crowdin에서 Braze 앱을 열고 왼쪽 패널에서 번역된 파일(각 파일에 대해 모든 대상 언어 또는 특정 언어만 선택할 수 있음)을 선택한 후 **Braze에 동기화를** 클릭합니다.

![An image of a user selecting their translation files and syncing them to Braze.]({% image_buster /assets/img/crowdin/sync_translations.png %})


