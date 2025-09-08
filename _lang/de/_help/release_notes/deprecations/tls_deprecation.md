---
nav_title: TLS 1.0 &amp; 1.1 Ausmusterung
page_order: 2

page_type: update
description: "Dieser Artikel beschreibt die Abschaffung von TLS 1.0 und TLS 1.1 durch Braze, die im Mai 2018 abgeschlossen wurde."
---
# TLS 1.0 & 1.1 veraltet

{% alert update %}
Braze hat die Unterstützung für Transport Layer Security (TLS) Chiffren sowohl in TLS 1.0 als auch in 1.1 entfernt, in Übereinstimmung mit den Empfehlungen des PCI Security Standards Council. Wir haben diese Abschaffung der Unterstützung in zwei Phasen durchgeführt, die im Mai 2018 abgeschlossen wurden.
{% endalert %} 

## Hintergrund

Braze veraltet bekannte schwache Chiffren der Transport Layer Security (TLS) sowohl in TLS 1.0 als auch in 1.1 gemäß den Empfehlungen des PCI Security Standards Council in zwei Phasen, die im Mai 2018 abgeschlossen wurden.

Diese Änderung erfolgt nicht als Reaktion auf einen Verstoß oder ein Problem im Zusammenhang mit der Plattform von Braze, sondern als Vorsichtsmaßnahme, um unsere erstklassigen Sicherheits- und Datenstandards aufrechtzuerhalten und unsere Kunden und deren Kunden proaktiv zu schützen.

