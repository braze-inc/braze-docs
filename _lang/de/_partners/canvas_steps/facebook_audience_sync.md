---
nav_title: Facebook
article_title: Canvas Audience Sync mit Facebook
description: "In diesem Referenzartikel erfahren Sie, wie Sie Braze Audience Sync für Facebook verwenden, um Anzeigen auf der Grundlage von verhaltensbezogenen Auslösern, Segmentierung und mehr zu schalten."
page_order: 2
alias: "/audience_sync_facebook/"

Tool:
  - Canvas

---

# Audience Sync mit Facebook

Mit der Braze Audience Sync to Facebook können Marken die Daten ihrer eigenen Nutzer aus ihrer eigenen Braze-Integration zu Facebook Custom Audiences hinzufügen, um Anzeigen auf der Grundlage von verhaltensbezogenen Auslösern, Segmentierung und mehr zu schalten. Jedes Kriterium, das Sie normalerweise zum Auslösen einer Nachricht (Push, E-Mail, SMS oder Webhook) in einem Braze Canvas auf der Grundlage Ihrer Benutzerdaten verwenden, kann jetzt auch zum Auslösen einer Anzeige für diesen Benutzer in Facebook mit Custom Audiences verwendet werden.

**Häufige Anwendungsfälle für die Synchronisierung von Custom Audiences sind**:

- Ansprechen von hochwertigen Nutzern über mehrere Kanäle, um Käufe oder Engagement zu fördern.
- Retargeting von Nutzern, die auf andere Marketingkanäle weniger gut reagieren.
- Erstellen von Unterdrückungszielgruppen, um zu verhindern, dass Nutzer Werbung erhalten, wenn sie bereits treue Kunden Ihrer Marke sind.
- Erstellen Sie Lookalike Audiences, um neue Nutzer effizienter zu gewinnen.

