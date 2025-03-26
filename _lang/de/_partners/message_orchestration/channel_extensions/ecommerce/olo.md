---
nav_title: Olo
article_title: Olo
description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze und Olo, einer führenden offenen SaaS-Plattform für Restaurants, die Gastfreundschaft an jedem Touchpoint ermöglicht."
alias: /partners/olo/
page_type: partner
search_tag: Partner
---

# Olo

> [Olo][1] ist eine führende offene SaaS-Plattform für Restaurants, die Gastfreundschaft an jedem Touchpoint ermöglicht.

Durch die Integration von Olo und Braze können Sie:

- Aktualisieren Sie die Benutzerprofile in Braze, damit sie mit den Olo-Benutzerprofilen übereinstimmen.
- Senden Sie die richtige nächstbeste Nachricht von Braze basierend auf Olo-Ereignissen

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Olo-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Olo-Konto mit Zugriff auf Webhooks. Richten Sie Webhook-Abonnements über das [Self-Service-Tool für Webhooks](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks) im Olo Dashboard ein. |
| Braze Data Transformation | Eine [Datenumwandlungs-URL]({{site.baseurl}}/data_transformation/) ist erforderlich, um Daten von Olo zu empfangen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Ein Webhook ist eine Möglichkeit für Olo, ereignisgesteuerte Informationen über Benutzer und ihre Aktionen an Braze zu senden, einschließlich Ereignissen wie "Bestellung aufgegeben", "Gast angemeldet", "Bestellung abgeholt" und mehr. Der Olo Webhook liefert das Ereignis in der Regel innerhalb von Sekunden nach Ausführung der Aktion an Braze.

## Haftungsausschluss

In Olo sind Sie auf einen Webhook pro Umgebung für jede genehmigte Marke beschränkt, die alle an dieselbe **Ziel-URL** gesendet werden. Verschiedene Marken können unterschiedliche URLs haben, aber Veranstaltungen der gleichen Marke müssen eine gemeinsame URL haben. In Braze bedeutet dies, dass Sie nur eine Transformation für die Verwendung mit Olo erstellen können.

Um mehrere Olo-Ereignisse innerhalb dieser einzigen Transformation zu verarbeiten, suchen Sie in jedem Webhook nach der Kopfzeile `X-Olo-Event-Type`. Mit dieser Kopfzeile können Sie verschiedene Olo-Ereignisse bedingt verarbeiten.

## Integration

### Schritt 1: Richten Sie die Braze Data Transformation so ein, dass sie Olos Test-Ereignis akzeptiert. {#step-1}

{% multi_lang_include create_transformation.md location="default" %}

### Schritt 2: Olo Webhooks einrichten

Verwenden Sie das [Self-Service-Webhooks-Tool][2] im Olo-Dashboard, um Webhooks einzurichten, die an Ihre Data Transformation gesendet werden.

