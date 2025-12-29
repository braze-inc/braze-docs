# Feature-Flags

> Feature-Flags ermöglichen es Ihnen, Funktionen für eine bestimmte oder zufällige Auswahl von Nutzer:innen aus der Ferne zu aktivieren oder zu deaktivieren. Wichtig ist, dass Sie damit ein Feature in der Produktion ein- und ausschalten können, ohne zusätzlichen Code zu implementieren oder Updates im App Shop durchzuführen. Dies erlaubt es Ihnen, neue Features sicher und zuverlässig einzuführen.

{% alert tip %}
Wenn Sie bereit sind, Ihre eigenen Feature-Flags zu erstellen, lesen Sie den Abschnitt [Erstellen von Feature-Flags]({{site.baseurl}}/developer_guide/feature_flags/create/).
{% endalert %}

## Voraussetzungen

Dies sind die SDK-Versionen, die Sie mindestens benötigen, um Feature-Flags verwenden zu können:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

## Anwendungsfälle

### Schrittweise Einführungen

Verwenden Sie Feature-Flags, um Features schrittweise für eine Stichprobenpopulation zu aktivieren. Sie können zum Beispiel ein neues Feature zuerst für Ihre VIP Nutzer:innen einführen. Diese Strategie mindert die Risiken, die mit der gleichzeitigen Bereitstellung neuer Features für alle verbunden sind, und hilft, Fehler frühzeitig zu erkennen.

![Bewegtes Bild des Rollout-Verkehrsschiebers, der von 0 auf 100 % geht.]({% image_buster /assets/img/feature_flags/feature-flags-rollout.gif %})

Nehmen wir zum Beispiel an, wir haben beschlossen, unserer App einen neuen Link "Live Chat Support" hinzuzufügen, um den Dienst für unsere Kund:in zu beschleunigen. Wir könnten dieses Feature für alle Kund:innen auf einmal freigeben. Eine breite Veröffentlichung birgt jedoch Risiken, wie z.B.: 

* Unser Support-Team ist noch in der Ausbildung und Kund:innen können nach der Veröffentlichung Support-Tickets starten. Das gibt uns keinen Spielraum, falls das Support Team mehr Zeit benötigt.
* Wir wissen nicht, wie viele neue Support-Fälle wir tatsächlich erhalten werden, so dass wir möglicherweise nicht ausreichend mit Personal ausgestattet sind.
* Wenn unser Support Team überfordert ist, haben wir keine Strategie, dieses Feature schnell wieder abzuschalten.
* Es könnte sein, dass das Chat-Widget Fehler enthält, und wir möchten nicht, dass Kunden:in ein negatives Erlebnis haben.

Mit den Feature-Flags von Braze können wir das Feature stattdessen schrittweise einführen und diese Risiken abmildern:

* Wir werden das Feature "Live-Chat-Support" einschalten, sobald das Team des Supports sich bereit erklärt.
* Wir werden dieses neue Feature nur für 10 % der Nutzer:innen aktivieren, um festzustellen, ob wir angemessen besetzt sind.
* Wenn es Fehler gibt, können wir das Feature schnell deaktivieren, anstatt überstürzt eine neue Version zu veröffentlichen.

Um dieses Feature schrittweise einzuführen, [erstellen Sie ein Feature-Flag]({{site.baseurl}}/developer_guide/feature_flags/create/) namens "Live Chat Widget".

![Feature-Flag-Details für ein Beispiel mit dem Namen "Live Chat Widget". Die ID lautet enable_live_chat. Dieses Feature-Flag beschreibt, dass das Live Chat Widget auf der Support-Seite angezeigt wird.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-livechat-1.png %})

In unserem Code für die App wird der Button **Start Live Chat** nur angezeigt, wenn das Feature-Flag von Braze aktiviert ist:

{% tabs %}
{% tab JavaScript %}

```javascript
import {useState} from "react";
import * as braze from "@braze/web-sdk";

// Get the initial value from the Braze SDK
const featureFlag = braze.getFeatureFlag("enable_live_chat");
const [liveChatEnabled, setLiveChatEnabled] = useState(featureFlag.enabled);

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(() => {
    const newValue = braze.getFeatureFlag("enable_live_chat").enabled;
    setLiveChatEnabled(newValue);
});

// Only show the Live Chat if the Braze SDK determines it is enabled
return (<>
  Need help? <button>Email Our Team</button>
  {liveChatEnabled && <button>Start Live Chat</button>}
</>)
```

{% endtab %}
{% tab Java %}

