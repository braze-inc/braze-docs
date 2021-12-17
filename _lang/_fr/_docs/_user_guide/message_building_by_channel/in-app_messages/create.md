---
nav_title: Créer un message In-App
article_title: Créer un message In-App
page_order: 0
description: "Vous pouvez créer un message dans l'application en utilisant la plateforme Braze en utilisant des campagnes, Canvas, ou en tant que campagne API. Cet article vous guidera tout au long de ce processus."
channel:
  - messages intégrés à l'application
tool:
  - Campagnes
---

# Création d'un message dans l'application

Vous pouvez créer un message dans l'application ou un message dans le navigateur en utilisant la plateforme Braze en utilisant des campagnes, Canvas ou en tant que campagne API. Nous vous recommandons vivement de planifier vos messages et de préparer tout le matériel à l'avance en utilisant notre [guide de préparation des messages dans l'application]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/) pratique.

## Étape 1 : Choisissez où construire votre message {#create-new-campaign-in-app}

{% tabs %}
  {% tab Campaigns %}
  Cliquez sur __Créer une campagne__ pour ouvrir un nouvel assistant de messagerie pour les campagnes de messages dans l'application. Ensuite, suivez le flux de l'assistant de messagerie pour créer et lancer rapidement votre campagne de message dans l'application.

  ![Sélecteur de plateforme]({% image_buster /assets/img/iam_platforms.gif %})

1. Nommez votre campagne quelque chose de clair et significatif.
2. Ajouter __Teams__ et __Tags__, si nécessaire.
3. Ajoutez et nommez autant de variantes que vous avez besoin pour cette campagne.
  - Vous pouvez choisir différentes plateformes, types de messages et mises en page pour chacune de vos variantes ajoutées.

  {% alert tip %}
Si tous les messages de votre campagne vont être similaires ou ont le même contenu, composez votre message avant d'ajouter des variantes supplémentaires - vous serez en mesure de choisir **Copier de la variante** dans le menu déroulant **Ajouter une variante**.
{% endalert %}

 {% endtab %}
 {% tab Canvas %}
 Après avoir [créé votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) en utilisant l'assistant de Canvas

1. Nommez votre étape quelque chose de clair et de significatif.
2. Ajouter un délai, si nécessaire. Notez que les étapes contenant des messages dans l'application ne peuvent pas être basées sur des actions.
3. Filtrer votre audience, si nécessaire.
4. Choisissez vos options d'avancement, si nécessaire.
5. Choisissez tous les autres canaux de messagerie que vous souhaitez associer à votre message.

{% alert important %}
Vous ne pouvez pas avoir plusieurs variantes de messages dans l'application en une seule étape.
{% endalert %}

Vous pouvez trouver plus d'informations spécifiques à Canvas dans [Messages In-app dans Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/).

{% endtab %}
{% endtabs %}

## Étape 2: Spécifiez les plates-formes de livraison

Commencez par choisir les plates-formes à recevoir le message. Utilisez cette sélection pour limiter la distribution d'une campagne à un ensemble d'applications spécifiques. Vous pouvez choisir __Navigateurs Web__ pour un message dans le navigateur encourageant les utilisateurs à télécharger votre application mobile pour s'assurer qu'ils ne reçoivent pas le message après avoir déjà reçu votre application. Parce que les sélections de plateformes sont spécifiques à chaque variante, vous pouvez essayer de tester l'engagement de messages par plateforme !

La capture d'e-mails Web et le modal Web avec CSS sont tous deux uniques au SDK Web et ne peuvent être utilisés qu'après avoir sélectionné __Navigateurs Web__.

| Plateforme                             | Envoi du message        |
| -------------------------------------- | ----------------------- |
| Applications mobiles                   | SDKs iOS & Android      |
| Web Browsers                           | SDK Web                 |
| Applications mobiles & Navigateurs Web | iOS, Android & Web SDKs |
{: .reset-td-br-1 .reset-td-br-2}

## Étape 3 : Spécifiez vos types de messages

Une fois que vous avez sélectionné une plate-forme d'envoi, parcourez les types de messages, les mises en page et les autres options qui y sont associées. En savoir plus sur le comportement et l'apparence attendus de chacun de ces messages sur notre page [Détails Créatifs]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/) , ou en cliquant sur les types de messages liés dans les tableaux suivants.

