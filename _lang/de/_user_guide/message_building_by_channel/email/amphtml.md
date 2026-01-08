---
nav_title: AMP für E-Mail
article_title: AMP für E-Mail
alias: /amphtml/
page_order: 11
description: "Dieser Referenzartikel bietet einen Überblick über AMP für E-Mail und häufige Anwendungsfälle."
channel:
  - email

---

# AMP für E-Mail

> Mit [AMP für E-Mails](https://amp.dev/about/email) können Sie interaktive Elemente in Ihre E-Mails einfügen und die Kommunikation mit Ihren Kunden aufwerten, indem Sie ein umfassendes Erlebnis direkt in den Posteingang Ihrer Nutzer liefern. AMP macht dies durch die Verwendung verschiedener Komponenten möglich, mit denen sich spannende E-Mail-Angebote wie Umfragen, Feedback-Fragebögen, Abstimmungskampagnen, Rezensionen, Abo-Center und mehr erstellen lassen. Tools wie diese können Opportunitäten zur Steigerung des Engagements und der Bindung bieten.

## Anforderungen

Braze ist nicht dafür verantwortlich, dass sich Benutzer bei Google registrieren oder die erforderlichen Sicherheitsanforderungen erfüllen. AMP für E-Mail ist nur für SparkPost und SendGrid verfügbar.

| Anforderung   | Beschreibung |
| --------------| ----------- |
| AMP für E-Mail aktiviert | AMP ist für alle Nutzer:innen verfügbar. |
| Aktivierung des Gmail-Kontos | Siehe [Aktivieren des Google Mail-Kontos](#enabling-gmail-account). |
| Google Absender-Authentifizierung | Gmail [authentifiziert den Sender](https://developers.google.com/gmail/ampemail/security-requirements#sender_authentication) von AMP-E-Mails mit DKIM, SPF und DMARC. Diese müssen für Ihr Konto eingerichtet werden. <br><br>- [Domain Keys Identified Mail](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail) (DKIM) <br>- [Sender Policy Framework](https://en.wikipedia.org/wiki/Sender_Policy_Framework)(SPF)<br>- [Domänenbasierte Nachrichtenauthentifizierung, Berichterstattung und Konformität](https://en.wikipedia.org/wiki/DMARC)(DMARC)
| AMP-E-Mail-Elemente | Zu einer überzeugenden AMP-E-Mail gehört der strategische Einsatz verschiedener Komponenten. Siehe die Registerkarte Essentials im Abschnitt [Komponenten](#components) weiter unten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Unterstützte E-Mail Clients

Bevor Sie AMP-E-Mails an Nutzer:innen senden können, müssen Sie sich bei unseren E-Mail Clients registrieren. Der Registrierungsprozess beinhaltet das Versenden einer AMP HTML-Test E-Mail, um zugelassen zu werden. Die Genehmigungszeiten variieren von Client zu Client. Folgen Sie den Links zur Registrierung für weitere Informationen.

| Kunde | Registrierung Link |
| ------ | -------- |
| Gmail | [Google](https://developers.google.com/gmail/ampemail/register) |
| FairEmail | [FairEmail](https://email.faircode.eu/) |
| Yahoo | [Yahoo](https://senders.yahooinc.com/amp/) |
| Mail.ru | [Mail.ru](https://postmaster.mail.ru/amp/) |

Eine vollständige Liste der unterstützten E-Mail Clients finden Sie in der [AMP Dokumentation](https://amp.dev/support/faq/email-support).

### Aktivieren des Gmail-Kontos

Gehen Sie zu Ihren Google Mail-Einstellungen und wählen Sie unter **Allgemein** die Option **Dynamische E-Mail aktivieren**.

![Ein Beispiel für die Einstellungen von Google Mail mit ausgewähltem Kontrollkästchen "Dynamische E-Mails aktivieren".]({% image_buster /assets/img/dynamic-content.png %})

## API-Nutzung

Sie können AMP auch für E-Mails mit unserer API verwenden. Wenn Sie einen der [Endpunkte]({{site.baseurl}}/api/endpoints/messaging/) von Braze [Messaging]({{site.baseurl}}/api/endpoints/messaging/) verwenden, um eine E-Mail zu versenden, fügen Sie `amp_body` als Objektspezifikation wie unten gezeigt hinzu.

### Spezifikation des E-Mail-Objekts

```json
{
  "app_id": (required, string) see app identifier above,
  "subject": (optional, string),
  "from": (required, valid email address in the format "Display Name <email@address.com>"),
  "reply_to": (optional, valid email address in the format "email@address.com" - defaults to your workspace's default reply to if not set),
  "plaintext_body": (optional, valid plaintext, defaults to autogenerating plaintext from "body" when this is not set),
  "amp_body": (optional, updates the text-amp-html MIME type) the email body in AMP HTML. The MIME (Multipurpose Internet Mail Extensions) type to be referenced is "text/x-amp-html",
  "body": (required unless email_template_id is given, valid HTML),
  "preheader": (optional*, string) Recommended length 50-100 characters,
  "email_template_id": (optional, string) If provided, we will use the subject/body/should_inline_css values from the given email template UNLESS they are specified here, in which case we will override the provided template,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "extras": (optional, valid key-value hash), extra hash - for SendGrid customers, this will be passed to SendGrid as Unique Arguments,
  "headers": (optional, valid key-value hash), hash of custom extensions headers. Currently, only supported for SendGrid customers,
  "should_inline_css": (optional, boolean), whether to inline CSS on the body. If not provided, falls back to the default CSS inlining value for the workspace,
  "attachments": (optional, array), array of JSON objects like [{"file_name","url"}] that define the files you need attached. Your file name's extension will be detected automatically from the URL, which should return the appropriate `Content-Type` as a response header,
}
```

## Erstellen Ihrer AMP-E-Mail

Erstellen Sie zunächst Ihre AMP-E-Mail mit Hilfe von [Komponenten](#components). Als nächstes verwenden Sie die [Braze API](#api-usage), um Ihre Nachricht zu versenden. Achten Sie darauf, dass Sie `amp_body` für Ihr AMP HTML einbeziehen.

Zusätzlich zum AMP-HTML benötigen wir eine reguläre HTML-`body`-Version und schlagen eine `plaintext_body`-Version Ihrer AMP-E-Mail vor. Alle AMP-E-Mails werden mehrteilig versendet, d. h. Braze versendet eine E-Mail, die HTML, Klartext und AMP-HTML unterstützt. Dies ist nützlich, wenn Ihre E-Mail über einen Anbieter versendet wird, der AMP für E-Mails noch nicht unterstützt, da die E-Mail automatisch auf die entsprechende Version basierend auf dem Nutzer:innen und seinem Gerät eingestellt wird.

{% alert note %}
Wenn Sie eine AMP-E-Mail erstellen, vergewissern Sie sich, dass Sie sich im AMP-Editor befinden, da AMP-Code nicht in den HTML-Editor eingefügt werden sollte.
{% endalert %}

Beziehen Sie sich auf diese zusätzlichen Ressourcen:

- [AMP-Tutorial](https://amp.dev/documentation/guides-and-tutorials/start/create_email?format=email)
- [Beispielcode](https://gist.github.com/CrystalOnScript/988c3f0a2eb406da27e9d9bf13a8bf73), um zu sehen, wie das endgültige Produkt aussehen soll. 
- [AMP-E-Mail-Komponenten-Bibliothek](https://amp.dev/documentation/components/?format=email/)

### Komponenten

Bei der Erstellung der AMP-Elemente empfehlen wir Ihnen, sich mit Ihrem Entwicklerteam abzustimmen und Design-Ressourcen und -Elemente für einen zusätzlichen Feinschliff einzubeziehen.

{% tabs %}
  {% tab Essentials %}

Jedes dieser Elemente muss im Text Ihrer AMP-E-Mail enthalten sein.

| Komponente | Beschreibung | Beispiel |
|---------|--------------|---------|
| Identifikation <br><br> `⚡4email` oder `amp4email`| Kennzeichnet Ihre E-Mail als AMP-HTML-E-Mail. | `<!doctype html>` <br> `<html ⚡4email>` <br> `<head>` |
| AMP-Laufzeit laden <br><br> `<script>` | Ermöglicht die Ausführung von AMP in Ihrer E-Mail mithilfe von JavaScript. | `<script async src="https://cdn.ampproject.org/v0.js"></script>`|
| CSS Boilerplate | Blendet den Inhalt aus, bis AMP geladen ist. <br> E-Mail-Anbieter, die AMP-E-Mails unterstützen, führen Sicherheitsprüfungen durch, die nur die Ausführung geprüfter AMP-Skripte in ihren Clients zulassen. | `<style amp4email-boilerplate>body{visibility:hidden}</style>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

  {% endtab %}
  {% tab Dynamic %}

Verwenden Sie diese Komponenten, um dynamische Layouts und Verhaltensweisen in Ihren E-Mails zu erstellen.

| Komponente | Beschreibung | Erforderliches Skript |
|---------|--------------|---------|
| [Akkordeon](https://amp.dev/documentation/components/amp-accordion?format=email) <br><br> `amp-accordion`| Ermöglicht es Benutzern, die Inhaltsübersicht zu sehen und zu einem beliebigen Abschnitt zu springen. | `<script async custom-element="amp-accordion" src="https://cdn.ampproject.org/v0/amp-accordion-0.1.js"></script>` |
| [Formulare](https://amp.dev/documentation/components/amp-form?format=email) <br><br> `amp-form`| Erstellen Sie Formulare zur Übermittlung von Eingabefeldern in einem AMP-Dokument. | `<script async custom-element="amp-form" src="https://cdn.ampproject.org/v0/amp-form-0.1.js"></script>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Jede Komponente, die eine Authentifizierung des Nutzers oder der Nutzerin erfordert, muss [Google-Zugriffstoken](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) oder [Proxy-Assertion-Token](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens) verwenden.
{% endalert %}
  {% endtab %}
  {% tab Creative %}

  Nutzen Sie die AMP-Komponenten, mit denen Sie Ihre E-Mails auf Ihre Zielgruppe zuschneiden können.

| Komponente | Beschreibung | Erforderliches Skript |
|---------|--------------|---------|
| [Animiertes Bild](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-anim`| Zeigt ein animiertes Bild (normalerweise ein GIF) an, das über die Laufzeit verwaltet wird. | `<script async custom-element="amp-anim" src="https://cdn.ampproject.org/v0/amp-anim-0.1.js"></script>` |
| [Karussell](https://amp.dev/documentation/components/amp-carousel?format=email) <br><br> `amp-carousel`| Zeigt mehrere ähnliche Inhalte entlang einer horizontalen Achse an. | `<script async custom-element="amp-carousel" src="https://cdn.ampproject.org/v0/amp-carousel-0.1.js"></script>` |
| [Bild](https://amp.dev/documentation/components/amp-img?format=email) | Ein zur Laufzeit verwalteter Ersatz für den HTML `img` Tag. <br>  Sie können auch einen [Leuchtkasten für Ihr Bild](https://amp.dev/documentation/components/amp-image-lightbox?format=email) erstellen. | `<amp-img alt="A view of the sea"` <br> `src="images/sea.jpg"` <br> `width="900"` <br>  `height="675"` <br>  `layout="responsive">`  <br> `</amp-img>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Jede Komponente, die eine Authentifizierung des Nutzers oder der Nutzerin erfordert, muss [Google-Zugriffstoken](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) oder [Proxy-Assertion-Token](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens) verwenden.
{% endalert %}

  {% endtab %}
  {% tab Other %}

| Komponente | Beschreibung |
|---------|--------------|
| [Daten Bindung & Ausdrücke](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-bind`| Fügt Ihren AMP-Seiten über Datenbindung und JavaScript-ähnliche Ausdrücke eine benutzerdefinierte zustandsabhängige Interaktivität hinzu. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Jede Komponente, die eine Authentifizierung des Nutzers oder der Nutzerin erfordert, muss [Google-Zugriffstoken](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) oder [Proxy-Assertion-Token](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens) verwenden.
{% endalert %}

{% endtab %}
{% endtabs %}

Eine vollständige Liste der AMP-Komponenten finden Sie in der [AMP-Dokumentation](https://amp.dev/documentation/components/?format=email).  

### Anwendungsfälle

{% tabs local %}
{% tab Interactive Surveys %}

Mit der Komponente `<amp-form>` können Sie interaktive Umfragen erstellen, die ausgefüllt werden können, ohne den E-Mail-Posteingang zu verlassen. Verwenden Sie dazu `<amp-form>`, um die Antworten auf Umfragen zu übermitteln, und lassen Sie dann Ihr Backend diese aggregierten Daten liefern. 

Einige Beispiele sind:
* Umfrage zur Konferenz per E-Mail
* Artikel im Feed dynamisch aktualisieren
* E-Mail zu Lesezeichen für Artikel

Mit dieser Komponente können Benutzer Feldwerte übermitteln oder löschen. Je nachdem, wie Sie Ihre E-Mail einrichten, können Sie den Nutzern auch zusätzliche Hinweise geben, z. B. ob die Umfrage erfolgreich war oder nicht, oder die Antworten Ihrer Nutzer mit den Umfrageergebnissen darstellen (z. B. bei einer Abstimmungskampagne).

{% endtab %}
{% tab Collapsable Content %}

Erweitern Sie Ihre Content-Bereiche mit der Komponente `<amp-accordion>`. Mit dieser Komponente können Sie zusammenklappbare und erweiterbare Inhaltsabschnitte anzeigen, so dass die Betrachter einen Blick auf den Inhaltsüberblick werfen und zu einem beliebigen Abschnitt springen können. 

Wenn Sie eher lange, lehrreiche Artikel oder personalisierte Empfehlungen verschicken, bietet dies den Zuschauern die Möglichkeit, einen Blick auf die Inhaltsübersicht zu werfen und zu einem beliebigen Abschnitt oder einer bestimmten Produktempfehlung zu springen, um weitere Details zu erfahren. Dies kann besonders für Nutzer:innen hilfreich sein, die schon nach wenigen Sätzen in einem Abschnitt scrollen müssen.
{% endtab %}
{% tab Image Heavy Emails %}

Wenn Sie wie Einzelhandelsmarken dazu neigen, E-Mails mit vielen professionellen Fotos zu versenden, können Sie die Komponente `<amp-image-lightbox>` verwenden, die es Nutzer:innen ermöglicht, sich mit einem Bild zu engagieren, das sie anspricht. Wenn der Benutzer auf das Bild klickt, zeigt diese Komponente das Bild in der Mitte der Nachricht an und erzeugt so einen Leuchtkasteneffekt. 

Außerdem erlaubt die Komponente `<amp-image-lightbox>` dem Nutzer:innen, eine detaillierte Bildbeschreibung anzuzeigen. Sie können dieselbe Komponente für mehr als ein Bild verwenden. Wenn Sie z. B. mehrere Bilder in Ihrer E-Mail haben und der Benutzer auf eines der Bilder klickt, wird das Bild in einem Leuchtkasten angezeigt.

{% endtab %}
{% tab Font Driven Emails %}

Für E-Mails, die hauptsächlich auf Textkopien beruhen, können Sie mit der Komponente `<amp-fit-text>` die Größe und Einpassung des Textes in einen bestimmten Bereich verwalten.

Beispiele hierfür sind:

- Skalierung des Textes zur Anpassung an einen Bereich
- Skalierung des Textes, damit er in den Bereich passt, in dem Sie die maximale Schriftgröße einstellen können
- Abschneiden des Textes, wenn der Inhalt den Bereich überschreitet

{% endtab %}
{% endtabs %}

### AMP-Mustache verwenden

Ähnlich wie Liquid unterstützt AMP eine Skriptsprache für erweiterte Anwendungsfälle. Diese Komponente wird als [`amp-mustache`](https://amp.dev/documentation/components/amp-mustache/?format=email) bezeichnet. Wenn Sie eine beliebige Mustache-Markup-Sprache einfügen, müssen Sie sie um das [`raw`](https://shopify.github.io/liquid/tags/raw/)-Tag von Liquid einschließen. Beachten Sie, dass Liquid und Mustache das gleiche Syntax-Styling haben. 

Indem Sie Ihren Inhalt um den `raw` Tag wickeln, ignoriert die Braze-Verarbeitungsmaschine jeglichen Inhalt zwischen den `raw` Tags und sendet die von Ihrem Team benötigte Mustache-Variable aus.

## Metriken und Analysen

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Metrisch</th>
            <th>Details</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split">Öffnungen gesamt</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Opens' %} Bei AMP-E-Mails ist dies die Gesamtzahl der Öffnungen für die HTML- und die Klartextversion.</td>
        </tr>
        <tr>
            <td class="no-split">Klicks gesamt</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Clicks' %} Bei AMP-E-Mails ist dies die Gesamtzahl der Klicks in der HTML- und der Klartextversion.</td>
        </tr>
        <tr>
            <td class="no-split">AMP-Öffnungen</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='AMP Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split">AMP-Klicks</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='AMP Clicks' %}</td>
        </tr>
    </tbody>
</table>

## Testen und Fehlerbehebung

Beachten Sie, dass die Gesamtzahl der Klicks und die eindeutigen Klicks nicht die Klicks berücksichtigen, die von einer AMP-Nachricht (nur HTML und Klartext) ausgehen. AMP-spezifische Klicks werden der Attribution *amp_click* Metrik zugeordnet.

Bevor Sie Ihre AMP E-Mail versenden, empfehlen wir Ihnen, diese [Google Mail-Richtlinien](https://developers.google.com/gmail/ampemail/testing-dynamic-email) zu befolgen.

Damit Ihre AMP-E-Mail einem beliebigen Google Mail-Konto zugestellt werden kann, muss die E-Mail die folgenden Bedingungen erfüllen:

- Die AMP für E-Mail-Sicherheitsanforderungen müssen erfüllt werden.
- Der AMP-MIME-Teil muss ein gültiges AMP-Dokument enthalten.
- Die E-Mail sollte den AMP-MIME-Teil vor dem HTML-MIME-Teil enthalten.
- Der AMP-MIME-Teil muss kleiner als 100 KB sein.

Wenn keine dieser Bedingungen den Fehler verursacht, wenden Sie sich an den [Support]({{site.baseurl}}/support_contact/).

### Häufig gestellte Fragen

#### Sollte ich mit AMP E-Mails segmentieren?

Wir plädieren dafür, nicht zu segmentieren, um an alle verschiedenen Nutzer:innen zu senden. Das liegt daran, dass wir AMP-Nachrichten mehrteilig versenden, d. h. dass verschiedene Versionen in der ursprünglichen E-Mail enthalten sind. Wenn ein Nutzer:innen die AMP-Version nicht sehen kann, wird der Standard wieder auf HTML zurückgesetzt. 


