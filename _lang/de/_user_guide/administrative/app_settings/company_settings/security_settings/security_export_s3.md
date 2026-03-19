---
nav_title: Export von Sicherheitsereignissen mit S3
article_title: Sicherheitseinstellungen Export mit S3
page_order: 1
page_type: reference
description: "Dieser referenzierte Artikel beschreibt, wie Sie jeden Tag um Mitternacht UTC automatisch Sicherheitsereignisse in Amazon S3 exportieren können."
---

# Export von Sicherheitsereignissen mit Amazon S3

> Sie können Sicherheitsereignisse automatisch zu Amazon S3, einem Cloud-Speicheranbieter, exportieren, wobei ein täglicher Job um Mitternacht UTC ausgeführt wird. Nach der Einrichtung ist es nicht erforderlich, Sicherheitsereignisse manuell aus dem Dashboard zu exportieren. Der Job exportiert die Sicherheitsereignisse der letzten 24 Stunden im CSV-Format in Ihren konfigurierten S3-Speicher. Die CSV-Datei weist dieselbe Struktur auf wie ein manuell exportierter Bericht.

{% alert note %}
Die Begrenzung auf 10.000 Zeilen gilt ausschließlich für den manuellen Download von CSV-Berichten über das Dashboard. Sicherheitsereignis-Exporte nach S3 unterliegen dieser Zeilenbegrenzung nicht.
{% endalert %}

Braze unterstützt zwei verschiedene S3-Authentifizierungs- und Autorisierungsmethoden für die Einrichtung des Amazon S3-Exports:

- AWS geheime Zugriffsschlüsselmethode
- AWS Rolle ARN Methode

## AWS geheime Zugriffsschlüsselmethode

Diese Methode generiert einen geheimen Schlüssel und eine Zugriffsschlüssel-ID, die es Braze erlaubt, sich als Nutzer:in Ihrem AWS-Konto zu authentifizieren, um Daten in Ihren Bucket zu schreiben.

### Schritt 1: Erstellen Sie einen Nutzer für die Identitäts- und Zugriffsverwaltung (IAM).

