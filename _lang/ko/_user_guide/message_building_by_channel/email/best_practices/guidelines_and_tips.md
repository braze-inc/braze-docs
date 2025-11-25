---
nav_title: 이메일 가이드라인
article_title: 이메일 가이드라인
page_order: 1
page_type: reference
description: "이 문서에서는 다양한 사용 사례와 주제를 위한 이메일 캠페인을 구축할 때 염두에 두어야 할 일반적인 팁과 요령을 다룹니다."
channel: email

---

# 이메일 가이드라인

> 이메일 캠페인을 구축할 때, 다양한 사용자와 이메일 서비스 제공업체(ESP)에서 이메일 메시지가 어떻게 수신되는지를 염두에 두는 것이 중요합니다. 

콘텐츠를 구축할 때 염두에 두어야 할 몇 가지 빠른 팁은 다음과 같습니다:

- 이메일을 포맷할 때는 CSS로 인라인 스타일 시트를 사용하세요.
- 모바일과 데스크탑 버전 모두에 대해 하나의 이메일 템플릿을 사용하려면 너비를 500픽셀 이하로 유지하세요.
- 이메일 템플릿에 업로드된 이미지는 5MB 미만이어야 합니다. 지원되는 형식에는 PNG, JPEG 및 GIF가 포함됩니다.
- 이미지의 높이와 너비를 설정하지 마세요. 이는 저하된 이메일에서 불필요한 공백을 초래할 수 있습니다.
- `div` 태그는 대부분의 이메일 클라이언트에서 지원되지 않으므로 사용하지 않아야 합니다. 대신 중첩 테이블을 사용하세요.
- JavaScript 사용을 피하세요. 이는 어떤 ESP와도 작동하지 않습니다.
- Braze는 모든 이메일 이미지를 호스팅하기 위해 글로벌 CDN을 사용하여 로드 시간을 개선합니다.

### 대체 텍스트 구현하기

스팸 필터는 메시지의 HTML 및 일반 텍스트 버전을 모두 감시하므로, 일반 텍스트 대안을 활용하는 것은 스팸 점수를 낮추는 좋은 방법입니다. 또한, 대체 텍스트 `(alt="")`는 사용자의 이메일 제공업체에 의해 필터링된 이메일 본문에 포함된 이미지를 보완하거나 경우에 따라 대신할 수 있습니다. 스크린 리더는 이미지를 설명하기 위해 대체 텍스트를 발표하므로, 이는 이미지에 대한 주요 정보를 제공하기 위해 간단한 언어를 사용할 수 있는 기회입니다.

### 이메일 검증

{% alert important %}
검증은 대시보드 이메일 주소, 최종 사용자 이메일 주소(고객) 및 이메일 메시지의 발신자 및 회신 주소에 사용됩니다.
{% endalert %}

이메일 검증은 사용자의 이메일 주소가 업데이트되거나 API, CSV 업로드, SDK를 통해 Braze에 가져오거나 대시보드에서 수정될 때 수행됩니다. 이메일 주소에는 공백이 포함될 수 없으며, API를 사용하여 전송할 경우 공백은 400 오류를 초래합니다.

Braze 서버를 통해 타겟팅된 이메일 주소는 [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822) 표준에 따라 검증되어야 하며, Braze는 특정 문자를 허용하지 않으며 이를 유효하지 않은 것으로 인식합니다. 이메일이 반송되면 Braze는 이메일을 유효하지 않은 것으로 표시하고 구독 상태는 변경되지 않습니다. 

{% details Unaccepted characters outside of RFC standards %}
- *
- /
- ?
- !
- $
- #
- %
- ^
- &
- (
- )
- {
- }
- [
- ]
- ~
- ,
{% enddetails %}

### 보낸 사람 및 회신 주소 설정

"보낸 사람" 주소를 설정할 때, "보낸 사람" 이메일 도메인이 발송 도메인(예: `marketing.yourdomain.com`)과 일치하는지 확인하세요. 이 작업을 수행하지 않으면 SPF 및 DKIM 불일치가 발생할 수 있습니다. 모든 회신 이메일은 귀하의 루트 도메인으로 설정할 수 있습니다.

{% alert note %}
"보낸 사람" 주소에서 유니코드 인코딩은 지원되지 않습니다.
{% endalert %}

### HTML 세부정보 확인

일부 HTML 태그 및 속성은 허용되지 않으므로 악성 코드가 브라우저에서 실행될 수 있습니다.

