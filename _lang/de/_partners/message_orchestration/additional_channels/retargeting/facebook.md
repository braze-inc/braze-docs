---
nav_title: Facebook
article_title: Facebook Zielgruppen-Export
alias: /partners/facebook/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Facebook, einer führenden sozialen Plattform, über die Marken ihre Kunden erreichen und mit ihnen in Kontakt treten können."
page_type: partner
search_tag: Partner

---

# Facebook Zielgruppen-Export

> Die Integration von Braze und Facebook ermöglicht es Ihnen, Ihre Braze-Segmente manuell nach Facebook zu exportieren, um Facebook Custom Audiences zu erstellen. Dies ist ein einmaliger, statischer Audience-Export und erstellt nur neue Facebook Custom Audiences.

Häufige Anwendungsfälle für den Export von Facebook Custom Audiences sind:
- Retargeting von Nutzern an bestimmten Punkten ihres Lebenszyklus
- Erstellen von Listen mit Ausschlusszielen
- Erstellen von [Lookalike Audiences][4] zur effizienteren Gewinnung neuer Benutzer
<br><br>

{% alert note %}
Der Facebook Audience Export verwendet das **User Access Token**, um Anfragen zu autorisieren.<br><br>
Wenn Sie diese Funktion zusammen mit der Funktion [Audience Sync to Facebook]({{site.baseurl}}/audience_sync_facebook/) verwenden, verwendet Braze standardmäßig das zuverlässigere **System User Token**, das Sie bereits erstellt haben, um Anfragen zu autorisieren.
{% endalert %}

{% alert note %}
Wenn Sie an den Beta-Tests für Meta-Arbeitskonten teilnehmen, stellen Sie sicher, dass Sie die Verbindung zwischen Ihrem Konto und der [Facebook-Partnerseite]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync#step-1-connect-to-facebook) trennen und erneut herstellen.
{% endalert %}

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| [Facebook Business Manager][1] | Ein zentrales Tool zur Verwaltung der Facebook-Assets Ihrer Marke (z. B. Werbekonten, Seiten, Apps). |
| [Facebook-Anzeigenkonto][2] | Ein aktives Facebook-Anzeigenkonto, das mit dem Business Manager Ihrer Marke verbunden ist und das Sie mit Braze Custom Audiences verwenden möchten.<br><br>Vergewissern Sie sich, dass Ihr Facebook Business Manager-Administrator Ihnen Administratorrechte für die Facebook-Anzeigenkonten erteilt hat, die Sie mit Braze verwenden möchten, und dass Sie die Geschäftsbedingungen für Ihr Anzeigenkonto akzeptiert haben. Andernfalls können Sie innerhalb von Braze nicht auf Facebook-Anzeigenkonten zugreifen. |
| [Facebook Benutzerdefinierte Zielgruppen Bedingungen][3]| Sie müssen die Facebook-Bedingungen für benutzerdefinierte Zielgruppen für Ihre Facebook-Anzeigenkonten, die Sie mit Braze verwenden möchten, akzeptieren.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Mit Facebook verbinden

1. Gehen Sie im Braze-Dashboard zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Facebook**. 

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Technologiepartner** unter **Integrationen**.
{% endalert %}

{: start="2"}
2\. Im Modul Facebook Audience Export wählen Sie **Facebook verbinden**. <br><br>![Facebook-Technologiepartnerseite auf der Braze-Plattform.][6]{: style="max-width:70%;"}

{: start="3"}
3\. Im Dialogfenster Facebook oAuth autorisieren Sie Braze zur Erstellung von Custom Audiences in Ihren Facebook-Anzeigenkonten. <br><br>![Das erste Facebook-Dialogfeld mit der Aufforderung "Verbinden als X", wobei X Ihr Facebook-Benutzername ist.][8]{: style="max-width:30%;"}  ![Das zweite Dialogfeld von Facebook, in dem Sie um die Erlaubnis gebeten werden, Anzeigen für Ihre Werbekonten zu verwalten.][7]{: style="max-width:40%;"}

{: start="4"}
4\. Nachdem Braze mit Ihrem Facebook-Konto verknüpft ist, wählen Sie aus, welche Anzeigenkonten Sie mit Ihrem Braze-Arbeitsbereich synchronisieren möchten. <br><br>![Eine Liste der verfügbaren Anzeigenkonten, die Sie mit Facebook verbinden können.][9]{: style="max-width:70%;"}<br><br> Nachdem Sie eine Verbindung hergestellt haben, gelangen Sie zurück zur Partnerseite, wo Sie sehen können, welche Konten verbunden sind, und wo Sie bestehende Konten trennen können. <br><br> ![Eine aktualisierte Version der Facebook-Technologiepartnerseite, die die erfolgreich verbundenen Werbekonten anzeigt.][10]{: style="max-width:70%;"}<br>
<br> Ihre Facebook-Verbindung wird auf der Ebene des Braze-Arbeitsbereichs angewendet. Wenn Ihr Facebook-Administrator Sie aus Ihrem Facebook Business Manager oder dem Zugriff auf die verbundenen Facebook-Konten entfernt, erkennt Braze ein ungültiges Token. Infolgedessen werden Ihre aktiven Canvases mit Facebook-Publikumsschritten Fehler anzeigen, und Braze kann die Benutzer nicht synchronisieren. 

