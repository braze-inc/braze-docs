---
nav_title: Dynamics 365 Customer Insights
article_title: Dynamics 365 Customer Insights
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Dynamics 365 Customer Insights, einer führenden Kundendaten-Plattform für Unternehmen, die es Ihnen erlaubt, Segmente von Kunden nach Braze zu exportieren, um sie in Kampagnen oder Canvase zu verwenden."
alias: /partners/dynamics_365_customer_insights/
page_type: partner
search_tag: Partner
---

# Dynamics 365 Customer Insights
 
> [Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) ist eine führende Customer Data Platform (CDP) für Unternehmen, die personalisierte Kundenerlebnisse mit einer 360-Grad-Sicht auf Ihre Kunden zustellt.

_Diese Integration wird von Dynamics 365 Customer Insights gepflegt._

## Über die Integration

Die Integration von Braze und Dynamics 365 Customer Insights erlaubt es Ihnen, Segmente von Kunden nach Braze zu exportieren, um sie in Kampagnen oder Canvase zu verwenden.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Dynamics 365 Customer Insights Konto | Um die Vorteile dieser Partnerschaft nutzen zu können, benötigen Sie [ein Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) Konto. Sie benötigen Zugriff als Administrator, um Verbindungen innerhalb Ihres Dynamics 365 Customer Insights-Kontos anzuzeigen und zu bearbeiten, um auf die erforderlichen Plugins zuzugreifen. |
| Braze REST API-Schlüssel | Sie benötigen einen Braze REST API-Schlüssel mit den Berechtigungen `users.track` und `users.export.segment`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Passende Bezeichner für Profile | Vereinheitlichte Kundenprofile in den exportierten Segmenten enthalten ein Feld für eine E-Mail Adresse und eine Braze `external_id`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Braze-Verbindung einrichten

Navigieren Sie in Customer Insights zu **Admin > Verbindungen**. Wählen Sie dann **Verbindungen hinzufügen** und wählen Sie **Braze**, um die Verbindung zu konfigurieren. 

1. Geben Sie Ihrer Verbindung im Feld **Anzeigename** einen erkennbaren Namen. 
2. Wählen Sie, wer diese Verbindung nutzen kann. Wenn Sie dieses Feld leer lassen, ist der Standardwert Administratoren. Weitere Informationen finden Sie unter [Beitragenden erlauben, eine Verbindung für Exporte zu verwenden](https://docs.microsoft.com/en-us/dynamics365/customer-insights/connections#allow-contributors-to-use-a-connection-for-exports).
3. Geben Sie Ihren Braze API-Schlüssel und den REST-Endpunkt im Format `rest.iad-03.braze.com` an.
4. Wählen Sie **Ich stimme zu**, um die Einhaltung der Daten und des Datenschutzes zu bestätigen.
5. Wählen Sie **Verbinden**, um die Verbindung zu Braze zu initialisieren.
6. Wählen Sie **Sich als Exportbenutzer hinzufügen** und geben Sie Ihre Nutzer:innen für Customer Insights an.
7. Wählen Sie **Speichern**, um die Verbindung abzuschließen.

### Schritt 2: Erstellen eines Braze Segments

1. Gehen Sie in Braze zu **Zielgruppe** > **Segmente**.
2. Erstellen Sie ein Segment der Nutzer:innen, die Microsoft über Dynamics 365 Customer Insights aktualisieren soll.
3. Erfassen Sie den **API-Bezeichner** des Segments

### Schritt 3: Konfigurieren Sie einen Export

Sie können diesen Export konfigurieren, wenn Sie Zugang zu einer Verbindung dieses Typs haben. Weitere Informationen finden Sie in der [Übersicht über Exporte](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#set-up-a-new-export).

1. Gehen Sie in Customer Insights zu **Daten > Exporte**. Um einen neuen Export zu erstellen, wählen Sie **Ziel hinzufügen**.
2. Wählen Sie im Feld **Verbindung für den Export** eine Verbindung für den Abschnitt Braze aus. Wenn Sie diesen Abschnittsnamen nicht sehen, stehen Ihnen keine Verbindungen dieses Typs zur Verfügung.
3. Geben Sie den Bezeichner der Segment API des Segments in Braze an.
4. Wählen Sie im Abschnitt **Datenabgleich** im Feld **E-Mail** das Feld aus, das die E-Mail-Adresse eines Kunden darstellt. Wählen Sie dann im Feld **Braze Customer ID** das Feld aus, das die Braze ID des Kunden darstellt. Sie können auch ein zusätzliches, optionales Feld für den Abgleich der Daten auswählen.
  a. Wenn Sie die Abbildung `external_id` in Braze dem Feld Kund:in in Customer Insights zuordnen, werden die vorhandenen Datensätze beim Exportieren in Braze aktualisiert.
  b. Wenn Sie ein anderes ID-Feld, das nicht der `external_id` eines Datensatzes in Braze entspricht, oder ein leeres Feld abbilden, werden beim Exportieren neue Datensätze in Braze erstellt.
5. Wählen Sie schließlich die Segmente aus, die Sie exportieren möchten, und wählen Sie **Speichern**. 

Beachten Sie, dass durch das Speichern eines Exports der Export nicht sofort ausgeführt wird. Dieser Export wird bei jeder [geplanten Aktualisierung](https://docs.microsoft.com/en-us/dynamics365/customer-insights/system#schedule-tab) ausgeführt. Zudem können Sie [Daten auf Anfrage exportieren](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#run-exports-on-demand). 


### Verwendung dieser Integration

Nachdem Ihre Segmente erfolgreich nach Braze exportiert wurden, finden Sie sie als angepasste Attribute in den Nutzerprofilen. Das angepasste Attribut wird mit dem Bezeichner der Braze Segmente API benannt, der bei der Konfiguration der Exportverbindung eingegeben wurde. Zum Beispiel, `"Segment_API_Identifier": "0000-0000-0000"`

Um ein Segment dieser Nutzer:innen in Braze zu erstellen, gehen Sie zu **Segmente**, erstellen Sie ein neues Segment und wählen Sie **angepasste Attribute** als Filter. Von hier aus können Sie das angepasste Attribut auswählen, das mit Dynamics 365 synchronisiert wurde. Nachdem das Segment erstellt wurde, können Sie es als Zielgruppen-Filter auswählen, wenn Sie eine Kampagne oder ein Canvas erstellen.

{% alert note %}
Weitere Informationen zu dieser Integration finden Sie im [Artikel über die Integration von](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-braze) Braze von Microsoft.
{% endalert %}


