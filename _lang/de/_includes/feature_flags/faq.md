# Häufig gestellte Fragen

> Dieser Artikel enthält Antworten auf einige häufig gestellte Fragen zu Feature-Flags.

## Funktionalität und Unterstützung

### Auf welchen Plattformen werden die Feature-Flags von Braze unterstützt? {#platforms}

Braze unterstützt Feature-Flags auf iOS-, Android- und Internet-Plattformen mit den folgenden SDK-Versionsanforderungen:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

Benötigen Sie Unterstützung auf anderen Plattformen? Mailen Sie unserem Team: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

### Wie hoch ist der Aufwand für die Implementierung eines Feature-Flags? {#level-of-effort}

Ein Feature-Flag kann in wenigen Minuten erstellt und integriert werden. 

Der größte Teil des Aufwands entfällt auf Ihr Entwicklerteam, das das neue Feature entwickelt, das Sie einführen möchten. Das Hinzufügen eines Feature-Flag selbst ist so einfach wie eine `IF`/`ELSE`-Anweisung im Code Ihrer App oder Website:

{% tabs %}
{% tab JavaScript %}

```javascript
import { getFeatureFlag } from "@braze/web-sdk";

if (getFeatureFlag("new_shopping_cart").enabled) {
    // Show the new homepage your team has built
}
else {
    // Show the old homepage
}
```

{% endtab %}
{% tab Java %}

```java
if (braze.getFeatureFlag("new_shopping_cart").getEnabled()) {
  // Show the new homepage your team has built
} else {
  // Show the old homepage
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
if (braze.getFeatureFlag("new_shopping_cart")?.enabled == true) {
  // Show the new homepage your team has built
} else {
  // Show the old homepage
}
```

{% endtab %}
{% endtabs %}

### Wie können Marketing Teams von Feature-Flags profitieren? {#marketing-teams}

Marketingteams können Feature-Flags verwenden, um Produktankündigungen (z. B. E-Mails zur Produkteinführung) zu koordinieren, wenn ein Feature nur für einen kleinen Prozentsatz der Nutzer aktiviert ist.

Mit den Feature-Flags von Braze können Sie beispielsweise ein neues Kundenbindungs-Programm für 10 % der Benutzer Ihrer App einführen und über den Canvas-Schritt für Feature-Flags eine E-Mail, eine Push-Mitteilung oder ein anderes Messaging an dieselben 10 % der aktivierten Benutzer senden. 

### Wie können Produkt Teams von Feature-Flags profitieren? {#product-teams}

Produktteams können Feature-Flags verwenden, um neue Features schrittweise einzuführen, um die wichtigsten Performance-Indikatoren und das Feedback der Kunden zu überwachen, bevor sie allen Nutzern zur Verfügung gestellt werden.

Produkt Teams können [Feature-Flag Eigenschaften]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#properties) verwenden, um Inhalte in einer App aus der Ferne aufzufüllen, z. B. Deeplinks, Text, Bilder oder andere dynamische Inhalte.

Mit dem Canvas-Schritt Feature-Flag können Produktteams auch einen A/B-Splittest durchführen, um zu messen, wie sich ein neues Feature auf die Konversionsraten im Vergleich zu Nutzern mit deaktiviertem Feature auswirkt. 

### Wie können Entwicklerteams von Feature-Flags profitieren? {#engineering-teams}

Entwicklerteams können Feature-Flags verwenden, um das mit der Einführung neuer Features verbundene Risiko zu verringern und zu vermeiden, dass sie mitten in der Nacht überstürzt Code-Korrekturen bereitstellen müssen.

Durch die Freigabe von neuem Code, der hinter einem Feature-Flag ausgeblendet ist, kann Ihr Team das Feature aus der Ferne über das Braze-Dashboard ein- oder ausschalten und so die Verzögerung durch das Pushing von neuem Code oder das Warten auf eine Genehmigung für ein Update im App Shop umgehen.

## Feature-Rollouts und Targeting

### Ist es möglich, ein Feature-Flag nur für eine ausgewählte Gruppe von Nutzern auszurollen? {#target-users}

