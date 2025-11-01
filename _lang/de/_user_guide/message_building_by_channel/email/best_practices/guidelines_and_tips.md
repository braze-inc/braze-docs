---
nav_title: E-Mail-Richtlinien
article_title: E-Mail-Richtlinien
page_order: 1
page_type: reference
description: "Dieser Artikel enthält allgemeine Tipps und Tricks, die Sie bei der Erstellung von E-Mail-Kampagnen für verschiedene Anwendungsfälle und Themen beachten sollten."
channel: email

---

# E-Mail-Richtlinien

> Bei der Erstellung Ihrer E-Mail-Kampagne müssen Sie berücksichtigen, wie Ihre E-Mail-Nachrichten von den verschiedenen Benutzern und E-Mail-Dienstanbietern (ESPs) empfangen werden. 

Hier sind einige kurze Tipps, die Sie bei der Erstellung Ihrer Inhalte beachten sollten:

- Verwenden Sie bei der Formatierung Ihrer E-Mail Inline-Stylesheets als CSS.
- Wenn Sie eine E-Mail-Template sowohl für die mobile als auch für die Desktop-Version verwenden möchten, sollten Sie die Breite unter 500 Pixel halten.
- Die in das Template für die E-Mail hochgeladenen Bilder müssen kleiner als 5 MB sein. Unterstützte Formate sind PNG, JPEG und GIF.
- Legen Sie keine Höhen und Breiten für Bilder fest, da dies zu unnötigem Leerraum in einer degradierten E-Mail führt.
- `div`-Tags sollten nicht verwendet werden, da die meisten E-Mail-Clients ihre Verwendung nicht unterstützen. Verwenden Sie stattdessen verschachtelte Tabellen.
- Vermeiden Sie die Verwendung von JavaScript, da es mit keinem ESP funktioniert.
- Braze verbessert die Ladezeiten, indem es ein globales CDN verwendet, um alle E-Mail-Bilder zu hosten.

### Implementierung von Alternativtext

Da Spam-Filter sowohl auf eine HTML- als auch auf eine Nur-Text-Version einer Nachricht achten, ist die Verwendung von Nur-Text-Alternativen eine gute Möglichkeit, Ihre Spam-Quote zu senken. Darüber hinaus kann alternativer Text `(alt="")` dazu dienen, Bilder in Ihrer E-Mail zu ergänzen und in manchen Fällen zu ersetzen, die vom E-Mail-Anbieter der Nutzerin oder des Nutzers herausgefiltert wurden. Bildschirmleseprogramme geben Alt-Text zur Erläuterung von Bildern bekannt. Dies ist also eine Gelegenheit, die wichtigsten Informationen über ein Bild in einfacher Sprache zu vermitteln.

### E-Mail-Validierung

{% alert important %}
Die Validierung wird für Dashboard-E-Mail-Adressen, Endnutzer-E-Mail-Adressen (Ihre Kund:innen) sowie Absender- und Antwort-E-Mail-Adressen einer Nachricht verwendet.
{% endalert %}

Die E-Mail-Überprüfung wird durchgeführt, wenn die E-Mail-Adresse einer Nutzerin oder eines Nutzers aktualisiert wurde oder über API, CSV-Upload, SDK in Braze importiert oder im Dashboard geändert wurde. Beachten Sie, dass Ihre E-Mail-Adressen keine Leerzeichen enthalten dürfen. Wenn Sie sie über die API senden, führen Leerzeichen zu einem 400-Fehler.

E-Mail-Adressen, die über die Braze-Server angesprochen werden, müssen gemäß [RFC 2822-Standards](https://datatracker.ietf.org/doc/html/rfc2822) validiert werden. Braze akzeptiert bestimmte Zeichen nicht und erkennt sie als ungültig an. Wenn eine E-Mail gebounced wird, markiert Braze die E-Mail als ungültig und der Status des Abos wird nicht geändert. 

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

### Absender- und Antwortadressen festlegen

Achten Sie beim Einrichten Ihrer Absenderadressen darauf, dass Ihre Absender-E-Mail-Domäne mit Ihrer Absenderdomäne übereinstimmt (z. B. `marketing.yourdomain.com`). Wenn Sie dies nicht tun, kann dies zu einer falschen Ausrichtung von SPF und DKIM führen. Alle Antwort-E-Mails können auf Ihre Stammdomäne eingestellt werden.

{% alert note %}
Unicode encoding is not supported in "from" addresses.
{% endalert %}

### Prüfen von HTML-Details

Denken Sie daran, dass einige HTML-Tags und -Attribute nicht erlaubt sind, da sie möglicherweise bösartigen Code im Browser laufen lassen können.

In den folgenden Listen finden Sie HTML Tags und Attribute, die in Ihren E-Mails nicht zulässig sind:
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



