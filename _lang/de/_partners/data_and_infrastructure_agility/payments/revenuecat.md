---
nav_title: RevenueCat
article_title: RevenueCat
description: "Die Integration von RevenueCat und Braze ermöglicht Ihnen die automatische plattformübergreifende Synchronisierung der Kauf- und Abonnement-Lebenszyklusereignisse Ihrer Kunden. So können Sie Kampagnen erstellen, die auf die Phase des Abonnement-Lebenszyklus Ihrer Kunden reagieren, z. B. indem Sie Kunden ansprechen, die sich während der kostenlosen Testphase abgemeldet haben, oder Erinnerungen an Kunden mit Rechnungsproblemen senden."
alias: /partners/revenuecat/
page_type: partner
search_tag: Partner

---

# RevenueCat

> [RevenueCat](https://www.revenuecat.com/) ist die einzige Quelle der Wahrheit für Ihren Abonnementstatus auf iOS, Android und im Internet. Egal, ob Sie eine neue App entwickeln oder bereits Millionen von Abonnenten haben, Sie können RevenueCat nutzen, um plattformübergreifende In-App-Käufe zu erstellen, Ihre Produkte und Abonnenten zu verwalten und Ihre Daten zu analysieren - ganz ohne Servercode.

Die Integration von RevenueCat und Braze ermöglicht Ihnen die automatische plattformübergreifende Synchronisierung der Kauf- und Abonnement-Lebenszyklusereignisse Ihrer Kunden. So können Sie Kampagnen erstellen, die auf die Phase des Abonnement-Lebenszyklus Ihrer Kunden reagieren, z. B. indem Sie Kunden ansprechen, die sich während der kostenlosen Testphase abgemeldet haben, oder Erinnerungen an Kunden mit Rechnungsproblemen senden.

## Voraussetzungen

Zumindest müssen Sie die Integration über das RevenueCat-Dashboard aktivieren, um RevenueCat mit Braze zu verbinden. Wenn Sie das Braze SDK verwenden, können Sie die SDKs von RevenueCat und Braze zusammen verwenden, um die Integration zu verbessern, indem Sie sicherstellen, dass in beiden Systemen die gleiche Kundenkennung verwendet wird.

| Anforderung | Beschreibung |
|---|---|
| RevenueCat Konto und App | Ein [RevenueCat-Konto][9] ist erforderlich, um die Vorteile dieser Partnerschaft zu nutzen. Sie müssen auch eine konfigurierte RevenueCat-App haben. |
| RevenueCat SDK | Zusätzlich zum erforderlichen Braze SDK empfehlen wir die Installation des [RevenueCat SDK][8] ], um RevenueCat Benutzer-Aliase zur Verfügung zu stellen. |
| Hartlöt-Instanz | Ihre Braze-Instanz erhalten Sie von Ihrem Braze-Onboarding-Manager oder Sie finden sie auf der [API-Übersichtsseite]({{site.baseurl}}/api/basics/#endpoints).<br><br>RevenueCat erfordert, dass die Braze-Instanz serverseitig an den richtigen Braze-REST-Endpunkt sendet. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| REST-API-Schlüssel für den Braze-Test (optional) | Ein Test-API-Schlüssel kann für Test- und Produktionskäufe verwendet werden, wenn Sie möchten, dass diese Anfragen an separate Braze-Instanzen gesendet werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle 

- Starten Sie eine Onboarding-Kampagne, die Ihre Premium-Funktionen hervorhebt, wenn ein Kunde eine kostenlose Testversion beginnt.
- Senden Sie eine Erinnerung zur Aktualisierung der Abrechnungsinformationen, wenn ein Ereignis "Abrechnungsproblem" empfangen wird.
- Senden Sie eine Feedback-Umfrage, nachdem ein Kunde eine kostenlose Testversion gekündigt hat. 

## Integration

### Schritt 1: Braze Benutzeridentität festlegen

Im Braze SDK können Sie die Braze-Benutzer-ID so einstellen, dass sie mit der Benutzer-ID der RevenueCat-App übereinstimmt. Dadurch wird sichergestellt, dass Ereignisse, die von Braze und RevenueCat gesendet werden, mit demselben Benutzer synchronisiert werden können.

Konfigurieren Sie das Braze SDK mit der gleichen App-Benutzer-ID wie RevenueCat oder verwenden Sie die Methode Braze SDK `.changeUser()`.

{% tabs local %}
{% tab schnell %}
```swift
// Configure Purchases SDK
Purchases.configure(withAPIKey: "public_sdk_key", appUserID: "my_app_user_id")

// Change user in Braze SDK
Appboy.sharedInstance()?.changeUser("my_app_user_id")

// Optional User Alias Object attributes
Purchases.shared.setAttributes(["$brazeAliasName" : "name", 
                             "$brazeAliasLabel" : "label"])
```
{% endtab %}
{% tab objektiv-c %}
```objc
// Configure Purchases SDK
[RCPurchases configureWithAPIKey:@"public_sdk_key" appUserID:@"my_app_user_id"];

// Change user in Braze SDK
[[Appboy sharedInstance] changeUser:@"my_app_user_id"];

// Optional User Alias Object attributes
[[RCPurchases sharedPurchases] setAttributes:@{
    @"$brazeAliasName": @"name",
    @"$brazeAliasLabel": @"label"
}];
```
{% endtab %}
{% tab java %}
```java
// Configure Purchases SDK
Purchases.configure(this, "public_sdk_key", "my_app_user_id");

// Change user in Braze SDK
Braze.getInstance(context).changeUser(my_app_user_id);

// Optional User Alias Object attributes
Map<String, String> attributes = new HashMap<String, String>();
attributes.put("$brazeAliasName", "name");
attributes.put("$brazeAliasLabel", "label");

Purchases.getSharedInstance().setAttributes(attributes);
```
{% endtab %}
{% endtabs %}

#### Benutzer-Aliasobjekt an Braze senden (optional) 

Wenn Sie eine andere eindeutige Benutzerkennung als die Benutzer-ID der RevenueCat-App senden möchten, aktualisieren Sie die Benutzer mit den folgenden Daten als RevenueCat-Abonnentenattribute.

| Schlüssel | Beschreibung |
|---|---|
| `$brazeAliasName` | Das Braze `alias_name` im [Benutzer-Alias-Objekt][2] |
| `$brazeAliasLabel` | Das Braze `alias_label` im [Benutzer-Alias-Objekt][2] |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Beide Attribute sind erforderlich, damit das [Benutzer-Aliasobjekt][2] zusammen mit Ihren Ereignisdaten gesendet werden kann. Diese Eigenschaften können wie jedes andere [RevenueCat-Abonnenten-Attribut][4] manuell festgelegt werden. Beispielhafte Codeschnipsel finden Sie in Schritt eins.

### Schritt 2: RevenueCat-Ereignisse an Braze senden

Nachdem Sie das RevenueCat SDK für Einkäufe und das Braze SDK so eingerichtet haben, dass sie dieselbe Benutzeridentität haben, können Sie die Integration aktivieren und die Ereignisnamen im RevenueCat Dashboard konfigurieren.

1. Navigieren Sie zu Ihrem Projekt im RevenueCat Dashboard und suchen Sie die Karte **Integrationen** im linken Menü. Wählen Sie **\+ Neu**.
2. Wählen Sie dann **Braze** aus der verfügbaren Integration aus und fügen Sie Ihre Braze-Instanz und Ihren Braze REST API-Schlüssel hinzu. 
3. Geben Sie die Ereignisnamen ein, die RevenueCat senden soll, oder wählen Sie die Standard-Ereignisnamen. Weitere Einzelheiten zu den verfügbaren Ereignissen finden Sie in [Schritt 3](#configure-event-names).
4. Wählen Sie aus, ob RevenueCat die Erlöse (nach App-Store-Schnitt) oder den Umsatz (Bruttoverkauf) melden soll.

![Braze-Einstellungen in RevenueCat mit Feldern für Braze-Instanz, API-Schlüsselkennung und Sandbox-Kennung.][3]

### Schritt 3: Ereignisnamen konfigurieren {#configure-event-names}

Geben Sie die Ereignisnamen ein, die RevenueCat senden soll, oder wählen Sie aus den Standard-Ereignisnamen, indem Sie **Standard-Ereignisnamen verwenden** wählen. Die Ereignisse, die RevenueCat senden kann, werden in der folgenden Tabelle beschrieben.

| Event | Beschreibung |
|---|---|
| Erster Kauf | Der erste Kauf eines sich automatisch verlängernden Abonnementprodukts, das keine kostenlose Testversion enthält. |
| Versuch gestartet | Der Beginn eines sich automatisch verlängernden kostenlosen Testabos. |
| Versuch konvertiert | Wenn ein sich automatisch verlängerndes Abonnementprodukt von einem kostenlosen Testzeitraum in einen normalen bezahlten Zeitraum übergeht. |
| Prozess abgebrochen | Wenn ein Benutzer während eines kostenlosen Testzeitraums die Verlängerung eines sich automatisch verlängernden Abonnements deaktiviert. |
| Erneuerung | Wenn ein sich automatisch verlängerndes Abonnementprodukt erneuert wird oder ein Benutzer das sich automatisch verlängernde Abonnementprodukt nach Ablauf seines Abonnements erneut erwirbt. |
| Stornierung | Wenn ein Benutzer die Verlängerungen für ein sich automatisch verlängerndes Abonnementprodukt während des normalen Zahlungszeitraums deaktiviert. |
| Kauf ohne Abonnement | Der Kauf eines Produkts, das kein sich automatisch erneuerndes Abonnement ist. |
| Ablauf | Wenn ein Abonnement ausläuft. |
| Abrechnungsproblem | Wenn es beim Versuch, den Benutzer zu belasten, ein Problem gegeben hat. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Bei Ereignissen, die Einnahmen beinhalten, wird RevenueCat diesen Betrag automatisch zusammen mit dem Ereignis in Braze aufzeichnen, wie z.B. Testkonvertierungen und Verlängerungen.

## Mit dieser Integration

Nachdem Sie die Braze-Einstellungen in RevenueCat konfiguriert haben, werden die Ereignisse automatisch von RevenueCat zu Braze fließen, ohne dass Sie etwas tun müssen.

## Anpassung

### Fügen Sie einen Sandbox-API-Schlüssel für Tests hinzu

Wenn Sie RevenueCat nur einen Braze REST API-Schlüssel zur Verfügung stellen, werden nur Produktionsereignisse gesendet. Wenn Sie auch Sandbox-Testereignisse senden möchten, [erstellen Sie einen weiteren Braze REST API-Schlüssel][11] und fügen Sie ihn zu Ihren Braze-Einstellungen in RevenueCat hinzu.

[2]: {{site.baseurl}}/api/objects_filters/user_alias_object/
[3]: {% image_buster /assets/img/revenuecat/braze_settings_in_revenuecat.png %}
[4]: https://docs.revenuecat.com/docs/subscriber-attributes
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[8]: https://docs.revenuecat.com/docs/configuring-sdk
[9]: https://app.revenuecat.com/login
[11]: {{site.baseurl}}/api/basics/#app-group-rest-api-keys
