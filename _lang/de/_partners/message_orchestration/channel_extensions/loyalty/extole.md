---
nav_title: Extole
article_title: Extole
description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze und Extole, einem Unternehmen für Empfehlungsmarketing, die es Ihnen erlaubt, Kunden-Events und -Attribute aus Empfehlungs- und Wachstumsprogrammen in Braze zu übernehmen."
alias: /partners/extole/
page_type: partner
search_tag: Partner

---

# Extole

> [Extole](https://www.extole.com/), ein SaaS-Unternehmen, ist branchenführend im Empfehlungsmarketing und hilft bei der Erstellung und Optimierung effektiver Programme für das Empfehlungsmarketing, um die Kundenakquise zu steigern.

_Diese Integration wird von Extole gepflegt._

## Über die Integration

Mit der Integration von Braze und Extole können Sie Kunden-Events und -Attribute aus den Freundschaftswerbungs- und Wachstumsprogrammen von Extole in Braze übernehmen und so personalisierte Marketingkampagnen erstellen, die die Kundenakquise, das Engagement und die Loyalität steigern. Sie können auch dynamisch Attribute von Extole-Inhalten, wie personalisierte Codes und Links, in die Braze-Kommunikation einbeziehen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Extole-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Extole-Konto. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit der Berechtigung `users.track`. Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze API URL | Ihre Braze API URL ist spezifisch für Ihre [Braze-Instanz]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Die folgenden Anwendungsfälle zeigen einige Möglichkeiten auf, wie Sie die Integration von Extole mit Braze nutzen können. Arbeiten Sie mit Ihren Extole-Implementierungs- und Customer-Success-Managern zusammen, um eine Option zu entwickeln, die den speziellen Anforderungen Ihres Unternehmens entspricht.

- Nutzen Sie angepasste Events aus Ihren Empfehlungs- und Engagement-Programmen, um eine Kampagne oder ein Canvas von Braze zu triggern.
- Erstellen Sie angepasste Segmente, Dashboards und Berichte mit Daten aus Ihren Extole-Programmen
- Automatisches Abmelden oder Anmelden von Nutzern:in Ihrer Marketing-Liste in Braze

## Integration

Führen Sie die folgenden Schritte aus, um Ihre Integration schnell zum Laufen zu bringen. Ihre Extole Manager:in für die Implementierung und den Kundenerfolg unterstützen Sie bei diesem Prozess und beantworten alle Ihre Fragen.

### Verbinden Sie sich mit Ihrem Braze-Konto

1. Wählen Sie die Braze Integration auf der [Partnerseite](https://my.extole.com/partners) Ihres My Extole-Kontos aus.
2. In der Braze Integration wählen Sie **Installieren**, um die Verbindung zwischen Extole und Braze herzustellen.
3. Füllen Sie die erforderlichen Felder aus, beginnend mit Ihrem Braze REST API-Schlüssel. 
4. Geben Sie Ihre Braze API URL ein. Diese URL hängt davon ab, auf welcher Instanz Ihr Braze-Konto eingerichtet ist.
5. Fügen Sie alle Extole-Ereignisse hinzu, die Sie an Braze senden möchten. Die Standard-Ereignisse, Event-Eigenschaften und Nutzer:innen-Attribute sind in der [Tabelle Extole Events](https://dev.extole.com/docs/braze#extole-program-events) beschrieben.
6. Fügen Sie alle Reward-Status hinzu, die Sie an Braze senden möchten, außer dem Staat `FULFILLED`. In der [Tabelle Extole Rewards](https://dev.extole.com/docs/braze#extole-rewards) finden Sie Beschreibungen der verfügbaren Reward-Status.
7. Wählen Sie die Abbildung Ihres externen ID-Schlüssels von Braze aus. So aktualisiert Extole die Nutzerprofile in Braze. Sie können den externen ID-Schlüssel von Braze der `email_address` oder `partner_user_id` von Extole für die Nutzer:innen zuordnen. Wir empfehlen die Verwendung von `external_id` anstelle von `email_address`, da dies sicherer ist.
8. Speichern Sie Ihre Einstellungen, um die Verbindung abzuschließen. Jetzt können Extole-Ereignisse auf Ihr Braze-Konto fließen.

### Extole Programm Ereignisse

Im Folgenden finden Sie die Standard-Ereignisse, Event-Eigenschaften und Nutzer:innen-Attribute, die Extole an Braze sendet. Wenden Sie sich an Ihre Extole-Implementierungs- oder Customer-Success-Manager:in, um zusätzliche Extole-Events zu identifizieren und zu Ihrer Integration hinzuzufügen.

| Event | Beschreibung | Event-Eigenschaften | Nutzerattribute |
| ----------- | ----------- | ----------- | ----------- |
| `extole_created_share_link` | Ein Teilnehmer erstellt seinen Share-Link, indem er seine E-Mail in der Extole Share Experience eingibt. | Event-Name  <br>Zeit der Veranstaltung  <br>Partner (Extole)  <br>Funnel (Fürsprecher oder Freund)  <br>Programm | <br>Externe ID <br>E-Mail  <br>Link teilen |
| `extole_shared` | Ein Teilnehmer teilt seinen Empfehlungslink mit einem Freund. | Event-Name  <br>Zeit der Veranstaltung  <br>Partner (Extole)  <br>Externe ID  <br>Funnel (Fürsprecher oder Freund)  <br>Programm  <br>Kanal teilen | E-Mail <br>Vorname <br>Nachname |
| `outcome` - Das Ergebnis ist dynamisch und hängt von der Konfiguration Ihres Programms ab (z.B. `extole_shipped`, `extole_converted`).| Ein Teilnehmer hat das für das Programm konfigurierte Ereignis mit dem gewünschten Ergebnis umgewandelt oder abgeschlossen. | Dynamisch pro Programm | E-Mail <br>Vorname <br>Nachname |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Extole Abo Staaten

| Abo-Status | Beschreibung | Event-Eigenschaften | Nutzerattribute |
| ----------- | ----------- | ----------- | ----------- |
| `subscribed` | Ein Teilnehmer hat sich für den Erhalt von Marketing Nachrichten entschieden. | -- | E-Mail  <br>Listentyp  <br>Externe ID  <br>E-Mail abonnieren (Opt-in) |
| `unsubscribed` | Ein Teilnehmer hat sich gegen den Erhalt von E-Mails von Extole entschieden.| E-Mail  <br>Externe ID  <br>Abo-Status (abgemeldet)  <br>Abo-Gruppe ID  | Listentyp |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Extole Rewards

Standardmäßig sendet Extole Reward-Ereignisse im Status `FULFILLED` an Braze, damit Sie Reward-Benachrichtigungen über eine Kampagne oder ein Canvas triggern können. In der folgenden Tabelle finden Sie weitere Rewards.

| Reward Staat | Beschreibung | Event-Eigenschaften | Nutzerattribute |
| ----------- | ----------- | ----------- | ----------- |
| `FULFILLED` | Der Standardstatus. Der Prämie wurde von einem Extole Prämienanbieter ein Wert zugewiesen (z.B. ein Gutschein oder eine Geschenkkarte). | E-Mail <br>Nennwert  <br>Coupon Code  <br>Nennwert Typ  | E-Mail <br>Vorname  <br>Nachname |
| `EARNED` | Eine Belohnung wurde erstellt und mit einer Person verknüpft. | E-Mail <br>Nennwert  <br>Coupon Code  <br>Nennwert Typ  | E-Mail <br>Vorname  <br>Nachname |
| `SENT` | Die Prämie wurde erfüllt und entweder per E-Mail oder auf einem Gerät an den Empfänger:in gesendet. | E-Mail <br>Nennwert  <br>Coupon Code  <br>Nennwert Typ  | E-Mail <br>Vorname  <br>Nachname |
| `REDEEMED` | Die Rewards wurden vom Empfänger:in verwendet, was durch ein Konversions-Event oder ein Einlösungs-Event an Extole belegt wird.| E-Mail <br>Nennwert  <br>Coupon Code  <br>Nennwert Typ  | E-Mail <br>Vorname  <br>Nachname |
| `FAILED` | Ein Problem hat die Ausgabe oder den Versand der Rewards verhindert und muss behoben werden. | E-Mail <br>Nennwert  <br>Coupon Code  <br>Nennwert Typ  | E-Mail <br>Vorname  <br>Nachname |
| `CANCELED` | Die Belohnung wurde deaktiviert und kehrt ins Inventar zurück. | E-Mail <br>Nennwert  <br>Nennwert Typ  | E-Mail <br>Vorname  <br>Nachname |
| `REVOKED` | Die erfüllte Belohnung wurde für ungültig erklärt. Extole hat zum Beispiel eine Geschenkkarte eines Lieferanten angefordert und dann festgestellt, dass die Karte irrtümlich verschickt wurde. Wenn der Anbieter den Widerruf der Prämie unterstützt, wird Extole das Geld zurückfordern, und die Prämie ist nicht mehr gültig. | E-Mail <br>Nennwert   <br>Nennwert Typ  | E-Mail <br>Vorname  <br>Nachname |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }


## Anpassung

### Nutzer:innen in Braze finden und erstellen

Für bestimmte Anwendungsfälle, wie z.B. ein neues E-Mail- oder SMS-Abonnement, für das Extole keine externe ID (Benutzer-ID) hat, kann Extole über den Braze-Endpunkt [Export Benutzerprofil nach Bezeichner]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) nach dem Profil des Nutzers suchen. Extole fügt alle Attribute des Profils hinzu und aktualisiert sie, wenn der Nutzer:in in Braze existiert. Wenn die Anfrage kein Nutzerprofil zurückgibt, verwendet Extole den Endpunkt `/users/track`, um einen Nutzer-Alias mit der E-Mail Adresse des Nutzers als Alias-Namen zu erstellen.

## Verwendung dieser Integration

Nachdem Sie Ihre Konten verbunden haben, werden die Ereignisse automatisch von Extole zu Braze fließen, ohne dass Sie etwas tun müssen. Eine Live-Ansicht der Ereignisse, die an Braze gesendet werden, finden Sie zur Fehlerbehebung im Outbound Webhook Center von Extole. 

