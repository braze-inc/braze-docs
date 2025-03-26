---
nav_title: Taxi for Email
article_title: Taxi for Email
alias: /partners/taxi_for_email
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Taxi for Email, einem Online-E-Mail-Marketing-Tool, mit dem Braze-Kunden intelligente E-Mail-Vorlagen über eine Drag-and-Drop-Oberfläche und eine einfache, aber leistungsstarke Syntax erstellen können."
page_type: partner
search_tag: Partner

---

# Taxi for Email

> [Taxi for Email](http://taxiforemail.com/) ist ein Online-E-Mail-Marketing-Tool, das einen intuitiven visuellen Drag-and-Drop-E-Mail-Editor bietet. Taxi fördert die Zusammenarbeit von Teams bei E-Mail-Kampagnen, indem es Textern und Redakteuren den Zugang und die Ressourcen ermöglicht, die sie für die Erstellung von E-Mails benötigen, und zwar ganz ohne Code.

Die Integration von Braze und Taxi nutzt die einfache, aber leistungsstarke Syntax von Taxi, um intelligente E-Mail-Vorlagen zu erstellen und nach Braze zu exportieren. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ------------| ----------- |
| Taxi for Email-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Taxi for Email-Konto. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit vollständigen **Vorlagenberechtigungen**. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze Endpunkt | [Ihr Braze-Endpunkt]({{site.baseurl}}/api/basics/#endpoints) ist mit der URL Ihres Braze-Dashboards verknüpft.<br><br> Wenn Ihre Dashboard-URL zum Beispiel `https://dashboard-03.braze.com` lautet, ist Ihr Endpunkt `dashboard-03`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

### Schritt 1: Erstellen Sie eine Taxi-E-Mail-Vorlage

Erstellen Sie eine Taxi-Vorlage auf der Taxi-Plattform. Nachdem die Vorlage erstellt wurde, navigieren Sie zu Ihren **Organisationseinstellungen** und wählen die Registerkarte **ESP Connectors**.

### Schritt 2: Lötverbinder erstellen

1. Klicken Sie in dem daraufhin angezeigten Dialog auf die Schaltfläche **Neu hinzufügen** und wählen Sie dann **Braze** aus der Dropdown-Liste. 
2. Wählen Sie **Braze**, um die Einstellungen für den Braze-Anschluss zu bearbeiten.
3. Geben Sie Ihren Braze-Endpunkt und Ihren Braze-API-Schlüssel ein.

Ihr Anschlussfeld ändert seine Farbe, nachdem die Details mit den richtigen Berechtigungen eingegeben wurden. Wenn sich dieses Feld nicht ändert, überprüfen Sie, ob Ihre Felder mit den aufgeführten Anforderungen übereinstimmen.

## Nutzung

Sie finden Ihre hochgeladene Taxi-Vorlage in Ihrem Braze-Konto im Bereich **Vorlagen & Medien > E-Mail-Vorlagen**. Mit dieser E-Mail-Vorlage können Sie jetzt damit beginnen, ansprechende E-Mail-Nachrichten an Ihre Kunden zu versenden!

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
