---
nav_title: Accessibility
article_title: Accessibility
platform: Web
page_order: 22
page_type: reference
description: "This article describes our support for accessibility as well as limitations"

---

# Accessibility

> This article provides an overview of Braze's support for accessibility as well as consideration for your integration

Braze Web SDK supports the standards provided by the [Web Content Accessibility Guidelines (WCAG 2.1)](https://www.w3.org/TR/WCAG21/). We maintain a [100/100 lighthouse score](https://developer.chrome.com/docs/lighthouse/accessibility/scoring) for content cards, and in-app messages on all of our new builds to uphold our standard for accessibility.

---

## Prerequisites

The minimum SDK version that satisfies WCAG 2.1 is around v3.4.0. However, we recommend upgrading to at least v6.0.0 for major image tag fixes.

**Notable Accessibility Fixes**


| Version | Type | Key Changes |
|---------|------|-------------|
| **6.0.0** | **Major** | Images as `<img>` tags, `imageAltText`/`language` fields, general UI accessibility improvements |
| **3.5.0** | Minor | Scrollable text accessibility improvements |
| **3.4.0** | Fix | Content Cards `article` role fix |
| **3.2.0** | Minor | 45x45px minimum touch targets for buttons |
| **3.1.2** | Minor | Default alt text for images |
| **2.4.1** | **Major** | Semantic HTML (`h1`/`button`), ARIA attributes, keyboard navigation, focus management |
| **2.0.5** | Minor | Focus management, keyboard navigation, labels |

---

## Accessibility Features

The following are already supported for content cards, and in-app messages:

- ✅ ARIA roles and labels
- ✅ Keyboard navigation support
- ✅ Focus management
- ✅ Screen reader announcements
- ✅ Alt text support for images

## Accessibility Guide for SDK Integrators

Please read the [message fundamental accessibility guide](/docs/user_guide/engagement_tools/messaging_fundamentals/accessibility) first for general accessibility guidelines.

This guide provides Web SDK specific tips and best practices for ensuring maximum accessibility when integrating the Braze Web SDK into your web application.

### Content Cards

#### Setting Maximum Height

To prevent Content Cards from taking up too much vertical space and improve accessibility, you can set a maximum height on the feed container:

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

#### Viewport Considerations

For Content Cards displayed inline, consider viewport constraints:

```css
/* Limit feed height on mobile to prevent covering too much screen */
@media (max-width: 768px) {
  body > .ab-feed {
    max-height: 80vh; /* Leave space for other content */
  }
}
```

### In-App Messages

{% alert warning %}
Due to the nature of slide up in-app messages, they are not accessible for screen readers. Do not put important information within a slide up in-app message.
{% endalert %}

### Mobile Considerations

#### Responsive Design

The SDK includes responsive breakpoints. Ensure your customizations work across screen sizes:

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


### Testing Accessibility
#### Manual Testing Checklist

- Navigate Content Cards and In-App Messages with keyboard only (Tab, Enter, Space)
- Test with screen reader (NVDA, JAWS, VoiceOver)
- Verify all images have alt text
- Check color contrast ratios (use tools like WebAIM Contrast Checker)
- Test on mobile devices with touch
- Verify focus indicators are visible
- Test modal message focus trapping
- Verify all interactive elements are reachable via keyboard

### Common Accessibility Issues to Avoid

1. **Don't remove focus styles**: The SDK's focus indicators are essential for keyboard users
2. **Don't use `display: none` on interactive elements**: Use `visibility: hidden` or `opacity: 0` if you need to hide elements
3. **Don't override ARIA attributes**: The SDK sets appropriate ARIA roles and labels
4. **Don't remove `tabindex` attributes**: These control keyboard navigation order
5. **Don't set `overflow: hidden` without providing scroll**: Ensure scrollable content remains accessible
6. **Don't interfere with built-in keyboard handlers**: Ensure that existing keyboard navigation works