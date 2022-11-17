---
nav_title: Création d’un message In-App
article_title: Création d’un message In-App
page_order: 0
description: "Vous pouvez créer un message In-App à l’aide de la plateforme Braze par le biais de campagnes, de Canvas ou d’une campagne API. Le présent article vous guidera dans ce processus."
channel:
  - messages In-App
tool:
  - Campagnes

---

# Création d’un message In-App

> Le présent article explique comment créer un message dans l’application Braze. Nous allons voir ici comment composer votre message, styliser son contenu et planifier son envoi.

Vous pouvez créer un message In-App ou dans le navigateur en utilisant la plateforme Braze par le biais de campagnes, de Canvas ou d’une campagne API. Nous vous recommandons vivement de planifier vos messages et de préparer tout le matériel à l’avance en suivant notre [guide pratique de préparation des messages In-App]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/).

## Étape 1 : Choisir où créer votre message {#create-new-campaign-in-app}

Vous ne savez pas si votre message doit être envoyé à l’aide d’une campagne ou d’un Canvas ? Les campagnes sont préférables pour des messages simples, tandis que les Canvas se prêtent davantage aux expériences utilisateur en plusieurs étapes.

{% tabs %}
{% tab Campaign %}

**Étapes :**

1. Dans la page **Campaigns** (Campagnes), cliquez sur <i class="fas fa-plus"></i>Create Campaign** (Créer une campagne)**.
2. Sélectionner **In-App Message** (Message In-App). Notez que les messages In-App ne sont pas disponibles dans les campagnes multicanaux.
3. Nommez votre campagne de manière claire et pertinente.
4. Ajouter des [teams]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/) et des [balises]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/) si nécessaire.
   * Les balises facilitent la recherche et la création de rapports. Par exemple, lorsque vous utilisez le [créateur de rapports]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/report_builder/), vous pouvez filtrer des éléments par balises spécifiques.
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Vous pouvez le choix de plateformes, de types de messages et de mises en page pour chaque variante ajoutée. Pour plus d’informations sur cette rubrique, consultez [Tests A/B et multivariés]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Si tous les messages de votre campagne vont être similaires ou avoir le même contenu, composez votre message avant d’ajouter d’autres variantes. Vous pouvez ensuite choisir **Copy from Variant** (Copier à partir de la variante) dans le menu déroulant **Add Variant** (Ajouter une variante).
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Étapes :**

1. [Créez votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) à l’aide de l’assistant Canvas.
2. Après avoir configuré votre Canvas, ajoutez une étape dans le créateur de Canvas. Nommez votre étape de manière claire et pertinente.
3. Choisissez une [planification des étapes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) et indiquez un délai si besoin est. Notez que les étapes contenant des messages dans l’application ne peuvent pas être basées sur des actions.
4. Filtrez votre public pour cette étape si nécessaire. Vous pouvez affiner davantage les destinataires de cette étape en spécifiant des segments et en ajoutant plus de filtres. Les options de public sont vérifiées après le délai, au moment où les messages sont envoyés.
5. Choisissez votre [comportement d’avancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Choisissez les autres canaux de messagerie que vous souhaitez associer à votre message.

{% alert important %}
Vous ne pouvez pas avoir plusieurs variantes de messages In-App dans une même étape.
{% endalert %}

Vous pouvez trouver plus d’informations spécifiques à Canvas dans [Messages In-App dans Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/).

{% endtab %}
{% endtabs %}

## Étape 2 : Spécifier les plateformes de livraison

Commencez par choisir les plateformes devant recevoir le message. Cette sélection vous permet de limiter la livraison d’une campagne à un ensemble spécifique d’applications. Vous pouvez par exemple choisir **Web Browsers** (Navigateurs Web) pour un message en ligne encourageant les utilisateurs à télécharger votre application mobile, afin de vous assurer qu’ils ne reçoivent pas le message une fois l’application obtenue. Les sélections de plateforme étant spécifiques à chaque variante, vous pouvez tester l’engagement des messages par plateforme.

| Plateforme | Livraison des messages |
|---|---|
| Applications mobiles | SDK iOS et Android|
| Navigateurs Web | SDK Web|
| Applications mobiles et navigateurs Web | SDK iOS, Android et Web|
{: .reset-td-br-1 .reset-td-br-2}

## Étape 3 : Spécifier vos types de messages

Une fois que vous avez sélectionné une plateforme d’envoi, parcourez les types de messages, les mises en page et autres options associées. Découvrez-en plus sur le comportement et l’apparence que chacun de ces messages doit avoir dans notre page [Détails créatifs]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/), ou cliquez sur les types de messages liés dans les tableaux suivants.

