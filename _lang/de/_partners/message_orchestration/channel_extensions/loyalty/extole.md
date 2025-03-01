---
nav_title: Extole
article_title: Extole
description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze und Extole, einem Unternehmen für Empfehlungsmarketing, das es Ihnen ermöglicht, Kundenereignisse und -attribute aus Freundschaftswerbungs- und Wachstumsprogrammen in Braze zu übernehmen."
alias: /partners/extole/
page_type: partner
search_tag: Partner

---

# Extole

> [Extole](https://www.extole.com/), ein SaaS-Unternehmen, ist branchenführend im Empfehlungsmarketing und hilft bei der Erstellung und Optimierung effektiver Empfehlungsmarketingprogramme zur Steigerung der Kundenakquise.

Mit der Integration von Braze und Extole können Sie Kundenereignisse und -attribute aus Extole-Werbe- und Wachstumsprogrammen in Braze übernehmen. So können Sie personalisierte Marketingkampagnen erstellen, die die Kundenakquise, -bindung und -treue fördern. Sie können auch Extole-Inhaltsattribute wie personalisierte Freigabecodes und Links dynamisch in die Braze-Kommunikation übernehmen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Extole-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Extole-Konto. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit der Berechtigung `users.track`. Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze API URL | Ihre Braze-API-URL ist spezifisch für Ihre [Braze-Instanz]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Die folgenden Anwendungsfälle zeigen einige Möglichkeiten, wie Sie die Integration von Extole mit Braze nutzen können. Arbeiten Sie mit Ihren Extole-Implementierungs- und Kundenerfolgsmanagern zusammen, um eine Option zu entwickeln, die den spezifischen Anforderungen Ihres Unternehmens entspricht.

- Nutzen Sie benutzerdefinierte Ereignisse aus Ihren Empfehlungs- und Engagementprogrammen, um eine Braze-Kampagne oder ein Canvas auszulösen.
- Erstellen Sie benutzerdefinierte Segmente, Dashboards und Berichte mit Daten aus Ihren Extole-gestützten Programmen.
- Automatische Abmeldung oder Eintragung von Benutzern in Ihre Marketingliste in Braze

## Integration

Führen Sie die folgenden Schritte aus, um Ihre Integration schnell zum Laufen zu bringen. Ihre Extole-Implementierungs- und Kundenerfolgsmanager werden Sie während dieses Prozesses unterstützen und alle Ihre Fragen beantworten.

### Verbinden Sie sich mit Ihrem Braze-Konto

1. Wählen Sie die Braze-Integration auf der [Partnerseite](https://my.extole.com/partners) Ihres My Extole-Kontos.
2. In der Braze-Integration wählen Sie **Installieren**, um die Verbindung zwischen Extole und Braze zu initiieren.
3. Füllen Sie die erforderlichen Felder aus, beginnend mit Ihrem Braze REST API-Schlüssel. 
4. Geben Sie Ihre Braze API URL ein. Diese URL hängt davon ab, auf welcher Instanz Ihr Braze-Konto eingerichtet ist.
5. Fügen Sie alle Extole-Ereignisse hinzu, die Sie an Braze senden möchten. Die Standardereignisse, Ereigniseigenschaften und Benutzerattribute sind in der [Tabelle Extole-Ereignisse](https://dev.extole.com/docs/braze#extole-program-events) beschrieben.
6. Fügen Sie alle Reward-Status hinzu, die Sie an Braze senden möchten, außer dem Status `FULFILLED`. In der [Tabelle Extole Rewards](https://dev.extole.com/docs/braze#extole-rewards) finden Sie eine Beschreibung der verfügbaren Reward-Status.
7. Wählen Sie die Zuordnung Ihrer externen Braze ID-Taste. So aktualisiert Extole die Benutzerprofile in Braze. Sie können den externen ID-Schlüssel von Braze der `email_address` oder `partner_user_id` von Extole für den Benutzer zuordnen. Wir empfehlen die Verwendung von `external_id` anstelle von `email_address`, da dies sicherer ist.
8. Speichern Sie Ihre Einstellungen, um die Verbindung abzuschließen. Jetzt können Extole-Ereignisse in Ihr Braze-Konto fließen.

### Extole Programm Ereignisse

Im Folgenden finden Sie die Standardereignisse, Ereigniseigenschaften und Benutzerattribute, die Extole an Braze sendet. Wenden Sie sich an Ihre Extole-Implementierungs- oder Kundenerfolgsmanager, um zusätzliche Extole-Ereignisse zu identifizieren und zu Ihrer Integration hinzuzufügen.

| Event | Beschreibung | Event-Eigenschaften | Nutzerattribute |
| ----------- | ----------- | ----------- | ----------- |
| `extole_created_share_link` | Ein Teilnehmer erstellt seinen Share-Link, indem er seine E-Mail-Adresse in das Extole Share Experience eingibt. | Event-Name  <br>Zeit der Veranstaltung  <br>Partner (Extole)  <br>Trichter (Fürsprecher oder Freund)  <br>Programm | <br>Externe ID <br>E-Mail  <br>Link teilen |
| `extole_shared` | Ein Teilnehmer teilt seinen Empfehlungslink mit einem Freund. | Event-Name  <br>Zeit der Veranstaltung  <br>Partner (Extole)  <br>Externe ID  <br>Trichter (Fürsprecher oder Freund)  <br>Programm  <br>Kanal teilen | E-Mail <br>Vorname <br>Nachname |
| `outcome` - Das Ergebnis ist dynamisch und hängt von der Konfiguration Ihres Programms ab (z.B. `extole_shipped`, `extole_converted`).| Ein Teilnehmer hat das für das Programm konfigurierte Ereignis mit dem gewünschten Ergebnis umgewandelt oder abgeschlossen. | Dynamisch pro Programm | E-Mail <br>Vorname <br>Nachname |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Extole Abo-Status

| Abonnement-Status | Beschreibung | Event-Eigenschaften | Nutzerattribute |
| ----------- | ----------- | ----------- | ----------- |
| `subscribed` | Ein Teilnehmer hat sich für den Erhalt von Marketingnachrichten entschieden. | -- | E-Mail  <br>Liste Typ  <br>Externe ID  <br>E-Mail-Abonnement (abonniert) |
| `unsubscribed` | Ein Teilnehmer hat sich gegen den Erhalt von Extole E-Mail-Nachrichten entschieden.| E-Mail  <br>Externe ID  <br>Status des Abonnements (abgemeldet)  <br>ID der Abonnementgruppe  | Liste Typ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Extole Belohnungen

Standardmäßig sendet Extole Belohnungsereignisse im Status `FULFILLED` an Braze, so dass Sie Belohnungsbenachrichtigungen über eine Braze-Kampagne oder Canvas auslösen können. In der folgenden Tabelle finden Sie weitere Reward-Status.

| Belohnung Staat | Beschreibung | Event-Eigenschaften | Nutzerattribute |
| ----------- | ----------- | ----------- | ----------- |
| `FULFILLED` | Der Standardstatus. Der Prämie wurde von einem Extole Prämienanbieter ein Wert zugewiesen (z.B. ein Gutschein oder eine Geschenkkarte). | E-Mail <br>Nennwert  <br>Gutscheincode  <br>Nennwert Typ  | E-Mail <br>Vorname  <br>Nachname |
| `EARNED` | Es wurde eine Belohnung erstellt und mit einer Person verknüpft. | E-Mail <br>Nennwert  <br>Gutscheincode  <br>Nennwert Typ  | E-Mail <br>Vorname  <br>Nachname |
| `SENT` | Die Prämie wurde erfüllt und wurde entweder per E-Mail oder auf einem Gerät an den Empfänger gesendet. | E-Mail <br>Nennwert  <br>Gutscheincode  <br>Nennwert Typ  | E-Mail <br>Vorname  <br>Nachname |
| `REDEEMED` | Die Prämie wurde vom Empfänger verwendet, was durch ein an Extole gesendetes Umwandlungs- oder Einlösungsereignis belegt wird.| E-Mail <br>Nennwert  <br>Gutscheincode  <br>Nennwert Typ  | E-Mail <br>Vorname  <br>Nachname |
| `FAILED` | Ein Problem hat die Ausgabe oder den Versand der Belohnung verhindert und muss behoben werden. | E-Mail <br>Nennwert  <br>Gutscheincode  <br>Nennwert Typ  | E-Mail <br>Vorname  <br>Nachname |
| `CANCELED` | Die Belohnung wurde deaktiviert und wird ins Inventar zurückkehren. | E-Mail <br>Nennwert  <br>Nennwert Typ  | E-Mail <br>Vorname  <br>Nachname |
| `REVOKED` | Die erfüllte Belohnung ist ungültig geworden. Extole hat zum Beispiel eine Geschenkkarte eines Lieferanten angefordert und dann festgestellt, dass die Karte irrtümlich verschickt wurde. Wenn der Anbieter den Widerruf der Prämie unterstützt, fordert Extole das Geld zurück und die Prämie ist nicht mehr gültig. | E-Mail <br>Nennwert   <br>Nennwert Typ  | E-Mail <br>Vorname  <br>Nachname |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }


## Anpassung

### Benutzer in Braze suchen und erstellen

Für bestimmte Anwendungsfälle, wie z.B. ein neues E-Mail- oder SMS-Abonnement, für das Extole keine externe ID (Benutzer-ID) hat, kann Extole mit dem [Endpunkt]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) Braze [Export user profile by identifier]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) nach der Kennung des Benutzers suchen. Extole wird alle Profilattribute hinzufügen und aktualisieren, wenn der Benutzer in Braze existiert. Wenn die Anfrage kein Benutzerprofil zurückgibt, verwendet Extole den Endpunkt `/users/track`, um einen Benutzeralias mit der E-Mail-Adresse des Benutzers als Aliasnamen zu erstellen.

## Mit dieser Integration

Nachdem Sie Ihre Konten miteinander verbunden haben, fließen die Ereignisse automatisch von Extole zu Braze, ohne dass Sie etwas dafür tun müssen. Eine Live-Ansicht der Ereignisse, die an Braze gesendet werden, finden Sie im Outbound Webhook Center von Extole zur Fehlerbehebung. 
