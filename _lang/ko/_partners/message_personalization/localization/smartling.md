---
nav_title: Smartling
article_title: Smartling
description: "이 참고 문서에서는 Braze와 현지화를 위한 클라우드 기반 소프트웨어인 Smartling 간의 파트너십을 설명합니다. 브레이즈 커넥터는 HTML 이메일 템플릿, 콘텐츠 블록, 캔버스 및 캠페인 이메일 메시지의 번역을 지원합니다."
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> [Smartling](https://www.smartling.com/) is an end-to-end cloud translation management software for customers looking to automate the translation of websites, applications, and customer experiences.

_This integration is maintained by Smartling._

## 통합 정보

Braze 커넥터는 캠페인과 캔버스(이메일, 푸시 및 인앱 메시지), 이메일 템플릿 및 콘텐츠 블록의 메시지에 대한 번역을 지원합니다. 다국어 지원 또는 레거시 워크플로우와 함께 새 커넥터를 사용할지 결정할 때 지원되는 채널 및 기능에 대해 알아보려면 다음 표를 참조하세요.

| 채널/기능 | 기존 편집기(예. HTML) | 드래그 앤 드롭 편집기 |
| --------------- | ----------------------------- | -------------------- |
| [Email]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email) | ✅ | ✅ |
| [IAM]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message) | ✅ | ✅ |
| [푸시]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push) | ✅ | 해당 없음 |
| 이메일 템플릿 | 레거시 워크플로 | 레거시 워크플로|
| 콘텐츠 블록 |  ✅* |  ✅* |

