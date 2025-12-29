---
nav_title: E-Mail-Authentifizierung
article_title: E-Mail-Authentifizierung
page_order: 2
page_type: reference
description: "Dieser Referenzartikel behandelt die E-Mail-Authentifizierung, eine Sammlung von Techniken, die darauf abzielen, Ihre E-Mails mit überprüfbaren Informationen über ihre Herkunft auszustatten."
channel: email

---

# E-Mail-Authentifizierung

> Die E-Mail-Authentifizierung ist eine Sammlung von Techniken, die Ihre E-Mails mit überprüfbaren Informationen über ihre Herkunft ausstatten.<br><br>Eine ordnungsgemäße Authentifizierung ist entscheidend dafür, dass Internet Service Provider (ISPs) Sie als Absender erwünschter E-Mails erkennen und Ihre Post sofort zustellen können. Ohne Authentifizierung werden Ihre Nachrichten als Betrugsversuche eingestuft. 

## Methoden der Authentifizierung

### Sender Policy Framework (SPF)

Diese Methode bestätigt, dass die IP-Adresse, von der aus Braze E-Mails versendet, berechtigt ist, in Ihrem Namen E-Mails zu versenden. SPF ist Ihre Basisauthentifizierung und wird durch die Veröffentlichung der Texteinträge in den DNS-Einstellungen erreicht. Der empfangende Server überprüft die DNS-Einträge und stellt fest, ob sie authentisch sind. Diese Methode dient dazu, den E-Mail-Absender zu überprüfen.

Ihr SPF-Eintrag wird eingerichtet, wenn Braze Ihre IPs und Domains konfiguriert - abgesehen vom Hinzufügen der DNS-Einträge, die wir Ihnen zur Verfügung stellen, ist keine weitere Aktion erforderlich.

### Domain Keys Identified Mail (DKIM)

Diese Methode bestätigt, dass Ihre Braze-Domain berechtigt ist, E-Mails in Ihrem Namen zu versenden. Diese Methode dient dazu, die Authentizität des Absenders und die Integrität der Nachricht zu überprüfen. Außerdem werden individuelle kryptografische digitale Signaturen verwendet, damit ISPs sicher sein können, dass die von ihnen zugestellte E-Mail mit der von Ihnen gesendeten E-Mail übereinstimmt.

Braze signiert die E-Mail mit Ihrem geheimen privaten Schlüssel. Die ISP überprüfen die Signatur anhand des öffentlichen Schlüssels in Ihrem benutzerdefinierten DNS-Eintrag. Keine zwei Signaturen sind exakt gleich, und nur mit Ihrem öffentlichen Schlüssel kann die Signatur des privaten Schlüssels verifiziert werden.

Ihr DKIM-Eintrag wird eingerichtet, wenn Braze Ihre IPs und Domains konfiguriert - abgesehen vom Hinzufügen der DNS-Einträge, die wir Ihnen zur Verfügung stellen, sind keine weiteren Maßnahmen erforderlich.

### Domänenbasierte Nachrichtenauthentifizierung, Berichterstattung und Konformität (DMARC)

