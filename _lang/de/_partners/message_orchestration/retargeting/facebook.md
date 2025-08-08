---
nav_title: Facebook
article_title: Facebook Audience Export
alias: /partners/facebook/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Facebook, einer führenden sozialen Plattform, über die Marken ihre Kund:in erreichen und mit ihnen in Kontakt treten können."
page_type: partner
search_tag: Partner

---

# Facebook Audience exportieren

> Die Integration von Braze und Facebook ermöglicht es Ihnen, Ihre Segmente aus Braze manuell nach Facebook zu exportieren, um angepasste Zielgruppen für Facebook zu erstellen. Dies ist ein einmaliger, statischer Zielgruppenexport und erstellt nur neue Facebook Custom Audiences.

Häufige Anwendungsfälle für den Export von Facebook angepassten Zielgruppen sind:
- Retargeting von Nutzer:innen zu bestimmten Zeitpunkten in ihrem Lebenszyklus
- Erstellen von Listen für das Targeting von Ausschlüssen
- Erstellen von [Lookalike Audiences](https://www.facebook.com/business/help/164749007013531?id=401668390442328) zur effizienteren Gewinnung neuer Nutzer:innen
<br><br>

{% alert note %}
Der Facebook Audience Export verwendet das **User Access Token**, um Anfragen zu autorisieren.<br><br>
Wenn Sie dieses Feature zusammen mit dem Feature [Audience Sync to Facebook]({{site.baseurl}}/audience_sync_facebook/) verwenden, verwendet Braze standardmäßig das zuverlässigere **System User Token**, das Sie bereits erstellt haben, um Anfragen zu autorisieren.
{% endalert %}

{% alert note %}
Wenn Sie an den Beta-Tests für Meta Work Accounts teilnehmen, stellen Sie sicher, dass Sie Ihr Konto von der [Facebook Partnerseite]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync#step-1-connect-to-facebook) trennen und erneut verbinden.
{% endalert %}

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| [Facebook Business Manager:in](https://www.facebook.com/business/help/113163272211510?id=180505742745347) | Ein zentrales Tool zur Verwaltung der Facebook-Assets Ihrer Marke (z.B. Werbekonten, Seiten, Apps). |
| [Facebook Werbekonto](https://www.facebook.com/business/help/910137316041095?id=420299598837059) | Ein aktives Facebook-Anzeigenkonto, das an den Business Manager Ihrer Marke gebunden ist und das Sie mit angepassten Zielgruppen von Braze verwenden möchten.<br><br>Vergewissern Sie sich, dass der Administrator Ihres Facebook Business Managers Ihnen Administratorrechte für die Facebook-Anzeigenkonten erteilt hat, die Sie mit Braze verwenden möchten, und dass Sie die Geschäftsbedingungen für Ihr Anzeigenkonto akzeptiert haben. Andernfalls können Sie innerhalb von Braze nicht auf Facebook-Anzeigenkonten zugreifen. |
| [Facebook angepasste Zielgruppen Bedingungen](https://www.facebook.com/ads/manage/customaudiences/tos.php)| Sie müssen die Facebook-Bedingungen für angepasste Zielgruppen für Ihre Facebook-Werbekonten akzeptieren, die Sie mit Braze verwenden möchten.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Mit Facebook verbinden

1. Gehen Sie im Braze-Dashboard zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Facebook** aus. 

{: start="2"}
2\. Wählen Sie im Modul Facebook Audience Export die Option **Facebook verbinden**. <br><br>![Technologie-Partnerseite von Facebook auf der Braze-Plattform.]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:70%;"}

{: start="3"}
3\. Im Dialogfenster Facebook oAuth autorisieren Sie Braze, angepasste Zielgruppen in Ihren Facebook-Anzeigenkonten zu erstellen. <br><br>![Das erste Facebook-Dialogfeld mit der Aufforderung "Verbinden Sie sich als X", wobei X Ihr Facebook-Benutzername ist.]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"}  ![Das zweite Facebook-Dialogfeld mit der Aufforderung, Anzeigen für Ihre Werbekonten verwalten zu dürfen.]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

{: start="4"}
4\. Nachdem Braze mit Ihrem Facebook-Konto verknüpft ist, wählen Sie aus, welche Anzeigenkonten Sie in Ihrem Braze Workspace synchronisieren möchten. <br><br>![Eine Liste der verfügbaren Werbekonten, die Sie mit Facebook verbinden können.]({% image_buster /assets/img/fb/afb_4.png %}){: style="max-width:70%;"}<br><br> Nachdem Sie eine Verbindung hergestellt haben, gelangen Sie zurück zur Partnerseite, wo Sie sehen können, welche Konten verbunden sind und bestehende Konten trennen können. <br><br> ![Eine aktualisierte Version der Technologie-Partnerseite von Facebook, auf der die erfolgreich verbundenen Werbekonten angezeigt werden.]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:70%;"}<br>
<br> Ihre Facebook-Verbindung wird auf der Ebene des Braze Workspace angewendet. Wenn Ihr Facebook-Administrator Sie von Ihrem Facebook Business Manager oder dem Zugriff auf die verbundenen Facebook-Konten abmeldet, erkennt Braze ein ungültiges Token. Infolgedessen werden Ihre aktiven Canvase, die die Schritte der Facebook Audience verwenden, Fehler anzeigen, und Braze kann die Nutzer:innen nicht synchronisieren. 

{% alert important %}
Für Nutzer:in, die bereits den Facebook App-Überprüfungsprozess für [Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) und [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/access#standard) durchlaufen haben, ist Ihr Nutzer:in für den Schritt Facebook Zielgruppe weiterhin gültig. Sie können das Nutzer:in-Token des Facebook-Systems nicht über die Partnerseite von Facebook bearbeiten oder widerrufen. Stattdessen können Sie Ihr Facebook-Konto verbinden, um Ihr Nutzer:in-Token für das Facebook-System in Ihrem Braze-Workspace zu ersetzen. 

<br><br>Die neue Facebook oAuth-Konfiguration wird auch für [Facebook-Exporte über Segmente]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites) gelten.
{% endalert %}

### Schritt 2: Exportieren Sie Ihre Nutzer:innen in Facebook

In Braze ist der Export von Facebook Zielgruppen über die Seite **Segmente** zugänglich. 

1. Wählen Sie auf der Seite **Segmente** das Segment aus, das Sie exportieren möchten.
2. Wählen Sie **Nutzerdaten**, und wählen Sie dann **Als Facebook Audience exportieren**. <br><br>![Im Abschnitt "Segmentdetails" eines Segments, in dem "Nutzerdaten" ausgewählt ist, wird eine Dropdown-Liste mit Optionen angezeigt, die "Als Facebook Audience exportieren" enthält.]({% image_buster /assets/img/fb/afb_6.png %})

{: start="3"}
3\. Wenn Sie Facebook in Braze noch nicht aktiviert haben, werden Sie im Dashboard aufgefordert, die Facebook Technologie-Partner-Seite aufzurufen. Wenn Sie Facebook bereits über **Technologiepartner** > **Facebook** aktiviert haben, können Sie Ihr Facebook-Anzeigenkonto und die zu exportierenden Nutzer:innen-Felder auswählen. <br><br> Es gibt drei mögliche Nutzer:innen-Felder, die Sie exportieren können:
- Geräte-IDFA
- Telefonnummer 
- E-Mail

{% alert note %}
Sie können nur ein Nutzer:innen-Feld in einem einzigen Export auswählen. Wenn Sie mehr als einen Datentyp auswählen, erstellt Braze für jede Zielgruppe eine eigene angepasste Zielgruppe.
{% endalert %}

{: start="4"}
4\. Nachdem Sie das Nutzer:innen-Feld ausgewählt haben, wählen Sie **Segment exportieren**. Wie beim CSV-Export erhalten Sie eine E-Mail, wenn der Export des Segments in Facebook abgeschlossen ist.
5\. Sehen Sie sich die angepasste Zielgruppe im [Facebook Ads Manager:in](https://www.facebook.com/ads/manager/audiences/manage/) an.

{% alert important %}
Aus Gründen des Schutzes der Nutzer:innen ist es bei Facebook nicht zulässig, dass Sie diese sehen:

- Die genauen Nutzer:innen, die erfolgreich zu einer angepassten Zielgruppe hinzugefügt wurden. [Mehr erfahren.](https://www.facebook.com/business/help/112061095610075)
- Die Größe der angepassten Zielgruppe. [Mehr erfahren.](https://marketingland.com/exclusive-facebook-will-no-longer-show-audience-reach-estimates-for-custom-audiences-after-vulnerability-detected-236923)
{% endalert %}

#### Konfigurieren Sie den Export Ihrer Zielgruppe

Beim Aufbau von Facebook Zielgruppen können Sie bestimmte Nutzer:innen auf der Grundlage ihrer Präferenzen ein- oder ausschließen, um Datenschutzgesetze einzuhalten, wie z.B. das Recht "Nicht verkaufen oder teilen" gemäß dem [CCPA](https://oag.ca.gov/privacy/ccpa). Marketer sollten die entsprechenden Filter für die Eignung der Nutzer:innen in ihre Canvas-Eingangskriterien aufnehmen. Nachfolgend finden Sie einige Optionen. 

- Wenn Sie den [iOS Identifier for Advertisers (IDFA) über das Braze SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection) erfasst haben, können Sie den Filter **Ads Tracking Enablement** verwenden. Wählen Sie den Wert `true` aus, um Nutzer:innen nur in Zielgruppen zu schicken, für die sie ein Opt-in gesetzt haben. 

![]({% image_buster /assets/img/tiktok/tiktok16.png %}){: style="max-width:75%;"}

- Wenn Sie Opt-Ins, Opt-Outs, `Do Not Sell Or Share` oder andere angepasste Attribute sammeln, sollten Sie diese als Filter in Ihre Canvas-Eingangskriterien aufnehmen: 

![Ein Canvas mit einem Eingang Zielgruppe "opted_in_marketing" ist gleich "true".]({% image_buster /assets/img/tiktok/tiktok13.png %}){: style="max-width:75%;"}


#### Ähnlich aussehende Zielgruppen

Sobald Sie ein Segment erfolgreich als Facebook Audience exportiert haben, können Sie mit Facebook [Lookalike Audiences](https://www.facebook.com/business/help/164749007013531?id=401668390442328) weitere Gruppen erstellen. Dieses Feature betrachtet die demografischen Daten, Interessen und anderen Attribute der von Ihnen gewählten Zielgruppe und erstellt eine neue Zielgruppe mit ähnlichen Attributen.