Lorsque vous décidez quel type de message utiliser, vous devez réfléchir au degré d’intrusion que votre campagne de messages In-App doit avoir. Il s’agit d’évaluer la place que le message va occuper dans l’écran et l’interruption qu’il supposera pour l’expérience normale de votre client dans votre application ou votre site. Plus vous voulez fournir de contenu riche, plus votre message doit être intrusif.

![Graphique montrant une échelle du moins instrusif au plus intrusif, le moins intrusif étant avec le curseur, suivi de modal, le plein écran étant le plus intrusif]({% image_buster /assets/img_archive/iam_intrusive.png %}){: style="max-width:80%" }

### Types de messages

Ces messages In-App sont acceptés par les applications mobiles et les applications Web.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table class="tg">
<thead>
  <tr>
    <th>Type de message</th>
    <th>Description du type</th>
    <th>Dispositions disponibles</th>
    <th>Autres actions</th>
    <th>Utilisation recommandée</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen'>Plein écran</a></td>
    <td>Messages occupant tout l’écran avec un bloc de texte.</td>
    <td>
      <ul>
      <li>Image et texte</li>
      <li>Image uniquement</li>
      </ul>
    </td>
    <td>Orientation de l’appareil appliquée (portrait ou paysage)</td>
    <td>Grand et en gras ! À utiliser pour vous assurer que les utilisateurs voient votre contenu, comme vos campagnes clés, des notifications importantes ou des promotions massives.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/modal'>Modal</a></td>
    <td>Messages occupant tout l’écran entier avec une incrustation et un bloc de texte.</td>
    <td>
      <ul>
      <li>Texte (avec image facultative)</li>
      <li>Image uniquement</li>
      </ul>
    </td>
    <td>N/A</td>
    <td>Un bon juste milieu. À utiliser lorsque vous avez besoin d’une façon apparente d’attirer l’attention de vos utilisateurs, par exemple pour essayer une nouvelle fonctionnalité ou profiter d’une promotion.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup'>Slideup</a></td>
    <td>Messages qui glissent à un endroit concret sans bloquer le reste de l’écran.</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>Discret car il occupe un espace minimal à l’écran. À utiliser pour avertir les utilisateurs d’extraits de code d’informations, comme de nouvelles fonctionnalités, des annonces, l’utilisation de cookies, etc.<br></td>
  </tr>
</tbody>
</table>

### Types de messages avancés

Ces messages In-App sont personnalisables selon vos besoins.

<table class="tg">
<thead>
  <tr>
    <th>Type de message</th>
    <th>Description du type</th>
    <th>Dispositions disponibles</th>
    <th>Exigences</th>
    <th>Utilisation recommandée</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages'>Message HTML personnalisé</a></td>
    <td>Messages personnalisés qui s’affichent comme défini dans votre code personnalisé (HTML, CSS et/ou Javascript).</td>
    <td>N/A</td>
    <td>L’option d’initialisation <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> doit être définie à <code>true</code> pour que votre message In-App fonctionne.</td>
    <td>Une option utile pour bénéficier de tous les avantages des messages In-App si vous avez aussi besoin d’autres fonctionnalités ou que l’apparence doit rester cohérente. Vous pouvez modifier chaque détail du message : police, couleur, forme, taille, boutons, etc. <br><br>Exemples de cas d’utilisation : demander aux utilisateurs des commentaires sur l’application, des formulaires de capture d’e-mail ou des messages paginés</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#email-capture-form'>Formulaire de capture d’e-mail</a></td>
    <td>Généralement utilisé pour obtenir l’e-mail d’un visiteur.</td>
    <td>N/A</td>
    <td>L’option d’initialisation <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> doit être définie à <code>true</code> pour que votre message In-App fonctionne.</td>
    <td>Il consiste à demander aux utilisateurs de soumettre leur adresse e-mail.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css'>Modal Web avec CSS</a></td>
    <td>Messages modaux pour le Web avec CSS personnalisable.</td>
    <td>
      <ul>
      <li>Texte (avec image facultative)</li>
      <li>Image uniquement</li>
      </ul>
    </td>
    <td>Un modal Web avec CSS est unique au SDK Web et peut uniquement être utilisé après avoir sélectionné <b>Navigateurs Web</b>.</td>
    <td>À utiliser lorsque vous voulez télécharger ou écrire un CSS personnalisé pour créer une élégante messagerie personnalisée. </td>
  </tr>
