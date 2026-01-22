---
nav_title: CSS-Inlining
article_title: CSS-Inlining
page_order: 5.1
description: "In diesem Referenzartikel erfahren Sie, wie Sie das CSS-Inlining aktivieren können und welche bewährten Praktiken es gibt."
channel:
  - email

---

# CSS-Inlining

> CSS-Inlining ist eine Form der E-Mail-Vorverarbeitung, bei der Stile aus einem CSS-Stylesheet in den Textkörper einer HTML-E-Mail verschoben werden. Der Begriff "Inlining" bezieht sich auf die Tatsache, dass Stile "inline" auf einzelne HTML-Elemente angewendet werden.

Bei einigen E-Mail-Clients kann das CSS-Inlining die Darstellung von E-Mails verbessern und dazu beitragen, dass Ihre E-Mails so aussehen, wie Sie es erwarten. Wenn Sie bereits einen Großteil des CSS inlined haben oder sicher sind, dass Ihr HTML und CSS mit den Anforderungen der meisten Mail Clients kompatibel sind, ist es möglicherweise nicht notwendig, dieses Feature zu aktivieren. Es kann dazu führen, dass dynamisch eingebettete Stile mit Ihren bestehenden Inline-Stilen in Konflikt geraten und die erwartete Vorschau und das Rendering von E-Mails verändern.

## CSS-Inlining verwenden

Mit dem **Enablement CSS inline** umschalten auf dem Tab **Sendeinfo** des HTML-Editors können Sie festlegen, ob das CSS-Inlining für jede E-Mail Nachricht ein- oder ausgeschaltet wird.

![Kontrollkästchen zur Verwaltung des CSS-Inlinings im HTML Composer.]({% image_buster /assets/img_archive/css-inline2.png %}){: style="max-width:40%;"}

### Standard-Inlining-Status

Sie können unter **Einstellungen** > **E-Mail-Einstellungen** einen Standardstatus für die Aktivierung oder Deaktivierung festlegen. Suchen Sie die Einstellung für **CSS Inlining**. Diese Einstellung legt den gewünschten Standardwert fest, mit dem alle neuen E-Mail-Nachrichten beginnen. Beachten Sie, dass eine Änderung dieser Einstellung keine Auswirkungen auf Ihre bestehenden E-Mail-Nachrichten hat. Sie können diesen Standard auch jederzeit beim Verfassen von E-Mails außer Kraft setzen.

![Inline CSS auf neuen E-Mails als Standard-Option in den E-Mail-Einstellungen.]({% image_buster /assets/img_archive/css-inline1.png %})

