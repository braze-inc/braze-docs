---
nav_title: 電子メールガイドライン
article_title: 電子メールガイドライン
page_order: 1
page_type: reference
description: "この記事では、さまざまなユースケースとトピックのメールキャンペーンを構築する際に留意すべき一般的なヒントとコツについて説明します。"
channel: email

---

# 電子メールガイドライン

> メールキャンペーンを構築する際には、さまざまなユーザとメールサービスプロバイダ(ESP)間でメールメッセージがどのように受信されるかに留意することが重要です。 

コンテンツを作成する際に留意すべきいくつかのヒントを以下に示します。

- メールをフォーマットする場合は、CSS としてインラインスタイルシートを使用します。
- モバイルバージョンとデスクトップバージョンの両方に1 つのメールテンプレートを使用するには、幅を500 ピクセル未満に保ちます。
- メールテンプレートにアップロードされるイメージは5MB 未満である必要があります。サポートされる形式には、PNG、JPEG、GIF などがあります。
- イメージの高さと幅を設定しないでください。これにより、劣化した電子メールに不要な空白が生じます。
- `div` ほとんどの電子メールクライアントがタグの使用をサポートしていないため、タグは使用しないでください。代わりに、ネストした表を使用します。
- JavaScript はESP では動作しないため、使用しないでください。
- Braze は、グローバルCDN を使用してすべてのメールイメージをホストすることで、ロード時間を改善します。

### 代替テキストの実装

スパムフィルタは、メッセージのHTML とプレーンテキストバージョンの両方を監視するため、プレーンテキストの代替を使用すると、スパムスコアを下げるのに便利です。さらに、代替テキスト`(alt="")` は、ユーザの電子メールプロバイダによってフィルタリングされた可能性がある電子メール本文に含まれている画像を補完し、場合によってはその代わりに使用できます。スクリーンリーダーは、画像を説明するためにaltテキストを発表するので、これは、画像に関する重要な情報を提供するためにプレーン言語を使用する機会である。

### メール検証

{% alert important %}
検証は、ダッシュボードの電子メールアドレス、エンドユーザーの電子メールアドレス(顧客)、および電子メールメッセージの送信元アドレスと返信先アドレスに使用されます。
{% endalert %}

メール検証は、ユーザのメールアドレスが更新された場合、またはAPI、CSV アップロード、SDK、またはダッシュボードで変更されている場合に実行されます。メールアドレスに空白を含めることはできません。API を使用して送信する場合、空白は400 エラーになります。

ブレーズ・サーバーを介してターゲットとなる電子メール・アドレスは、[RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822)標準に従って検証されなければなりません。ブレーズは特定の文字を受け入れず、無効として認識します。メールがバウンスされた場合、Braze はメールを無効としてマークし、サブスクリプションステータスは変更されません。 

{% details Unaccepted characters outside of RFC standards %}
\- *
\- /
\- ?
\- !
\- $
\- #
\- %
\- ^
\- &
\- (
\- )
\- {
\- }
\- [
\- ]
\- ~
\- ,
{% enddetails %}

### アドレスの設定と返信

"from"addresses を設定するときは、"from"emailドメインが送信ドメイン(`marketing.yourdomain.com`など)と一致していることを確認してください。これを怠ると、SPF とDKIM のアライメントミスが発生する可能性があります。すべての返信メールをルートドメインに設定できます。

### HTMLの詳細を確認する

一部のHTML タグおよび属性は、悪意のあるコードをブラウザで実行する可能性があるため、許可されていないことに注意してください。

メールで許可されていないHTML タグと属性については、次のリストを参照してください。
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
(+)
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


[24]: http://tools.ietf.org/html/rfc2822

