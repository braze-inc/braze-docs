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
{% tab Datenerfassung - Übermittlung von Formularen %}

Wenn ein Nutzer:innen ein anpassbares Datenerfassungsformular in Komo abschickt, werden die in der Braze Integration abgebildeten Komo-Felder über den `/users/track/` API-Aufruf an Braze übergeben.

Datenerfassungsformulare gibt es entweder am Anfang oder am Ende von Karten.

{% endtab %}
{% tab Marktforschung - Demnächst %}

In Kürze wird Komo die Möglichkeit bieten, Marktforschungsdaten weiterzuleiten, die erfasst werden, wenn ein Nutzer eine Quizfrage, eine Umfrage, einen Persönlichkeitstest, einen Swiper usw. beantwortet. Diese Daten ermöglichen es Ihnen, das Profil eines Nutzers:innen über die in Formularen erfassten Daten hinaus zu erweitern.

{% endtab %}
{% endtabs %}

## Integration

### Schritt 1: Veröffentlichen Sie einen Komo Engagement Hub und eine Karte

Sie müssen einen Komo Engagement Hub mit mindestens einer Karte veröffentlichen, die ein Formular zur Datenerfassung enthält. Nach der Veröffentlichung können Sie die Nutzer:innen End-to-End testen und überprüfen, ob die Integration korrekt funktioniert.

![]({% image_buster /assets/img/komo/komo_hub_publish.png %})

### Schritt 2: Fügen Sie die Integration von Braze hinzu

Gehen Sie in Komo auf den Tab **Hub-Einstellungen** und wählen Sie den Bereich **Integrationen** aus. Suchen Sie dann die Braze Integration in der Liste und wählen Sie den Button **Verbinden**, um die Integration zu aktivieren.

![]({% image_buster /assets/img/komo/komo_hub_settings_integrations.png %})

![]({% image_buster /assets/img/komo/komo_hub_settings_braze_connect.png %})

#### Konfigurieren Sie die Abbildung der Nutzer:innen

Als erstes müssen Sie konfigurieren, wie Sie die in Komo erfassten Nutzer:innen den Nutzern in Braze zuordnen. Wenn Sie die `braze_id` oder `external_id` über ein Feld innerhalb von Komo erfassen, können Sie den entsprechenden Schlüssel auswählen; andernfalls wählen Sie als häufigste Option einen Nutzer:innen-Alias von E-Mail oder Telefon.

![]({% image_buster /assets/img/komo/komo_hub_settings_braze_key.png %}){: style="max-width:65%;"}

Als nächstes müssen Sie eine Abbildung der Komo-Felder definieren, die Sie in Braze-Attribute übertragen möchten. Komo erfasst eine große Menge an Daten, so dass nur die Felder, die in der Braze Integration abgebildet sind, an Braze gesendet werden.

![]({% image_buster /assets/img/komo/komo_hub_settings_braze_settings.png %}){: style="max-width:65%;"}

Fügen Sie schließlich Ihren API-Schlüssel und die URL des REST-Endpunkts hinzu und klicken Sie auf **Speichern**, um die Integration zu aktivieren.

## Verwendung der Integration

Sobald Ihre Integration abgeschlossen ist, können Sie die an Braze gesendeten Komo-Daten verwenden, um Segmente für das Targeting zu erstellen.


