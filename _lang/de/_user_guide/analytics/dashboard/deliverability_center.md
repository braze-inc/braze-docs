---
nav_title: Zustellbarkeitszentrum
article_title: Zustellbarkeitszentrum
alias: "/deliverability_center/"
page_order: 4
description: "In diesem Referenzartikel erfahren Sie, wie Sie das Zustellbarkeitszentrum einrichten – ein Feature, mit dem Marketer ihre E-Mail-Versanddomains und IP-Reputationen einsehen und die Zustellbarkeit ihrer E-Mails besser verstehen können."
channel:
  - email

---

# Zustellbarkeitszentrum

> Das Zustellbarkeitszentrum bietet Ihnen mehr Insights in Ihre E-Mail-Performance, indem es die Verwendung der [Gmail Postmaster Tools](https://www.gmail.com/postmaster/) unterstützt, um Daten über gesendete E-Mails zu tracken und Informationen über Ihre Versanddomain zu sammeln.

Die Zustellbarkeit von E-Mails ist der Schlüssel zum Kampagnenerfolg. Mit dem Zustellbarkeitszentrum im Braze-Dashboard können Sie Ihre Domains nach **IP-Reputation** oder **Zustellungsfehlern** anzeigen, um mögliche Probleme mit der E-Mail-Zustellbarkeit zu erkennen und zu beheben. 

Um auf das Zustellbarkeitszentrum zugreifen zu können, benötigen Sie die [alten Benutzerberechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions) „Zugriff auf Kampagnen, Canvase, Karten, Segmente, Medienbibliothek" und „Nutzungsdaten anzeigen" oder die [detaillierten Berechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions) im folgenden Dropdown-Menü für Ihren Workspace.

{% details Benutzerberechtigungen für das Zustellbarkeitszentrum %}

{% multi_lang_include deprecations/user_permissions.md %}

- Kampagnen anzeigen
- Kampagnen bearbeiten
- Kampagnen archivieren
- Canvase anzeigen
- Canvase bearbeiten
- Canvase archivieren
- Frequency-Capping-Regeln anzeigen
- Frequency-Capping-Regeln bearbeiten
- Nachrichtenpriorisierung anzeigen
- Nachrichtenpriorisierung bearbeiten
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
- E-Mail-Templates archivieren
- Webhook-Templates anzeigen
- Webhook-Templates bearbeiten
- Webhook-Templates archivieren
- E-Mail-Link-Templates anzeigen
- E-Mail-Link-Templates bearbeiten
- Medienbibliothek-Assets anzeigen
- Medienbibliothek-Assets bearbeiten
- Medienbibliothek-Assets löschen
- Standorte anzeigen
- Standorte bearbeiten
- Standorte archivieren
- Aktionscodes anzeigen
- Aktionscodes bearbeiten
- Aktionscodes exportieren
- Präferenzzentren anzeigen
- Präferenzzentren bearbeiten
- Berichte anzeigen
- Berichte bearbeiten
- Nutzungsdaten anzeigen

{% enddetails %}

## Einrichten Ihres Google Postmaster-Kontos

Bevor Sie sich mit dem Zustellbarkeitszentrum verbinden, müssen Sie ein Konto bei Google Postmaster Tools einrichten. Sie können ein geschäftliches oder privates Gmail-Konto verwenden, um Ihren Google Postmaster einzurichten. 

1. Rufen Sie das [Dashboard der Google Postmaster Tools](https://postmaster.google.com/managedomains?pli=1) auf.
2. Wählen Sie unten rechts das Plus-Symbol <i class="fas fa-plus-circle"></i> aus.
3. Geben Sie Ihre Root-Domain (übergeordnete Domain) ein, um Ihre E-Mail zu authentifizieren. Stellen Sie sicher, dass der TXT-Eintrag mit dieser Root-Domain (übergeordneten Domain) verknüpft ist und **nicht** mit der Subdomain, die Sie über Braze verwenden. Durch die Verifizierung der Root-Domain (übergeordneten Domain) können Sie später Subdomains in den Postmaster Tools hinzufügen, ohne zusätzliche TXT-Einträge erstellen zu müssen. Wenn Sie beispielsweise `braze.com` verifizieren, können Sie später `demo.braze.com` als separate Subdomain in den Postmaster Tools hinzufügen, um Metriken auf Subdomain-Ebene einzusehen.
4. Google generiert einen TXT-Eintrag, der direkt zum DNS Ihrer Domain hinzugefügt werden kann. Dieser wird in der Regel von der Person verwaltet, die für Ihr DNS zuständig ist. Informationen und Anleitungen zur Aktualisierung Ihres spezifischen DNS finden Sie unter [Domain verifizieren (hostspezifische Schritte)](https://support.google.com/a/topic/1409901).
5. Wählen Sie **Weiter**. <br>![Eine Beispiel-Domain „demo.braze.com" zur Authentifizierung einer E-Mail.]({% image_buster /assets/img_archive/domain_authentication.png %})
6. Nachdem der TXT-Eintrag zum DNS hinzugefügt wurde, kehren Sie zum Dashboard der Google Postmaster Tools zurück und wählen **Überprüfen**. Dieser Schritt bestätigt, dass Sie die Domain besitzen, sodass Sie in Ihrem Postmaster-Konto auf die Gmail-Zustellbarkeitsmetriken zugreifen können. <br> ![Eine Aufforderung, die Eigentümerschaft der Domain „demo.braze.com" zu überprüfen.]({% image_buster /assets/img_archive/domain_verification.png %})

{% alert note %}
Wenn Ihre Subdomains nicht im Zustellbarkeitszentrum für Google Postmaster angezeigt werden, kann dies daran liegen, dass nur die Root-Domain (übergeordnete Domain) zu Google Postmaster hinzugefügt wurde. Nachdem die Root-Domains in Google Postmaster verifiziert wurden, können Sie Ihre Subdomains hinzufügen, die automatisch verifiziert werden. So kann Google Metriken auf Subdomain-Ebene bereitstellen, die dann in das Braze Zustellbarkeitszentrum übernommen werden können.
{% endalert %}

## Integration von Google Postmaster

Bevor Sie Ihr Zustellbarkeitszentrum einrichten, überprüfen Sie, ob Ihre Domains [zu den Gmail Postmaster Tools hinzugefügt](https://support.google.com/mail/answer/9981691?hl=en) wurden.

Befolgen Sie diese Schritte, um Google Postmaster zu integrieren und das Zustellbarkeitszentrum einzurichten:

1. Gehen Sie zu **Analytics** > **E-Mail-Performance**.
2. Wählen Sie den Tab **Zustellbarkeitszentrum** aus. <br>![Ein Zustellbarkeitszentrum, das nicht mit Google Postmaster verbunden ist.]({% image_buster /assets/img_archive/deliverability_center1.png %})
3. Wählen Sie **Mit Google Postmaster verbinden**. 
4. Wählen Sie Ihr Google-Konto aus und wählen Sie dann **Zulassen**, damit Braze die Metriken zum E-Mail-Verkehr für die in den Postmaster Tools registrierten Domains anzeigen kann. 

Ihre verifizierten Domains werden im Zustellbarkeitszentrum angezeigt. 

![Zwei verifizierte Domains für Google Postmaster mit mittlerer und niedriger Reputation.]({% image_buster /assets/img_archive/deliverability_center2.png %})

Sie können auch über das Braze-Dashboard auf Google Postmaster zugreifen, indem Sie zu **Partnerintegrationen** > **Technologiepartner** > **Google Postmaster** gehen. Nach der Integration ruft Braze die Reputations- und Fehlerdaten der letzten 30 Tage ab. Die Daten sind möglicherweise nicht sofort verfügbar und das Laden kann einige Minuten dauern.

### Metriken und Definitionen

Die folgenden Metriken und Definitionen gelten für Google Postmaster Tools.

#### IP-Reputation 

Um die Einstufungen für die IP-Reputation besser zu verstehen, sehen Sie sich diese Tabelle an:

| Reputation | Definition |
| ----- | ---------- |
| Hoch | Gute Erfolgsbilanz mit wenigen Spam-Beschwerden (z. B. wenn Nutzer:innen auf den „Spam"-Button klicken). |
| Mittel | Bekannt für positives Engagement, erhält aber gelegentlich Spam-Beschwerden. Die meisten E-Mails von dieser Domain werden in den Posteingang zugestellt, es sei denn, die Spam-Beschwerden nehmen zu. |
| Niedrig | Bekannt dafür, regelmäßig eine erhöhte Anzahl von Spam-Beschwerden zu erhalten. E-Mails von diesem Sender werden wahrscheinlich in den Spam-Ordner verschoben. |
| Schlecht | Hat einen Verlauf mit einer erhöhten Anzahl von Spam-Beschwerden. E-Mails von dieser Domain werden fast immer bei der Verbindung abgelehnt oder in den Spam-Ordner verschoben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Domain-Reputation 

Verwenden Sie die folgende Tabelle, um die Reputation Ihrer Domain zu überwachen und zu verstehen, damit Ihre Nachrichten nicht im Spam-Ordner landen.

| Reputation | Definition |
| ----- | ---------- |
| Hoch | Hat eine gute Erfolgsbilanz mit sehr wenigen Spam-Beschwerden. Entspricht den Absenderrichtlinien von Gmail. E-Mails werden selten in den Spam-Ordner verschoben. Hat eine gute Erfolgsbilanz mit einer sehr niedrigen Spam-Rate. Entspricht den [Gmail-Absenderrichtlinien](https://developers.google.com/gmail/markup/registering-with-google). |
| Mittel | Bekannt für positives Engagement, hat aber gelegentlich wenige Spam-Beschwerden erhalten. Die meisten E-Mails von dieser Domain erreichen den Posteingang (es sei denn, es kommt zu einem deutlichen Anstieg des Spam-Aufkommens). |
| Niedrig | Bekannt dafür, regelmäßig Spam-Beschwerden zu erhalten. E-Mails von diesem Sender werden wahrscheinlich in den Spam-Ordner verschoben. |
| Schlecht | Hat einen Verlauf mit einer erhöhten Anzahl von Spam-Beschwerden. E-Mails von dieser Domain werden fast immer bei der Verbindung abgelehnt oder in den Spam-Ordner verschoben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Authentifizierung

Verwenden Sie das Authentifizierungs-Dashboard, um den Prozentsatz der E-Mails zu überprüfen, die das Sender Policy Framework (SPF), DomainKeys Identified Mail (DKIM) und Domain-based Message Authentication, Reporting and Conformance (DMARC) bestanden haben.

| Diagrammtyp | Definition |
| ----- | ---------- |
| SPF | Zeigt den prozentualen Anteil der E-Mails an, die SPF bestanden haben, im Verhältnis zu allen E-Mails der Domain, bei denen SPF geprüft wurde. Gefälschte E-Mails sind hiervon ausgeschlossen. |
| DKIM | Zeigt den prozentualen Anteil der E-Mails an, die DKIM bestanden haben, im Verhältnis zu allen E-Mails der Domain, bei denen DKIM geprüft wurde. |
| DMARC | Zeigt den prozentualen Anteil der E-Mails an, die den DMARC-Abgleich bestanden haben, im Verhältnis zu allen von der Domain empfangenen E-Mails, die entweder SPF oder DKIM bestanden haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Verschlüsselung

Anhand dieser Tabelle können Sie nachvollziehen, wie viel Prozent Ihres eingehenden und ausgehenden Datenverkehrs verschlüsselt ist.

| Begriff | Definition |
| ----- | ---------- |
| TLS eingehend | Zeigt den prozentualen Anteil eingehender E-Mails (an Gmail) an, die TLS bestanden haben, im Verhältnis zu allen von dieser Domain empfangenen E-Mails. |
| TLS ausgehend | Zeigt den prozentualen Anteil ausgehender E-Mails (von Gmail) an, die über TLS akzeptiert wurden, im Verhältnis zu allen an diese Domain gesendeten E-Mails. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Weitere Ideen zur Verbesserung der Zustellbarkeit finden Sie unter [Zustellbarkeits-Fallen und Spam-Traps]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/deliverability_pitfalls_and_spam_traps/#deliverability-pitfalls-and-spam-traps). Schauen Sie sich auch unsere [Best Practices für E-Mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/) an, um zu erfahren, worauf Sie vor dem Versand einer E-Mail-Kampagne achten sollten.

## Einrichten von Microsoft Smart Network Data Services (SNDS)

Wenn Microsoft Ihr Hauptpostfach-Anbieter ist, können Sie diese Integration nutzen, um auf Ihre Microsoft-Reputationsdaten zuzugreifen und diese einzusehen. Auf diese Weise können Sie den Zustand Ihrer IPs überwachen und besser einschätzen, wie Ihre E-Mails empfangen werden.

{% alert important %}
Wenn Ihre Daten nicht im Zustellbarkeitszentrum angezeigt werden, kontaktieren Sie den [Support]({{site.baseurl}}/user_guide/administrative/access_braze/support/) mit einer Liste Ihrer IP-Adressen.
{% endalert %}

![Ein Beispiel für Ergebnisse von Microsoft SNDS, einschließlich Beispiel-IPs, Empfänger:innen, RCPT-Befehlen, DATA-Befehlen, Filterergebnissen, Beschwerdequote, Beginn und Ende des Trap-Nachrichtenzeitraums sowie Spam-Trap-Treffern.]({% image_buster /assets/img_archive/deliverability_center_msnds.png %})

### Metriken und Definitionen

Die folgenden Metriken gelten für Microsoft SNDS.

#### Empfänger:innen

Diese Metrik bezieht sich auf die Anzahl der Empfänger:innen von Nachrichten, die von der IP übertragen wurden.

#### DATA-Befehle

Diese Metrik erfasst die Anzahl der DATA-Befehle, die von der IP gesendet wurden. DATA-Befehle sind Teil des SMTP-Protokolls, das für den E-Mail-Versand verwendet wird.

#### Filterergebnisse

In dieser Tabelle finden Sie die Filterergebnisse: 

| Ergebnis | Definition |
| ----- | ---------- |
| Grün | Wurde vom Microsoft-Spamfilter in bis zu 10 % des angegebenen Zeitraums als Spam eingestuft. |
| Gelb | Wurde vom Microsoft-Spamfilter in 10 % bis 90 % des angegebenen Zeitraums als Spam eingestuft. |
| Rot | Wurde vom Microsoft-Spamfilter in mehr als 90 % des angegebenen Zeitraums als Spam eingestuft.| 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Beschwerdequote

Dies ist der Anteil der Fälle, in denen sich Hotmail- oder Windows-Live-Nutzer:innen während des Aktivitätszeitraums über eine von der IP empfangene Nachricht beschwert haben. Nutzer:innen haben die Möglichkeit, fast alle Nachrichten über die Benutzeroberfläche als Junk zu melden. 

Um die Beschwerdequote zu berechnen, teilen Sie die Anzahl der Beschwerden durch die Anzahl der Nachrichtenempfänger:innen.  

| Ergebnis | Definition |
| ----- | ---------- |
| Weniger als 0,3 % | Die ideale Beschwerdequote. |
| Mehr als 0,3 % | Überprüfen Sie Ihren Registrierungsprozess und stellen Sie sicher, dass der Abmeldelink funktioniert. Überlegen Sie auch, ob die E-Mail besser auf Ihre Zielgruppe personalisiert werden könnte. |
| Mehr als 100 % | Beachten Sie, dass SNDS Beschwerden für den Tag anzeigt, an dem sie gemeldet wurden, und nicht rückwirkend für den Tag, an dem die beanstandete E-Mail zugestellt wurde. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Spam-Trap-Treffer

Spam-Trap-Treffer geben die Anzahl der Nachrichten an, die an „Trap-Konten" gesendet wurden – also an Konten von Outlook.com, die keine E-Mails angefordert haben. Es ist wahrscheinlich, dass alle Nachrichten, die an diese Trap-Konten gesendet werden, als Spam eingestuft werden. Daher ist es wichtig, diese Metrik zu überwachen und sicherzustellen, dass sie niedrig bleibt. Niedrige Spam-Trap-Treffer bedeuten, dass die Nachrichten nicht an diese Konten gesendet werden, sondern an echte Konten.

{% alert tip %}
Wenn Sie nach Datensätzen zu einer Ihrer verifizierten Domains in Braze suchen, beachten Sie bitte, dass das Zustellbarkeitszentrum Ihre Daten von Google Postmaster oder Microsoft SNDS auflistet. Das bedeutet, dass möglicherweise keine der beiden Plattformen über Daten verfügt, die mit Braze geteilt werden können. Alternativ empfehlen wir, für eine konsistente E-Mail-Zustellung zu sorgen, da dies zu einer besseren Reputation führen kann. 
{% endalert %}