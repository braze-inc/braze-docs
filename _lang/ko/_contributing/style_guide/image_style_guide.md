---
nav_title: 이미지 카피 스타일 가이드
article_title: 이미지 카피 스타일 가이드
description: "Braze 문서에서 이미지를 생성하고 스타일링하기 위한 가이드라인입니다."
page_order: 1
noindex: true
---

# 이미지 카피 스타일 가이드

<style>
.style-guide-table td {
  overflow-wrap: break-word;
  word-break: break-word;
  min-width: 0;
}
</style>

## 배치 및 크기 최적화

가능하면 관련 텍스트 근처에 이미지를 배치하고, 이미지 스타일링 마크다운을 사용하여 큰 이미지의 크기를 조정하세요. 일부 콘텐츠의 경우 이미지와 사용 가능한 공간에 따라 [텍스트를 페이지의 왼쪽 또는 오른쪽에 앵커링]({{site.baseurl}}/home/styling_test_page/#image-test)하여 처리해야 합니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/optimize_placement_do.png %}" alt="이미지 배치를 올바르게 최적화한 예시."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/optimize_placement_dont.png %}" alt="이미지 배치를 잘못 최적화한 예시."></td></tr>
</tbody>
</table>
{:/}

## 이미지 자르기

관련 섹션을 가깝게 잘라주세요. 필요한 경우가 아니라면 왼쪽 내비게이션 바를 포함하지 말고, 대신 문서에 내비게이션 방향을 안내하세요. 이렇게 하면 UI가 변경될 때 수정해야 하는 이미지 수를 줄일 수 있습니다.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_do_1.png %}" alt="올바르게 잘린 이미지 예시."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_dont_1.png %}" alt="잘못 잘린 이미지 예시."></td></tr>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_do_2.png %}" alt="올바르게 잘린 이미지 예시."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_dont_2.png %}" alt="잘못 잘린 이미지 예시."></td></tr>
</tbody>
</table>
{:/}

Braze 문서에서는 이미 각 이미지에 테두리를 추가하므로, 섹션 스크린샷에서는 테두리를 생략하세요. 깔끔하게 자르는 것이 목표입니다. 테두리 바깥이나 안쪽에 구성요소가 있는 경우에는 테두리를 남겨둘 수 있습니다. 다음 이미지를 예시로 참고하세요.

**권장:**
![이미지를 올바르게 자른 예시.]({% image_buster /assets/img/contributing/style_guide/cropping_do_3.png %})

**비권장:**  
![이미지를 잘못 자른 예시.]({% image_buster /assets/img/contributing/style_guide/cropping_dont_3.png %})
  
**권장:**  
![이미지를 올바르게 자른 예시.]({% image_buster /assets/img/contributing/style_guide/cropping_do_4.png %})

## 민감한 정보 블러 처리

이름, 이메일, API 키 등 개인 식별 정보(PII)는 블러 처리하세요.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/censorship_do.png %}" alt="올바르게 블러 처리한 예시."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/censorship_dont.png %}" alt="잘못 블러 처리한 예시."></td></tr>
</tbody>
</table>
{:/}

## 이미지 안에 중요한 텍스트를 삽입하지 마세요

모든 사용자가 영어 텍스트를 읽을 수 있는 것은 아니며, 페이지 번역 도구는 이미지를 번역하지 않으므로 이미지 안에 텍스트를 삽입하지 마세요. 해당 텍스트는 문서 본문에 제공해야 합니다. 사용자의 접근성을 최대한 보장하기 위해 이미지에 대체 텍스트를 제공하세요.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/embed_text_do.png %}" alt="이미지에 텍스트를 삽입하지 않은 올바른 예시."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/embed_text_dont.png %}" alt="이미지에 텍스트를 잘못 삽입한 예시."></td></tr>
</tbody>
</table>
{:/}

## 구성요소를 강조하지 마세요

필요한 경우가 아니라면 이미지의 구성요소를 강조하지 마세요. 이미지의 다양한 구성요소를 강조할 때는 얇은~중간 두께의 파란색 사각형(가장 접근성이 좋은 옵션)을 사용하세요. "강조 섹션"이 일반 UI를 가리지 않도록 주의하세요.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">권장</th><th style="width: 50%;">비권장</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_do_1.png %}" alt="이미지에서 구성요소를 올바르게 강조한 예시."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_dont_1.png %}" alt="이미지에서 구성요소를 잘못 강조한 예시."></td></tr>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_do_2.png %}" alt="이미지에서 구성요소를 올바르게 강조한 예시."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_dont_2.png %}" alt="이미지에서 구성요소를 잘못 강조한 예시."></td></tr>
</tbody>
</table>
{:/}