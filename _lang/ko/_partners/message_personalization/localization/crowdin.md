---
nav_title: Crowdin
article_title: Crowdin
description: "Crowdin 통합을 사용하여 번역 메모리, 용어집, 기계 번역을 활용해 캠페인, 캔버스 경험, 이메일 템플릿, 콘텐츠 블록을 번역할 수 있습니다."
alias: /partners/crowdin/
page_type: partner
search_tag: Partner

---

# Crowdin

> [Crowdin](https://crowdin.com/)은 AI 기반 현지화 관리 플랫폼으로, 팀이 소프트웨어, 앱, 마케팅 콘텐츠의 번역을 자동화할 수 있도록 도와줍니다.

Crowdin을 Braze에 연결하여 캠페인과 캔버스 경험의 번역을 관리할 수 있습니다. 자동 동기화는 기계 번역, 번역 메모리, 용어집과 함께 작동하여 수동 및 자동화 워크플로의 일관성을 유지합니다.

_이 통합은 Crowdin에서 유지 관리합니다._

## 통합 정보

Crowdin은 Braze용 앱을 두 가지 제공합니다: [Braze Campaigns & Canvas](https://store.crowdin.com/braze-content-translation)와 [Braze Email Templates](https://store.crowdin.com/braze-app). 현지화하려는 Braze 기능에 따라 선택하세요. 다음 표에서 두 앱을 비교합니다.

### 적합한 Crowdin 앱 선택하기

| 채널 또는 기능 | Braze Campaigns & Canvas | Braze Email Templates |
| --- | --- | --- |
| **캠페인** | ✅ 지원됨 | ❌ 지원되지 않음 |
| **캔버스 단계** | ✅ 지원됨 | ❌ 지원되지 않음 |
| **이메일 템플릿** | ❌ 지원되지 않음 | ✅ 지원됨 |
| **콘텐츠 블록** | ❌ 지원되지 않음 | ✅ 지원됨 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 필수 조건

| 요구 사항 | 설명 |
| --- | --- |
| **Crowdin 계정** | [Crowdin.com 계정](https://accounts.crowdin.com/register) 또는 [Crowdin Enterprise 계정](https://accounts.crowdin.com/workspace/create)이 필요합니다. |
| **Crowdin 프로젝트** | Braze를 연결하기 전에 Crowdin 또는 Crowdin Enterprise에서 [번역 프로젝트를 생성](https://support.crowdin.com/creating-project/)해야 합니다. |
| **Braze REST API 키** | 캠페인, 캔버스, 콘텐츠 블록, 커스텀 속성, 이메일, 템플릿에 대한 권한이 있는 Braze REST API 키. |
| **Braze REST 엔드포인트** | 사용 중인 Braze REST 엔드포인트 URL(예: `https://rest.iad-03.braze.com`). |
| **Braze 다국어 설정** | Braze 대시보드의 **설정** > **현지화 설정**에서 로케일을 구성해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Braze Campaigns & Canvas 통합

라이브 메시지 내 콘텐츠를 현지화하는 경우, [Braze Campaigns & Canvas 앱](https://store.crowdin.com/braze-content-translation)을 사용하여 캠페인 및 캔버스 초안에서 번역 가능한 문자열을 Braze 다국어 지원과 동기화할 수 있습니다.

동영상 안내는 [Braze Campaigns & Canvas 통합](https://youtu.be/ahG1ET4VRKA)을 참조하세요.

### 1단계: Braze에서 다국어 설정 구성

Crowdin을 연결하기 전에 Braze에서 대상 언어를 추가하세요.

1. Braze에서 **설정** > **현지화 설정**으로 이동합니다.
2. 지원할 언어를 추가합니다.

![설정 아래 Braze 로케일 페이지에서 로케일 이름, 로케일 키, 로케일 추가가 표시됩니다.]({% image_buster /assets/img/crowdin/braze_locales.png %})

{: start="3"}
3. 각 **로케일 키**(예: `en-US`, `fr-FR`, `es-ES`)를 확인하세요. Crowdin에서 언어를 매핑할 때 이 값을 사용합니다.

### 2단계: Crowdin에서 Braze 프로젝트 설정

1. Crowdin Enterprise 또는 Crowdin.com 계정에서 왼쪽 메뉴의 **Store**로 이동합니다.
2. **Braze Campaigns & Canvas**를 검색한 후 **Install**을 선택합니다.

![Crowdin Store에서 Braze Campaigns & Canvas가 선택되고 Install이 강조 표시된 화면.]({% image_buster /assets/img/crowdin/crowdin_store_campaigns_canvas.png %})

{: start="3"}
3. 이 통합을 사용할 프로젝트를 선택합니다.
4. 통합을 열려면 프로젝트의 **Integrations** > **Braze Campaigns & Canvas**로 이동합니다.

#### Braze를 Crowdin에 연결

Braze API 자격 증명으로 연결을 인증합니다:

![Crowdin Braze Campaigns & Canvas 연결 양식에 REST API 키, REST 엔드포인트, Log in with Braze Campaigns & Canvas가 표시됩니다.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_login.png %})

- **Braze REST API 키:** Braze의 **설정** > **API 및 식별자** > **API 키**에서 생성합니다. 이 통합에 필요한 권한(캠페인, 캔버스, 콘텐츠 블록, 커스텀 속성)을 부여하세요.
- **Braze REST 엔드포인트:** Braze 인스턴스의 URL을 입력합니다(예: `https://rest.iad-03.braze.com`). 자세한 내용은 [REST API 엔드포인트]({{site.baseurl}}/api/basics/#endpoints)를 참조하세요.

![Braze REST API 키 페이지에 API 키 생성 및 REST 엔드포인트 복사 컨트롤이 표시됩니다.]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %})

**Log in with Braze Campaigns & Canvas**를 선택합니다.

### 3단계: Crowdin에서 언어 매핑 구성

계정을 연결한 후 각 Crowdin 프로젝트 언어를 해당하는 Braze 로케일에 매핑합니다.

1. **Braze Campaigns & Canvas** 통합 대시보드에서 오른쪽 상단의 **Settings** 기어 아이콘을 선택합니다.

![Braze Campaigns & Canvas 통합 화면에서 상단 작업 바에 Settings가 표시됩니다.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_settings.png %})

{: start="2"}
2. **General Settings** 탭을 엽니다.
3. 로케일 키를 입력합니다. Crowdin에 프로젝트 언어(예: French, Italian)가 나열됩니다. 각 필드에 해당하는 **Braze 로케일 키**를 입력합니다.
   - 예를 들어, Braze에서 이탈리아어에 `it`를 사용하는 경우 Crowdin의 Italian 옆에 `it`를 입력합니다.
   - 각 항목은 Braze **현지화 설정**에서 해당 로케일의 **로케일 키**와 정확히 일치해야 합니다.

![Settings 모달의 General Settings 탭에서 파일 필터 필드와 언어 매핑 행(예: French가 fr에 매핑됨)이 표시됩니다.]({% image_buster /assets/img/crowdin/crowdin_language_mapping_settings.png %})

{: start="4"}
4. **Save**를 선택하여 매핑을 확인합니다.

### 4단계: Braze 메시지에 번역 태그 추가

Crowdin은 Braze가 다국어 메시지에 사용하는 것과 동일한 Liquid **번역 태그**를 읽습니다. 번역하려는 모든 텍스트, 이미지 URL 또는 링크 URL 주위에 {% raw %}`{% translation your_id_here %}` 및 `{% endtranslation %}`{% endraw %}를 추가하세요. 각 블록에는 고유한 `id`(예: `greeting` 또는 `welcome_header`)가 필요합니다.

**예시:**

{% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

HTML, 링크 내 Liquid 및 기타 패턴의 경우 [로케일 번역]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales)과 동일한 규칙을 따르세요(예: 가능한 한 작은 세그먼트 주위에 태그를 배치하고, 링크를 현지화할 때 언어별 부분만 감싸기).

Crowdin이 콘텐츠를 감지하고 가져올 수 있도록 Braze 메시지를 **초안**으로 저장하세요.

### 5단계: Crowdin에서 번역 관리

통합 화면은 두 부분으로 구성됩니다:

- **오른쪽(Braze):** 캠페인과 캔버스.
- **왼쪽(Crowdin):** 번역을 위해 이미 동기화된 콘텐츠.

![Crowdin과 Braze Campaigns & Canvas 패널에 캠페인 및 로케일 폴더, Sync to Braze, Sync to Crowdin이 표시됩니다.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_sync_panels.png %})

#### 콘텐츠 동기화

1. **Braze(오른쪽)** 측에서 번역할 캠페인 또는 캔버스의 체크박스를 선택합니다.
2. **Sync to Crowdin**을 선택합니다.
3. 동기화가 완료되면 **Crowdin(왼쪽)** 측에 파일이 나타납니다. 번역자는 Crowdin 편집기에서 문자열을 열 수 있습니다.

#### Braze로 번역 반환

1. Crowdin에서 번역이 100% 완료되면 **Integrations** 탭으로 돌아갑니다.
2. **Crowdin(왼쪽)** 측에서 완료된 콘텐츠를 선택합니다.
3. **Sync to Braze**를 선택합니다. 번역된 문자열이 Braze 캠페인의 해당 언어 배리언트에 푸시됩니다.

### 6단계: Braze에서 다국어 사용자로 메시지 미리보기

통합을 확인하려면:

1. **Braze 메시지 작성기**에서 캠페인을 엽니다.
2. **테스트** 탭으로 이동합니다.
3. **사용자로 메시지 미리보기**를 선택합니다.
4. 번역된 로케일 중 하나와 일치하는 `language` 속성을 가진 고객 프로필을 검색합니다.
5. 콘텐츠가 소스 언어에서 번역된 버전으로 전환되는지 확인합니다.

## Braze Email Templates 통합

템플릿 수준에서 이메일을 현지화하는 경우, [Braze Email Templates 앱](https://store.crowdin.com/braze-app)을 사용하여 Braze 미디어 라이브러리의 HTML을 동기화할 수 있습니다.

동영상 안내는 [Braze Email Templates 통합](https://youtu.be/g0YMKW3jEjk)을 참조하세요.

### 1단계: 앱 설치

1. Crowdin 프로젝트에서 **Store** 탭으로 이동합니다.
2. **Braze Email Templates**를 검색하고 **Install**을 선택합니다.

![Crowdin Store에서 Braze Email Templates가 선택되고 Install이 강조 표시된 화면.]({% image_buster /assets/img/crowdin/crowdin_store_email_templates.png %})

{: start="3"}
3. 이 통합을 사용할 프로젝트를 선택합니다.
4. 통합을 열려면 프로젝트의 **Integrations** > **Braze Email Templates**로 이동합니다.

### 2단계: Braze에 연결

Braze API 자격 증명으로 연결을 인증합니다:

![Crowdin Braze Email Templates 연결 양식에 REST API 키, REST 엔드포인트, Log in with Braze Email Templates가 표시됩니다.]({% image_buster /assets/img/crowdin/crowdin_email_templates_login.png %}){: style="max-width:85%;"}

1. **Braze REST API 키:** `templates.email` 및 `content_blocks`(읽기 및 쓰기) 권한을 부여합니다. Braze의 **설정** > **API 및 식별자** > **API 키**에서 키를 생성합니다.

![Braze REST API 키 페이지에 API 키 생성 및 REST 엔드포인트 복사 컨트롤이 표시됩니다.]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %})

{: start="2"}
2. **Braze REST 엔드포인트**에 인스턴스별 URL을 사용합니다(예: `https://rest.iad-03.braze.com`).
3. **Log in with Braze Email Templates**를 선택합니다.

### 3단계: 번역할 콘텐츠 동기화

통합 화면에 Braze 라이브러리가 표시됩니다:

- **오른쪽(Braze):** 동기화할 수 있는 **이메일 템플릿**과 **콘텐츠 블록**.
- **왼쪽(Crowdin):** 번역 중인 콘텐츠.

1. **Braze(오른쪽)** 측에서 현지화할 템플릿 또는 블록 옆의 체크박스를 선택합니다.
2. **Sync to Crowdin**을 선택합니다.
3. Crowdin이 HTML 소스를 가져옵니다. 번역자는 레이아웃이 유지되도록 라이브 **WYSIWYG 미리보기**가 포함된 Crowdin 편집기에서 작업합니다.

![Crowdin 편집기 미리보기 탭에 현지화된 이메일 HTML과 번역 가능한 문자열이 표시됩니다.]({% image_buster /assets/img/crowdin/crowdin_editor_wysiwyg_preview.png %}){: style="max-width:85%;"}

### 4단계: 번역된 템플릿 전달

번역이 100% 완료되면:

1. **Crowdin(왼쪽)** 측에서 완료된 파일을 선택합니다.
2. **Sync to Braze**를 선택합니다.
3. Crowdin이 Braze 미디어 라이브러리에 이러한 자산의 현지화된 버전을 자동으로 생성합니다(예: `Template_Name_fr`).

![Crowdin과 Braze Email Templates 패널에 이메일 템플릿과 콘텐츠 블록이 나열되고, Sync to Braze와 Sync to Crowdin이 표시됩니다.]({% image_buster /assets/img/crowdin/crowdin_email_templates_sync_panels.png %})