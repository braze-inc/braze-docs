---
nav_title: AMP pour e-mail
article_title: AMP pour e-mail
alias: /amphtml/
page_order: 9.2
description: "Le présent article de référence fournit un aperçu des AMP pour les e-mails et des cas d’utilisation courants."
channel:
  - e-mail

---

# AMP pour e-mail

Avec [AMP pour les e-mails](https://amp.dev/about/email), vous pouvez ajouter des éléments interactifs à vos e-mails et améliorer vos communications avec vos clients à un tout autre niveau, en livrant une expérience complète directement dans la boîte de réception de votre utilisateur. AMP le rend possible en utilisant plusieurs composants qui peuvent vous aider à créer des communications par e-mail passionnantes comme des sondages, questionnaires de commentaires, campagnes de vote, critiques, centres d’abonnement et plus encore ! Ces outils vous proposent des opportunités importantes pour augmenter l’engagement et la rétention. 

{% alert important %}
AMP pour e-mail est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Conditions

Braze n’est en aucun cas responsable de l’inscription d’un client auprès de Google ou de son application des exigences de sécurité nécessaires.

| Condition   | Description |
| --------------| ----------- |
| AMP activé pour les e-mails | AMP est disponible pour tout le monde. Veuillez contacter votre gestionnaire du succès des clients pour qu’il œuvre avec votre équipe produit pour activer cette fonctionnalité pour vous. |
| Activation de compte Gmail | Consultez l’[activation du compte Gmail](#enabling-gmail-account) ci-dessous. |
| Authentification de l’expéditeur Google | Gmail authentifie l’expéditeur d’e-mails AMP avec DKIM, SPF et DMARC. Ceux-ci doivent être paramétrés pour votre compte. Apprenez-en plus [ici](https://developers.google.com/gmail/ampemail/security-requirements#sender_authentication). <br><br>- [E-mail identifié des clés de domaine](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail) (DKIM) <br>- [Cadre de politique de l’expéditeur](https://en.wikipedia.org/wiki/Sender_Policy_Framework) (SPF)<br>- [Authentification, reporting et conformité des messages basés sur les domaines](https://en.wikipedia.org/wiki/DMARC) (DMARC)
| Éléments d’e-mail AMP | Un e-mail AMP attractif comporte l’utilisation stratégique de plusieurs composants.<br>Découvrez l’onglet Essentials dans la section [Composants](#components) ci-dessous. |
{: .reset-td-br-1 .reset-td-br-2}

### Clients pris en charge

Avant de pouvoir envoyer des e-mails AMP à vos utilisateurs, vous devez vous enregistrer auprès de nos clients. Le processus d’enregistrement implique d’envoyer un e-mail de test AMPHTML pour qu’il soit approuvé. Le délai d’approbation varie entre les clients. Suivez les liens d’enregistrement pour obtenir plus d’informations.

| Client | Lien d’enregistrement |
| ------ | -------- |
| Gmail pour iOS | [Google](https://developers.google.com/gmail/ampemail/register) |
| Gmail pour Android | [Google](https://developers.google.com/gmail/ampemail/register) |
| Gmail Desktop | [Google](https://developers.google.com/gmail/ampemail/register) |
| Outlook sur le Web | [Outlook](https://docs.microsoft.com/en-us/outlook/amphtml/register-outlook)
| Mail.ru | [Mail.ru](https://postmaster.mail.ru/amp/?lang=en) |

Pour obtenir la liste complète des plateformes prises en charge, veuillez cliquer [ici](https://developers.google.com/gmail/ampemail/supported-platforms). 

### Activation d’un compte Gmail

Rendez-vous dans vos paramètres Gmail et, dans Général, cochez la case `Activer la messagerie dynamique`.

![Contenu dynamique][1]

## Utilisation de l’API

Vous pouvez utiliser AMP for Email à l’aide de notre API. Lorsque vous utilisez un [nos endpoints d’envoi de messages]({{site.baseurl}}/api/endpoints/messaging/) pour envoyer un e-mail, ajoutez `amp_body` comme spécification d’objet, comme indiqué ci-dessous.

### Spécifier l’objet d’un e-mail

```json
{
  "app_id": (required, string) see App Identifier above,
  "subject": (optional, string),
  "from": (required, valid email address in the format "Display Name <email@address.com>"),
  "reply_to": (optional, valid email address in the format "email@address.com" - defaults to your workspace's default reply to if not set),
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

Construisez votre e-mail AMP en utilisant les [composants](#components) ci-dessous. Consultez nos [exemples de cas d’utilisation](#example-use-cases) puis utilisez [nos API](#api-usage) pour envoyer votre message ! Veillez à utiliser `amp_body` pour l’HTML de votre AMP ! 

Vous pouvez aussi consulter : 
- Le [tutoriel AMP](https://amp.dev/documentation/guides-and-tutorials/start/create_email?format=email)
- L’[exemple de code](https://gist.github.com/CrystalOnScript/988c3f0a2eb406da27e9d9bf13a8bf73) pour voir comment le produit final devrait s’afficher. 
- [La bibliothèque de composants pour les e-mails complets AMP](https://amp.dev/documentation/components/?format=email/)

<br>
En plus de l’AMPHTML, nous __require__ une version du `body` en HTML ordinaire et suggérons une version `plaintext_body` de votre e-mail AMP. Tous les e-mails AMP sont envoyés en plusieurs parties ce qi signifie que Braze envoie un e-mail qui prend en charge l’HTML, le texte brut et l’AMPHTML. Cela peut s’avérer utile si votre e-mail est envoyé à l’aide d’un fournisseur qui ne prend pas encore en charge AMP pour les e-mails, basculant automatiquement par défaut sur la version appropriée selon l’utilisateur et son appareil.

### Composants

{% tabs %}
  {% tab Essentials %}

Voilà les éléments qui constituent un e-mail AMPHTML... AMP ! Chacun de ces éléments est requis dans le corps de votre e-mail AMP.

| Composant | Son utilité | Exemple |
|---------|--------------|---------|
| Identification <br><br> `⚡4email` ou `amp4email`| Identifie votre e-mail comme un e-mail AMPHTML. | `<!doctype html>` <br> `<html ⚡4email>` <br> `<head>` |
| Chargement de l’exécution AMP <br><br> `<script>` | Allows AMP to fun within your email using JavaScript. | `<script async src="https://cdn.ampproject.org/v0.js"></script>`|
| CSS réutilisable | Masque le contenu jusqu’à ce qu’AMP soit chargé. <br> Les fournisseurs de messagerie qui prennent en charge les e-mails AMP instaurent des contrôles de sécurité renforcés qui permettent uniquement aux scripts AMP vérifiés de fonctionner dans leurs clients| `<style amp4email-boilerplate>body{visibility:hidden}</style>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

  {% endtab %}
  {% tab Dynamic %}

Vous voulez voir quelque chose de cool ? Oh mais, c’est ton e-mail. Utilisez ces composants pour créer des présentations et comportements dynamiques dans vos e-mails.

| Composant | Son utilité | Script requis |
|---------|--------------|---------|
| [Accordéon](https://amp.dev/documentation/components/amp-accordion?format=email) <br><br> `amp-accordion`| Permet à vos utilisateurs d’afficher la description de contenu et d’accéder à une section spécifique. | `<script async custom-element="amp-accordion" src="https://cdn.ampproject.org/v0/amp-accordion-0.1.js"></script>` |
| [Formulaires](https://amp.dev/documentation/components/amp-form?format=email) <br><br> `amp-form`| Créez des formulaires pour soumettre des champs d’entrée dans un document AMP. | `<script async custom-element="amp-form" src="https://cdn.ampproject.org/v0/amp-form-0.1.js"></script>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
Tout composant nécessitant une authentification doit utiliser les [jetons d’accès Google](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) ou les [jetons d’assertion de proxy](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}
  {% endtab %}
  {% tab Creative %}

  Laissez-vous séduire par les composants AMP qui sublimeront votre contenu.

| Composant | Son utilité | Script requis |
|---------|--------------|---------|
| [Image animée](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-anim`| Afficher une image animée (généralement un GIF) gérée par l’exécution. | `<script async custom-element="amp-anim" src="https://cdn.ampproject.org/v0/amp-anim-0.1.js"></script>` |
| [Carrousel](https://amp.dev/documentation/components/amp-carousel?format=email) <br><br> `amp-carousel`| Afficher plusieurs extraits de contenu similaires le long d’un axe horizontal. | `<script async custom-element="amp-carousel" src="https://cdn.ampproject.org/v0/amp-carousel-0.1.js"></script>` |
| [Image](https://amp.dev/documentation/components/amp-img?format=email) | Un remplacement géré par l’exécution pour la balise HTML `img`. <br>  Vous pouvez également créer une [lightbox pour votre image](https://amp.dev/documentation/components/amp-image-lightbox?format=email). | `<amp-img alt="Une vue de la mer"` <br> `src="images/sea.jpg"` <br> `width="900"` <br>  `height="675"` <br>  `layout="responsive">`  <br> `</amp-img>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
Tout composant nécessitant une authentification doit utiliser les [jetons d’accès Google](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) ou les [jetons d’assertion de proxy](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}

  {% endtab %}
  {% tab Other %}

  Il y a plus que ces autres onglets. Voici d’autres composants amusants à consulter.

| Composant | Son utilité |
|---------|--------------|
| [Liaison des données et expressions](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-bind`| Ajoute une interactivité dynamique personnalisée à vos pages AMP par liaison des données et expressions de type JS. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
Tout composant nécessitant une authentification doit utiliser les [jetons d’accès Google](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) ou les [jetons d’assertion de proxy](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}

{% endtab %}
{% endtabs %}

Consultez la [documentation AMP](https://amp.dev/documentation/components/?format=email) pour obtenir une liste complète des composants AMP.  

### Exemples de cas d’utilisation
Vous trouverez ci-dessous quelques exemples de cas d’utilisation pour les divers composants abordés ci-dessus.

{% tabs local %}
{% tab Interactive Surveys %}
__Interactif Surveys__

Idée : En utilisant le composant `<amp-form>`, vous pouvez créer des sondages interactifs qui peuvent être remplis sans quitter la boîte de réception de l’e-mail. Vous pouvez le réaliser en utilisant `<amp-form>` pour envoyer la réponse au sondage et pour que votre back-end fournisse alors ces données agrégées. 

Quelques exemples :
* E-mail de sondage sur une conférence
* Mettre à jour dynamiquement des objets dans le flux
* E-mail de mise en favori d’un article

En utilisant ce composant, les utilisateurs peuvent soumettre ou effacer les valeurs du champ. En outre, selon le paramétrage de votre e-mail, vous pouvez effectuer des actions comme fournir des demandes supplémentaires aux utilisateurs telles que s’enquérir de la réussite ou non de l’envoi du sondage ou même afficher les réponses du sondage à votre utilisateur si cela est pertinent (c.-à-d. une campagne de vote)

{% endtab %}
{% tab Collapsable Content %}
__Pouvant être réduit Content__

Idée : Étendez vos sections de contenu en utilisant le composant `<amp-accordion>`. Ce composant vous permet d’afficher les sections de contenu pouvant être réduites ou étendues, ce qui permet aux utilisateurs de visualiser rapidement les contours du contenu et de se rendre dans n’importe quelle section. 

Si vous avez tendance à envoyer de longs articles éducatifs ou des recommandations personnalisées, il fournit à vos utilisateurs un moyen de visualiser rapidement les contours du contenu pour passer directement à une section donnée ou à un produit spécifique recommandé pour obtenir plus de détails. Il est également utile pour les appareils mobiles pour lesquels quelques phrases seulement dans une section nécessitent un défilement. Son utilisation efficace réduit le défilement nécessaire sur les appareils mobiles.
{% endtab %}
{% tab Image Heavy Emails %}
__Image lourde Emails__

Idée : Si vous avez tendance à envoyer des e-mails possédant un grand nombre de photos professionnelles, telles que des ventes de marques, vous pouvez utiliser le composant `<amp-image-lightbox>` pour permettre aux utilisateurs d’interagir avec une image qui leur plait. Lorsqu’un utilisateur clique sur l’image, ce composant affiche l’image au centre du message, créant un effet de boîte lumineuse. 

De plus, le composant `<amp-image-lightbox>` permet à l’utilisateur de zoomer, effectuer un panoramique ou afficher une description plus détaillée de l’image. Vous pouvez utiliser le même composant pour plusieurs images. Par exemple, si plusieurs images sont comprises dans votre e-mail, lorsque l’utilisateur clique sur n’importe laquelle d’entre elles, l’image s’affiche dans la boîte lumineuse.
{% endtab %}
{% tab Font Driven Emails %}
__Basé sur la police Emails__

Idée : Pour les e-mails qui reposent principalement sur du texte, le composant `<amp-fit-text>` vous permet de gérer la taille et l’ajustement du texte dans une zone donnée.

Quelques exemples :
  * Le texte se met à l’échelle pour s’ajuster à la zone
  * Le texte se met à l’échelle pour s’ajuster à la zone en utilisant une taille de police de caractères maximale que vous pouvez définir. 
  * Le texte se tronque lorsque le contenu déborde de la zone
{% endtab %}
{% endtabs%}

### Utilisation d’amp-mustache

Comme Liquid, AMP prend en charge un langage de script pour les cas d’utilisation plus avancés.  Ce composant est appelé [amp-mustache](https://amp.dev/documentation/components/amp-mustache/?format=email).  Si vous voulez utiliser le langage Mustache, vous devrez le positionner entre les balises [brutes](https://shopify.github.io/liquid/tags/raw/) de Liquid.  Malheureusement, Liquid (le langage des marques utilisé pour Braze) et Mustache partagent la même syntaxe. 

En configurant votre contenu autour de la balise Raw (brute), le moteur de traitement Braze ignorera correctement tout le contenu situé entre les balises brutes et enverra la variable Mustache dont votre équipe a besoin.

## Indicateurs et analyses

| Indicateur | Détails |
|---|---|
| Nombre total d’ouvertures | Le nombre total d’ouvertures dans les versions HTML et texte brut de votre e-mail AMP. |
| Nombre total de clics | Le nombre total de clics dans les versions HTML et texte brut de votre e-mail AMP. |
| Ouvertures AMP | Nombre total d’ouvertures pour l’e-mail HTML AMP, nombre cumulé de versions HTML, texte brut et AMPHTML de l’e-mail. |
| Clics AMP | Nombre total de clics pour l’e-mail HTML AMP, nombre cumulé de versions HTML, texte brut et AMPHTML de l’e-mail. |
{: .reset-td-br-1 .reset-td-br-2}  


## Tests et résolution des problèmes

Veuillez noter que le nombre total de clics et le nombre de clics uniques ne tiennent pas compte des clics provenant d’un message AMP (HTML et texte brut uniquement). Les clics spécifiques AMP sont attribués à l’indicateur `amp_click`.

Avant d’envoyer votre e-mail AMP, nous vous recommandons d’effectuer un test selon [les directives de Gmail disponibles ici](https://developers.google.com/gmail/ampemail/testing-dynamic-email).

Pour que votre e-mail AMP soit envoyé et reçu sur un compte Gmail, l’e-mail doit répondre aux conditions suivantes :
- Les exigences en matière de sécurité d’AMP pour les e-mails doivent être respectées (voir le tableau ci-dessus).
- La partie MIME AMP doit contenir un document AMP valide.
- L’e-mail doit inclure la partie MIME AMP avant la partie MIME HTML.
- La partie MIME AMP doit être inférieure à 100 Ko.

Si aucune de ces conditions ne génère l’erreur, contactez [l’assistance][support].

### Foire aux questions

{% details Dois-je segmenter avec les e-mails AMP ? %}
Nous vous recommandons de ne pas segmenter pour envoyer à tous les types d’utilisateurs. La raison en est que nous envoyons les messages AMP en plusieurs parties en ayant les différentes versions comprises dans l’e-mail d’origine. Si votre client ne peut pas afficher la version AMP, elle basculera par défaut vers l’HTML. 
{% enddetails %}

{% details Quelques conseils pour créer mes e-mails AMP ? %}
Reposez-vous le plus possible sur vos ingénieurs pour concevoir les éléments AMP. Une fois que les éléments sont définis, nous vous encourageons à inclure toutes les ressources et tous les éléments de conception dont vous disposez pour le peaufiner le plus possible. Présenter certaines des fonctionnalités apportées aux e-mails par AMP peut s’avérer irrésistible pour faire en sorte que votre équipe d’ingénierie en fasse une priorité.
{% enddetails %}

[1]: {% image_buster /assets/img/dynamic-content.png %} "Dynamic Content"
[support]: {{site.baseurl}}/support_contact/
