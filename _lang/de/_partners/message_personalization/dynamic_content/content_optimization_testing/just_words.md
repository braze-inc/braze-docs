---
nav_title: Just Words
article_title: Just Words
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Just Words, einer KI-basierten SaaS-Business-Plattform, die personalisierte Versionen bestehender Kampagnen erstellt und Betreffzeilen, kreative Inhalte und HTML-Layouts für E-Mails im Laufe der Zeit optimiert."
alias: /partners/just_words/
page_type: partner
---

# Just Words Integrationsleitfaden

> [Just Words](https://www.justwords.ai/) personalisiert Nachrichten in großem Umfang auf Lifecycle-Marketing-Kanälen und ermöglicht es Ihnen, Hunderte von Variationen dynamisch zu testen und unterdurchschnittliche Inhalte automatisch zu aktualisieren.

Wenn Sie Just Words mit Braze [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) verwenden, um Ihre bestehenden Kampagnen und Canvase von Braze zu personalisieren, nutzt Just Words Braze-Currents, um den Content dynamisch zu optimieren - damit Sie das nicht tun müssen.

## Was sind die Vorteile?

Nachdem Ihre Integration abgeschlossen ist, können Sie die Just Works Plattform nutzen, um:

- Sehen Sie Realtime-Experimentierergebnisse
- Kopie dynamisch bearbeiten
- Performance Insights anzeigen

{% alert note %}
Fragen? Kontaktieren Sie Just Words auf ihrer [Buchungsseite](https://www.justwords.ai/book-demo) oder über den gemeinsamen Slack-Kanal.
{% endalert %}

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Just Words Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Just Words-Konto](https://www.justwords.ai/). Wenn Sie noch kein Just Words-Konto haben, [vereinbaren Sie ein 30-minütiges Gespräch für das Onboarding](https://www.justwords.ai/book-demo). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration von Just Words mit Braze

### Schritt 1: Erstellen Sie eine Just Words Vorlage

1. Gehen Sie zu Ihrer Just Words Konsole und [erstellen Sie ein neues Template](https://console.justwords.ai/new).
2. Wählen Sie eine leicht zu merkende ID, die nur Buchstaben, Zahlen und Unterstriche enthält.
3. Füllen Sie grundlegende Angaben zur Kampagne aus.
4. Nutzen Sie KI, um personalisierte Varianten zu erstellen.

![Die Just Words Plattform zur Erstellung von Templates.]({% image_buster /assets/img/just_words/creation_interface.png %}){: style="max-width:80%;"}

### Schritt 2: Erstellen Sie einen Just Words API-Schlüssel

1. Gehen Sie zu **Org-Einstellungen** > **API-Schlüssel** > **API-Schlüssel generieren**.
2. Kopieren Sie den API-Schlüssel und speichern Sie ihn an einem sicheren Standort.

![Das Just Words API-Schlüssel-Formular.]({% image_buster /assets/img/just_words/api_key_form.png %}){: style="max-width:80%;"}

### Schritt 3: Verwenden Sie Just Words in Ihrem Braze-Inhalt

Just Words arbeitet mit Canvase und Kampagnen, indem es Connected-Content verwendet. Wenn Sie ein Canvas erstellen, sollte jeder E-Mail-Schritt einem eindeutigen Just Words Template entsprechen.

#### Schritt 3.1: Richten Sie Ihren A/B-Test ein

{% tabs %}
{% tab Canvas %}

1. Wählen Sie in einem Canvas **Variante hinzufügen** > **Variante hinzufügen**, bis Sie die gewünschte Anzahl von Varianten haben, und fügen Sie jeder Variante Schritte hinzu (z.B. einen Schritt für eine E-Mail Nachricht).
2. Teilen Sie den Verkehr der Zielgruppe nach Belieben auf. Wenn Sie zum Beispiel zwei Varianten haben, können Sie jeder Variante 50% geben. Oder Sie könnten zwei Varianten mit jeweils 40% und eine Kontrollgruppe mit 20% haben. Weitere Informationen über A/B-Tests für Canvase finden Sie unter [Erstellen eines Canvase]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
3. In den Composern für die Nachrichten-Schritte, die Sie mit Connected-Content verwenden möchten, fügen Sie das Snippet für Connected-Content aus der Just Words-Konsole ein, z. B. das folgende Snippet.

{% raw %}
```liquid
{% connected_content https://worker.justwords.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

![Braze A/B-Test Canvas-Einrichtung.]({% image_buster /assets/img/just_words/braze_canvas.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Kampagne %}

1. In dem Schritt **Nachrichten verfassen** Ihrer Kampagne erstellen Sie zwei Varianten.
2. Gehen Sie im Schritt **Zielgruppe** zum Abschnitt **A/B-Tests** und ändern Sie die Prozentsätze der Nutzer:innen, die jede Ihrer Varianten (und Ihre optionale Kontrollgruppe) erhalten sollen. Sie können Ihren Test weiter anpassen, indem Sie eine Optimierungsoption auswählen. Weitere Informationen über A/B-Tests für Kampagnen finden Sie unter [Erstellen von multivariaten und A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/).
3. Fügen Sie im Nachrichten-Editor das Snippet Connected-Content aus der Just Words-Konsole ein, z. B. das folgende Snippet.

{% raw %}
```liquid
{% connected_content https://worker.justwords.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

{% endtab %}
{% endtabs %}

#### Schritt 3.2:  Personalisierung mit angepassten Attributen hinzufügen (optional)

Um Ihre Nachrichten mit angepassten Attributen (wie `industry`) anzupassen, verwenden Sie das folgende Liquid-Format:

{% raw %}
```liquid
{% connected_content https://worker.justwords.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}&attrs.industry={{ custom_attribute.industry }}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

Beachten Sie, dass das angepasste Attribut von `industry` durch {% raw %}```&attrs.industry={{ custom_attribute.industry }}```{% endraw %} gekennzeichnet ist. 

![Braze Liquid Logik in einem HTML Nachrichten-Editor.]({% image_buster /assets/img/just_words/just_words_personalization.png %}){: style="max-width:80%;"}

### Schritt 4: Vorschau auf die E-Mail

Vergewissern Sie sich, dass Sie die E-Mail in Braze in der Vorschau anzeigen lassen, um sicherzustellen, dass der personalisierte Inhalt korrekt dargestellt wird.

![Braze Nachricht Vorschau für eine Just Words E-Mail.]({% image_buster /assets/img/just_words/just_words_preview.png %}){: style="max-width:80%;"}

### Schritt 5: Braze-Currents einrichten

Braze-Currents ermöglicht das Tracking und die Optimierung der Performance im Laufe der Zeit.

1. Gehen Sie in Braze zu **Partnerintegrationen** > **Datenexport**.
2. Wählen Sie **Neuen Teststrom erstellen** und wählen Sie dann **Test Amazon S3 Datenexport**.

![Dropdown-Menü "Neuen Teststrom erstellen" mit der Option "Amazon S3 Datenexport testen".]({% image_buster /assets/img/just_words/test_amazon_s3.png %}){: style="max-width:80%;"}

{: start="3" }
3\. Geben Sie die S3-Zugangs-ID, den geheimen AWS-Zugangsschlüssel, den Bucket-Namen und den Ordner ein, die Sie von Just Words beim Onboarding erhalten haben.

![Abschnitt "Zugangsdaten" für den geheimen AWS-Zugangsschlüssel.]({% image_buster /assets/img/just_words/aws_secret_access_key.png %}){: style="max-width:80%;"}

{: start="4" }
4\. Wählen Sie die Ereignisse aus, die Sie tracken möchten, z. B. Sendungen, Öffnungen, Klicks, Abmeldungen, Konversionen und andere.

![Abschnitt "Messaging Engagement Events" mit Ereignissen zum Auswählen.]({% image_buster /assets/img/just_words/message_engagement_events.png %}){: style="max-width:80%;"}

{: start="5" }
5\. Starten Sie den Braze-Currents.

Jetzt können Sie loslegen! Jetzt können Sie Just Words mit Braze Connected-Content verwenden.