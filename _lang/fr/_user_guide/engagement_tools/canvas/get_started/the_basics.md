---
nav_title: Fondamentaux de Canvas
article_title: Fondamentaux de Canvas
page_order: 1
page_type: reference
description: "Cet article de référence aborde les fondamentaux de Canvas, notamment diverses questions que vous devez vous poser lorsque vous configurez votre premier Canvas."
tool: Canvas

---

# Canvas : Fondamentaux

## Trouvez votre stratégie avec les cinq W de la visualisation

Répondez aux questions suivantes pour commencer :

1. **Que (What)** puis-je faire pour aider le client à mieux comprendre ? (Nom du Canvas)<br><br>

2. **Quand (When)** un utilisateur commencera-t-il cette expérience ? Choisissez l’un des éléments suivants :
    * **Planification** : Entrer les utilisateurs à un moment donné
    * **En fonction de l’action** : Entrer les utilisateurs lorsqu’ils effectuent des actions
      * Effectuer un achat
      * Lancer une session
      * Effectuer un événement personnalisé
      * Saisir un emplacement
      * Interagir ou quitter une autre campagne ou Canvas
    * **Déclenché par un API** (avancé) : Entrer des utilisateurs lorsqu’ils effectuent une action spécifique déclenchant une demande API à Braze
      * Les campagnes déclenchées par API vous donnent la possibilité de stocker le contenu d’un message dans le tableau de bord Braze, en indiquant le moment où un message est envoyé et son destinataire, via votre API.<br><br>

3. **Qui (Who)** essayons-nous de joindre ? (Nom du segment avec filtres facultatifs supplémentaires)
  * Données personnalisées
  * Activité de l’utilisateur
  * Reciblage
  * Activité de marketing
  * Attributs utilisateur
  * Attribution d’installation
  * Activité sociale<br><br>

4. **Pourquoi (Why)** je crée ce Canvas ?
  * **Lancer la session** : Je souhaite qu’ils rejoignent l’application.
  * **Effectuer un achat** : Je souhaite qu’ils effectuent un achat.
  * **Effectuer un événement personnalisé** : Je souhaite qu’ils effectuent une action spécifique pour laquelle je réalise un suivi comme événement personnalisé.
  * Mises à niveau d’application : Je souhaite qu’ils mettent à niveau leur version d’application<br><br>

5. **Où (Where)** devrais-je les contacter ?
  * E-mail
  * Notification push (Android, iOS, Windows, Web)
  * Messages in-app
  * Cartes de contenu
  * SMS ou MMS
  * Webhook<br><br>

6. **How (Comment)** devrais-je les contacter ? (Endroit idéal pour tester les différentes configurations de messagerie)
  * **Timing** : Planifier ou déclencher des messages à l’aide d’outils tels que Timing Intelligent et des délais après le déclenchement d’événements
  * **Cadence et canal** : Utiliser un canal puis un autre ou envoyer plusieurs messages sur plusieurs canaux simultanément
  * **Contenu** : Concevoir une copie créatrice avec plusieurs appels, des propositions de valeur et CTA
  * **Ciblage** : Ajouter des segments supplémentaires et des filtres
  * **Déclencheurs** : Utiliser des actions client pour déclencher des messages

## Anatomie de Canvas

Voici un Overview de l’anatomie d’un Canvas :

{% tabs %}
  {% tab Canvas %}
    **Canvas** fait référence à l’espace de travail et à la visualisation globale.<br><br>
    ![Parcours]({% image_buster /assets/img/Canvas2.png %})
  {% endtab %}

  {% tab Journey %}
    Un **parcours ou parcours client** désigne une expérience utilisateur spécifique dans le Canvas.<br><br>
    ![Parcours pour nouvel utilisateur]({% image_buster /assets/img_archive/Journey_2.png %})
  {% endtab %}

  {% tab Entry Step %}
    **L’étape Entrée** et **L’assistant Entrée** sont les premières étapes que vous exécutez lorsque vous créez votre Canvas. À ce niveau, vous pouvez contrôler la façon dont vos utilisateurs commencent et réalisent leur parcours client.<br><br>
    ![Parcours_3]({% image_buster /assets/img/entry-wizard.gif %})
  {% endtab %}

  {% tab Variants %}
    Les **Variantes** désignent les flux de variantes conçus par les marketeurs, créant des parcours personnalisés.<br><br>
    ![Parcours_3]({% image_buster /assets/img/variants.gif %})
  {% endtab %}

  {% tab Steps %}
    Les **Étapes** désignent des points de décision (tels que des messages) dans une variante.<br><br>
    ![Parcours_4]({% image_buster /assets/img/steps.gif %})
  {% endtab %}
{% endtabs %}

## Création du parcours client dans Canvas

### Nommez votre Canvas : Le « what (quoi) »

