---
nav_title: Feature-Flag-Experimente
article_title: Feature-Flag-Experimente
page_order: 40
description: "Mit Feature-Flag-Experimenten können Sie A/B-Tests mit Anwendungsänderungen durchführen, um die Konversionsraten zu optimieren."
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web

---

# Feature-Flag Experimente

> Mit Feature-Flag-Experimenten können Sie A/B-Tests mit Anwendungsänderungen durchführen, um die Konversionsraten zu optimieren. Marketer können Feature-Flags verwenden, um herauszufinden, ob sich ein neues Feature positiv oder negativ auf die Konversionsraten auswirkt, oder welche Feature-Flag-Eigenschaften am besten geeignet sind.

## Voraussetzungen

Bevor Sie Nutzerdaten im Experiment tracken können, muss Ihre App aufzeichnen, wann ein Nutzer mit einem Feature-Flag interagiert. Dies wird als Feature-Flag-Impression bezeichnet. Vergewissern Sie sich, dass Sie jedes Mal eine Feature-Flag-Impression protokollieren, wenn ein Nutzer das zu testende Feature sieht oder gesehen haben könnte, auch wenn er in der Kontrollgruppe ist.

Weitere Informationen zur Protokollierung von Feature-Flag-Impression finden Sie unter [Erstellen von Feature-Flags]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#impressions).

{% tabs %}
{% tab JavaScript %}

```javascript
const featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag?.enabled) {
   return <NewFeature />
} else {
   return <ExistingFeature />
}
```

{% endtab %}
{% tab Java %}

```java
FeatureFlag featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag != null && featureFlag.getEnabled()) {
  return new NewFeature();
} else {
  return new ExistingFeature();
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("my-new-feature")
braze.logFeatureFlagImpression("my-new-feature")
if (featureFlag?.enabled == true) {
  return NewFeature()
} else {
  return ExistingFeature()
}
```

{% endtab %}
{% endtabs %}

## Ein Feature Flag Experiment erstellen

### Schritt 1: Ein Experiment erstellen

1. Gehen Sie zu **Messaging** > **Kampagnen** und wählen Sie dann **\+ Kampagne erstellen**.
2. Wählen Sie **Feature Flag Experiment**.
3. Geben Sie Ihrer Kampagne einen klaren und aussagekräftigen Namen.

### Schritt 2: Experimentiervarianten hinzufügen

Als nächstes erstellen Sie Variationen. Wählen Sie für jede Variante das Feature-Flag, das Sie ein- oder ausschalten möchten, und überprüfen Sie dann die zugewiesenen Eigenschaften.

Um die Wirkung Ihres Features zu testen, verwenden Sie Varianten, um den Traffic in zwei oder mehr Gruppen aufzuteilen. Nennen Sie eine Gruppe "Meine Kontrollgruppe" und deaktivieren Sie die Feature-Flags.

### Schritt 3: Eigenschaften überschreiben (optional)

Sie können die Standard-Eigenschaften, die Sie ursprünglich für Nutzer:innen mit einer bestimmten Kampagnenvariante eingerichtet haben, überschreiben.

Um zusätzliche Standardeigenschaften zu bearbeiten, hinzuzufügen oder zu entfernen, bearbeiten Sie die Funktionsflagge selbst unter **Messaging** > **Funktionsflaggen**. Wenn eine Variante deaktiviert ist, gibt das SDK ein leeres Eigenschaften-Objekt für das angegebene Feature-Flag zurück.

![Der Abschnitt 'Experiment-Varianten' mit dem variablen Schlüssel 'link' wurde mit '/sales' überschrieben.]({% image_buster /assets/img/feature_flags/feature_flag_experiment_override.png %}){: style="max-width:80%"}

### Schritt 4: Zielgruppe auswählen

Verwenden Sie eines Ihrer Segmente oder Filter, um Ihre [Nutzer:innen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) auszuwählen. Sie können zum Beispiel den Filter **Received Feature-Flag Variant** verwenden, um Nutzer:innen, die bereits einen A/B-Test erhalten haben, erneut zu retargeten.

![Die Seite 'Target' in einem Feature-Flag Experiment mit 'Received Feature-Flag Variante' in der Suchleiste der Filtergruppe hervorgehoben.]({% image_buster /assets/img/feature_flags/variant-filter-dropdown.png %}){: style="max-width:70%"}

{% alert note %}
Die Segmentzugehörigkeit wird berechnet, wenn die Feature-Flags für einen bestimmten Nutzer aktualisiert werden. Die Änderungen werden bereitgestellt, wenn Ihre App die Feature-Flags aktualisiert oder wenn eine neue Sitzung gestartet wird.
{% endalert %}

### Schritt 5: Varianten verteilen

Wählen Sie die prozentuale Verteilung für Ihr Experiment. Es empfiehlt sich, die Verteilung nach dem Starten des Experiments nicht mehr zu ändern.

### Schritt 6: Konversionen zuweisen

Mit Braze können Sie nachverfolgen, wie oft Benutzer nach Erhalt einer Kampagne bestimmte Aktionen, d.h. [Conversion Events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), durchführen. Geben Sie ein Zeitfenster von bis zu 30 Tagen an, in dem eine Konversion gezählt wird, wenn der Nutzer die angegebene Aktion durchführt.

### Schritt 7: Überprüfen und starten

Nachdem Sie den letzten Teil Ihres Experiments fertiggestellt haben, überprüfen Sie dessen Details und wählen dann **Experiment starten**.

## Überprüfung der Ergebnisse

Nachdem Ihr Feature-Flag-Experiment abgeschlossen ist, können Sie die Impressions-Daten für Ihr Experiment überprüfen. Gehen Sie zu **Messaging** > **Kampagnen** und wählen Sie die Kampagne mit Ihrem Feature-Flag Experiment.

### Kampagnen-Analysen

**Campaign Analytics** bietet eine Übersicht über die Performance Ihres Experiments, z.B:

- Die Gesamtzahl der Impressionen
- Die Anzahl der eindeutigen Impressionen
- Die primäre Konversionrate
- Der Gesamtumsatz, der durch die Nachricht generiert wird
- Die geschätzte Zielgruppe

Sie können auch die Einstellungen des Experiments für Zustellung, Zielgruppe und Konversion einsehen.

### Feature-Flag Experiment Performance

**Feature-Flags Experimente Performance** zeigt, wie gut Ihre Nachricht in verschiedenen Dimensionen abgeschnitten hat. Die spezifischen Metriken, die Sie sehen, hängen von dem von Ihnen gewählten Messaging-Kanal ab und davon, ob Sie einen multivariaten Test durchführen. Um die mit jeder Variante verbundenen Feature-Flag-Werte zu sehen, wählen Sie **Vorschau**.
