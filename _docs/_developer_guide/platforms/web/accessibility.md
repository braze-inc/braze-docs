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

Braze supports the standards provided by the [Web Content Accessibility Guidelines (WCAG 2.1)](https://www.w3.org/TR/WCAG21/). We maintain a [100/100 lighthouse score](https://developer.chrome.com/docs/lighthouse/accessibility/scoring) for content cards, in-app messages, and content cards on all of our new builds to ensure we maintain our accessibility standards.

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

The following are already supported for content cards, in-app messages, banners:

- ✅ ARIA roles and labels
- ✅ Keyboard navigation support
- ✅ Focus management
- ✅ Screen reader announcements
- ✅ Alt text support for images

# Accessibility Guide for SDK Integrators

This guide provides tips and best practices for ensuring maximum accessibility when integrating the Braze Web SDK into your web application.

### Avoid Sporatic Viewport Changes

Session start modals, full, or HTML in-app messages may shift elements of the page around sporatically. This makes navigating via keyboard shortcuts more confusing for the user.

## Content Cards

### Setting Maximum Height

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

### Ensuring Scrollable Content is Accessible

The SDK automatically makes the feed scrollable with `overflow-y: auto`. Ensure your customizations maintain keyboard accessibility:

```css
/* Ensure the feed can receive focus and is scrollable with keyboard */
.ab-feed:focus {
  outline: 2px solid #1676d0; /* Visible focus indicator */
  outline-offset: 2px;
}
```

### Customizing Card Spacing

Adjust card spacing for better readability:

```css
.ab-card {
  margin-bottom: 20px; /* Default is 20px, adjust as needed */
}

/* Ensure sufficient spacing between cards for touch targets */
@media (max-width: 768px) {
  .ab-card {
    margin-bottom: 24px; /* Larger spacing on mobile */
  }
}
```

## In-App Messages

### Modal Message Accessibility

Modal messages automatically include:
- `role="dialog"` with `aria-modal="true"`
- Proper ARIA labels (`aria-labelledby` or `aria-label`)
- Focus trapping and keyboard navigation

Ensure your custom CSS doesn't interfere with these features:

```css
/* Don't override focus styles - SDK handles accessibility */
.ab-in-app-message:focus,
.ab-in-app-message *:focus {
  /* Let SDK handle focus styles */
}
```

### Scrollable Message Content

In-App Messages with long content automatically become scrollable. The SDK sets appropriate `max-height` values. If you customize heights, ensure scrolling remains accessible:

```css
.ab-message-text {
  /* SDK already handles overflow-y: auto */
  /* Maintain scrollable behavior for accessibility */
}
```

## Keyboard Navigation

### Built-in Keyboard Support

The SDK includes keyboard navigation support:

- **Content Cards Feed**: 
  - Tab navigation through cards and buttons
  - Enter/Space to activate buttons
  - Focus management for sidebar feeds

- **In-App Messages**:
  - Tab trapping in modal messages
  - Enter/Space to dismiss or interact
  - Escape key handling (where applicable)

### Custom Keyboard Handlers

If you add custom keyboard handlers, ensure they don't interfere with built-in accessibility:

```javascript
// Example: Adding custom keyboard navigation
document.addEventListener('keydown', (event) => {
  // Always check if the event was already handled
  if (event.defaultPrevented) {
    return;
  }
  
  // Your custom keyboard handling
});
```

## Screen Reader Support

### ARIA Attributes

The SDK automatically includes ARIA attributes:

- **Content Cards**:
  - `role="article"` on individual cards
  - `role="dialog"` on the feed container
  - `aria-label` on buttons and interactive elements
  - `aria-labelledby` for card titles

- **In-App Messages**:
  - `role="alert"` for slide-up messages
  - `role="dialog"` for modal messages
  - `aria-modal="true"` for modal dialogs
  - `role="article"` for message content

### Image Alt Text

Ensure images in Content Cards have descriptive alt text:

```javascript
// The SDK automatically sets alt text from card.altImageText
// Make sure your Braze dashboard provides meaningful alt text
// If no alt text is provided, the SDK uses an empty string (prevent verbose announcements)
```

**Best Practice**: Always provide meaningful alt text in your Braze campaigns for images in Content Cards.

### Semantic HTML

The SDK uses semantic HTML elements:
- `<h1>` for card titles
- `<button>` for interactive elements (close buttons, etc.)
- Proper heading hierarchy

Avoid overriding these with CSS that changes their semantic meaning.

## Visual Accessibility

### Color Contrast

Ensure sufficient color contrast when customizing colors:

```css
/* Minimum contrast ratios (WCAG AA):
   - Normal text: 4.5:1
   - Large text (18pt+): 3:1
   - UI components: 3:1
*/

/* Example: Customizing card text colors */
.ab-title {
  color: #333; /* Ensure sufficient contrast with background */
}

.ab-description {
  color: #545454; /* Default meets contrast requirements */
}

/* Links should have sufficient contrast */
.ab-url-area a {
  color: #1676d0; /* Default meets contrast requirements */
}
```

### Focus Indicators

The SDK provides focus indicators, but you can enhance them:

```css
/* Enhanced focus indicators for better visibility */
.ab-close-button:focus,
.ab-refresh-button:focus {
  outline: 2px solid #1676d0;
  outline-offset: 2px;
  opacity: 1; /* Close button becomes visible on focus */
}

/* Ensure all interactive elements have visible focus */
.ab-card a:focus {
  outline: 2px dashed #1676d0;
  outline-offset: 2px;
}
```

## Mobile Considerations

### Responsive Design

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

### Viewport Considerations

For Content Cards displayed inline, consider viewport constraints:

```css
/* Limit feed height on mobile to prevent covering too much screen */
@media (max-width: 768px) {
  body > .ab-feed {
    max-height: 80vh; /* Leave space for other content */
  }
}
```

## Testing Accessibility
### Manual Testing Checklist

- Navigate Content Cards and In-App Messages with keyboard only (Tab, Enter, Space)
- Test with screen reader (NVDA, JAWS, VoiceOver)
- Verify all images have alt text
- Check color contrast ratios (use tools like WebAIM Contrast Checker)
- Test on mobile devices with touch
- Verify focus indicators are visible
- Test modal message focus trapping
- Verify all interactive elements are reachable via keyboard

## Common Accessibility Issues to Avoid

1. **Don't remove focus styles**: The SDK's focus indicators are essential for keyboard users
2. **Don't use `display: none` on interactive elements**: Use `visibility: hidden` or `opacity: 0` if you need to hide elements
3. **Don't override ARIA attributes**: The SDK sets appropriate ARIA roles and labels
4. **Don't remove `tabindex` attributes**: These control keyboard navigation order
5. **Don't set `overflow: hidden` without providing scroll**: Ensure scrollable content remains accessible