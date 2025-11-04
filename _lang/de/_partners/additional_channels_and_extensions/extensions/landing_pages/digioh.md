---
nav_title: Digioh
article_title: Digioh
description: "Dieser Artikel referenziert die Partnerschaft zwischen Braze und Digioh, einer Umfrageplattform, mit der Sie auf einfache Weise Pop-ups, Formulare, Umfragen und Kommunikationspräferenzzentren erstellen können, die ein echtes Engagement in Ihren Kampagnen von Braze fördern."
alias: /partners/digioh/
page_type: partner
search_tag: Partner

---

# Digioh

> [Digioh](https://www.digioh.com/) hilft Ihnen, Ihre Listen zu erweitern, First-Party-Daten zu erfassen und Ihre Daten für Ihre Kampagnen bei Braze zu nutzen.

_Diese Integration wird von Digioh gepflegt._

## Über die Integration

Die Integration von Braze und Digioh erlaubt es Ihnen, den flexiblen Drag-and-Drop-Builder zu nutzen, um Formulare, Pop-ups, Performance Center, Landing Pages und Umfragen zu erstellen, die Sie mit Ihren Kund:innen verbinden. Digioh unterstützt Sie bei der Integration und hilft Ihnen bei der Erstellung, Gestaltung und dem Start Ihrer ersten Kampagne.

!["Erstellen Sie mit Digioh flexible E-Mail- und Kommunikations-Präferenzzentren"]({% image_buster /assets/img/digioh/pref_pop_examples.png %}){: style="border:0"}

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
|Digioh Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Digioh-Konto](https://www.digioh.com/). |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze API `/users/track/` Endpunkt | Ihre REST-Endpunkt-URL mit den angehängten `/users/track/` Details. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/api/basics/#endpoints) ab.<br><br>Wenn Ihr REST API Endpunkt z.B. `https://rest.iad-01.braze.com` lautet, wird Ihr `/users/track/` Endpunkt `https://rest.iad-01.braze.com/users/track/` sein. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integration 

Um Digioh zu integrieren, müssen Sie zunächst den Konnektor von Braze konfigurieren. Wenn Sie fertig sind, müssen Sie die Integration auf ein Leuchtpult (Widget) anwenden. Besuchen Sie [Digioh](https://help.digioh.com/knowledgebase/digioh-integration-basics/), um mehr über die Grundlagen der Integration zu erfahren.

### Schritt 1: Digioh-Integration erstellen 

Klicken Sie in Digioh auf den Tab **Integrationen** und dann auf den Button **Neue Integration**. Wählen Sie **Braze** aus der Dropdown-Liste **Integration** aus und benennen Sie die Integration. 

!["Wählen Sie die richtige Integration aus der Dropdown-Liste aus"]({% image_buster /assets/img/digioh/2.png %}){: style="max-width:50%;"}

Als nächstes geben Sie den REST API-Schlüssel von Braze und den Endpunkt Ihrer Braze API `/users/track/` ein. 

Verwenden Sie schließlich den Abschnitt Abbildung der Felder, um weitere angepasste Felder als E-Mail und Name abzubilden. Der folgende Code Snippet zeigt eine Beispiel-Nutzlast. Wenn Sie fertig sind, wählen Sie **Integration erstellen**.

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

### Schritt 2: Einen Digioh Leuchtkasten erstellen

Verwenden Sie den Digioh [Design-Editor](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/), um ein Leuchtpult (Widget) zu erstellen. <br>
Möchten Sie eine Galerie sehen, wie Sie den Design Editor nutzen können? Besuchen Sie die Digioh [Themengalerie](https://www.digioh.com/theme-gallery).

### Schritt 3: Integration anwenden

Um diese Integration auf einen [Digioh-Leuchtkasten](https://help.digioh.com/knowledgebase/digioh-platform-training-videos-video-series-getting-started-with-digioh/) anzuwenden, navigieren Sie zur Seite **Boxen** und wählen Sie den Link **Hinzufügen** oder **Bearbeiten** in der Spalte **Integrationen**. Dies kann auch über den Bereich **Integration** des Editors hinzugefügt werden.

!["Fügen Sie die Integration zu einem Leuchttisch hinzu"]({% image_buster /assets/img/digioh/3.png %}){: style="max-width:90%"}

Wählen Sie hier **Integration hinzufügen**, wählen Sie die gewünschte Integration aus und **speichern Sie**. Digioh wird Ihre erfassten Leads jetzt in Realtime an Braze weiterleiten.


