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

Das Braze Web SDK unterstützt die Standards der [Web Content Accessibility Guidelines (WCAG 2.1)](https://www.w3.org/TR/WCAG21/). Wir halten bei allen unseren neuen Versionen einen [Lighthouse-Score von 100/100](https://developer.chrome.com/docs/lighthouse/accessibility/scoring) für Content-Cards und In-App-Nachrichten ein, um unseren Standard für Barrierefreiheit aufrechtzuerhalten.

## Voraussetzungen

Die Mindest-SDK-Version, die WCAG 2.1 erfüllt, liegt nahe an v3.4.0. Wir empfehlen jedoch, auf mindestens Version 6.0.0 zu upgraden, um wichtige Fehlerbehebungen bei Bild-Tags zu erhalten.

### Wichtige Verbesserungen der Barrierefreiheit

| Version | Typ | Wichtige Änderungen |
|---------|------|-------------|
| **6.0.0** | **Major** | Bilder als`<img>`Tags oder`language`Felder`imageAltText`, allgemeine Verbesserungen der Barrierefreiheit der UI |
| **3.5.0** | Geringfügig | Verbesserungen der Barrierefreiheit für scrollbaren Text |
| **3.4.0** | Behebung | Content-Cards`article`  Rollenanpassung |
| **3.2.0** | Geringfügig | Mindestgröße von 45 x 45 Pixel für Touch-Ziele bei Buttons |
| **3.1.2** | Geringfügig | Standard-Alt-Text für Bilder |
| **2.4.1** | **Major** | Semantisches HTML (`h1`oder `button`), ARIA-Attribute, Tastaturnavigation, Fokusverwaltung |
| **2.0.5** | Geringfügig | Fokusverwaltung, Tastaturnavigation, Beschriftungen |
{: .reset-td-br-1, .reset-td-br-2 role="presentation" }

## Unterstützte Barrierefreiheitsfeatures

Wir unterstützen die folgenden Features für Content-Cards und In-App-Nachrichten:

- ARIA-Rollen und -Labels
- Unterstützung der Tastaturnavigation
- Fokusmanagement
- Ankündigungen des Bildschirmlesegeräts
- Alt-Text-Unterstützung für Bilder

## Richtlinien zur Barrierefreiheit für SDK-Integrationen

Allgemeine Richtlinien zur Barrierefreiheit referenzieren Sie unter [„Barrierefreie Nachrichten in Braze erstellen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/accessibility)“. Dieser Leitfaden enthält Tipps und bewährte Verfahren für maximale Barrierefreiheit bei der SDK-Integration des Braze Web SDK in Ihre Webanwendung.

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

Bei Content-Cards, die inline angezeigt werden, sollten Sie die Einschränkungen des Darstellungsbereichs berücksichtigen, wie in diesem Beispiel dargestellt.

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
Bitte fügen Sie keine wichtigen Informationen in Slide-up-In-App-Nachrichten ein, da diese für Screenreader nicht zugänglich sind.
{% endalert %}

### Überlegungen zur Mobilität

#### Responsives Design

Das SDK enthält responsive Haltepunkte. Bitte überprüfen Sie, ob Ihre Anpassungen auf allen Bildschirmgrößen funktionieren, wie in diesem Beispiel:

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

### Prüfung der Barrierefreiheit

#### Manuelle Test-Checkliste

Bitte überprüfen Sie die Barrierefreiheit manuell, indem Sie die folgenden Schritte ausführen:

- Navigieren Sie ausschließlich mit der Tastatur (Tab, Enter, Leertaste) durch Content-Cards und In-App-Nachrichten.
- Bitte überprüfen Sie die Website mit einem Screenreader (NVDA, JAWS, VoiceOver).
- Bitte überprüfen Sie, ob alle Bilder über Alternativtext verfügen.
- Bitte überprüfen Sie die Farbkontrastverhältnisse (verwenden Sie dazu Tools wie den WebAIM Contrast Checker).
- Bitte testen Sie auf mobilen Geräten mit Touchscreen.
- Bitte überprüfen Sie, ob die Fokusindikatoren sichtbar sind.
- Modale Nachricht zum Testen des Fokus-Trappings
- Bitte überprüfen Sie, ob alle interaktiven Elemente über eine Tastatur erreichbar sind.

### Häufige Probleme bei der Barrierefreiheit

Um häufige Probleme mit der Barrierefreiheit zu vermeiden, gehen Sie bitte wie folgt vor:

1. **Fokusstile beibehalten:** Die Fokusindikatoren des SDK sind für Tastaturnutzer:innen von entscheidender Bedeutung.
2. **Bitte verwenden Sie dies ausschließlich`display: none` für nicht-interaktive Elemente:** Verwenden Sie`visibility: hidden`  oder`opacity: 0`  zum Ausblenden interaktiver Elemente.
3. **Bitte überschreiben Sie keine ARIA-Attribute:** Das SDK legt geeignete ARIA-Rollen und -Bezeichnungen fest.
4. **Verwenden Sie`tabindex`Attribute:** Diese steuern die Reihenfolge der Tastaturnavigation.
5. **Bitte stellen Sie eine Bildlaufleiste zur Verfügung, wenn Sie Folgendes festlegen`overflow: hidden`:** Bitte stellen Sie sicher, dass scrollbare Inhalte weiterhin zugänglich sind.
6. **Bitte greifen Sie nicht in die integrierten Tastatur-Handler ein:** Bitte überprüfen Sie, ob die vorhandene Tastaturnavigation ordnungsgemäß funktioniert.