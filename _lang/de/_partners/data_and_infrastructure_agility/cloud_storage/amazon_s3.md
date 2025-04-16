---
nav_title: Amazon S3
article_title: Amazon S3
alias: /partners/amazon_s3/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Amazon S3, einem hochskalierbaren Speichersystem, das von Amazon Web Services angeboten wird."
page_type: partner
search_tag: Partner

---

# Amazon S3

> [Amazon S3](https://aws.amazon.com/s3/) ist ein hoch skalierbares Speichersystem, das von Amazon Web Services angeboten wird.



- 
- 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Amazon S3-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Amazon S3-Konto. |
| Dedizierter S3 Bucket | Bevor Sie die Integration mit Amazon S3 vornehmen, müssen Sie einen S3-Bucket für Ihre App erstellen.<br><br>Wenn Sie bereits einen S3-Bucket haben, empfehlen wir Ihnen dennoch, einen neuen Bucket speziell für Braze zu erstellen, damit Sie die Berechtigungen einschränken können. Lesen Sie die folgende Anleitung, wie Sie einen neuen Eimer erstellen. |
| Currents | Um Daten zurück in Amazon S3 exportieren zu können, müssen Sie [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 



1.  
2.  
3.  
4. Sie werden aufgefordert, Ihren Bucket zu erstellen und eine Region auszuwählen.

{% alert note %}

{% endalert %}

## Integration

 

- [AWS-Methode für den geheimen Zugriffsschlüssel](#aws-secret-key-auth-method)
- [AWS-Rolle ARN-Methode](#aws-role-arn-auth-method)

## AWS Geheimschlüssel-Authentifizierungsmethode

Diese Authentifizierungsmethode generiert einen geheimen Schlüssel und eine Zugriffsschlüssel-ID, die es Braze ermöglicht, sich als Benutzer Ihres AWS-Kontos zu authentifizieren, um Daten in Ihren Bucket zu schreiben.

### Schritt 1: Benutzer erstellen {#secret-key-1}

Um Ihre Zugangsschlüssel-ID und Ihren geheimen Zugangsschlüssel abzurufen, müssen Sie [einen IAM-Benutzer und eine Administratorengruppe in AWS anlegen](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html).

### Schritt 2: Anmeldeinformationen erhalten {#secret-key-2}

 

![][11]

### Schritt 3: Richtlinie erstellen {#secret-key-3}

  Dadurch erhalten Sie eingeschränkte Berechtigungen, so dass Braze nur auf die angegebenen Buckets zugreifen kann. 

![][12]

{% alert note %}

{% endalert %}

Geben Sie den Namen einer Richtlinie Ihrer Wahl an und fügen Sie den folgenden Codeschnipsel in den Abschnitt **Richtliniendokument** ein. Stellen Sie sicher, dass Sie `INSERTBUCKETNAME` durch den Namen Ihres Eimers ersetzen. Ohne diese Berechtigungen wird die Integration bei der Prüfung der Anmeldeinformationen scheitern und nicht erstellt werden.

{% tabs %}
{% tab Lötende Ströme %}
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
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```
{% endtab %}
{% tab Dashboard Daten Export %}
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
{% endtab %}
{% endtabs %}

### Schritt 4: Police beifügen {#secret-key-4}

  

![][13]

### Schritt 5: Verknüpfung von Braze mit AWS {#secret-key-5}

{% tabs %}
{% tab Lötende Ströme %}





 

![]({{site.baseurl}}/assets/img/currents-s3-example.png)

{% alert warning %}
Halten Sie Ihre AWS-Zugangsschlüssel-ID und Ihren geheimen Zugangsschlüssel auf dem neuesten Stand. Wenn die Anmeldeinformationen Ihres Connectors ablaufen, wird der Connector keine Ereignisse mehr senden. Wenn dies länger als **48 Stunden** andauert, werden die Ereignisse des Connectors gelöscht und die Daten gehen dauerhaft verloren.
{% endalert %}

Sie können auch die folgenden Anpassungen nach Ihren Wünschen vornehmen:

- **Ordner Pfad:** Die Standardeinstellung ist `currents`. Wenn dieser Ordner nicht existiert, wird Braze ihn automatisch für Sie erstellen. 
- **Server-seitige AES-256-Verschlüsselung im Ruhezustand:** Die Standardeinstellung ist AUS und enthält die Kopfzeile `x-amz-server-side-encryption`.



Eine Benachrichtigung informiert Sie darüber, ob Ihre Anmeldedaten erfolgreich validiert wurden. AWS S3 sollte nun für Braze Currents eingerichtet sein.

{% endtab %}
{% tab Dashboard Daten Export %}



 

![]({{site.baseurl}}/assets/img/s3_tech_partners.png)

{% alert tip %}

{% endalert %}

Eine Benachrichtigung informiert Sie darüber, ob Ihre Anmeldedaten erfolgreich validiert wurden. AWS S3 sollte nun in Ihr Braze-Konto integriert sein.

{% endtab %}
{% endtabs %}

## AWS-Rolle ARN Auth-Methode



### Schritt 1: Richtlinie erstellen {#role-arn-1}

Um loszulegen, melden Sie sich bei der AWS Verwaltungskonsole als Account Administrator an. 

![]({{site.baseurl}}/assets/img/create_policy_1_list.png)

{% alert note %}

{% endalert %}

Öffnen Sie die Registerkarte **JSON** und geben Sie den folgenden Codeschnipsel in den Abschnitt **Policy Document** ein. Stellen Sie sicher, dass Sie `INSERTBUCKETNAME` durch den Namen Ihres Eimers ersetzen. Wählen Sie **Richtlinie überprüfen**, wenn Sie fertig sind.

{% tabs %}
{% tab Lötende Ströme %}

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
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% tab Dashboard Daten Export %}

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

{% endtab %}
{% endtabs %}



![]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### Schritt 2: Rolle erstellen {#role-arn-2}



![]({{site.baseurl}}/assets/img/create_role_1_list.png)

Rufen Sie Ihre Braze-Konto-ID und Ihre externe ID von Ihrem Braze-Konto ab:
- **Ströme**:   Hier finden Sie die Identifikatoren, die Sie zur Erstellung Ihrer Rolle benötigen.
- **Export von Dashboard-Daten**:  

Zurück in der AWS-Konsole wählen Sie **Anderes AWS-Konto** als Auswahltyp für die vertrauenswürdige Entität. Geben Sie Ihre Braze-Konto-ID an, markieren Sie das Feld **Externe ID erforderlich** und geben Sie die externe Braze-ID ein. Wählen Sie nach Abschluss **Weiter** aus.

![Die S3-Seite "Rolle erstellen". Diese Seite enthält Felder für den Rollennamen, die Rollenbeschreibung, vertrauenswürdige Entitäten, Richtlinien und die Berechtigungsgrenze.]({{site.baseurl}}/assets/img/create_role_2_another.png)

### Schritt 3: Police beifügen {#role-arn-3}

Als Nächstes verknüpfen Sie die zuvor erstellte Richtlinie mit der Rolle. Suchen Sie die Police in der Suchleiste und setzen Sie ein Häkchen neben die Police, um sie anzuhängen. Wählen Sie nach Abschluss **Weiter** aus.

![Rollen-ARN]({{site.baseurl}}/assets/img/create_role_3_attach.png)



![Rollen-ARN]({{site.baseurl}}/assets/img/create_role_4_name.png)

Sie sollten nun Ihre neu erstellte Rolle in der Liste sehen.

### Schritt 4: Link zu Braze AWS {#role-arn-4}

In der AWS-Konsole finden Sie Ihre neu erstellte Rolle in der Liste. 

![]({{site.baseurl}}/assets/img/create_role_5_created.png)

Achten Sie auf den **ARN der Rolle** oben auf der Seite mit der Rollenübersicht.

![]({{site.baseurl}}/assets/img/create_role_6_summary.png)

Kehren Sie zu Ihrem Braze-Konto zurück und kopieren Sie die Rollen-ARN in das dafür vorgesehene Feld.

{% tabs %}
{% tab Lötende Ströme %}

 

![]({{site.baseurl}}/assets/img/currents-role-arn.png)

Geben Sie Ihrem Strom einen Namen. 

Sie können auch die folgenden Anpassungen nach Ihren Wünschen vornehmen:

- Ordnerpfad (Standardeinstellung: `currents`)
- Serverseitige AES-256-Verschlüsselung im Ruhezustand (Standardeinstellung: OFF) - Enthält den `x-amz-server-side-encryption` Header

  AWS S3 sollte nun für Braze Currents eingerichtet sein.

{% alert important %}
Wenn Sie die Fehlermeldung "S3-Anmeldeinformationen sind ungültig" erhalten, kann dies daran liegen, dass Sie sich nach der Erstellung einer Rolle in AWS zu schnell integriert haben. Warten Sie und versuchen Sie es erneut.
{% endalert %}

{% endtab %}
{% tab Dashboard Daten Export %}



![]({{site.baseurl}}/assets/img/data-export-role-arn.png)

Vergewissern Sie sich auf der Seite **AWS Credentials**, dass das Optionsfeld **AWS Role ARN** ausgewählt ist, und geben Sie dann Ihren Rollen-ARN und den Namen Ihres AWS S3-Buckets in die entsprechenden Felder ein. 

{% alert tip %}

{% endalert %}

Eine Benachrichtigung informiert Sie darüber, ob Ihre Anmeldedaten erfolgreich validiert wurden. AWS S3 sollte nun in Ihr Braze-Konto integriert sein.

{% endtab %}
{% endtabs %}

## Verhalten beim Exportieren

Benutzer, die eine Cloud-Datenspeicherlösung integriert haben und versuchen, APIs, Dashboard-Berichte oder CSV-Berichte zu exportieren, haben folgende Probleme:

- Alle API-Exporte geben keine Download-URL im Antwortkörper zurück und müssen über den Datenspeicher abgerufen werden.
- Alle Dashboard-Berichte und CSV-Berichte werden zum Download an die E-Mail des Benutzers gesendet (keine Speicherberechtigungen erforderlich) und auf dem Datenspeicher gesichert. 

## Mehrere Anschlüsse

Wenn Sie mehr als einen Currents-Connector erstellen möchten, um ihn an Ihren S3-Bucket zu senden, können Sie dieselben Anmeldedaten verwenden, müssen aber für jeden einen anderen Ordnerpfad angeben. Diese können in demselben Arbeitsbereich erstellt werden oder aufgeteilt und in mehreren Arbeitsbereichen erstellt werden. Sie haben auch die Möglichkeit, für jede Integration eine eigene Richtlinie zu erstellen, oder eine Richtlinie zu erstellen, die beide Integrationen abdeckt. 

Wenn Sie dasselbe S3-Bucket sowohl für Currents als auch für Datenexporte verwenden möchten, müssen Sie zwei separate Richtlinien erstellen, da jede Integration unterschiedliche Berechtigungen erfordert.


[11]: {% image_buster /assets/img_archive/S3_Credentials.png %}
[12]: {% image_buster /assets/img_archive/S3_CreatePolicy.png %}
[13]: {% image_buster /assets/img_archive/S3_AttachPolicy.png %}