```java
// Get the initial value from the Braze SDK
FeatureFlag featureFlag = braze.getFeatureFlag("enable_live_chat");
Boolean liveChatEnabled = featureFlag != null && featureFlag.getEnabled();

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(event -> {
  FeatureFlag newFeatureFlag = braze.getFeatureFlag("enable_live_chat");
  Boolean newValue = newFeatureFlag != null && newFeatureFlag.getEnabled();
  liveChatEnabled = newValue;
});

// Only show the Live Chat view if the Braze SDK determines it is enabled
if (liveChatEnabled) {
  liveChatView.setVisibility(View.VISIBLE);
} else {
  liveChatView.setVisibility(View.GONE);
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
// Get the initial value from the Braze SDK
val featureFlag = braze.getFeatureFlag("enable_live_chat")
var liveChatEnabled = featureFlag?.enabled

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates() { event ->
  val newValue = braze.getFeatureFlag("enable_live_chat")?.enabled
  liveChatEnabled = newValue
}

// Only show the Live Chat view if the Braze SDK determines it is enabled
if (liveChatEnabled) {
  liveChatView.visibility = View.VISIBLE
} else {
  liveChatView.visibility = View.GONE
}

```

{% endtab %}
{% tab Swift %}

```swift
// Get the initial value from the Braze SDK
let featureFlag = braze.featureFlags.featureFlag(id: "enable_live_chat")
var liveChatEnabled = featureFlag?.enabled ?? false

// Listen for updates from the Braze SDK
braze.featureFlags.subscribeToUpdates() { _ in  
  let newValue = braze.featureFlags.featureFlag(id: "enable_live_chat")?.enabled ?? false
  liveChatEnabled = newValue
}

// Only show the Live Chat view if the Braze SDK determines it is enabled
liveChatView.isHidden = !liveChatEnabled
```

{% endtab %}
{% endtabs %}

### App-Variablen aus der Ferne steuern

Verwenden Sie Feature-Flags, um die Funktionalität Ihrer App in der Produktion zu ändern. Dies kann besonders wichtig für mobile Apps sein, bei denen die Genehmigung des App Store eine schnelle Einführung von Änderungen für alle Nutzer:innen verhindert.

Nehmen wir zum Beispiel an, dass unser Marketing Team unsere aktuellen Verkäufe und Aktionen in der Navigation unserer App auflisten möchte. Normalerweise benötigen unsere Techniker eine Woche Vorlaufzeit für alle Änderungen und drei Tage für eine Überprüfung im App Shop. Aber mit Thanksgiving, Black Friday, Cyber Monday, Chanukka, Weihnachten und Neujahr, die alle innerhalb von zwei Monaten stattfinden, werden wir diese engen Fristen nicht einhalten können.

Mit Feature-Flags können wir Braze den Inhalt unseres App-Navigationslinks bestimmen lassen, so dass unser Marketing Manager:in Minuten statt in Tagen Änderungen vornehmen kann.

Um dieses Feature remote zu konfigurieren, erstellen wir ein neues Feature-Flag namens `navigation_promo_link` und definieren die folgenden anfänglichen Eigenschaften:

![Feature-Flag mit Link- und Texteigenschaften, die auf eine generische Verkaufsseite verweisen.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-1.png %})

In unserer App werden wir Getter-Methoden von Braze verwenden, um die Eigenschaften dieses Feature-Flags abzurufen und die Navigationslinks auf der Grundlage dieser Werte zu erstellen:

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";
import {useState} from "react";

const featureFlag = braze.getFeatureFlag("navigation_promo_link");
// Check if the feature flag is enabled
const [promoEnabled, setPromoEnabled] = useState(featureFlag.enabled);
// Read the "link" property
const [promoLink, setPromoLink] = useState(featureFlag.getStringProperty("link"));
// Read the "text" property
const [promoText, setPromoText] = useState(featureFlag.getStringProperty("text"));

return (<>
  <div>
    <a href="/">Home</a>
    { promoEnabled && <a href={promoLink}>{promoText}</a> }
    <a href="/products">Products</a>
    <a href="/categories">Categories
  </div>
</>)
```

{% endtab %}
{% tab Java %}

```java
// liveChatView is the View container for the Live Chat UI
FeatureFlag featureFlag = braze.getFeatureFlag("navigation_promo_link");
if (featureFlag != null && featureFlag.getEnabled()) {
  liveChatView.setVisibility(View.VISIBLE);
} else {
  liveChatView.setVisibility(View.GONE);
}
liveChatView.setPromoLink(featureFlag.getStringProperty("link"));
liveChatView.setPromoText(featureFlag.getStringProperty("text"));

