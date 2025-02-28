---
nav_title: Ada
article_title: Ada
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Ada, einer KI-gestützten Plattform, die Kundeninteraktionen automatisiert und personalisiert. Diese Integration ermöglicht es Ihnen, Benutzerprofile mit Daten aus Ihren automatisierten Ada-Gesprächen zu ergänzen."
alias: /partners/ada/
page_type: partner
search_tag: Partner

---

# Ada

> [Ada](https://ada.cx) ist eine Plattform für die Interaktion mit Marken, die das Kundenerlebnis mithilfe von KI automatisiert und personalisiert. Verwenden Sie Ada, um Ihre Nachrichten und Kampagnen auf der Grundlage von Benutzerdaten zu segmentieren, messen und analysieren Sie Konversationen, um neue Möglichkeiten zu entdecken, und nutzen Sie die Erkenntnisse aus dem Chat mit Kunden, um Ihre Benutzerprofile zu erweitern.  

Die Integration von Braze und Ada ermöglicht es Ihnen, Benutzerprofile mit Daten aus Ihren automatisierten Ada-Konversationen zu ergänzen. Sie können benutzerdefinierte Benutzerattribute auf der Grundlage der Informationen, die Sie während eines Ada-Chats sammeln, festlegen und benutzerdefinierte Ereignisse in Braze an bestimmten Punkten in einer Ada-Konversation aufzeichnen. Indem Sie Ihren Ada-Chatbot mit Braze verbinden, können Sie mehr über Ihre Kunden erfahren, und zwar anhand der Fragen, die sie zu Ihrer Marke stellen, oder indem Sie proaktiv Gespräche mit ihnen beginnen und ihnen Fragen stellen, die es Ihnen ermöglichen, mehr über ihre Interessen und Vorlieben zu erfahren.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Ada-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Ada-Konto](https://ada.cx), in dem die Anwendungen Braze und Answer Utilities aktiviert sind. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre REST-Endpunkt-URL][1]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Häufige Anwendungsfälle für die Integration von Braze und Ada sind:
- Verfolgen Sie die verschiedenen Interaktionen Ihrer Kunden mit Ihrem Ada-Bot als benutzerdefinierte Ereignisse in Braze. So wissen Sie, welche Kunden sich auf proaktive Kampagnen in Ada eingelassen haben, an Support-Agenten weitergeleitet wurden, bestimmte Fragen gestellt oder bestimmte Aktionen durchgeführt haben.
- Befragen Sie Ihre Kunden zu ihren Interessen, Vorlieben, demografischen Daten und mehr. Aktualisieren Sie ihr Profil in Braze automatisch mit diesen neuen Informationen unter Verwendung benutzerdefinierter Attribute.

## Integration

Um Braze und Ada zu integrieren, müssen Sie zunächst die Braze-Anwendung in Ihrem Ada-Dashboard einrichten und mit Ihrem Ada-Team zusammenarbeiten, um eine Metavariable für die Benutzer-ID in Ihrem Ada-Einbettskript einzurichten. Dann ziehen Sie den Braze-Block in den Antwort-Editor an die Stelle, an der Sie Informationen an Braze zurücksenden möchten - entweder ein Ereignis oder ein Attribut.

### Schritt 1: Einrichten der Braze-App in Ada

Gehen Sie auf dem Ada Dashboard zu **Einstellungen > Integrationen > Handoff-Integrationen**.

Klicken Sie neben Braze auf **Verbinden** und geben Sie die folgenden Informationen ein:
- **REST-Endpunkt**: Geben Sie die URL Ihres Braze REST-Endpunkts ein. 
- **API-Schlüssel**: Geben Sie Ihren Braze REST API-Schlüssel ein. 
- **App-ID**: Geben Sie die App-ID ein, die Sie mit Ada-Chattern verknüpfen möchten.

### Schritt 2: Einen Bezeichner von Braze zu Ada durchreichen

Um sicherzustellen, dass Sie den richtigen Benutzer aktualisieren, müssen Sie sich an Ihr Ada-Team wenden. Es kann Ihnen dabei helfen, die notwendigen Änderungen am Ada-Einbettungsskript vorzunehmen, um eine Kennung von Braze zu erhalten. Diese Integration ist so konzipiert, dass sie eine externe ID akzeptiert, aber es ist auch möglich, andere Identifikatoren zu übergeben, wie z.B. einen Benutzer-Alias. 

### Schritt 3: Lassen Sie den Lötblock in die entsprechenden Antworten fallen

Um den Braze-Block zu verwenden, ziehen Sie ihn aus der Blockschublade in die entsprechende Antwort und wählen eine Aktion aus. Mit dem Lötblock können Sie zwei Aktionen durchführen:
* Strecke Ereignis
* Attribut aktualisieren

{% tabs local %}
{% tab Laufwettbewerb %}

#### Antwort Utilities blockieren

1. Ziehen Sie den Block Answer Utilities aus der Blockschublade in die Position direkt über Ihrem Braze-Block. 
2. Wählen Sie die Aktion **Datum formatieren** und geben Sie `today` in das Feld **Datum** ein.
3. Geben Sie `iso` in das Feld **Ausgabeformat** ein. Erstellen Sie unter **Antwort als Variable speichern** eine Variable für **Formatiertes Datum** mit dem Namen `iso_time`.

![Der Answer Utilities-Block mit Feldern, die wie im vorangegangenen Text beschrieben ausgefüllt sind.]({% image_buster /assets/img/ada/ada-braze-2.png %})

#### Hartlötblock

**4\.** Geben Sie im Braze-Block die von Ada im vorherigen Schritt eingerichtete Metavariable `external_id` in das Feld **Externe ID** ein.<br>
**5\.** Geben Sie in das Feld **Ereignisname** den Namen des Braze-Ereignisses ein, das Sie verfolgen möchten.<br>
**6\.** Geben Sie in das Feld **Time of Event** die Variable `iso_time` ein, die Sie im Block Answer Utilities erstellt haben.<br>
**7\.** Wählen Sie eine Fallback-Antwort aus, die angezeigt wird, wenn bei der Übertragung des Ereignisses an Braze ein Problem auftritt.

![Der Braze-Block mit Feldern, die wie im vorangegangenen Text beschrieben ausgefüllt sind.]({% image_buster /assets/img/ada/ada-braze-3.png %})

{% endtab %}
{% tab Attribut aktualisieren %}

#### Hartlötblock

1. Geben Sie im Braze-Block die von Ada im vorherigen Schritt eingerichtete Metavariable `external_id` in das Feld **Externe ID** ein. 
2. Geben Sie in das Feld **Attributname** den Namen des Braze-Attributs ein, das Sie verfolgen möchten. 
3. Geben Sie in das Feld **Attributwert** den Wert ein, den Sie festlegen möchten. Das kann ein Text, eine Variable oder eine Kombination aus Text und Variablen sein. 
4. Wählen Sie eine Fallback-Antwort aus, die angezeigt werden soll, wenn bei der Übertragung des Attributs an Braze ein Problem auftritt.

![Der Braze-Block mit Feldern, die wie im vorangegangenen Text beschrieben ausgefüllt sind.]({% image_buster /assets/img/ada/ada-braze-4.png %})

{% endtab %}
{% endtabs %}

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/ada/ada-braze-1.png %}
[3]: {% image_buster /assets/img/ada/ada-braze-2.png %}
[4]: {% image_buster /assets/img/ada/ada-braze-3.png %}
[5]: {% image_buster /assets/img/ada/ada-braze-4.png %}