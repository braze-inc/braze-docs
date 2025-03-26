---
nav_title: TLS 1.0 &amp; 1.1 Ausmusterung
page_order: 2

page_type: update
description: "Dieser Artikel beschreibt die Abschaffung von TLS 1.0 und TLS 1.1 durch Braze, die im Mai 2018 abgeschlossen wurde."
---
# Ablehnung von TLS 1.0 & 1.1

{% alert update %}
Braze hat die Unterstützung für Transport Layer Security (TLS)-Chiffren sowohl in TLS 1.0 als auch in 1.1 entfernt, in Übereinstimmung mit den Empfehlungen des PCI Security Standards Council. Wir haben diese Abschaffung der Unterstützung in zwei Phasen durchgeführt, die im Mai 2018 abgeschlossen wurden.
{% endalert %} 

## Hintergrund

Braze veraltet bekannte schwache Transport Layer Security (TLS)-Chiffren sowohl in TLS 1.0 als auch in 1.1, entsprechend den Empfehlungen des PCI Security Standards Council in zwei Phasen, die im Mai 2018 abgeschlossen werden.

Diese Änderung erfolgt nicht als Reaktion auf einen Verstoß oder ein Problem im Zusammenhang mit der Plattform von Braze, sondern als Vorsichtsmaßnahme, um unsere erstklassigen Sicherheits- und Datenstandards aufrechtzuerhalten und unsere Kunden und deren Kunden proaktiv zu schützen.

In den letzten Jahren gab es eine Reihe von systematischen Sicherheitsproblemen im Zusammenhang mit TLS und seinem Vorgänger Secure Sockets Layer (SSL), darunter [POODLE][1], [Heartbleed][2], [LOGJAM][3] und andere, die den verschlüsselten Webverkehr bedrohten und Teile des Internets für Sicherheitsverletzungen anfällig machten. Zusammen mit anderen Technologieunternehmen hat Braze bereits Maßnahmen ergriffen, um schwache Verschlüsselungsprotokolle und -chiffren zu deaktivieren, sobald Angriffe entdeckt werden. So wurde beispielsweise die Unterstützung für SSLv3 im Jahr 2014 eingestellt.

Vor kurzem hat der PCI Security Standards Council im April 2015 eine Anleitung zur Verschlüsselung für den [Payment Card Industry Data Security Standard][4] (PCI-DSS) veröffentlicht. Der Leitfaden schließt SSL 3.0, TLS 1.0 und einige der von TLS 1.1 unterstützten Chiffriersuiten von der Protokollliste starker kryptographischer Chiffren aus und ermutigt Unternehmen, die Unterstützung für diese Protokolle oder Chiffren einzustellen, um die Sicherheit der Internetnutzer zu gewährleisten.

Eine Cipher Suite ist eine Kombination von Algorithmen, die bei der Aushandlung einer sicheren SSL- oder TLS-Verbindung für Verschlüsselung, Authentifizierung und Kommunikationsintegrität sorgen. Wenn entdeckt wird, dass eine bestimmte Chiffre geknackt werden kann - unabhängig davon, ob es derzeit bekannte Angriffe gibt oder nicht -, wird die Chiffre als "Schwachstelle" betrachtet, die zukünftige Angriffe ermöglichen könnte. Durch den Ausschluss dieser TLS-Verschlüsselungen von den PCI DSS-Compliance-Anforderungen verlangt der PCI DSS Council von den Dienstanbietern, dass sie nur die besten Verschlüsselungsstandards der Branche unterstützen. Der PCI DSS Council hat eine Frist bis zum 30\. Juni 2018 für die Einhaltung der Verschlüsselungsanforderung gesetzt, um die Unterstützung für TLS 1.0 und TLS 1.1 einzustellen.

## Braze's Abschreibungsplan
Um die Empfehlungen des PCI DSS Council zu erfüllen, wird Braze die Mindestversionen von TLS, die wir in unseren Services unterstützen, anheben. Damit Sie sich ein besseres Bild von unserem Compliance-Plan und seinen möglichen Auswirkungen auf Ihre Marke und Ihre Nutzer machen können, sollten Sie sich über die zwei Hauptphasen unseres Plans im Klaren sein:

### Phase 1: Oktober 1, 2017

Braze entfernt die Möglichkeit, die folgenden Chiffren aus dem Web-Dashboard und den REST-APIs von Braze zu verwenden:

- `TLS_RSA_WITH_AES_256_CBC_SHA`
- `TLS_RSA_WITH_AES_128_CBC_SHA`
- `TLS_RSA_WITH_AES_256_CBC_SHA256`
- `TLS_RSA_WITH_AES_256_GCM_SHA384`
- `TLS_RSA_WITH_AES_128_CBC_SHA256`
- `TLS_RSA_WITH_AES_128_GCM_SHA256`
- `TLS_RSA_WITH_3DES_EDE_CBC_SHA`