1. Wählen Sie, welche Ereignisse an Braze gesendet werden sollen
2. Konfigurieren Sie die **Ziel-URL**. Dies ist die in [Schritt 1](#step-1) erstellte Datenumwandlungs-URL.

{% alert note %}
`OAuth` und das gemeinsame Geheimnis des `X-Olo-Signature` Headers werden für die Umwandlung nicht benötigt.
{% endalert %}

{:start="3"}
3\. Überprüfen Sie, ob der Webhook richtig konfiguriert ist, indem Sie ein [Test-Ereignis][3] an Ihre Datenumwandlung senden. Nur Olo Dashboard-Benutzer mit der [Berechtigung Developer Tools][4] können Test-Ereignisse senden.

Olo benötigt eine erfolgreiche Antwort vom Test Event Webhook, bevor Sie den Olo Webhook-Konfigurationsprozess abschließen können.

### Schritt 3: Schreiben Sie Transformationscode, um die von Ihnen gewählten Olo-Ereignisse zu akzeptieren

In diesem Schritt wandeln Sie die Webhook-Nutzlast, die von der Quellplattform gesendet wird, in einen JavaScript-Objektrückgabewert um.

1. Senden Sie eine Anfrage an Ihre Datenumwandlungs-URL mit einer Beispiel-Nutzlast für ein Olo-Ereignis, das Sie unterstützen möchten. Siehe [Format des Anfragekörpers](#request-body-format) für Hilfe bei der Formatierung Ihrer Anfrage.
2. Aktualisieren Sie Ihre Datenumwandlung und vergewissern Sie sich, dass Sie die Beispiel-Nutzlast des Ereignisses in den **Webhook-Details** sehen können.
3. Aktualisieren Sie Ihren Datenumwandlungscode, um die von Ihnen gewählten Olo-Ereignisse zu unterstützen.
4. Klicken Sie auf **Validieren**, um eine Vorschau der Ausgabe Ihres Codes zu erhalten und um zu prüfen, ob es sich um eine akzeptable `/users/track` Anfrage handelt.
5. Speichern und aktivieren Sie Ihre Datenumwandlung.

#### Format des Anfragekörpers

Dieser Rückgabewert muss dem Format des `/users/track` Anfragekörpers von Braze entsprechen:

- Transformationscode wird in der Programmiersprache JavaScript akzeptiert. Jeder Standard-JavaScript-Kontrollfluss, wie z.B. die if/else-Logik, wird unterstützt.
- Der Transformationscode greift über die Payload-Variable auf den Körper der Webhook-Anfrage zu. Diese Variable ist ein Objekt, das durch Parsen des JSON-Anfragekörpers erstellt wird.
- Jede Funktion, die in unserem `/users/track` Endpunkt unterstützt wird, wird unterstützt, einschließlich:
    - Objekte mit Benutzerattributen, Ereignisobjekte und Kaufobjekte
    - Verschachtelte Attribute und verschachtelte benutzerdefinierte Ereigniseigenschaften
    - Aktualisierungen von Abonnementgruppen
    - E-Mail-Adresse als Identifikator

## Beispiel Datenumwandlungen für Olo Webhooks

Dieser Abschnitt enthält Beispielvorlagen, die Sie als Ausgangspunkt verwenden können. Fangen Sie einfach von vorne an oder löschen Sie bestimmte Komponenten, wenn Sie es für richtig halten.

In jeder Vorlage definiert der Code eine Variable, `brazecall`, um eine `/users/track` Anfrage zu erstellen.

Nachdem die Anfrage `/users/track `an `brazecall` zugewiesen wurde, geben Sie explizit `brazecall` zurück, um eine Ausgabe zu erstellen.

### Transformation eines einzelnen Ereignisses

Wenn Sie nur ein einziges Olo-Ereignis unterstützen möchten, brauchen Sie den `X-Olo-Event-Type` Header nicht zu verwenden, um die Nutzdaten der `/users/track` Anfrage bedingt zu erstellen. Zum Beispiel das Protokollieren eines Kaufereignisses oder eines benutzerdefinierten Ereignisses im Benutzerprofil, wenn ein Olo Order Placed Webhook an Braze gesendet wird.

### Jedes Produkt als Kauf protokollieren

```javascript
// iterate through the items included within the order

const purchases = payload.items.map((item) => {
 return {
   external_id: payload.customer.customerId.toString(),
   product_id: item.productId.toString(),
   currency: 'USD',
   price: item.sellingPrice,
   time: new Date().toISOString(),
   quantity: item.quantity,
   properties: {
     customValues: item.customValues
   }
 };
});

// log a purchase per item in the order

let brazecall = {
 "purchases": purchases
};

return brazecall;
```

### Protokollieren eines benutzerdefinierten Ereignisses

```javascript
// log an event “Order Placed” to the profile that includes all items in the order as event properties.

let brazecall = { 
"events": [
   {
     "external_id": payload.customer.customerId.toString(),
     "_update_existing_only": false,
     "name": "Order Placed",
     "time": new Date().toISOString(),
     "properties": {
       "Delivery Method": payload.deliveryMethod,
       "Items": payload.items,
       "Total": payload.totals.total,
       "Location": payload.location.name
     }
   }
 ]
};

return brazecall;
```

## Multi-Ereignis-Transformation

Olo sendet den Ereignistyp in der `X-Olo-Event-Type` Kopfzeile jedes Webhooks. Um mehrere Olo-Webhook-Ereignisse innerhalb einer einzigen Transformation zu unterstützen, verwenden Sie eine bedingte Logik, um die Webhook-Nutzdaten basierend auf dem Wert dieses Header-Typs zu transformieren.  

In dem folgenden Transformationsbeispiel erstellt unser JavaScript eine bestimmte Nutzlast für die Ereignisse von `UserSignedUp` und `OrderPlaced`. Zusätzlich behandelt eine `else` Bedingung eine Nutzlast für alle Olo-Ereignisse, die an Braze ohne den X-Olo-Event-Type Header von `UserSignedUp` und `OrderPlaced` gesendet werden.

```javascript
// captures the value within the X-Olo-Event-Type header for use in the conditional logic

let event_type = headers["X-Olo-Event-Type"];

// defines a variable 'brazecall' that will hold the request payload for the /users/track request

let brazecall;

// if the X-Olo-Event-Type header is 'UserSignedUp', define a variable for the different subscription statuses that could be included within the Olo event payload

if (event_type == "UserSignedUp") {
	let emailSubscribe;
	let emailSubscriptionGroup;
	let smsSubscriptionGroup;


// determine if the user has opted into marketing emails


	if (payload.allowEmail) {
		emailSubscribe = "opted_in";
		emailSubscriptionGroup = "subscribed";
	} else {
		emailSubscribe = "unsubscribed";
		emailSubscriptionGroup = "unsubscribed";
	}


	// determine if the user has opted into SMS


	if (payload.allowMarketingSms) {
		smsSubscriptionGroup = "subscribed";
	} else {
		smsSubscriptionGroup = "unsubscribed";
	}

	// build the /users/track request and pass in the appropriate subscription statuses


	brazecall = {
		"attributes": [{
			"external_id": payload.id.toString(),
			"_update_existing_only": false,
			"email": payload.emailAddress,
			"first_name": payload.firstName,
			"last_name": payload.lastName,
			"email_subscribe": emailSubscribe,
			"phone": payload.contactNumber,
			"subscription_groups": [{
					"subscription_group_id": "57e5307f-9084-490d-9d6d-8244dc919a48",
					"subscription_state": emailSubscriptionGroup
				},
				{
					"subscription_group_id": "6440ba26-86ea-47db-a935-6647941dc78b",
					"subscription_state": smsSubscriptionGroup
				}
			]
		}]
	}; // if the X-Olo-Event-Type header is 'OrderPlaced', build the /users/track request to log an event to the user profile
} else if (event_type == "OrderPlaced") {
	brazecall = {
		"events": [{
			"external_id": payload.customer.customerId.toString(),
			"_update_existing_only": false,
			"name": "Order Placed",
			"time": new Date().toISOString(),
			"properties": {
				"Delivery Method": payload.deliveryMethod,
				"Items": payload.items,
				"Total": payload.totals.total,
				"Location": payload.location.name
			}
		}]
	};
} else { // if the X-Olo-Event-Type header is anything else, build the /users/track request to log an event to the user profile
	brazecall = {
		"events": [{
			"external_id": payload.customer.customerId.toString(),
			"_update_existing_only": true,
			"name": "Another Event",
			"time": new Date().toISOString()
		}]

	};
}

// return `brazecall` to create an output.

return brazecall;
```

### Schritt 4: Veröffentlichen Sie Ihren Olo Webhook

Nachdem Sie Ihre Data Transformation in Braze aktiviert haben, verwenden Sie das [Self-Service-Webhook-Tool][2] im Olo-Dashboard, um Ihren Webhook zu veröffentlichen. Wenn der Webhook veröffentlicht wird, beginnt die Datenumwandlung, Olo Webhook-Ereignisnachrichten zu empfangen.

## Was Sie wissen sollten

### Wiederholungen

Olo wird Webhook-Aufrufe, die zu einem HTTP-Antwortstatuscode von `429 - Too Many Requests` oder im Bereich von `5xx` führen (z. B. aufgrund einer Gateway-Zeitüberschreitung oder eines Serverfehlers), innerhalb von 24 Stunden bis zu 50 Mal wiederholen, bevor die Anfrage verworfen wird.

### Mindestens eine Lieferung

Wenn ein Webhook-Aufruf zu einem HTTP-Antwortstatuscode von `429 - Too Many Requests` oder im Bereich `5xx` führt (z. B. aufgrund einer Gateway-Zeitüberschreitung oder eines Serverfehlers), versucht Olo die Nachricht innerhalb von 24 Stunden bis zu 50 Mal erneut, bevor es aufgibt.

Webhooks können daher mehrfach von einem Abonnenten empfangen werden. Es obliegt dem Abonnenten, Duplikate zu ignorieren, indem er die Kopfzeile `X-Olo-Message-Id` überprüft.


[1]: https://www.olo.com/
[2]: https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks
[3]: https://developer.olo.com/docs/load/webhooks#operation/test
[4]: https://olosupport.zendesk.com/hc/en-us/articles/115001427843-Dashboard-Permissions