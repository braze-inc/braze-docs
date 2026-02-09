---
nav_title: 랜딩 페이지
article_title: Landing Pages
page_order: 31
guide_top_header: "Landing Pages"
description: "이 문서에는 Braze 랜딩 페이지를 구축하고 커스텀하는 리소스가 포함되어 있습니다."
alias: /landing_pages/
---

# About landing pages

> 브레이즈 랜딩 페이지는 사용자 확보 및 참여 전략을 추진할 수 있는 독립형 웹 페이지입니다.

랜딩 페이지를 사용하여 잠재고객을 늘리고, 사용자 데이터를 수집하고, 특별 행사를 홍보하고, 멀티채널 캠페인을 지원하세요.

{% alert note %}
랜딩 페이지 및 커스텀 도메인 사용 가능 여부는 Braze 패키지에 따라 다릅니다. 시작하려면 계정 매니저 또는 고객 성공 매니저에게 문의하세요.
{% endalert %}

{% multi_lang_include video.html id="eg4r7agod1" source="wistia" %}

## 필수 조건

랜딩 페이지에 액세스하고, 만들고, 게시하려면 관리자 [권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) 또는 다음 권한이 모두 필요합니다:

- Access Landing Pages
- Create Landing Page Drafts
- Publish Landing Pages

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## Plan tiers

The number of published landing pages and custom domains you can use depends on your plan type: free or paid (incremental).

| Feature                                                                                                   | Free tier     | Paid tier (incremental)     |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| Published landing pages                                                                 | Five per company | 20 additional |
| Custom domains          | One per company | Five additional |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## 랜딩 페이지에 Google 태그 매니저 추가하기

랜딩 페이지에 Google 태그 매니저를 추가하려면 드래그 앤 드롭 편집기에서 랜딩 페이지에 **커스텀 코드** 블록을 추가한 다음 태그 매니저 코드를 블록에 삽입합니다. 이 예제에서처럼 태그 매니저 코드 앞에 데이터 레이어를 추가해야 합니다:

```
<script>
window.dataLayer = window.dataLayer || [];
</script>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXX');</script>
<!-- End Google Tag Manager -->
```

Google 태그 매니저 구현에 대한 자세한 내용은 [Google 설명서를 참조](https://developers.google.com/tag-platform/tag-manager/datalayer#installation)하세요 [.](https://developers.google.com/tag-platform/tag-manager/datalayer#installation)

## Frequently asked questions

### What's the maximum size for landing pages?

랜딩 페이지 본문 크기는 최대 500KB까지 가능합니다.

### Are there any technical requirements to publish a landing page?

No, there aren't any technical requirements.

### Is there an HTML editor for landing pages?

예. 드래그 앤 드롭 편집기에서 **사용자 지정 코드** 블록을 사용하여 HTML을 추가하거나 편집합니다.

### 랜딩 페이지 안에 웹훅을 만들 수 있나요?

아니요, 현재 지원되지 않습니다.
