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
- メールテンプレートにアップロードされるすべての画像は 5 MB 未満でなければなりません。サポートされている形式には PNG、JPEG、および GIF があります。
- 画像に高さや幅を設定しないこと。劣化したメールに不要な余白が生じるからだ。
- `div` タグは、ほとんどの電子メールクライアントがその使用をサポートしていないため、使用すべきではない。その代わりに、ネストされたテーブルを使う。
- JavaScript は メールサービスプロバイダー (ESP) でサポートされていないため、使用しないでください。
- Brazeは、すべてのメール画像をホストするためにグローバルCDNを使用することにより、ロード時間を改善する。

### 代替テキストを導入する

スパムフィルターは、HTMLとプレーンテキストの両方を見ているため、プレーンテキストの代替を利用することは、スパムスコアを下げる素晴らしい方法である。さらに、代替テキスト（`(alt="")` ）は、メール本文に含まれる画像を補完し、場合によっては、ユーザーのメールプロバイダーによってフィルタリングされた画像の代わりとなる。スクリーンリーダーは、画像を説明するために alt テキストを読み上げるので、これは、平易な文章で画像に関する重要な情報を提供する機会です。

### メールの検証

{% alert important %}
検証は、ダッシュボードのメールアドレス、エンドユーザーのメールアドレス （お客様の顧客）、およびメールメッセージの送信元および返信先アドレスに対して行われます。
{% endalert %}

ユーザーのメールアドレスが更新された場合、またはAPI、CSVアップロード、SDK経由でBrazeにインポートされた場合、またはダッシュボードで変更された場合に、メールアドレスのバリデーションが行われる。メールアドレスに空白を含めることはできませず。API を使用して送信する場合、空白により 400 エラーが発生することに注意してください。

Braze サーバーを介してターゲットされるメールアドレスは、[RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822) 標準に従って検証されなければなりません。Braze は特定の文字を受け入れず、無効として認識します。メールがバウンスされた場合、Braze はメールを無効としてマークし、その購読ステータスは変更されません。 

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
- [
- ]
- ~
- ,
{% enddetails %}

### 差出人アドレスと返信先アドレスの設定

from "アドレスを設定する際は、"from "メールドメインが送信ドメイン（`marketing.yourdomain.com` など）と一致していることを確認すること。一致しない場合、SPF と DKIM の不一致が生じる可能性があります。すべての返信先メールアドレスをルートドメインに設定できます。

{% alert note %}
Unicodeエンコーディングは、「差出人」のアドレスではサポートされていません。
{% endalert %}

### HTMLの詳細をチェックする

HTMLのタグや属性の中には、ブラウザ上で悪意のあるコードを実行させる可能性があるため、許可されていないものがあることを覚えておいてほしい。

Eメールで使用できないHTMLタグや属性については、以下のリストをチェックしよう：
{% details 展開して、許可されていない HTML タグを表示 %}
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

{% details 展開して、許可されていない HTML 属性を表示 %}
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



