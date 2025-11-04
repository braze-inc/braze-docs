---
nav_title: Friendbuy
article_title: Friendbuy
description: "Lernen Sie, wie Sie Friendbuy in Braze integrieren können."
alias: /partners/friendbuy/
page_type: partner
search_tag: Partner

---

# Friendbuy

> Nutzen Sie die Integration zwischen Friendbuy und Braze, um Ihre E-Mail- und SMS-Funktionen zu erweitern und gleichzeitig die Kommunikation Ihrer Empfehlungen und Kundenbindungs-Programme mühelos zu automatisieren. Braze erstellt Kundenprofile für alle Opt-in-Telefonnummern, die über Friendbuy erfasst wurden.

_Diese Integration wird von Friendbuy gepflegt._

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung          | Beschreibung                                                                                                                              |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Ein Friendbuy-Konto   | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Friendbuy-Konto](https://retailer.friendbuy.io/).                                                              |
| Ein Braze REST API-Schlüssel  | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden.        |
| Ein Braze REST Endpunkt | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints), die von der URL für Ihre Braze-Instanz abhängt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration von Friendbuy

Gehen Sie in [Friendbuy](https://retailer.friendbuy.io/) zu **Entwickler:in** > **Integrationen** und wählen Sie dann auf der Braze-Integrationskarte **Integration hinzufügen**.

![Die Braze-Integrationskarte in Friendbuy.]({% image_buster /assets/img/friendbuy/choosing_braze.png %}){: style="max-width:75%;"}

Geben Sie in das Formular Ihren REST Endpunkt und API-Schlüssel ein und wählen Sie dann **Integration installieren**.

![Das Formular für die Integration von Friendbuy.]({% image_buster /assets/img/friendbuy/install_form.png %}){: style="max-width:55%;"}

Gehen Sie zurück zu Ihrem [Friendbuy-Konto](https://retailer.friendbuy.io/) und aktualisieren Sie die Seite. Wenn Ihre Integration erfolgreich war, sehen Sie eine Nachricht ähnlich der folgenden:

![Integration installiert]({% image_buster /assets/img/friendbuy/install_success.png %}){: style="max-width:55%;"}

### Angepasste Attribute

| Name des angepassten Attributs            | Definition                                                                                                                                         | Datentyp |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| **Friendbuy-Empfehlungsstatus**    | Empfehlende Personen werden als *Advocate* und referenzierende Personen als *Referred Friend* kategorisiert.                                                          | String    |
| **Friendbuy Kund:in Name**      | Der Name, den die Kund:in bei der Übermittlung ihrer Daten über ein Empfehlungs-Widget eingegeben hat                                                                 | String    |
| **Friendbuy-Empfehlungslink**      | Ein persönlicher Empfehlungslink (PURL), der für einen Advocate erstellt wurde. Zum Beispiel, https://fbuy.io/EzcW                                                       | String    |
| **Friendbuy Datum der letzten Aktie** | Das Datum und die Uhrzeit, zu der der Advokat das letzte Mal über einen beliebigen Kanal mit einem Freund geteilt hat. Wenn der Advokat noch nicht geteilt hat, ist die Eigenschaft nicht sichtbar. | Uhrzeit      |
| **Friendbuy Kampagne ID**        | Die ID der Kampagne, die mit dem für einen Advocate generierten persönlichen Empfehlungslink verknüpft ist                                                               | String    |
| **Friendbuy Kampagne Name**      | Der Kampagnenname, der mit dem für einen Advocate generierten persönlichen Empfehlungslink verknüpft ist                                                             | String    |
| **Friendbuy Coupon Code**        | Der neueste Empfehlungs-Gutscheincode, der an die Kund:in verteilt wird. Hinweis: Es wird nur ein Code angezeigt                                            | String    |
| **Friendbuy Coupon Wert**       | Der Währungswert des letzten an die Kund:in verteilten Gutscheincodes.                                                                     | Zahl    |
| **Friendbuy Coupon Status**      | Der Status des letzten an die Kund:in verteilten Coupon Codes. Hinweis: Der Status wird 'verteilt' oder 'eingelöst'.                            | String    |
| **Friendbuy Coupon Währung**    | Währungscode (USD, CAD, etc.) oder Prozentsatz (%) in Verbindung mit dem letzten an die Kund:in verteilten Gutscheincode.                             | String    |
| **Friendbuy Coupon Kampagne ID** | Die ID der Kampagne, die mit dem für eine Kund:in generierten Coupon Code verknüpft ist.                                                                          | String    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Standard-Verhalten

Bevor Kundendaten an Braze gesendet werden können, müssen die Kunden über das Empfehlungs-Widget ein Opt-in durchführen, indem sie eines oder mehrere der folgenden Kästchen ankreuzen:

![Empfehlungs-Widget]({% image_buster /assets/img/friendbuy/referral_widget.png %})

{% alert note %}
Friendbuy verwendet den internationalen Standard (E.164), um echte Telefonnummern zu überprüfen. Ungültige Nummern, wie z.B. `555-555-5555`, werden nicht an Braze gesendet.
{% endalert %}

### Verhalten bei Checkboxen

| Kontrollkästchen ausgewählt | Verhalten                                                        |
|-------------------|-----------------------------------------------------------------|
| Nur E-Mail        | Nur die E-Mail Adresse der Kund:in wird an Braze gesendet.             |
| Nur Telefon        | Nur die Telefonnummer der Kund:in wird an Braze gesendet.              |
| Weder           | Es werden keine Kundendaten an Braze gesendet.                              |
| Beides              | Die E-Mail Adresse und Telefonnummer der Kund:in wird an Braze gesendet. |