</tbody>
</table>

{% alert important %}
Si Braze détecte que vous n’avez pas de bouton de fermeture dans votre code, nous vous demanderons d’en ajouter un. Pour votre commodité, nous fournissons un extrait de code que vous pouvez copier et coller dans votre code : <br><br>`<a href= "appboy://close">X</a>`.
{% endalert %}

## Étape 4 : Composer votre message In-App

L’onglet **Compose** (Composer) vous permet de modifier tous les aspects du contenu et du comportement de votre message.

![][24]{: style="max-width:85%" }

Le contenu de l’onglet **Compose** (Composer) varie en fonction des options de message choisies à l’étape précédente, mais peut inclure l’une des options suivantes :

#### Langue

Cliquez sur **Add Languages** (Ajouter des langues) et sélectionnez les langues souhaitées dans la liste fournie. [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) sera alors inséré dans votre message. Nous vous recommandons de sélectionner vos langues avant d’écrire votre contenu afin que vous puissiez remplir votre texte dans Liquid. Voir notre [liste complète des langues disponibles][18].

#### Image

Selon votre type de message, vous pouvez **télécharger une image**, **choisir un badge** ou utiliser **Font Awesome**. Pour télécharger une image, cliquez sur **Add Image** (Ajouter une image) ou entrez une URL d’image. Cliquer sur **Add Image** (Ajouter une image) ouvre la **médiathèque**, où vous pouvez sélectionner une image précédemment téléchargée ou en ajouter une nouvelle. Chaque type de message et chaque plateforme peuvent avoir des proportions et des exigences propres ; veillez à en prendre connaissance avant de demander ou de créer une image de zéro.

#### En-tête et corps

Écrivez ce que bon vous semble ! Incluez un texte entièrement personnalisé (souvent avec des fonctionnalités HTML personnalisées) à l’aide des options pour inclure [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) et d’autres types de personnalisation. Plus vite votre message est diffusé et votre client clique, mieux c’est ! Nous recommandons des en-têtes et un contenu de message clairs et concis.

Certains types de messages ne requièrent pas et ne demandent donc pas d’en-têtes.

{% alert tip %}
Besoin d’aide pour créer un texte d’exception ? Essayez d’utiliser l’[assistant de rédaction IA]({{site.baseurl}}/user_guide/intelligence/ai_copywriting/). Saisissez un nom ou une description de produit : telle une personne, l’IA génère un texte marketing utilisable dans votre messagerie.

![Bouton Launch AI Copywriter (Lancer l’IA de rédaction) situé dans le champ Message du composeur de messages In-App.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_iam.png %}){: style="max-width:60%"}
{% endalert %}

#### Texte du bouton {#buttons}

Lorsque le type de message est disponible, jusqu’à deux boutons peuvent apparaître sous le corps du texte. Vous pouvez créer et modifier le texte et la couleur du bouton personnalisé. Vous pouvez également ajouter un lien aux conditions de service dans les formulaires de capture d’e-mail.

![Boutons principaux et secondaires dans un message In-App]({% image_buster /assets/img/primary-secondary-buttons.png %}){: style="float:right;margin-left:15px;height:30%;width:30%"}

Si vous choisissez d’utiliser un seul bouton, il s’ajuste automatiquement pour occuper l’espace disponible au bas de votre message au lieu de laisser de la place pour un autre bouton.

##### Choisir un bouton principal

