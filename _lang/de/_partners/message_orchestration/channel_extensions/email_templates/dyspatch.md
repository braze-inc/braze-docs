---
nav_title: Dyspatch
article_title: Dyspatch
alias: /partners/dyspatch
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Dyspatch, einem Drag-and-Drop-E-Mail-Builder, mit dem Sie schöne, reaktionsschnelle und ansprechende E-Mails erstellen können, ohne Code schreiben zu müssen."
page_type: partner
search_tag: Partner

---

# Dyspatch

> [Dyspatch][1] bietet einen intuitiven Drag-and-Drop-E-Mail-Builder, mit dem Sie schöne, ansprechende und ansprechende E-Mails erstellen können, ohne Code schreiben zu müssen. Arbeiten Sie mit Ihrem Team zusammen, um E-Mails in Dyspatch zu erstellen und zu genehmigen und sie dann in wenigen Schritten nach Braze zu exportieren! 

Die Integration von Dyspatch und Braze ermöglicht es Ihnen, den Lebenszyklus Ihrer E-Mail-Erstellung zu vereinfachen, indem Sie Dyspatch-E-Mail-Vorlagen direkt nach Braze exportieren.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Dyspatch-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Dyspatch-Konto][3] mit einer [Eigentümer- oder Administratorrolle][4]. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit vollständigen **Vorlagenberechtigungen**. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

Mit der Integration von Braze und Dyspatch können Sie Dyspatch-E-Mail-Vorlagen direkt in Ihre Braze-Mediathek exportieren oder Ihre Vorlage herunterladen und manuell hochladen. 

### Schritt 1: Erstellen Sie die Braze-Integration

Öffnen Sie im Dyspatch-Verwaltungsportal das Dropdown-Menü Ihres Benutzernamens und wählen Sie **Integrationen**. Erstellen Sie eine neue Integration, wählen Sie **Braze** und geben Sie Ihren Braze API-Schlüssel ein.

Im Feld **Exporte lokalisieren nach** können Sie wählen, wie Sie die Lokalisierung verwalten möchten. Mit diesem Feld können Sie [Ihre E-Mail-Vorlagen lokalisieren][6] und nach Braze exportieren, um auf einfache Weise nach Sprache oder Landessprache personalisierte E-Mails zu versenden. 

![Dyspatch Exportvorlage]({% image_buster /assets/img/dyspatch/dyspatch_integration_create.png %}){: style="max-width:50%;"}

### Schritt 2: Vorlage nach Braze exportieren

Nachdem Sie eine E-Mail in Dyspatch fertiggestellt haben, zeigen Sie die veröffentlichte E-Mail-Vorlage an und klicken Sie auf **Herunterladen/Exportieren** und dann auf **Zur Integration exportieren**, um Ihre Vorlage an Braze zu senden.

Wenn Sie Ihre Vorlage manuell hochladen möchten, sehen Sie sich die veröffentlichte E-Mail-Vorlage an und klicken Sie auf **Download/Export** und dann auf **HTML herunterladen**. Als nächstes wählen Sie in Ihrem Braze-Konto im Bereich **Vorlagen & Medien > E-Mail-Vorlagen** die Option **Aus Datei**, um Ihre Vorlage hochzuladen.

![Dyspatch Exportvorlage]({% image_buster /assets/img/dyspatch/dyspatch_export.gif %})

{% alert important %}
Wählen Sie kein **Inline-CSS** im Abschnitt **Sendeinfo** für eine Dyspatch-E-Mail-Vorlage in Braze. Dyspatch kümmert sich darum, indem es dafür sorgt, dass Ihre E-Mails stabil, reaktionsschnell und versandfertig sind.
{% endalert %}

### Nutzung

Sie finden Ihre hochgeladene Dyspatch-Vorlage in Ihrem Braze-Konto im Bereich **Vorlagen & Medien > E-Mail-Vorlagen**. Mit dieser E-Mail-Vorlage können Sie jetzt damit beginnen, ansprechende E-Mail-Nachrichten an Ihre Kunden zu versenden!

[1]: https://www.dyspatch.io
[2]: https://dashboard.braze.com/sign_in
[3]: https://www.dyspatch.io/login/
[4]: https://docs.dyspatch.io/administration/dyspatch_roles/
[5]: https://docs.dyspatch.io/exports/export_to_braze/#download-your-template
[6]: https://docs.dyspatch.io/localization/localizing_a_template/
