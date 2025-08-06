---
nav_title: ViralSweep
article_title: ViralSweep
alias: /partners/viralsweep/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und ViralSweep, einem Software-Dienst, der es Marken erlaubt, digitale Marketing Aktionen wie Gewinnspiele, Wettbewerbe, Sofortgewinne, Wartelisten, Empfehlungen und mehr zu erstellen, durchzuführen und zu verwalten."
page_type: partner
search_tag: Partner

---

# ViralSweep

> [ViralSweep](https://viralsweep.com) ist ein Software-Dienst, der es Marken erlaubt, digitale Marketing Aktionen wie Verlosungen, Wettbewerbe, Sofortgewinne, Wartelisten, Empfehlungen und vieles mehr zu erstellen, durchzuführen und zu verwalten. 

_Diese Integration wird von ViralSweep gepflegt._

## Über die Integration

Die Integration von Braze und ViralSweep ermöglicht es Ihnen, Gewinnspiele und Wettbewerbe auf der ViralSweep-Plattform zu veranstalten (und so Ihre E-Mail- und SMS-Listen zu erweitern) und dann die Informationen über den Eingang von Gewinnspielen oder Wettbewerben an Braze zu senden, um sie in Kampagnen oder Canvase zu verwenden. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| ViralSweep Konto | Um diese Partnerschaft zu nutzen, benötigen Sie ein ViralSweep-Konto, das den Geschäftsplan verwendet. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit allen Nutzerdaten und E-Mail-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
|Braze REST Endpunkt | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der Braze-URL für [Ihre Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1 : Verbinden Sie sich mit Braze innerhalb von ViralSweep

Navigieren Sie in ViralSweep zu **Integrationen > E-Mail & SMS > Dienst hinzufügen** und wählen Sie **Braze** aus. 

![]({% image_buster /assets/img/viralsweep/connect.gif %})

### Schritt 2 : Braze Zugangsdaten hinzufügen

Geben Sie im Fenster zur Konfiguration der Integrationen Ihren REST API-Schlüssel und den REST-Endpunkt von Braze an. Vergewissern Sie sich, dass der von Ihnen angegebene Endpunkt nicht `https://` enthält, zum Beispiel `dashboard-03.braze.com`. 

![ViralSweep Seite zur Integration von Diensten, die den Nutzer:innen zur Eingabe des Braze API-Schlüssels und der URL des Braze-Dashboards auffordert.]({% image_buster /assets/img/viralsweep/connect2.png %}){: style="max-width:40%;"}

Klicken Sie auf **Verbinden**.

### Schritt 3 : Braze Zugangsdaten hinzufügen
Sie sind verbunden! Die Aktion ist jetzt mit Braze verbunden, und alle Eingänge, die von ViralSweep gesammelt werden, werden automatisch an Braze gesendet.

## Häufig gestellte Fragen

### Welche Felder werden von ViralSweep an Braze weitergegeben?
- Vorname
- Nachname
- E-Mail-Adresse
- Adresse
- Adresse 2
- Ort
- Status
- Reißverschluss
- Land
- Geburtsdatum
- Telefon
- Aktion ID
- Empfehlung Link
- Name der Tracking Kampagne

### Werden Abonnent:innen von ViralSweep aktualisiert?
Ja Wenn Sie eine Aktion durchführen und ViralSweep jemanden an Braze weiterleitet und Sie in Zukunft eine weitere Aktion durchführen und dieselbe Person daran teilnimmt, werden die Informationen dieser Person automatisch in Braze aktualisiert (sofern neue Informationen bereitgestellt werden). Hauptsächlich wird die URL der Empfehlung mit der neuesten URL für jede Aktion, die sie eingeben, aktualisiert, und das Feld für die ID der Aktion enthält die ID aller Aktionen, die sie eingegeben haben.

## Fehlersuche

Wenn Sie eine Verbindung zu Braze hergestellt haben und Ihrem Konto keine Daten hinzugefügt werden, kann das daran liegen:

- **E-Mail existiert bereits in Braze**<br>
Die für die Aktion eingegebene E-Mail Adresse befindet sich möglicherweise bereits in Ihrem Braze-Konto und wird daher nicht erneut hinzugefügt. Sie wird nur aktualisiert, wenn neue Informationen für diesen Kontakt angegeben werden.<br><br>
- **E-Mail bereits in ViralSweep eingegeben**<br>
Die für die Aktion eingegebene E-Mail Adresse wurde bereits zuvor eingegeben und wird daher nicht erneut an Braze übermittelt. Dies kann passieren, wenn Sie die Integration von Braze einrichten, nachdem Sie die Aktion bereits eingegeben haben.