Si vous décidez d’appliquer vos couleurs à ces boutons, nous vous recommandons d’utiliser le bouton 2 pour votre résultat préféré. En d’autres termes, si vous souhaitez que votre utilisateur clique sur un bouton plus que l’autre, assurez-vous qu’il se trouve sur la droite. Les clics s’avèrent plus fréquents sur le bouton de droite, notamment s’il a a une couleur légèrement contrastée ou tranchant par rapport au reste du message. Ce cas ne se vérifie que si le bouton sur la gauche se fond davantage dans le message.

#### Comportement en cas de clic {#button-actions}

Lorsque votre client clique sur un bouton dans votre message In-App, les actions suivantes sont disponibles. 

| Action | Description |
|---|---|
| Rediriger vers une URL Web | Ouvrir une page Web non native. |
| [Lien profond dans l’application]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content) | Lien profond vers un écran existant dans votre application. |
| Fermer le message | Ferme le message actuellement actif. |
| Consigner un événement personnalisé | Choisissez un [événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) à déclencher. Utilisable pour afficher un autre message In-App ou déclencher d’autres messages. |
| Consigner un attribut personnalisé | Choisissez un [attribut personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) pour l’utilisateur actuel. |
| Demander l’autorisation pour les notifications push | Affiche l’autorisation native pour les notifications push. En savoir plus sur les [meilleures pratiques]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/creating_custom_opt-in_prompts/) pour les utilisateurs d’amorçage de notification push. |
{: .reset-td-br-1 .reset-td-br-2}

Note: Les options  __Request Push Permission__ (Demander l’autorisation pour les notifications push), __Log Custom Event__ (Consigner un événement personnalisé) et  __Log Custom Attribute__  (Consigner un attribut personnalisé) nécessitent les versions minimum suivantes du SDK :

{% sdk_min_versions ios:5.1.0 android:21.0.0 web:4.0.3 %}

#### Options d’appareil iOS

Vous avez la possibilité de restreindre l’envoi de vos messages In-App à des appareils iOS. Pour ce faire, cliquez sur **Change** (Changer) et sélectionnez **Only send to iOS devices** (Envoyer uniquement aux appareils iOS).

#### Fermeture du message

Choisissez entre les options suivantes :
 
- **Dismiss automatically (Rejeter automatiquement) :** Sélectionnez le nombre de secondes que le message reste à l’écran.
- **Wait for User Swipe or Touch (Attendre que l’utilisateur glisse ou touche) :** Nécessite une option de rejet ou de fermeture.

#### Position de slideup

Ce paramètre s’applique uniquement au type de message slideup. Choisissez entre faire apparaître votre slideup **depuis le bas de l’écran de l’application** ou **depuis le haut de l’écran de l’application**.

#### HTML et ressources

Ce paramètre s’applique uniquement au type de message personnalisé. Copiez et collez le code HTML dans l’espace disponible et chargez vos ressources via ZIP.

#### Marque substitutive d’entrée de capture d’e-mail

Ce paramètre s’applique uniquement au type de message de formulaire de capture d’e-mail. Saisissez un texte personnalisé qui apparaîtra comme marque substitutive pour le champ d’entrée d’e-mail. Par défaut s’affiche le message « Enter your email address » (Saisissez votre adresse e-mail).

### Générations

Braze dispose de trois générations de messages In-App disponibles. Vous pouvez affiner les appareils auxquels vos messages doivent être envoyés, selon la génération qu’ils prennent en charge, dans la section d’[aperçu]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) lors de la composition de votre message In-App.

![Bascule entre des générations de messages In-App dans la section d’aperçu][2]{: height="50%" width="50%"}

En fonction des versions de SDK que vos utilisateurs emploient, cette option est ou non visible. Vous devez seulement sélectionner une génération lorsque vous avez des utilisateurs sur plusieurs générations.

{% details What is a generation? %}
Une génération correspond à une collection de versions de SDK qui contiennent un grand nombre d’importantes mises à niveau. Par exemple, la génération 3 est la dernière à inclure les plus récentes mises à jour de style.

