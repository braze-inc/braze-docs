---
nav_title: Création d’un message in-app
article_title: Création d’un message in-app
page_order: 1
description: "Cet article de référence explique comment créer un message in-app à l'aide de la plateforme Braze en utilisant des campagnes ou Canvas."
channel:
  - in-app messages
tool:
  - Campaigns
search_rank: 4.8
toc_headers: h2
---

# Création d’un message in-app

> Vous pouvez créer un message in-app ou intégré au navigateur en utilisant la plateforme Braze par le biais de campagnes, de Canvas ou d’une campagne API. Nous vous recommandons vivement de planifier vos messages et de préparer tous les documents à l'avance à l'aide de notre [guide pratique de préparation des messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/).

## Étape 1 : Choisir où créer votre message {#create-new-campaign-in-app}

Vous ne savez pas si votre message doit être envoyé via une campagne ou un Canvas ? Les campagnes sont mieux adaptées aux campagnes de communication simples et uniques, tandis que les Canvas sont mieux adaptés aux parcours client en plusieurs étapes.

{% tabs %}
{% tab Campagne %}

1. Allez dans **Messagerie** > **Campagnes** et sélectionnez **Créer une campagne**.
2. Sélectionnez **Message in-app.** Notez que les messages in-app ne sont pas disponibles dans les campagnes multicanaux.
3. Donnez un nom clair et significatif à votre campagne.
4. Ajoutez [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) et [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) au besoin.
   * Les balises facilitent la recherche et l’identification des campagnes, et la création de rapports. Par exemple, lorsque vous utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), vous pouvez filtrer les éléments en fonction de certaines étiquettes spécifiques.
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Vous pouvez choisir différentes plates-formes, types de messages et mises en page pour chacune de vos variantes ajoutées. Pour plus d'informations sur ce sujet, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Si tous les messages de votre campagne vont être similaires ou avoir le même contenu, composez votre message avant d’ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copier à partir de la variante** dans la liste déroulante **Ajouter une variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Créez votre canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) à l'aide du compositeur de canvas.
2. Après avoir configuré votre Canvas, ajoutez une étape dans le Créateur de Canvas. Donnez un nom clair et significatif à votre étape.
3. Choisissez une [planification des étapes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) et spécifiez un délai si nécessaire. Notez que les étapes contenant des messages in-app ne peuvent pas être basées sur des actions.
4. Filtrez votre audience pour cette étape, si nécessaire. Vous pouvez affiner davantage les destinataires de cette étape en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options d’audience seront vérifiées après le délai, au moment de l’envoi des messages.
5. Choisissez votre [comportement d'avancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Choisissez les autres canaux de communication que vous souhaitez associer à votre message.

{% alert important %}
Vous ne pouvez pas avoir plusieurs variantes de messages in-app dans une même étape.
{% endalert %}

Vous trouverez davantage d'informations spécifiques à Canvas dans les [messages in-app dans Canvas.]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/)

{% endtab %}
{% endtabs %}

## Étape 2 : Spécifier les plateformes de livraison

Commencez par choisir les plateformes devant recevoir le message. Cette sélection vous permet de limiter la livraison d’une campagne à un ensemble spécifique d’applications. Par exemple, vous pouvez choisir **Navigateurs web** pour un message dans le navigateur encourageant les utilisateurs à télécharger votre application mobile afin de vous assurer qu'ils ne reçoivent pas le message après avoir déjà obtenu votre application. Les sélections de plateformes étant spécifiques à chaque variante, vous pourriez essayer de tester l'engagement des messages par plateforme.

| Plateforme                        | Livraison des messages        |
|---------------------------------|-------------------------|
| Applications mobiles                     | SDK iOS et Android      |
| Navigateurs Web                    | Web SDK                 |
| Applications mobiles et navigateurs Web | SDK iOS, Android et Web |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Étape 3 : Spécifiez vos types de messages

Une fois que vous avez sélectionné une plateforme d’envoi, parcourez les types de messages, les mises en page et autres options associées. Pour en savoir plus sur le comportement attendu et l'aspect de chacun de ces messages, consultez notre page [Détails créatifs]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/), ou cliquez sur les types de messages liés dans les tableaux suivants.

Lorsque vous décidez du type de message à utiliser, tenez compte de l'espace que votre message occupera et de l'effet perturbateur qu'il peut avoir sur l'expérience de l'utilisateur.

- Les messages **contextuels** sont les moins intrusifs, car ils apparaissent subtilement sans bloquer le contenu.
- Les messages **modaux** se situent au milieu, suffisamment présents pour attirer l'attention sans envahir l'écran.
- Les messages **en plein écran** sont ceux qui attirent le plus l'attention et qui conviennent le mieux aux annonces ou aux promotions importantes.

Plus votre contenu est complexe, plus vous aurez besoin d'espace et plus votre message risque d'interrompre le flux de l'utilisateur.

### Types de messages

Ces messages in-app sont acceptés par les applications mobiles et les applications Web.

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
    <td>Grand et en gras ! À utiliser pour vous assurer que les utilisateurs voient votre contenu, comme vos campagnes clés, des notifications importantes ou des promotions massives.<br><br>Notez que sur les appareils mobiles, les messages en mode portrait et paysage ne s'affichent pas si l'orientation de l'appareil ne correspond pas à celle du message.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/modal'>Boîte de dialogue modale</a></td>
    <td>Messages occupant tout l’écran entier avec une incrustation et un bloc de texte.</td>
    <td>
      <ul>
      <li>Texte (avec image facultative)</li>
      <li>Image uniquement</li>
      </ul>
    </td>
    <td>S.O.</td>
    <td>Un bon juste milieu. À utiliser lorsque vous avez besoin d’une façon apparente d’attirer l’attention de vos utilisateurs, par exemple pour essayer une nouvelle fonctionnalité ou profiter d’une promotion.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup'>Fenêtre contextuelle</a></td>
    <td>Messages qui glissent à un endroit concret sans bloquer le reste de l’écran.</td>
    <td>S.O.</td>
    <td>S.O.</td>
    <td>Discret car il occupe un espace minimal à l’écran. À utiliser pour avertir les utilisateurs d’extraits de code d’informations, comme de nouvelles fonctionnalités, des annonces, l’utilisation de cookies, etc.<br></td>
  </tr>
</tbody>
</table>

### Types de messages avancés

Ces messages in-app sont personnalisables selon vos besoins.

<table class="tg">
<thead>
  <tr>
    <th>Type de message</th>
    <th>Description du type</th>
    <th>Dispositions disponibles</th>
    <th>Conditions</th>
    <th>Utilisation recommandée</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages'>Message HTML personnalisé</a></td>
    <td>Messages personnalisés qui s’affichent comme défini dans votre code personnalisé (HTML, CSS et/ou Javascript).</td>
    <td>S.O.</td>
    <td>Doit définir l’option d’initialisation <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> sur <code>true</code> pour que votre message in-app fonctionne.</td>
    <td>Une option utile pour bénéficier de tous les avantages des messages in-app si vous avez aussi besoin d’autres fonctionnalités ou que l’apparence doit rester cohérente. Vous pouvez modifier chaque détail du message : police, couleur, forme, taille, boutons, etc. <br><br>Exemples de cas d’utilisation : demander aux utilisateurs des commentaires sur l’application, des formulaires de capture d’e-mail ou des messages paginés</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#email-capture-form'>Formulaire de capture d’adresses e-mail</a></td>
    <td>Généralement utilisé pour obtenir l’e-mail d’un visiteur.</td>
    <td>S.O.</td>
    <td>Doit définir l’option d’initialisation <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> sur <code>true</code> pour que votre message in-app fonctionne.</td>
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
    <td>Un modal Web avec CSS est unique au SDK Web et peut uniquement être utilisé après avoir sélectionné <b>Web Browsers (Navigateurs Web)</b>.</td>
    <td>À utiliser lorsque vous voulez télécharger ou écrire un CSS personnalisé pour créer une élégante communication personnalisée. </td>
  </tr>
</tbody>
</table>

{% alert important %}
Si Braze détecte que vous n’avez pas de bouton de fermeture dans votre code, nous vous demanderons d’en ajouter un. Pour votre commodité, nous fournissons un extrait de code que vous pouvez copier et coller dans votre code : <br><br>`<a href= "appboy://close">X</a>`.
{% endalert %}

## Étape 4 : Composer votre message in-app

L'onglet **Composer** vous permet de modifier tous les aspects du contenu et du comportement de votre message.

![Un exemple de message in-app d'une marque pour souhaiter la bienvenue aux nouveaux clients et les inviter à créer un profil utilisateur.]({% image_buster /assets/img_archive/iam_compose.png %}).{: style="max-width:85%" }

Le contenu de l'onglet **Composer** varie en fonction des options de message que vous avez choisies à l'étape précédente, mais peut inclure l'une des options suivantes :

### Langue

Sélectionnez **Ajouter des langues** et sélectionnez les langues souhaitées dans la liste proposée. Cela permettra d'insérer [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) dans votre message. Nous vous recommandons de sélectionner vos langues avant d’écrire votre contenu afin que vous puissiez remplir votre texte dans Liquid. Consultez la [liste complète des langues disponibles]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

### Image

Selon le type de message, vous pouvez **télécharger une image**, **choisir un badge** ou utiliser **Font Awesome.** Pour télécharger une image, cliquez sur **Ajouter une image** ou indiquez l'URL de l'image. En cliquant sur **Ajouter une image**, vous ouvrez la **bibliothèque multimédia**, où vous pouvez sélectionner une image déjà téléchargée ou en ajouter une nouvelle. Chaque type de message et plateforme peut avoir ses propres proportions suggérées et ses conditions, donc vérifiez-les avant de les mettre en œuvre ou de créer une image à partir de zéro !

### En-tête et corps

Écrivez ce que bon vous semble ! Inclure un texte entièrement personnalisé (souvent avec des capacités HTML personnalisées) avec la possibilité d'inclure des [liquides]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) et d'autres types de personnalisation. Plus vite votre message est diffusé et votre client clique, mieux c’est ! Nous recommandons des en-têtes et un contenu de message clairs et concis.

Certains types de messages ne requièrent pas et ne demandent donc pas d’en-têtes.

#### Conseils 

##### Générer une copie d'intelligence artificielle

Besoin d’aide pour créer un texte d’exception ? Essayez d'utiliser l'[assistant de rédaction de l'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Saisissez un nom ou une description du produit et l’IA générera un texte marketing semblant d’origine humaine pour une utilisation dans votre envoi de messages.

![Bouton Lancer le rédacteur IA situé dans le champ Message du composeur de messages in-app.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_iam.png %}){: style="max-width:60%"}

##### Création d'envois de messages de droite à gauche

Vous avez besoin d'aide pour rédiger des messages de droite à gauche dans des langues telles que l'arabe et l'hébreu ? Reportez-vous à la section [Créer des messages de droite à gauche]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) pour connaître les meilleures pratiques.

### Texte du bouton {#buttons}

Lorsque le type de message est disponible, jusqu’à deux boutons peuvent apparaître sous le corps du texte. Vous pouvez créer et modifier le texte et la couleur du bouton personnalisé. Vous pouvez également ajouter un lien aux conditions de service dans les formulaires de capture d’e-mail.

Si vous choisissez d’utiliser un seul bouton, il s’ajuste automatiquement pour occuper l’espace disponible au bas de votre message au lieu de laisser de la place pour un autre bouton.

#### Choisir un bouton principal

Si vous décidez d’appliquer vos couleurs à ces boutons, nous vous recommandons d’utiliser le bouton 2 pour votre résultat préféré.

En d’autres termes, si vous souhaitez que votre utilisateur clique sur un bouton plus que l’autre, assurez-vous qu’il se trouve sur la droite. Les clics s’avèrent plus fréquents sur le bouton de droite, notamment s’il a une couleur légèrement contrastée ou tranchante par rapport au reste du message. Ce cas ne se vérifie que si le bouton sur la gauche se fond davantage dans le message.

![Boutons primaires et secondaires dans un message in-app]({% image_buster /assets/img/primary-secondary-buttons.png %})

### Comportement lors du clic {#button-actions}

Lorsque votre client clique sur un bouton dans votre message in-app, les actions suivantes sont disponibles. 

| Action | Description |
|---|---|
| Rediriger vers une URL Web | Ouvrir une page Web non native. |
| [Lien profond dans l'application]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content) | Lien profond vers un écran existant de votre appli. |
| Fermer le message | Ferme le message actuellement actif. |
| Enregistrer un événement personnalisé | Choisissez un [événement personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) à déclencher. Utilisable pour afficher un autre message in-app ou déclencher des envois de messages supplémentaires. |
| Enregistrer un attribut personnalisé | Choisissez un [attribut personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) à définir pour l'utilisateur actuel. |
| Demander l’autorisation pour les notifications push | Affiche l’autorisation native pour les notifications push. Découvrez plus d’informations plus sur l'[amorçage des notifications push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/), ainsi que sur les [bonnes pratiques]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#best-practices) pour préparer les utilisateurs aux notifications push. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Remarque : les options __Request Push Permission__, __Log Custom Event__ et __Log Custom Attribute__ nécessitent les versions minimales suivantes du SDK :

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

### Options d’appareil iOS

Vous avez la possibilité de restreindre l’envoi de vos messages in-app à des appareils iOS. Pour ce faire, cliquez sur **Modifier** et sélectionnez **Envoyer uniquement aux appareils iOS.**

### Fermeture du message

Choisissez entre les options suivantes :
 
- **Fermer automatiquement :** Sélectionnez le nombre de secondes que le message reste à l’écran.
- **Attendez que l'utilisateur glisse ou touche :** Nécessite une option de rejet ou de fermeture.

### Position de slideup

Ce paramètre s’applique uniquement au type de message slideup. Vous pouvez choisir de faire apparaître votre contextuel **en bas** ou **en haut** de l'écran de l'application.

### HTML et ressources

Ce paramètre s’applique uniquement au type de message personnalisé. Copiez et collez le code HTML dans l'espace disponible et téléchargez vos ressources à l'aide d'un fichier ZIP.

### Marque substitutive d’entrée de capture d’e-mail

Ce paramètre s’applique uniquement au type de message de formulaire de capture d’e-mail. Saisissez un texte personnalisé qui apparaîtra comme marque substitutive pour le champ d’entrée d’e-mail. Par défaut s’affiche le message « Enter your email address » (Saisissez votre adresse e-mail).

## Étape 5 : Styliser votre message in-app

L'onglet **Style** vous permet d'ajuster tous les aspects visuels de votre message. Téléchargez une image ou un badge, ou choisissez une icône de badge préconçue. Modifiez les couleurs de l’en-tête, du texte du corps, des boutons et de l’arrière-plan à l’aide d’une palette ou en saisissant un code hexadécimal, RVB ou HSB.

Le contenu de l'onglet **Style** varie en fonction des options de message que vous avez choisies à l'étape précédente, mais peut inclure l'une des options suivantes :

| Formatage | Entrée | Description |
|---|---|---|
|[Profil de couleur]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/color_profiles_and_css) | Appliquer à partir de la galerie des modèles de messages in-app. | Sélectionnez **Appliquer un modèle** et choisissez dans la galerie. Sélectionnez ensuite **Enregistrer**. |
|Alignement du texte | Gauche, Centre ou Droite.  | Disponible uniquement pour les versions plus récentes du SDK Braze. |
|En-tête | Code de couleur HEX. | La couleur HEX souhaitée s’affiche. Vous pouvez également choisir l’opacité de la couleur.  |
|Texte | Code de couleur HEX. | La couleur HEX souhaitée s’affiche. Vous pouvez également choisir l’opacité de la couleur. |
|Boutons | Code de couleur HEX. | Les couleurs HEX souhaitées s’affichent. Vous pouvez également choisir l’opacité des couleurs. Vous pouvez choisir des couleurs pour l’arrière-plan du bouton de fermeture du message, ainsi que l’arrière-plan, le texte et la bordure de chaque bouton. |
| Bordure du bouton | Code de couleur HEX. | Nouveau ! Vous pouvez ainsi définir les boutons principaux et secondaires de façon indépendante. Nous suggérons de choisir pour le contour des boutons des couleurs contrastantes. |
|Couleur d’arrière-plan | Code de couleur HEX. | La couleur HEX souhaitée s’affiche. Vous pouvez également choisir l’opacité de la couleur. Il s’agit de l’arrière-plan du message entier qui s’affiche clairement derrière le corps de votre texte. |
|Incrustation à l’écran | Code de couleur HEX. | La couleur HEX souhaitée s’affiche. Vous pouvez également choisir l’opacité de la couleur. Disponible uniquement pour les versions plus récentes du SDK Braze. Il s’agit du cadre autour du message entier. |
|Chevron ou autre option de fermeture du message | Code de couleur HEX. | La couleur HEX souhaitée s’affiche. Vous pouvez également choisir l’opacité de la couleur. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[Prévisualisez et testez]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) toujours votre message avant de l'envoyer.

{% alert important %}
Certains types de messages in-app n'ont pas d'option de style personnalisé autre que le téléchargement de HTML (ou CSS ou JavaScript) et de ressources à l'aide d'un fichier ZIP. [Web Modal with CSS]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css) vous permet de télécharger ou d'écrire des feuilles de style personnalisé (CSS) pour créer de magnifiques envois de messages personnalisés.
{% endalert %}