이메일에서 허용되지 않는 HTML 태그 및 속성에 대한 다음 목록을 확인하세요:
{% details Expand for disallowed HTML tags %}
- `<!doctype>`
- `<applet>`
- `<bgsound>`
- `<embed>`
- `<frameset>`
- `<iframe>`
- `<ilayer>`
- `<layer>`
- `<link>`
- `<meta>`
- `<object>`
- `<script>`
- `<title>`
- `<xml>`
- `<svg>`
{% enddetails %}

{% details Expand for disallowed HTML attributes %}
- `<animationend>`
- `<animationiteration>`
- `<animationstart>`
- `<data-bind>`
- `<fscommand>`
- `<onabort>`
- `<onabort>`
- `<onactivate>`
- `<onafterprint>`
- `<onafterupdate>`
- `<onbeforeactivate>`
- `<onbeforecopy>`
- `<onbeforecut>`
- `<onbeforedeactivate>`
- `<onbeforeeditfocus>`
- `<onbeforepaste>`
- `<onbeforeprint>`
- `<onbeforeunload>`
- `<onbeforeupdate>`
- `<onbegin>`
- `<onblur>`
- `<onbounce>`
- `<oncanplay>`
- `<oncanplaythrough>`
- `<oncellchange>`
- `<onchange>`
- `<onclick>`
- `<oncontextmenu>`
- `<oncontrolselect>`
- `<oncopy>`
- `<oncut>`
- `<ondataavailable>`
- `<ondatasetchanged>`
- `<ondatasetcomplete>`
- `<ondblclick>`
- `<ondeactivate>`
- `<ondrag>`
- `<ondragdrop>`
- `<ondragend>`
- `<ondragenter>`
- `<ondragleave>`
- `<ondragover>`
- `<ondragstart>`
- `<ondrop>`
- `<ondurationchange>`
- `<onemptied>`
- `<onend>`
- `<onended>`
- `<onerror>`
- `<onerror>`
- `<onerrorupdate>`
- `<onfilterchange>`
- `<onfinish>`
- `<onfocus>`
- `<onfocusin>`
- `<onfocusout>`
- `<onhashchange>`
- `<onhelp>`
- `<oninput>`
- `<oninvalid>`
- `<onkeydown>`
- `<onkeypress>`
- `<onkeyup>`
- `<onlayoutcomplete>`
- `<onload>`
- `<onloadeddata>`
- `<onloadedmetadata>`
- `<onloadstart>`
- `<onlosecapture>`
- `<onmediacomplete>`
- `<onmediaerror>`
- `<onmessage>`
- `<onmousedown>`
- `<onmouseenter>`
- `<onmouseleave>`
- `<onmousemove>`
- `<onmouseout>`
- `<onmouseover>`
- `<onmouseup>`
- `<onmousewheel>`
- `<onmove>`
- `<onmoveend>`
- `<onmovestart>`
- `<onoffline>`
- `<ononline>`
- `<onopen>`
- `<onoutofsync>`
- `<onpagehide>`
- `<onpageshow>`
- `<onpaste>`
- `<onpause>`
- `<onplay>`
- `<onplaying>`
- `<onpopstate>`
- `<onprogress>`
- `<onpropertychange>`
- `<onratechange>`
- `<onreadystatechange>`
- `<onredo>`
- `<onrepeat>`
- `<onreset>`
- `<onresize>`
- `<onresizeend>`
- `<onresizestart>`
- `<onresume>`
- `<onreverse>`
- `<onrowdelete>`
- `<onrowexit>`
- `<onrowinserted>`
- `<onrowsenter>`
- `<onscroll>`
- `<onsearch>`
- `<onseek>`
- `<onseeked>`
- `<onseeking>`
- `<onselect>`
- `<onselectionchange>`
- `<onselectstart>`
- `<onshow>`
- `<onstalled>`
- `<onstart>`
- `<onstop>`
- `<onstorage>`
- `<onsubmit>`
- `<onsuspend>`
- `<onsyncrestored>`
- `<ontimeerror>`
- `<ontimeupdate>`
- `<ontoggle>`
- `<ontouchcancel>`
- `<ontouchend>`
- `<ontouchmove>`
- `<ontouchstart>`
- `<ontrackchange>`
- `<onundo>`
- `<onunload>`
- `<onurlflip>`
- `<onvolumechange>`
- `<onwaiting>`
- `<onwheel>`
- `<seeksegmenttime>`
- `<transitionend>`
{% enddetails %}



