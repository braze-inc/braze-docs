---
nav_title: Facebook
article_title: Canvas Audience Sync mit Facebook
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie Braze Audience Sync für Facebook verwenden, um Anzeigen auf der Grundlage von verhaltensbezogenen Triggern, Segmentierung und mehr zuzustellen."
page_order: 2
alias: /audience_sync_facebook/

Tool:
  - Canvas

---

# Zielgruppe Synchronisierung mit Facebook

> Mit der Braze Audience Sync to Facebook können Sie die Daten Ihrer Nutzer:in aus Ihrer Braze Integration zu den angepassten Zielgruppen von Facebook hinzufügen, um Anzeigen auf der Grundlage von Verhaltenstriggern, Segmentierung und mehr zu liefern.

Alle Kriterien, die Sie normalerweise verwenden, um eine Nachricht (Push, E-Mail, SMS oder Webhook) in einem Braze-Canvas auf der Grundlage Ihrer Benutzerdaten auszulösen, können jetzt verwendet werden, um mit angepassten Zielgruppen eine Anzeige für diesen Benutzer in Facebook auszulösen. Wenn Sie beispielsweise eine Audience-Synchronisierung mit Facebook konfigurieren, können Sie eine Vielzahl von Erstanbieterfeldern wie E-Mail, Telefon, Vorname und Nachname verwenden.

**Zu den häufigen Anwendungsfällen für die Synchronisierung angepasster Zielgruppen gehören**:

- Targeting von hochwertigen Nutzer:innen über mehrere Kanäle, um Käufe oder Engagement zu fördern.
- Retargeting von Nutzer:innen, die auf andere Marketing-Kanäle weniger responsiv sind.
- Erstellen von Zielgruppen, um zu verhindern, dass Nutzer:innen, die bereits treue Verbraucher:innen Ihrer Marke sind, Werbung erhalten.
- Erstellen Sie ähnliche Zielgruppen, um neue Nutzer:innen effizienter zu gewinnen.