Lorsque vous décidez du type de message à utiliser, vous devriez considérer à quel point votre campagne de message doit être intrusive. Ceci est une mesure de la quantité d'écran que prendra le message et de la quantité que cela perturbe l'expérience régulière de votre client dans votre application ou votre site. Plus vous souhaitez fournir de contenu riche, plus votre message devra être intrusif.

![Graphique montrant une échelle de moins instrusive à plus intrusive, le curseur étant le moins intrusif, suivi par la modale, et le plein écran étant le plus intrusif]({% image_buster /assets/img_archive/iam_intrusive.png %}){: style="largeur-max-80%" }

### Types de messages

Ces messages sont acceptés par les applications mobiles et les applications web.

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
    <th>Autres options</th>
    <th>Utilisation recommandée</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen'>Plein écran</a></td>
    <td>Messages qui couvrent tout l'écran avec un bloc de messages.</td>
    <td>
      <ul>
      <li>Image & Texte</li>
      <li>Image uniquement</li>
      </ul>
    </td>
    <td>Orientation de périphériques forcés (Portrait ou Paysage)</td>
    <td>Gros et audacieux! Utilisez lorsque vous voulez vous assurer que les utilisateurs voient votre contenu, comme vos campagnes les plus critiques, les notifications importantes ou les promotions massives.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/modal'>Modal</a></td>
    <td>Messages qui couvrent tout l'écran avec une superposition d'écran et un bloc de messages.</td>
    <td>
      <ul>
      <li>Texte (avec image optionnelle)</li>
      <li>Image uniquement</li>
      </ul>
    </td>
    <td>N/A</td>
    <td>Un bon point de milieu. Utilisez lorsque vous avez besoin d'une façon apparente pour attirer l'attention de votre utilisateur, comme encourager les utilisateurs à essayer une nouvelle fonctionnalité ou profiter d'une promotion.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup'>Glissement vers le haut</a></td>
    <td>Les messages qui glissent dans la vue dans un endroit désigné sans bloquer le reste de l'écran.</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>Unobtrusive: prend le moins de biens immobiliers de l'écran. À utiliser pour avertir les utilisateurs de petits extraits d'information, tels que les nouvelles fonctionnalités, les annonces, l'utilisation des cookies, etc.<br></td>
  </tr>
</tbody>
</table>

### Types de messages avancés

Ces messages intégrés sont personnalisables en fonction de vos besoins.

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
    <td>Messages personnalisés qui s'exécutent comme définis dans votre code personnalisé (HTML, CSS, et/ou JavaScript).</td>
    <td>N/A</td>
    <td>Vous devez définir l'option d'initialisation <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> à <code>true</code> pour que votre message dans l'application fonctionne.</td>
    <td>C'est une bonne option si vous voulez tous les avantages des IAMs mais que vous avez besoin de fonctionnalités supplémentaires ou pour que l'apparence reste "sur marque". Vous pouvez modifier chaque petit détail du message : police, couleur, forme, taille, boutons, etc. <br><br>Les exemples de cas d'utilisation incluent la demande de commentaires aux utilisateurs, les formulaires de capture d'e-mails ou les messages paginés</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#email-capture-form'>Formulaire de capture d'email Web</a></td>
    <td>Généralement utilisé pour capturer le courriel du lecteur.</td>
    <td>N/A</td>
    <td>Vous devez définir l'option d'initialisation <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> à <code>true</code> pour que votre message dans l'application fonctionne.</td>
    <td>Lorsque vous demandez aux utilisateurs de soumettre leur adresse e-mail.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css'>Web modal avec CSS</a></td>
    <td>Messages modaux pour le web avec CSS personnalisables.</td>
    <td>
      <ul>
      <li>Texte (avec image optionnelle)</li>
      <li>Image uniquement</li>
      </ul>
    </td>
    <td>N/A</td>
    <td>Lorsque vous voulez télécharger ou écrire un CSS personnalisé pour créer de la beauté, tout autour de la messagerie personnalisée. </td>
  </tr>