Diese Änderung sollte keine Auswirkungen auf Kunden haben, die auf das Braze Dashboard zugreifen, da alle modernen Webbrowser sicherere Verschlüsselungen unterstützen. Sollte jedoch nach dem 1\. Oktober beim Zugriff auf das Web-Dashboard ein Fehler bei der SSL-Verschlüsselung auftreten, können Sie das Problem beheben, indem Sie einfach auf die neueste Version Ihres Webbrowsers aktualisieren.

Ihr Entwicklungsteam sollte sicherstellen, dass es keine dieser Verschlüsselungen für die Server-zu-Server-Kommunikation mit den REST-APIs von Braze verwendet. Wenn dies der Fall ist, müssen sie ihren Code vor dem 1\. Oktober aktualisieren, um sicherere Verschlüsselungscodes zu verwenden, damit sie die APIs von Braze weiterhin nutzen können. Um jedoch die Unterstützung für alte und veraltete mobile Geräte aufrechtzuerhalten, die möglicherweise schwache Chiffren verwenden, wird Braze diese Chiffren weiterhin auf den APIS unterstützen, die Daten von unseren SDKs erhalten haben.

### Phase 2: Mai 31, 2018

Braze wird am 31\. Mai 2018 die Unterstützung für TLS 1.0 und TLS 1.1 für alle Braze-Dienste deaktivieren - einschließlich des Braze-Dashboards, der REST-APIs und der APIs, die mit unseren SDKs kommunizieren. Wir werden auch die Unterstützung für die im vorangegangenen Abschnitt aufgeführten Chiffren in Verbindung mit den APIs, die SDK-Daten empfangen, entfernen. Das bedeutet, dass alle TLS 1.0- und 1.1-Kommunikation von und zu Braze ab diesem Datum nicht mehr von unserem Netzwerk unterstützt wird.

Infolge dieser Änderung können einige alte oder veraltete mobile Geräte - wahrscheinlich solche, auf denen frühe Versionen von Android laufen - nicht mehr mit Braze kommunizieren, so dass sie keine Daten mehr an Braze senden oder In-App-Nachrichten von Braze empfangen können. Wir gehen jedoch davon aus, dass die Änderung nur eine kleine Anzahl von Geräten betreffen wird. Alle betroffenen Geräte verlieren einen Monat später, am 30\. Juni 2018, die Möglichkeit, mit einer PCI-konformen Website oder einem PCI-konformen Dienst zu kommunizieren. Dies ist das vom PCI DSS Council festgelegte Datum für die Entfernung der TLS 1.0- und TLS 1.1-Verschlüsselungen.

## Aktionsplan
Wenn Ihre Marke die REST-APIs von Braze nutzt, sprechen Sie mit Ihrem technischen Team, um sicherzustellen, dass alle Server-zu-Server-Aufrufe an Braze TLS 1.2 verwenden, um eine Unterbrechung des Dienstes zu vermeiden. Beachten Sie, dass einige Programmiersprachen - wie z.B. Java 7 - standardmäßig ältere Versionen von TLS verwenden, so dass Ihr Entwicklungsteam möglicherweise einige Codeänderungen vornehmen muss, um die verbesserten Verschlüsselungsanforderungen zu unterstützen.

Apple-Geräte werden von der geplanten Abschaffung von Braze nicht betroffen sein, da Apple seit Ende 2016 TLS 1.2 verlangt. Dasselbe gilt für moderne Webbrowser, so dass wir nicht davon ausgehen, dass diese Änderungen Auswirkungen auf die Nutzung des Web SDK haben werden. Android-Geräte mit Android 4.4 (KitKat) oder niedriger verwenden jedoch möglicherweise nicht standardmäßig TLS 1.2\. Aktualisieren Sie daher alle Ihre Android-Integrationen bis zum 31\. Mai 2018 mindestens auf die Version 2.0.3 des Braze SDK (das standardmäßig TLS 1.2 verwendet, wenn ein bestimmtes Gerät es unterstützen kann).

Und schließlich ist es aufgrund der bekannten Schwachstellen in TLS 1.0 und der TLS 1.1 Cipher Suite möglich, dass in Zukunft Angriffe auftreten, die es erforderlich machen, dass Braze unseren Plan zur Abschaffung des Systems beschleunigt, um die Sicherheit aller unserer Kunden zu gewährleisten. Braze wird den Stand der Sicherheit und alle relevanten Angriffe im Zusammenhang mit den Protokollen TLS 1.0 und 1.1 überwachen und Sie auf dem Laufenden halten, wenn wir von Angriffen erfahren, die den in den vorangegangenen Abschnitten dargelegten Zeitplan verändern. Aufgrund dieser potenziellen Auswirkungen empfehlen wir Ihnen jedoch dringend, mit Ihrem technischen Team zusammenzuarbeiten, um sicherzustellen, dass Ihre API-Aufrufe an Braze mit TLS 1.2 gesichert sind, und dass Sie in den kommenden Monaten ein Upgrade auf das neueste Android SDK planen.


[1]: https://www.us-cert.gov/ncas/alerts/TA14-290A
[2]: https://en.wikipedia.org/wiki/Heartbleed
[3]: https://en.wikipedia.org/wiki/Logjam_(computer_security)
[4]: https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard
