---
nav_title: ViralSweep
article_title: ViralSweep
alias: /partners/viralsweep/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und ViralSweep, einem Softwareservice, der es Marken ermöglicht, digitale Marketingaktionen wie Verlosungen, Wettbewerbe, Sofortgewinne, Wartelisten, Empfehlungsaktionen und mehr zu erstellen, durchzuführen und zu verwalten."
page_type: partner
search_tag: Partner

---

# ViralSweep

> [ViralSweep](https://viralsweep.com) ist ein Softwareservice, mit dem Marken digitale Marketingaktionen wie Verlosungen, Wettbewerbe, Sofortgewinne, Wartelisten, Empfehlungsaktionen und vieles mehr erstellen, durchführen und verwalten können. 

Die Integration von Braze und ViralSweep ermöglicht es Ihnen, Gewinnspiele und Wettbewerbe auf der ViralSweep-Plattform zu veranstalten (und so Ihre E-Mail- und SMS-Listen zu erweitern) und dann die Informationen über die Teilnahme an Gewinnspielen oder Wettbewerben an Braze zu senden, um sie in Kampagnen oder Canvases zu verwenden. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| ViralSweep Konto | Ein ViralSweep-Konto, das den Geschäftsplan nutzt, ist erforderlich, um diese Partnerschaft zu nutzen. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit allen Benutzerdaten und E-Mail-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
|Braze REST Endpunkt | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der Braze-URL für Ihre [Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1 : Verbindung zu Braze innerhalb von ViralSweep

Navigieren Sie in ViralSweep zu **Integrationen > E-Mail & SMS > Service hinzufügen** und wählen Sie **Braze**. 

![][1]

### Schritt 2 : Braze Credentials hinzufügen

Geben Sie im Fenster für die Integrationskonfiguration Ihren Braze REST API-Schlüssel und Ihren REST-Endpunkt an. Vergewissern Sie sich, dass der von Ihnen angegebene Endpunkt nicht `https://` enthält, zum Beispiel `dashboard-03.braze.com`. 

![ViralSweep Service-Integrationsseite, die den Benutzer zur Eingabe des Braze API-Schlüssels und der Braze Dashboard-URL auffordert.][2]{: style="max-width:40%;"}

Klicken Sie auf **Verbinden**.

### Schritt 3 : Braze Credentials hinzufügen
Sie sind verbunden! Die Aktion ist jetzt mit Braze verbunden, und alle von ViralSweep gesammelten Einträge werden automatisch an Braze gesendet.

## Häufig gestellte Fragen

### Welche Felder übergibt ViralSweep an Braze?
- Vorname
- Nachname
- E-Mail-Adresse
- Adresse
- Adresse 2
- Ort
- Staat
- Reißverschluss
- Land
- Geburtsdatum
- Tel.
- Werbe-ID
- Empfehlungs-Link
- Name der Verfolgungskampagne

### Werden die Abonnenten von ViralSweep aktualisiert?
Ja. Wenn Sie eine Werbeaktion durchführen und ViralSweep jemanden an Braze weiterleitet und Sie dann in Zukunft eine weitere Werbeaktion durchführen und dieselbe Person teilnimmt, werden die Informationen dieser Person in Braze automatisch aktualisiert (sofern neue Informationen bereitgestellt werden). Hauptsächlich wird die Empfehlungs-URL mit der neuesten URL für jede Aktion, die sie eingeben, aktualisiert, und das Feld Aktions-ID enthält die ID aller Aktionen, die sie eingegeben haben.

## Fehlersuche

Wenn Sie eine Verbindung zu Braze hergestellt haben und Ihrem Konto keine Daten hinzugefügt werden, kann dies daran liegen:

- **E-Mail existiert bereits in Braze**<br>
Die E-Mail-Adresse, die Sie für die Aktion eingegeben haben, befindet sich möglicherweise bereits in Ihrem Braze-Konto. Sie wird also nicht erneut hinzugefügt, sondern nur aktualisiert, wenn Sie neue Informationen für diesen Kontakt angeben.<br><br>
- **E-Mail bereits in ViralSweep eingegeben**<br>
Die E-Mail-Adresse, die Sie für die Aktion eingegeben haben, wurde bereits zuvor eingegeben, so dass sie nicht erneut an Braze übermittelt wird. Dies kann passieren, wenn Sie Ihre Braze-Integration einrichten, nachdem Sie bereits an der Aktion teilgenommen haben.

[1]: {% image_buster /assets/img/viralsweep/connect.gif %}
[2]: {% image_buster /assets/img/viralsweep/connect2.png %}