Ne sous-estimez jamais le pouvoir du nom. Braze est conçu pour la collaboration, c’est donc le moment idéal pour évaluer la façon dont vous communiquez les objectifs à votre équipe. Vous pouvez ajouter des balises (dont des balises Teams) et nommer les étapes et les variantes dans le Canvas. Pour en savoir plus sur les parcours client, consultez notre Cours d’apprentissage Braze sur le [mappage des cycles de vie utilisateur](https://learning.braze.com/mapping-customer-lifecycles) !

### Créer des conditions de démarrage : Le « When » (quand)

Quand un client accédera-t-il à ce Canvas ? Les utilisateurs peuvent accéder à votre Canvas de 2 façons : par une planification ou des déclencheurs basés sur une action.

| Planification | En fonction de l’action |
|---|---|
|Vous pouvez planifier une livraison lorsque vous souhaitez envoyer un Canvas immédiatement à votre audience cible, l’envoyer régulièrement ou planifier l’envoi à un moment spécifique dans le futur. | Ces Canvas répondent à des comportements des clients spécifiques, lorsqu’ils se produisent. Ces déclencheurs basés sur une action peuvent inclure l’ouverture de votre application, un achat effectué, l’interaction avec une autre campagne ou le déclenchement d’un événement personnalisé. |
{: .reset-td-br-1 .reset-td-br-2}

### Sélectionnez une audience d’entrée pour l’entrée : Le « who » (qui)

Qui (Who) essayez-vous de joindre ? À ce niveau, vous pouvez utiliser un segment prédéfini et ajouter d’autres filtres. Les filtres comprennent les éléments suivants :

| Filtre | Description |
|---|---|
| Données personnalisées | Les filtres Données personnalisées vous permettent de segmenter des utilisateurs en fonction d’événements et d’attributs que vous définissez. Ils vous permettent d’utiliser des fonctionnalités spécifiques pour votre produit. |
| Activité de l’utilisateur | Les filtres Activité de l’utilisateur vous permettent de segmenter des clients en fonction de leurs actions et achats. |
| Reciblage | Les filtres Reciblage vous permettent de segmenter des clients ayant été transférés, reçus ou ayant interagi avec des campagnes ou Canvas précédent(e)s. |
| Activité de marketing | Les filtres Marketing segmentent les clients en fonction de comportements universels, tels que le dernier engagement ou les campagnes reçues. |
| Attributs utilisateur | Les filtres Attribut utilisateur segmentent les clients en fonction de leurs caractéristiques et attributs constants. |
| Attribution d’installation | Les filtres Attribution d’installation segmentent les clients en fonction de leur première source, groupe d’annonces, campagne ou annonce. |
| Activité sociale | Les filtres Activité sociale segmentent les clients en fonction de leur activité sur les réseaux sociaux, à savoir leur connexion à Facebook et Twitter. |
{: .reset-td-br-1 .reset-td-br-2}

Seuls les utilisateurs répondant à ces critères d’audience cible peuvent accéder au parcours.

### Identifier des événements de conversion : Le « why » (pourquoi)

Pourquoi créez-vous ce Canvas ? Il est toujours important d’avoir un objectif défini en tête et Canvas vous permet de comprendre comment vous vous situez par rapport aux KPI tels que l’engagement de session, les achats et les événements personnalisés.

Sélectionnez au moins un événement de conversion pour pouvoir comprendre vos performances de campagne et optimiser vos performances dans le Canvas, comme si votre Canvas avait plusieurs variantes et/ou un groupe de contrôle Braze utilisait l’événement de conversion pour déterminer la meilleure variante pour atteindre cet objectif.

### Consolider l’expérience : Le « how » (comment) et « where » (où)

1. **Configuration de variantes** : Une variante désigne la piste que chaque utilisateur suit sur son parcours. Canvas prend en charge jusqu’à huit variantes avec un groupe de contrôle. Bien que cela ne soit pas nécessaire, vous pouvez nommer chaque variante et contrôler la répartition de l’audience cible, suivant chaque variante.

2. **Création d’étapes** : Une étape désigne un point de décision marketing, quelle expérience créez-vous ? Dans une étape, vous pouvez définir des déclencheurs ou planifier une livraison, affiner le ciblage en ajoutant des filtres ou en marquant des [événements d’exception][1] et ajouter des canaux à partir d’e-mails, notifications push et webhooks.

3. **Déterminer quand et comment utiliser des étapes et des variantes :** Chaque Canvas doit avoir au moins une variante et au moins une étape. Il n’y a pas de limites, comment définissez-vous donc la forme de votre Canvas ? C’est à ce niveau que vos objectifs, données et hypothèses entrent en jeu. La réflexion « how » (comment) et « where » (où) vous aidera à tracer la forme appropriée et la structure de votre Canvas. Vous pouvez utiliser deux approches :
    - **Travailler à contresens** : Certains objectifs ont des sous-objectifs identiques. Par exemple, si votre objectif est de convaincre un utilisateur libre de souscrire, vous aurez besoin d’un document indiquant vos services d’abonnement. Un visiteur doit voir les options avant d’acheter. Vous devez mettre en avant cette page avant une page de paiement. Travailler à contresens pour comprendre le parcours d’un client va de pair avec la réalisation de votre objectif, élément clé pour la conversion.
    - **Commencer par le statu quo et ajouter des éléments** : Avez-vous déjà réalisé une campagne identique dans le passé ? Ou est-ce la première que vous menez ? Utilisez un message et ajoutez-en d’autres. Essayez un nouveau filtre ou ajoutez un message de réponse. Examinez vos performances et continuez à optimiser en apportant des modifications progressives.
    - **Regarder les autres** : L’imitation est la plus grande forme de flatterie. Ne réinventez pas la roue. N’ayez crainte, nous avons une solution. À la fin de ce guide, vous trouverez des caractéristiques essentielles qui vous aideront à démarrer.


[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events/
