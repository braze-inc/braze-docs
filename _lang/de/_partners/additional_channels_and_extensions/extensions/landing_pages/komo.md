---
nav_title: Komo
article_title: Komo
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Komo, einer Customer-Engagement-Plattform, die auf Gamification, interaktive Inhalte, Wettbewerbe, Preise und Loyalität spezialisiert ist. Durch diese Integration können First-Party-Daten und Zero-Party-Daten, die in Komo erfasst wurden, in Braze veröffentlicht werden."
alias: /partners/komo/
page_type: partner
search_tag: Partner

---

# Komo

> [Komo](https://komo.tech/) ist eine Customer-Engagement-Plattform, die sich auf Gamification, interaktive Inhalte, Wettbewerbe, Prämien und Loyalität spezialisiert hat.

_Diese Integration wird von Komo gepflegt._

## Über die Integration

Die Integration von Braze und Komo erlaubt es Ihnen, First-Party-Daten und Zero-Party-Daten über Komo Engagement Hubs zu sammeln. Diese Hubs sind dynamische Microsites, die interaktive Inhalte und Gamification-Features bieten. Die von diesen Knotenpunkten gesammelten Nutzerdaten werden dann an die Braze API übermittelt.

- Datenaufnahme von First-Party-Daten und Zero-Party-Daten von Nutzern:innen aus Komo nach Braze in Realtime
- Datenaufnahme von Marktforschungs- und Nutzer:innen-Daten, wenn sie Umfragen, Abstimmungen und Quizfragen beantworten
- Erstellen Sie im Laufe der Zeit Nutzer:innen-Profile in Braze, wenn die Nutzer:innen sich weiter engagieren und mehr Daten über sich preisgeben.
- Standardisieren Sie das Erscheinungsbild von Transaktions-E-Mails, die über Braze versendet werden.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Komo-Konto | Sie benötigen ein aktives Komo-Konto, um die Vorteile dieser Partnerschaft zu nutzen. Besuchen Sie [Komo](https://komo.tech/), um jetzt eine Testversion zu starten. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab.<br><br>Es sollte zum Beispiel so aussehen: https://rest.iad-03.braze.com |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Anwendungsfälle

{% tabs local %}
{% tab Data Capture - Form Submission %}

Wenn ein Nutzer:innen ein anpassbares Datenerfassungsformular in Komo abschickt, werden die in der Braze Integration abgebildeten Komo-Felder über den `/users/track/` API-Aufruf an Braze übergeben.

Datenerfassungsformulare gibt es entweder am Anfang oder am Ende von Karten.

{% endtab %}
{% tab Market Research - Coming soon %}

Komo ermöglicht auch die Weitergabe von Marktforschungsdaten, die erfasst werden, wenn ein Nutzer eine Quizfrage, eine Umfrage, einen Persönlichkeitstest, einen Swiper und ähnliches beantwortet. Diese Daten ermöglichen es Ihnen, das Profil eines Nutzers:innen über die in Formularen erfassten Daten hinaus zu erweitern.

{% endtab %}
{% endtabs %}

## Integration

### Schritt 1: Veröffentlichen Sie einen Komo Engagement Hub und eine Karte

Sie müssen einen Komo Hub mit mindestens einer Karte veröffentlichen, die ein Datenerfassungsformular enthält. Nach der Veröffentlichung können Sie die Nutzer:innen End-to-End testen und überprüfen, ob die Integration korrekt funktioniert.

![Komo Hub.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step1.png %})

### Schritt 2: Hinzufügen der Braze Connected App 

Gehen Sie in Komo auf den Tab **Unternehmenseinstellungen** und wählen Sie den Abschnitt **Verbundene Apps** aus. 

Suchen Sie dann die Braze Integration in der Liste und wählen Sie den Button **Verbinden**, um die Integration zu aktivieren.

![Connect Braze Integration.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step2a.png %}){: style="max-width:50%;"}

![Verbinden Sie Braze Integration Schritt 2b.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step2b.png %})

#### Konfigurieren Sie die Integration über einen Workflow

Jetzt müssen Sie einen Workflow innerhalb eines Workspace, einer Site oder einer Karte einrichten, um Daten mit Braze zu synchronisieren. 

Ob Sie den Workflow auf den gesamten Workspace, eine Site (die viele Karten enthält) oder eine einzelne Karte anwenden, hängt davon ab, ob Sie den Workflow über viele Karten oder Kampagnen hinweg triggern möchten. 

Nachdem Sie einen Workflow erstellt haben, definieren Sie Ihren Trigger, suchen im Schrittmenü nach Braze und fügen den Schritt "Nutzer:in verfolgen" hinzu. 

![Tracking Nutzer:innen einrichten.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step3a.png %})

Von hier aus konfigurieren Sie die Ereignisse, Attribute und Abos, die Sie von Komo mit Braze synchronisieren möchten. 

![Content-Blöcke Liste.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step3b.png %})

## Verwendung der Integration

Jetzt ist Ihre Integration betriebsbereit, und Sie können jeden Lauf auf dem Tab Workflow-Läufe überwachen. 