En sélectionnant **Send to all Generations that support this message** (Envoyer à toutes les générations qui prennent en charge ce message), Braze livre les utilisateurs pouvant recevoir toute forme du message. Par exemple, si vous avez des utilisateurs sur les trois générations, un modal est livré aux utilisateurs sur les générations 2 et 3, car la génération 1 ne prend pas en charge les modaux. Le message est différent pour les deux groupes d’utilisateurs : Les utilisateurs de la génération 3 reçoivent le message dans les styles les plus récents, tandis que ceux de la génération 2 voient des styles plus anciens (différences cosmétiques et absence de bordure du bouton).

Vous pouvez décocher la case **Send to all Generations that support this message** (Envoyer à toutes les générations qui prennent en charge ce message) et sélectionner **Send only to users on Generation 3 (the latest)** (Envoyer uniquement aux utilisateurs sur la génération 3 (la plus récente) si vous ne souhaitez pas autoriser les utilisateurs à recevoir les styles de message plus anciens. Les utilisateurs de la génération 3 seront les seuls à recevoir le message.
{% enddetails %}

## Étape 5 : Styliser votre message In-App

L’onglet **Style** permet d’ajuster tous les aspects visuels de votre message. Téléchargez une image ou un badge, ou choisissez une icône de badge préconçue. Modifiez les couleurs de l’en-tête, du texte du corps, des boutons et de l’arrière-plan à l’aide d’une palette ou en saisissant un code hexadécimal, RVB ou HSB.

Le contenu de l’onglet **Style** varie en fonction des options de message choisies à l’étape précédente, mais peut inclure l’une des options suivantes :

| Formatage | Entrée | Description |
|---|---|---|
|Profil de couleur | Appliquer à partir de la galerie des modèles de messages In-App. | Cliquez sur **Apply Template** (Appliquer le modèle) et sélectionnez-le dans la galerie. Cliquez ensuite sur **Save** (Enregistrer). |
|Alignement du texte | Gauche, Centre ou Droite.  | Disponible uniquement pour les versions plus récentes du SDK Braze. |
|En-tête | Code de couleur HEX. | La couleur HEX souhaitée s’affiche. Vous pouvez également choisir l’opacité de la couleur.  |
|Texte | Code de couleur HEX. | La couleur HEX souhaitée s’affiche. Vous pouvez également choisir l’opacité de la couleur. |
|Boutons | Code de couleur HEX. | Les couleurs HEX souhaitées s’affichent. Vous pouvez également choisir l’opacité des couleurs. Vous pouvez choisir des couleurs pour l’arrière-plan du bouton de fermeture du message, ainsi que l’arrière-plan, le texte et la bordure de chaque bouton. |
| Bordure du bouton | Code de couleur HEX. | Nouveau ! Vous pouvez ainsi définir les boutons principaux et secondaires de façon indépendante. Nous suggérons de choisir pour le contour des boutons des couleurs contrastantes. |
|Couleur d’arrière-plan | Code de couleur HEX. | La couleur HEX souhaitée s’affiche. Vous pouvez également choisir l’opacité de la couleur. Il s’agit de l’arrière-plan du message entier qui s’affiche clairement derrière le corps de votre texte. |
|Incrustation à l’écran | Code de couleur HEX. | La couleur HEX souhaitée s’affiche. Vous pouvez également choisir l’opacité de la couleur. Disponible uniquement pour les versions plus récentes du SDK Braze. Il s’agit du cadre autour du message entier. |
|Chevron ou autre option de fermeture du message | Code de couleur HEX. | La couleur HEX souhaitée s’affiche. Vous pouvez également choisir l’opacité de la couleur. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

[Affichez l’aperçu et testez]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) toujours votre message avant de l’envoyer.

{% alert important %}
La stylisation de certains types de messages In-App n’est pas possible au-delà du téléchargement de HTML personnalisé (ou CSS ou Javascript) et de ressources via un ZIP. [Web Modal with CSS]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css) (Modal Web avec CSS) vous permet de télécharger ou d’écrire un CSS personnalisé pour créer d’élégants messages personnalisés.
{% endalert %}

## Étape 6 : Configurer des paramètres supplémentaires (facultatif)

### Paires clé-valeur

Vous pouvez ajouter des [paires clé-valeur][19] pour envoyer d’autres champs personnalisés aux appareils utilisateur.

## Étape 7 : Créer le reste de votre campagne ou Canvas