Um Ihren geheimen Zugriffsschlüssel und Ihre Zugriffsschlüssel-ID abzurufen, müssen Sie einen IAM-Nutzer erstellen. Befolgen Sie dazu die Anweisungen unter [Einrichten Ihres AWS-Kontos](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-account-iam.html#create-an-admin).

### Schritt 2: Zugangsdaten abrufen

1. Nachdem Sie einen neuen Nutzer:innen angelegt haben, generieren Sie den Zugangsschlüssel und laden Ihre ID und Ihren geheimen Zugangsschlüssel herunter.

![Eine Übersichtsseite für eine Rolle namens „liyu-chen-test”.]({% image_buster /assets/img/security_export/credentials1.png %})

{: start="2"}
2\. Notieren Sie sich diese Zugangsdaten irgendwo, oder laden Sie die Dateien mit den Zugangsdaten herunter, da Sie diese später in Braze eingeben müssen.

![Felder, die den Zugriffsschlüssel und den geheimen Zugriffsschlüssel enthalten.]({% image_buster /assets/img/security_export/retrieve_access_keys.png %})

### Schritt 3: Richtlinie erstellen

1. Bitte gehen Sie zu **IAM** (Identitäts- und Zugriffsverwaltung) > **Richtlinien** > **Richtlinie erstellen,** um Berechtigungen für Ihre Nutzer:innen hinzuzufügen. 
2. Wählen Sie **Eigene Richtlinie erstellen**, die eingeschränkte Berechtigungen erteilt, so dass Braze nur auf die angegebenen Buckets zugreifen kann.
3. Geben Sie den Namen einer Richtlinie Ihrer Wahl an.
4. Geben Sie den folgenden Code-Snippet in den Abschnitt **Richtlinien-Dokument** ein. Ersetzen Sie "INSERTBUCKETNAME" durch Ihren Bucket-Namen. Ohne diese Berechtigungen schlägt die Integration bei der Prüfung der Zugangsdaten fehl und kann nicht erstellt werden.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME*", "arn:aws:s3:::INSERTBUCKETNAME/", "arn:aws:s3:::INSERTBUCKETNAME"]
        }
    ]
}
```

### Schritt 4: Richtlinie beifügen

1. Nachdem Sie eine neue Richtlinie erstellt haben, gehen Sie zu **Nutzer:innen** und wählen Sie Ihren speziellen Nutzer aus. 
2. Wählen Sie auf dem Tab **Berechtigungen** die Option **Berechtigungen hinzufügen**, fügen Sie die Richtlinie direkt hinzu und wählen Sie dann diese Richtlinie aus. 

Jetzt können Sie Ihre AWS-Zugangsdaten mit Ihrem Braze-Konto verknüpfen!

### Schritt 5: Verknüpfung von Braze mit AWS

1. Gehen Sie in Braze zu **Einstellungen** > **Unternehmenseinstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen** und blättern Sie zum Abschnitt **Sicherheitsereignis-Download**.
2. Schalten Sie **Export zu AWS S3** unter **Export in Cloud-Speicher** um und wählen Sie den **geheimen AWS-Zugangsschlüssel** aus, der den S3-Export ermöglicht. 
3. Geben Sie Folgendes ein:
- AWS-Zugriffsschlüssel-ID
- Geheimer Zugriffsschlüssel für AWS
    - Wenn Sie diesen Schlüssel eingeben, wählen Sie zunächst **Zugangsdaten testen** aus, um zu bestätigen, dass Ihre Zugangsdaten funktionieren.
- AWS Bucket-Name 

![Die Seite „Sicherheitsereignis-Download“ mit ausgefüllten Braze-Konto- und Braze-externen IDs.]({% image_buster /assets/img/security_export/security_event_download1.png %})

{: start="4"}
4\. Wählen Sie **Änderungen speichern**. 

![Button „Änderungen speichern“.]({% image_buster /assets/img/security_export/save_changes_button.png %}){: style="max-width:50%;"}

Sie haben AWS S3 in Ihr Braze-Konto integriert!

## AWS Rolle ARN Methode

Die AWS-Rollen-ARN-Methode generiert einen Rollen-Amazon-Ressourcennamen (ARN), der es dem Braze-Amazon-Konto erlaubt, sich als Mitglied dieser Rolle zu authentifizieren.

### Schritt 1: Richtlinie erstellen

1. Melden Sie sich bei der AWS Verwaltungskonsole als Account Manager an. 
2. Bitte gehen Sie in der AWS-Konsole zum Abschnitt **„IAM** (Identity and Access Management)“ > **„Richtlinien“** und wählen Sie **„Create Policy“** aus.

![Eine Seite mit einer Liste von Richtlinien und einem Button zum Erstellen einer Richtlinie.]({% image_buster /assets/img/security_export/policies.png %})

{: start="3"}
3\. Öffnen Sie den Tab **JSON** und geben Sie den folgenden Code-Snippet in den Abschnitt **Richtliniendokument** ein. Ersetzen Sie `INSERTBUCKETNAME` durch Ihren Bucket-Namen. 

```json
  {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject","s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{: start="4"}
4\. Wählen Sie nach der Überprüfung der Richtlinie **Weiter** aus.

![Eine Seite, auf der Sie Ihre Richtlinie überprüfen und optional Berechtigungen hinzufügen können.]({% image_buster /assets/img/security_export/specify_permissions.png %})

{: start="5"}
5\. Geben Sie der Richtlinie einen Namen und eine Beschreibung, und wählen Sie dann **Richtlinie erstellen**.

![Eine Seite, auf der Sie Ihre Richtlinie überprüfen und erstellen können.]({% image_buster /assets/img/security_export/review_and_create.png %})

### Schritt 2: Rolle erstellen

1. Gehen Sie in Braze zu **Einstellungen** > **Unternehmenseinstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen** und blättern Sie zum Abschnitt **Sicherheitsereignis-Download**. 
2. Wählen Sie **AWS Role ARN**. 
3. Notieren Sie sich die Bezeichner, die Braze-Konto ID und die externe ID, die Sie zur Erstellung Ihrer Rolle benötigen.

![Die Seite „Sicherheitsereignis-Download“ mit ausgefüllten Braze-Konto- und Braze-externen IDs.]({% image_buster /assets/img/security_export/security_event_download2.png %})

4. Bitte navigieren Sie in der AWS-Konsole zum Abschnitt **„IAM** (Identity and Access Management)“ > **„Roles“** > **„Create Role**“. 
5. Wählen Sie **Anderes AWS-Konto** als SELEKTOR-Typ für die vertrauenswürdige Entität aus. 
6. Geben Sie die ID Ihres Braze-Kontos an, markieren Sie das Kästchen **Externe ID erforderlich** und geben Sie dann Ihre externe ID von Braze ein. 
7. Wählen Sie nach Abschluss **Weiter** aus.

![Eine Seite mit Optionen, um einen vertrauenswürdigen Entitätstyps auszuwählen und Informationen zu Ihrem AWS-Konto anzugeben.]({% image_buster /assets/img/security_export/select_trusted_entity.png %})

### Schritt 3: Richtlinie beifügen

1. Suchen Sie in der Suchleiste nach der Richtlinie, die Sie zuvor erstellt haben, und setzen Sie dann ein Häkchen neben die Richtlinie, um sie anzuhängen. 
2. Wählen Sie **Weiter**.

![Eine Liste von Richtlinien mit Spalten für deren Typ und Beschreibung.]({% image_buster /assets/img/security_export/add_permissions.png %})

{: start="3"}
3\. Geben Sie der Rolle einen Namen und eine Beschreibung, und wählen Sie **Rolle erstellen**.

![Felder zur Angabe von Rollendetails, wie Name, Beschreibung, Vertrauensrichtlinie, Berechtigungen und Tags.]({% image_buster /assets/img/security_export/name_review_create.png %})

Ihre neu erstellte Rolle wird in der Liste erscheinen!

### Schritt 4: Link zu Braze AWS

1. In der AWS-Konsole finden Sie Ihre neu erstellte Rolle in der Liste. Wählen Sie den Namen aus, um die Details zu dieser Rolle zu öffnen, und notieren Sie sich den **ARN**.

![Die Übersichtsseite für eine Rolle namens „security-event-export-olaf”.]({% image_buster /assets/img/security_export/credentials2.png %})

{: start="2"}
2\. Gehen Sie in Braze zu **Einstellungen** > **Unternehmenseinstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen** und blättern Sie zum Abschnitt **Sicherheitsereignis-Download**.

![Abschnitt „Sicherheitsereignis herunterladen“ mit umgeschalteter Option „Nach AWS S3 exportieren“.]({% image_buster /assets/img/security_export/security_event_download3.png %})

{: start="3"}
3\. Vergewissern Sie sich, dass die **AWS-Rolle ARN** ausgewählt ist, und geben Sie dann Ihren Rollen-ARN und den AWS S3 Bucket-Namen in die entsprechenden Felder ein.
4\. Wählen Sie **Zugangsdaten testen**, um zu bestätigen, dass Ihre Zugangsdaten richtig funktionieren.
5\. Wählen Sie **Änderungen speichern**. 

![Button „Änderungen speichern“.]({% image_buster /assets/img/security_export/save_changes_button.png %}){: style="max-width:40%;"}

Sie haben AWS S3 in Ihr Braze-Konto integriert!