## Étape 6 : Configurer des paramètres supplémentaires (facultatif)

### Paires clé-valeur

Vous pouvez ajouter des [paires clé-valeur]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) pour envoyer des champs personnalisés supplémentaires aux appareils des utilisateurs.

## Étape 7 : Créer le reste de votre campagne ou de votre Canvas

{% tabs %}
{% tab Campagne %}

Élaborez le reste de votre campagne ; consultez les sections suivantes pour obtenir des conseils supplémentaires sur le meilleur usage de nos outils afin de créer des messages in-app.

#### Choisir un déclencheur

Sélectionnez l’action à partir de laquelle votre message doit être déclenché, ainsi que les heures de début et de fin pour votre campagne ou Canvas.

{% alert important %}
Notez que si vous avez l'intention de déclencher votre message in-app sur la base d'un événement personnalisé, cet événement personnalisé doit être envoyé à l'aide du SDK.
{% endalert %}

![Campagne basée sur l'action avec l'action de déclenchement réglée sur "Démarrer la session".]({% image_buster /assets/img_archive/in_app_schedule.png %}){: style="max-width:80%"}

La livraison des messages in-app est entièrement basée sur les déclencheurs d’action suivants :

- Faire un achat
- Ouvrir l’application/la page Web
- Exécution d'un événement personnalisé (ne fonctionne qu'avec les événements envoyés à l'aide du SDK)
- Ouvrir un message de notification push spécifique
- Planifiez automatiquement les campagnes pour des envois à des moments précis en fonction de l’heure locale de chacun de vos utilisateurs.
- Les messages peuvent également être configurés pour une récurrence quotidienne, hebdomadaire (éventuellement à des jours spécifiques) ou mensuelle.