Ja, erstellen Sie in Braze ein Segment, das auf bestimmte Nutzer abzielt – nach E-Mail Adresse, `user_id` oder einem anderen Attribut in den Nutzerprofilen. Setzen Sie dann das Feature-Flag für 100 % des betreffenden Segments.

### Wie wirkt sich die Anpassung des Rollout-Prozentsatzes auf Nutzer aus, die bisher in der aktivierten Gruppe waren? {#random-buckets}

Feature-Flags bleiben für Nutzer über alle Geräte und Sitzungen hinweg konsistent.

- Wenn ein Feature-Flag an 10% der Nutzer:innen ausgerollt wird, bleiben diese 10% aktiviert und persistent für die Lifetime dieses Feature-Flags.
- Wenn Sie den Rollout von 10 auf 20 % erhöhen, bleiben dieselben 10 % aktiviert und es werden weitere 10 % der Nutzer zur aktivierten Gruppe hinzugefügt.
- Wenn Sie den Rollout von 20 auf 10 % reduzieren, bleiben nur die ursprünglichen 10 % der Nutzer aktiviert.

Mit dieser Strategie stellen Sie sicher, dass Nutzer:innen ein einheitliches Erlebnis in Ihrer App haben und nicht zwischen den Sitzungen hin- und herspringen. Wenn Sie ein Feature durch Setzen von 0 % deaktivieren, werden natürlich alle Nutzer aus dem Feature-Flag entfernt, was hilfreich ist, wenn Sie einen Fehler entdecken oder das Feature ganz deaktivieren wollen.

## Technische Themen

### Können Feature-Flags verwendet werden, um zu steuern, wann das Braze SDK initialisiert wird? {#initialization}

Nein, das SDK muss initialisiert werden, um Feature-Flags für den aktuellen Nutzer herunterzuladen und zu synchronisieren. Das bedeutet, dass Sie Feature-Flags nicht verwenden können, um einzuschränken, welche Nutzer in Braze erstellt oder getrackt werden.

### Wie oft werden Feature-Flags vom SDK aktualisiert? {#refresh-frequency}

Feature-Flags werden beim Start der Sitzung und beim Wechsel aktiver Nutzer aktualisiert. Feature-Flags können auch manuell mit der [Aktualisierungsmethode]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#refreshing) des SDKs aktualisiert werden. Die Aktualisierungsrate für Feature-Flags ist auf einmal alle fünf Minuten begrenzt (Änderungen vorbehalten).

Denken Sie daran, dass gute Datenpraktiken empfehlen, Feature-Flags nicht zu schnell zu aktualisieren (mit möglichem Rate-Limiting). Aktualisieren Sie also am besten nur, bevor ein Nutzer mit neuen Features interagiert oder in regelmäßigen Abständen in der App, falls erforderlich.

### Sind Feature-Flags verfügbar, wenn Nutzer offline sind? {#offline}

Ja, nachdem die Feature-Flags aktualisiert wurden, werden sie lokal auf dem Gerät des Nutzers gespeichert und können auch offline abgerufen werden.

### Was passiert, wenn Feature-Flags mitten in der Sitzung aktualisiert werden? {#listen-for-updates}

Feature-Flags können während der Sitzung aktualisiert werden. Es gibt Szenarien, in denen Sie Ihre App aktualisieren möchten, wenn sich bestimmte Variablen oder Ihre Konfiguration ändern sollten. Es kann auch andere Szenarien geben, in denen Sie Ihre App vielleicht nicht aktualisieren möchten, um gravierende Änderungen in der UI-Darstellung zu vermeiden.

Um dies zu kontrollieren, [achten Sie auf Updates]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#updates) von Feature-Flags und entscheiden Sie anhand der geänderten Feature-Flags, ob Ihre App neu gerendert werden soll. 

### Warum erhalten Nutzer:innen in meiner globalen Kontrollgruppe keine Feature-Flags-Experimente?

Sie können Feature-Flags für Nutzer:innen in Ihrer [globalen Kontrollgruppe]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) nicht aktivieren. Das bedeutet, dass Nutzer:innen in Ihrer globalen Kontrollgruppe auch nicht an Feature-Flag Experimenten teilnehmen können.

## Weitere Fragen?

Haben Sie Fragen oder Anregungen? Mailen Sie unserem Team: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

