---
nav_title: Barrierefreiheit
article_title: Barrierefreiheit
platform: Web
page_order: 22
page_type: reference
description: "Dieser Artikel beschreibt, wie Braze die Barrierefreiheit unterstützt."

---

# Barrierefreiheit

> Dieser Artikel bietet eine Übersicht darüber, wie Braze die Barrierefreiheit innerhalb Ihrer Integration unterstützt.

Braze Web SDK unterstützt die Standards der [Web Content Accessibility Guidelines (WCAG 2.1)](https://www.w3.org/TR/WCAG21/). Um unseren Standard für Barrierefreiheit aufrechtzuerhalten, erhalten wir für Content-Cards und In-App-Nachrichten bei allen neuen Builds eine [100/100-Leuchtturmwertung](https://developer.chrome.com/docs/lighthouse/accessibility/scoring).

## Voraussetzungen

Die Mindestversion des SDK, die die WCAG 2.1 erfüllt, liegt nahe an v3.4.0. Wir empfehlen jedoch, mindestens auf v6.0.0 zu upgraden, um wichtige Korrekturen an den Tags für Bilder vorzunehmen.

### Bemerkenswerte Korrekturen zur Barrierefreiheit

| Version | Typ | Wichtige Änderungen |
|---------|------|-------------|
| **6.0.0** | **Major** | Bilder als `<img>` Tags, `imageAltText` oder `language` Felder, allgemeine UI Verbesserungen der Zugänglichkeit |
| **3.5.0** | Geringfügig | Verbesserungen der Zugänglichkeit von scrollbarem Text |
| **3.4.0** | Behebung | Content-Cards `article` Rolle beheben |
| **3.2.0** | Geringfügig | 45x45px Mindest-Targeting für Buttons |
| **3.1.2** | Geringfügig | Standard Alt-Text für Bilder |
| **2.4.1** | **Major** | Semantisches HTML (`h1` oder `button`), ARIA-Attribute, Tastaturnavigation, Fokusverwaltung |
| **2.0.5** | Geringfügig | Fokusverwaltung, Tastaturnavigation, Etiketten |
{: .reset-td-br-1, .reset-td-br-2 role="presentation" }

## Unterstützte Features für Barrierefreiheit

Wir unterstützen diese Features für Content-Cards und In-App-Nachrichten:

- ARIA-Rollen und -Bezeichnungen
- Unterstützung der Tastaturnavigation
- Schwerpunkt Management
- Bildschirmleser-Ankündigungen
- Alttext-Unterstützung für Bilder

## Zugänglichkeitsrichtlinien für SDK-Integrationen

Allgemeine Richtlinien zur [Barrierefreiheit]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/accessibility) finden Sie unter [Erstellen barrierefreier Nachrichten in Braze]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/accessibility). In diesem Leitfaden finden Sie Tipps und bewährte Verfahren für maximale Barrierefreiheit bei der Integration des Braze Web SDK in Ihre Webanwendung.

### Content-Cards

#### Festlegen einer maximalen Höhe

Um zu verhindern, dass Content-Cards zu viel vertikalen Platz einnehmen, und um die Zugänglichkeit zu verbessern, können Sie eine maximale Höhe für den Feed-Container festlegen, wie in diesem Beispiel:

{% raw %}
```css
/* Limit the height of the Content Cards feed */
.ab-feed {
  max-height: 600px; /* Adjust to your needs */
  overflow-y: auto;
}

/* For inline feeds (non-sidebar), you may want to limit individual cards */
.ab-card {
  max-height: 400px; /* Optional: limit individual card height */
  overflow: hidden;
}
```
{% endraw %}

#### Überlegungen zum Ansichtsfenster

Für Content-Cards, die inline angezeigt werden, sollten Sie die Einschränkungen des Ansichtsfensters berücksichtigen, wie in diesem Beispiel.

{% raw %}
```css
/* Limit feed height on mobile to prevent covering too much screen */
@media (max-width: 768px) {
  body > .ab-feed {
    max-height: 80vh; /* Leave space for other content */
  }
}
```
{% endraw %}

### In-App-Nachrichten

{% alert warning %}
Stellen Sie wichtige Informationen nicht in In-App-Nachrichten ein, da diese für Bildschirmleser nicht zugänglich sind.
{% endalert %}

### Mobile Überlegungen

#### Responsives Design

Das SDK enthält responsive Haltepunkte. Vergewissern Sie sich, dass Ihre Anpassungen bei allen Bildschirmgrößen funktionieren, wie in diesem Beispiel:

{% raw %}
```css
/* Mobile-specific accessibility considerations */
@media (max-width: 768px) {
  /* Ensure readable font sizes */
  .ab-feed {
    font-size: 14px; /* Minimum 14px for mobile readability */
  }
  
  /* Ensure sufficient touch targets */
  .ab-card {
    padding: 16px; /* Adequate padding for touch */
  }
}
```
{% endraw %}

### Zugänglichkeit testen

#### Checkliste für manuelle Tests

Testen Sie Ihre Zugänglichkeit manuell, indem Sie diese Aufgaben erledigen:

- Navigieren Sie in Content-Cards und In-App-Nachrichten nur mit der Tastatur (Tab, Enter, Leertaste)
- Test mit Bildschirmleseprogramm (NVDA, JAWS, VoiceOver)
- Überprüfen Sie, ob alle Bilder einen Alt-Text haben
- Überprüfen Sie das Farbkontrastverhältnis (verwenden Sie Tools wie WebAIM Contrast Checker)
- Test auf mobilen Geräten mit Touch
- Überprüfen Sie, ob die Fokusanzeigen sichtbar sind
- Testen Sie den Fokus von modalen Nachrichten
- Überprüfen Sie, ob alle interaktiven Elemente über eine Tastatur erreichbar sind.

### Häufige Probleme mit der Zugänglichkeit

Um häufige Probleme mit der Zugänglichkeit zu vermeiden, gehen Sie wie folgt vor:

1. **Behalten Sie den Fokusstil bei:** Die Fokusindikatoren des SDK sind für Nutzer:innen der Tastatur unerlässlich.
2. **Verwenden Sie `display: none` nur für nicht interaktive Elemente:** Verwenden Sie `visibility: hidden` oder `opacity: 0`, um interaktive Elemente auszublenden.
3. **Setzen Sie ARIA-Attribute nicht außer Kraft:** Das SDK legt die entsprechenden ARIA-Rollen und -Bezeichnungen fest.
4. **Verwenden Sie `tabindex` Attribute:** Diese steuern die Reihenfolge der Tastaturnavigation.
5. **Stellen Sie eine Schriftrolle bereit, wenn Sie `overflow: hidden` einstellen:** Bestätigen Sie, dass scrollbare Inhalte zugänglich bleiben.
6. **Greifen Sie nicht in die eingebauten Handler für die Tastatur ein:** Bestätigen Sie, dass die vorhandene Tastaturnavigation funktioniert.