In den letzten Jahren gab es eine Reihe von systematischen Sicherheitsproblemen im Zusammenhang mit TLS und seinem Vorgänger Secure Sockets Layer (SSL), darunter [POODLE](https://www.us-cert.gov/ncas/alerts/TA14-290A), [Heartbleed](https://en.wikipedia.org/wiki/Heartbleed), [LOGJAM](https://en.wikipedia.org/wiki/Logjam_(computer_security)) und andere, die den verschlüsselten Internetverkehr bedrohten und Teile des Internets Sicherheitslücken aussetzten. Zusammen mit anderen Technologieunternehmen hat Braze bereits früher Maßnahmen ergriffen, um schwache Verschlüsselungsprotokolle und Chiffren zu deaktivieren, wenn Angriffe entdeckt werden. So wurde beispielsweise die Unterstützung für SSLv3 im Jahr 2014 eingestellt.

Vor kurzem hat der PCI Security Standards Council im April 2015 einen Leitfaden zur Verschlüsselung für den [Payment Card Industry Data Security Standard](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard) (PCI-DSS) veröffentlicht. Der Leitfaden schließt SSL 3.0, TLS 1.0 und einige der von TLS 1.1 unterstützten Chiffre-Suiten von der Protokollliste starker kryptographischer Chiffren aus und ermutigt Unternehmen, die Unterstützung für diese Protokolle oder Chiffren einzustellen, um die Sicherheit der Nutzer:innen zu gewährleisten.

Eine Chiffre Suite ist eine Kombination von Algorithmen, die bei der Aushandlung einer sicheren SSL- oder TLS-Verbindung für Verschlüsselung, Authentifizierung und Kommunikationsintegrität sorgen. Wenn entdeckt wird, dass eine bestimmte Chiffre geknackt werden kann - unabhängig davon, ob es bereits bekannte Angriffe gibt oder nicht -, wird die Chiffre als "Schwachstelle" betrachtet, die zukünftige Angriffe ermöglichen könnte. Durch den Ausschluss dieser TLS Chiffren von den PCI DSS Compliance-Anforderungen verlangt der PCI DSS Council von Dienstleistern, dass sie nur die besten Verschlüsselungsstandards unterstützen. Der PCI DSS Council hat eine Frist bis zum 30\. Juni 2018 für die Einhaltung der Verschlüsselungsanforderung gesetzt, um die Unterstützung für TLS 1.0 und TLS 1.1 einzustellen.

## Der Abschreibungsplan von Braze
Um die Empfehlungen des PCI DSS Council zu erfüllen, wird Braze die Mindestversionen von TLS, die wir in unseren Diensten unterstützen, anheben. Um Ihnen eine bessere Idee von unserem Compliance-Plan und seinen potenziellen Auswirkungen auf Ihre Marke und Ihre Nutzer:innen zu geben, sollten Sie sich über die zwei Hauptphasen unseres Plans im Klaren sein:

### Phase 1: Oktober 1, 2017

Braze wird die Möglichkeit, die folgenden Chiffren zu verwenden, aus dem Internet-Dashboard und den REST APIs von Braze entfernen:

- `TLS_RSA_WITH_AES_256_CBC_SHA`
- `TLS_RSA_WITH_AES_128_CBC_SHA`
- `TLS_RSA_WITH_AES_256_CBC_SHA256`
- `TLS_RSA_WITH_AES_256_GCM_SHA384`
- `TLS_RSA_WITH_AES_128_CBC_SHA256`
- `TLS_RSA_WITH_AES_128_GCM_SHA256`
- `TLS_RSA_WITH_3DES_EDE_CBC_SHA`

Diese Änderung sollte keine Auswirkungen auf Kund:innen haben, die auf das Braze-Dashboard zugreifen, da alle modernen Webbrowser sicherere Chiffren unterstützen. Sollte jedoch nach dem 1\. Oktober beim Zugriff auf das Internet Dashboard ein Fehler bei der SSL-Verschlüsselung auftreten, können Sie das Problem beheben, indem Sie einfach ein Upgrade auf die neueste Version Ihres Webbrowsers vornehmen.

Ihr Entwicklerteam sollte sicherstellen, dass es keine dieser Chiffren für die Server-zu-Server-Kommunikation mit den REST APIs von Braze verwendet. Wenn ja, müssen sie ihren Code vor dem 1\. Oktober auf sicherere Chiffren aktualisieren, um die APIs von Braze weiterhin nutzen zu können. Um jedoch die Unterstützung für alte und veraltete mobile Geräte, die möglicherweise schwache Chiffren verwenden, aufrechtzuerhalten, wird Braze diese Chiffren auf den APIS, die Daten von unseren SDKs erhalten haben, weiterhin unterstützen.

### Phase 2: Mai 31, 2018

Braze wird die Unterstützung für TLS 1.0 und TLS 1.1 in allen Braze Diensten am 31\. Mai 2018 abschalten - einschließlich des Braze-Dashboards, der REST APIs und der APIs, die mit unseren SDKs kommunizieren. Wir werden auch die Unterstützung für die im vorangegangenen Abschnitt aufgeführten Chiffren in Verbindung mit den APIs, die SDK-Daten empfangen, entfernen. Das bedeutet, dass alle TLS 1.0- und 1.1-Kommunikation von und zu Braze ab diesem Datum von unserem Netzwerk nicht mehr unterstützt wird.

Infolge dieser Änderung können einige alte oder veraltete mobile Geräte - wahrscheinlich solche, auf denen frühe Versionen von Android laufen - möglicherweise nicht mehr mit Braze kommunizieren, so dass sie keine Daten mehr an Braze senden oder In-App-Nachrichten von Braze empfangen können. Wir gehen jedoch davon aus, dass die Änderung nur eine kleine Anzahl von Geräten betreffen wird. Alle betroffenen Geräte verlieren einen Monat später, am 30\. Juni 2018, die Möglichkeit, mit einer PCI-konformen Website oder einem Dienst zu kommunizieren. Dies ist das vom PCI DSS Council festgelegte Datum für die Entfernung der Chiffren TLS 1.0 und TLS 1.1.

## Aktionsplan
Wenn Ihre Marke die REST APIs von Braze nutzt, sprechen Sie mit Ihrem Entwicklerteam, um sicherzustellen, dass alle Server-zu-Server-Aufrufe an Braze TLS 1.2 verwenden, um eine Unterbrechung des Dienstes zu vermeiden. Beachten Sie, dass einige Programmiersprachen - wie z.B. Java 7 - standardmäßig ältere Versionen von TLS verwenden, so dass Ihr Entwicklerteam möglicherweise einige Änderungen am Code vornehmen muss, um die upgegradeten Verschlüsselungsanforderungen zu unterstützen.

Apple Geräte werden von der geplanten Abschaffung von Braze nicht betroffen sein, da Apple seit Ende 2016 TLS 1.2 verlangt. Dasselbe gilt für moderne Webbrowser, so dass wir nicht davon ausgehen, dass diese Änderungen Auswirkungen auf die Nutzung des Internet SDK haben werden. Android-Geräte mit Android 4.4 (KitKat) oder niedriger verwenden jedoch möglicherweise nicht standardmäßig TLS 1.2\. Upgraden Sie daher alle Ihre Android-Integrationen bis zum 31\. Mai 2018 mindestens auf die Version 2.0.3 des Braze SDK (das standardmäßig TLS 1.2 verwendet, wenn ein bestimmtes Gerät dies unterstützen kann).

Aufgrund der bekannten Schwachstellen in TLS 1.0 und der Chiffre-Suite TLS 1.1 ist es möglich, dass es in Zukunft zu Angriffen kommt, die es erforderlich machen, dass Braze seinen Plan zur Abschaffung der Chiffre beschleunigt, um die Sicherheit aller unserer Kund:innen zu gewährleisten. Braze wird den Stand der Sicherheit und alle relevanten Angriffe im Zusammenhang mit den Protokollen TLS 1.0 und 1.1 überwachen und Sie auf dem Laufenden halten, wenn wir von Angriffen erfahren, die den in den vorangegangenen Abschnitten dargelegten Zeitplan verändern. Aufgrund dieser möglichen Auswirkungen empfehlen wir Ihnen jedoch dringend, mit Ihrem Entwicklerteam zusammenzuarbeiten, um sicherzustellen, dass Ihre API-Aufrufe an Braze mit TLS 1.2 gesichert sind, und dass Sie in den kommenden Monaten ein Upgrade auf das neueste Android SDK planen.


