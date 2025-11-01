---
nav_title: Créer un message in-app
article_title: "Création d'un message in-app"
page_order: 1
description: "Cet article de référence explique comment créer un message in-app à l'aide de la plateforme Braze en utilisant des campagnes ou Canvas."
channel:
  - in-app messages
tool:
  - Campaigns
search_rank: 4.8
toc_headers: h2
---

# Créer un message in-app

> Vous pouvez créer un message in-app ou un message in-browser à l'aide de la plateforme Braze en utilisant des campagnes, Canvas, ou en tant que campagne API. Nous vous recommandons vivement de planifier vos messages et de préparer tous les documents à l'avance à l'aide de notre [guide]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/) pratique [de préparation des messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/).

## Étape 1 : Choisissez où créer votre message {#create-new-campaign-in-app}

Vous ne savez pas si votre message doit être envoyé par le biais d'une campagne ou d'un canvas ? Les campagnes sont plus adaptées aux campagnes d'envoi de messages simples et uniques, tandis que les Canevas sont plus adaptés aux parcours utilisateurs en plusieurs étapes.

{% tabs %}
{% tab Campaign %}

1. Allez dans **Messagerie** > **Campagnes** et sélectionnez **Créer une campagne.**
2. Sélectionnez **Message in-app.** Notez que les messages in-app ne sont pas disponibles dans les campagnes multicanales.
3. Donnez à votre campagne un nom clair et significatif.
4. Ajoutez des [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) et des [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) si nécessaire.
   * Les étiquettes facilitent la recherche de vos campagnes et permettent de créer des rapports. Par exemple, lorsque vous utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), vous pouvez filtrer par des étiquettes particulières.
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Vous pouvez choisir des plateformes, des types de messages et des mises en page différents pour chacune de vos variantes ajoutées. Pour en savoir plus sur ce sujet, reportez-vous aux [tests multivariés et aux tests A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Si tous les messages de votre campagne seront similaires ou auront le même contenu, composez votre message avant d'ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copier à partir de la variante** dans la liste déroulante **Ajouter une variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Créez votre canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) à l'aide du compositeur de canvas.
2. Après avoir configuré votre canvas, ajoutez une étape dans le générateur de canvas. Donnez à votre démarche un nom clair et significatif.
3. Choisissez une [planification des étapes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) et spécifiez un délai si nécessaire. Notez que les étapes contenant des messages in-app ne peuvent pas être basées sur des actions.
4. Filtrez votre audience pour cette étape, si nécessaire. Vous pouvez encore affiner les destinataires de cette étape en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options d'audience seront vérifiées après le délai, au moment de l'envoi des messages.
5. Choisissez votre [comportement en matière d'avancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Choisissez les autres canaux de communication que vous souhaitez associer à votre message.

{% alert important %}
Vous ne pouvez pas avoir plusieurs variantes de messages in-app en une seule étape.
{% endalert %}

Vous trouverez davantage d'informations spécifiques à Canvas dans les [messages in-app dans Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/).

{% endtab %}
{% endtabs %}

## Étape 2 : Spécifier les plateformes de réception/distribution

Commencez par choisir les plateformes qui doivent recevoir le message. Utilisez cette sélection pour limiter la réception/distribution d'une campagne à un ensemble spécifique d'apps. Par exemple, vous pouvez choisir **Navigateurs web** pour un message dans le navigateur encourageant les utilisateurs à télécharger votre application mobile afin de vous assurer qu'ils ne reçoivent pas le message après avoir déjà obtenu votre application. Les sélections de plateformes étant spécifiques à chaque variante, vous pourriez essayer de tester l'engagement des messages par plateforme.

| Plateforme                        | Réception/distribution des messages        |
|---------------------------------|-------------------------|
| Applications mobiles                     | iOS & SDK Android      |
| Navigateurs web                    | SDK Web                 |
| Les deux applications mobiles & Navigateurs web | iOS, Android & Web SDKs |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Étape 3 : Spécifiez vos types de messages

Une fois que vous avez sélectionné une plate-forme d'envoi, parcourez les types de messages, les mises en page et les autres options qui y sont associées. Pour en savoir plus sur le comportement attendu et l'aspect de chacun de ces messages, consultez notre page [Détails créatifs]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/), ou cliquez sur les types de messages liés dans les tableaux suivants.

Lorsque vous décidez du type de message à utiliser, tenez compte de l'espace que votre message occupera et de l'effet perturbateur qu'il peut avoir sur l'expérience de l'utilisateur.

- Les messages **contextuels** sont les moins intrusifs, car ils apparaissent subtilement sans bloquer le contenu.
- Les messages **modaux** se situent au milieu, suffisamment présents pour attirer l'attention sans envahir l'écran.
- Les messages **en plein écran** sont ceux qui attirent le plus l'attention et qui conviennent le mieux aux annonces ou aux promotions importantes.

Plus votre contenu est complexe, plus vous aurez besoin d'espace et plus votre message risque d'interrompre le flux de l'utilisateur.

### Types de messages

Ces messages in-app sont acceptés aussi bien par les applications mobiles que par les applications web.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table class="tg">
<thead>
  <tr>
    <th>Type de message</th>
    <th>Type Description</th>
    <th>Modèles disponibles</th>
    <th>Autres options</th>
    <th>Utilisation recommandée</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen'>Plein écran</a></td>
    <td>Les messages qui couvrent l'ensemble de l'écran avec un bloc de messages.</td>
    <td>
      <ul>
      <li>Image et texte</li>
      <li>Image seulement</li>
      </ul>
    </td>
    <td>Orientation forcée de l'appareil (portrait ou paysage)</td>
    <td>Grandes et audacieuses ! À utiliser lorsque vous voulez vous assurer que les utilisateurs voient votre contenu, par exemple pour vos campagnes les plus critiques, vos notifications importantes ou vos promotions massives.<br><br>Notez que sur les appareils mobiles, les messages en mode portrait et paysage ne s'affichent pas si l'orientation de l'appareil ne correspond pas à celle du message.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/modal'>Fenêtre modale/boîte de dialogue modale, etc.</a></td>
    <td>Messages qui couvrent tout l'écran avec une superposition d'écran et un bloc de messages.</td>
    <td>
      <ul>
      <li>Texte (avec image optionnelle)</li>
      <li>Image seulement</li>
      </ul>
    </td>
    <td>N/A</td>
    <td>Un bon compromis. À utiliser lorsque vous avez besoin d'un moyen apparent d'attirer l'attention de vos utilisateurs, par exemple pour les encourager à essayer une nouvelle fonctionnalité ou à profiter d'une promotion.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup'>Contextuel</a></td>
    <td>Messages qui se glissent dans la vue à un endroit désigné sans bloquer le reste de l'écran.</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>Discret - occupe le moins d'espace possible sur l'écran. À utiliser pour avertir les utilisateurs de petits extraits de code, tels que les nouvelles fonctionnalités, les annonces, l'utilisation de cookies, etc.<br></td>
  </tr>
</tbody>
</table>

### Types d'envoi de messages avancés

Ces messages in-app sont personnalisables en fonction de vos besoins.

<table class="tg">
<thead>
  <tr>
    <th>Type de message</th>
    <th>Type Description</th>
    <th>Modèles disponibles</th>
    <th>Exigences</th>
    <th>Utilisation recommandée</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages'>Message HTML personnalisé</a></td>
    <td>Les messages personnalisés qui fonctionnent comme défini dans votre code personnalisé (HTML, CSS, et/ou JavaScript).</td>
    <td>N/A</td>
    <td>Vous devez définir <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> à <code>true</code> pour que votre message in-app fonctionne.</td>
    <td>Il s'agit d'une bonne option si vous souhaitez bénéficier de tous les avantages des IAM, mais que vous avez besoin de fonctionnalités supplémentaires ou que vous souhaitez que l'apparence reste "fidèle à la marque". Vous pouvez modifier chaque petit détail de l'envoi : police, couleur, forme, taille, boutons, etc. <br><br>Parmi les exemples de cas d'utilisation, citons les demandes de commentaires sur les applications, les formulaires de capture d'e-mails ou les messages paginés.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#email-capture-form'>Formulaire de capture d'e-mail</a></td>
    <td>Généralement utilisé pour capturer l'e-mail de l'internaute.</td>
    <td>N/A</td>
    <td>Vous devez définir <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> à <code>true</code> pour que votre message in-app fonctionne.</td>
    <td>Lorsque l'on demande aux utilisateurs d'indiquer leur adresse e-mail.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css'>Fenêtre modale/boîte de dialogue, etc.</a></td>
    <td>Messages modaux pour le web avec CSS personnalisable.</td>
    <td>
      <ul>
      <li>Texte (avec image optionnelle)</li>
      <li>Image seulement</li>
      </ul>
    </td>
    <td>La fenêtre modale/boîte de dialogue avec CSS est unique au SDK Web et ne peut être utilisée qu'après avoir sélectionné les <b>navigateurs web.</b></td>
    <td>Lorsque vous souhaitez télécharger ou écrire des CSS personnalisés pour créer de beaux messages au style personnalisé. </td>
  </tr>
</tbody>
</table>

{% alert important %}
Si Braze détecte que votre code ne comporte pas de bouton de fermeture ou de renvoi, nous vous demanderons d'en ajouter un. Pour vous faciliter la tâche, nous avons fourni un extrait de code que vous pouvez copier et coller dans votre code : <br><br>`<a href= "appboy://close">X</a>`.
{% endalert %}

## Étape 4 : Composez votre message in-app

L'onglet **Composer** vous permet de modifier tous les aspects du contenu et du comportement de votre message.

\![Exemple de message in-app d'une marque pour souhaiter la bienvenue à ses nouveaux clients et les inviter à créer un profil utilisateur.]({% image_buster /assets/img_archive/iam_compose.png %}){: style="max-width:85%" }

Le contenu de l'onglet **Composer** varie en fonction des options de message que vous avez choisies à l'étape précédente, mais peut inclure l'une des options suivantes :

### Langue

Sélectionnez **Ajouter des langues** et sélectionnez les langues souhaitées dans la liste proposée. Cela permettra d'insérer [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) dans votre message. Nous vous recommandons de sélectionner vos langues avant de rédiger votre contenu afin de pouvoir remplir votre texte à l'endroit voulu dans le Liquid. Consultez la [liste complète des langues disponibles]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

### Image

Selon le type de message, vous pouvez **télécharger une image**, **choisir un badge** ou utiliser **Font Awesome**. Pour télécharger une image, cliquez sur **Ajouter une image** ou indiquez l'URL de l'image. En cliquant sur **Ajouter une image**, vous ouvrez la **bibliothèque multimédia**, où vous pouvez sélectionner une image déjà téléchargée ou en ajouter une nouvelle. Chaque type de message et de plateforme peut avoir ses propres proportions et exigences - assurez-vous de les vérifier avant de commander ou de créer une image à partir de zéro !

### En-tête et corps

Écrivez ce que vous voulez ! Inclure un texte entièrement personnalisé (souvent avec des capacités HTML personnalisées) avec la possibilité d'inclure des [liquides]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) et d'autres types de personnalisation. Plus vite vous pouvez faire passer votre message et inciter votre client à cliquer, mieux c'est ! Nous vous recommandons d'utiliser des en-têtes et des messages clairs et concis.

Certains types de messages n'ont pas besoin d'en-têtes et n'en demandent donc pas.

#### Conseils 

##### Générer des copies d'intelligence artificielle

Vous avez besoin d'aide pour créer un texte percutant ? Essayez d'utiliser l'[assistant de rédaction de l'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Saisissez le nom ou la description d'un produit et l'intelligence artificielle générera un texte marketing de type humain à utiliser dans vos messages.

Lancez le bouton de l'intelligence artificielle Copywriter, situé dans le champ Message du compositeur de messages in-app.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_iam.png %}){: style="max-width:60%"}

##### Création d'envois de droite à gauche

Vous avez besoin d'aide pour rédiger des messages de droite à gauche dans des langues telles que l'arabe et l'hébreu ? Reportez-vous à la section [Créer des messages de droite à gauche]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) pour connaître les meilleures pratiques.

### Texte du bouton {#buttons}

Lorsqu'ils sont disponibles pour votre type de message, vous pouvez faire apparaître jusqu'à deux boutons sous votre corps de texte. Vous pouvez créer et modifier le texte et la couleur des boutons personnalisés. Vous pouvez également ajouter un lien vers les conditions de service dans les formulaires de capture d'e-mail.

Si vous choisissez de n'utiliser qu'un seul bouton, il s'ajustera automatiquement pour occuper l'espace disponible au bas de votre message au lieu de laisser de la place pour un bouton supplémentaire.

#### Choix d'un bouton principal

Si vous décidez de formater ces boutons avec vos propres couleurs, nous vous recommandons d'utiliser le bouton 2 pour obtenir le résultat que vous préférez.

En d'autres termes, si vous voulez que votre utilisateur clique sur un bouton plus que sur l'autre, assurez-vous qu'il se trouve à droite. Le bouton de droite a souvent plus de chances d'être cliqué, surtout s'il a une couleur quelque peu contrastée ou qui se démarque du reste du message. L'accent est mis sur le fait que le bouton de gauche se fond plus visuellement dans le message.

!boutons primaires et secondaires dans un message in-app]({% image_buster /assets/img/primary-secondary-buttons.png %})

### Comportement au clic {#button-actions}

Lorsque votre client clique sur un bouton dans votre message in-app, les actions suivantes sont disponibles. 

| Action | Description |
|---|---|
| Redirection vers l'URL | Ouvrez une page web non native. |
| [Lien profond dans l'application]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content) | Lien profond vers un écran existant dans votre application. |
| Fermer le message | Ferme le message en cours. |
| Enregistrer un événement personnalisé | Choisissez un [événement personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) à déclencher. Peut être utilisé pour afficher un autre message in-app ou déclencher un envoi de messages supplémentaires. |
| Attribut personnalisé du journal | Choisissez un [attribut personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) à définir pour l'utilisateur actuel. |
| Demander l'autorisation de pousser | Affiche l'autorisation native de pousser. En savoir plus sur l'[amorçage de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/), ainsi que sur les [meilleures pratiques]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#best-practices) pour amorcer les utilisateurs pour push. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Remarque : les options __Request Push Permission__, __Log Custom Event__ et __Log Custom Attribute__ nécessitent les versions minimales suivantes du SDK :

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

### Options pour les appareils iOS

Si vous le souhaitez, vous pouvez restreindre votre message in-app pour qu'il ne soit envoyé qu'aux appareils iOS. Pour ce faire, cliquez sur **Modifier** et sélectionnez **Envoyer uniquement aux appareils iOS**.

### Fermeture du message

Choisissez parmi les options suivantes :
 
- **Rejeter automatiquement :** Sélectionnez le nombre de secondes pendant lesquelles le message restera affiché à l'écran.
- **Attendez que l'utilisateur glisse ou touche :** Nécessite une option de licenciement ou de clôture.

### Position de glissement vers le haut

Ce paramètre ne s'applique qu'au type de message contextuel. Choisissez de faire apparaître votre contextuel **en bas** ou en **haut de l'écran de l'application**.

### HTML et ressources

Ce paramètre ne s'applique qu'au type de message Code personnalisé. Copiez et collez le code HTML dans l'espace disponible et téléchargez vos ressources à l'aide d'un fichier ZIP.

### Marque substitutive pour la saisie de l'e-mail

Ce paramètre ne s'applique qu'au type de message du formulaire de capture d'e-mail. Saisissez le texte personnalisé qui apparaîtra comme marque substitutive dans le champ de saisie de l'e-mail. La valeur par défaut est "Entrez votre adresse e-mail".

## Étape 5 : Donnez du style à votre message in-app

L'onglet **Style** vous permet d'ajuster tous les aspects visuels de votre message. Téléchargez une image ou un badge, ou choisissez une icône de badge prédéfinie. Modifiez les couleurs du texte de l'en-tête et du corps, des boutons et de l'arrière-plan en sélectionnant dans une palette ou en saisissant un code hexadécimal, RVB ou HSB.

Le contenu de l'onglet **Style** varie en fonction des options de message que vous avez choisies à l'étape précédente, mais peut inclure l'une des options suivantes :

| Formatage | Entrée | Description |
|---|---|---|
|[Profil de couleur]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/color_profiles_and_css) | Appliquer à partir de la galerie de modèles de messages in-app. | Sélectionnez **Appliquer un modèle** et choisissez dans la galerie. Sélectionnez ensuite **Enregistrer**. |
|Alignement du texte | Gauche, centre ou droite.  | Uniquement disponible pour les versions plus récentes du SDK de Braze. |
|En-tête | Code couleur HEX. | La couleur HEX souhaitée s'affiche. Vous pourrez également choisir l'opacité de la couleur.  |
|Texte | Code couleur HEX. | La couleur HEX souhaitée s'affiche. Vous pourrez également choisir l'opacité de la couleur. |
|Boutons | Code couleur HEX. | Les couleurs HEX souhaitées s'affichent. Vous pourrez également choisir l'opacité des couleurs. Vous pouvez choisir des couleurs pour : l'arrière-plan du bouton de fermeture du message ainsi que l'arrière-plan, le texte et la bordure de chaque bouton. |
| Bordure des boutons | Code couleur HEX. | Nouveau ! Cela vous permettra de différencier vos boutons principaux et secondaires. Nous vous suggérons de souligner les boutons avec des couleurs contrastées. |
|Couleur de fond | Code couleur HEX. | La couleur HEX souhaitée s'affiche. Vous pourrez également choisir l'opacité de la couleur. Il s'agit de l'arrière-plan de l'ensemble du message, qui s'affiche clairement derrière le corps du texte. |
|Superposition d'écran | Code couleur HEX. | La couleur HEX souhaitée s'affiche. Vous pourrez également choisir l'opacité de la couleur. Uniquement disponible pour les versions plus récentes du SDK de Braze. C'est le cadre dans lequel s'inscrit l'ensemble du message. |
|Chevron ou autre option Fermer le message | Code couleur HEX. | La couleur HEX souhaitée s'affiche. Vous pourrez également choisir l'opacité de la couleur. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[Prévisualisez et testez]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) toujours votre message avant de l'envoyer.

