---
nav_title: Intelligence Suite
article_title: Intelligence Suite
page_order: 10
layout: dev_guide
search_rank: 12
guide_top_header: "Intelligence Suite"
guide_top_text: "Die Braze Intelligence Suite unterstützt Sie bei der Automatisierung von Entscheidungsprozessen mit datenbasierten Insights. Von der Zustellung bis zu multivariaten Tests können Marken diese Tools und Features nutzen, um dynamische, kanalübergreifende Erlebnisse zu schaffen, die in großem Umfang optimiert werden. <br> <br> Die Intelligence Suite besteht aus drei Hauptfunktionen: Intelligentes Timing, intelligenter Kanal und intelligente Auswahl."
description: "Die Braze Intelligence Suite unterstützt Sie bei der Automatisierung von Entscheidungsprozessen mit datenbasierten Insights. Von der Zustellung bis zu multivariaten Tests können Marken diese Tools und Features nutzen, um dynamische, kanalübergreifende Erlebnisse zu schaffen, die in großem Umfang optimiert werden."

Tool:
  - Dashboard

guide_featured_title: "Tools und Funktionen"
guide_featured_list:
- name: Intelligentes Timing
  link: /docs/user_guide/brazeai/intelligence/intelligent_timing/
  image: /assets/img/braze_icons/clock.svg
- name: Intelligenter Kanal
  link: /docs/user_guide/brazeai/intelligence/intelligent_channel/
  image: /assets/img/braze_icons/mail-04.svg
- name: Intelligente Auswahl
  link: /docs/user_guide/brazeai/intelligence/intelligent_selection/
  image: /assets/img/braze_icons/hearts.svg

guide_menu_title: "Additional resources"
guide_menu_list:
- name: Intelligenz FAQ
  link: /docs/user_guide/brazeai/intelligence/faqs/
  image: /assets/img/braze_icons/annotation-question.svg


---

## Anwendungsfälle

Die Intelligence Suite bietet leistungsstarke Funktionen zur Analyse des Nutzerverlaufs und der Kampagnen- und Canvas-Performance und nimmt dann automatische Anpassungen vor, um Engagement, Zuschauerzahlen und Konversionen zu steigern. Einige Beispiele dafür, wie diese Funktionen verschiedenen Branchen zugute kommen können, finden Sie in den folgenden Anwendungsfällen.

### E-Commerce

- **Flash-Sales:** Verwenden Sie den [intelligenten Kanalfilter]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/), um die Benutzerhistorie zu untersuchen und die Benutzer zu identifizieren, die eher auf Push-Benachrichtigungen als auf E-Mails reagieren, und senden Sie dann Push-Benachrichtigungen und E-Mails an die entsprechenden Benutzer. Optional können Sie einen bestimmten Kanal für Nutzer:innen auswählen, die nicht über genügend Daten verfügen, um ihren bevorzugten Kanal zu bestimmen.
- **Werbebanner:** Verwenden Sie die [intelligente Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/), um die Leistung verschiedener Werbebanner in einer wiederkehrenden Kampagne zu analysieren und dann automatisch das Banner auszuwählen und zu versenden, das die höchsten Klickraten erzielt.

### Reisen

- **Paketangebote:** Verwenden Sie die Intelligente Auswahl, um verschiedene Pauschalreiseangebote in einem wiederkehrenden Canvas zu testen und den Canvas-Traffic nach und nach auf die Variante mit der besten Leistung zu verlagern, um höhere Buchungsraten zu erzielen.
- **Reiseangebote:** Verwenden Sie den Intelligenten Kanalfilter, um personalisierte Reiseangebote über den aktivsten Kanal eines Nutzers zu versenden, z. B. per E-Mail oder SMS, und so die Wahrscheinlichkeit zu erhöhen, dass der Nutzer auf Ihre Nachrichten reagiert.

### Unterhaltung

- **Neue Aktion für Inhalte:** Nutzen Sie [intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/), um Benachrichtigungen über neue Filme, Sendungen, Musik und andere Arten von Inhalten dann zu versenden, wenn Nutzer Ihre Nachrichten am ehesten öffnen.
- **In-Game-Käufe:** Verwenden Sie die intelligente Auswahl, um verschiedene Nachrichten für In-Game-Käufe zu testen und automatisch diejenige auszuwählen, die die höchsten Konversionsraten erzielt.

### Restaurant mit schnellem Dienst

Stellen wir uns vor, wir arbeiten bei SandwichEmperor, einem Schnellrestaurant, das ein neues, zeitlich begrenztes Menüangebot hat: den Royal Roast. Wir werden zwei Features der Intelligence Suite verwenden, um personalisierte Aktionen in einem Canvas zu versenden.

#### Verwenden Sie intelligentes Timing für den Versand von Benachrichtigungen

Wir verwenden Intelligent Timing, um die vergangenen Interaktionen unserer Nutzer mit unserer App und den einzelnen Nachrichtenkanälen zu analysieren und dann automatisch den besten Zeitpunkt auszuwählen, um den Royal Roast für jeden Nutzer zu bewerben. Einige Nutzer erhalten die Aktion vielleicht am Nachmittag, andere am Abend. 

Für Benutzer, die nicht über genügend frühere Interaktionen verfügen, die analysiert werden können, bieten wir einen Ausweichzeitpunkt an: die beliebteste Zeit für die Nutzung der App unter allen Benutzern.

![Einstellungen für intelligentes Timing bei der Zustellung eines Nachrichtenschritts.][1]

#### Verwenden Sie die intelligente Auswahl, um die Aktion auszuwählen

Für die eigentlichen Werbebotschaften werden wir Intelligent Selection verwenden, um drei verschiedene Nachrichten (Push-Benachrichtigung, E-Mail und SMS) für den Royal Roast zu testen. Intelligent Selection analysiert die Leistung aller unserer Werbebotschaften zweimal täglich und sendet dann nach und nach mehr von den leistungsstärksten Botschaften und weniger von den anderen.

Nachdem die Intelligente Auswahl genügend Daten gesammelt hat, um die Nachricht mit der besten Leistung zu ermitteln, wird diese Nachricht bei 100 % aller zukünftigen Sendungen verwendet.

![A/B-Testbereich eines Canvas mit aktivierter intelligenter Auswahl.][3]

#### Starten Sie das Canvas

Mit Intelligent Timing und Intelligent Selection haben wir unsere Royal Roast-Promotions so gestaltet, dass sie in Bezug auf Timing und Botschaft optimiert sind. Wir können unseren Canvas starten und beobachten, wie sich unsere Sendungen an die Vorlieben der Nutzer:innen anpassen.

[1]: {% image_buster /assets/img/intelligence_suite1.png %}
[3]: {% image_buster /assets/img/intelligent_selection_canvas.png %}
