---
nav_title: AMP pour e-mail
permalink: /amphtml/
hidden: true
---

# AMP pour e-mail

Avec [AMP for Email](https://amp.dev/about/email), vous pouvez ajouter des éléments interactifs à vos e-mails et améliorer vos communications avec vos clients à un tout autre niveau.

## Exigences

Braze n’est en aucun cas responsable de l’inscription d’un client auprès de Google ou de son application des exigences de sécurité nécessaires.

Configuration requise   | Description
--------------| -----------
Activation de compte Gmail | Voir [activation du compte Gmail](#enabling-gmail-account).
Authentification de l’expéditeur Google | Gmail authentifie l’expéditeur des e-mails AMP avec [DomainKeys Identified Mail (DKIM)](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail), [Sender Policy Framework (SPF)](https://en.wikipedia.org/wiki/Sender_Policy_Framework), et [la spécification technique DMARC](https://en.wikipedia.org/wiki/DMARC). <br> Pour en savoir plus, cliquez [ici](https://developers.google.com/gmail/ampemail/security-requirements#sender_authentication).
Éléments d’e-mail AMP | Découvrez l’onglet Essentials dans la section [Composants](#components). |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
À l’heure actuelle, seul Gmail prend en charge AMP for Email. [Inscrivez-vous auprès de Google ici](https://developers.google.com/gmail/ampemail/register).
{% endalert %}

### Activation d’un compte Gmail

Accédez à vos paramètres Gmail et sélectionnez `Enable Dynamic Content`.

![Contenu dynamique][1]

## Utilisation de l’API

Vous pouvez utiliser AMP for Email à l’aide de notre API. Lorsque vous utilisez un [nos endpoints de messagerie]({{site.baseurl}}/api/endpoints/messaging/) pour envoyer un e-mail, ajoutez `amp_body` comme spécification d’objet, comme indiqué dans les éléments suivants :

### Spécifier l’objet d’un e-mail

```json
{
  "app_id": (required, string) see App Identifier,
  "subject": (optional, string),
  "from": (required, valid email address in the format "Display Name <email@address.com>"),
  "reply_to": (optional, valid email address in the format "email@address.com" - defaults to your app group's default reply to if not set),
  "plaintext_body": (optional, valid plaintext, defaults to autogenerating plaintext from "body" when this is not set),
  "amp_body": (optional, updates the text-amp-html MIME type) the email body in AMPHTML. The MIME (Multipurpose Internet Mail Extensions) type to be referenced is "text/x-amp-html".
  "body": (required unless email_template_id is given, valid HTML),
  "preheader": (optional*, string) Recommended length 50-100 characters.
  "email_template_id": (optional, string) If provided, we will use the subject/body/should_inline_css values from the given email template UNLESS they are specified here, in which case we will override the provided template,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "extras": (optional, valid Key-Value Hash), extra hash - for SendGrid customers, this will be passed to SendGrid as Unique Arguments,
  "headers": (optional, valid Key-Value Hash), hash of custom extensions headers. Currently, only supported for SendGrid customers,
  "should_inline_css": (optional, boolean), whether to inline css on the body. If not provided, falls back to the default css inlining value for the App Group,
  "attachments": (optional, array), array of json objects like [{"file_name","url"}] that define the files you need attached. Your file name's extension will be detected automatically from the URL, which should return the appropriate `Content-Type` as a response header,
}
```

## Écrire votre e-mail AMP

Générez votre e-mail AMP à l’aide des [composants](#components), puis utilisez [notre API](#api-usage) pour envoyer. Veillez à utiliser `amp_body` pour l’HTML de votre AMP ! Vous pouvez également consulter [Tutoriel AMP](https://amp.dev/documentation/guides-and-tutorials/start/create_email?format=email) ou le [code échantillon](https://gist.github.com/CrystalOnScript/988c3f0a2eb406da27e9d9bf13a8bf73) pour voir à quoi le produit final doit ressembler. Vous pouvez également consulter la [bibliothèque complète de composants de messagerie AMP ici](https://amp.dev/documentation/components/?format=email/).

Lorsque vous écrivez votre e-mail pour notre API, nous **avons besoin** d’une version `body` HTML normale. Nous recommandons une version `plaintext_body` de votre e-mail AMP au cas où votre e-mail est envoyé via un fournisseur qui ne prend pas encore en charge AMP for Email.

### Composants

{% tabs %}
  {% tab Essentials %}

Voilà les éléments qui constituent un e-mail AMPHTML... AMP ! Chacun de ces éléments est requis dans le corps de votre e-mail AMP.

| Composant | Son utilité | Exemple |
|---------|--------------|---------|
| Identification de <br> `⚡4email` ou `amp4email`| Identifie votre e-mail comme un e-mail AMPHTML. | `<!doctype html>` <br> `<html ⚡4email>` <br> `<head>` |
| Chargement de l’exécution AMP <br> `<script>` | Allows AMP to fun within your email using JavaScript. | `<script async src="https://cdn.ampproject.org/v0.js"></script>`|
| CSS réutilisable | Masque le contenu jusqu’à ce que AMP soit chargé. <br> Les fournisseurs de messagerie qui prennent en charge les e-mails AMP instaurent des contrôles de sécurité renforcés qui permettent uniquement aux scripts AMP vérifiés de fonctionner dans leurs clients| `<style amp4email-boilerplate>body{visibility:hidden}</style>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

  {% endtab %}
  {% tab Dynamic %}

Vous voulez voir quelque chose de cool ? Oh mais, c’est ton e-mail. Utilisez ces composants pour créer des présentations et comportements dynamiques dans vos e-mails.

| Composant | Son utilité | Script requis |
|---------|--------------|---------|
| [Accordéon](https://amp.dev/documentation/components/amp-accordion?format=email) <br> `amp-accordion`| Permet à vos utilisateurs d’afficher la description de contenu et d’accéder à une section spécifique. | `<script async custom-element="amp-accordion" src="https://cdn.ampproject.org/v0/amp-accordion-0.1.js"></script>` |
| [Formulaires](https://amp.dev/documentation/components/amp-form?format=email) <br> `amp-form`| Créez des formulaires pour soumettre des champs d’entrée dans un document AMP. | `<script async custom-element="amp-form" src="https://cdn.ampproject.org/v0/amp-form-0.1.js"></script>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
Tout composant nécessitant une authentification doit utiliser les [jetons d’accès Google](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) ou les [jetons d’assertion de proxy](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}
  {% endtab %}
  {% tab Creative %}

  Laissez-vous séduire par les composants AMP qui sublimeront votre contenu.

| Composant | Son utilité | Script requis |
|---------|--------------|---------|
| [Image animée](https://amp.dev/documentation/components/amp-anim?format=email) <br> `amp-anim`| Afficher une image animée (généralement un GIF) gérée par l’exécution. | `<script async custom-element="amp-anim" src="https://cdn.ampproject.org/v0/amp-anim-0.1.js"></script>` |
| [Carrousel](https://amp.dev/documentation/components/amp-carousel?format=email) <br> `amp-carousel`| Afficher plusieurs extraits de contenu similaires le long d’un axe horizontal. | `<script async custom-element="amp-carousel" src="https://cdn.ampproject.org/v0/amp-carousel-0.1.js"></script>` |
| [Image](https://amp.dev/documentation/components/amp-img?format=email) | Un remplacement géré par l’exécution pour la balise HTML `img`. <br>  Vous pouvez également créer une [lightbox pour votre image](https://amp.dev/documentation/components/amp-image-lightbox?format=email). | `<amp-img alt="A view of the sea"` <br> `src="images/sea.jpg"` <br> `width="900"` <br>  `height="675"` <br>  `layout="responsive">`  <br> `</amp-img>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
Tout composant nécessitant une authentification doit utiliser les [jetons d’accès Google](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) ou les [jetons d’assertion de proxy](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}

  {% endtab %}
  {% tab Other %}

  Il y a plus que ces autres onglets. Voici d’autres composants amusants à consulter.

| Composant | Son utilité |
|---------|--------------|
| [Liaison des données et expressions](https://amp.dev/documentation/components/amp-anim?format=email) <br> `amp-bind`| Ajoute une interactivité dynamique personnalisée à vos pages AMP par liaison des données et expressions de type JS. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
Tout composant nécessitant une authentification doit utiliser les [jetons d’accès Google](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) ou les [jetons d’assertion de proxy](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}

  {% endtab %}
{% endtabs %}

### Utilisation d’amp-mustache

Comme Liquid, AMP prend en charge un langage de script pour les cas d’utilisation plus avancés.  Ce composant est appelé [amp-mustache](https://amp.dev/documentation/components/amp-mustache/?format=email).  Si vous voulez utiliser le langage Mustache, vous devrez le positionner entre les balises [brutes](https://shopify.github.io/liquid/tags/raw/) de Liquid.  Malheureusement, Liquid (le langage des marques utilisé pour Braze) et Mustache partagent la même syntaxe. 

En configurant votre contenu autour de la balise Raw (brute), le moteur de traitement Braze ignorera correctement tout le contenu situé entre les balises brutes et enverra la variable Mustache dont votre équipe a besoin.


### Métriques et analyses

| Métrique | Détails |
|---|---|
| Nombre total d’ouvertures | Le nombre total d’ouvertures dans les versions HTML et texte brut de votre e-mail AMP. |
| Nombre total de clics | Le nombre total de clics dans les versions HTML et texte brut de votre e-mail AMP. |
| Début AMP | Nombre total d’ouvertures pour l’e-mail HTML AMP, nombre cumulé de versions HTML, texte brut et AMPHTML de l’e-mail. |
| Clics AMP | Nombre total de clics pour l’e-mail HTML AMP, nombre cumulé de versions HTML, texte brut et AMPHTML de l’e-mail. |
{: .reset-td-br-1 .reset-td-br-2}  

- Notez que le nombre total de clics et le nombre de clics uniques ne tiennent pas compte des clics provenant d’un message AMP (HTML et texte brut uniquement). Les clics spécifiques AMP sont attribués à la métrique `amp_click`.

### Tests et résolution des problèmes

Avant d’envoyer votre e-mail AMP, nous vous recommandons d’effectuer un test selon [les directives de Gmail disponibles ici](https://developers.google.com/gmail/ampemail/testing-dynamic-email).

Pour que votre e-mail AMP soit envoyé et reçu sur un compte Gmail, l’e-mail doit répondre aux conditions suivantes :
- Les exigences en matière de sécurité d’AMP for Email doivent être respectées (voir [Exigences](#requirements)).
- La partie MIME AMP doit contenir un document AMP valide.
- L’e-mail doit inclure la partie MIME AMP avant la partie MIME HTML.
- La partie MIME AMP doit être inférieure à 100 Ko.

Si aucune de ces conditions ne génère d’erreur, contactez [l’assistance][support].

 [1]: {% image_buster /assets/img/dynamic-content.png %} « Contenu dynamique »
 [support]: {{site.baseurl}}/support_contact/
