---
nav_title: In-App-Bewertungsaufforderung für iOS
article_title: In-App-Bewertungsaufforderung für iOS
page_order: 6
description: "Dieser Artikel beschreibt, wie Sie Braze verwenden können, um Nutzer:innen zu bitten, Ihre App zu bewerten."
channel:
  - in-app messages

---

# In-App-Bewertungsaufforderung für iOS

> Dieser Artikel beschreibt, wie Sie Braze verwenden können, um Nutzer:innen zu bitten, Ihre App zu bewerten. Tipps für eine effektive App-Bewertungskampagne finden Sie in [The Do's and Don'ts of Customer App Ratings](https://www.braze.com/resources/articles/the-dos-and-donts-of-customer-app-ratings).

Apple bietet eine native Eingabeaufforderung, die mit iOS 10.3 eingeführt wurde und mit der Benutzer Apps direkt aus der App heraus bewerten können. Wenn Sie App-Bewertungen von Benutzern über eine In-App-Nachricht unter iOS anfordern möchten, müssen Sie die systemeigene Eingabeaufforderung verwenden, da Apple benutzerdefinierte Bewertungsaufforderungen nicht zulässt (siehe [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/#code-of-conduct), Abschnitt 5.6.1).

Gemäß den Apple-Richtlinien können App-Bewertungsaufforderungen einem Nutzer bis zu dreimal pro Jahr angezeigt werden, so dass alle App-Bewertungskampagnen die [Ratenbegrenzung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) nutzen sollten. Benutzer können in ihren App-Einstellungen auch die Anzeige von App-Bewertungsaufforderungen vollständig deaktivieren. Weitere Informationen zu App Store-Bewertungen finden Sie in Apples Artikel über [Bewertungen, Rezensionen und Antworten](https://developer.apple.com/app-store/ratings-and-reviews/).

## Verwenden Sie Braze, um Benutzer um App-Bewertungen zu bitten

Apple verlangt zwar, dass Sie die systemeigene Eingabeaufforderung verwenden, aber Sie können dennoch die Vorteile von Braze-Kampagnen nutzen, um die Benutzer im richtigen Moment zu bitten, Ihre App zu bewerten und zu rezensieren. Es gibt zwei Hauptansätze, die Sie wählen können.

### Ansatz 1: Deeplinking zum App Store

Mit diesem Ansatz möchten Sie die Benutzer dazu ermutigen, den App Store zu besuchen, um eine Bewertung abzugeben. Erstellen Sie dazu eine In-App-Kampagne, die [Deeplinks]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) zum App Store enthält.

![Zwei mobile Bildschirme nebeneinander. Die erste ist eine In-App-Nachricht, die den Benutzer auffordert, die App im App Store zu bewerten. Die zweite ist die iOS App Store Seite für diese App.]({% image_buster /assets/img_archive/app_store_app_review.png %})

### Ansatz 2: Soft Priming

Wenn Sie nicht möchten, dass Nutzer:innen Ihre App verlassen, können Sie sie zunächst mit einer separaten In-App-Nachricht vorbereiten. Priming ist eine Möglichkeit, Nutzer:innen um Erlaubnis zu bitten, bevor Sie ihnen der native App Store-Bewertungs-Prompt senden. Erstellen Sie dazu eine In-App-Kampagne und fügen Sie einen angepassten Deeplink hinzu, der die Methode `requestReview` aufruft, wenn Sie darauf klicken. 

Detaillierte Schritte finden Sie unter [Aufforderung zur Überprüfung im App Store]({{site.baseurl}}/developer_guide/in_app_messages/customization/#swift_customizing-the-app-store-review-prompt).

![Zwei In-App-Nachrichten nebeneinander. Die erste veranlasst den Benutzer, die App zu bewerten, indem er gefragt wird, ob er einen Moment Zeit hat, die App zu bewerten. Die zweite ist die native iOS App Store-Bewertungs-Prompt, die eine Skala von fünf Sternen anzeigt, die der oder die Nutzer:in auswählen kann, um die App zu bewerten.]({% image_buster /assets/img_archive/prime_app_review.png %})

Die Benutzer geben eine Bewertung über die native App Store-Bewertungsabfrage ab und können eine Bewertung schreiben und abgeben, ohne die App zu verlassen.

### Überlegungen

Als Alternative zum Soft Priming können Sie auch direkt die Bewertungsaufforderung der iOS-App anzeigen lassen, ohne dass zuvor eine Meldung des Braze Soft Primers angezeigt wird. Das hat den Vorteil, dass der Benutzer, wenn er die Aufforderung zur Bewertung einer Anwendung nicht wünscht, nicht das suboptimale Benutzererlebnis hat, wenn er versucht, die Anwendung zu bewerten, aber keine Aufforderung dazu angezeigt wird.

{% alert important %}
Erstellen Sie keine angepassten HTML-In-App-Nachrichten, die einen nativen iOS-App-Bewertungs-Prompt imitieren, da dies gegen die Richtlinien von Apple verstößt.
{% endalert %}