[Domain-based Message Authentication, Reporting & Conformance (DMARC)](https://dmarc.org/) ist ein E-Mail-Authentifizierungsprotokoll, mit dem Absender die Legitimität ihrer Nachrichten nachweisen können, was das Vertrauen der Mailbox-Empfänger stärkt und die Annahme von Nachrichten fördert. Mit DMARC können E-Mail-Absender festlegen, wie mit E-Mails verfahren werden soll, die nicht per Sender Policy Framework (SPF) oder Domain Keys Identified Mail (DKIM) authentifiziert worden sind. Dabei wird überprüft, ob sowohl die SPF- als auch die DKIM-Prüfung bestanden worden sind. 

Absender können Postfachanbieter anweisen, wie sie mit E-Mails verfahren sollen, die ihre Signatur- oder Authentifizierungsprüfung nicht bestanden haben. Fehlversuche können darauf hindeuten, dass Dritte versuchen, Sie oder Ihre E-Mail zu imitieren. Absender können Mailbox-Anbieter anweisen, Mails abzulehnen oder in Quarantäne zu stellen, und sogar automatische Berichte über Mails senden, die nicht geprüft wurden. Auf diese Weise können Mailbox-Anbieter Spammer besser identifizieren und verhindern, dass böswillige E-Mails in die Postfächer eindringen. Gleichzeitig werden falsch-positive Ergebnisse minimiert und bessere Authentifizierungsberichte für mehr Transparenz auf dem Markt bereitgestellt.

#### Funktionsweise

Für DMARC müssen Sie einen DMARC-Eintrag in Ihrem Domain Naming System (DNS) veröffentlichen. Dies ist ein TXT-Eintrag, der die Richtlinien Ihrer E-Mail-Domäne nach Überprüfung des SPF- und DKIM-Status öffentlich zum Ausdruck bringt. DMARC überprüft, ob SPF, DKIM oder beide erfolgreich waren. Dies wird als DMARC-Abgleich bezeichnet.

Ein DMARC-Eintrag weist E-Mail-Server außerdem an, XML-Berichte an die im DMARC-Datensatz angegebene E-Mail-Adresse zurückzuschicken. Die Berichte geben Aufschluss darüber, wie sich Ihre E-Mails durch das System bewegen und ermöglichen die Erkennung von Versuchen, Ihre E-Mail-Domain für den Versand von E-Mails zu nutzen.

Die Richtlinie in Ihrem DMARC-Eintrag teilt dem teilnehmenden E-Mail-Empfängerserver mit, wie mit E-Mails verfahren werden soll, die SPF und DKIM nicht bestehen, aber behaupten, von Ihrer Domain zu stammen. Braze empfiehlt, eine DMARC-Richtlinie für die Root-Domain festzulegen, die dann auf alle Subdomains angewendet wird. Das bedeutet, dass für alle aktuellen und neuen Subdomains in Zukunft keine zusätzliche Einrichtung erforderlich ist. Es gibt drei Arten von Richtlinien, die Sie festlegen können:

| Richtlinie | Impact |
| --- | --- |
| Keine | Weisen Sie den Postfachanbieter an, bei fehlgeschlagenen Nachrichten nichts zu unternehmen. |
| Quarantäne | Weisen Sie den Postfachanbieter an, fehlgeschlagene Nachrichten an den Spam-Ordner zu senden. |
| Ablehnen | Sagen Sie dem Mailbox-Anbieter, dass Nachrichten, die fehlschlagen, im Spam-Ordner landen und blockiert werden sollten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Wie Sie die DMARC-Authentifizierung Ihrer Domain überprüfen

Es gibt zwei Möglichkeiten, die DMARC-Authentifizierung Ihrer Domain zu überprüfen:

- **Möglichkeit 1:** Sie können Ihre übergeordnete Domain oder Subdomain in ein DMARC-Prüfprogramm eines Drittanbieters, wie z.B. [MXToolbox](https://mxtoolbox.com/dmarc.aspx), eingeben, um zu überprüfen, ob Sie eine DMARC-Richtlinie eingeführt haben und wie diese Richtlinie eingestellt ist.
    - **MXToolbox**: Wenn Sie Ihr DMARC als Root-Domain eingestellt haben, geben Sie diese in MXToolbox ein. Wenn Sie DMARC auf der Subdomain eingestellt haben, geben Sie die Subdomain in MXToolbox ein. Beachten Sie, dass MXToolbox bei Suchvorgängen weder nach oben noch nach unten schaut. Wenn Sie DMARC auf der Root-Domain einstellen und die Subdomain eingeben, zeigt MXToolbox daher einen Fehler an, da es nicht weiß, dass DMARC auf der Root-Domain eingestellt wurde.
- **Option 2:** Öffnen Sie eine E-Mail von Ihrer Domain oder Subdomain in Ihrem Postfach und suchen Sie die ursprüngliche Nachricht, um herauszufinden, ob DMARC deren Authentifizierung durchlässt.

Wenn Sie zum Beispiel Google Mail verwenden, gehen Sie folgendermaßen vor:

1. Klicken Sie in einer E-Mail-Nachricht auf die Schaltfläche **Mehr** <i class="fa-solid fa-ellipsis"></i>.
2. Wählen Sie **Original anzeigen**.
3. Prüfen Sie, ob der **DMARC**-Status auf "PASS" lautet.

![Eine E-Mail, die den DMARC-Wert "PASS" enthält.]({% image_buster /assets/img_archive/dmarc_example.png %})