{% alert important %}
Certains types de messages in-app n'ont pas d'option de style personnalisé autre que le téléchargement de HTML (ou CSS ou JavaScript) et de ressources à l'aide d'un fichier ZIP. [Web Modal with CSS]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css) vous permet de télécharger ou d'écrire des feuilles de style personnalisé (CSS) afin de créer de magnifiques envois de messages personnalisés.
{% endalert %}

## Étape 6 : Configurer des paramètres supplémentaires (en option)

### Paires clé-valeur

Vous pouvez ajouter des [paires clé-valeur]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) pour envoyer des champs personnalisés supplémentaires aux appareils des utilisateurs.

## Étape 7 : Créez le reste de votre campagne ou Canvas

{% tabs %}
{% tab Campaign %}

Créez le reste de votre campagne ; consultez les sections suivantes pour obtenir des conseils supplémentaires sur la meilleure façon d'utiliser nos outils pour créer des messages in-app.

#### Choisissez un déclencheur

Sélectionnez l'action à partir de laquelle vous souhaitez déclencher votre message, ainsi que les heures de début et de fin de votre campagne ou Canvas.

{% alert important %}
Notez que si vous avez l'intention de déclencher votre message in-app sur la base d'un événement personnalisé, cet événement personnalisé doit être envoyé à l'aide du SDK.
{% endalert %}