Une date et une heure de début doivent être sélectionnées, mais une date de fin est facultative. Une date de fin empêche ce message in-app spécifique de s’afficher sur les appareils après la date et l’heure indiquées.

Reportez-vous à notre documentation destinée aux développeurs pour le [déclenchement d'événements côté serveur]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web) et la [réception/distribution locale de messages in-app.]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#local-in-app-messages)

##### Déclenchement en ligne ou hors ligne

Les messages in-app fonctionnent par l’envoi du message et de déclencheurs à l’appareil de l’utilisateur. Une fois que les messages in-app sont sur un appareil, la condition de déclenchement doit être remplie pour qu’ils puissent s’afficher. Si les messages in-app sont déjà mis en cache sur l’appareil de l’utilisateur, vous pouvez même les déclencher hors ligne sans connexion à Braze (par exemple, en mode Avion).

{% alert important %}
Une fois qu’un message in-app a été arrêté, certains utilisateurs peuvent continuer à voir le message s’ils ont démarré la session avant que le message ne soit arrêté et ont ensuite effectué l’événement déclencheur. Ces utilisateurs sont comptabilisés comme impression unique, même après l’arrêt de la campagne.
{% endalert %}

#### Choisir une priorité

Enfin, après avoir sélectionné l'action à partir de laquelle le message in-app sera déclenché, vous devez également définir une priorité. Si deux messages sont déclenchés depuis la même action, les messages de priorité élevée sont planifiés pour s’afficher sur les appareils des utilisateurs avant ceux moins prioritaires. 

Vous pouvez choisir entre les priorités de message suivantes :

- Priorité faible (affiché après d’autres messages)
- Priorité moyenne
- Priorité élevée (affiché avant d’autres messages)

Les options de priorité faible, moyenne et élevée pour les messages déclenchés sont des compartiments, et des messages multiples peuvent avoir la même priorité sélectionnée. Pour définir des priorités au sein de ces compartiments, cliquez sur **Définir une priorité exacte**. Vous pourrez alors glisser-déposer des campagnes pour les ordonner avec la priorité correcte.

![Exemple de définition des priorités pour une campagne de messages in-app et Canvas.]({% image_buster /assets/img_archive/bucket_prioritization.png %}){: style="max-width:70%"}

#### Choisir les utilisateurs à cibler

Ensuite, vous devez [cibler les utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) en choisissant des segments ou des filtres pour réduire votre audience. Vous recevez automatiquement un aperçu de ce à quoi ressemble la population approximative du segment à ce moment-là. Gardez à l’esprit que l’appartenance à un segment exact est toujours calculée juste avant l’envoi du message.

{% alert note %}
En cas de retard à l’étape de message in-app, l’appartenance à un segment est évaluée après le délai. Si l’utilisateur est éligible, le message in-app se synchronise lors de la prochaine session disponible.
{% endalert %}

##### Réévaluer l’éligibilité de la campagne et de Liquid

Dans certains scénarios, vous voulez éventuellement réévaluer l’éligibilité d’un utilisateur lorsqu’il déclenche un message in-app à afficher. Les exemples incluent des campagnes qui ciblent un attribut personnalisé amené à changer fréquemment, ou des messages devant refléter les changements de profil de dernière minute.

![Case à cocher pour "Réévaluer l'éligibilité de la campagne avant de l'afficher".]({% image_buster /assets/img_archive/re-evaluate-iam-membership.png %}){:style="max-width:60%"}

Lorsque vous sélectionnez **Réévaluer l'éligibilité de la campagne avant l'affichage**, une demande supplémentaire sera adressée à Braze pour confirmer que l'utilisateur est toujours éligible pour ce message avant l'envoi. En outre, toute variable [liquide]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) ou [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) sera mis en forme à ce moment-là, avant l'affichage du message.