```

{% endtab %}
{% tab Kotlin %}

```kotlin
// liveChatView is the View container for the Live Chat UI
val featureFlag = braze.getFeatureFlag("navigation_promo_link")
if (featureFlag?.enabled == true) {
  liveChatView.visibility = View.VISIBLE
} else {
  liveChatView.visibility = View.GONE
}
liveChatView.promoLink = featureFlag?.getStringProperty("link")
liveChatView.promoText = featureFlag?.getStringProperty("text")
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "navigation_promo_link")
if let featureFlag {
  liveChatView.isHidden = !featureFlag.enabled
} else {
  liveChatView.isHidden = true
}
liveChatView.promoLink = featureFlag?.stringProperty("link")
liveChatView.promoText = featureFlag?.stringProperty("text")
```

{% endtab %}
{% endtabs %}

Jetzt, am Tag vor Thanksgiving, müssen wir nur noch die Werte dieser Eigenschaften im Braze-Dashboard ändern.

![Feature-Flag mit Link- und Texteigenschaften, die auf eine Thanksgiving-Verkaufsseite verweisen.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-2.png %})

Das nächste Mal, wenn jemand die App lädt, sieht er die neuen Thanksgiving-Angebote.

### Nachrichtenkoordination

Verwenden Sie Feature-Flags, um das Rollout eines Features und die Nachrichten zu synchronisieren. Dies erlaubt es Ihnen, Braze als Quelle der Wahrheit sowohl für Ihre Nutzer:innen als auch für die entsprechenden Nachrichten zu nutzen. Um dies zu erreichen, richten Sie das neue Feature auf ein bestimmtes Segment oder einen gefilterten Teil Ihrer Zielgruppe aus. Erstellen Sie dann eine Kampagne oder ein Canvas, das nur auf dieses Segment abzielt. 

Nehmen wir an, dass wir ein neues Kundenbindungs-Programm für unsere Nutzer:innen einführen wollen. Für Marketing- und Produkt-Teams kann es schwierig sein, das Messaging für Werbeaktionen mit der Einführung eines Features perfekt zu koordinieren. Mit Feature-Flags in Canvas können Sie eine ausgeklügelte Logik anwenden, um ein Feature für eine ausgewählte Zielgruppe zu aktivieren und die damit verbundenen Nachrichten für dieselben Nutzer:innen zu steuern.

Um die Einführung von Features und Messaging effektiv zu koordinieren, erstellen wir ein neues Feature-Flag namens `show_loyalty_program`. In der ersten Phase der Veröffentlichung werden wir Canvas die Kontrolle darüber überlassen, wann und für wen das Feature-Flag aktiviert wird. Für den Moment belassen wir den Rollout-Prozentsatz bei 0 % und wählen keine Targeting-Segmente aus.

![Ein Feature-Flag mit dem Namen Loyalty Rewards Program. Die ID show_loyalty_program und die Beschreibung, dass dies das neue Kundenbindungs-Programm auf dem Startbildschirm und der Profil-Seite anzeigt.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-loyalty.png %})

Anschließend erstellen wir in Canvas einen [Feature-Flag-Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/), der das Feature-Flag `show_loyalty_program` für unser Segment "Hochwertige Kunden" aktiviert:

![Ein Beispiel für ein Canvas mit einem Schritt zur Segmentierung der Zielgruppe, bei dem das Segment der hochwertigen Kunden das Feature-Flag show_loyalty_program aktiviert wird.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-canvas-flow.png %})

Die Nutzer:innen dieses Segments werden nun das neue Kundenbindungs-Programm sehen, und nach dessen Aktivierung werden automatisch eine E-Mail und eine Umfrage verschickt, damit unser Team Feedback einholen kann.

### Experimentieren mit Features

Verwenden Sie Feature-Flags, um zu experimentieren und Ihre Hypothesen über Ihr neues Feature zu bestätigen. Wenn Sie den Datenverkehr in zwei oder mehr Gruppen aufteilen, können Sie die Auswirkungen eines Feature-Flags in den verschiedenen Gruppen vergleichen und anhand der Ergebnisse die beste Vorgehensweise festlegen.

Ein [A/B-Test]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) ist ein leistungsstarkes Instrument, das die Reaktionen der Nutzer:innen auf mehrere Versionen einer Variable vergleicht.

In diesem Beispiel hat unser Team einen neuen Checkout-Flow für unsere E-Commerce App erstellt. Obwohl wir sicher sind, dass es das Nutzer:innen-Erlebnis verbessert, möchten wir einen A/B-Test durchführen, um die Auswirkungen auf den Umsatz unserer App zu messen.

Zunächst erstellen wir ein neues Feature-Flag namens `enable_checkout_v2`. Wir fügen keine Zielgruppen oder Rollout-Prozente hinzu. Stattdessen verwenden wir ein Feature-Flag-Experiment, um den Datenverkehr aufzuteilen, das Feature zu aktivieren und das Ergebnis zu messen.

In unserer App prüfen wir, ob das Feature-Flag aktiviert ist oder nicht, und ändern den Checkout-Flow entsprechend der Antwort:

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

const featureFlag = braze.getFeatureFlag("enable_checkout_v2");
braze.logFeatureFlagImpression("enable_checkout_v2");
if (featureFlag?.enabled) {
  return <NewCheckoutFlow />  
} else {
  return <OldCheckoutFlow />
}
```

