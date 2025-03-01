---
nav_title: Friendbuy
article_title: Friendbuy
description: "Erfahren Sie, wie Sie Friendbuy mit Braze integrieren können."
alias: /partners/friendbuy/
page_type: partner
search_tag: Partner

---

# Friendbuy

> Nutzen Sie die Integration zwischen Friendbuy und Braze, um Ihre E-Mail- und SMS-Möglichkeiten zu erweitern und gleichzeitig die Kommunikation Ihrer Empfehlungs- und Treueprogramme mühelos zu automatisieren. Braze erstellt Kundenprofile für alle über Friendbuy gesammelten Opt-in-Telefonnummern.

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung          | Beschreibung                                                                                                                              |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Ein Friendbuy-Konto   | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Friendbuy-Konto][1].                                                              |
| Ein Braze REST API Schlüssel  | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden.        |
| Ein Braze REST Endpunkt | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints), die von der URL für Ihre Braze-Instanz abhängt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, können Sie einen API-Schlüssel unter **Entwicklerkonsole** > **API-Einstellungen** erstellen.
{% endalert %}

## Friendbuy einbinden

Gehen Sie in [Friendbuy][1] zu **Developer Center** > **Integrationen** und wählen Sie dann auf der Braze-Integrationskarte **Integration hinzufügen**.

![Die Braze Integrationskarte in Friendbuy.][100]{: style="max-width:75%;"}

Geben Sie in das Formular Ihren REST-Endpunkt und Ihren API-Schlüssel ein und wählen Sie dann **Integration installieren**.

![Das Friendbuy-Integrationsformular.][101]{: style="max-width:55%;"}

Gehen Sie zurück zu Ihrem [Friendbuy-Konto][1] und aktualisieren Sie die Seite. Wenn Ihre Integration erfolgreich war, sehen Sie eine Meldung ähnlich der folgenden:

![Integration installiert][102]{: style="max-width:55%;"}

### Angepasste Attribute

| Name des angepassten Attributs            | Definition                                                                                                                                         | Datentyp |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| **Friendbuy-Empfehlungsstatus**    | Referrer werden als *Advocate* und Referees als *Referred Friend* kategorisiert.                                                          | String    |
| **Friendbuy Kundenname**      | Der Name, den der Kunde eingegeben hat, als er seine Daten über ein Empfehlungs-Widget einreichte                                                                 | String    |
| **Friendbuy Empfehlungslink**      | Ein persönlicher Empfehlungslink (PURL), der für einen Advocate erstellt wurde. Zum Beispiel, https://fbuy.io/EzcW                                                       | String    |
| **Friendbuy Datum der letzten Aktie** | Das Datum und die Uhrzeit, zu der der Advokat das letzte Mal über einen beliebigen Freigabekanal mit einem Freund geteilt hat. Wenn der Advokat noch nicht geteilt hat, wird die Immobilie nicht sichtbar sein. | Uhrzeit      |
| **Friendbuy-Kampagnen-ID**        | Die Kampagnen-ID, die mit dem persönlichen Empfehlungslink verbunden ist, der für einen Advocate erstellt wurde                                                               | String    |
| **Name der Friendbuy-Kampagne**      | Der Kampagnenname, der mit dem persönlichen Empfehlungslink für einen Advocate verknüpft ist                                                             | String    |
| **Friendbuy Coupon Code**        | Der letzte an den Kunden verteilte Empfehlungsgutscheincode. Hinweis: Es wird nur ein Code angezeigt                                            | String    |
| **Friendbuy Coupon Wert**       | Der Währungswert des letzten an den Kunden verteilten Gutscheincodes.                                                                     | Nummer    |
| **Friendbuy Coupon Status**      | Der Status des letzten an den Kunden verteilten Gutscheincodes. Hinweis: Der Status wird 'verteilt' oder 'eingelöst'.                            | String    |
| **Friendbuy Coupon Währung**    | Währungscode (USD, CAD, etc.) oder Prozent (%), der mit dem letzten an den Kunden verteilten Gutscheincode verbunden ist.                             | String    |
| **Friendbuy Coupon Kampagnen-ID** | Die Kampagnen-ID, die mit dem für einen Kunden generierten Gutscheincode verbunden ist.                                                                          | String    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Standardverhalten

Bevor Kundendaten an Braze gesendet werden können, müssen sich die Kunden über das Empfehlungs-Widget anmelden, indem sie eines oder mehrere der folgenden Felder ankreuzen:

![Empfehlungs-Widget][103]

{% alert note %}
Friendbuy verwendet den internationalen Standard (E.164), um echte Telefonnummern zu verifizieren. Ungültige Nummern, wie `555-555-5555`, werden nicht an Braze gesendet.
{% endalert %}

### Verhalten bei Checkboxen

| Kontrollkästchen ausgewählt | Verhalten                                                        |
|-------------------|-----------------------------------------------------------------|
| Nur E-Mail        | Nur die E-Mail-Adresse des Kunden wird an Braze gesendet.             |
| Nur Telefon        | Nur die Telefonnummer des Kunden wird an Braze gesendet.              |
| Weder           | Es werden keine Kundendaten an Braze gesendet.                              |
| Beides              | Die E-Mail-Adresse und die Telefonnummer des Kunden werden an Braze gesendet. |

[1]: https://retailer.friendbuy.io/
[100]: {% image_buster /assets/img/friendbuy/choosing_braze.png %}
[101]: {% image_buster /assets/img/friendbuy/install_form.png %}
[102]: {% image_buster /assets/img/friendbuy/install_success.png %}
[103]: {% image_buster /assets/img/friendbuy/referral_widget.png %}