{% tabs %}
{% tab Campaign %}

Élaborez le reste de votre campagne ; consultez les sections suivantes pour obtenir des conseils supplémentaires sur le meilleur usage de nos outils afin de créer des messages In-App.

#### Choisir un déclencheur

Sélectionnez l’action à partir de laquelle votre message doit être déclenché, ainsi que les heures de début et de fin pour votre campagne ou Canvas.

{% alert important %}
Notez que si vous souhaitez déclencher votre message In-App à partir d’un événement personnalisé, ce dernier doit être envoyé via le SDK.
{% endalert %}

![Campagne basée sur l’action, avec l’action de déclenchement définie à « Start Session » (Démarrer la session).]({% image_buster /assets/img_archive/in_app_schedule.png %}){: style="max-width:80%"}

La livraison des messages In-App est entièrement basée sur les déclencheurs d’action suivants :

- Faire un achat
- Ouvrir l’application/la page Web
- Réaliser un événement personnalisé (fonctionne uniquement avec les événements envoyés via le SDK)
- Ouvrir un message de notification push spécifique
- Planifiez automatiquement les campagnes pour des envois à des moments précis en fonction de l’heure locale de chacun de vos utilisateurs.
- Les messages peuvent également être configurés pour une récurrence quotidienne, hebdomadaire (éventuellement à des jours spécifiques) ou mensuelle.

Une date et une heure de début doivent être sélectionnées, mais une date de fin est facultative. Une date de fin empêche ce message In-App spécifique de s’afficher sur les appareils après la date et l’heure indiquées.

Reportez-vous à notre documentation pour développeurs concernant le [déclenchement d’événements côté serveur]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/) et la [livraison de messages In-App locaux]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#local-in-app-messages).

##### Déclenchement en ligne ou hors ligne

Les messages In-App fonctionnent par l’envoi du message et de déclencheurs à l’appareil de l’utilisateur. Une fois les messages In-App sur un appareil, ils attendent pour s’afficher que la condition de déclenchement soit remplie. Si les messages In-App sont déjà mis en cache sur l’appareil de l’utilisateur, vous pouvez même les déclencher hors ligne sans connexion à Braze (par exemple, en mode Avion).

{% alert important %}
Une fois qu’une campagne de messages In-App a été interrompue, certains utilisateurs peuvent avoir reçu le message sans le voir car ils n’ont pas ouvert votre application. Ces utilisateurs voient toujours votre message In-App et sont comptabilisés comme impression unique, même après l’arrêt de votre campagne.
{% endalert %}

#### Choisir une priorité

Enfin, une fois sélectionnée l’action à partir de laquelle le message In-App est déclenché, vous devez également définir une priorité. Si deux messages sont déclenchés depuis la même action, les messages de priorité élevée sont planifiés pour s’afficher sur les appareils des utilisateurs avant ceux moins prioritaires. 

Vous pouvez choisir entre les priorités de message suivantes :

- Priorité faible (affiché après d’autres messages)
- Priorité moyenne
- Priorité élevée (affiché avant d’autres messages)

Les options de priorité faible, moyenne et élevée pour les messages déclenchés sont des compartiments, et des messages multiples peuvent avoir la même priorité sélectionnée. Pour définir des priorités dans ces compartiments, cliquez sur **Set Exact Priority** (Définir la priorité exacte) afin de glisser-déposer des campagnes pour les classer avec la priorité correcte.

![]({% image_buster /assets/img_archive/bucket_prioritization.png %}){: style="max-width:70%"}

#### Choisir les utilisateurs à cibler

Ensuite, vous devez [cibler des utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) en choisissant des segments ou des filtres pour limiter votre public. Vous recevez automatiquement un aperçu de ce à quoi ressemble la population approximative du segment à ce moment-là. Gardez à l’esprit que l’appartenance à un segment exact est toujours calculée juste avant l’envoi du message.

{% alert note %} 
En cas de retard à l’étape de message In-App, l’appartenance à un segment est évaluée après le délai. Si l’utilisateur est éligible, le message In-App se synchronise lors de la prochaine session disponible.
{% endalert %}

##### Réévaluer l’éligibilité de la campagne et de Liquid