{% endtab %}
{% tab Java %}

```java
FeatureFlag featureFlag = braze.getFeatureFlag("enable_checkout_v2");
braze.logFeatureFlagImpression("enable_checkout_v2");
if (featureFlag != null && featureFlag.getEnabled()) {
  return new NewCheckoutFlow();
} else {
  return new OldCheckoutFlow();
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("enable_checkout_v2")
braze.logFeatureFlagImpression("enable_checkout_v2")
if (featureFlag?.enabled == true) {
  return NewCheckoutFlow()
} else {
  return OldCheckoutFlow()
}
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "enable_checkout_v2")
braze.featureFlags.logFeatureFlagImpression(id: "enable_checkout_v2")
if let featureFlag, featureFlag.enabled {
  return NewCheckoutFlow()
} else {
  return OldCheckoutFlow()
}
```

{% endtab %}
{% endtabs %}

Wir werden unseren A/B-Test in einem [Feature-Flag-Experiment]({{site.baseurl}}/developer_guide/feature_flags/experiments/) einrichten.

Jetzt werden 50 % der Nutzer:innen das alte Erlebnis sehen, während die anderen 50 % das neue Erlebnis sehen werden. Wir können dann die beiden Varianten analysieren, um festzustellen, welcher Checkout-Flow zu einer höheren Konversionsrate geführt hat. {% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}

![Ein Feature-Flag Experiment, bei dem der Verkehr in zwei 50-Prozent-Gruppen aufgeteilt wird.]({% image_buster /assets/img/feature_flags/feature-flag-use-case-campaign-experiment.png %})

Sobald wir den Gewinner ermittelt haben, können wir diese Kampagne stoppen und den Prozentsatz für die Einführung des Feature-Flags auf 100% für alle Nutzer:innen erhöhen, während unser Entwicklerteam dies in unsere nächste App-Version fest einkodiert.

### Segmentierung

Verwenden Sie den Filter **Feature-Flag**, um ein Segment zu erstellen oder Messaging an Nutzer:innen zu richten, je nachdem, ob sie ein Feature-Flag aktiviert haben. Nehmen wir zum Beispiel an, wir haben ein Feature-Flag, das Premium-Inhalte in unserer App kontrolliert. Wir könnten ein Segment erstellen, das nach Nutzer:innen filtert, die das Feature-Flag nicht aktiviert haben, und diesem Segment dann eine Nachricht schicken, in der sie aufgefordert werden, ihr Konto zu upgraden, um Premium-Inhalte zu sehen.

![]({% image_buster /assets/img/feature_flags/feature_flag_segmentation_filter.png %})

Weitere Informationen zum Filtern nach Segmenten finden Sie unter [Erstellen eines Segments]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).

{% alert note %}
Um rekursive Segmente zu vermeiden, ist es nicht möglich, ein Segment zu erstellen, das auf andere Feature-Flags referenziert.
{% endalert %}

## Beschränkungen je Tarif

Dies sind die Feature-Flag-Beschränkungen für den kostenlosen und den kostenpflichtigen Tarif.

| Merkmal                                                                                                   | Kostenlose Version     | Kostenpflichtige Version      |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| [Aktive Feature-Flags](#active-feature-flags)                                                                     | 10 pro Workspace | 110 pro Workspace |
| [Aktive Kampagnen-Experimente]({{site.baseurl}}/developer_guide/feature_flags/experiments/)          | 1 pro Workspace  | 100 pro Workspace |
| [Feature-Flag-Canvas-Schritte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) | Unbegrenzt        | Unbegrenzt         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Ein Feature-Flag gilt als aktiv und wird auf Ihr Limit angerechnet, wenn einer der folgenden Punkte zutrifft:

- Rollout ist mehr als 0 %
- In einem aktiven Canvas verwendet
- In einem aktiven Experiment verwendet

Selbst wenn dasselbe Feature-Flag mehrere Kriterien erfüllt, z. B. wenn es in einem Canvas verwendet wird und der Rollout 50 % beträgt, zählt es nur als 1 aktives Feature-Flag für Ihr Limit.

{% alert note %}
Wenn Sie die kostenpflichtige Version der Feature-Flags erwerben möchten, wenden Sie sich an Ihren Braze-Konto Manager, oder fragen Sie im Braze-Dashboard nach einem Upgrade.
{% endalert %}