---
nav_title: RevenueCat
article_title: RevenueCat
description: "Die Integration von RevenueCat und Braze ermöglicht es Ihnen, die Kauf-Events und Abo-Lebenszyklen Ihrer Kund:innen automatisch plattformübergreifend zu synchronisieren. So können Sie Kampagnen erstellen, die auf die Phase des Kundenlebenszyklus Ihrer Kunden reagieren, z. B. die Ansprache von Kunden, die sich während der kostenlosen Testphase abgemeldet haben, oder das Versenden von Erinnerungen an Kunden mit Rechnungsproblemen."
alias: /partners/revenuecat/
page_type: partner
search_tag: Partner

---

# RevenueCat

> [RevenueCat](https://www.revenuecat.com/) ist die einzige Quelle der Wahrheit für Ihren Abo-Status auf iOS, Android und im Internet. Ganz gleich, ob Sie eine neue App entwickeln oder bereits Millionen von Abonnenten haben, mit RevenueCat können Sie plattformübergreifende In-App-Käufe erstellen, Ihre Produkte und Abonnenten verwalten und Ihre Daten analysieren - ganz ohne Server Code.

_Diese Integration wird von RevenueCat gepflegt._

## Über die Integration

Die Integration von RevenueCat und Braze ermöglicht es Ihnen, die Kauf-Events und Abo-Lebenszyklen Ihrer Kund:innen automatisch plattformübergreifend zu synchronisieren. So können Sie Kampagnen erstellen, die auf die Phase des Kundenlebenszyklus Ihrer Kunden reagieren, z. B. die Ansprache von Kunden, die sich während der kostenlosen Testphase abgemeldet haben, oder das Versenden von Erinnerungen an Kunden mit Rechnungsproblemen.

## Voraussetzungen

Zumindest müssen Sie die Integration über das RevenueCat-Dashboard aktivieren, um RevenueCat mit Braze zu verbinden. Wenn Sie das Braze SDK verwenden, können Sie die SDKs von RevenueCat und Braze zusammen verwenden, um die Integration zu verbessern, indem Sie sicherstellen, dass in beiden Systemen derselbe Bezeichner für die Kunden verwendet wird.

| Anforderung | Beschreibung |
|---|---|
| RevenueCat Konto und App | Ein [RevenueCat-Konto](https://app.revenuecat.com/login) ist erforderlich, um die Vorteile dieser Partnerschaft zu nutzen. Sie müssen auch über eine konfigurierte RevenueCat App verfügen. |
| RevenueCat SDK | Wir empfehlen, zusätzlich zum erforderlichen Braze SDK das [RevenueCat SDK](https://docs.revenuecat.com/docs/configuring-sdk) zu installieren, um Nutzer:innen mit User-Aliasing zu versorgen. |
| Braze-Instanz | Ihre Braze-Instanz erhalten Sie von Ihrem Braze Onboarding Manager oder auf der [Übersichtsseite über die APIs]({{site.baseurl}}/api/basics/#endpoints).<br><br>RevenueCat erfordert, dass die Braze-Instanz serverseitig an den richtigen Braze REST-Endpunkt sendet. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| REST API-Schlüssel für den Braze-Test (optional) | Sie können einen API-Schlüssel für Test- und Produktionskäufe verwenden, wenn Sie möchten, dass diese Anfragen an separate Braze-Instanzen gesendet werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle 

- Triggern Sie eine Onboarding-Kampagne, die Ihre Premium Features hervorhebt, wenn ein Kund:in eine kostenlose Testversion einsteigt.
- Senden Sie eine Erinnerung zum Update der Abrechnungsinformationen, wenn ein Ereignis "Abrechnungsproblem" empfangen wird.
- Senden Sie eine Umfrage, nachdem eine Kund:in eine kostenlose Testversion gekündigt hat. 

## Integration

### Schritt 1: Braze Nutzer:in festlegen

Im Braze SDK können Sie die ID des Braze-Benutzers so einstellen, dass sie mit der ID des Nutzers der App RevenueCat übereinstimmt. So wird sichergestellt, dass die von Braze und RevenueCat gesendeten Ereignisse mit demselben Nutzer:innen synchronisiert werden können.

Konfigurieren Sie das Braze SDK mit der gleichen App Nutzer:in ID wie RevenueCat oder verwenden Sie die Braze SDK `.changeUser()` Methode.

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

#### Nutzer-Alias Objekt an Braze senden (optional) 

Wenn Sie einen alternativen eindeutigen Bezeichner senden möchten, der sich von der Abonnent:innen ID der RevenueCat App unterscheidet, aktualisieren Sie die Nutzer:innen mit den folgenden Daten als Attribute der RevenueCat Abonnenten.

| Schlüssel | Beschreibung |
|---|---|
| `$brazeAliasName` | Der Braze `alias_name` im [Nutzer-Alias Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object/) |
| `$brazeAliasLabel` | Der Braze `alias_label` im [Nutzer-Alias Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object/) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Beide Attribute sind erforderlich, damit das [Nutzer-Alias-Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object/) zusammen mit Ihren Ereignisdaten gesendet werden kann. Diese Eigenschaften können manuell eingestellt werden, wie jedes andere [RevenueCat Abonnent:in Attribut](https://docs.revenuecat.com/docs/subscriber-attributes). Beispiele für Code-Snippets finden Sie in Schritt eins.

### Schritt 2: Senden Sie RevenueCat Ereignisse an Braze

Nachdem Sie das RevenueCat SDK für Einkäufe und das Braze SDK so eingerichtet haben, dass sie dieselbe Nutzer:in haben, können Sie die Integration einschalten und die Namen der Ereignisse über das RevenueCat-Dashboard konfigurieren.

1. Navigieren Sie zu Ihrem Projekt im RevenueCat Dashboard und suchen Sie im linken Menü die Karte **Integrationen**. Wählen Sie **\+ Neu**.
2. Als nächstes wählen Sie **Braze** aus der verfügbaren Integration aus und fügen Ihre Braze-Instanz und Ihren Braze REST API-Schlüssel hinzu. 
3. Geben Sie die Ereignisnamen ein, die RevenueCat senden soll, oder wählen Sie die Standard-Ereignisnamen. Weitere Einzelheiten zu den verfügbaren Ereignissen finden Sie in [Schritt 3](#configure-event-names).
4. Wählen Sie aus, ob Sie möchten, dass RevenueCat den Erlös (nach dem App Shop-Schnitt) oder den Umsatz (Bruttoumsatz) meldet.

![Braze-Einstellungen in RevenueCat mit Feldern für Braze-Instanz, API-Schlüssel-Bezeichner und Sandbox-Bezeichner.]({% image_buster /assets/img/revenuecat/braze_settings_in_revenuecat.png %})

### Schritt 3: Ereignisnamen konfigurieren {#configure-event-names}

Geben Sie die Ereignisnamen ein, die RevenueCat senden soll, oder wählen Sie aus den Standard-Ereignisnamen, indem Sie **Standard-Ereignisnamen verwenden** auswählen. Die Ereignisse, deren Versand RevenueCat unterstützt, werden im folgenden Chart beschrieben.

| Event | Beschreibung |
|---|---|
| Erster Kauf | Der erste Kauf eines sich automatisch verlängernden Abo-Produkts, das keine kostenlose Testversion enthält. |
| Versuch gestartet | Der Beginn eines sich automatisch verlängernden Abo-Produkts, das Sie kostenlos testen können. |
| Versuchsweise umgewandelt | Wenn ein sich automatisch verlängerndes Abo-Produkt von einer kostenlosen Testphase in eine normale bezahlte Phase übergeht. |
| Prozess abgebrochen | Wenn ein Nutzer:innen die Verlängerung eines sich automatisch verlängernden Abo-Produkts während einer kostenlosen Testphase ausschaltet. |
| Erneuerung | Wenn ein sich automatisch verlängerndes Abo-Produkt erneuert wird oder ein Nutzer:in das sich automatisch verlängernde Abo-Produkt zurückkehrt, nachdem sein Abo ausgelaufen ist. |
| Stornierung | Wenn ein Nutzer:innen die Verlängerungen für ein sich automatisch verlängerndes Abo-Produkt während des normalen Bezahlzeitraums deaktiviert. |
| Kauf ohne Abo | Der Kauf eines Produkts, das kein automatisch verlängerndes Abo ist. |
| Ablauf | Wenn ein Abo ausläuft. |
| Abrechnungsproblem | Wenn es beim Versuch, den Nutzer:innen zu belasten, ein Problem gegeben hat. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Bei Ereignissen, die Einnahmen beinhalten, zeichnet RevenueCat diesen Betrag automatisch zusammen mit dem Ereignis in Braze auf, z. B. bei Konversionen von Testversionen und Verlängerungen.

## Verwendung dieser Integration

Nachdem Sie die Braze-Einstellungen in RevenueCat konfiguriert haben, werden die Ereignisse automatisch von RevenueCat zu Braze fließen, ohne dass Sie etwas tun müssen.

## Anpassung

### Fügen Sie einen API-Schlüssel für die Sandbox zum Testen hinzu

Wenn Sie RevenueCat nur einen Braze REST API-Schlüssel zur Verfügung stellen, werden nur Produktionsereignisse gesendet. Wenn Sie auch Sandbox-Testereignisse senden möchten, [erstellen Sie einen weiteren REST API-Schlüssel von Braze]({{site.baseurl}}/api/basics/#app-group-rest-api-keys) und fügen Sie ihn zu Ihren Braze-Einstellungen in RevenueCat hinzu.


