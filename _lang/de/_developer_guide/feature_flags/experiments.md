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

# Ein Feature Flag Experiment erstellen

> Mit Feature-Flag-Experimenten können Sie A/B-Tests mit Anwendungsänderungen durchführen, um die Konversionsraten zu optimieren. Marketer können Feature-Flags verwenden, um herauszufinden, ob sich ein neues Feature positiv oder negativ auf die Konversionsraten auswirkt, oder welche Feature-Flag-Eigenschaften am besten geeignet sind.

## Voraussetzungen

Bevor Sie Nutzerdaten im Experiment tracken können, muss Ihre App aufzeichnen, wann ein Nutzer mit einem Feature-Flag interagiert. Dies wird als Feature-Flag-Impression bezeichnet. Vergewissern Sie sich, dass Sie jedes Mal eine Feature-Flag-Impression protokollieren, wenn ein Nutzer das zu testende Feature sieht oder gesehen haben könnte, auch wenn er in der Kontrollgruppe ist.

Weitere Informationen zur Protokollierung von Feature-Flag-Impression finden Sie unter [Erstellen von Feature-Flags]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#impressions).

```javascript
const featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag?.enabled) {
   return <NewFeature />
} else {
   return <ExistingFeature />
}

```

## Schritt 1: Ein Experiment erstellen

1. Gehen Sie zu **Messaging** > **Kampagnen** und klicken Sie auf **\+ Kampagne erstellen**.
2. Wählen Sie **Feature Flag Experiment**.
3. Geben Sie Ihrer Kampagne einen klaren und aussagekräftigen Namen.

## Schritt 2: Experimentiervarianten hinzufügen

Als nächstes erstellen Sie Variationen. Wählen Sie für jede Variante das Feature-Flag aus, das Sie aktivieren oder deaktivieren möchten, und überprüfen Sie die zugewiesenen Eigenschaften.

Um die Wirkung Ihres Features zu testen, verwenden Sie Varianten, um den Traffic in zwei oder mehr Gruppen aufzuteilen. Nennen Sie eine Gruppe "Meine Kontrollgruppe" und deaktivieren Sie die Feature-Flags.

### Überschreiben von Eigenschaften

Auch wenn Sie bei der ursprünglichen Einrichtung Ihres Funktionsmerkmals Standardeigenschaften festgelegt haben, können Sie diese Werte für Benutzer, die eine bestimmte Kampagnenvariante erhalten, überschreiben.

![]({% image_buster /assets/img/feature_flags/feature_flag_experiment_override.png %}){: style="max-width:80%"}

Um zusätzliche Standardeigenschaften zu bearbeiten, hinzuzufügen oder zu entfernen, bearbeiten Sie die Funktionsflagge selbst unter **Messaging** > **Funktionsflaggen**.

Wenn eine Variante deaktiviert ist, gibt das SDK ein leeres Eigenschaften-Objekt für das angegebene Feature-Flag zurück. 

## Schritt 3: Zielgruppe auswählen

Als Nächstes müssen Sie durch Auswählen von Segmenten oder Filtern eine [Zielgruppe zusammenstellen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/). Die Segmentzugehörigkeit wird berechnet, wenn die Feature-Flags für einen bestimmten Nutzer aktualisiert werden.

{% alert note %}
Die Änderungen werden bereitgestellt, wenn Ihre App die Feature-Flags aktualisiert oder wenn eine neue Sitzung gestartet wird.
{% endalert %}

## Schritt 4: Varianten verteilen

Wählen Sie die prozentuale Verteilung für Ihr Experiment. Es empfiehlt sich, die Verteilung nach dem Starten des Experiments nicht mehr zu ändern.

## Schritt 5: Konversionen zuweisen

Mit Braze können Sie nachverfolgen, wie oft Benutzer nach Erhalt einer Kampagne bestimmte Aktionen, d.h. [Conversion Events]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/), durchführen. Geben Sie ein Zeitfenster von bis zu 30 Tagen an, in dem eine Konversion gezählt wird, wenn der Nutzer die angegebene Aktion durchführt.

## Schritt 6: Überprüfen und starten

Nachdem Sie den letzten Teil Ihres Experiments erstellt haben, überprüfen Sie die Details und klicken dann auf **Experiment starten**.