Mit diesem Feature können Marken kontrollieren, welche spezifischen First-Party-Daten mit Facebook geteilt werden. Bei Braze werden die Integrationen, mit denen Sie Ihre First-Party-Daten teilen können und nicht teilen können, genauestens berücksichtigt. Weitere Informationen finden Sie in unserer [Richtlinie zum Datenschutz](https://www.braze.com/privacy).

## Überlegungen zur Synchronisierung von Nutzer:innen und Rate-Limits
 
Wenn Nutzer:innen den Audience Sync-Schritt erreichen, wird Braze diese Zielgruppen nahezu in Realtime synchronisieren und dabei die Rate-Limits der Facebook Marketing API beachten. In der Praxis bedeutet dies, dass Braze versuchen wird, alle 5 Sekunden so viele Nutzer:innen wie möglich zu verarbeiten, bevor diese an Facebook weitergeleitet werden. 

Das Rate-Limits der Marketing API von Facebook besagt, dass innerhalb einer Stunde nicht mehr als ~190.000 API-Anfragen für jedes Anzeigenkonto gestellt werden dürfen. Erreicht eine Braze-Kund:in dieses Rate-Limit, wird Braze-Canvas die Synchronisierung für bis zu ~13 Stunden wiederholen. Wenn die Synchronisierung nicht möglich ist, werden diese Nutzer:innen unter der Metriken Users Errored aufgeführt.

## Voraussetzungen

Bevor Sie den Facebook Audience-Schritt in Canvas einrichten, müssen Sie sicherstellen, dass Sie die folgenden Artikel erstellt und abgeschlossen haben. 

| Anforderung | Herkunft | Beschreibung |
| ----------- | ------ | ----------- |
| Facebook Business Manager:in | [Facebook](https://www.facebook.com/business/help/113163272211510) | Ein zentrales Tool zur Verwaltung der Facebook-Assets Ihrer Marke (z.B. Werbekonten, Seiten und Apps). |
| Facebook Werbekonto | [Facebook](https://www.facebook.com/business/help/910137316041095) | Ein aktives Facebook-Anzeigenkonto, das an den Business Manager Ihrer Marke gebunden ist.<br><br>Vergewissern Sie sich, dass Ihr Facebook Business Manager-Administrator Ihnen entweder die Berechtigung "Kampagnen verwalten" oder "Anzeigenkonten verwalten" für die Facebook-Anzeigenkonten erteilt hat, die Sie mit Braze verwenden möchten. Vergewissern Sie sich außerdem, dass Sie die Geschäftsbedingungen für Ihr Anzeigenkonto akzeptiert haben. |
| Facebook angepasste Zielgruppen Bedingungen | [Facebook](https://www.facebook.com/ads/manage/customaudiences/tos.php) | Akzeptieren Sie die Facebook-Bedingungen für angepasste Zielgruppen für Ihre Facebook-Anzeigenkonten, die Sie mit Braze verwenden möchten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

### Schritt 1: Mit Facebook verbinden

Gehen Sie im Braze-Dashboard zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Facebook** aus. Wählen Sie unter Facebook Audience Export die Option **Facebook verbinden**.

![Facebook-Technologie-Seite in Braze mit einer Übersicht und einem Abschnitt für den Export von Facebook Audience mit dem Button Verbunden mit Facebook.]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:85%;"}

Es erscheint ein Facebook oAuth-Dialogfenster, um Braze zu autorisieren, angepasste Zielgruppen in Ihren Facebook-Anzeigenkonten zu erstellen.

![Das erste Facebook-Dialogfeld mit der Aufforderung "Verbinden Sie sich als X", wobei X Ihr Facebook-Benutzername ist.]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"}  ![Das zweite Facebook-Dialogfeld mit der Aufforderung, Anzeigen für Ihre Werbekonten verwalten zu dürfen.]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

Nachdem Sie Braze mit Ihrem Facebook-Konto verknüpft haben, wählen Sie die Anzeigenkonten aus, die Sie in Ihrem Braze Workspace synchronisieren möchten. Wenn Sie verbunden sind, gelangen Sie zurück zur Partnerseite, wo Sie sehen können, welche Konten verbunden sind, und wo Sie bestehende Konten trennen können.

![Eine aktualisierte Version der Technologie-Partnerseite von Facebook, auf der die erfolgreich verbundenen Werbekonten angezeigt werden.]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:85%;"}

Ihre Facebook-Verbindung wird auf der Ebene des Braze Workspace angewendet. Wenn Ihr Facebook-Administrator Sie von Ihrem Facebook Business Manager oder dem Zugriff auf die verbundenen Facebook-Konten entfernt, erkennt Braze ein ungültiges Token. Infolgedessen werden Ihre aktiven Canvase, die Facebook Audience-Komponenten verwenden, Fehler anzeigen, und Braze kann die Nutzer:innen nicht synchronisieren. 

{% alert important %}
Für Nutzer:in, die zuvor den Facebook App Review-Prozess für [Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) und [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/access#standard) durchlaufen haben, ist Ihr System User Token weiterhin für die Facebook Audience-Komponente gültig. Sie können das Facebook System User Token nicht über die Partnerseite von Facebook bearbeiten oder widerrufen. Stattdessen können Sie Ihr Facebook-Konto verbinden, um Ihr Facebook System User Token innerhalb Ihres Braze Workspace zu ersetzen. 

<br><br>Die Facebook oAuth-Konfiguration gilt auch für [Facebook-Exporte mit Segmenten]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites).
{% endalert %}

### Schritt 2: Akzeptieren Sie angepasste Zielgruppen Bedingungen für den Dienst

Bevor Sie Ihr Canvas einrichten, müssen Sie die folgenden Nutzungsbedingungen von Facebook unter den folgenden Links akzeptieren:

- **Kundenliste Angepasste Zielgruppen Bedingungen für Ihr persönliches Konto:** `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- **Facebook Business Tools Bedingungen für Ihr Geschäftskonto:** `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

![Ein Beispiel für die Bedingungen, die für angepasste Zielgruppen in der Kund:in akzeptiert werden müssen.]({% image_buster /assets/img/fb_audience_sync/fb_sync_tos.png %}){: style="max-width:85%;"}
![Ein Beispiel für die Bedingungen, die Sie für Facebook Business Tools akzeptieren müssen.]({% image_buster /assets/img/fb_audience_sync/fb_sync_tos2.png %}){: style="max-width:85%;"}

Weitere Einzelheiten zur Überprüfung Ihres Facebook-Kontos bei der Integration finden Sie im [Abschnitt FAQ](#terms).

### Schritt 3: Hinzufügen einer Facebook Audience Komponente in Canvas Flow

Fügen Sie eine Komponente in Ihrem Canvas hinzu und wählen Sie **Facebook Audience** aus.

![Eine Liste von Komponenten, die dem Canvas hinzugefügt werden können.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![Die Audience Sync Komponente.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Schritt 4: Sync-Einrichtung

Wählen Sie den Button **Angepasste Zielgruppe** aus, um den Komponenteneditor zu öffnen. Wählen Sie dann **Facebook** als Partner für die Audience Sync aus.

!["Audience Sync einrichten" mit Optionen zur Auswahl eines Partners.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Wählen Sie das gewünschte Facebook-Anzeigenkonto aus. Geben Sie in der Dropdown-Liste **Neue oder bestehende Zielgruppe auswählen** den Namen einer neuen oder bestehenden Zielgruppe ein. 

{% tabs %}
{% tab Eine neue Zielgruppe erstellen %}

1. Geben Sie einen Namen für die neue angepasste Zielgruppe ein.
2. Wählen Sie **Nutzer:innen zur Zielgruppe hinzufügen** und wählen Sie die Felder aus, die Sie mit Facebook synchronisieren möchten. 
3. Wählen Sie dann **Zielgruppe erstellen**, um Ihre Zielgruppe zu speichern.

![Einrichtung der Zielgruppen-Synchronisierung für eine Zielgruppe mit den entsprechenden Informationen zu E-Mail, Telefon, Vorname und Nachname.]({% image_buster /assets/img/audience_sync/fb_sync.png %})

Sie werden oben im Schritt-Editor benachrichtigt, wenn die Zielgruppe erfolgreich erstellt wurde oder wenn während dieses Vorgangs ein Fehler auftritt. Sie können diese Zielgruppe auch referenzieren, wenn Nutzer:in später in der Canvas-Reise entfernt werden, da die Zielgruppe im Entwurfsmodus erstellt wurde.

Wenn Sie ein Canvas mit einer neuen Zielgruppe starten, erstellt Braze die neue angepasste Zielgruppe beim Start des Canvas und synchronisiert die Nutzer:innen anschließend nahezu in Realtime, wenn sie den Schritt zur Synchronisierung der Zielgruppe betreten.

{% endtab %}
{% tab Mit einer bestehenden Zielgruppe synchronisieren %}

Braze bietet die Möglichkeit, Nutzer:innen aus bestehenden angepassten Facebook Zielgruppen hinzuzufügen oder zu entfernen, um zu bestätigen, dass diese Zielgruppen aktuell sind. Um sich mit einer bestehenden Zielgruppe zu synchronisieren, gehen Sie wie folgt vor:

1. Geben Sie den Namen der bestehenden Zielgruppe in die Dropdown-Liste ein.
2. Wählen Sie, ob Sie **der Zielgruppe etwas hinzufügen** oder **aus der Zielgruppe entfernen** möchten. 
3. Braze fügt Nutzer:innen nahezu in Realtime hinzu oder entfernt sie, sobald sie die Facebook Audience betreten. 

![Einrichtung der Zielgruppen-Synchronisation zum Entfernen der Informationen zu E-Mail, Telefon, Vorname und Nachname.]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

{% alert important %}
Facebook verbietet es, Nutzer:innen aus angepassten Zielgruppen zu entfernen, wenn die Zielgruppen zu klein sind (in der Regel weniger als 1.000 Nutzer:innen). Infolgedessen kann Braze Nutzer:innen für eine Entfernung aus dem Schritt Audience Sync nicht synchronisieren, bis die Zielgruppe die entsprechende Zielgruppengröße erreicht hat.
{% endalert %}

{% endtab %}
{% endtabs %}

### Schritt 5: Canvas starten

Nachdem Sie Ihre Facebook Audience-Komponente konfiguriert haben, ist es an der Zeit, das Canvas zu starten! Die neue angepasste Zielgruppe wird erstellt, und Nutzer:innen, die den Schritt Facebook Audience durchlaufen, werden in diese angepasste Zielgruppe auf Facebook weitergeleitet. Wenn Ihr Canvas nachfolgende Schritte enthält, werden Ihre Nutzer:innen zum nächsten Schritt in ihrer User Journey voranbringen.

Der Tab **Verlauf** der angepassten Zielgruppe im Facebook Audience Manager zeigt die Anzahl der Nutzer:innen an, die von Braze an die Zielgruppe gesendet wurden. Wenn ein Nutzer:innen den Schritt erneut betritt, wird er erneut zu Facebook weitergeleitet.

![Details zur Zielgruppe und der Tab Verlauf für eine bestimmte Facebook Zielgruppe, der eine Tabelle Verlauf der Zielgruppe mit Spalten für die Aktivität, Aktivitätsdetails, geänderte Artikel sowie Datum und Uhrzeit enthält.]({% image_buster /assets/img/fb_audience_sync/audience_history.png %}){: style="max-width:80%;"}

## Analytics verstehen

Die folgende Tabelle enthält Metriken und Beschreibungen, die Ihnen helfen, die Analytics Ihrer Audience Sync-Komponente besser zu verstehen.

| Metrisch | Beschreibung |
| --- | --- |
| Eingetreten | Anzahl der Nutzer:innen, die diese Komponente eingegeben haben, um mit Facebook synchronisiert zu werden. |
| Fortgefahren mit nächstem Schritt | Wie viele Nutzer:innen zur nächsten Komponente vorgebracht wurden, falls es eine gibt. Alle Nutzer:innen werden automatisch vorangebracht, wenn dies der letzte Schritt im Canvas-Zweig ist. |
| Nutzer:innen synchronisiert | Anzahl der Nutzer:innen, die erfolgreich mit Facebook synchronisiert wurden. |
| Nutzer:innen nicht synchronisiert | Anzahl der Nutzer:innen, die nicht synchronisiert wurden, weil Felder zum Abgleich fehlen. Die Felder werden mit einem "OR"-Operator abgeglichen, d.h. solange ein Nutzer:in eines der Felder in Facebook eingetragen ist, wird Facebook den Nutzer:in abgleichen, auch wenn es keine Übereinstimmung in allen anderen Feldern gibt. |
| Nutzer:innen ausstehend | Anzahl der Nutzer:innen, die derzeit von Braze für die Synchronisierung mit Facebook bearbeitet werden. |
| Fehler bei Nutzer:innen | Anzahl der Nutzer:innen, die aufgrund eines API-Fehlers nach etwa 13 Stunden nicht mit Facebook synchronisiert wurden. Mögliche Fehlerursachen können ein ungültiges Facebook Token sein oder wenn die angepasste Zielgruppe auf Facebook gelöscht wurde. |
| Canvas wurde verlassen | Anzahl der Nutzer:innen, die den Canvas verlassen haben. Dies geschieht, wenn der letzte Schritt in einem Canvas ein Facebook-Schritt ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Bei den Metriken für synchronisierte Nutzer:innen und Nutzer:innen mit Fehlern kommt es aufgrund der internen Verarbeitung zu einer Verzögerung bei der Berichterstattung.
{% endalert %}

## Häufig gestellte Fragen

### Wie lange dauert es, bis meine Zielgruppen in meinem Audience Sync Partner Dashboard angezeigt werden?

Wie lange es dauert, eine Zielgruppe zu bevölkern, hängt von dem jeweiligen Partner ab. Alle Netzwerke werden die Anfragen von Braze verarbeiten und versuchen, Nutzer:innen zu finden. Es kann bis zu 24 Stunden dauern, bis die angepassten Zielgruppen aktualisiert sind.

### Was sollte ich als nächstes tun, wenn ich den Fehler eines ungültigen Tokens erhalte?

Sie können Ihr Facebook-Konto auf der Facebook Partnerseite einfach trennen und wieder verbinden. Vergewissern Sie sich bei Ihrem Facebook Business Manager-Administrator, dass Sie die entsprechenden Berechtigungen für das Anzeigenkonto haben, mit dem Sie synchronisieren möchten.

### Warum ist es nicht zulässig, meinen Canvas zu starten?

- Vergewissern Sie sich, dass Ihr System Nutzer:in authentifiziert ist und Zugriff auf die gewünschten Anzeigenkonten im Facebook Business Manager hat.
- Vergewissern Sie sich, dass Sie ein Anzeigenkonto ausgewählt, einen Namen für die neue angepasste Zielgruppe eingegeben und die entsprechenden Felder ausgewählt haben.
- Möglicherweise haben Sie das Limit von 500 angepassten Zielgruppen auf Facebook erreicht. Gehen Sie zum Facebook Audience Manager, um einige nicht benötigte Zielgruppen zu löschen, bevor Sie neue angepasste Zielgruppen mit Canvas erstellen.

### Woher weiß ich, ob sich Nutzer:innen gefunden haben, nachdem ich Nutzer:innen an Facebook weitergegeben habe?

Facebook stellt diese Informationen aus Gründen des Datenschutzes nicht zur Verfügung.

### Unterstützt Braze wertorientierte angepasste Zielgruppen?

Derzeit werden wertbasierte angepasste Zielgruppen von Braze nicht unterstützt. Wenn Sie daran interessiert sind, diese Arten von angepassten Zielgruppen zu synchronisieren, senden Sie uns Ihr [Produkt-Feedback]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

### Verschlüsselt Braze Daten, bevor es sie an Audience Sync Partner sendet?

Sobald die E-Mail-Daten normalisiert sind, hasst Braze sie mit SHA256.

**IDFA/AAID/phone:** Braze hasht mit SHA256. Die Zielgruppen, die wir synchronisieren, sind immer eine der folgenden:

- IDFA_SHA256
- AAID_SHA256
- EMAIL_SHA256
- PHONE_SHA256\.

Was die Häufigkeit betrifft, so wird Braze nur dann personenbezogene Daten (PII) von Nutzern:innen hacken, wenn diese den Schritt der Audience Sync in der User Journey zur Vorbereitung der Synchronisierung betreten.

### Wie löse ich ein Problem bei der Synchronisierung einer wertbasierten, angepassten Zielgruppe?

Derzeit werden von Braze keine wertorientierten, angepassten Zielgruppen erwartet. Wenn Sie versuchen, mit dieser Zielgruppe zu synchronisieren, kann dies zu Fehlern bei Ihrem Schritt der Zielgruppensynchronisierung führen. Führen Sie die folgenden Schritte aus, um dieses Problem zu lösen:

1. Gehen Sie zu Ihrem Facebook Ad Manager Dashboard und wählen Sie **Zielgruppen**:in.
2. Wählen Sie **Zielgruppe erstellen** > Angepasste **Zielgruppe.**
3. Wählen Sie **Kundenliste** aus.
4. Laden Sie Ihre CSV-Datei oder Liste ohne die Spalte **Wert** hoch. Wählen Sie **Nein, fahren Sie mit einer Kundenliste fort, die keinen Kundenwert enthält**.
5. Beenden Sie die Erstellung Ihrer angepassten Zielgruppe.
6. Aktualisieren Sie in Braze den Schritt Facebook Audience Sync mit der angepassten Zielgruppe, die Sie erstellt haben.

### Ich habe eine E-Mail zu den Nutzungsbedingungen für angepasste Zielgruppen von Facebook erhalten. Was sollte ich tun, um dieses Problem zu lösen?

Um Audience Sync to Facebook nutzen zu können, müssen Sie diese Vereinbarung über die Bedingungen des Dienstes akzeptieren. 

- Wenn Ihr Anzeigenkonto direkt mit Ihrem persönlichen Facebook-Konto verknüpft ist, können Sie die Bedingungen für den Dienst von in Ihrem persönlichen Konto hier akzeptieren: `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- Wenn Ihr Anzeigenkonto mit dem Business Manager-Konto Ihres Unternehmens verknüpft ist, müssen Sie die Bedingungen für den Dienst in Ihrem Facebook Business Manager-Konto hier akzeptieren: `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

Nachdem Sie die Nutzungsbedingungen für Ihre angepasste Facebook Zielgruppe akzeptiert haben, gehen Sie wie folgt vor:

1. Aktualisieren Sie Ihr Facebook Token mit Braze, indem Sie die Verbindung zu Ihrem Facebook-Konto trennen und erneut herstellen.
2. Aktivieren Sie Ihren Facebook Audience Sync-Schritt wieder, indem Sie Ihr Canvas bearbeiten und aktualisieren.

Dann kann Braze die Nutzer:innen synchronisieren, sobald sie den Schritt Facebook Audience Sync erreichen.

## Fehlersuche

<style>
table th:nth-child(1) {
    width: 20%;
}
table th:nth-child(2) {
    width: 40%;
}
table th:nth-child(2) {
    width: 40%;
}
table td {
    word-break: break-word;
}
</style>

<table>
  <thead>
    <tr>
      <th>Fehler</th>
      <th>Beschreibung</th>
      <th>Schritte zur Klärung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Ungültiges Token</b></td>
      <td>Typische Ursachen sind, wenn der Nutzer:innen, der die Integration verbunden hat, sein Passwort ändert, Zugangsdaten ablaufen und mehr.</td>
      <td>Gehen Sie zu <b>Partnerintegrationen</b> > <b>Facebook</b> und trennen Sie die Verbindung zu Ihrem Konto und verbinden Sie es erneut. In <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>diesem Abschnitt zur Fehlerbehebung</a> finden Sie weitere Schritte zur Überprüfung Ihres Facebook-Kontos.</td>
    </tr>
    <tr>
      <td><b>Zielgruppe zu klein</b></td>
      <td>Dieser Fehler kann auftreten, wenn Sie einen Audience Sync-Schritt erstellt haben, der Nutzer:innen aus Ihren Zielgruppen entfernt. Wenn die Größe Ihrer Zielgruppe gegen Null geht, kann es sein, dass das Netzwerk feststellt, dass die Zielgruppe zu klein ist, um bedient zu werden.</td>
      <td> Verwenden Sie eine Strategie zur Synchronisierung von Zielgruppen, die regelmäßig Nutzer:innen hinzufügt und entfernt, ohne dass die Zielgruppengröße völlig erschöpft wird.</td>
    </tr>
    <tr>
      <td><b>Zielgruppe gibt es nicht</b></td>
      <td>Der Schritt Audience Sync verwendet eine Zielgruppe, die nicht existiert oder gelöscht wurde. Dies kann auch getriggert werden, wenn Sie nicht mehr über die erforderliche Berechtigung zum Zugriff auf die Zielgruppe verfügen.</td>
      <td>Lassen Sie einen Administrator auf der Partner-Plattform prüfen, ob die Zielgruppe noch existiert. <br><br>Falls vorhanden, prüfen Sie, ob der Nutzer:innen, der die Integration verbunden hat, über die Berechtigung für die Zielgruppe verfügt. Ist dies nicht der Fall, muss dem Nutzer:innen der Zugang zu dieser Zielgruppe gewährt werden. <br><br>Wenn die Zielgruppe absichtlich entfernt wurde, fügen Sie eine aktive Zielgruppe hinzu und erstellen eine neue Zielgruppe auf dem Schritt.</td>
    </tr>
    <tr>
      <td><b>Versuch eines Zugriffs auf ein Anzeigenkonto</b></td>
      <td>Sie haben keine Berechtigung für das von Ihnen ausgewählte Anzeigenkonto oder die Zielgruppe.</td>
      <td>Arbeiten Sie mit den Administratoren Ihres Anzeigenkontos zusammen, um den richtigen Zugang und die richtigen Berechtigungen zu erhalten.</td>
    </tr>
    <tr>
      <td><b>Bedingungen für Serviceleistungen Nicht akzeptiert</b></td>
      <td>Bei einigen Zielgruppen, wie z.B. Facebook, ist es für die Nutzung des Features Audience Sync erforderlich, dass das Werbenetzwerk bestimmte Dienste akzeptiert. Dieser Fehler wird ausgelöst, wenn Sie die entsprechenden Bedingungen nicht akzeptiert haben. Daher haben Sie vielleicht auch eine E-Mail mit diesem Betreff von Braze erhalten: "Ihre Zugangsdaten für Facebook sind ungültig."</td>
      <td>Prüfen Sie, ob Sie die erforderlichen Bedingungen von Facebook akzeptiert haben.</td>
    </tr>
    <tr>
      <td><b>Alle Nutzer:in sind fehlerhaft</b></td>
      <td>Wenn alle Nutzer:innen bei einem Schritt einen Fehler machen, obwohl Sie bestätigt haben, dass diese Nutzer:innen Werte für die ausgewählten Felder des Schritts haben, könnte dies auf ein Problem mit Ihrem Facebook-Konto hinweisen.</td>
      <td>Folgen Sie den Schritten in <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>diesem Abschnitt zur Fehlerbehebung</a>, um Ihr Konto auf Probleme zu überprüfen.
      </td>
    </tr>
    <tr>
      <td><b>Zielgruppe nicht erreicht</b></td>
      <td>Auf der Facebook Technologie-Partnerseite sehen Sie "Verbunden", aber im Schritt Facebook Audience Sync beim Synchronisieren einer Zielgruppe erscheint die Fehlermeldung "Failed to create audience "audience name". Die Autorisierung Ihres Facebook-Kontos ist fehlgeschlagen. Bitte besuchen Sie die Technologie-Partnerseite, um Ihr Konto erneut zu verbinden.</td>
      <td>Folgen Sie den Schritten in <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>diesem Abschnitt zur Fehlerbehebung</a>, um Ihr Konto auf Probleme zu überprüfen.
      </td>
    </tr>
  </tbody>
</table>

### Prüfen Sie Ihr Facebook-Konto

Wenn Sie weitere Probleme mit Ihrer Integration haben, lesen Sie die folgenden Abschnitte und Schritte zur Überprüfung Ihres Facebook-Kontos. 

#### Kontoberechtigungen überprüfen

1. Lesen Sie [in der Dokumentation von Facebook](https://www.facebook.com/business/help/186007118118684?id=829106167281625) nach, wie Sie diese Berechtigungen auf der Plattform verwalten können. Für Facebook Business Manager benötigen Sie mindestens die Rolle **Admin** oder **Employee** Business Manager mit Zugriff auf die erforderlichen Anzeigenkonten.
2. Bestätigen Sie als **Mitarbeiter**, dass der Administrator Ihnen für jedes Anzeigenkonto die volle Berechtigung zum **Verwalten von** Zielgruppen oder zum Synchronisieren von Nutzer:innen mit Zielgruppen erteilt. 
3. Nachdem dies geschehen ist, müssen Sie die Verbindung zu Ihrem Konto trennen und erneut herstellen.

#### Akzeptieren Sie die Bedingungen des Dienstes {#terms}

Akzeptieren Sie alle anstehenden Allgemeinen Geschäftsbedingungen (AGB) von Facebook. Facebook fordert Sie (den Nutzer:innen) und den Manager:in regelmäßig auf, die Bedingungen für den Dienst erneut zu genehmigen.

1. Der angeschlossene Nutzer:innen muss alle Bedingungen des Dienstes für jedes seiner Anzeigenkonten akzeptieren:
- Angepasste Audience TOS für Ihr persönliches Facebook-Konto:
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<AD_ACCOUNT_ID>`

![Ein Konto mit voller Kontrollbefugnis zur Verwaltung eines Anzeigenkontos.]({% image_buster /assets/img/fb_audience_sync/ad_account_permission.png %}){: style="max-width:70%;"}

Um Ihr Konto und Ihre ID zu finden, gehen Sie folgendermaßen vor:

1. Gehen Sie zu Ihrem [Facebook Ads Manager-Konto](https://adsmanager.facebook.com/):in.
2. Überprüfen Sie, ob Sie das richtige Anzeigenkonto verwenden, indem Sie es im Dropdown-Menü überprüfen.
3. Suchen Sie in der URL die Konto-ID nach `act=` und die ID des Unternehmens nach `business_id=`

![Die URL mit der hervorgehobenen Konto-ID und Geschäfts-ID.]({% image_buster /assets/img/fb_audience_sync/fb_businessid_url.png %}){: style="max-width:90%;"}

{:start="4"}

4. Lesen Sie die Bedingungen für angepasste Zielgruppen und wählen Sie **Akzeptieren** aus. Wir empfehlen Ihnen, sich zu vergewissern, für welches Konto die Bedingungen des Dienstes unterzeichnet werden, indem Sie die Dropdown-Liste oben in den Bedingungen verwenden.

![Die Auswahlliste, die das Konto anzeigt, das die Bedingungen des Dienstes unterzeichnet.]({% image_buster /assets/img/fb_audience_sync/confirm_accept_tos.png %}){: style="max-width:90%;"}

{:start="5"}
5\. Sie müssen **Akzeptieren** für die Bedingungen der Dienste auswählen. Danach sehen Sie diese Nachricht: "Sie haben diese Bedingungen für den Dienst im Namen von Braze akzeptiert".
6\. Aktualisieren Sie Ihr Facebook Token mit Braze, indem Sie die Verbindung zu Ihrem Facebook-Konto trennen und erneut herstellen.
7\. Aktivieren Sie Ihren Facebook Audience Sync-Schritt wieder, indem Sie Ihr Canvas bearbeiten und aktualisieren. Braze kann dann Nutzer:innen synchronisieren, sobald sie den Schritt „Facebook-Zielgruppe“ erreichen.
8\. Wenn das Problem weiterhin besteht, versuchen Sie, einen separaten Nutzer:in mit Administratorrechten zu verwenden, um die Bedingungen manuell über den Manager:in für Anzeigen zu akzeptieren.

#### Erledigen Sie alle anstehenden Aufgaben 

Prüfen Sie, ob Sie irgendwelche offenen Aufgaben bei Facebook haben, die Sie daran hindern könnten, die Dienste von Facebook Ads zu nutzen:

1. [Melden Sie sich beim Facebook Ads Manager an](https://adsmanager.facebook.com/).
2. Wählen Sie das Anzeigenkonto aus, mit dem Sie Probleme haben.
3. Wählen Sie in der Navigation Ihre **Kontoübersicht** aus. <br> ![Die Navigation mit ausgewählter Kontoübersicht.]({% image_buster /assets/img/fb_audience_sync/ads_manager_accouint_overview.png %})
4. Prüfen Sie, ob es Warnmeldungen gibt, die behoben werden müssen. <br> ![Ein Konto mit einer abgelaufenen Kreditkarte.]({% image_buster /assets/img/fb_audience_sync/resolve_alerts.png %})

{:start="5"}

5. Prüfen Sie, ob es Setup-Aufgaben gibt, die erledigt werden müssen. <br> ![Ein Konto mit einer teilweise abgeschlossenen Kontoeinrichtung.]({% image_buster /assets/img/fb_audience_sync/confirm_tasks.png %})

#### Mit einem anderen Nutzer:in verbinden

Als weitere Fehlerbehebung empfehlen wir, dass ein anderer Nutzer:innen versucht, sein Konto zu verbinden, indem er Folgendes tut:

1. Trennen Sie die Currents-Integration.
2. Ein separater Nutzer:innen mit Admin-Rechten verbindet ihr Facebook-Benutzerkonto.