</tbody>
</table>

{% alert important %}
Si Braze détecte que vous n'avez pas de bouton de fermeture ou de rejet inclus dans votre code, nous vous demanderons d'en ajouter un. Pour votre commodité, nous avons fourni un snippet que vous pouvez copier et coller dans votre code : `<a href= "appboy://close">X</a>`.
{% endalert %}

## Étape 4 : Composer un message dans l'application

L'onglet **Composer** vous permet de modifier tous les aspects du contenu et du comportement de votre message.

!\[Composez votre message dans l'application\]\[24\]

Le contenu de l'onglet Composer varie selon les options que vous avez choisies lors de l'étape précédente, mais peut inclure l'une des options ci-dessous :

| Contenus                               | Options                                                                                                                                                      | Libellé                                                                                                                                                                                                                                                                                                            |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Langue                                 | Consultez notre [liste complète des langues disponibles][18].                                                                                                | Cliquez sur __Ajouter des langues__ et sélectionnez les langues désirées dans la liste fournie. Ceci insérera Liquid dans votre message. Nous vous recommandons de sélectionner vos langues avant d'écrire votre contenu afin que vous puissiez renseigner votre texte où il appartient dans le Liquid.            |
| Image                                  | __Télécharger l'image__, __choisissez un badge__, ou utilisez __Font Awesome__.                                                                              | Le cas échéant, cliquez sur __Include Image__ ou __Upload Image__ et suivez les instructions présentées. Chaque type de message et plate-forme peut avoir ses propres proportions et exigences suggérées - assurez-vous de vérifier ce qui est avant de mettre en service ou de faire une image à partir de zéro ! |
| Texte du bouton & Comportement du clic | Ajoutez jusqu'à deux [boutons](#buttons).                                                                                                                    | Vous pouvez créer et modifier le texte et la couleur des boutons personnalisés. Vous pouvez également ajouter le lien des conditions d'utilisation dans les formulaires de capture d'e-mails Web.                                                                                                                  |
| Options de l'appareil                  | Restreindre l'envoi aux appareils iOS uniquement.                                                                                                            | Cliquez sur __Changer de__ et cochez la case comme vous le souhaitez.                                                                                                                                                                                                                                              |
| Options de fermeture du message        | __Rejeter automatiquement__ ou __Attendre pour l'utilisateur Swipe ou Touchez__.                                                                             | __Rejeter automatiquement__ vous permet de sélectionner combien de secondes le message restera à l'écran. __Attendez que l'utilisateur Swipe ou Touch__ nécessite une option de renvoi ou de fermeture.                                                                                                            |
| En-tête & Texte du corps               | Copie entièrement personnalisée (souvent avec des capacités HTML personnalisées) avec les options pour inclure Liquid et d'autres types de personnalisation. | Certains types de messages n'ont pas besoin et ne demandent donc pas d'en-têtes.                                                                                                                                                                                                                                   |
| Position                               | __Du bas de l'écran des applications__ ou __du haut de l'écran des applications__.                                                                           | Ceci n'existe que dans le constructeur de messages Universal Slideup.                                                                                                                                                                                                                                              |
| HTML & Actifs                          | Complètement personnalisé via téléchargement, URL, ou copier et coller.                                                                                      | Copiez et collez du HTML dans l'espace disponible et téléchargez vos ressources via ZIP.                                                                                                                                                                                                                           |
| Placeholder de saisie d'email          | Copie personnalisée.                                                                                                                                         | Ceci est utilisé uniquement dans le formulaire de capture de courriel Web et dirigera vos utilisateurs à entrer le contenu désiré dans l'espace.                                                                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Paramètres supplémentaires

#### Boutons {#buttons}

Lorsqu'il est disponible pour votre type de message, vous pouvez avoir jusqu'à deux boutons sous votre corps de texte.

![Primaire_Secondaire]({% image_buster /assets/img/primary-secondary-buttons.png %}){: height="40%" width="40%"}

Si vous choisissez d'utiliser un seul bouton, il s'ajuste automatiquement pour prendre en charge l'espace disponible au bas de votre message au lieu de laisser de la place à un bouton supplémentaire.

{% alert tip %}
  Si vous décidez de formater ces boutons avec vos propres couleurs, nous vous recommandons d'utiliser le bouton 2 pour votre résultat préféré. En d'autres termes, si vous voulez que votre utilisateur clique sur un bouton plus que l'autre, assurez-vous qu'il est sur la droite. Le bouton droit a souvent affiché un meilleur potentiel pour être cliqué, surtout si elle a une couleur quelque peu contrastée ou autrement distincte du reste du message. Ceci n'est mis en évidence que lorsque le bouton de gauche se fond plus visuellement avec le message.
{% endalert %}

#### Générations

Braze a trois générations de messages dans l'application disponibles. Vous pouvez affiner les appareils sur lesquels vos messages doivent être envoyés, en fonction de la génération qu'ils supportent, dans la section [Aperçu]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) lors de la composition de votre message dans l'application.

