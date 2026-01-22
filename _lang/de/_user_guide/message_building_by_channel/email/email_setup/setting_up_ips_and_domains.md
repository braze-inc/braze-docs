---
nav_title: Einrichten von IPs &amp; Domains
article_title: Einrichten von IPs &amp; Domains
page_order: 0
page_type: tutorial
channel: email
description: "In diesem Artikel erfahren Sie, wie Sie Ihre IPs und Domains für den Versand von E-Mails über Braze einrichten."

---

# Einrichten von IPs und Domänen

{% multi_lang_include video.html id="iTm3yQkJ0UU" align="right"  %}

> In diesem Artikel erfahren Sie, welche Voraussetzungen erfüllt sein müssen und welche Schritte Sie unternehmen müssen, um Ihre IP-Adressen und Pools sowie Domains und Subdomains einzurichten, bevor Sie mit Braze E-Mails versenden können.<br><br>Obwohl der Großteil des Einrichtungsprozesses von Braze übernommen wird, haben wir die Anforderungen und Materialien für diese Einrichtung skizziert.

## Methode 1: Koordinieren Sie mit Braze (empfohlen)

### Schritt 1: Informationen skizzieren

Senden Sie die folgenden Informationen an Ihren Braze-Vertreter:

* Ihre ausgewählten Domains und Subdomains
* Die ungefähre Anzahl der E-Mails, die Sie pro Monat versenden werden, was Ihnen hilft, die Anzahl der benötigten IPs zu bestimmen
* Wie Sie Ihre sendenden Domains auf Ihre zugewiesene IP zuordnen möchten

### Schritt 2: Braze konfiguriert Informationen

Nachdem wir Ihre E-Mail erhalten haben, machen wir uns an die Arbeit und konfigurieren Ihre IPs, Domains und Subdomains sowie IP-Pools.

### Schritt 3: DNS-Einträge hinzufügen

Nachdem Ihre IPs, Domains, Subdomains und IP-Pools konfiguriert sind, senden wir Ihnen eine Liste der DNS-Einträge. Bitten Sie Ihre Techniker und Entwickler, diese DNS-Einträge bei Bedarf hinzuzufügen, und informieren Sie das Braze Onboarding-Team, nachdem sie hinzugefügt wurden.

### Nächste Schritte

Wir überprüfen Ihre Einrichtung und validieren alle Informationen in unseren internen Systemen. Das Braze Onboarding-Team wird Sie informieren, wenn Sie bereit sind oder wenn es Probleme mit Ihren DNS-Einträgen gibt, die Sie mit Ihrem technischen Team klären müssen.

## Methode 2: SB-E-Mail-Setup

Mit dieser Methode wird eine Sende-Domain, eine Tracking-Domain und insgesamt eine IP für ein Unternehmen eingerichtet. Wenn Sie planen, mehr einzurichten, wenden Sie sich bitte an das Braze Onboarding-Team (Methode 1).

{% alert important %}
Diese Selbstbedienungsfunktion zur Einrichtung von E-Mails befindet sich derzeit in der Beta-Phase. Wenden Sie sich an Ihre:n Braze-Kundenbetreuer:in, wenn Sie an einer Teilnahme an der Beta interessiert sind.<br>Wenn Sie die Self-Service-E-Mail-Einrichtungsfunktion verwenden, sollten Sie sich auch mit dem Braze Onboarding-Team beraten.
{% endalert %}

### Voraussetzungen

Um das SB-E-Mail-Setup zu nutzen, müssen Sie die folgenden Voraussetzungen erfüllen:

1. Sie sind ein: neue:r Kund:in im Onboarding.
2. Sie haben die Berechtigung "Unternehmenseinstellungen verwalten können" auf Unternehmensebene.

### Schritt 1: Einrichtung starten

1. Gehen Sie zu **Einstellungen** > **Admin-Einstellungen** unter **Unternehmenseinstellungen**. 
2. Wählen Sie dann die Registerkarte **Absenderüberprüfung**. Um diese Registerkarte sehen zu können, müssen Sie über die Berechtigung "Unternehmenseinstellungen verwalten können" auf Unternehmensebene verfügen.
3. Klicken Sie auf die Schaltfläche **Einrichtung starten**.

### Schritt 2: Sender-Domain hinzufügen und überprüfen

Eine Sender-Domain wird in der „Von“-Adresse verwendet, wenn eine E-Mail gesendet wird. Geben Sie eine Senderdomäne ein und klicken Sie auf **Senden**. 

Als nächstes fügen Sie die TXT- und CNAME-Einträge unten auf der Seite zu Ihrem DNS-Anbieter hinzu. Kehren Sie dann zum Braze Dashboard zurück und klicken Sie auf **Überprüfen**.

![]({% image_buster /assets/img_archive/email_setup_rdns_records.png %})

{% alert important %}
Die sendende Domain muss einer Domain untergeordnet sein, die Sie besitzen. Wenn Sie z. B. „example.com“ besitzen, könnte eine Subdomain „mail.example.com“ sein, die es Ihnen ermöglicht, die Sendeadresse „@mail.example.com“ zu verwenden.
{% endalert %}

### Schritt 3: Tracking-Domain hinzufügen und überprüfen

Eine Tracking-Domain wird verwendet, um Links in Ihren E-Mails für Click-Tracking- und Branding-Zwecke einzubinden. Dies ist für die Nutzer:innen sichtbar, wenn sie mit dem Mauszeiger über Ihre E-Mail-Links fahren oder darauf klicken. Wir empfehlen Ihnen, diese mit Ihrer Sender-Domain abzustimmen.

Geben Sie eine Tracking-Domain ein und klicken Sie auf **Senden**. Als nächstes fügen Sie die CNAME-Einträge unten auf der Seite zu Ihrem DNS-Anbieter hinzu. Kehren Sie dann zum Braze Dashboard zurück und klicken Sie auf **Überprüfen**.

### Schritt 4: Eine IP-Adresse hinzufügen

Braze erstellt einen A-Eintrag, um Ihre IP-Adresse mit Ihrer sendenden Subdomain in einem Reverse DNS (rDNS) genannten Setup zu verknüpfen. Fügen Sie den A-Eintrag in Ihrem DNS-Anbieter hinzu und klicken Sie dann auf **rDNS einrichten**, um die Zustellbarkeit zu unterstützen.

Beachten Sie, dass zusätzliche Domains, die hinzugefügt wurden, nicht im Abschnitt **Senderüberprüfung** erscheinen. Wenn Sie weitere Domains hinzufügen möchten, wenden Sie sich an das Braze Support-Team.

### Nächste Schritte

Nachdem Ihre Absenderüberprüfung abgeschlossen ist, empfehlen wir Ihnen die IP-Erwärmung, damit Ihre Nachrichten mit einer gleichbleibend hohen Rate den Posteingang des Empfängers erreichen. Wenden Sie sich nach Abschluss dieser Einrichtung an das Braze Onboarding-Team, um zu überprüfen, ob Ihre Domains und [IP-Adresse]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) funktionieren.

