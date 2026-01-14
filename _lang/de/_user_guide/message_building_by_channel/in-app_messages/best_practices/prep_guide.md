---
nav_title: Anleitung zur Vorbereitung
article_title: Anleitung zur Vorbereitung von In-App-Nachrichten
page_order: 0.5

page_type: reference
description: "Dieser Artikel behandelt einige Fragen und bewährte Praktiken, die Sie vor der Erstellung Ihrer In-App-Nachrichten berücksichtigen sollten."
channel: in-app messages

---

# Anleitung zur Vorbereitung von In-App-Nachrichten

> Bevor Sie Ihre In-App-Nachrichten erstellen, sollten Sie einige der folgenden Themen berücksichtigen, damit Sie Ihre Nachrichten schnell und einfach erstellen können.

## Allgemeine Überlegungen

- Wenn Sie eine Kampagne erstellen, wie viele Varianten dieser Nachricht möchten Sie anzeigen? Ideen für Varianten-Tests finden Sie unter [Tipps für verschiedene Kanäle]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#tips-different-channels).
- Wenn Sie ein Canvas erstellen, wird diese Nachricht in diesem Schritt mit anderen Nachrichtenkanälen gekoppelt?
- Wann möchten Sie, dass [Ihre Nachricht abläuft]({{site.baseurl}}/canvas_in-app_messages/)?

## Überlegungen zum Targeting

- In-App-Nachrichten sind am besten für Nutzer geeignet, die Ihre App regelmäßig besuchen. Beziehen Sie diese Zielgruppe mit ein?
- Wo möchten Sie, dass Ihre Nutzer Ihre Nachricht sehen? In Ihrer Web-App? In Ihrer mobilen App?
- Welches Ereignis sollte diese Nachricht auslösen?
- Verwenden einige Ihrer Benutzer ältere Versionen Ihrer Anwendung? Wenn ja, kann es sein, dass sie einige Elemente Ihrer Nachricht nicht sehen können.
- Für welche Art von Gerät oder Geräten erstellen Sie diese Nachricht? Denken Sie daran, dass Sie Ihre Nachricht über das Feld **Vorschau** oder die Registerkarte **Test** in der Vorschau anzeigen können. Weitere Informationen finden Sie unter [Testen]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/).

## Inhaltliche Überlegungen

- Welche Sprachen werden Sie in dieser Nachricht verwenden?
- Wie lauten Ihre Kopf- und Fußzeilen? Sind sie auffällig und relevant für Ihren Benutzer?
- In-App-Nachrichten erscheinen nur für eine bestimmte Zeit. Ist Ihr Text prägnant und einprägsam?
- Werden Sie [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) verwenden, um eigene Texte hinzuzufügen?
- Liegt Ihr Bild oder ein anderes Medium bei In-App-Nachrichten im Vollbildmodus innerhalb der [Sicherheitszone]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/#image-safe-zone)?
- Möchten Sie bei In-App-Nachrichten zu Umfragen Attribute oder Übermittlungen protokollieren? Haben Sie Ihre Bestätigungsseite eingerichtet?

## Überlegungen zur Konvertierung

- Was ist Ihr Ziel für diese Nachricht? Wie können Sie das in Ihrer Nachricht darstellen?
- Bieten Ihre Schaltflächen Optionen, die für Ihre Benutzer sinnvoll sind? Was ist Ihre [wichtigste Aufforderung zum Handeln]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#buttons)?
- Verwenden Sie [Deeplinks zu anderen In-App-Inhalten]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content)? Verwenden Sie diese In-App-Nachricht, um eine [Anfrage für eine Genehmigung oder ein Push-Priming]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/) zu senden und zu akzeptieren?
- Haben Sie eine Option zum Beenden von Nachrichten? Falls nicht, können Sie dieses Snippet jederzeit kopieren und einfügen, um einen schnellen Button zu erstellen:
    ```html
    <a href="appboy://close">X</a>
    ```