!\[In-App_Messages_Generations\]\[2\]{: height="50%" width="50%"}

Selon les versions du SDK sur lesquelles vos utilisateurs sont actifs, vous pouvez ou non voir cette option. On ne vous demande de sélectionner une génération que lorsque vous avez des utilisateurs sur plus d'une génération.

{% détails Qu'est-ce qu'une génération ? %}
Une Génération est définie comme une collection de versions SDK qui contiennent un grand nombre de mises à jour majeures. Par exemple, la Génération 3 est la dernière qui englobe les dernières mises à jour de style.

En sélectionnant __Envoyer à toutes les générations qui supportent ce message__, Braze livrera aux utilisateurs qui peuvent recevoir n'importe quelle forme de message. Par exemple, si vous avez des utilisateurs sur les trois générations, un modal sera livré aux utilisateurs sur les générations 2 et 3, car la génération 1 ne prend pas en charge les modaux. Le message sera différent pour vos deux groupes d'utilisateurs : les utilisateurs de la génération 3 recevront le message dans les derniers styles, tandis que les utilisateurs de Generation 2 verront les anciens styles (différences cosmétiques et absence de bordure de bouton).

Vous pouvez effacer la case à cocher __Envoyer à toutes les générations qui prennent en charge ce message__ et sélectionner __Envoyer uniquement aux utilisateurs à la génération 3 (la dernière)__ si vous ne voulez pas permettre aux utilisateurs de recevoir les anciens styles de message. Les utilisateurs de la génération 3 seront les seuls à recevoir le message.
{% enddetails %}

## Étape 5 : Stylez votre message dans l'application

L'onglet **Style** vous permet d'ajuster tous les aspects visuels de votre message. Téléchargez une image ou un badge, ou choisissez une icône de badge pré-conçue. Modifiez les couleurs du texte de l'en-tête et du corps, des boutons et de l'arrière-plan en sélectionnant une palette ou en saisissant un code hexadécimal, RGB ou HSB.

Le contenu de l'onglet **Style** varie en fonction des options de message que vous avez choisies lors de la dernière étape. mais peut inclure l'une des options ci-dessous:

