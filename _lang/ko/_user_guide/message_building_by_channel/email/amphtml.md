---
nav_title: 이메일용 AMP
article_title: 이메일용 AMP
alias: /amphtml/
page_order: 11
description: "이 참조 문서에서는 이메일용 AMP에 대한 개요와 일반적인 사용 사례를 제공합니다."
channel:
  - email

---

# 이메일용 AMP

> [이메일용 AMP를](https://amp.dev/about/email) 사용하면 이메일에 대화형 요소를 추가하고 고객과의 커뮤니케이션을 강화하여 사용자의 받은 편지함으로 바로 완벽한 경험을 제공할 수 있습니다. AMP는 설문조사, 피드백 설문지, 투표 캠페인, 리뷰, 구독 센터 등 흥미로운 이메일 오퍼링을 구축하는 데 사용할 수 있는 다양한 구성 요소를 사용하여 이를 가능하게 합니다. 이러한 도구는 유지와 인게이지먼트 증대 기회를 제공합니다.

## 요구 사항

Braze는 사용자가 Google에 등록하거나 필요한 보안 요건을 충족하는 것에 대해 책임을 지지 않습니다.

| 요구 사항   | 설명 |
| --------------| ----------- |
| 이메일용 AMP 사용 설정 | AMP는 모든 사용자가 사용할 수 있습니다. |
| Gmail 계정 활성화 | [Gmail 계정 활성화](#enabling-gmail-account)를 참조하세요. |
| Google 발신자 인증 | Gmail은 DKIM, SPF 및 DMARC를 사용하여 AMP 이메일의 [발신자를 인증합니다](https://developers.google.com/gmail/ampemail/security-requirements#sender_authentication). 계정에 대해 설정해야 합니다. <br><br>- [도메인 키 식별 메일](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail)(DKIM) <br>- [발신자 정책 프레임워크](https://en.wikipedia.org/wiki/Sender_Policy_Framework)(SPF)<br>- [도메인 기반 메시지 인증, 보고 및 적합성](https://en.wikipedia.org/wiki/DMARC)(DMARC)
| AMP 이메일 요소 | 매력적인 AMP 이메일에는 다양한 구성 요소를 전략적으로 사용하는 것이 포함됩니다. 아래 [구성 요소](#components) 섹션의 필수 탭을 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 지원되는 이메일 클라이언트

사용자에게 AMP 이메일을 보내려면 먼저 이메일 클라이언트에 등록해야 합니다. 등록 절차에는 승인을 받기 위해 테스트 AMP HTML 이메일을 보내는 과정이 포함됩니다. 승인 시간은 고객마다 다릅니다. 자세한 내용은 등록 링크를 참조하세요.

| 클라이언트 | 등록 링크 |
| ------ | -------- |
| Gmail | [Google](https://developers.google.com/gmail/ampemail/register) |
| FairEmail | [FairEmail](https://email.faircode.eu/) |
| Yahoo | [Yahoo](https://senders.yahooinc.com/amp/) |
| Mail.ru | [Mail.ru](https://postmaster.mail.ru/amp/) |

지원되는 이메일 클라이언트의 전체 목록은 [AMP 설명서를](https://amp.dev/support/faq/email-support) 참조하세요.

### Gmail 계정 사용 설정

Gmail 설정으로 이동하여 **일반** **동적 이메일 사용**을 선택합니다.

!['동적 이메일 사용' 확인란이 선택된 Gmail 설정의 예입니다.][1]

## API 사용

또한 이메일용 AMP를 API로 사용할 수도 있습니다. Braze [메시징 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/)를 사용하여 이메일을 보내는 경우, 아래와 같이 `amp_body`를 객체 사양으로 추가하세요.

### 이메일 개체 사양

```json
{
  "app_id": (required, string) see app identifier above,
  "subject": (optional, string),
  "from": (required, valid email address in the format "Display Name <email@address.com>"),
  "reply_to": (optional, valid email address in the format "email@address.com" - defaults to your workspace's default reply to if not set),
  "plaintext_body": (optional, valid plaintext, defaults to autogenerating plaintext from "body" when this is not set),
  "amp_body": (optional, updates the text-amp-html MIME type) the email body in AMP HTML. The MIME (Multipurpose Internet Mail Extensions) type to be referenced is "text/x-amp-html",
  "body": (required unless email_template_id is given, valid HTML),
  "preheader": (optional*, string) Recommended length 50-100 characters,
  "email_template_id": (optional, string) If provided, we will use the subject/body/should_inline_css values from the given email template UNLESS they are specified here, in which case we will override the provided template,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "extras": (optional, valid key-value hash), extra hash - for SendGrid customers, this will be passed to SendGrid as Unique Arguments,
  "headers": (optional, valid key-value hash), hash of custom extensions headers. Currently, only supported for SendGrid customers,
  "should_inline_css": (optional, boolean), whether to inline CSS on the body. If not provided, falls back to the default CSS inlining value for the workspace,
  "attachments": (optional, array), array of JSON objects like [{"file_name","url"}] that define the files you need attached. Your file name's extension will be detected automatically from the URL, which should return the appropriate `Content-Type` as a response header,
}
```

## AMP 이메일 만들기

먼저 [구성요소](#components)를 사용하여 AMP 이메일을 작성합니다. 그런 다음 [Braze API](#api-usage)를 사용하여 메시지를 전송하고, AMP HTML에 `amp_body`를 포함하세요.

AMP HTML 외에도 일반 HTML `body` 버전이 필요하며, `plaintext_body` 버전의 AMP 이메일을 사용하는 것이 좋습니다. 모든 AMP 이메일은 멀티파트로 전송되므로 Braze는 HTML, 일반 텍스트 및 AMP HTML을 지원하는 이메일을 발송합니다. 이메일이 사용자와 디바이스에 따라 적절한 버전으로 자동 기본 설정되므로 이메일용 AMP를 아직 지원하지 않는 제공업체를 통해 이메일을 전송하는 경우에 유용합니다.

{% alert note %}
AMP 이메일을 작성할 때는 AMP 코드가 HTML 편집기에 추가되어서는 안 되므로 AMP 편집기에 있는지 확인하세요.
{% endalert %}

다음 추가 리소스를 참조하세요:

- [AMP 튜토리얼](https://amp.dev/documentation/guides-and-tutorials/start/create_email?format=email)
- 최종 결과물이 어떻게 보이는지 확인할 수 있는 [샘플 코드입니다](https://gist.github.com/CrystalOnScript/988c3f0a2eb406da27e9d9bf13a8bf73). 
- [AMP 이메일 컴포넌트 라이브러리](https://amp.dev/documentation/components/?format=email/)

### 구성요소

AMP 요소를 구축할 때는 엔지니어링 팀과 협의하여 디자인 리소스와 요소를 추가하여 완성도를 높일 것을 권장합니다.

{% tabs %}
  {% tab 필수 항목 %}

이러한 각 요소는 AMP 이메일 본문에 필수적으로 포함되어야 합니다.

| 구성 요소 | 설명 | 예시 |
|---------|--------------|---------|
| 식별 작업 <br><br> `⚡4email` 또는 `amp4email`| 이메일을 AMP HTML 이메일로 식별합니다. | `<!doctype html>` <br> `<html ⚡4email>` <br> `<head>` |
| AMP 런타임 로드 <br><br> `<script>` | JavaScript를 사용하여 이메일에서 AMP를 실행할 수 있도록 허용합니다. | `<script async src="https://cdn.ampproject.org/v0.js"></script>`|
| CSS 보일러플레이트 | AMP가 로드될 때까지 콘텐츠를 숨깁니다. <br> AMP 이메일을 지원하는 이메일 제공업체는 검증된 AMP 스크립트만 클라이언트에서 실행하도록 허용하는 보안 검사를 시행합니다. | `<style amp4email-boilerplate>body{visibility:hidden}</style>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

  {% endtab %}
  {% tab 동적 %}

이러한 구성 요소를 사용하여 이메일에 동적 레이아웃과 동작을 만들 수 있습니다.

| 구성 요소 | 설명 | 필수 스크립트 |
|---------|--------------|---------|
| [Accordion](https://amp.dev/documentation/components/amp-accordion?format=email) <br><br> `amp-accordion`| 사용자가 콘텐츠 개요를 보고 원하는 섹션으로 이동할 수 있습니다. | `<script async custom-element="amp-accordion" src="https://cdn.ampproject.org/v0/amp-accordion-0.1.js"></script>` |
| [양식](https://amp.dev/documentation/components/amp-form?format=email) <br><br> `amp-form`| AMP 문서에서 입력 필드를 제출하는 양식을 만듭니다. | `<script async custom-element="amp-form" src="https://cdn.ampproject.org/v0/amp-form-0.1.js"></script>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
사용자 인증이 필요한 모든 구성요소는 [Google 액세스 토큰](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) 또는 [프록시 어설션 토큰](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens)을 사용해야 합니다.
{% endalert %}
  {% endtab %}
  {% tab 크리에이티브 %}

  AMP의 구성요소를 활용하여 오디언스에게 맞춤화된 이메일을 제작할 수 있습니다.

| 구성 요소 | 설명 | 필수 스크립트 |
|---------|--------------|---------|
| [애니메이션 이미지](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-anim`| 런타임을 통해 관리되는 애니메이션 이미지(일반적으로 GIF)를 표시합니다. | `<script async custom-element="amp-anim" src="https://cdn.ampproject.org/v0/amp-anim-0.1.js"></script>` |
| [캐러셀](https://amp.dev/documentation/components/amp-carousel?format=email) <br><br> `amp-carousel`| 가로 축을 따라 여러 개의 유사한 콘텐츠를 표시합니다. | `<script async custom-element="amp-carousel" src="https://cdn.ampproject.org/v0/amp-carousel-0.1.js"></script>` |
| [이미지](https://amp.dev/documentation/components/amp-img?format=email) | HTML `img` 태그의 런타임 관리형 대체품입니다. <br>  [이미지에 대한 라이트박스](https://amp.dev/documentation/components/amp-image-lightbox?format=email)를 만들 수도 있습니다. | `<amp-img alt="A view of the sea"` <br> `src="images/sea.jpg"` <br> `width="900"` <br>  `height="675"` <br>  `layout="responsive">`  <br> `</amp-img>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
사용자 인증이 필요한 모든 구성요소는 [Google 액세스 토큰](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) 또는 [프록시 어설션 토큰](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens)을 사용해야 합니다.
{% endalert %}

  {% endtab %}
  {% tab 기타 %}

| 구성 요소 | 설명 |
|---------|--------------|
| [데이터 바인딩 및 표현식](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-bind`| 데이터 바인딩과 자바스크립트 유사 표현식을 통해 AMP 페이지에 커스텀 상태 저장형 상호 작용을 추가합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
사용자 인증이 필요한 모든 구성요소는 [Google 액세스 토큰](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) 또는 [프록시 어설션 토큰](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens)을 사용해야 합니다.
{% endalert %}

{% endtab %}
{% endtabs %}

AMP 구성 요소의 전체 목록은 [AMP 설명서](https://amp.dev/documentation/components/?format=email)를 확인하세요.  

### 사용 사례

{% tabs 로컬 %}
{% tab 대화형 설문조사 %}

`<amp-form>` 구성 요소를 사용하면 이메일 받은 편지함을 벗어나지 않고도 완료할 수 있는 대화형 설문조사를 만들 수 있습니다. `<amp-form>`을 사용하여 설문조사 응답을 제출한 다음 백엔드에서 이 집계 데이터를 제공하도록 하면 됩니다. 

몇 가지 예는 다음과 같습니다:
* 컨퍼런스 설문조사 이메일
* 피드에서 동적으로 항목 업데이트하기
* 기사 북마크 이메일

사용자는 이 구성요소를 사용하여 필드 값을 제출하거나 지울 수 있습니다. 또한 이메일을 설정하는 방법에 따라 설문조사 제출 성공 여부와 같은 추가 메시지를 사용자에게 표시하거나 투표 캠페인과 같이 설문조사 결과를 표시하는 사용자의 응답을 렌더링할 수 있습니다.

{% endtab %}
{% tab 접을 수 있는 콘텐츠 %}

`<amp-accordion>` 컴포넌트를 사용하여 콘텐츠 섹션을 확장합니다. 이 구성 요소를 사용하면 접을 수 있고 확장 가능한 콘텐츠 섹션을 표시하여 시청자가 콘텐츠 개요를 한눈에 확인하고 원하는 섹션으로 이동할 수 있습니다. 

긴 교육 기사나 개인화된 추천을 보내는 경우, 시청자가 콘텐츠 개요를 한눈에 살펴보고 원하는 섹션이나 특정 제품 추천으로 이동하여 자세한 내용을 확인할 수 있습니다. 이는 한 섹션에서 몇 문장을 읽더라도 스크롤을 해야 하는 모바일 사용자에게 특히 유용할 수 있습니다.
{% endtab %}
{% tab 이미지가 많은 이메일 %}

리테일 브랜드처럼 전문적인 사진이 많이 포함된 이메일을 보내는 경우 사용자가 관심을 끌 수 있는 이미지로 참여를 유도하는 `<amp-image-lightbox>` 구성 요소를 사용할 수 있습니다. 사용자가 이미지를 클릭하면 이 컴포넌트는 메시지 중앙에 이미지를 표시하여 라이트박스 효과를 만듭니다. 

또한 `<amp-image-lightbox>` 컴포넌트를 통해 사용자는 자세한 이미지 설명을 볼 수 있습니다. 동일한 구성요소를 두 개 이상의 이미지에 사용할 수 있습니다. 예를 들어 이메일에 여러 개의 이미지가 포함되어 있는 경우 사용자가 이미지를 클릭하면 해당 이미지가 라이트박스에 표시됩니다.

{% endtab %}
{% tab 글꼴 기반 이메일 %}

주로 텍스트 복사에 의존하는 이메일의 경우 `<amp-fit-text>` 구성 요소를 사용하여 지정된 영역 내에서 텍스트의 크기와 맞춤을 관리할 수 있습니다.

예를 들면 다음과 같습니다:

- 영역에 맞게 텍스트 크기 조정하기
- 최대 글꼴 크기를 설정할 수 있는 최대 글꼴 크기를 사용하여 영역에 맞게 텍스트 크기 조정하기
- 콘텐츠가 영역을 초과하는 경우 텍스트 잘라내기

{% endtab %}
{% endtabs %}

### amp-mustache 사용

Liquid와 마찬가지로 AMP는 고급 사용 사례를 위한 스크립팅 언어를 지원합니다. 이 구성 요소는 [`amp-mustache`](https://amp.dev/documentation/components/amp-mustache/?format=email)이라고 합니다. 머스탱 마크업 언어를 포함할 때는 Liquid의 [`raw`](https://shopify.github.io/liquid/tags/raw/) 태그를 사용해야 합니다. Liquid와 머스탱은 구문 스타일을 공유한다는 점에 유의하세요. 

콘텐츠를 `raw` 태그로 감싸면 Braze 처리 엔진은 `raw` 태그 사이의 모든 콘텐츠를 무시하고 팀에 필요한 머스탱 변수를 전송합니다.

## 메트릭 및 분석

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>측정기준</th>
            <th>세부 정보</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split">총 열람 수</td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Opens' %} AMP 이메일의 경우 HTML 및 일반 텍스트 버전의 총 열람 횟수입니다.</td>
        </tr>
        <tr>
            <td class="no-split">총 클릭 수</td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Clicks' %} AMP 이메일의 경우 HTML 및 일반 텍스트 버전의 총 클릭 수입니다.</td>
        </tr>
        <tr>
            <td class="no-split">AMP 열람 수</td>
            <td class="no-split">{% multi_lang_include metrics.md metric='AMP Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split">AMP 클릭 수</td>
            <td class="no-split">{% multi_lang_include metrics.md metric='AMP Clicks' %}</td>
        </tr>
    </tbody>
</table>

## 테스트 및 문제 해결

총 클릭 수와 고유 클릭 수에는 AMP 메시지에서 발생한 클릭은 포함되지 않습니다(HTML 및 일반 텍스트만 해당). AMP 관련 클릭은 *amp_click* 지표로 어트리뷰션됩니다.

AMP 이메일을 보내기 전에 다음 [Gmail 가이드라인](https://developers.google.com/gmail/ampemail/testing-dynamic-email)에 따라 테스트하는 것이 좋습니다.

AMP 이메일이 Gmail 계정으로 전달되려면 이메일이 다음 조건을 충족해야 합니다.

- 이메일용 AMP 보안 요구 사항을 충족해야 합니다.
- AMP MIME 부분에는 유효한 AMP 문서가 포함되어야 합니다.
- 이메일에는 HTML MIME 부분 앞에 AMP MIME 부분이 포함되어야 합니다.
- AMP MIME 부분은 100KB보다 작아야 합니다.

이러한 조건 중 어느 것도 오류의 원인이 되지 않는 경우 [지원팀에]({{site.baseurl}}/support_contact/) 문의하세요.

### 자주 묻는 질문

#### AMP 이메일로 세분화해야 하나요?

다양한 유형의 사용자에게 모두 전송하기 위해 세분화하지 않는 것을 권장합니다. 이는 원본 이메일에 여러 버전이 포함된 AMP 메시지를 여러 부분으로 전송하기 때문입니다. 사용자가 AMP 버전을 볼 수 없는 경우 기본적으로 HTML로 돌아갑니다. 


[1]: {% image_buster /assets/img/dynamic-content.png %}