\*자세한 내용은 [콘텐츠 블록 번역 관리하기를](#managing-translations-for-content-blocks) 참조하세요.

### 레거시 워크플로

사용 사례에 따라 레거시 번역 워크플로 또는 업데이트된 워크플로를 사용하여 콘텐츠 블록의 번역을 관리하세요. 

업데이트된 워크플로에서는 메시징에서 Braze 다국어 지원 및 로캘을 사용하여 콘텐츠 블록에 번역 태그가 추가됩니다. 그러나 스마트링은 메시지 수준에서 번역을 실행합니다. 콘텐츠가 캠페인 또는 캔버스에 포함되어 있고 타겟 로캘이 설정된 경우에만 콘텐츠가 번역됩니다. 자세히 알아보려면 [콘텐츠 블록 번역 관리하기를](#managing-translations-for-content-blocks) 참조하세요.

이메일 템플릿의 경우 레거시 워크플로만 지원됩니다. 자세히 알아보려면 [레거시 워크플로를 사용하여 번역 관리하기를](#managing-translations-using-the-legacy-workflow) 참조하세요.

## 필수 조건

| Requirement                   | 설명                                                                                                                                                         |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Smartling 계정             | A [Smartling account](https://dashboard.smartling.com/) is required to take advantage of this partnership.                                                          |
| Smartling 번역 프로젝트 | To connect your Braze account with Smartling, you must first sign in and [create a translation project](https://help.smartling.com/hc/en-us/articles/115003074093). |
| Braze REST API key            | A Braze REST API key with the following permissions: <br>- campaigns.translations.get<br>- campaigns.translations.update<br>- campaigns.list<br>- campaigns.details<br>- canvas.translations.get<br>- canvas.translations.update<br>- campaigns.details<br>- templates.email.create<br>- templates.email.update<br>- templates.email.list<br>- templates.email.info<br>- templates.translations.get<br>- templates.translations.update<br>- content_blocks.info<br>- content_blocks.list<br>- content_blocks.create<br>- content_blocks.update<br><br> This can be created in the Braze dashboard from **Settings > API Keys**. |
| Braze REST endpoint           | [Your REST endpoint URL]({{site.baseurl}}/api/basics/#endpoints). Your endpoint depends on the Braze URL for your instance.             |
| Braze 다국어 설정 | [Braze의 완벽한 다국어 설정]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### 1단계: Braze에서 다국어 설정 설정하기

Braze의 [다국어 설정 지침을]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites) 참조하여 현지화를 설정하세요.

### 2단계: Smartling TMS에서 Braze 프로젝트 설정

커넥터 구성에 대한 자세한 내용은 [스마트링 설명서를](https://help.smartling.com/hc/en-us/articles/13248549217435) 참조하세요.

### Braze를 Smartling에 연결

1. [스마트링 계정에서](https://dashboard.smartling.com/) [Braze 커넥터](https://help.smartling.com/hc/en-us/articles/115003074093) 프로젝트 유형을 생성합니다.

![Smartling에서 Braze 연결.]({% image_buster /assets/img/smartling/image1_Connecting_Braze_to_Smartling.png %})

{: start="2"}
2\. 이 프로젝트에서 **설정** > **브레이즈 설정** > **브레이즈에 연결**를 선택합니다.
3\. API URL 및 API 키와 같은 필수 입력란을 작성합니다. 테스트 연결이 성공하면 연결을 저장합니다. 테스트가 성공하지 못하면 올바른 API URL과 API 키를 입력했는지 확인하세요.

![Smartling API 설정에서 Braze 연결.]({% image_buster /assets/img/smartling/image2_API.png %})

{: start="4"}
4\. 프로젝트 언어를 추가합니다.

![스마트링 프로젝트 언어에서 Braze 연결.]({% image_buster /assets/img/smartling/image3_project_languages.png %})

{: start="5"}
5\. Braze 설정에서 **타겟 언어(Braze** ) 열의 값이 Braze 다국어 설정에서 구성된 로캘과 일치하는지 확인합니다. 로캘 명명 규칙이 정확히 일치해야 합니다.

![스마트링 언어 확인에서 Braze 연결.]({% image_buster /assets/img/smartling/image4_language_confirmation.png %})

### 3단계: Braze 메시징에 번역 태그 추가하기

메시징에 번역 태그를 추가하는 방법에 대한 [Braze의 안내를]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/?tab%3Dhtml%2520editor#prerequisites) 참조하세요:

- [Email]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email)
- [푸시]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push)
- [인앱 메시지]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message)

다음은 번역 태그가 있는 HTML 이메일 캠페인의 예입니다.

![번역 태그가 있는 Braze 이메일.]({% image_buster /assets/img/smartling/image5_translation_tags.png %})

메시지를 초안으로 저장해야 로캘을 선택할 수 있습니다.

### 4단계: 스마트링에서 번역 관리하기

커넥터를 연결하고 설정한 후 스마트링 프로젝트의 Braze 탭에서 Braze 콘텐츠를 찾습니다. 자세한 내용은 [스마트링 설명서를](https://help.smartling.com/hc/en-us/articles/13248577069979) 참조하세요.

Smartling은 다음과 같은 고급 기능을 제공하여 콘텐츠를 검색하고 선택합니다:
- 키워드 검색
- Braze 콘텐츠 유형
- Braze 태그 지정

1. 이 예제에서는 [3단계에서](#step-3-add-translation-tags-to-your-braze-message) 새해 프로모션 이메일 캠페인을 만들었습니다.

![번역 태그가 있는 Braze 이메일.]({% image_buster /assets/img/smartling/image6_ny_promotion.png %})

{: start="2"}
2\. 번역하려는 캠페인을 찾은 후 폴더를 선택하고 배리언트를 선택한 다음 **번역 요청을** 선택합니다.

![번역 요청하기.]({% image_buster /assets/img/smartling/image7_request_translation.png %})

{: start="3"}
3\. 번역을 위한 새 작업을 만듭니다.

![번역을 위한 새 작업을 만듭니다.]({% image_buster /assets/img/smartling/image8_request_translation.png %})

{: start="4"}
4\. 작업이 승인된 후에는 CAT 도구에서 각 번역을 편집합니다.

![번역 CAT 도구.]({% image_buster /assets/img/smartling/image9_translation_job.png %})

{: start="5"}
5\. 번역이 완료되면 번역을 저장하고 Braze에 제출하세요.

![Braze에 번역을 제출하세요.]({% image_buster /assets/img/smartling/image10_translations.png %})

### 5단계: Braze에서 다국어 사용자로서 메시지 미리보기

Braze에서 다국어 사용자로 캠페인을 미리 보고 번역이 올바르게 적용되었는지 확인합니다.

![다국어 사용자 미리 보기.]({% image_buster /assets/img/smartling/image11_preview.png %})

## 콘텐츠 블록 번역 관리하기

콘텐츠 블록은 Braze의 **템플릿 & 미디어** 섹션에서 관리됩니다.

### 메시지 구성 요소의 일부로 저장된 번역

번역 태그는 콘텐츠 블록에 속합니다. 그러나 스마트링은 메시지 수준에서 번역을 실행하며, 콘텐츠가 캠페인이나 캔버스에 포함되고 타겟 로캘이 설정된 경우에만 번역을 실행합니다.

### 고려 사항

- 번역 태그는 HTML 및 드래그 앤 드롭 콘텐츠 블록 편집기 모두에 대해 콘텐츠 블록에 수동으로 추가해야 합니다.
- 로캘은 콘텐츠 블록 자체가 아니라 메시지 수준에서 선택됩니다.
- 캔버스의 경우 Liquid 태그를 사용하여 콘텐츠 블록을 수동으로 추가하는 대신 행을 사용하여 메시징에 콘텐츠 블록을 삽입하는 것이 좋습니다. 콘텐츠 블록을 미리 보기에서 이메일로 드래그하면 로컬 사본이 만들어지며, '상위' 콘텐츠 블록의 변경 사항은 해당 블록을 사용하는 다른 캠페인에 전파되지 않습니다.
- 콘텐츠 블록 Liquid 태그를 사용하는 경우 이메일 본문에 번역 태그를 하나 이상 직접 포함해야 합니다. 번역 태그를 수동으로 추가하면 다국어 드롭다운에서 로캘을 선택할 수 있습니다. 스마틀링은 콘텐츠 블록의 번역 태그를 선택합니다. `comment` 태그를 추가하여 사용자에게 텍스트가 표시되지 않도록 할 수 있습니다.

## 레거시 워크플로를 사용하여 번역 관리하기

콘텐츠 블록 또는 이메일 템플릿 내에서 직접 번역을 관리하려면 [스마트링 설명서의](https://help.smartling.com/hc/en-us/articles/13248577069979-Translating-with-the-Braze-Connector) 레거시 지침을 [참조하세요](https://help.smartling.com/hc/en-us/articles/13248577069979-Translating-with-the-Braze-Connector). 이 메서드는 언어 속성과 Liquid if/else 로직을 사용하여 텍스트를 다른 언어로 표시합니다.

## Frequently asked questions

### 드래그 앤 드롭 편집기에 번역 태그가 지원되나요?

드래그 앤 드롭 편집기(이메일, 콘텐츠 블록, 인앱 메시지)의 경우 번역 태그를 수동으로 Liquid 태그로 추가해야 합니다.

### Liquid 태그 내의 텍스트는 어떻게 번역하나요?

스마트링은 Liquid 태그를 인식하여 컴포저에서 편집할 수 없는 변수로 만듭니다. 기본값 텍스트나 join과 같은 필터 등 Liquid 태그 내의 다른 텍스트도 스마트링에서 수정할 수 없게 됩니다. 그러나 스마트링에서 Liquid 태그를 제거하고 번역된 기본값 텍스트로 Liquid 태그를 다시 생성하세요. 번역을 저장할 때 경고가 표시됩니다.