Cela permet d'éviter que des messages in-app soient envoyés à des utilisateurs dans le cadre de campagnes expirées ou archivées. Si vous ne réévaluez pas l'éligibilité d'un utilisateur, celui-ci recevra le message in-app même après l'expiration ou l'archivage de la campagne, car le message se trouve dans votre SDK et attend que les utilisateurs le déclenchent.

{% alert note %}
L’activation de cette option entraîne un léger retard (< 100 ms) entre le déclenchement d’un message in-app et son affichage en raison de la demande ajoutée d’éligibilité et de mise en place.
<br><br>
N’utilisez pas cette option pour les messages qui peuvent être déclenchés lorsqu’un utilisateur est hors ligne ou lorsque l’éligibilité et la réévaluation de Liquid ne sont pas requises.
{% endalert %}

#### Sélectionner des événements de conversion

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), après avoir reçu une campagne. Vous avez la possibilité d’autoriser une fenêtre allant jusqu’à 30 jours pendant laquelle une conversion sera comptée si l’utilisateur entreprend l’action spécifiée.

{% endtab %}
{% tab Canvas %}

Si vous ne l’avez pas déjà fait, complétez les sections restantes de votre composant de Canvas. Pour plus de détails sur la manière de créer le reste de votre Canvas, de mettre en œuvre les tests multivariés et la sélection intelligente, et plus encore, reportez-vous à l'étape [Créer votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de notre documentation sur le Canvas.

