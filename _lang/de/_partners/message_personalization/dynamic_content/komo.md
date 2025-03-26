---
nav_title: Komo
article_title: Komo
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Komo, einer Plattform zur Kundenbindung, die sich auf Gamification, interaktive Inhalte, Wettbewerbe, Preise und Loyalität spezialisiert hat. Durch diese Integration können die in Komo erfassten First- und Zero-Party-Daten in Braze veröffentlicht werden."
alias: /partners/komo/
page_type: partner
search_tag: Partner

---

# Komo

> [Komo][7] ist eine Plattform zur Kundenbindung, die sich auf Gamification, interaktive Inhalte, Wettbewerbe, Prämien und Loyalität spezialisiert hat.

Die Integration von Braze und Komo ermöglicht es Ihnen, First- und Zero-Party-Daten über Komo Engagement Hubs zu sammeln. Diese Hubs sind dynamische Microsites, die interaktive Inhalte und Spielfunktionen bieten. Die von diesen Hubs gesammelten Benutzerdaten werden dann an die Braze API übertragen.

- Ingest von First- und Zero-Party-Benutzerdaten, die von Komo gesammelt wurden, zu Braze in Echtzeit
- Erfassen Sie Marktforschungs- und Benutzerpräferenzdaten, wenn sie Umfragen, Abstimmungen und Quizfragen beantworten.
- Erstellen Sie im Laufe der Zeit Benutzerprofile in Braze, wenn der Benutzer sich weiter engagiert und mehr Daten über sich selbst mitteilt.
- Standardisieren Sie das Erscheinungsbild von Transaktions-E-Mails, die über Braze versendet werden.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Komo-Konto | Sie benötigen ein aktives Komo-Konto, um die Vorteile dieser Partnerschaft zu nutzen. Besuchen Sie [Komo][7], um jetzt eine Testversion zu starten. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre REST-Endpunkt-URL][1]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab.<br><br>Es sollte zum Beispiel so aussehen: https://rest.iad-03.braze.com |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Anwendungsfälle

{% tabs local %}
{% tab Datenerfassung - Übermittlung von Formularen %}

Wenn ein Benutzer ein anpassbares Datenerfassungsformular in Komo abschickt, werden die Komo-Felder, die in der Braze-Integration zugeordnet sind, über den `/users/track/` API-Aufruf an Braze übergeben.

Datenerfassungsformulare gibt es entweder am Anfang oder am Ende von Cards.

{% endtab %}
{% tab Marktforschung - Demnächst erhältlich %}

In Kürze wird Komo die Möglichkeit bieten, Marktforschungsdaten weiterzuleiten, die erfasst werden, wenn ein Benutzer eine Quizfrage, eine Umfrage, einen Persönlichkeitstest, einen Swiper usw. beantwortet. Diese Daten ermöglichen es Ihnen, das Profil eines Benutzers über die in Formularen erfassten Daten hinaus zu erweitern.

{% endtab %}
{% endtabs %}

## Integration

### Schritt 1: Veröffentlichen Sie einen Komo Engagement Hub und eine Karte

Sie müssen einen Komo Engagement Hub mit mindestens einer Karte veröffentlichen, die ein Datenerfassungsformular enthält. Nach der Veröffentlichung können Sie die Benutzerfreundlichkeit von Anfang bis Ende testen und überprüfen, ob die Integration korrekt funktioniert.

![][2]

### Schritt 2: Fügen Sie die Braze-Integration hinzu

Gehen Sie in Komo auf die Registerkarte **Hub-Einstellungen** und wählen Sie den Abschnitt **Integrationen**. Suchen Sie dann die Braze-Integration in der Liste und klicken Sie auf die Schaltfläche **Verbinden**, um die Integration zu aktivieren.

![][3]

![][4]

#### Konfigurieren Sie die Benutzerzuordnung

Als erstes müssen Sie konfigurieren, wie Sie die in Komo erfassten Benutzer den Benutzern in Braze zuordnen wollen. Wenn Sie `braze_id` oder `external_id` über ein Feld innerhalb von Komo erfassen, können Sie den entsprechenden Schlüssel auswählen; andernfalls wählen Sie die häufigste Option ist ein Benutzeralias von E-Mail oder Telefon.

![][5]{: style="max-width:65%;"}

Als nächstes müssen Sie eine Zuordnung der Komo-Felder definieren, die Sie in Braze-Attribute übertragen möchten. Komo erfasst eine große Menge an Daten, so dass nur die Felder, die in der Braze-Integration zugeordnet sind, an Braze gesendet werden.

![][6]{: style="max-width:65%;"}

Fügen Sie schließlich Ihren API-Schlüssel und die URL des REST-Endpunkts hinzu und klicken Sie auf **Speichern**, um die Integration zu aktivieren.

## Verwendung der Integration

Sobald Ihre Integration abgeschlossen ist, können Sie die an Braze gesendeten Komo-Daten verwenden, um Segmente für das Targeting zu erstellen.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/komo/komo_hub_publish.png %}
[3]: {% image_buster /assets/img/komo/komo_hub_settings_integrations.png %}
[4]: {% image_buster /assets/img/komo/komo_hub_settings_braze_connect.png %}
[5]: {% image_buster /assets/img/komo/komo_hub_settings_braze_key.png %}
[6]: {% image_buster /assets/img/komo/komo_hub_settings_braze_settings.png %}
[7]: https://komo.tech/