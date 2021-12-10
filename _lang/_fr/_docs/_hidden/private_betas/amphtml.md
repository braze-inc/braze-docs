---
nav_title: AMP pour les e-mails
permalink: /fr/amphtml/
hidden: vrai
---

# AMP pour les e-mails

Avec [AMP pour l'e-mail](https://amp.dev/about/email), vous pouvez ajouter des éléments interactifs à vos e-mails et élever vos communications avec vos clients à un tout nouveau niveau.

## Exigences

Braze n'est pas responsable de l'enregistrement du client auprès de Google ou du respect des exigences de sécurité nécessaires.

| Exigences                      | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Activation du compte Gmail     | [Voir ci-dessous.](#enabling-gmail-account)                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Authentification Google Sender | Gmail authentifie l'expéditeur des emails AMP avec [Domain Keys Identified Mail](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail), [Sender Policy Framework](https://en.wikipedia.org/wiki/Sender_Policy_Framework), et [Authentication, Rapports et Conformité de messages basés sur le domaine](https://en.wikipedia.org/wiki/DMARC). <br> En savoir plus [ici](https://developers.google.com/gmail/ampemail/security-requirements#sender_authentication). |
| Éléments de courriel AMP       | Consultez l'onglet Essentials dans la section [Composants](#components) ci-dessous.                                                                                                                                                                                                                                                                                                                                                                                         |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Pour le moment, seul Gmail fournit le support de la SAP pour le courrier électronique. [Inscrivez-vous avec Google ici](https://developers.google.com/gmail/ampemail/register).
{% endalert %}

### Activation du compte Gmail

Allez dans vos paramètres Gmail et sélectionnez `Activer le contenu dynamique`.

!\[Contenu dynamique\]\[1\]

## Utilisation de l'API

Vous pouvez utiliser AMP pour les e-mails en utilisant notre API. Lorsque vous utilisez l'un de nos [points de terminaison de messagerie]({{site.baseurl}}/api/endpoints/messaging/) pour envoyer un e-mail, ajoutez `amp_body` comme une spécification d'objet, comme indiqué ci-dessous.

### Spécification de l'objet de l'e-mail

```json
{
  "app_id": (requis, chaîne) voir App Identifier ci-dessus,
  "subject": (optionnel, chaîne),
  "from": (requis, adresse email valide au format "Nom affiché <email@address.com>"),
  "reply_to": (facultatif, adresse e-mail valide au format "email@adresse. om" - par défaut à la réponse par défaut de votre groupe d'applications si elle n'est pas définie),
  "plaintext_body": (optionnel, texte brut valide, par défaut pour générer automatiquement le texte brut à partir de "body" lorsque ce n'est pas défini),
  "amp_body": (optionnel, met à jour le text-amp-html type MIME) le corps de l'e-mail en AMPHTML. Le type MIME (Multipurpose Internet Mail Extensions) à référencer est "text/x-amp-html".
  "body": (requis sauf si email_template_id est fourni, HTML valide),
  "preheader": (optionnel*, chaîne) Longueur recommandée de 50-100 caractères.
  "email_template_id": (optionnel, chaîne) Si fourni, nous utiliserons les valeurs objet/body/should_inline_css du modèle d'email donné UNIQUEMENT elles sont spécifiées ici, auquel cas nous remplacerons le modèle fourni,
  "message_variation_id": (optionnel, string) utilisée lors de la fourniture d'un campaign_id pour spécifier la variation de message sous laquelle ce message doit être suivi,
  "extras": (optionnel, valeur de la clé hachée), hash supplémentaire - pour les clients de SendGrid, ceci sera passé à SendGrid en tant qu'Arguments Uniques,
  "en-têtes": (optionnel, hachage Key-Value valide), hachage des en-têtes d'extensions personnalisées. Actuellement, uniquement pris en charge par les clients de SendGrid,
  "should_inline_css": (optionnel, booléen), si vous voulez inline css sur le corps. S'il n'est pas fourni, retourne à la valeur d'inline css par défaut pour le groupe d'applications,
  "pièces jointes": (facultatif, tableau), tableau d'objets json comme [{"file_name","url"}] qui définissent les fichiers dont vous avez besoin. L'extension de votre nom de fichier sera automatiquement détectée à partir de l'URL, qui devrait retourner le `Content-Type` approprié en tant qu'en-tête de réponse,
}
```

## Écriture de votre e-mail AMP

Construisez votre e-mail AMP en utilisant les [composants](#components) ci-dessous, puis utilisez [notre API](#api-usage) pour envoyer. Assurez-vous d'utiliser `amp_body` pour votre AMP HTML ! Vous pouvez également consulter le tutoriel [AMP](https://amp.dev/documentation/guides-and-tutorials/start/create_email?format=email) ou [exemple de code](https://gist.github.com/CrystalOnScript/988c3f0a2eb406da27e9d9bf13a8bf73) pour voir à quoi devrait ressembler le produit final. Vous pouvez également extraire la bibliothèque de composants de messagerie complète [d'AMP ici](https://amp.dev/documentation/components/?format=email/).

Lorsque vous écrivez votre email pour notre API, nous __avons besoin__ d'une version normale `HTML` et suggérons une version `plaintext_body` de votre e-mail AMP dans le cas où votre courriel est envoyé par l'intermédiaire d'un fournisseur qui ne supporte pas encore la SAP pour le courrier électronique.

### Composants

{% tabs %}
  {% tab Essentials %}

Voici ce qui fait un e-mail AMPHTML... AMP'ed! Chacun de ces éléments est requis dans le corps de votre courriel de SAP.

| Composant                                           | Ce que ça fait                                                                                                                                                                                                                                                   | Exemple                                                                             |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Identification <br> `⚡4email` or `amp4email`  | Identifie votre e-mail en tant qu'e-mail AMPHTML.                                                                                                                                                                                                                | `<!doctype html>` <br> `<html ⚡4email>` <br> `<head>` |
| Charger l'exécution AMP <br> `<script>` | Permet à AMP de s'amuser dans votre email en utilisant JavaScript.                                                                                                                                                                                               | `<script async src="https://cdn.ampproject.org/v0.js"></script>`        |
| CSS Boilerplate                                     | Masque le contenu jusqu'à ce que AMP soit chargé. <br> Fournisseurs de messagerie qui prennent en charge les courriels AMP imposent des vérifications de sécurité féroces qui permettent uniquement aux scripts AMP vérifiés d'exécuter dans leurs clients | `<style amp4email-boilerplate>corps{visibility:hidden}</style>`         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

  {% endtab %}
  {% tab Dynamic %}

Vous voulez voir quelque chose de cool? Oh attendez - c'est votre email. Utilisez ces composants pour créer des mises en page et des comportements dynamiques dans vos e-mails.

| Composant                                                                                                   | Ce que ça fait                                                                                                  | Script requis                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| [Accordéon](https://amp.dev/documentation/components/amp-accordion?format=email) <br> `amp-accordéon` | Permet à vos utilisateurs de jeter un coup d'œil au contour du contenu et de sauter à n'importe quelle section. | `<script async custom-element="amp-accordion" src="https://cdn.ampproject.org/v0/amp-accordion-0.1.js"></script>` |
| [Formulaires](https://amp.dev/documentation/components/amp-form?format=email) <br> `ample-forme`      | Créez des formulaires pour soumettre des champs de saisie dans un document SAP.                                 | `<script async custom-element="amp-form" src="https://cdn.ampproject.org/v0/amp-form-0.1.js"></script>`           |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
N'importe quel composant qui nécessite une authentification de l'utilisateur doit utiliser [Google Access Tokens](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) ou [Jetons d'Assertion de Proxy](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}
  {% endtab %}
  {% tab Creative %}

  Appréciez les composants de l'AMP qui vous aident à mieux répondre à vos attentes.

| Composant                                                                                                | Ce que ça fait                                                                                                                                                                                                | Script requis                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Image animée](https://amp.dev/documentation/components/amp-anim?format=email) <br> `amp-anim`     | Afficher une image animée (généralement un GIF) gérée via l'exécution.                                                                                                                                        | `<script async custom-element="amp-anim" src="https://cdn.ampproject.org/v0/amp-anim-0.1.js"></script>`                                                                              |
| [Carousel](https://amp.dev/documentation/components/amp-carousel?format=email) <br> `amp-carousel` | Affiche plusieurs éléments de contenu similaires le long d'un axe horizontal.                                                                                                                                 | `<script async custom-element="amp-carousel" src="https://cdn.ampproject.org/v0/amp-carousel-0.1.js"></script>`                                                                      |
| [Image](https://amp.dev/documentation/components/amp-img?format=email)                                   | Un remplacement géré en runtime pour la balise HTML `img`. <br>  Vous pouvez également créer une lightbox [pour votre image](https://amp.dev/documentation/components/amp-image-lightbox?format=email). | `<amp-img alt="A view of the sea"` <br> `src="images/sea.jpg"` <br> `width="900"` <br>  `height="675"` <br>  `layout="responsive">`  <br> `</amp-img>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
N'importe quel composant qui nécessite une authentification de l'utilisateur doit utiliser [Google Access Tokens](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) ou [Jetons d'Assertion de Proxy](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}

  {% endtab %}
  {% tab Other %}

  Il y a plus de choses dans le monde que ces autres onglets. Voici quelques autres composants amusants que vous devriez vérifier.

| Composant                                                                                                                        | Ce que ça fait                                                                                                   |
| -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| [Liaison de données & Expressions](https://amp.dev/documentation/components/amp-anim?format=email) <br> `Lier à l'ampoule` | Ajoute une interactivité étatique personnalisée à vos pages AMP via la liaison de données et les expressions JS. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
N'importe quel composant qui nécessite une authentification de l'utilisateur doit utiliser [Google Access Tokens](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) ou [Jetons d'Assertion de Proxy](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens).
{% endalert %}

  {% endtab %}
{% endtabs %}

### Utiliser amp-moustache

Similaire à Liquid, AMP prend en charge un langage de script pour des cas d'utilisation plus avancés.  Ce composant est appelé [amp-mustache](https://amp.dev/documentation/components/amp-mustache/?format=email).  En incluant n'importe quel langage de balisage de Mustache, vous devrez l'envelopper autour de la balise [brute](https://shopify.github.io/liquid/tags/raw/) de Liquid.  Malheureusement Liquid (le langage de balisage utilisé ici au Brésil) et Mustache partagent le style de syntaxe.

En enveloppant votre contenu autour de la balise brute, le moteur de traitement de Braze ignorera correctement tout contenu entre les balises brutes et enverra la variable Mustache dont votre équipe a besoin.


### Métriques et analyses

| Métrique              | Détails du produit                                                                                                                        |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Ouvertures totales    | Total s'ouvre pour les versions HTML et texte de votre courriel AMP.                                                                      |
| Nombre total de clics | Total des clics dans les versions HTML et texte de votre courriel AMP.                                                                    |
| Ouverture de l'AMP    | Le nombre total d'ouvertures dans votre courriel HTML AMP, le nombre cumulatif de versions HTML, en texte brut et en AMPHTML du courriel. |
| Clics AMP             | Le nombre total de clics dans votre courriel AMP HTML, le nombre cumulatif de versions HTML, en texte brut et en AMPHTML du courriel.     |
{: .reset-td-br-1 .reset-td-br-2}

- Veuillez noter que le total des clics et des clics uniques ne tiennent compte d'aucun clic qui s'est produit à partir d'un message AMP (HTML et texte brut seulement). Les clics spécifiques à AMP sont attribués à la métrique `amp_click`.

### Test & Dépannage

Avant d'envoyer votre e-mail AMP, nous vous recommandons de tester selon les directives de [Gmail ici](https://developers.google.com/gmail/ampemail/testing-dynamic-email).

Pour que votre courriel AMP soit envoyé à n'importe quel compte Gmail, le courriel doit remplir les conditions suivantes :
- Les SAP pour les exigences en matière de sécurité des courriels doivent être respectées (voir le tableau ci-dessus).
- La partie AMP MIME doit contenir un document AMP valide.
- Le courriel doit inclure la partie AMP MIME avant la partie HTML MIME.
- La partie AMP MIME doit être inférieure à 100KB.

Si aucune de ces conditions ne provoque d'erreur, contactez [le support][support].

 [1]: {% image_buster /assets/img/dynamic-content.png %} "Contenu dynamique"

 [support]: {{site.baseurl}}/support_contact/
