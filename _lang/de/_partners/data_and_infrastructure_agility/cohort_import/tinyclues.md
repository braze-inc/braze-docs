---
nav_title: Tinyclues
article_title: Tinyclues
alias: /partners/tinyclues/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Tinyclues, die eine Funktion zum Aufbau von Zielgruppen bietet, mit der Sie mithilfe einer unglaublich benutzerfreundlichen Benutzeroberfläche zielgerichtetere Kampagnen versenden, neue Produktmöglichkeiten finden und Ihren Umsatz steigern können."
page_type: partner
search_tag: Partner

---

# Tinyclues

> [Tinyclues](https://www.tinyclues.com/) ist eine Funktion zum Aufbau von Zielgruppen, die es ermöglicht, die Anzahl der Kampagnen und den Umsatz zu erhöhen, ohne die Kundenerfahrung zu beeinträchtigen. Außerdem können Sie die Leistung von CRM-Kampagnen sowohl online als auch offline verfolgen.

Die Integration von Braze und Tinyclues bietet Anwendern einen Weg zu einer besseren CRM-Planung und -Strategie und ermöglicht es ihnen, mithilfe einer unglaublich benutzerfreundlichen Benutzeroberfläche gezieltere Kampagnen zu versenden, neue Produktmöglichkeiten zu finden und den Umsatz zu steigern.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Tinyclues Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Tinyclues Konto. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration von Datenimporten

Um Braze und Tinyclues zu integrieren, müssen Sie die Tinyclues-Plattform konfigurieren, eine bestehende Tinyclues-Kampagne exportieren und ein Nutzerkohortensegment in Braze erstellen, das für die Ausrichtung von Nutzern in zukünftigen Kampagnen verwendet werden kann.

### Schritt 1: Holen Sie sich den Braze-Datenimportschlüssel

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Tinyclues**. 

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Technologiepartner** unter **Integrationen**.
{% endalert %}

Hier finden Sie Ihren REST-Endpunkt und generieren Ihren Braze-Datenimportschlüssel. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen.<br><br>![][6]{: style="max-width:90%;"} 

Um die Integration abzuschließen, müssen Sie den Datenimportschlüssel und den REST-Endpunkt an Ihr Tinyclues Data Operations Team weitergeben. Tinyclues stellt dann die Verbindung her und meldet sich bei Ihnen, sobald die Einrichtung abgeschlossen ist.

### Schritt 2: Exportieren Sie eine Kampagne aus der Tinyclues Plattform

Jedes Mal, wenn Sie eine Kohorte von Tinyclues-Benutzern zur Verwendung in Braze erstellen möchten, müssen Sie diese zunächst aus der Tinyclues-Plattform exportieren.

Wählen Sie in Tinyclues die Kampagne(n), die Sie exportieren möchten, und klicken Sie auf **Kampagnen exportieren**. Beim Export wird die Audience automatisch in Ihr Braze-Konto hochgeladen.

![][1]

### Schritt 3: Erstellen Sie ein Segment aus der benutzerdefinierten Zielgruppe von Tinyclues

Navigieren Sie in Braze zu **Segmente**, benennen Sie Ihr Tinyclues-Kohortensegment und wählen Sie **Tinyclues-Kohorten** als Ihren Filter. Von hier aus können Sie wählen, welche Tinyclues Kohorte Sie einbeziehen möchten. Nachdem Ihr Tinyclues Kohortensegment erstellt wurde, können Sie es bei der Erstellung einer Kampagne oder eines Canvas als Zielgruppenfilter auswählen.

![][3]{: style="max-width:90%;"}<br><br>
![Im Braze Segment Builder ist der Benutzerattributfilter "Tinyclues cohort" auf "includes" und "Primary cohort" eingestellt.][4]{: style="max-width:90%;"}

Haben Sie Probleme, Ihre Kohorte zu finden? In unserem Abschnitt [zur Fehlerbehebung](#troubleshooting) finden Sie eine Anleitung. 

## Mit dieser Integration

Um Ihr Tinyclues-Segment zu verwenden, erstellen Sie eine Braze-Kampagne oder ein Canvas und wählen das Segment als Ihre Zielgruppe aus. 

![In der Braze-Kampagnenerstellung im Schritt "Targeting" ist der Filter "Zielbenutzer nach Segment" auf "Tinyclues-Kohorte" eingestellt.][5]{: style="max-width:90%;"}

## Benutzerabgleich

Identifizierte Benutzer können entweder über ihre `external_id` oder `alias` abgeglichen werden. Anonyme Benutzer können über ihre `device_id` abgeglichen werden. Identifizierte Benutzer, die ursprünglich als anonyme Benutzer angelegt wurden, können nicht über ihre `device_id` identifiziert werden, sondern müssen über ihre `external_id` oder `alias` identifiziert werden.

## Fehlersuche

Haben Sie Probleme, die richtige Kohorte in der Liste zu finden? Sehen Sie sich in Tinyclues die Details Ihrer Kampagne an und überprüfen Sie den Namen, indem Sie die Option **Dateiname exportieren** markieren.

![Unten auf der Seite mit den Kampagnendetails wird der Name Ihrer Kohorte angezeigt.][2]{: style="max-width:30%;"}

Haben Sie immer noch Probleme, Ihr Publikum zu finden? Kontaktieren Sie das [Tinyclues Team](mailto:support@tinyclues.com) für zusätzliche Unterstützung.

[1]: {% image_buster /assets/img/tinyclues/tinyclues_1.png %}
[2]: {% image_buster /assets/img/tinyclues/tinyclues_2.png %}
[3]: {% image_buster /assets/img/tinyclues/tinyclues_3.png %}
[4]: {% image_buster /assets/img/tinyclues/tinyclues_4.png %}
[5]: {% image_buster /assets/img/tinyclues/tinyclues_5.png %}  
[6]: {% image_buster /assets/img/tinyclues/tinyclues_6.png %}  