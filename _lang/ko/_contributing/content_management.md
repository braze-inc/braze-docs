---
nav_title: 콘텐츠 관리
article: Content Management
description: "브레이즈 문서에서 콘텐츠가 관리되는 방식에 대한 개요입니다."
page_order: 2 
noindex: true
---

# 콘텐츠 관리 정보

> 브레이즈 문서에서 콘텐츠가 관리되는 방식에 대한 개요입니다. 특정 주제에 대해 자세히 알아보려면 탐색에서 전용 주제 페이지를 선택하세요.

## 방법론

Braze Docs는 버전 관리 시스템을 사용하여 소프트웨어 개발 라이프사이클을 반영하는 문서 관리 방법인 코드형 문서(docs-as-code)를 사용하여 관리됩니다. Braze Docs는 Git 버전 관리 시스템을 사용하여 기여자들이 서로의 작업을 덮어쓰지 않고 동일한 문서에서 작업할 수 있도록 합니다. 자세한 내용은 [버전 관리 및 Git에 대한](https://docs.github.com/en/get-started/using-git/about-git#about-version-control-and-git) 정보를 참조하세요.

![The Braze Docs repository's home page on GitHub.]({% image_buster /assets/img/contributing/github/home_page.png %})

## 사이트 생성기 

Braze Docs는 콘텐츠 파일과 디자인 파일을 별도의 디렉터리(예: 콘텐츠 파일은 `_docs`, 디자인 파일은 `assets` )에 저장할 수 있는 인기 있는 정적 사이트 생성기인 Jekyll을 사용하여 구축되었습니다. 사이트가 구축되면 Jekyll은 각 파일을 지능적으로 병합하여 `_site` 디렉터리에 XML 및 HTML 데이터로 저장합니다. 자세한 내용은 [지킬 디렉토리 구조를](https://jekyllrb.com/docs/structure/) 참조하세요.

![The home page for Braze Docs.]({% image_buster /assets/img/contributing/styling_examples/home.png %})

기여자는 주로 다음 디렉터리에서 작업하게 됩니다.

| 디렉토리 | 설명 | 설명
|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`_docs`](https://github.com/braze-inc/braze-docs/tree/develop/_docs)         | 브라즈 문서의 모든 작성된 콘텐츠를 마크다운으로 작성된 텍스트 파일로 포함합니다. 텍스트 파일은 [API 섹션의]({{site.baseurl}}/api/home) 경우 `_api`, [사용자 가이드 섹션의]({{site.baseurl}}/user_guide/introduction) 경우 `user_guide` 등 문서 사이트를 미러링하는 디렉터리와 하위 디렉터리로 구성되어 있습니다. |
| [`_includes`](https://github.com/braze-inc/braze-docs/tree/develop/_includes) | `_docs` 디렉터리 내의 모든 파일에서 재사용할 수 있는 텍스트 파일("포함"이라고 함)을 포함합니다. 일반적으로 인클루드는 표준 형식을 사용하지 않는 짧은 모듈식 콘텐츠입니다. 이 위치에 저장된 파일은 [콘텐츠 재사용에](#content-reuse) 중요합니다.                                            |
| [`assets`](https://github.com/braze-inc/braze-docs/tree/develop/assets)       | 브라즈 문서에 대한 모든 이미지가 포함되어 있습니다. `_docs` 또는 `_includes` 디렉터리에 있는 모든 텍스트 파일은 이 디렉터리에 링크하여 해당 페이지에 이미지를 표시할 수 있습니다.                                                                                                                                                                         |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
전체 안내는 [미리 보기 생성을]({{site.baseurl}}/contributing/generating_a_preview/) 참조하세요.
{% endalert %}

## 페이지

Braze Docs의 각 페이지는 마크다운 구문으로 작성되며 `.md` 파일 확장자를 사용하여 마크다운 파일로 저장됩니다. 각 마크다운 파일의 맨 위에는 각 페이지에 대한 숨겨진 메타데이터를 추가하는 데 YAML 앞부분이 사용됩니다.

\`\`\`markdown
---
메타데이터\_키: 메타데이터\_값
---

# 콘텐츠
\`\`\`

다음을 교체합니다.

| 자리 표시자 | 설명 | 설명
|------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `METADATA_KEY` | 지원되는 메타데이터 유형을 나타내는 키입니다. 자세한 내용은 [메타데이터를]({{site.baseurl}}/contributing/yaml_front_matter/metadata/) 참조하세요. |
| `METADATA_VALUE` | 메타데이터 유형의 키에 할당된 값입니다. 자세한 내용은 [메타데이터를]({{site.baseurl}}/contributing/yaml_front_matter/metadata/) 참조하세요.  |
| `CONTENT` | 페이지의 콘텐츠가 마크다운 구문으로 작성되었습니다.                                                                                           |
{: .reset-td-br-1 .reset-td-br-2}

{% tabs local %}
{% tab example input %}
\`\`\`markdown
---
nav_title: Braze Docs에 기여하기
기사: Braze Docs에 기여하기
description: "브레이즈 닥스에 기여하기 위해 필요한 것은 다음과 같습니다!"
page_order: 0
search_tag: 기여
---

# Braze Docs에 기여하기

> Braze Docs에 기여해 주셔서 감사합니다! 매주 화요일과 목요일에 커뮤니티 기여를 병합하여 Braze Docs에 배포합니다. 이 가이드를 사용하여 다음 배포 시 변경 사항을 병합하세요.
\`\`\`
{% endtab %}

{% tab example output %}
![Example page on Braze Docs.]({% image_buster /assets/img/contributing/styling_examples/page.png %})
{% endtab %}
{% endtabs %}

{% alert tip %}
전체 안내는 [페이지 만들기를]({{site.baseurl}}/contributing/content_management/pages/#creating-a-page) 참조하세요.
{% endalert %}

## 이미지

이미지는 `assets/img` 안에 PNG 파일로 저장됩니다. `img` 디렉터리의 구조가 Braze Docs의 구조와 일치할 필요는 없지만, 관련 이미지를 하위 디렉터리로 그룹화하는 것이 가장 좋습니다.

각 이미지는 다음 구문을 사용하여 하나 이상의 페이지에 링크할 수 있습니다.

{% raw %}
```markdown
![ALT_TEXT.]({% image_buster /assets/img/DIRECTORY/IMAGE.png %})
```
{% endraw %}

다음을 교체합니다.

| 자리 표시자 | 설명 | 설명
|-------------|-------------------------------------------------------------------------------------------------------------------------|
| `ALT_TEXT` | 이미지의 대체 텍스트입니다. 이는 화면 리더를 사용하는 사용자도 Braze Docs에 동등하게 액세스할 수 있도록 하기 위해 필요합니다. |
| `IMAGE` | `img` 디렉터리에서 시작하는 이미지의 상대 경로입니다.                                                      |
{: .reset-td-br-1 .reset-td-br-2}

인라인 이미지는 다음과 비슷해야 합니다:

{% raw %}
```markdown
![The form for creating a new pull request on GitHub.]({% image_buster /assets/img/contributing/getting_started/github_pull_request.png %})
```
{% endraw %}

{% alert tip %}
전체 안내는 [새 이미지 추가하기를]({{site.baseurl}}/contributing/content_management/images/#adding-a-new-image) 참조하세요.
{% endalert %}

## 섹션

Braze Docs는 [기본 섹션과](#primary-sections) [하위 섹션으로](#subsections) 구성되어 있습니다.

### 기본 섹션

Braze Docs의 주요 섹션은 다음과 같습니다:

- [Braze Docs 홈]({{site.baseurl}})
- [사용 설명서]({{site.baseurl}}/user_guide/introduction)
- [개발자 가이드]({{site.baseurl}}/developer_guide/home)
- [Braze API 가이드]({{site.baseurl}}/api/home)
- [기술 파트너]({{site.baseurl}}/partners/home)
- [브레이즈 도움말]({{site.baseurl}}/help/home)
- [Braze Docs에 기여하기]({{site.baseurl}}/contributing/home/)

**브레이즈 문서에 기여하기** 외에 이러한 기본 섹션은 브레이즈 문서의 모든 페이지에서 사이트 헤더에서 액세스할 수 있습니다.

![The primary sections as shown on the site header on Braze Docs.]({% image_buster /assets/img/contributing/styling_examples/header.png %})

각 기본 섹션은 [지킬 컬렉션을](https://jekyllrb.com/docs/collections/) 사용하여 구축되므로 관련 콘텐츠를 함께 그룹화하여 쉽게 관리할 수 있습니다. 모든 기본 섹션은 컬렉션이지만 모든 컬렉션이 기본 섹션인 것은 아닙니다. 브레이즈 문서 컬렉션의 전체 목록은 지킬 구성 파일( `_config.yml`)에서 확인할 수 있습니다.

```yaml
collections:
  home:
    title: Documentation
    output: true
    default_nav_url: ''
    page_order: 1
  user_guide:
    title: User Guide
    output: true
    default_nav_url: introduction/
    page_order: 2
  developer_guide:
    title: Developer Guide
    output: true
    default_nav_url: home/
    page_order: 3
  api:
    title: API
    output: true
    default_nav_url: home/
    page_order: 4
  partners:
    title: Technology Partners
    output: true
    default_nav_url: home/
    page_order: 5
  help:
    title: Help
    output: true
    default_nav_url: home/
    page_order: 6
  contributing:
    output: true
    default_nav_url: contributing/
  hidden: # Hidden pages not directly linked via navigation
    title: Braze
    output: true
    hidden: true
  docs_pages: # Site specific pages. ie main redirects and search
    title: Braze
    output: true
    hidden: true
```

나열된 각 컬렉션은 `_docs` 디렉터리 내의 디렉터리를 나타냅니다.

```plaintext
braze-docs
└── _docs
    ├── _api
    ├── _contributing
    ├── _developer_guide
    ├── _docs_pages
    ├── _help
    ├── _hidden
    ├── _home
    ├── _partners
    └── _user_guide
```

각 기본 섹션의 랜딩 페이지는 `page_order:` 키가 `0` 으로 설정된 표준 마크다운 파일입니다.

{% tabs local %}
{% tab example input %}
\`\`\`markdown
---
1\.
주택
article_title: Braze 사용자 가이드
layout: user\_guide
user\_top\_header: "Braze 사용자 가이드"
---
\`\`\`
{% endtab %}

{% tab example output %}
![An example landing page on Braze Docs.]({% image_buster /assets/img/contributing/styling_examples/primary_section.png %})
{% endtab %}
{% endtabs %}

### 하위 섹션

Braze 문서의 모든 기본 섹션에는 하나 이상의 하위 섹션이 있으며, 각 하위 섹션은 왼쪽 탐색에서 확장 가능한 항목을 나타냅니다.

기본 섹션과 달리 하위 섹션은 랜딩 페이지를 포함하거나 포함하지 않고 구성할 수 있습니다. 랜딩 페이지가 없는 하위 섹션은 관련 콘텐츠를 함께 정리하는 동시에 Braze 문서에서 쓸모없는 페이지의 수를 최소화하는 데 도움이 됩니다. 하위 섹션이 랜딩 페이지를 포함하거나 포함하지 않고 구성되든 모든 하위 섹션은 리포지토리의 디렉토리와 마크다운 파일을 모두 나타냅니다. 예를 들어 다음을 참조하세요.

```plaintext
braze-docs
└── _docs
    └── _primary_section
        ├── subsection_a
        │   ├── page_a.md
        │   └── page_b.md
        ├── subsection_b
        │   ├── page_a.md
        │   └── page_b.md
        ├── subsection_a.md # not configured as a landing page
        └── subsection_b.md # configured as a landing page  
```

{% alert tip %}
전체 안내는 [섹션 만들기를]({{site.baseurl}}/contributing/content_management/sections/#creating-a-section) 참조하세요.
{% endalert %}

`_primary_section` 디렉터리에서 `subsection_a` 에는 랜딩 페이지가 구성되어 있지 않은 반면 `subsection_b` 에는 랜딩 페이지가 구성되어 있습니다. 다음 예제에서 `subsection_a.md` 에는 `config_only:` 이 `true` 로 설정되어 있어 이 페이지가 랜딩 페이지로 렌더링되지 않습니다.

{% tabs local %}
{% tab example input %}
\`\`\`markdown
---
nav_title: 하위 섹션 A
1\.
true
---
\`\`\`
{% endtab %}

{% tab example output %}
![The left-side navigation on Braze Docs, showing an example of an expanded section without a landing page.]({% image_buster /assets/img/contributing/styling_examples/subsection_config_only.png %})
{% endtab %}
{% endtabs %}

그러나 `subsection_b.md` 은 `config_only:` 키를 사용하지 않으므로 이 페이지는 랜딩 페이지로 _렌더링됩니다_.

{% tabs local %}
{% tab example input %}
\`\`\`markdown
---
nav_title: 하위 섹션 B
1\.
---
\`\`\`
{% endtab %}

{% tab example output %}
![The left-side navigation on Braze Docs, showing an example of an expanded section with a landing page.]({% image_buster /assets/img/contributing/styling_examples/subsection_landing_page.png %})
{% endtab %}
{% endtabs %}

{% alert note %}
`config_only:` 이 `true` 으로 설정된 하위 섹션은 페이지로 렌더링되지 않지만 하위 섹션의 디렉토리 이름은 해당 하위 섹션에 있는 페이지의 URL에 계속 사용됩니다. 자세한 내용은 [URL을](#urls) 참조하세요.
{% endalert %}

## 콘텐츠 재사용

지킬은 `include` 태그를 사용하여 문서 전체에서 작성된 콘텐츠를 재사용할 수 있는 기능을 제공합니다. 포함 파일은 `_includes` 디렉터리에 있으며, 마크다운 또는 HTML 구문으로 작성할 수 있습니다.

```markdown
{% raw %}{% multi_lang_include RELATIVE_PATH/FILE %}{% endraw %}
```

다음을 교체합니다:

| 자리 표시자 | 설명 | 설명
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `RELATIVE_PATH` | (선택 사항) `_includes` 디렉터리에서 파일의 상대 경로입니다. `_includes/braze/upgrade_notice.md` 과 같이 `_includes` 디렉터리 내에 있는 디렉터리의 파일을 포함하는 경우에만 필요합니다. |
| `FILE` | 파일 확장자를 포함한 파일 이름입니다.                                                                                                                                                                      |
{: .reset-td-br-1 .reset-td-br-2}

{% tabs local %}
{% tab example input %}
{% raw %}
\`\`\`markdown
# 페이지

> Braze 문서에서 페이지를 만들고, 수정하고, 제거하는 방법을 알아보세요.

{% multi_lang_include contributing/prerequisites.md %}
\`\`\`
{% endraw %}
{% endtab %}

{% tab example output %}
![Content reuse example on Braze Docs.]({% image_buster /assets/img/contributing/styling_examples/includes.png %})
{% endtab %}
{% endtabs %}

{% alert tip %}
전체 안내는 [콘텐츠 재사용을]({{site.baseurl}}/contributing/content_management/reusing_content) 참조하세요.
{% endalert %}

## 레이아웃

기본적으로 지킬은 `_layouts` 디렉토리의 `default.html` 레이아웃을 사용하여 Braze Docs의 각 페이지를 작성합니다. 그러나 YAML 앞부분의 `layout:` 키에 레이아웃을 할당하여 다른 레이아웃을 사용할 수 있습니다.

\`\`\`markdown
---
layout: LAYOUT\_VALUE
---
\`\`\`

`LAYOUT_VALUE` 을 레이아웃 파일의 이름으로 바꾸고 파일 확장자를 제거합니다.

{% tabs local %}
{% tab example input %}
**파일 트리**

```plaintext
braze-docs
└── _layouts
    └── api_page.html
```

**페이지 내 메타데이터**

\`\`\`markdown
---
layout: api\_page
---
\`\`\`
{% endtab %}

{% tab example output %}
![API glossary layout example on Braze Docs.]({% image_buster /assets/img/contributing/styling_examples/layouts/api_page.png %})
{% endtab %}
{% endtabs %}

{% alert tip %}
자세한 내용은 [페이지 레이아웃을]({{site.baseurl}}/contributing/yaml_front_matter/page_layouts) 참조하세요.
{% endalert %}

## URL

Braze Docs의 URL은 항상 문서 저장소 내의 디렉토리 구조와 일치합니다. 다음 예제 파일 트리를 고려할 때 `page_a.md` 의 URL은 `https://www.braze.com/docs/primary_section/subsection_a/page_a` 입니다.

```plaintext
braze-docs
└── _docs
    └── _primary_section
        └── subsection_a
            └── page_a.md
```

여기에는 `config_only:` 이 `true` 으로 설정된 [하위 섹션에](#subsections) 있는 페이지의 URL이 포함됩니다. `config_only` 하위 섹션이 페이지로 렌더링되지 않더라도 하위 섹션의 디렉토리 이름은 해당 디렉토리에 있는 페이지의 URL을 생성하는 데 사용됩니다. 예를 들어 다음을 참조하세요.

```plaintext
braze-docs
└── _docs
    └── _primary_section
        ├── subsection_a
        │   ├── page_a.md
        │   └── page_b.md
        ├── subsection_b
        │   ├── page_a.md
        │   └── page_b.md
        ├── subsection_a.md # not configured as a landing page
        └── subsection_b.md # configured as a landing page  
```

{% tabs local %}
{% tab subsection a %}

**랜딩 페이지 예시**

\`\`\`markdown
---
nav_title: 하위 섹션 A
page_order: 1
config_only: true
---
\`\`\`

`subsection_a.md` 이 랜딩 페이지로 구성되어 있으므로 `page_a.md` 및 `page_b.md` 만 고유 URL을 받게 됩니다. `subsection_b.md` 에는 어떤 URL도 **수신되지 않습니다**.

**URL 예시**

```plaintext
Subsection A URL: N/A
Page A URL: https://www.braze.com/docs/primary_section/subsection_a/page_a
Page B URL: https://www.braze.com/docs/primary_section/subsection_a/page_b
```
{% endtab %}
{% tab subsection b %}
**랜딩 페이지 예시**

\`\`\`markdown
---
nav_title: 하위 섹션 B
page_order: 2 
---
\`\`\`

`subsection_b.md` 이 랜딩 페이지로 구성되어 있으므로 `page_a.md`, `page_b.md`, `subsection_b.md` 은 고유한 URL을 받게 됩니다.

**URL 예시**

```plaintext
Subesction B URL: https://www.braze.com/docs/primary_section/subsection_b
Page A URL: https://www.braze.com/docs/primary_section/subsection_b/page_a
Page B URL: https://www.braze.com/docs/primary_section/subsection_b/page_b
```
{% endtab %}
{% endtabs %}