{% alert important %}
Für Kunden, die bereits den Facebook-App-Überprüfungsprozess für [Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) und [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/access#standard) durchlaufen haben, ist Ihr System-Benutzer-Token für den Facebook-Zielgruppenschritt weiterhin gültig. Sie können das Benutzer-Token des Facebook-Systems nicht über die Facebook-Partnerseite bearbeiten oder widerrufen. Stattdessen können Sie Ihr Facebook-Konto verbinden, um Ihr Facebook-System-Benutzertoken in Ihrem Braze-Arbeitsbereich zu ersetzen. 

<br><br>Die neue Facebook oAuth-Konfiguration wird auch für [Facebook-Exporte über Segmente]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites) gelten.
{% endalert %}

### Schritt 2: Exportieren Sie Ihre Benutzer in Facebook

In Braze ist der Export von Facebook-Zielgruppen über die Seite **Segmente** zugänglich. 

1. Wählen Sie auf der Seite **Segmente** das Segment, das Sie exportieren möchten.
2. Wählen Sie **Benutzerdaten** und dann **Als Facebook-Zielgruppe exportieren**. <br><br>![Im Abschnitt "Segmentdetails" eines Segments mit der Option "Benutzerdaten" wird ein Dropdown-Menü mit Optionen angezeigt, darunter "Als Facebook-Zielgruppe exportieren".][11]

{: start="3"}
3\. Wenn Sie Facebook noch nicht in Braze aktiviert haben, werden Sie aufgefordert, die Seite Facebook Technology Partners im Dashboard aufzurufen. Wenn Sie Facebook bereits über **Technologiepartner** > **Facebook** aktiviert haben, können Sie Ihr Facebook-Anzeigenkonto und die zu exportierenden Benutzerfelder auswählen. <br><br> Es gibt drei mögliche Benutzerfelder, die Sie exportieren können:
- Geräte-IDFA
- Telefonnummer 
- E-Mail

{% alert note %}
Sie können nur ein Benutzerfeld in einem einzigen Export auswählen. Wenn Sie mehr als einen Datentyp auswählen, erstellt Braze für jeden eine eigene benutzerdefinierte Zielgruppe.
{% endalert %}

{: start="4"}
4\. Nachdem Sie das Benutzerfeld ausgewählt haben, wählen Sie **Segment exportieren**. Wie beim CSV-Export erhalten Sie eine E-Mail, wenn der Export des Segments in Facebook abgeschlossen ist.
5\. Sehen Sie sich die benutzerdefinierte Zielgruppe im [Facebook Ads Manager][13] an.

{% alert important %}
Aus Gründen des Schutzes der Privatsphäre der Nutzer erlaubt Facebook nicht, dass Sie das sehen:

- Die genauen Benutzer, die erfolgreich zu einer benutzerdefinierten Zielgruppe hinzugefügt wurden. [Mehr erfahren.](https://www.facebook.com/business/help/112061095610075)
- Die Größe des benutzerdefinierten Publikums. [Mehr erfahren.](https://marketingland.com/exclusive-facebook-will-no-longer-show-audience-reach-estimates-for-custom-audiences-after-vulnerability-detected-236923)
{% endalert %}

#### Konfigurieren Sie Ihren Publikumsexport

Bei der Erstellung von Facebook-Zielgruppen möchten Sie möglicherweise bestimmte Nutzer auf der Grundlage ihrer Präferenzen ein- oder ausschließen, um Datenschutzgesetze einzuhalten, wie z. B. das Recht "Nicht verkaufen oder weitergeben" gemäß [CCPA](https://oag.ca.gov/privacy/ccpa). Vermarkter sollten die entsprechenden Filter für die Eignung der Nutzer in ihre Canvas-Eingabekriterien integrieren. Nachfolgend finden Sie einige Optionen. 

- Wenn Sie die [iOS IDFA über das Braze SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection) gesammelt haben, können Sie den Filter " **Ads Tracking Enabled** " verwenden. Wählen Sie den Wert `true`, um Benutzer nur an Audience Sync-Ziele zu senden, für die sie sich angemeldet haben. 

![][16]{: style="max-width:75%;"}

- Wenn Sie Opt-Ins, Opt-Outs, `Do Not Sell Or Share` oder andere relevante benutzerdefinierte Attribute sammeln, sollten Sie diese als Filter in Ihre Canvas-Eingabekriterien aufnehmen: 

![Ein Canvas mit einem Eintrag Publikum von "opted_in_marketing" ist gleich "true".][15]{: style="max-width:75%;"}


#### Gleichgesinnte Zielgruppen

Sobald Sie ein Segment erfolgreich als Facebook Audience exportiert haben, können Sie mit Facebook [Lookalike Audiences][4] weitere Gruppen erstellen. Diese Funktion untersucht die demografischen Daten, Interessen und anderen Attribute der von Ihnen gewählten Zielgruppe und erstellt eine neue Zielgruppe mit ähnlichen Attributen.

[1]: https://www.facebook.com/business/help/113163272211510?id=180505742745347
[2]: https://www.facebook.com/business/help/910137316041095?id=420299598837059
[3]: https://www.facebook.com/ads/manage/customaudiences/tos.php
[4]: https://www.facebook.com/business/help/164749007013531?id=401668390442328
[6]: {% image_buster /assets/img/fb/afb_1.png %}
[7]: {% image_buster /assets/img/fb/afb_2.png %}
[8]: {% image_buster /assets/img/fb/afb_3.png %}
[9]: {% image_buster /assets/img/fb/afb_4.png %}
[10]: {% image_buster /assets/img/fb/afb_5.png %}
[11]: {% image_buster /assets/img/fb/afb_6.png %}
[13]: https://www.facebook.com/ads/manager/audiences/manage/
[15]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
