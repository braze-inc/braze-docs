---
nav_title: Dynamics 365 Kundeneinblicke
article_title: Dynamics 365 Kundeneinblicke
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Dynamics 365 Customer Insights, einer führenden Plattform für Unternehmenskundendaten, die es Ihnen ermöglicht, Kundensegmente zur Verwendung in Kampagnen oder Canvases nach Braze zu exportieren."
alias: /partners/dynamics_365_customer_insights/
page_type: partner
search_tag: Partner
---

# Dynamics 365 Kundeneinblicke
 
> [Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) ist eine führende Kundendatenplattform für Unternehmen, die personalisierte Kundenerlebnisse mit einer 360-Grad-Sicht auf Ihre Kunden bietet.



## Über die Integration

Die Integration von Braze und Dynamics 365 Customer Insights ermöglicht Ihnen den Export von Kundensegmenten nach Braze zur Verwendung in Kampagnen oder Canvases.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Dynamics 365 Customer Insights Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie [ein Dynamics 365 Customer Insights-Konto](https://dynamics.microsoft.com/en-gb/ai/customer-insights/). Sie benötigen einen Administrator-Zugang, um Verbindungen innerhalb Ihres Dynamics 365 Customer Insights-Kontos anzuzeigen und zu bearbeiten, damit Sie auf die erforderlichen Plugins zugreifen können. |
| Braze REST API Schlüssel |  <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
|  |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Lötverbindung einrichten

Navigieren Sie in Customer Insights zu **Verwaltung > Verbindungen**. Wählen Sie dann **Verbindungen hinzufügen** und wählen Sie **Braze**, um die Verbindung zu konfigurieren. 

1. Geben Sie Ihrer Verbindung im Feld **Anzeigename** einen erkennbaren Namen. 
2. Wählen Sie, wer diese Verbindung nutzen kann. Wenn Sie dieses Feld leer lassen, ist die Voreinstellung Administratoren. Weitere Informationen finden Sie unter [Beitragenden erlauben, eine Verbindung für Exporte zu verwenden](https://docs.microsoft.com/en-us/dynamics365/customer-insights/connections#allow-contributors-to-use-a-connection-for-exports).
3. 
4. Wählen Sie **Ich stimme zu**, um die Einhaltung der Daten und des Datenschutzes zu bestätigen.
5. Wählen Sie **Verbinden**, um die Verbindung zu Braze zu initialisieren.
6. Wählen Sie **Sich als Exportbenutzer hinzufügen** und geben Sie Ihre Customer Insights-Zugangsdaten ein.
7. Wählen Sie **Speichern**, um die Verbindung abzuschließen.

### Schritt 2: 

1. 
2. 
3. 

### Schritt 3: Konfigurieren Sie einen Export

Sie können diesen Export konfigurieren, wenn Sie Zugang zu einer Verbindung dieses Typs haben. Weitere Informationen finden Sie in der [Übersicht Exporte](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#set-up-a-new-export).

1. Gehen Sie in Customer Insights zu **Daten > Exporte**. Um einen neuen Export zu erstellen, wählen Sie **Ziel hinzufügen**.
2.  Wenn Sie diesen Abschnittsnamen nicht sehen, stehen Ihnen keine Verbindungen dieses Typs zur Verfügung.
3. 
4. Wählen Sie im Abschnitt **Datenabgleich** im Feld **E-Mail** das Feld aus, das die E-Mail-Adresse eines Kunden darstellt.  
  a. 
  b. 
5.  

Beachten Sie, dass durch das Speichern eines Exports der Export nicht sofort ausgeführt wird. Dieser Export wird bei jeder [geplanten Aktualisierung](https://docs.microsoft.com/en-us/dynamics365/customer-insights/system#schedule-tab) ausgeführt. Sie können [die Daten](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#run-exports-on-demand) auch [bei Bedarf exportieren](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#run-exports-on-demand). 


### Mit dieser Integration

  

  Nachdem das Segment erstellt wurde, können Sie es bei der Erstellung einer Kampagne oder eines Canvas als Zielgruppenfilter auswählen.

{% alert note %}
Weitere Informationen zu dieser Integration finden Sie im [Artikel über die Integration von](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-braze) Braze von Microsoft.
{% endalert %}


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