Pour plus d'informations sur les options d'envoi de messages in-app spécifiques à Canvas, reportez-vous à [Messages in-app dans Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/).

{% endtab %}
{% endtabs %}

## Étape 8 : Revue et déploiement

Une fois que vous avez fini de créer la dernière partie de votre campagne ou de votre canvas, passez en revue ses détails, [testez-le]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/), puis envoyez-le !

Ensuite, consultez le [rapport sur les messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/) pour savoir comment accéder aux résultats de vos campagnes de communication.

## Choses à savoir

### Limites de campagnes actives de messages in-app

Braze accorde de l’importance à la fiabilité et à la vitesse. Tout comme nous vous suggérons d’envoyer uniquement les données dont vous avez besoin à Braze, nous vous recommandons de désactiver les campagnes qui n’ajoutent plus de valeur à votre marque.

Le traitement des campagnes de messages in-app par événement, qui sont toujours actives mais n’envoient plus de messages ou qui sont devenues inutiles, ralentit la performance globale des services de Braze pour vous et d’autres clients. Ce temps supplémentaire nécessaire pour traiter ces nombreuses campagnes inactives ralentit l’affichage de tous les messages in-app sur les appareils de l’utilisateur final, ce qui affecte l’expérience de ce dernier.

{% alert important %}
Vous pouvez avoir jusqu'à 200 campagnes de messages in-app actives, basées sur des actions, par espace de travail afin d'optimiser la vitesse de réception/distribution des messages et d'éviter les dépassements de délai. Cela ne s'applique pas aux toiles.
{% endalert %}

Cette limite de 200 inclut des campagnes de communication in-app actives qui n’ont pas encore atteint l’heure de fin et celles qui n’en possèdent pas. Les campagnes de communication in-app actives qui ont dépassé leur heure de fin ne sont pas comptabilisées. Le client Braze standard possédant un total de 26 campagnes actives simultanées, vous ne risquez pas d’être affecté par cette limitation.


