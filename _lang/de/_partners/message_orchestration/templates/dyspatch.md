---
nav_title: Dyspatch
article_title: Dyspatch
alias: /partners/dyspatch
description: "Dieser referenzierende Artikel beschreibt die Partnerschaft zwischen Braze und Dyspatch, einem E-Mail-Builder per Drag-and-Drop, der es Ihnen erlaubt, schöne, responsive und engagierte E-Mails zu erstellen, ohne Code schreiben zu müssen."
page_type: partner
search_tag: Partner

---

# Dyspatch

> [Dyspatch](https://www.dyspatch.io) bietet einen intuitiven E-Mail-Builder per Drag-and-Drop, mit dem Sie schöne, responsive und engagierte E-Mails erstellen können, ohne Code schreiben zu müssen. Arbeiten Sie mit Ihrem Team zusammen, um E-Mails in Dyspatch zu erstellen und zu genehmigen und sie dann in wenigen Schritten nach Braze zu exportieren! 

_Diese Integration wird von Dyspatch gepflegt._

## Über die Integration

Die Integration von Dyspatch und Braze erlaubt es Ihnen, Ihren Lebenszyklus für die Erstellung von E-Mails zu vereinfachen, indem Sie Dyspatch Templates direkt nach Braze exportieren.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Dyspatch Konto | Sie benötigen ein [Dyspatch-Konto](https://www.dyspatch.io/login/) mit einer [Eigentümer- oder Administratorrolle](https://docs.dyspatch.io/administration/dyspatch_roles/), um die Vorteile dieser Partnerschaft zu nutzen. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit vollständigen **Templates-Berechtigungen**. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

Mit der Integration von Braze und Dyspatch können Sie E-Mail-Templates von Dyspatch direkt in Ihre Bibliothek von Braze exportieren oder Ihr Template herunterladen und manuell hochladen. 

### Schritt 1: Erstellen Sie die Braze Integration

Öffnen Sie im Dyspatch Administrationsportal das Dropdown-Menü Ihres Benutzernamens und wählen Sie **Integrationen**. Erstellen Sie eine neue Integration, wählen Sie **Braze** aus, und geben Sie Ihren Braze API-Schlüssel ein.

Im Feld **Lokalisierung von Exporten nach** können Sie wählen, wie Sie die Lokalisierung verwalten möchten. Mit diesem Feld können Sie [Ihre Templates für E-Mails lokalisieren](https://docs.dyspatch.io/localization/localizing_a_template/) und nach Braze exportieren, um auf einfache Weise E-Mails zu versenden, die nach Sprache oder Region personalisiert sind. 

![Dyspatch Export Template]({% image_buster /assets/img/dyspatch/dyspatch_integration_create.png %}){: style="max-width:50%;"}

### Schritt 2: Template nach Braze exportieren

Nachdem Sie eine E-Mail in Dyspatch erstellt haben, zeigen Sie die veröffentlichte E-Mail-Vorlage an und klicken auf **Herunterladen/Exportieren** und dann auf **Zur Integration exportieren**, um Ihre Vorlage an Braze zu senden.

Wenn Sie Ihre Vorlage manuell hochladen möchten, sehen Sie sich die veröffentlichte E-Mail-Vorlage an und klicken Sie auf **Download/Export** und dann auf **HTML herunterladen**. Als nächstes wählen Sie in Ihrem Braze-Konto im Bereich **Templates und Medien > E-Mail-Vorlagen** die Option **Aus Datei aus**, um Ihre Vorlage hochzuladen.

![Dyspatch Export Template]({% image_buster /assets/img/dyspatch/dyspatch_export.gif %})

{% alert important %}
Wählen Sie kein **Inline CSS** im Abschnitt **Sendeinfo** für eine Dyspatch E-Mail-Vorlage in Braze aus. Dyspatch kümmert sich darum, indem es dafür sorgt, dass Ihre E-Mails stabil, responsiv und versandfertig sind.
{% endalert %}

### Nutzung

Sie finden Ihr hochgeladenes Dyspatch Template in Ihrem Braze-Konto im Bereich **Templates und Medien > E-Mail Templates**. Mit dieser E-Mail-Vorlage können Sie jetzt damit beginnen, ansprechende Nachrichten an Ihre Kund:in zu versenden!