| Formatage en cours                              | Input                                                           | Libellé                                                                                                                                                                                                                                               |
| ----------------------------------------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Profil de couleur                               | Appliquer à partir de la galerie de modèles de messages In-App. | Cliquez sur __Appliquer le modèle__ et sélectionnez dans la galerie. Ensuite, cliquez sur __Enregistrer__.                                                                                                                                            |
| Alignement du texte                             | À gauche, au centre ou à droite.                                | Uniquement disponible pour les nouvelles versions de Braze SDK.                                                                                                                                                                                       |
| En-tête                                         | Code de couleur HEX.                                            | La couleur HEX de votre choix s'affiche. Vous pourrez également choisir l'opacité de la couleur.                                                                                                                                                      |
| Texte du texte                                  | Code de couleur HEX.                                            | La couleur HEX de votre choix s'affiche. Vous pourrez également choisir l'opacité de la couleur.                                                                                                                                                      |
| Boutons                                         | Code de couleur HEX.                                            | Les couleurs HEX de votre choix s'affichent. Vous pourrez également choisir l'opacité des couleurs. Vous pouvez choisir les couleurs pour : l'arrière-plan du message de fermeture ainsi que l'arrière-plan de chaque bouton, le texte et la bordure. |
| Bordure du bouton                               | Code de couleur HEX.                                            | Nouveau! Cela vous permettra de définir vos boutons principaux et secondaires. Nous vous suggérons des boutons avec des couleurs contrastées.                                                                                                         |
| Couleur d'arrière-plan                          | Code de couleur HEX.                                            | La couleur HEX de votre choix s'affiche. Vous pourrez également choisir l'opacité de la couleur. Ceci est l'arrière-plan de l'ensemble du message et s'affichera clairement derrière votre corps texte.                                               |
| Superposition d'écran                           | Code de couleur HEX.                                            | La couleur HEX de votre choix s'affiche. Vous pourrez également choisir l'opacité de la couleur. Uniquement disponible pour les nouvelles versions de Braze SDK. Voici le cadre autour de l'ensemble du message.                                      |
| Chevron ou autre option de message de fermeture | Code de couleur HEX.                                            | La couleur HEX de votre choix s'affiche. Vous pourrez également choisir l'opacité de la couleur.                                                                                                                                                      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Toujours [prévisualiser et tester]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) votre message avant l'envoi.

{% alert important %}
Certains types de messages dans l'application n'ont pas l'option pour le style au-delà du téléchargement de HTML personnalisé (et/ou CSS et/ou JavaScript) et d'actifs via ZIP, comme décrit dans les étapes ci-dessus. [Web Modal avec CSS]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css) vous permet de télécharger ou d'écrire des CSS personnalisés pour créer de la beauté, tout autour de la messagerie personnalisée.
{% endalert %}

## Étape 6 : Configurer des paramètres supplémentaires

### Paires clé-valeur

Ajouter [paires clé-valeur][19] pour envoyer des champs personnalisés supplémentaires aux appareils utilisateurs.

### Réévaluer l'éligibilité de la campagne et la liquidité

Dans certains scénarios, vous pouvez vouloir réévaluer l'éligibilité d'un utilisateur qui déclenche un message dans l'application à afficher. Des exemples incluent des campagnes qui ciblent un attribut personnalisé qui change fréquemment ou des messages qui devraient refléter toute modification de profil de dernière minute.

