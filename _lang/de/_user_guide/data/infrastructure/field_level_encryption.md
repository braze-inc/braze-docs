---
nav_title: Verschlüsselung des Bezeichners auf Feldebene
article_title: Verschlüsselung auf Bezeichner-Feldebene
page_order: 2
alias: "/field_level_encryption/"
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie E-Mail-Adressen verschlüsseln können, um den Austausch von persönlichen Bezeichnern (PII) in Braze zu minimieren."
page_type: reference
---

# Verschlüsselung des Bezeichners auf Feldebene

> Mit der Verschlüsselung auf Bezeichnerfeld-Ebene können Sie E-Mail-Adressen nahtlos mit dem AWS Key Management Service (KMS) verschlüsseln, um die in Braze freigegebenen personenbezogenen Daten (PII) zu minimieren. Bei der Verschlüsselung werden sensible Daten durch Chiffretext ersetzt, d.h. durch unlesbare verschlüsselte Informationen.

{% alert important %}
Die Verschlüsselung auf Bezeichner-Feldebene ist als zusätzliches Feature verfügbar. Wenden Sie sich an Ihren Braze-Konto Manager:in, um mit der Verschlüsselung auf Bezeichnerfeld-Ebene zu beginnen.
{% endalert %}

## Funktionsweise

E-Mail-Adressen müssen gehasht und verschlüsselt werden, bevor sie zu Braze hinzugefügt werden. Wenn eine Nachricht gesendet wird, erfolgt ein Aufruf an AWS KMS für die entschlüsselte E-Mail Adresse. Anschließend wird die gehashte E-Mail Adresse in die Metadaten für Zustellungs- und Engagement-Ereignisse eingefügt, um sie mit dem ursprünglichen Nutzer:in zu verknüpfen. So kann Braze E-Mail Analytics tracken. Braze schwärzt alle E-Mail-Adressen im Klartext und speichert die Klartext-E-Mail-Adresse der Nutzer:innen nicht.

## Voraussetzungen

Um die Verschlüsselung auf Bezeichnerfeld-Ebene zu verwenden, müssen Sie Zugriff auf AWS KMS haben, um E-Mail-Adressen [zu verschlüsseln](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) und zu [hacken](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html) **, bevor** Sie sie an Braze senden. 

Führen Sie diese Schritte aus, um Ihre AWS Secret Key-Authentifizierungsmethode einzurichten.

