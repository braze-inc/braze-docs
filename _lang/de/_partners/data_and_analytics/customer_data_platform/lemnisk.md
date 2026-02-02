---
nav_title: Lemnisk
article_title: Integration von Lemnisk mit Braze
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Lemnisk, einer KI-fähigen, auf einer Kundendatenplattform basierenden Plattform für Marketing-Automatisierung, die es Ihnen erlaubt, die von Lemnisk gesammelten Daten aus verschiedenen Quellen in Braze zu streamen, um sie mit den Tools von Braze über verschiedene Kanäle und Ziele hinweg zu aktivieren."
alias: /partners/lemnisk/
page_type: partner
search_tag: Partner

---

# Lemnisk

> [Lemnisk](https://www.lemnisk.co/) ist eine KI-gestützte Customer Data Platform (CDP) und Marketing-Automatisierungslösung, die die Erfassung, Vereinheitlichung und Aktivierung von Kundendaten aus verschiedenen, isolierten Quellen in Echtzeit ermöglicht. Sie stellt diese vereinheitlichten Daten nahtlos über verschiedene MarTech- und Geschäftsplattformen hinweg bereit und bietet gleichzeitig robuste Echtzeit-Analysen, um jede Phase des Kundenlebenszyklus zu verfolgen. 

_Diese Integration wird von Lemnisk gepflegt._

## Über die Integration

Die Integration von Lemnisk und Braze ermöglicht es Marken und Unternehmen, das volle Potenzial von Braze auszuschöpfen, indem sie als CDP-geführte Intelligenzschicht fungiert, die Nutzerdaten plattformübergreifend in Realtime zusammenführt und die gesammelten Nutzer:innen-Informationen und Verhaltensdaten in Echtzeit an Braze sendet. Lemnisk liefert angereicherte Kundenprofile direkt in Braze, indem es Verhaltenssignale und persönliche Attribute zusammenführt, mit denen Sie Ihr Messaging mit tieferem Kontext anpassen können.

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| Lemnisker Konten | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Lemnisk-Konto](https://www.lemnisk.co/). |
| Externe API in Lemnisk | Kontaktieren Sie Ihren Lemnisk CSM, um **externe APIs** für Ihr Konto zu aktivieren. |
| Braze REST API-Schlüssel | Ein REST API-Schlüssel von Braze mit der Berechtigung `users.track`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der [Braze-URL für Ihr Konto]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints#api-and-sdk-endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Integration von Lemnisk

### Schritt 1: Erstellen einer externen Braze API {#create-a-braze-external-api}

Gehen Sie in Lemnisk zum Kanal External APIs. Wählen Sie **Neue externe API hinzufügen**. Wir richten nun den Endpunkt [Tracking Nutzer:innen]({{site.baseurl}}/api/endpoints/user_data/post_user_track) als externe API ein.

![Starten Sie den Prozess der Erstellung externer APIs in Lemnisk]({% image_buster /assets/img/lemnisk/open_external_api.png %})

Geben Sie unter **Grundlegende Details** einen Namen, eine Beschreibung, einen Kanal und einen Bezeichner für den Kanal ein.

![Eingabe der grundlegenden Konfigurationsdetails für eine neue externe API in Lemnisk]({% image_buster /assets/img/lemnisk/ext_api_basic_details.png %})

Geben Sie unter **Externe API-Details** die entsprechenden Details für Ihren `users.track` Endpunkt ein. Mit {% raw %}`{{}}`{% endraw %} können Sie mehrere Felder auf Engagement-Ebene definieren. So können Sie für verschiedene Kampagnen unterschiedliche Werte festlegen.

![Ausfüllen der Details für den Endpunkt und die Nutzdaten der externen APIs]({% image_buster /assets/img/lemnisk/ext_api_ext_api_details.png %})

Um die Einrichtung Ihrer Tracking Nutzer:innen Konfiguration abzuschließen, wählen Sie **Speichern**. Sie werden automatisch auf die Seite **Test API** weitergeleitet.

### Schritt 2: Testen Sie die Konfiguration

Geben Sie auf der Seite **Test API** einige Testwerte für die API-Parameter in Ihrer JSON-Strukturansicht ein und wählen Sie dann **Testkonfiguration**.

Wenn Ihre Zugangsdaten und API-Definitionen korrekt sind, wird Braze eine erfolgreiche Antwort zurückgeben.

![Testen einer externen API-Konfiguration mit einer Beispiel-Nutzlast und einer erfolgreichen Antwort]({% image_buster /assets/img/lemnisk/test_ext_api.png %})

Als nächstes überprüfen Sie, ob Ihre Ereignisse erfolgreich an Braze gesendet werden. Gehen Sie im Braze-Dashboard zu **Zielgruppe** > **Nutzer:innen suchen** und geben Sie dann einen der Bezeichner aus Ihrer Externen API-Konfiguration ein (z.B. eine E-Mail Adresse eines Nutzers). Wenn alles richtig funktioniert, wird das Profil aufgelistet, das Ihren Test-API-Trigger erhalten hat.

![Anzeigen des Profils und der Übersicht über die Aktivitäten eines Nutzers:in in Braze]({% image_buster /assets/img/lemnisk/braze_cov.png %})

### Schritt 3: Triggern Sie Nutzer:innen-Ereignisse in Braze

1. Auf Lemnisk erstellen Sie ein neues Segment. Sie könnten zum Beispiel ein Segment erstellen, das Informationen an Braze sendet, sobald Nutzer:innen ein Lead-Formular abschicken.
2. Gehen Sie in Ihrem neuen Segment auf **Externe API** > **Engagement hinzufügen**.
3. Geben Sie unter **Engagement-Erstellung** die grundlegenden Details ein und wählen Sie die Konfiguration aus, [die Sie zuvor erstellt haben](#create-a-braze-external-api).
4. Unter **Configure Parameters (Parameter konfigurieren**) finden Sie die Eingaben für die Braze-Parameter, die Sie auf der Ebene des Engagements freigeben möchten. Im folgenden Beispiel werden der _Name des Nutzers_:innen, die _Produkt ID_ und der _Zeitpunkt des Ereignisses_ angezeigt.
    ![Erstellen eines Engagements zum Senden von Nutzerdaten an Braze]({% image_buster /assets/img/lemnisk/create_an_engagement.png %})
5. Geben Sie die relevanten Personalisierungsvariablen für die von uns gewählten Parameter ein und wählen Sie dann **Speichern**.
6. Wenn Sie fertig sind, aktivieren Sie das Engagement.
