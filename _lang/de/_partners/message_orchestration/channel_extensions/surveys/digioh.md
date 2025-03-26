---
nav_title: Digioh
article_title: Digioh
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Digioh, einer Umfrageplattform, mit der Sie auf einfache Weise Pop-ups, Formulare, Umfragen und Kommunikationspräferenzzentren erstellen können, die ein echtes Engagement in Ihren Braze-Kampagnen fördern."
alias: /partners/digioh/
page_type: partner
search_tag: Partner

---

# Digioh

> [Digioh](https://www.digioh.com/) hilft Ihnen, Ihre Listen zu erweitern, Daten von Erstanbietern zu erfassen und Ihre Daten für Ihre Braze-Kampagnen zu nutzen.

Mit der Integration von Braze und Digioh können Sie den flexiblen Drag-and-Drop-Builder verwenden, um markenbezogene Formulare, Pop-ups, Performance Center, Landing Pages und Umfragen zu erstellen, die Sie mit Ihren Kunden verbinden. Digioh unterstützt Sie bei der Einrichtung der Integration und hilft Ihnen bei der Erstellung, dem Design und dem Start Ihrer ersten Kampagne.

!["Erstellen Sie mit Digioh flexible E-Mail- und Kommunikationspräferenzzentren".][5]{: style="border:0"}

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
|Digioh Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Digioh-Konto](https://www.digioh.com/). |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze API `/users/track/` Endpunkt | Ihre REST-Endpunkt-URL mit den angehängten `/users/track/` Details. Ihr Endpunkt hängt von der [Braze URL für Ihre Instanz][6] ab.<br><br>Wenn Ihr REST-API-Endpunkt zum Beispiel `https://rest.iad-01.braze.com` lautet, wird Ihr `/users/track/` -Endpunkt `https://rest.iad-01.braze.com/users/track/` sein. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integration 

Um Digioh zu integrieren, müssen Sie zunächst den Braze-Anschluss konfigurieren. Wenn Sie fertig sind, müssen Sie die Integration auf ein Leuchtpult (Widget) anwenden. Besuchen Sie [Digioh](https://help.digioh.com/knowledgebase/digioh-integration-basics/), um mehr über die Grundlagen der Integration zu erfahren.

### Schritt 1: Digioh-Integration erstellen 

Klicken Sie in Digioh auf die Registerkarte **Integrationen** und dann auf die Schaltfläche **Neue Integration**. Wählen Sie **Braze** aus der Dropdown-Liste **Integration** aus und benennen Sie die Integration. 

!["Wählen Sie die richtige Integration aus dem Dropdown-Menü"][2]{: style="max-width:50%;"}

Als nächstes geben Sie den Braze REST API-Schlüssel und Ihren Braze API `/users/track/` Endpunkt ein. 

Verwenden Sie schließlich den Abschnitt Felder zuordnen, um weitere benutzerdefinierte Felder als E-Mail und Name zuzuordnen. Der folgende Codeausschnitt zeigt eine Beispiel-Nutzlast. Wenn Sie fertig sind, wählen Sie **Integration erstellen**.

```json
{
    "attributes" : [
         {
           "external_id": "[EMAIL_MD5]",
           "email" : "[EMAIL]"
         }
     ]
}
```

### Schritt 2: Einen Digioh-Leuchtkasten erstellen

Verwenden Sie den [Digioh-Design-Editor](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/), um ein Leuchtpult (Widget) zu erstellen. <br>
Möchten Sie eine Galerie sehen, wie Sie den Design-Editor einsetzen können? Besuchen Sie die Digioh [Themengalerie](https://www.digioh.com/theme-gallery).

### Schritt 3: Integration anwenden

Um diese Integration auf einen [Digioh-Leuchtkasten](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/) anzuwenden, navigieren Sie zur Seite **Boxen** und wählen Sie den Link **Hinzufügen** oder **Bearbeiten** in der Spalte **Integrationen**. Dies kann auch über den Bereich **Integration** des Editors hinzugefügt werden.

!["Fügen Sie die Integration zu einem Leuchttisch hinzu"][3]{: style="max-width:90%"}

Wählen Sie hier **Integration hinzufügen**, wählen Sie die gewünschte Integration und **speichern Sie**. Digioh wird Ihre erfassten Leads jetzt in Echtzeit an Braze weiterleiten.

[2]: {% image_buster /assets/img/digioh/2.png %}
[3]: {% image_buster /assets/img/digioh/3.png %}
[4]: {% image_buster /assets/img/digioh/4.png %}
[5]: {% image_buster /assets/img/digioh/pref_pop_examples.png %}
[6]: {{site.baseurl}}/api/basics/#endpoints