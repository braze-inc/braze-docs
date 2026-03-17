---
nav_title: Zustellbarkeitszentrum
article_title: Zustellbarkeitszentrum
alias: "/deliverability_center/"
page_order: 4
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie das Deliverability Center einrichten, ein Feature, mit dem Marketer ihre Domains und IP-Reputationen für den E-Mail-Versand einsehen und die Zustellbarkeit ihrer E-Mails verstehen können."
channel:
  - email

---

# Zustellbarkeitszentrum

> Das Zustellbarkeitscenter bietet mehr Insights in Ihre E-Mail Performance, indem es die Verwendung der [Gmail Postmaster Tools](https://www.gmail.com/postmaster/) unterstützt, um Daten über gesendete E-Mails zu tracken und Daten über Ihre sendende Domain zu sammeln.

Die Zustellbarkeit von E-Mails ist der Schlüssel zum Kampagnenerfolg. Mit dem Deliverability Center im Braze-Dashboard können Sie Ihre Domains nach **IP-Reputation** oder **Zustellungsfehlern** anzeigen, um mögliche Probleme mit der E-Mail-Zustellbarkeit zu erkennen und zu beheben. 

Um auf das Center für Zustellbarkeit zugreifen zu können, benötigen Sie die [alten Benutzerberechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions) „Zugriff auf Kampagnen, Canvases, Karten, Segmente, Medienbibliothek“ und „Nutzungsdaten anzeigen“ oder die [detaillierten Berechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions) im folgenden Dropdown-Menü für Ihren Workspace.

{% details User permissions for the Deliverability Center %}

{% multi_lang_include deprecations/user_permissions.md %}

- Kampagnen anzeigen
- Kampagnen bearbeiten
- Kampagnen archivieren
- Canvase anzeigen
- Canvase bearbeiten
- Canvase archivieren
- Frequency-Capping-Regeln anzeigen
- Frequency-Capping-Regeln bearbeiten
- Priorisierung von Nachrichten anzeigen
- Priorisierung von Nachrichten bearbeiten
- Content-Blöcke anzeigen
- Feature-Flags anzeigen
- Feature-Flags bearbeiten
- Feature-Flags archivieren
- Segmente anzeigen
- Segmente bearbeiten
- IAM-Templates anzeigen
- IAM-Templates bearbeiten
- IAM-Templates archivieren
- E-Mail-Templates anzeigen
- E-Mail-Templates bearbeiten
- E-Mail Templates archivieren
- Webhook-Templates anzeigen
- Webhook-Templates bearbeiten
- Webhook-Templates archivieren
- Link-Templates anzeigen
- Link-Templates bearbeiten
- Mediathek Assets ansehen
- Assets der Medienbibliothek bearbeiten
- Assets der Medienbibliothek löschen
- Standorte anzeigen
- Standorte bearbeiten
- Standorte archivieren
- Aktionscodes anzeigen
- Aktionscodes bearbeiten
- Exportförderungsaktionscodes
- Präferenzzentren anzeigen
- Präferenzzentren bearbeiten
- Berichte anzeigen
- Berichte bearbeiten
- Nutzungsdaten anzeigen

{% enddetails %}

## Einrichten Ihres Google Postmaster-Kontos

Bevor Sie sich mit dem Deliverability Center verbinden, müssen Sie ein Konto bei Google Postmaster Tools einrichten. Sie können ein geschäftliches oder privates Gmail-Konto verwenden, um Ihren Google Postmaster einzurichten. 

1. Rufen Sie das [Dashboard der Google Postmaster Tools](https://postmaster.google.com/managedomains?pli=1) auf.
2. Wählen Sie unten rechts das Plus-Symbol <i class="fas fa-plus-circle"></i> aus.
3. Geben Sie Ihre Root- oder Subdomäne ein, um Ihre E-Mail-Adresse zu bestätigen. Wenn Sie die Root-Domain hinzufügen und überprüfen, ist es zulässig, die Überprüfung auch auf Subdomains anzuwenden. Durch die Überprüfung `braze.com`von können Sie später und andere `demo.braze.com`Subdomains hinzufügen, ohne diese einzeln überprüfen zu müssen.

{% alert important %}
Bitte stellen Sie sicher, dass der TXT-Eintrag mit der übergeordneten Domain verknüpft ist und nicht mit der Subdomain, die Sie über Braze verwenden.
{% endalert %}

{: start="4"}
4\. Google generiert einen TXT-Eintrag, der direkt zum DNS Ihrer Domain hinzugefügt werden kann. Dieser gehört in der Regel der Person, die Ihr DNS verwaltet. Informationen und Anleitungen zur Aktualisierung Ihres DNS finden Sie unter [Domain-Verifizierung (für Hosts)](https://support.google.com/a/topic/1409901).
5\. Wählen Sie **Weiter**. <br>![Eine Beispiel-Domain „“demo.braze.com zur Authentifizierung einer E-Mail.]({% image_buster /assets/img_archive/domain_authentication.png %})
6\. Nachdem der TXT-Eintrag zum DNS hinzugefügt wurde, kehren Sie zum Dashboard der Google Postmaster Tools zurück und wählen **Überprüfen**. Dieser Schritt bestätigt, dass Sie der Eigentümer der Domain sind, sodass Sie in Ihrem Postmaster-Konto auf die Metriken zur Zustellbarkeit von Gmail zugreifen können. <br> ![Eine Aufforderung, die Eigentumsrechte an der Domain „“demo.braze.com zu überprüfen.]({% image_buster /assets/img_archive/domain_verification.png %})

{% alert note %}
Wenn Ihre Subdomains nicht im Zustellbarkeitscenter für Google Postmaster enthalten sind, kann dies daran liegen, dass nur die übergeordnete Domain zu Google Postmaster hinzugefügt wurde. Nachdem die übergeordneten Domains in Google Postmaster überprüft wurden, können Sie Ihre Subdomains hinzufügen, die automatisch überprüft werden. So kann Google Kennzahlen zur Subdomain erstellen, die dann in das Braze Deliverability Center übernommen werden können.
{% endalert %}

## Integration von Google Postmaster

Bevor Sie Ihr Zustellbarkeitscenter einrichten, überprüfen Sie, ob Ihre Domains [zu den Gmail Postmaster Tools hinzugefügt](https://support.google.com/mail/answer/9981691?hl=en) wurden.

Befolgen Sie diese Anleitung, um Google Postmaster einzubinden und das Deliverability Center einzurichten:

1. Gehen Sie zu **Analytics** > E-Mail Performance.
2. Wählen Sie den Tab **Zustellbarkeitscenter** aus. <br>![Ein Zentrum für die Zustellbarkeit, das nicht mit Google Postmaster verbunden ist.]({% image_buster /assets/img_archive/deliverability_center1.png %})
3. Wählen Sie **Mit Google Postmaster verbinden**. 
4. Wählen Sie Ihr Google-Konto aus und wählen Sie dann **Zulassen**, damit Braze die Metriken zum E-Mail-Verkehr für die in den Postmaster Tools registrierten Domains anzeigen kann. 

Ihre verifizierten Domains werden im Bereich der Zustellbarkeit angezeigt. 

![Zwei verifizierte Domains für Google Postmaster mit mittlerer und niedriger Reputation.]({% image_buster /assets/img_archive/deliverability_center2.png %})

Sie können auch über das Braze-Dashboard auf Google Postmaster zugreifen, indem Sie zu **Partnerintegrationen** > **Technologiepartner** > **Google Postmaster** gehen. Nach der Integration zieht Braze die Reputations- und Fehlerdaten der letzten 30 Tage ab. Die Daten sind möglicherweise nicht sofort verfügbar und das Ausfüllen kann einige Minuten dauern.

### Metriken und Definitionen

Die folgenden Metriken und Definitionen gelten für Google Postmaster Tools.

#### IP-Reputation 

Um die Einstufungen für die IP-Reputation besser zu verstehen, sehen Sie sich diese Tabelle an:

| Reputation | Definition |
| ----- | ---------- |
| Hoch | Gute Erfolgsbilanz mit wenig Beschwerden wegen Spam (etwa durch Anklicken der Schaltfläche "Spam"). |
| Mittel | Es ist bekannt, dass es positives Engagement erzeugt, aber gelegentlich erhält es Spam-Beschwerden. Die meisten E-Mails von dieser Domain werden in den Posteingang weitergeleitet, es sei denn, es gibt vermehrt Beschwerden über Spam. |
| Niedrig | Sie sind dafür bekannt, dass sie regelmäßig eine hohe Anzahl von Spam-Beschwerden erhalten. E-Mails von diesem Sender werden wahrscheinlich in den Spam-Ordner verschoben. |
| Schlecht | Hat einen Verlauf mit einer erhöhten Anzahl von Spam-Beschwerden. E-Mails von dieser Domain werden in der Regel bei der Verbindung abgelehnt oder in den Spam-Ordner verschoben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Domain-Reputation 

Mit dieser Tabelle können Sie die Reputation Ihrer Domain kontrollieren und verhindern, dass Ihre Nachrichten im Spam-Ordner landen.

| Reputation | Definition |
| ----- | ---------- |
| Hoch | Hat eine gute Erfolgsbilanz mit sehr wenigen Spam-Beschwerden. Entspricht den Richtlinien für Absender von Google Mail. E-Mails werden selten in den Spam-Ordner verschoben. Hat eine gute Erfolgsbilanz mit einer sehr niedrigen Spam-Rate. Entspricht den [Gmail-Absenderrichtlinien](https://developers.google.com/gmail/markup/registering-with-google). |
| Mittel | Es ist bekannt, dass es positives Engagement erzeugt, jedoch wurden gelegentlich wenige Beschwerden über Spam gemeldet. Die meisten E-Mails von dieser Domain werden in den Posteingang zugestellt (es sei denn, es kommt zu einem deutlichen Anstieg der Spam-Menge). |
| Niedrig | Bekannt dafür, regelmäßig Spam-Beschwerden zu erhalten. E-Mails von diesem Sender werden wahrscheinlich in den Spam-Ordner verschoben. |
| Schlecht | Hat einen Verlauf mit einer erhöhten Anzahl von Spam-Beschwerden. E-Mails von dieser Domain werden in der Regel bei der Verbindung abgelehnt oder in den Spam-Ordner verschoben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Authentifizierung

Verwenden Sie das Dashboard zur Authentifizierung, um den Prozentsatz der E-Mails zu überprüfen, die das Sender Policy Framework (SPF), DomainKeys Identified Mail (DKIM) und Domain-based Message Authentication, Reporting and Conformance (DMARC) bestanden haben.

| Diagramm | Definition |
| ----- | ---------- |
| SPF | Gibt den prozentualen Anteil der E-Mails an, die das SPF bestanden haben, gemessen an allen E-Mails der Domain, die dies versucht haben. Dies schließt jegliche gefälschte E-Mail aus. |
| DKIM | Gibt den prozentualen Anteil der E-Mails an, die das DKIM bestanden haben, gemessen an allen E-Mails der Domain, die dies versucht haben. |
| DMARC | Gibt den prozentualen Anteil der E-Mails an, die den DMARC-Abgleich bestanden haben, gemessen an allen E-Mails der Domain, die SPF bzw. DKIM bestanden haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Verschlüsselung

Anhand dieser Tabelle können Sie nachvollziehen, wie viel Prozent Ihres eingehenden und ausgehenden Datenverkehrs verschlüsselt ist.

| Begriff | Definition |
| ----- | ---------- |
| TLS Eingehend | Gibt den prozentualen Anteil (bei Gmail) eingehender E-Mails an, die TLS bestanden haben, gemessen an allen von dieser Domain empfangenen E-Mails. |
| TLS Ausgehend | Gibt den prozentualen Anteil (von Gmail) ausgehender E-Mails an, die TLS bestanden haben, gemessen an allen von dieser Domain gesendeten E-Mails. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Weitere Ideen zur Verbesserung der Zustellbarkeit finden Sie unter [Zustellbarkeits-Fallen und Spam-Trap]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/deliverability_pitfalls_and_spam_traps/#deliverability-pitfalls-and-spam-traps). Bitte referenzieren Sie unsere [Best Practices für E-Mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/), um zu erfahren, worauf Sie achten sollten, bevor Sie eine Kampagne per E-Mail versenden.

## Einrichten von Microsoft Smart Network Data Serviceleistungen; Dienste (SNDS)

Wenn Sie Ihr Hauptpostfach bei Microsoft haben, können Sie diese Integration nutzen, um auf Ihre Microsoft-Reputationsdaten zuzugreifen. Auf diese Weise können Sie den Zustand Ihrer IPs überwachen, um festzustellen, wie Ihre E-Mails ankommen.

{% alert important %}
Wenn Sie Ihre Daten nicht im Deliverability Center sehen, kontaktieren Sie den [Support]({{site.baseurl}}/user_guide/administrative/access_braze/support/) mit einer Liste Ihrer IP-Adressen.
{% endalert %}

![Ein Beispiel für Ergebnisse von Microsoft SNDS, einschließlich Beispiel-IPs, Empfänger:innen, RCPT-Befehlen, Datenbefehlen, Filterergebnissen, Beschwerdequote, Beginn und Ende des Trap-Nachrichtenzeitraums sowie Spam-Trap-Treffern.]({% image_buster /assets/img_archive/deliverability_center_msnds.png %})

### Metriken und Definitionen

Die folgenden Metriken gelten für Microsoft SNDS.

#### Empfänger:innen

Diese Metrik referenziert die Anzahl der Empfänger:innen von Nachrichten, die von der IP übertragen werden.

#### DATA-Befehle

Diese Metrik trackt die Anzahl der DATA-Befehle, die von der IP gesendet wurden. DATA-Befehle sind Teil des SMTP-Protokolls, das für den Versand von E-Mails verwendet wird.

#### Ergebnisse filtern

Diese Tabelle enthält die Filterergebnisse 

| Ergebnis | Definition |
| ----- | ---------- |
| Grün | Vom Microsoft-Spamfilter in bis zu 10 % des angegebenen Zeitraums als Spam eingestuft. |
| Gelb | Vom Microsoft-Spamfilter in 10 bis 90 % des angegebenen Zeitraums als Spam eingestuft. |
| Rot | Vom Microsoft-Spamfilter in mehr als 90 % des angegebenen Zeitraums als Spam eingestuft.| 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Beschwerdequote

Dies ist der Anteil der Male, die sich ein:e Nutzer:in von Hotmail oder Windows Live während des Aktivitätszeitraums über eine von der IP empfangene Nachricht beschwert hat. Benutzer können über die Web-Benutzeroberfläche fast alle Nachrichten als Junk melden. 

Um die Beschwerdequote zu berechnen, teilen Sie die Anzahl der Beschwerden durch die Anzahl der Nachrichtenempfänger.  

| Ergebnis | Definition |
| ----- | ---------- |
| Weniger als 0,3% | Die ideale Beschwerdequote. |
| Mehr als 0,3% | Überprüfen Sie Ihren Anmeldeprozess und stellen Sie sicher, dass der Abmeldelink funktioniert. Bitte überlegen Sie auch, ob die E-Mail besser personalisiert werden könnte, um auf Ihre Zielgruppen zugeschnitten zu sein. |
| Mehr als 100% | Beachten Sie, dass SNDS Beschwerden für den Tag anzeigt, an dem sie gemeldet wurden, und nicht rückwirkend für den Tag, an dem die beanstandete Post zugestellt wurde. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Spam-Trap-Treffer

Spam-Trap-Treffer geben die Anzahl an Nachrichten an, die an Trap-Konten gesendet worden sind, also an Konten von Outlook.com, die keine E-Mails angefordert haben. Es ist wahrscheinlich, dass alle Nachrichten, die an diese Trap-Konten gesendet werden, als Spam angesehen werden. Daher ist es wichtig, diese Metrik zu überwachen, um sicherzustellen, dass sie niedrig ist. Niedrige Spam-Trap-Treffer bedeuten, dass die Nachrichten nicht an diese Konten gesendet werden, sondern an echte Konten.

{% alert tip %}
Wenn Sie nach Datensätzen zu einer Ihrer überprüften Domains in Braze suchen, beachten Sie bitte, dass das Center für Zustellbarkeit Ihre Daten von Google Postmaster oder Microsoft SNDS auflistet. Dies bedeutet, dass wahrscheinlich keine der beiden Plattformen über Daten verfügt, die mit Braze geteilt werden können. Alternativ empfehlen wir Ihnen, für eine einheitliche E-Mail-Zustellung zu sorgen, da dies Ihre Reputation verbessern kann.
{% endalert %}