Dans certains scénarios, vous voulez éventuellement réévaluer l’éligibilité d’un utilisateur lorsqu’il déclenche un message In-App à afficher. Les exemples incluent des campagnes qui ciblent un attribut personnalisé amené à changer fréquemment, ou des messages devant refléter les changements de profil de dernière minute.

![Section Sommaire du public de l’étape Utilisateurs cibles avec l’option « Re-evaluate campaign elegibility before displaying » (Réévaluer l’éligibilité de la campagne avant l’affichage) sélectionnée.]({% image_buster /assets/img_archive/re-evaluate-iam-membership.png %})

Lorsque vous sélectionnez **Re-evaluate campaign elegibility before displaying** (Réévaluer l’éligibilité de la campagne avant d’afficher), une nouvelle demande de Braze a lieu pour confirmer que l’utilisateur est toujours éligible pour ce message avant l’envoi. En outre, toutes les variables [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) ou tout [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) sont mis en place à ce moment avant l’affichage du message.

{% alert note %}
L’activation de cette option entraîne un léger retard (< 100 ms) entre le déclenchement d’un message In-App et son affichage en raison de la demande ajoutée d’éligibilité et de mise en place.
<br><br>
N’utilisez pas cette option pour les messages qui peuvent être déclenchés lorsqu’un utilisateur est hors ligne ou lorsque l’éligibilité et la réévaluation de Liquid ne sont pas requises.
{% endalert %}

#### Choisir des événements de conversion

Braze vous permet de suivre à quelle fréquence les utilisateurs effectuent des actions spécifiques, des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/), après avoir reçu une campagne. Vous avez la possibilité d’autoriser jusqu’à 30 jours pour qu’une conversion soit comptabilisée si l’utilisateur effectue l’action spécifiée.

{% endtab %}
{% tab Canvas %}

Si vous ne l’avez pas déjà fait, complétez les sections restantes de votre Canvas Step. Pour plus d’informations sur la création du reste de votre Canvas, la mise en œuvre d’un test multivarié et d’une sélection intelligente, reportez-vous à l’étape [Construire votre Canvas Step]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de notre documentation Canvas.

Pour plus d’informations sur les options de messagerie In-App spécifique à Canvas, reportez-vous à [Messages In-App dans Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/).

{% endtab %}
{% endtabs %}

## Étape 8 : Examiner et déployer

Après avoir terminé votre campagne ou votre Canvas, consultez-en les détails, [faites un test]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) et procédez à son envoi.

Ensuite, consultez les [rapports sur les messages In-App]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/) pour découvrir comment accéder aux résultats de vos campagnes de messagerie.

## Aspects à connaître

### Limites de campagnes actives de messages In-App

Braze accorde de l’importance à la fiabilité et à la vitesse. Tout comme nous vous suggérons d’envoyer uniquement les données dont vous avez besoin à Braze, nous vous recommandons de désactiver les campagnes qui n’ajoutent plus de valeur à votre marque.

Le traitement des campagnes de messages In-App, qui sont toujours actives mais n’envoient plus de messages ou qui sont devenues inutiles, ralentit la performance globale des services de Braze pour vous et d’autres clients. Ce temps supplémentaire nécessaire pour traiter ces nombreuses campagnes inactives ralentit l’affichage de tous les messages In-App sur les appareils de l’utilisateur final, ce qui affecte l’expérience de ce dernier.

Les campagnes actives de messages In-App basées sur l’action sont limitées à 200 par groupe d'apps afin d’optimiser la vitesse de livraison des messages et éviter les retards.

Cette limite de 200 inclut des campagnes actives de messages In-App qui n’ont pas encore atteint l’heure de fin et celles qui n’en possèdent pas. Les campagnes actives de messages In-App qui ont dépassé leur heure de fin ne sont pas comptabilisées. Le client Braze standard possédant un total de 26 campagnes actives simultanées, vous ne risquez pas d’être affecté par cette limitation.


[2]: {% image_buster /assets/img/iam-generations.gif %}
[16]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/
[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported
[19]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/
[24]: {% image_buster /assets/img_archive/iam_compose.png %}
[25]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[26]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/
[27]: {% image_buster /assets/img_archive/re-evaluate-iam-membership.png %}