1. Um Ihre ID und Ihren geheimen Zugangsschlüssel abzurufen, [erstellen Sie einen IAM Nutzer:innen und eine Administratorengruppe](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html#create-an-admin) in AWS mit einer Richtlinie für den AWS Key Management Service. Der IAM Nutzer:innen muss über die Berechtigungen [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) und [kms:GenerateMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html) verfügen. Weitere Einzelheiten finden Sie unter [AWS KMS-Berechtigungen](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html).
2. Wählen Sie **Zugangsdaten für Nutzer:innen anzeigen**, um Ihre ID und Ihren geheimen Zugangsschlüssel zu sehen. Notieren Sie sich diese Zugangsdaten irgendwo, oder wählen Sie den Button **Zugangsdaten herunterladen**, da Sie diese eingeben müssen, wenn Sie Ihre AWS KMS-Schlüssel verbinden.
3. Sie müssen KMS in den folgenden AWS Regionen einrichten:
    - **Braze US-Cluster:** `us-east-1`
    - **Braze EU-Cluster:** `eu-central-1`
4. Erstellen Sie im AWS Key Management Service zwei Schlüssel und vergewissern Sie sich, dass der IAM Nutzer:in den Schlüsselverwendungsberechtigungen hinzugefügt ist:
    - **[Verschlüsseln/Entschlüsseln](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk):** Wählen Sie den Typ des **symmetrischen** Schlüssels und die Verwendung des Schlüssels **zum Ver- und Entschlüsseln** aus.
    - **[Hash](https://docs.aws.amazon.com/kms/latest/developerguide/hmac-create-key.html):** Wählen Sie den Typ **Symmetrischer** Schlüssel und **Generieren und überprüfen Sie die** Verwendung des **MAC-Schlüssels**. Die Schlüsselspezifikation sollte lauten **HMAC_256**. Notieren Sie sich nach der Erstellung des Schlüssels irgendwo die HMAC-Schlüssel-ID, da Sie diese in Braze eingeben müssen.

![]({% image_buster /assets/img/field_level_encryption_aws_prereq.png %})

## Schritt 1: Verbinden Sie Ihre AWS KMS-Schlüssel

Gehen Sie im Braze-Dashboard zu **Dateneinstellungen** > **Verschlüsselung auf Feldebene**. Geben Sie für Ihre AWS KMS-Einstellungen Folgendes ein:

- ID des Zugriffsschlüssels
- Geheimer Zugangsschlüssel
- HMAC-Schlüssel ID (kann nach dem Speichern nicht mehr aktualisiert werden)

## Schritt 2: Wählen Sie Ihre verschlüsselten Felder aus

Wählen Sie anschließend **E-Mail Adresse**, um das Feld zu verschlüsseln. 

Wenn die Verschlüsselung für ein Feld aktiviert ist, kann es nicht wieder in ein entschlüsseltes Feld umgewandelt werden. Das bedeutet, dass die Verschlüsselung eine dauerhafte Einstellung ist. Vergewissern Sie sich beim Einrichten der Verschlüsselung für E-Mail-Adressen, dass keine Nutzer:innen über E-Mail-Adressen im Workspace verfügen. Dadurch wird sichergestellt, dass keine E-Mail-Adressen im Klartext in Braze gespeichert werden, wenn Sie das Feature für den Workspace aktivieren.

![]({% image_buster /assets/img/field_level_encryption.png %})

## Schritt 3: Nutzer:innen importieren und aktualisieren

Wenn die Verschlüsselung auf Bezeichner-Feldebene aktiviert ist, müssen Sie die E-Mail Adresse vor dem Hinzufügen zu Braze hacken und verschlüsseln. Vergewissern Sie sich, dass Sie die E-Mail Adresse vor dem Hashing verkleinern. Weitere Einzelheiten finden Sie unter [Nutzer:in-Objekt Attributes](#user-attributes-object).

Wenn Sie Ihre E-Mail Adresse in Braze aktualisieren, sollten Sie den Wert der gehashten E-Mail verwenden, wenn `email` enthalten ist. Dies beinhaltet:

- REST Endpunkte:
    - `/users/track`
    - `/campaigns/trigger/send`
    - `/canvas/trigger/send`
    - `/transactional/v1/campaigns/{campaign_id}/send`
- Hinzufügen oder Aktualisieren von Nutzer:innen über CSV

{% alert note %}
Wenn Sie einen neuen Nutzer:innen mit einer E-Mail Adresse anlegen, müssen Sie `email_encrypted` mit dem verschlüsselten E-Mail Wert des Nutzers hinzufügen. Andernfalls wird der Nutzer:in nicht erstellt. Ähnlich verhält es sich, wenn Sie einem Nutzer:innen, der noch keine E-Mail hat, eine E-Mail-Adresse hinzufügen, müssen Sie `email_encrypted` hinzufügen. Andernfalls wird der Nutzer:innen nicht aktualisiert.
{% endalert %}

## Überlegungen

Diese Features werden bei der Verschlüsselung auf Bezeichnerfeld-Ebene nicht unterstützt:

- Identifizieren und Erfassen von E-Mail-Adressen über SDK
- In-App-Nachricht E-Mail-Erfassungsformulare
- Berichte über Empfänger:in Domains, einschließlich Charts der Email Insights Mailbox-Anbieter
- Filter für E-Mail-Adressen mit regulärem Ausdruck
- Zielgruppen-Synchronisation
- Shopify Integration

### Nutzer:innen Attribute Objekt

Wenn Sie die Verschlüsselung auf Bezeichnerfeld-Ebene mit dem Endpunkt `/users/track` verwenden, beachten Sie diese Felddetails für das [Objekt Nutzer:in]({{site.baseurl}}/api/objects_filters/user_attributes_object):

- Das Feld `email` muss der Hash-Wert der E-Mail sein.
- Das Feld `email_encrypted` muss der verschlüsselte Wert für die E-Mail sein.

## Häufig gestellte Fragen

### Was ist der Unterschied zwischen Verschlüsseln und Hashing?

Bei der Verschlüsselung handelt es sich um eine zweiseitige Funktion, bei der Daten ver- und entschlüsselt werden können. Wenn derselbe Klartextwert mehrmals verschlüsselt wird, ergibt der Verschlüsselungsalgorithmus von AWS (AES-256-GCM) unterschiedliche verschlüsselte Werte. Hashing ist eine Einwegfunktion, bei der der Klartext so verschlüsselt wird, dass er nicht entschlüsselt werden kann. Hashing ergibt jedes Mal den gleichen Wert. Dies erlaubt es uns, den Status von Abos für mehrere Nutzer:innen zu verwalten, die dieselbe E-Mail Adresse haben.

### Welche E-Mail Adresse sollte ich für meinen Testversand verwenden?

E-Mail-Adressen im Klartext werden beim Testversand unterstützt. Um zu sehen, wie eine E-Mail für einen bestimmten Nutzer:innen aussieht, gehen Sie wie folgt vor:

1. Wählen Sie **Vorschau der Nachricht als Nutzer**: **in**.
2. Wählen Sie in **Test senden** die Option **Attribute des Empfängers mit den Attributen des Nutzers:in der aktuellen Vorschau überschreiben**.

{%raw%}
### Was passiert, wenn ich diese E-Mail Adresse Liquid `{{${email_address}}}` in Braze hinzufüge?

Braze rendert die Klartext-E-Mail-Adresse beim Senden der E-Mail. In der Vorschau zeigen wir Ihnen die verschlüsselte Version der E-Mail an. Wir empfehlen die Verwendung der externen ID des Nutzers:innen, wenn Sie in einer angepassten One-Click-URL auf einen Nutzer verweisen.

`{{${email_address}}}` wird derzeit im Einstellungscenter und auf den Abmeldeseiten nicht unterstützt.
{%endraw%}

### Welche E-Mail Adresse sollte ich in Currents sehen?

Die gehashte E-Mail-Adresse wird in E-Mail-Zustellung und Engagement-Ereignisse einbezogen.

### Welche E-Mail Adresse sollte ich bei der Archivierung von Nachrichten erwarten?

Die Klartext-E-Mail-Adresse wird in die Archivierung von Messaging aufgenommen. Diese werden direkt an den Anbieter des Cloud-Speichers des Kunden gesendet, und die E-Mails können weitere persönliche Daten enthalten.

### Kann ich mail-to list-unsubscribe für das Abo-Management mit Verschlüsselung auf Bezeichnerfeld-Ebene verwenden?

Nein. Die Verwendung von mail-to list-unsubscribe würde die im Klartext entschlüsselte E-Mail Adresse an Braze senden. Wenn die Verschlüsselung auf Bezeichnerfeld-Ebene aktiviert ist, unterstützen wir die URL-basierte HTTP:-Methode, einschließlich One-Click. Wir empfehlen außerdem, einen Link zum Abmelden mit einem Klick in Ihre E-Mail aufzunehmen.

### Unterstützt die Verschlüsselung auf Bezeichner-Feldebene auch andere Bezeichner wie das Telefon?

Nein. Derzeit wird die Verschlüsselung auf Bezeichnerfeld-Ebene nur für E-Mail-Adressen unterstützt.
