---
nav_title: AMP pour e-mail
article_title: AMP pour e-mail
alias: /amphtml/
page_order: 11
description: "Le présent article de référence fournit un aperçu des AMP pour les e-mails et des cas d’utilisation courants."
channel:
  - email

---

# AMP pour e-mail

> Avec [AMP pour les](https://amp.dev/about/email) e-mails, vous pouvez ajouter des éléments interactifs à vos e-mails et élever vos communications avec vos clients, en offrant une expérience complète directement dans la boîte de réception de votre utilisateur. AMP rend cela possible grâce à l'utilisation de divers composants qui peuvent être utilisés pour susciter de l’enthousiasme avec vos e-mails, par exemple avec des enquêtes, des questionnaires de feedback, des campagnes de vote, des évaluations, des centres d’abonnement, et plus encore. De tels outils peuvent offrir des possibilités d'accroître l'engagement et la fidélisation.

## Conditions

Braze n'est pas responsable de l'enregistrement des utilisateurs auprès de Google ou du respect des exigences de sécurité nécessaires.

| Condition   | Description |
| --------------| ----------- |
| Activation de l'AMP pour l'e-mail | AMP est disponible pour tout le monde. Contactez votre gestionnaire de compte si vous souhaitez activer cette fonctionnalité. |
| Activation du compte Gmail | Voir [Activation du compte Gmail.](#enabling-gmail-account) |
| Authentification de l'expéditeur par Google | Gmail [authentifie l'expéditeur](https://developers.google.com/gmail/ampemail/security-requirements#sender_authentication) des e-mails AMP avec DKIM, SPF et DMARC. Ceux-ci doivent être configurés pour votre compte. <br><br>- [Domain Keys Identified Mail](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail) (DKIM) <br>- [Sender Policy Framework](https://en.wikipedia.org/wiki/Sender_Policy_Framework)(SPF)<br>- [Authentification, notification et conformité des messages par domaine](https://en.wikipedia.org/wiki/DMARC)(DMARC)
| Éléments de l'e-mail AMP | Un e-mail AMP convaincant passe par l'utilisation stratégique de différents éléments. Reportez-vous à l'onglet Essentiels dans la section [Composants](#components) ci-dessous. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Clients pris en charge

Avant de pouvoir envoyer des e-mails AMP aux utilisateurs, vous devez vous inscrire auprès de nos clients. Le processus d'inscription implique l'envoi d'un e-mail HTML AMP de test pour obtenir l'approbation. Le délai d’approbation varie entre les clients. Suivez les liens d’enregistrement pour obtenir plus d’informations.

| Client | Lien d’enregistrement |
| ------ | -------- |
| Gmail | [Google](https://developers.google.com/gmail/ampemail/register) |
| FairEmail | [FairEmail](https://email.faircode.eu/) |
| Yahoo | [Yahoo](https://senders.yahooinc.com/amp/) |
| Mail.ru | [Mail.ru](https://postmaster.mail.ru/amp/) |

Pour obtenir la liste complète des plateformes prises en charge, reportez-vous à la [documentation 'AMP](https://amp.dev/support/faq/email-support). 

### Activation d’un compte Gmail

Accédez à vos paramètres Gmail et sélectionnez **Activer l'e-mail dynamique** dans la rubrique **Général.**

![Exemple de paramètres Gmail avec la case « Activer la messagerie dynamique » cochée.][1]

## Utilisation de l’API

Vous pouvez également utiliser AMP pour les e-mails avec notre API. Si vous utilisez l'un des [endpoints de messagerie]({{site.baseurl}}/api/endpoints/messaging/) Braze pour envoyer un e-mail, ajoutez `amp_body` comme spécification d'objet, comme indiqué ci-dessous.

### Spécification de l’objet E-mail

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

## Création de votre e-mail AMP

Tout d'abord, créez votre e-mail AMP à l'aide de [composants](#components). Ensuite, utilisez l'[API Braze](#api-usage) pour envoyer votre message, en veillant à inclure `amp_body` pour votre HTML AMP.

En plus du HTML AMP, nous exigeons une version HTML ordinaire du `body` et suggérons une version `plaintext_body` de votre e-mail AMP. Tous les e-mails AMP sont envoyés en plusieurs parties, ce qui signifie que Braze envoie un e-mail qui prend en charge le HTML, le texte brut et le HTML AMP. Cela devient utile dans le cas où votre e-mail est envoyé via un fournisseur qui ne prend pas encore en charge l'AMP pour l'e-mail, car l'e-mail sera automatiquement mis par défaut sur la version appropriée en fonction de l'utilisateur et de son appareil.

{% alert note %}
Lorsque vous créez un e-mail AMP, vérifiez que vous êtes bien dans l'éditeur AMP car le code AMP ne doit pas être ajouté à l'éditeur HTML.
{% endalert %}

Consultez ces ressources supplémentaires :

- [Tutoriel AMP](https://amp.dev/documentation/guides-and-tutorials/start/create_email?format=email)
- [Exemple de code](https://gist.github.com/CrystalOnScript/988c3f0a2eb406da27e9d9bf13a8bf73) pour voir à quoi doit ressembler le produit final. 
- [Bibliothèque de composants pour les e-mails AMP](https://amp.dev/documentation/components/?format=email/)

### Composants

{% tabs %}
  {% tab Essentiels %}

Ce sont ces éléments qui font d'un HTML AMP email...AMP'ed ! Chacun de ces éléments est requis dans le corps de votre e-mail AMP.

| Composant | Description | Exemple |
|---------|--------------|---------|
| Identification <br><br> `⚡4email` ou `amp4email`| Identifie votre e-mail en tant qu'e-mail HTML AMP. | `<!doctype html>` <br> `<html ⚡4email>` <br> `<head>` |
| Chargement de l’exécution AMP <br><br> `<script>` | Permet d'exécuter l'AMP dans votre e-mail à l'aide de JavaScript. | `<script async src="https://cdn.ampproject.org/v0.js"></script>`|
| CSS réutilisable | Masque le contenu jusqu’à ce qu’AMP soit chargé. <br> Les fournisseurs d'e-mails qui prennent en charge les e-mails AMP appliquent des contrôles de sécurité qui n'autorisent que les scripts AMP approuvés à s'exécuter dans leurs clients. | `<style amp4email-boilerplate>body{visibility:hidden}</style>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

  {% endtab %}
  {% tab Dynamique %}

Utilisez ces composants pour créer des présentations et comportements dynamiques dans vos e-mails.

| Composant | Description | Script requis |
|---------|--------------|---------|
| [Accordéon](https://amp.dev/documentation/components/amp-accordion?format=email) <br><br> `amp-accordion`| Permet aux utilisateurs de visualiser le plan du contenu et d'accéder à n'importe quelle section. | `<script async custom-element="amp-accordion" src="https://cdn.ampproject.org/v0/amp-accordion-0.1.js"></script>` |
| [Formulaires](https://amp.dev/documentation/components/amp-form?format=email) <br><br> `amp-form`| Créez des formulaires pour soumettre des champs d’entrée dans un document AMP. | `<script async custom-element="amp-form" src="https://cdn.ampproject.org/v0/amp-form-0.1.js"></script>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Tout composant nécessitant l'authentification de l'utilisateur doit utiliser des [jetons d'accès Google](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) ou des [jetons d'assertion de proxy](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}
  {% endtab %}
  {% tab Créatif %}

  Faites preuve de fantaisie avec les composants AMP, ceux-ci peuvent vous aider à adapter votre e-mail à votre audience.

| Composant | Description | Script requis |
|---------|--------------|---------|
| [Image animée](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-anim`| Affiche une image animée (généralement un GIF) gérée par le runtime. | `<script async custom-element="amp-anim" src="https://cdn.ampproject.org/v0/amp-anim-0.1.js"></script>` |
| [Carrousel](https://amp.dev/documentation/components/amp-carousel?format=email) <br><br> `amp-carousel`| Affiche plusieurs éléments de contenu similaires le long d'un axe horizontal. | `<script async custom-element="amp-carousel" src="https://cdn.ampproject.org/v0/amp-carousel-0.1.js"></script>` |
| [Image](https://amp.dev/documentation/components/amp-img?format=email) | Un remplacement géré par l’exécution pour la balise HTML `img`. <br>  Vous pouvez également créer une [lightbox pour votre image](https://amp.dev/documentation/components/amp-image-lightbox?format=email). | `<amp-img alt="A view of the sea"` <br> `src="images/sea.jpg"` <br> `width="900"` <br>  `height="675"` <br>  `layout="responsive">`  <br> `</amp-img>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Tout composant nécessitant l'authentification de l'utilisateur doit utiliser des [jetons d'accès Google](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) ou des [jetons d'assertion de proxy](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}

  {% endtab %}
  {% tab Autre %}

| Composant | Description |
|---------|--------------|
| [Liaison des données et expressions](https://amp.dev/documentation/components/amp-anim?format=email) <br><br> `amp-bind`| Ajoute une interactivité dynamique personnalisée à vos pages AMP par liaison des données et expressions de type JavaScript. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Tout composant nécessitant l'authentification de l'utilisateur doit utiliser des [jetons d'accès Google](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) ou des [jetons d'assertion de proxy](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}

{% endtab %}
{% endtabs %}

Pour obtenir une liste complète des composants AMP, consultez la [documentation AMP](https://amp.dev/documentation/components/?format=email).  

### Cas d’utilisation

{% tabs local %}
{% tab Sondages interactifs %}

En utilisant le composant `<amp-form>`, vous pouvez créer des sondages interactifs qui peuvent être remplis sans quitter la boîte de réception de l’e-mail. Vous pouvez le réaliser en utilisant `<amp-form>` pour envoyer la réponse au sondage et pour que votre back-end fournisse alors ces données agrégées. 

En voici quelques exemples :
* E-mail de sondage sur une conférence
* Mise à jour dynamique des éléments du flux
* E-mail de mise en favori d’un article

En utilisant ce composant, les utilisateurs peuvent soumettre ou effacer les valeurs du champ. En outre, selon la façon dont vous avez configuré votre e-mail, vous pouvez donner des indications supplémentaires aux utilisateurs, par exemple si l'envoi de l'enquête a réussi ou non, ou rendre les réponses de vos utilisateurs montrant les résultats de l'enquête (comme dans le cas d'une campagne de vote).

{% endtab %}
{% tab Contenu pouvant être réduit %}

Étendez vos sections de contenu en utilisant le composant `<amp-accordion>`. Ce composant vous permet d’afficher les sections de contenu pouvant être réduites ou étendues, ce qui permet aux utilisateurs de visualiser rapidement les contours du contenu et de se rendre dans n’importe quelle section. 

Si vous avez tendance à envoyer de longs articles éducatifs ou des recommandations personnalisées, cela permet aux internautes de jeter un coup d'œil sur le plan du contenu et de sauter à n'importe quelle section ou recommandation de produit spécifique pour obtenir plus de détails. Cela peut s'avérer particulièrement utile pour les utilisateurs de téléphones mobiles qui doivent faire défiler quelques phrases dans une section.
{% endtab %}
{% tab E-mails ayant beaucoup d’images %}

Si vous avez tendance à envoyer des e-mails contenant de nombreuses photos professionnelles, comme les marques de retailing, vous pouvez utiliser le composant `<amp-image-lightbox>` qui permet aux utilisateurs de s'engager avec une image qui les interpelle. Lorsqu’un utilisateur clique sur l’image, ce composant affiche l’image au centre du message, créant un effet de boîte lumineuse. 

En outre, le composant `<amp-image-lightbox>` permet à l'utilisateur d'afficher une description détaillée de l'image. Vous pouvez utiliser le même composant pour plusieurs images. Par exemple, si plusieurs images sont comprises dans votre e-mail, lorsque l’utilisateur clique sur n’importe laquelle d’entre elles, l’image s’affiche dans la boîte lumineuse.

{% endtab %}
{% tab E-mails basés sur les polices de caractères %}

Pour les e-mails qui reposent principalement sur du texte, le composant `<amp-fit-text>` vous permet de gérer la taille et l’ajustement du texte dans une zone donnée.

En voici quelques exemples :

- Mise à l'échelle du texte pour l'adapter à une zone
- Mise à l'échelle du texte pour l'adapter à la zone en utilisant une taille de police maximale que vous pouvez définir
- Troncature du texte lorsque le contenu déborde de la zone

{% endtab %}
{% endtabs %}

### Utilisation d’amp-mustache

Comme Liquid, AMP prend en charge un langage de script pour les cas d’utilisation plus avancés. Ce composant est appelé [`amp-mustache`](https://amp.dev/documentation/components/amp-mustache/?format=email). Lorsque vous incluez un langage de balisage Mustache, vous devez le positionner autour du tag [`raw`](https://shopify.github.io/liquid/tags/raw/) de Liquid. Notez que Liquid et Mustache partagent le même style de syntaxe. 

En positionnant votre contenu autour du tag `raw`, le moteur de traitement de Braze ignorera tout contenu entre les tags `raw` et enverra la variable Mustache dont votre équipe a besoin.

## Indicateurs et analyses

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Indicateur</th>
            <th>Détails</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split">Nombre total d’ouvertures</td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Opens' %} Pour les e-mails AMP, il s'agit du total des ouvertures pour les versions HTML et en clair.</td>
        </tr>
        <tr>
            <td class="no-split">Nombre total de clics</td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Clicks' %} Pour les e-mails AMP, il s'agit du total des clics dans les versions HTML et en texte clair.</td>
        </tr>
        <tr>
            <td class="no-split">Ouvertures AMP</td>
            <td class="no-split">{% multi_lang_include metrics.md metric='AMP Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split">Clics AMP</td>
            <td class="no-split">{% multi_lang_include metrics.md metric='AMP Clicks' %}</td>
        </tr>
    </tbody>
</table>

## Tests et résolution des problèmes

Notez que le nombre total de clics et les clics uniques ne tiennent pas compte des clics qui se produisent à partir d'un message AMP (HTML et texte en clair uniquement). Les clics spécifiques à l'AMP sont attribués à l'indicateur *amp_click.* 

Avant d'envoyer votre e-mail AMP, nous vous recommandons de le tester conformément à ces [directives de Gmail](https://developers.google.com/gmail/ampemail/testing-dynamic-email).

Pour que votre e-mail AMP soit envoyé et reçu sur un compte Gmail, l’e-mail doit répondre aux conditions suivantes :
- Les exigences de sécurité de l'AMP pour les e-mails doivent être respectées.
- La partie MIME AMP doit contenir un document AMP valide.
- L’e-mail doit inclure la partie MIME AMP avant la partie MIME HTML.
- La partie MIME de l'AMP doit être inférieure à 100 Ko.

Si aucune de ces conditions n'est à l'origine de l'erreur, contactez le [support][support].

### Foire aux questions

{% details Dois-je segmenter avec des e-mails AMP ? %}
Nous vous recommandons de ne pas segmenter pour envoyer à tous les types d’utilisateurs. La raison en est que nous envoyons les messages AMP en plusieurs parties en ayant les différentes versions comprises dans l’e-mail d’origine. Si un utilisateur ne peut pas voir la version AMP, il reviendra par défaut à la version HTML.
{% enddetails %}

{% details Avez-vous d'autres conseils pour créer un e-mail AMP ? %}
Consultez votre équipe d'ingénieurs pour créer les éléments AMP. Une fois que les éléments sont définis, nous vous encourageons à inclure toutes les ressources et tous les éléments de conception dont vous disposez pour le peaufiner le plus possible.
{% enddetails %}

[1]: {% image_buster /assets/img/dynamic-content.png %}
[support]: {{site.baseurl}}/support_contact/
