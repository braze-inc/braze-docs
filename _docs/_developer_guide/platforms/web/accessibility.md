---
nav_title: Accessibility
article_title: Accessibility
platform: Web
page_order: 22
page_type: reference
description: "This article describes how Braze supports accessibility."

---

# Accessibility

> This article provides an overview of how Braze supports accessibility within your integration.

Braze Web SDK supports the standards provided by the [Web Content Accessibility Guidelines (WCAG 2.1)](https://www.w3.org/TR/WCAG21/). We maintain a [100/100 lighthouse score](https://developer.chrome.com/docs/lighthouse/accessibility/scoring) for content cards and in-app messages on all of our new builds to uphold our accessibility standard.

## Prerequisites

The minimum SDK version that satisfies WCAG 2.1 is close to v3.4.0. However, we recommend upgrading to at least v6.0.0 for major image tag fixes.

### Notable accessibility fixes

| Version | Type | Key changes |
|---------|------|-------------|
| **6.0.0** | **Major** | Images as `<img>` tags, `imageAltText` or `language` fields, general UI accessibility improvements |
| **3.5.0** | Minor | Scrollable text accessibility improvements |
| **3.4.0** | Fix | Content Cards `article` role fix |
| **3.2.0** | Minor | 45x45px minimum touch targets for buttons |
| **3.1.2** | Minor | Default alt text for images |
| **2.4.1** | **Major** | Semantic HTML (`h1` or `button`), ARIA attributes, keyboard navigation, focus management |
| **2.0.5** | Minor | Focus management, keyboard navigation, labels |
{: .reset-td-br-1, .reset-td-br-2 role="presentation" }

## Supported accessibility features

We support these features for content cards and in-app messages:

- ARIA roles and labels
- Keyboard navigation support
- Focus management
- Screen reader announcements
- Alt text support for images

## Accessibility guidelines for SDK integrations

Refer to [Building accessible messages in Braze]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/accessibility) for general accessibility guidelines. This guide provides tips and best practices for maximum accessibility when integrating the Braze Web SDK into your web application.

### Content Cards

#### Setting a maximum height

To prevent Content Cards from taking up too much vertical space and improve accessibility, you can set a maximum height on the feed container, such as in this example:

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

#### Viewport considerations

For Content Cards that are displayed inline, consider viewport constraints, such as in this example.

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

### In-app messages

{% alert warning %}
Do not put important information within slide up in-app messages, as they are not accessible for screen readers.
{% endalert %}

### Mobile considerations

#### Responsive design

The SDK includes responsive breakpoints. Confirm that your customizations work across screen sizes, such as in this example:

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

### Testing accessibility

#### Manual test checklist

Manually test your accessibility by completing these tasks:

- Navigate Content Cards and in-app messages with keyboard only (Tab, Enter, Space)
- Test with screen reader (NVDA, JAWS, VoiceOver)
- Verify all images have alt text
- Check color contrast ratios (use tools like WebAIM Contrast Checker)
- Test on mobile devices with touch
- Verify focus indicators are visible
- Test modal message focus trapping
- Verify all interactive elements are reachable by a keyboard

### Common accessibility issues

To avoid common accessibility issues, do the following:

1. **Keep focus styles:** The SDK's focus indicators are essential for keyboard users.
2. **Only use `display: none` on non-interactive elements:** Use `visibility: hidden` or `opacity: 0` to hide interactive elements.
3. **Don't override ARIA attributes:** The SDK sets appropriate ARIA roles and labels.
4. **Use `tabindex` attributes:** These control keyboard navigation order.
5. **Provide a scroll if you set `overflow: hidden`:** Confirm that scrollable content remains accessible.
6. **Don't interfere with built-in keyboard handlers:** Confirm that existing keyboard navigation works.