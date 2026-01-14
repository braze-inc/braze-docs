---
nav_title: Fehlerbehebung beim Export
article_title: Fehlerbehebung beim Exportieren
page_order: 10
page_type: reference
description: "Dieser Artikel behandelt einige häufige Szenarien zur Fehlerbehebung bei API- und CSV-Exporten."

---

# Fehlerbehebung beim Export

> Diese Seite listet Fehlermeldungen auf, die beim Exportieren von Daten über CSV oder API von Braze auftreten können.

## Häufige Fehler

### 'AccessDenied' 

#### Wenn Sie Ihren eigenen S3-Bucket verwenden

Wenn Sie **Ihren eigenen S3-Bucket** verwenden, kann dies aus folgenden Gründen passieren:

- Das erwartete Objekt befindet sich nicht mehr im S3-Bucket; fragen Sie Ihre Techniker.
- Die konfigurierten S3-Anmeldedaten im Braze-Dashboard haben nicht die richtigen Berechtigungen. Bestätigen Sie die richtigen Zugangsdaten mit Ihrem Team.

#### Wenn Sie Ihren S3-Bucket von Braze verwenden

Wenn Sie einen **S3-Bucket von Braze** verwenden, kann dies aus folgenden Gründen passieren:

- Das Objekt ist nicht mehr da. Dies könnte passieren, wenn Sie auf einen Link für einen Export geklickt haben, der abgelaufen ist, da Dateien automatisch aus S3 gelöscht werden, wenn der Download-Link abläuft. Wenn nicht anders angegeben, werden die Dateien nach vier Stunden gelöscht. Wenn dies der Fall ist, führen Sie den Export erneut durch.
- Sie haben den Download-Link sofort ausgewählt, bevor S3 bereit war, das Objekt zu handhaben. Warten Sie ein paar Minuten und versuchen Sie es erneut. Größere Berichte dauern in der Regel länger. 
- Der Export ist zu groß, sodass unserem Server bei dem Versuch, die Zip-Datei zu erstellen, der Speicher ausgegangen ist. Wir senden dem Benutzer, der den Export versucht, in diesem Fall automatisch eine E-Mail. Wenn Sie immer wieder auf dieses Problem stoßen, empfehlen wir Ihnen, in Zukunft Ihre eigenen S3-Buckets zu verwenden.

### 'ExpiredToken'

Dies geschieht, wenn die E-Mail vor so langer Zeit gesendet wurde, dass die S3-Datei abgelaufen ist. Wenn nicht anders angegeben, werden die Dateien nach vier Stunden gelöscht. Führen Sie den Export erneut aus und laden Sie ihn herunter, bevor die Datei abläuft.

Eine weitere Ursache könnte sein, dass Braze keinen Zugriff mehr auf den S3-Bucket hat, in den Sie die Daten herunterladen. Vergewissern Sie sich mit dieser Anleitung, dass Sie Ihre S3-Zugangsdaten aktualisiert haben.

### "Sieht aus, als würde die Datei nicht mehr existieren. Bitte überprüfen Sie, ob Objekte aus Ihrem Bucket gelöscht werden.

Es kann zu einer leichten Verzögerung zwischen dem E-Mail-Versand durch Braze mit dem Export und der tatsächlichen Bereitschaft von S3 kommen, das Objekt zu handhaben. Wenn Sie diese Fehlermeldung sehen, warten Sie ein paar Minuten, bevor Sie es erneut versuchen.

### Apostrophe zu Feldern hinzugefügt

Braze stellt einem Feld im CSV-Export automatisch ein Hochkomma voran, wenn das Feld mit einem der folgenden Zeichen beginnt:

- -
- =
- +
- @

Zum Beispiel wird das Feld "-1943" als "'-1943" exportiert. Dies gilt nicht für JSON-Exporte, die etwa vom [Endpunkt`/users/export/segment` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) zurückgegeben werden.