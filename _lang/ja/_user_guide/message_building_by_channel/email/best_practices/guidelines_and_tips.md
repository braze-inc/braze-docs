---
nav_title: Eメールガイドライン
article_title: Eメールガイドライン
page_order: 1
page_type: reference
description: "この記事では、様々なユースケースやトピックに対応したメールキャンペーンを構築する際に覚えておきたい一般的なヒントを紹介する。"
channel: email

---

# 電子メールのガイドライン

> Eメールキャンペーンを構築する際、様々なユーザーやEメールサービスプロバイダー（ESP）間でEメールメッセージがどのように受け取られるかを念頭に置くことが重要である。 

コンテンツを構築する際に覚えておきたい簡単なヒントをいくつか紹介しよう：

- メールをフォーマットするときは、インラインスタイルシートをCSSとして使用する。
- 1つのメールテンプレートをモバイル版とデスクトップ版の両方で使用するには、幅を500ピクセル以下に保つ。
- Eメールテンプレートにアップロードする画像は5MB以下でなければならない。対応フォーマットはPNG、JPEG、GIFだ。
- 画像に高さや幅を設定しないこと。劣化したメールに不要な余白が生じるからだ。
- `div` タグは、ほとんどの電子メールクライアントがその使用をサポートしていないため、使用すべきではない。その代わりに、ネストされたテーブルを使う。
- JavaScriptの使用は、どのESPでも使えないので避けること。
- Brazeは、すべてのメール画像をホストするためにグローバルCDNを使用することにより、ロード時間を改善する。

### 代替テキストを導入する

スパムフィルターは、HTMLとプレーンテキストの両方を見ているため、プレーンテキストの代替を利用することは、スパムスコアを下げる素晴らしい方法である。さらに、代替テキスト（`(alt="")` ）は、メール本文に含まれる画像を補完し、場合によっては、ユーザーのメールプロバイダーによってフィルタリングされた画像の代わりとなる。スクリーンリーダーは画像を説明するためにaltテキストを発表する。

### 電子メールの検証

{% alert important %}
バリデーションは、ダッシュボードのEメールアドレス、エンドユーザーのEメールアドレス（あなたの顧客）、Eメールメッセージの送信元アドレスと返信先アドレスに使用される。
{% endalert %}

ユーザーのメールアドレスが更新された場合、またはAPI、CSVアップロード、SDK経由でBrazeにインポートされた場合、またはダッシュボードで変更された場合に、メールアドレスのバリデーションが行われる。また、APIを使用して送信する場合、空白文字は400エラーとなる。

Brazeサーバーをターゲットとする電子メールアドレスは、[RFC2822](https://datatracker.ietf.org/doc/html/rfc2822)標準に従って検証されなければならない。メールがバウンスされた場合、Brazeはそのメールを無効としてマークし、購読ステータスは変更されない。 

{% details RFC標準外の受け入れ不可能な文字 %}
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
- \[
- ]
- ~
- ,
{% enddetails %}

### 送信元アドレスと返信先アドレスを設定する

from "アドレスを設定する際は、"from "メールドメインが送信ドメイン（`marketing.yourdomain.com` など）と一致していることを確認すること。一致しない場合、SPF と DKIM の不一致が生じる可能性があります。すべての返信先メールアドレスをルートドメインに設定できます。

### HTMLの詳細をチェックする

HTMLのタグや属性の中には、ブラウザ上で悪意のあるコードを実行させる可能性があるため、許可されていないものがあることを覚えておいてほしい。

Eメールで使用できないHTMLタグや属性については、以下のリストをチェックしよう：
{% details 許可されていないHTMLタグを拡張する %}
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

{% details 許可されないHTML属性を拡張する %}
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


[24]: http://tools.ietf.org/html/rfc2822