Campagne basée sur l'action avec l'action de déclenchement définie sur "Démarrer la session".]({% image_buster /assets/img_archive/in_app_schedule.png %}){: style="max-width:80%"}

La réception/distribution des messages in-app est entièrement basée sur les déclencheurs d'action suivants :

- Effectuer un achat
- Ouverture de l'application/page web
- Exécution d'un événement personnalisé (ne fonctionne qu'avec les événements envoyés à l'aide du SDK)
- Ouverture d'un message push spécifique
- Planifiez automatiquement l'envoi des campagnes à une certaine heure en fonction de l'heure locale de chacun de vos utilisateurs.
- Les messages peuvent également être configurés pour se répéter chaque jour, chaque semaine (éventuellement à des jours précis) ou chaque mois.

Une date et une heure de début doivent être sélectionnées, mais une date de fin est facultative. Une date de fin empêchera ce message in-app spécifique de s'afficher sur les appareils après la date/heure spécifiée.

Reportez-vous à notre documentation destinée aux développeurs pour le [déclenchement d'événements côté serveur]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web) et la [réception/distribution locale de messages in-app]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#local-in-app-messages).

##### Déclenchement en ligne ou hors ligne

Les messages in-app fonctionnent en envoyant le message et les déclencheurs sur l'appareil de l'utilisateur. Une fois que les messages in-app sont sur un appareil, ils attendent pour s'afficher que la condition de déclenchement soit remplie. Si les messages in-app sont déjà mis en cache sur l'appareil de l'utilisateur, vous pouvez même déclencher des messages in-app hors ligne sans connexion à Braze (par exemple, en mode Avion).

{% alert important %}
Une fois qu'un message in-app a été arrêté, certains utilisateurs peuvent continuer à voir le message s'ils ont démarré une session avant l'arrêt du message et s'ils effectuent ensuite l'événement déclenchcheur. Ces utilisateurs seront comptabilisés comme une impression unique même après l'arrêt de la campagne.
{% endalert %}

#### Choisissez une priorité

Enfin, après avoir sélectionné l'action à partir de laquelle le message in-app sera déclenché, vous devez également définir une priorité. Si deux messages sont déclenchés par la même action, les messages hautement prioritaires seront planifiés pour apparaître sur les appareils des utilisateurs avant les messages moins prioritaires. 

Vous avez le choix entre les priorités d'envoi des messages suivantes :

- Faible priorité (affichée après d'autres messages)
- Priorité moyenne
- Priorité élevée (affichée avant les autres messages)

Les options haute, moyenne et basse pour les priorités des messages déclenchés sont des compartiments et, à ce titre, plusieurs messages peuvent avoir la même priorité sélectionnée. Pour définir des priorités au sein de ces compartiments, cliquez sur **Définir une priorité exacte**. Vous pourrez alors glisser-déposer des campagnes pour les ordonner avec la priorité correcte.

\![Exemple de définition de la priorité pour une campagne de messages in-app et Canvas.]({% image_buster /assets/img_archive/bucket_prioritization.png %}){: style="max-width:70%"}

#### Choisissez les utilisateurs à cibler

Ensuite, vous devez [cibler les utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) en choisissant des segments ou des filtres pour réduire votre audience. Vous obtiendrez automatiquement un aperçu de ce à quoi ressemble la population de ce segment approximatif à l'heure actuelle. N'oubliez pas que l'appartenance exacte à un segment est toujours calculée juste avant l'envoi du message.

{% alert note %}
S'il y a un délai sur l'étape de l'envoi de messages in-app, l'appartenance au segment sera évaluée après le délai. Si l'utilisateur est éligible, le message in-app se synchronisera lors de la prochaine session disponible.
{% endalert %}

##### Réévaluer l'éligibilité de la campagne et le liquide

Dans certains scénarios, vous pouvez vouloir réévaluer l'éligibilité d'un utilisateur lorsqu'il déclenche l'affichage d'un message in-app. Il peut s'agir, par exemple, de campagnes ciblant un attribut personnalisé qui change fréquemment ou d'envois de messages qui doivent tenir compte de tout changement de profil de dernière minute.

\![Case à cocher pour "Réévaluer l'éligibilité de la campagne avant de l'afficher" sélectionnée.]({% image_buster /assets/img_archive/re-evaluate-iam-membership.png %}){:style="max-width:60%"}

Lorsque vous sélectionnez **Réévaluer l'éligibilité de la campagne avant l'affichage**, une demande supplémentaire sera adressée à Braze pour confirmer que l'utilisateur est toujours éligible pour ce message avant l'envoi. En outre, toute variable [liquide]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) ou [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) sera mis en forme à ce moment-là, avant l'affichage du message.

Cela permet d'éviter que des messages in-app soient envoyés à des utilisateurs dans le cadre de campagnes expirées ou archivées. Si vous ne réévaluez pas l'éligibilité d'un utilisateur, celui-ci recevra le message in-app même après l'expiration ou l'archivage de la campagne, car le message se trouve dans votre SDK et attend que les utilisateurs le déclenchent.

{% alert note %}
L'activation de cette option entraînera un léger retard (< 100ms) entre le moment où un utilisateur déclenche un message in-app et le moment où le message est affiché en raison de l'éligibilité supplémentaire et de la demande de templating.
<br><br>
N'utilisez pas cette option pour les messages qui peuvent être déclenchés lorsque l'utilisateur n'est pas en ligne ou lorsque l'éligibilité et la réévaluation du liquide ne sont pas nécessaires.
{% endalert %}

#### Choisissez des événements de conversion

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), après avoir reçu une campagne. Vous avez la possibilité d'autoriser une fenêtre de 30 jours maximum pendant laquelle une conversion sera comptabilisée si l'utilisateur effectue l'action spécifiée.

