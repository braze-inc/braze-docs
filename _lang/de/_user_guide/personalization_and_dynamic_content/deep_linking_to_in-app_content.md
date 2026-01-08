---
nav_title: Deeplinking zu In-App-Content
article_title: Deeplinking zu In-App-Content
page_order: 3
description: "Dieser Referenzartikel erklärt, wie Sie Deeplinking zu Ihren In-App-Nachricht-Inhalten hinzufügen können."

---

# Deeplinking zu In-App-Content

## Was ist Deep Linking?

Deeplinking ist eine Möglichkeit, eine native App zu starten und zusätzliche Informationen bereitzustellen, die sie anweisen, eine bestimmte Aktion durchzuführen oder bestimmte Inhalte anzuzeigen.

Dies besteht aus drei Teilen:

1. Identifizieren Sie die zu startende App.
2. Weisen Sie die App an, welche Aktion sie durchführen soll.
3. Stellen Sie der Aktion alle zusätzlichen Daten zur Verfügung, die sie benötigt.

Deep Links sind benutzerdefinierte URIs, die auf einen bestimmten Teil der App verweisen und alle drei dieser Teile enthalten. Der Schlüssel ist die Definition eines benutzerdefinierten Schemas. `http:` ist das Schema, mit dem fast jeder vertraut ist, aber Schemata können mit jedem beliebigen Wort beginnen. Ein Schema muss mit einem Buchstaben beginnen, kann dann aber Buchstaben, Zahlen, Pluszeichen, Minuszeichen oder Punkte enthalten. Praktisch gesehen gibt es kein zentrales Register, um Konflikte zu vermeiden, daher ist es eine gute Praxis, Ihren Domain-Namen in das Schema aufzunehmen. Zum Beispiel ist `twitter://` die iOS-URI zum Starten der mobilen App für X, ehemals Twitter.

Alles nach dem Doppelpunkt innerhalb eines Deeplinks ist Freitext. Es liegt an Ihnen, seine Struktur und Interpretation zu definieren; eine gängige Konvention ist jedoch, ihn nach `http:` URLs zu modellieren, einschließlich eines führenden `//` und Abfrageparametern (zum Beispiel `?foo=1&bar=2`). Im vorherigen Beispiel würde `twitter://user?screen_name=[id]` verwendet, um ein bestimmtes Profil in der App zu starten.

{% alert important %}
Braze unterstützt nicht die Verwendung eines Wrappers wie Flutter, um Deeplinks zu setzen. Um dieses Feature zu nutzen, müssen Sie Deeplinks auf der nativen Ebene konfigurieren.
{% endalert %}

## UTM-Tags und Kampagnenzuordnung

### Was ist ein UTM Tag?

Mit [UTM-Tags (Urchin Traffic Manager)](https://support.google.com/analytics/answer/10917952?sjid=14344007686729081565-NC#zippy=%2Cin-this-article) können Sie Details zur Kampagnenzuordnung direkt in Links einfügen. UTM-Tags werden von Google Analytics zur Erfassung von Kampagnen-Attributionsdaten verwendet und können zur Verfolgung der folgenden Eigenschaften verwendet werden:

- `utm_source`: Der Bezeichner für die Quelle des Datenverkehrs (z.B.`my_app`)
- `utm_medium`: Das Medium der Kampagne (z.B.`newsfeed`)
- `utm_campaign`: Der Bezeichner für die Kampagne (z.B.`spring_2016_campaign`)
- `utm_term`: Bezeichner für einen bezahlten Suchbegriff, der den Nutzer:in zu Ihrer App oder Website geführt hat (z.B.`pizza`)
- `utm_content`: Ein Bezeichner für den spezifischen Link oder Inhalt, auf den der Nutzer:innen geklickt hat (z.B.`toplink` oder `android_iam_button2`)

UTM-Tags können sowohl in reguläre HTTP-(Web-)Links als auch in Deep Links eingebettet und mit Google Analytics verfolgt werden.

### Verwendung von UTM-Tags mit Braze

Wenn Sie UTM Tags mit normalen HTTP (Web)-Links verwenden möchten (z.B. für die Attribution von Kampagnen) und Ihr Unternehmen bereits Google Analytics nutzt, können Sie [den URL-Builder von Google](https://ga-dev-tools.google/ga4/campaign-url-builder/) verwenden, um UTM Links zu generieren. Diese Links können wie jeder andere Link in den Text einer Braze-Kampagne eingebettet werden.

Um UTM-Tags in Deep Links zu Ihrer App verwenden zu können, muss in Ihrer App das entsprechende [Google Analytics SDK](https://developers.google.com/analytics/devguides/collection/) integriert und korrekt für die Handhabung von Deep Links konfiguriert sein. Wenden Sie sich an Ihre Entwickler:innen, wenn Sie sich unsicher sind.

Nachdem das Analytics SDK integriert und konfiguriert ist, können UTM Tags mit Deeplinks in Kampagnen von Braze verwendet werden. Um UTM-Tags für Ihre Kampagne einzurichten, fügen Sie die erforderlichen UTM-Tags in die Ziel-URL oder Deep Links ein. Die folgenden Beispiele zeigen, wie Sie UTM-Tags in Push-Benachrichtigungen und In-App-Nachrichten verwenden können.

#### Push-Öffnungen mit UTM-Tags zuordnen

Um UTM-Tags in Ihre Deeplinks für Push-Benachrichtigungen einzubinden, stellen Sie das On-Click-Verhalten der Push-Nachricht auf einen Deeplink ein, schreiben Sie dann die Adresse des Deeplinks und fügen Sie die gewünschten UTM-Tags auf die folgende Weise ein:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=push&utm_campaign=spring2016giftcards&utm_content=ios_deeplink
```

![]({% image_buster /assets/img_archive/push_utm_tags.png %})

#### Klicks auf In-App-Nachrichten mit UTM-Tags zuordnen

Um UTM Tags in die Deeplinks in Ihren In-App-Nachrichten einzubinden, verwenden Sie Folgendes:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=iam&utm_campaign=spring2021giftcards&utm_content=web_link
```

![]({% image_buster /assets/img_archive/iam_utm_tags.png %})

