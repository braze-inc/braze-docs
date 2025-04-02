---
nav_title: Deeplinking zu In-App-Content
article_title: Deeplinking zu In-App-Content
page_order: 3
description: "Dieser Referenzartikel erklärt, wie Sie Deeplinking zu Ihren In-App-Nachricht-Inhalten hinzufügen können."

---

# Deeplinking zu In-App-Content

## Was ist Deep Linking?

Deeplinking ist eine Methode, eine native App zu starten und zusätzliche Informationen bereitzustellen, die sie anweisen, eine bestimmte Aktion durchzuführen oder bestimmte Inhalte anzuzeigen.

Dies besteht aus drei Teilen:

1. Identifizieren Sie die zu startende App
2. Weisen Sie die App an, welche Aktion sie durchführen soll
3. Stellen Sie der Aktion alle zusätzlichen erforderlichen Daten zur Verfügung

Deep Links sind benutzerdefinierte URIs, die auf einen bestimmten Teil der App verweisen und alle drei dieser Teile enthalten. Der Schlüssel ist die Definition eines benutzerdefinierten Schemas. `http:` ist das Schema, mit dem fast jeder vertraut ist, aber Schemata können mit jedem beliebigen Wort beginnen. Ein Schema muss mit einem Buchstaben beginnen, kann dann aber Buchstaben, Zahlen, Pluszeichen, Minuszeichen oder Punkte enthalten. Praktisch gesehen gibt es kein zentrales Register, um Konflikte zu vermeiden, daher ist es eine gute Praxis, Ihren Domain-Namen in das Schema aufzunehmen. Zum Beispiel ist `twitter://` die iOS-URI zum Starten der mobilen App für X, ehemals Twitter.

Alles nach dem Doppelpunkt innerhalb eines Deeplinks ist Freitext. Es ist Ihnen überlassen, seine Struktur und Interpretation zu definieren. Eine gängige Konvention ist jedoch, ihn nach `http:` URLs zu modellieren, einschließlich eines führenden `//` und Abfrageparametern (zum Beispiel `?foo=1&bar=2`). Im vorherigen Beispiel würde `twitter://user?screen_name=[id]` verwendet, um ein bestimmtes Profil in der App zu starten.

{% alert important %}
Braze unterstützt nicht die Verwendung eines Wrappers wie Flutter, um Deeplinks zu setzen. Um dieses Feature zu nutzen, müssen Sie Deeplinks auf der nativen Ebene konfigurieren.
{% endalert %}


## UTM-Tags und Kampagnenzuordnung

### Was ist ein UTM Tag?

Mit [UTM-Tags (Urchin Traffic Manager)][4] können Sie Details zur Kampagnenzuordnung direkt in Links einfügen. UTM-Tags werden von Google Analytics zur Erfassung von Kampagnen-Attributionsdaten verwendet und können zur Verfolgung der folgenden Eigenschaften verwendet werden:

- `utm_source`: die Kennung für die Quelle des Datenverkehrs (zum Beispiel`my_app`)
- `utm_medium`: das Kampagnenmedium (zum Beispiel`newsfeed`)
- `utm_campaign`: die Kennung für die Kampagne (zum Beispiel`spring_2016_campaign`)
- `utm_term`Bezeichner für einen bezahlten Suchbegriff, der die:den Nutzer:in zu Ihrer App oder Website geführt hat (z. B. `pizza`)
- `utm_content`Bezeichner für den spezifischen Link/Inhalt, auf den die:der Nutzer:in geklickt hat (zum Beispiel `toplink` oder `android_iam_button2`)

UTM-Tags können sowohl in reguläre HTTP-(Web-)Links als auch in Deep Links eingebettet und mit Google Analytics verfolgt werden.

### Verwendung von UTM-Tags mit Braze

Wenn Sie UTM-Tags mit regulären HTTP-Links (Web-Links) verwenden möchten - z. B. um Kampagnen-Attributionen für Ihre E-Mail-Kampagnen durchzuführen - und Ihr Unternehmen bereits Google Analytics verwendet, können Sie einfach [den URL-Builder von Google][6] verwenden, um UTM-Links zu generieren. Diese Links können wie jeder andere Link in den Text einer Braze-Kampagne eingebettet werden.

Um UTM-Tags in Deep Links zu Ihrer App verwenden zu können, muss in Ihrer App das entsprechende [Google Analytics SDK][5] integriert und korrekt für die Handhabung von Deep Links konfiguriert sein. Wenden Sie sich an Ihre Entwickler:innen, wenn Sie sich unsicher sind.

Nachdem das Analytics SDK integriert und konfiguriert ist, können UTM Tags mit Deeplinks in Kampagnen von Braze verwendet werden. Um UTM-Tags für Ihre Kampagne einzurichten, fügen Sie die erforderlichen UTM-Tags in die Ziel-URL oder Deep Links ein. Die folgenden Beispiele zeigen, wie Sie UTM-Tags in Push-Benachrichtigungen und In-App-Nachrichten verwenden können.

#### Push-Öffnungen mit UTM-Tags zuordnen

Um UTM-Tags in Ihre Deeplinks für Push-Benachrichtigungen einzubinden, stellen Sie das On-Click-Verhalten der Push-Nachricht auf einen Deeplink ein, schreiben Sie dann die Adresse des Deeplinks und fügen Sie die gewünschten UTM-Tags auf die folgende Weise ein:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=push&utm_campaign=spring2016giftcards&utm_content=ios_deeplink
```

![][8]

#### Klicks auf In-App-Nachrichten mit UTM-Tags zuordnen

Um UTM Tags in die Deeplinks in Ihren In-App-Nachrichten einzubinden, verwenden Sie Folgendes:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=iam&utm_campaign=spring2021giftcards&utm_content=web_link
```

![][10]

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/deep_linking/#Android_Deep_Advance
[4]: https://support.google.com/analytics/answer/1033863?hl=en
[5]: https://developers.google.com/analytics/devguides/collection/
[6]: https://support.google.com/analytics/answer/1033867
[8]: {% image_buster /assets/img_archive/push_utm_tags.png %}
[9]: {% image_buster /assets/img_archive/news_feed_utm_tags.png %}
[10]: {% image_buster /assets/img_archive/iam_utm_tags.png %}
[11]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/creating_a_news_feed_item/