Mit dieser Funktion können Marken kontrollieren, welche spezifischen Erstanbieterdaten mit Facebook geteilt werden. Bei Braze werden die Integrationen, mit denen Sie Ihre First-Party-Daten teilen können und mit denen Sie sie nicht teilen können, mit größter Sorgfalt ausgewählt. Weitere Informationen finden Sie in unserer [Datenschutzrichtlinie](https://www.braze.com/privacy).

## Voraussetzungen

Sie müssen bestätigen, dass Sie die folgenden Elemente erstellt und abgeschlossen haben, bevor Sie Ihren Facebook Audience Step in Canvas einrichten. 

| Anforderung | Herkunft | Beschreibung |
| ----------- | ------ | ----------- |
| Facebook Business Manager | [Facebook][1] | Ein zentrales Tool zur Verwaltung der Facebook-Assets Ihrer Marke (z. B. Anzeigenkonten, Seiten und Apps). |
| Facebook Anzeigenkonto | [Facebook][2] | Ein aktives Facebook-Anzeigenkonto, das mit dem Business Manager Ihrer Marke verbunden ist.<br><br>Vergewissern Sie sich, dass Ihr Facebook Business Manager-Administrator Ihnen entweder die Berechtigung "Kampagnen verwalten" oder "Werbekonten verwalten" für die Facebook-Werbekonten erteilt hat, die Sie mit Braze verwenden möchten. Vergewissern Sie sich außerdem, dass Sie die Geschäftsbedingungen für Ihr Anzeigenkonto akzeptiert haben. |
| Facebook Benutzerdefinierte Zielgruppen Bedingungen | [Facebook][3] | Akzeptieren Sie die Facebook-Bedingungen für Custom Audiences für Ihre Facebook-Anzeigenkonten, die Sie mit Braze verwenden möchten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

### Schritt 1: Mit Facebook verbinden

Gehen Sie im Braze-Dashboard zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Facebook**. Wählen Sie unter Facebook-Zielgruppen-Export die Option **Facebook verbinden**.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Technologiepartner** unter **Integrationen**.
{% endalert %}

![Facebook-Technologieseite in Braze, die einen Abschnitt Übersicht und einen Abschnitt Facebook Audience Export mit der Schaltfläche Verbundenes Facebook enthält.][4]{: style="max-width:70%;"}

Es erscheint ein Facebook oAuth-Dialogfenster, um Braze zu autorisieren, Custom Audiences in Ihren Facebook-Anzeigenkonten zu erstellen.

![Das erste Facebook-Dialogfeld mit der Aufforderung "Verbinden als X", wobei X Ihr Facebook-Benutzername ist.][6]{: style="max-width:30%;"}  ![Das zweite Dialogfeld von Facebook, in dem Sie um die Erlaubnis gebeten werden, Anzeigen für Ihre Werbekonten zu verwalten.][5]{: style="max-width:40%;"}

Sobald Sie Braze mit Ihrem Facebook-Konto verknüpft haben, können Sie auswählen, welche Anzeigenkonten Sie mit Ihrem Braze-Arbeitsbereich synchronisieren möchten. 

![Eine Liste der verfügbaren Anzeigenkonten, die Sie mit Facebook verbinden können.][7]{: style="max-width:70%;"}

Sobald Sie sich erfolgreich verbunden haben, gelangen Sie zurück zur Partnerseite, wo Sie sehen können, welche Konten verbunden sind und bestehende Konten trennen können.

![Eine aktualisierte Version der Facebook-Technologiepartnerseite, die die erfolgreich verbundenen Werbekonten anzeigt.][8]{: style="max-width:70%;"}

Ihre Facebook-Verbindung wird auf der Ebene des Braze-Arbeitsbereichs angewendet. Wenn Ihr Facebook-Administrator Sie aus Ihrem Facebook Business Manager oder dem Zugriff auf die verbundenen Facebook-Konten entfernt, erkennt Braze ein ungültiges Token. Infolgedessen werden Ihre aktiven Canvases, die Facebook Audience-Komponenten verwenden, Fehler anzeigen, und Braze kann die Benutzer nicht synchronisieren. 

{% alert important %}
Für Kunden, die bereits den Facebook App Review Prozess für [Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) und [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/access#standard) durchlaufen haben, ist Ihr System User Token für die Facebook Audience Komponente weiterhin gültig. Sie können das Facebook System User Token nicht über die Facebook Partnerseite bearbeiten oder widerrufen. Stattdessen können Sie Ihr Facebook-Konto verbinden, um Ihr Facebook-Systembenutzer-Token in Ihrem Braze-Arbeitsbereich zu ersetzen. 

<br><br>Die Facebook oAuth-Konfiguration gilt auch für [Facebook-Exporte über Segmente]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites).
{% endalert %}

### Schritt 2: Akzeptieren Sie die Servicebedingungen für Custom Audiences

Bevor Sie Ihr Canvas einrichten, müssen Sie zunächst die Nutzungsbedingungen von Facebook für benutzerdefinierte Zielgruppen akzeptieren. Ihre Nutzungsbedingungen finden Sie unter folgendem Link:
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<your_ad_account_id>`

### Schritt 3: Hinzufügen einer Facebook Audience-Komponente in Canvas Flow

Fügen Sie eine Komponente in Ihrem Canvas hinzu und wählen Sie **Facebook Audience**.

![][18]{: style="max-width:35%;"} ![][20]{: style="max-width:28%;"}

### Schritt 4: Sync-Einrichtung

Klicken Sie auf die Schaltfläche **Benutzerdefinierte Audience**, um den Komponenteneditor zu öffnen.

Wählen Sie **Facebook** als den gewünschten Audience Sync-Partner aus.

![][19]{: style="max-width:80%;"}

Wählen Sie das gewünschte Facebook-Anzeigenkonto aus. Geben Sie in der Dropdown-Liste **Neue oder bestehende Zielgruppe auswählen** den Namen einer neuen oder bestehenden Zielgruppe ein. 

{% tabs %}
{% tab Ein neues Publikum schaffen %}
**Ein neues Publikum schaffen**<br>
Geben Sie einen Namen für die neue benutzerdefinierte Zielgruppe ein, wählen Sie **Benutzer zur Zielgruppe hinzufügen** und wählen Sie die Felder aus, die Sie mit Facebook synchronisieren möchten. Als nächstes speichern Sie Ihre Zielgruppe, indem Sie unten im Schritteditor auf die Schaltfläche **Zielgruppe erstellen** klicken.

![]({% image_buster /assets/img/audience_sync/fb_sync.png %})

Als nächstes speichern Sie Ihre Zielgruppe, indem Sie unten im Schritteditor auf die Schaltfläche Zielgruppe erstellen klicken. Die Benutzer werden oben im Schritteditor benachrichtigt, wenn die Audienz erfolgreich erstellt wurde oder wenn während dieses Prozesses Fehler auftreten. Da die Zielgruppe im Entwurfsmodus erstellt wurde, können Benutzer auch später in der Canvas-Reise auf diese Zielgruppe verweisen, um sie zu entfernen.

![]({% image_buster /assets/img/audience_sync/fb_sync2.png %})

Wenn Sie ein Canvas mit einer neuen Zielgruppe starten, erstellt Braze die neue benutzerdefinierte Zielgruppe beim Start des Canvas und synchronisiert die Benutzer anschließend nahezu in Echtzeit, sobald sie den Schritt zur Synchronisierung der Zielgruppe betreten.

{% endtab %}
{% tab Synchronisieren Sie mit einer bestehenden Zielgruppe %}
**Synchronisieren Sie mit einer bestehenden Zielgruppe**<br>
Braze bietet auch die Möglichkeit, Benutzer zu bestehenden benutzerdefinierten Facebook-Zielgruppen hinzuzufügen oder zu entfernen, um zu bestätigen, dass diese Zielgruppen aktuell sind. Um eine Synchronisierung mit einer bestehenden Zielgruppe vorzunehmen, geben Sie den Namen der bestehenden Zielgruppe in das Dropdown-Menü ein und wählen Sie, ob Sie **der Zielgruppe hinzufügen** oder **aus ihr entfernen** möchten. Braze fügt dann nahezu in Echtzeit Nutzer hinzu oder entfernt sie, sobald sie den Facebook Audience-Schritt betreten. 

![]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

Es ist wichtig zu wissen, dass Facebook das Entfernen von Nutzern aus benutzerdefinierten Zielgruppen verbietet, wenn die Größe der Zielgruppe zu gering ist (in der Regel weniger als 1.000). Infolgedessen kann Braze keine Benutzer für den Schritt Aus der Zielgruppe entfernen synchronisieren, bis die Zielgruppe die entsprechende Größe erreicht hat.

{% endtab %}
{% endtabs %}

### Schritt 5: Canvas starten

Sobald Sie Ihre Facebook Audience-Komponente konfiguriert haben, starten Sie einfach die Canvas! Die neue benutzerdefinierte Zielgruppe wird erstellt, und Nutzer, die die Facebook Audience-Komponente durchlaufen, werden in diese benutzerdefinierte Zielgruppe auf Facebook weitergeleitet. Wenn Ihr Canvas nachfolgende Komponenten enthält, werden Ihre Benutzer zum nächsten Schritt in ihrer User Journey übergehen.

Auf der Registerkarte **Verlauf** der benutzerdefinierten Zielgruppe im Facebook Audience Manager wird die Anzahl der Nutzer angezeigt, die von Braze an die Zielgruppe gesendet wurden. Wenn ein Benutzer den Schritt erneut betritt, wird er erneut zu Facebook weitergeleitet.

![Publikumsdetails und die Registerkarte Verlauf für ein bestimmtes Facebook-Publikum, die eine Publikumsverlaufstabelle mit Spalten für die Aktivität, Aktivitätsdetails, geänderte Elemente sowie das Datum und die Uhrzeit enthält.][9]{: style="max-width:80%;"}

## Umstellung auf Meta-Arbeitskonten

Ab Juli 2023 führt Meta Meta-Arbeitskonten für eine kleine Gruppe von Unternehmen ein, die an der Einführung dieses neuen Kontotyps interessiert sind. Wenn Sie ein mit Braze integriertes Geschäftskonto haben, stellen Sie sicher, dass Sie die Verbindung zur [Facebook-Partnerseite]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync#step-1-connect-to-facebook) mit Ihrem Geschäftskonto trennen und wiederherstellen, um diese Implementierung beizubehalten und keine aktiven Canvases zu unterbrechen.

## Überlegungen zur Benutzer-Synchronisierung und Ratenbegrenzung
 
Wenn Benutzer die Audience Sync-Stufe erreichen, synchronisiert Braze diese Benutzer nahezu in Echtzeit und respektiert dabei die Marketing-API-Ratenlimits von Facebook. In der Praxis bedeutet dies, dass Braze versucht, alle 5 Sekunden so viele Benutzer wie möglich zu verarbeiten, bevor es diese Benutzer an Facebook weiterleitet. 

Facebooks Marketing-API-Ratenlimit besagt, dass nicht mehr als ~190k API-Anfragen für jedes Anzeigenkonto in einem Zeitraum von 1 Stunde erfolgen dürfen. Wenn ein Braze-Kunde dieses Ratenlimit erreicht, wird Braze the Canvas die Synchronisierung für bis zu ~13 Stunden wiederholen. Wenn die Synchronisierung nicht möglich ist, werden diese Benutzer unter der Metrik Fehlerhafte Benutzer aufgeführt.

## Analytik verstehen

Die folgende Tabelle enthält Metriken und Beschreibungen, damit Sie die Analysen Ihrer Audience Sync-Komponente besser verstehen.

| Metrisch | Beschreibung |
| --- | --- |
| Aufgenommen | Anzahl der Benutzer, die diese Komponente eingegeben haben, um mit Facebook synchronisiert zu werden. |
| Fortgefahren mit nächstem Schritt | Wie viele Benutzer sind zur nächsten Komponente weitergegangen, falls es eine gibt. Alle Benutzer werden automatisch weitergeleitet, wenn dies der letzte Schritt im Canvas-Zweig ist. |
| Nutzer:innen synchronisiert | Anzahl der Benutzer, die erfolgreich mit Facebook synchronisiert wurden. |
| Nutzer:innen nicht synchronisiert | Anzahl der Benutzer, die nicht synchronisiert wurden, weil Felder zum Abgleich fehlen. |
| Nutzer:innen ausstehend | Anzahl der Benutzer, die derzeit von Braze für die Synchronisierung mit Facebook bearbeitet werden. |
| Fehler bei Nutzer:innen | Anzahl der Benutzer, die aufgrund eines API-Fehlers nach etwa 13 Stunden Wiederholungsversuchen nicht mit Facebook synchronisiert wurden. Mögliche Fehlerursachen können ein ungültiges Facebook-Token sein oder wenn die benutzerdefinierte Zielgruppe auf Facebook gelöscht wurde. |
| Canvas verlassen | Anzahl der Benutzer, die den Canvas verlassen haben. Dies geschieht, wenn der letzte Schritt in einem Canvas ein Facebook-Schritt ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Denken Sie daran, dass es aufgrund des Bulk Flush und des 13-stündigen Wiederholungsversuchs zu einer Verzögerung bei den Berichten über synchronisierte Benutzer und fehlerhafte Benutzer kommen wird.
{% endalert %}   

## Fehlersuche

{% details Was sollte ich als nächstes tun, wenn ich einen ungültigen Token-Fehler erhalte? %}
Sie können die Verbindung zu Ihrem Facebook-Konto auf der Facebook-Partnerseite einfach trennen und wiederherstellen. Vergewissern Sie sich bei Ihrem Facebook Business Manager Admin, dass Sie die entsprechenden Berechtigungen für das Anzeigenkonto haben, mit dem Sie synchronisieren möchten.
{% enddetails %}

{% details Warum kann mein Canvas nicht gestartet werden? %}
- Stellen Sie sicher, dass Ihr Systembenutzer-Token authentifiziert ist und Zugriff auf die gewünschten Anzeigenkonten im Facebook Business Manager hat.
- Vergewissern Sie sich, dass Sie ein Anzeigenkonto ausgewählt, einen Namen für die neue benutzerdefinierte Zielgruppe eingegeben und entsprechende Felder ausgewählt haben.
- Möglicherweise haben Sie das Limit von 500 benutzerdefinierten Zielgruppen auf Facebook erreicht. Gehen Sie in den Facebook Audience Manager, um einige nicht benötigte Audiences zu löschen, bevor Sie neue Custom Audiences mit Canvas erstellen.
{% enddetails %}

{% details Woher weiß ich, ob die Benutzer übereinstimmen, nachdem ich sie an Facebook weitergegeben habe? %}
Facebook stellt diese Informationen aus Gründen des Datenschutzes nicht zur Verfügung.
{% enddetails %}

{% details Unterstützt Braze wertbasierte benutzerdefinierte Zielgruppen? %}
Zurzeit werden wertbasierte benutzerdefinierte Zielgruppen von Braze nicht unterstützt. Wenn Sie daran interessiert sind, diese Art von benutzerdefinierten Zielgruppen zu synchronisieren, senden Sie uns Ihr [Produkt-Feedback]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% enddetails %}

{% details Wie löse ich ein Problem bei der Synchronisierung einer wertbasierten Lookalike-Zielgruppe? %}

Zurzeit werden wertbasierte Lookalike-Zielgruppen von Braze nicht angenommen. Wenn Sie versuchen, mit dieser Zielgruppe zu synchronisieren, kann dies zu Fehlern bei Ihrem Audience Sync-Schritt führen. Führen Sie die folgenden Schritte aus, um dieses Problem zu lösen:

1. Gehen Sie zu Ihrem Facebook Ad Manager Dashboard und wählen Sie **Zielgruppen**.
2. Wählen Sie **Zielgruppe erstellen** > **Benutzerdefinierte Zielgruppe**.
3. Wählen Sie **Kundenliste**.
4. Laden Sie Ihre CSV-Datei oder Liste ohne die Spalte **Wert** hoch. Wählen Sie **Nein, fahren Sie mit einer Kundenliste fort, die keinen Kundenwert enthält**.
5. Beenden Sie die Erstellung Ihrer benutzerdefinierten Zielgruppe.
6. Aktualisieren Sie in Braze den Schritt Facebook Audience Sync mit der von Ihnen erstellten benutzerdefinierten Zielgruppe.
{% enddetails %}

{% details Ich habe eine E-Mail erhalten, die sich auf die Nutzungsbedingungen von Facebook für benutzerdefinierte Zielgruppen bezieht. Was sollte ich tun, um dieses Problem zu lösen? %}
Um Audience Sync to Facebook zu nutzen, müssen Sie diese Nutzungsbedingungen akzeptieren. 

- Wenn Ihr Anzeigenkonto direkt mit Ihrem persönlichen Facebook-Konto verknüpft ist, können Sie die ANB von Ihrem persönlichen Konto aus hier akzeptieren: `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=ACCOUNT_ID`.
- Wenn Ihr Anzeigenkonto mit dem Business Manager-Konto Ihres Unternehmens verknüpft ist, müssen Sie die AGB in Ihrem Business Manager-Konto hier akzeptieren: `https://business.facebook.com/customaudiences/value_based/tos.php?act=ACCOUNT_ID&business_id=BUSINESS_ID`.

Nachdem Sie die Nutzungsbedingungen für Ihre benutzerdefinierte Facebook-Zielgruppe akzeptiert haben, gehen Sie wie folgt vor:
1. Aktualisieren Sie Ihr Facebook-Zugangstoken mit Braze, indem Sie die Verbindung zu Ihrem Facebook-Konto trennen und wiederherstellen.
2. Aktivieren Sie den Schritt Facebook Audience Sync erneut, indem Sie Ihr Canvas bearbeiten und aktualisieren.
Braze wird dann in der Lage sein, Nutzer zu synchronisieren, sobald sie die Facebook-Publikumsstufe erreichen.
{% enddetails %}


[0]: https://www.braze.com/privacy
[1]: https://www.facebook.com/business/help/113163272211510
[2]: https://www.facebook.com/business/help/910137316041095
[3]: https://www.facebook.com/ads/manage/customaudiences/tos.php
[4]: {% image_buster /assets/img/fb/afb_1.png %}
[5]: {% image_buster /assets/img/fb/afb_2.png %}
[6]: {% image_buster /assets/img/fb/afb_3.png %}
[7]: {% image_buster /assets/img/fb/afb_4.png %}
[8]: {% image_buster /assets/img/fb/afb_5.png %}
[9]: {% image_buster /assets/img/fb_audience_sync/audience_history.png %}
[10]: {% image_buster /assets/img/fb_audience_sync/analytics_example.jpg %}
[11]: {% image_buster /assets/img/fb_audience_sync/add_step.png %}
[12]: {% image_buster /assets/img/fb_audience_sync/add_audience.png %}
[13]: {% image_buster /assets/img/fb_audience_sync/create_audience.png %}
[14]: {% image_buster /assets/img/fb_audience_sync/new_audience.png %}
[15]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}
[21]: {% image_buster /assets/img/audience_sync/fb_sync.png %}
[22]: {% image_buster /assets/img/audience_sync/fb_sync2.png %}
[23]: {% image_buster /assets/img/audience_sync/fb_sync3.png %}