{% endtab %}
{% tab Canvas %}

Si vous ne l'avez pas encore fait, complétez les sections restantes de votre composante Canvas. Pour plus de détails sur la manière de créer le reste de votre Canvas, de mettre en œuvre les tests multivariés et la sélection intelligente, et plus encore, reportez-vous à l'étape [Créer votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de notre documentation sur le Canvas.

Pour en savoir plus sur les options d'envoi de messages in-app spécifiques à Canvas, reportez-vous à [Messages in-app dans Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/).

{% endtab %}
{% endtabs %}

## Étape 8 : Examiner et déployer

Une fois que vous avez fini de créer la dernière partie de votre campagne ou de votre canvas, passez en revue ses détails, [testez-le]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/), puis envoyez-le !

Ensuite, consultez le [rapport sur les messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/) pour savoir comment accéder aux résultats de vos campagnes de communication.

## Ce qu'il faut savoir

### Limites des campagnes de messages in-app actives

Braze accorde une grande importance à la fiabilité et à la rapidité. Tout comme nous vous suggérons de n'envoyer à Braze que les données dont vous avez besoin, nous vous recommandons également de désactiver toutes les campagnes qui n'apportent plus de valeur ajoutée à votre marque.

Le traitement des campagnes de messages in-app basées sur des actions qui sont toujours dans un état actif mais qui n'envoient plus de messages ou qui ne sont plus nécessaires ralentit la performance globale des services Braze pour vous et d'autres clients. Ce temps supplémentaire nécessaire au traitement de ces nombreuses campagnes en veille signifie que tout message in-app mettra plus de temps à apparaître sur les appareils de l'utilisateur final, ce qui a un impact sur l'expérience finale de ce dernier.

{% alert important %}
Vous pouvez avoir jusqu'à 200 campagnes de messages in-app actives, basées sur des actions, par espace de travail afin d'optimiser la vitesse de réception/distribution des messages et d'éviter les dépassements de délai. Cela ne s'applique pas aux toiles.
{% endalert %}

Le nombre de 200 comprend les campagnes de messages in-app actives dont l'heure de fin n'a pas encore été atteinte et celles dont l'heure de fin n'a pas été fixée. Les campagnes de messages in-app actives dont l'heure de fin est dépassée ne seront pas comptabilisées. Le client moyen de Braze a un total de 26 campagnes actives en même temps. Il est donc peu probable que cette limitation vous affecte.