!\[Réévaluer l'adhésion IAM \]\[27\]

Lorsque vous sélectionnez **Ré-évaluer l'éligibilité de la campagne avant d'afficher**, une demande supplémentaire sera faite à Braze pour confirmer que l'utilisateur est toujours éligible pour ce message avant l'envoi. De plus, toutes les variables [Liquid][25] ou [Contenu Connecté][26] seront gabarites à ce moment-là avant que le message ne soit affiché.

{% alert note %}
L'activation de cette option entraînera un léger délai (< 100 ms) entre le moment où un utilisateur déclenche un message dans l'application et le moment où le message est affiché en raison de l'admissibilité ajoutée et de la demande de template. <br><br> N'utilisez pas cette option pour les messages qui peuvent être déclenchés lorsqu'un utilisateur est hors ligne ou quand l'éligibilité et la réévaluation Liquid ne sont pas requises.
{% endalert %}

## Étape 7 : Construisez le reste de votre campagne ou Canvas

Construisez le reste de votre campagne ou de Canvas ; voir les sections ci-dessous pour de plus amples conseils sur la meilleure façon d'utiliser nos outils pour construire des messages dans l'application. Pour plus d'informations sur les options de messagerie spécifiques à Canvas dans l'application, comme l'expiration et les étapes, reportez-vous à [Messages In-app dans Canvas][16].

### Déclenchement

Sélectionnez l'action dont vous souhaitez déclencher votre message, ainsi que les heures de début et de fin pour votre campagne ou Canvas.

{% alert important %}
Veuillez noter que si vous avez l'intention de déclencher votre message dans l'application basé sur un événement personnalisé, cet événement personnalisé doit être envoyé via le SDK.
{% endalert %}

![Planifier]({% image_buster /assets/img_archive/in_app_schedule.png %}){: style="largeur-max-80%"}

L'envoi de messages dans l'application est entièrement basé sur les déclencheurs d'action suivants :
- Faire un achat
- Ouverture de l'app/page web
- Effectuer un événement personnalisé (ne fonctionne qu'avec les événements envoyés via le SDK)
- Ouverture d'un message push spécifique
- Planifier automatiquement les campagnes à envoyer à un certain moment par rapport à l'heure locale de chacun de vos utilisateurs.
- Les messages peuvent également être configurés pour se reproduire sur une base journalière, hebdomadaire (optionnellement sur certains jours) ou mensuelle.

Une date et une heure de début doivent être sélectionnées ; cependant, une date de fin est facultative. Une date de fin empêchera ce message spécifique dans l'application d'apparaître sur les appareils après la date/heure spécifiée.

Veuillez vous référer à notre documentation de développeurs pour [déclencher un événement côté serveur]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/) et [envoyer des messages locaux dans l'application]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#local-in-app-messages).

#### Déclenchement en ligne vs. hors ligne

Les messages intégrés fonctionnent en envoyant le message et se déclenche sur l'appareil de l'utilisateur. Une fois que les messages intégrés sont sur un appareil, il attend de s'afficher jusqu'à ce que la condition de déclenchement soit remplie. Si les messages dans l'application sont déjà mis en cache sur l'appareil de l'utilisateur, vous pouvez même déclencher des messages dans l'application hors ligne sans connexion à Braze (par exemple, en mode avion).

{% alert important %}
Une fois qu'une campagne de message intégré a été arrêtée, il se peut que certains utilisateurs aient déjà reçu le message mais ne l'ont pas vu parce qu'ils n'ont pas ouvert votre application. Ces utilisateurs verront toujours votre message dans l'application et seront considérés comme une impression unique, même après l'arrêt de votre campagne.
{% endalert %}

### Prioriser

{% tabs %}
{% tab Campaigns %}

Enfin, une fois que vous aurez sélectionné l'action déclenchée par le message dans l'application, vous devriez également définir une priorité. Si deux messages sont déclenchés par la même action, les messages de haute priorité seront programmés pour apparaître sur les appareils des utilisateurs avant les messages avec des priorités plus faibles.

![Priorité de l'événement]({% image_buster /assets/img_archive/prioritization_options.png %}){: style="largeur-max-80%"}

Les options hautes, moyennes et basses pour les priorités de messages déclenchés sont des segments, et comme cela plusieurs messages peuvent avoir la même priorité sélectionnée. Pour définir des priorités dans ces segments, cliquez sur __Définir la priorité exacte__, et vous serez en mesure de faire glisser et déposer des campagnes pour les ordonner avec la bonne priorité.

![Priorisation du seau]({% image_buster /assets/img_archive/bucket_prioritization.png %}){: style="largeur-max-70%"}

{% endtab %}
{% tab Canvas %}

Un client peut déclencher deux messages dans l'application en même temps sur votre Canvas Lorsque cela se produit, Braze suivra l'ordre de priorité ci-dessous pour déterminer quel message dans l'application est affiché. Faites glisser les différentes étapes de Canvas pour réorganiser leur priorité. Par défaut, les étapes précédentes dans une variante de Canvas s'afficheront avant les étapes suivantes.

![priorité_étape]({% image_buster /assets/img_archive/step_priority.png %}){: style="largeur-max-80%"}

Naviguez vers **Envoyer les paramètres** de la section Canvas pour prioriser les messages dans l'application à partir d'un Canvas par rapport aux messages dans l'application provenant d'autres Canvases et campagnes.

Par défaut, la priorité de l'étape Canvas est définie sur médium, les étapes les plus récentes ayant la priorité relative la plus élevée. Les priorités au niveau de la toile et de la campagne sont également par défaut, avec la priorité relative la plus élevée par défaut par rapport aux éléments les plus récemment créés.

![priorité_canas]({% image_buster /assets/img_archive/canvas_priority.png %}){: style="largeur-max-70%"}

{% endtab %}
{% endtabs %}

### Target segment

Ensuite, vous devez choisir le segment cible dans le menu déroulant. Vous recevez automatiquement un instantané de ce à quoi ressemble cette population approximative de segments. Gardez à l'esprit que l'adhésion exacte au segment est toujours calculée juste avant l'envoi du message.

![Target Page]({% image_buster /assets/img_archive/target_page.png %}){: style="largeur-max:50%"}

{% alert note %}
S'il y a un délai à l'étape de message dans l'application, l'adhésion au segment sera évaluée après le délai. Si l'utilisateur est éligible, le message dans l'application sera synchronisé lors de la prochaine session disponible.
{% endalert %}

### Événements de conversion

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques (événements de conversion) après avoir reçu une campagne. Vous pouvez spécifier l'une des actions suivantes en tant qu'événement de conversion:

- Ouvre l'application
- Fait un achat (peut être un achat générique ou un article spécifique)
- Effectue un événement spécifique personnalisé

Vous pouvez autoriser jusqu'à une fenêtre de 30 jours au cours de laquelle une conversion sera comptée si l'utilisateur prend l'action spécifiée.

![Événement de conversion]({% image_buster /assets/img_archive/conversion_event_selection.png %}){: style="largeur-max:50%"}

> Une fois que vous avez fini de construire la dernière de votre campagne ou de Canvas, révisez ses détails, puis envoyez-le!

## Limites de campagne de messages actifs dans l'application

Le braze valorise la fiabilité et la vitesse. Tout comme nous vous suggérons d'envoyer uniquement les données dont vous avez besoin à Braze, Nous vous recommandons également de désactiver toutes les campagnes qui n'ajoutent plus aucune valeur à votre marque.

Le traitement des campagnes de messages dans l'application basée sur des actions qui sont toujours dans un état actif mais qui n'envoient plus de messages ou qui ne sont plus nécessaires ralentit la performance globale des services Braze pour vous et d'autres clients. Ce délai supplémentaire est nécessaire pour traiter ces nombreuses campagnes d'inactivité signifie que tous les messages dans l'application prendront plus de temps à apparaître sur les appareils de l'utilisateur final, qui affecte l'expérience de l'utilisateur final.

Il y a une limite de 200 campagnes de messages dans l'application par action par groupe d'applications afin d'optimiser la vitesse de livraison des messages et d'éviter les délais d'attente.

Le nombre de 200 comprend des campagnes IAM actives qui n'ont pas encore atteint l'heure de fin et celles qui n'ont pas de date de fin. Les campagnes IAM actives qui ont passé leurs heures de fin ne seront pas comptées. Le client moyen de Braze a un total de 26 campagnes actives à la fois — il est donc peu probable que cette limitation vous impacte.
[2]: {% image_buster /assets/img/iam-generations.gif %} [24]: {% image_buster /assets/img/iam_compose.gif %} [27]: {% image_buster /assets/img_archive/re-evaluate-iam-membership.png %}

[16]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/
[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported
[19]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/
[25]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[26]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/
