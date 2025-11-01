---
nav_title: FAQ
article_title: FAQ sur les campagnes
page_order: 10
page_type: FAQ
description: "Cette page fournit des réponses aux questions fréquemment posées sur les campagnes."
tool: Campaigns

---

# Questions fréquemment posées

> Cet article apporte des réponses à certaines questions fréquemment posées sur les campagnes.

### Comment créer une campagne multicanal ?

Pour créer une campagne multicanale, sélectionnez **Messagerie** > Campagnes. Sélectionnez ensuite **Créer une campagne** > **Multicanal**. À partir de là, vous pouvez sélectionner l'un des canaux de communication suivants : Cartes de contenu, e-mail, LINE, notifications push, SMS/MMS/RCS, webhook ou WhatsApp.

### Puis-je ajouter un groupe de contrôle à ma campagne multicanal ?

Non, les groupes de contrôle dans les campagnes sont destinés à la diffusion de messages sur un seul canal, comme l'e-mail A par rapport à l'e-mail B. En revanche, essayez d'utiliser [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas) pour tester différents canaux, contenus d'envoi de messages et délais de réception/distribution. 

### Comment puis-je commencer à tester et à optimiser mes campagnes ?

Les campagnes multivariées et les Canvas en cours d'exécution avec plusieurs variantes sont une excellente façon de commencer ! Par exemple, vous pouvez lancer une [campagne multivariée]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) pour tester un message avec différentes copies ou lignes d'objet. Les toiles comportant plusieurs variantes peuvent permettre de tester des flux de travail entiers.

### Pourquoi le taux d'ouverture de ma campagne a-t-il diminué ?

Un taux d'ouverture faible n'est pas toujours lié à un problème technique. Il peut y avoir des problèmes de découpage des e-mails, ce qui entraîne l'absence d'un pixel de suivi. Cependant, il est également possible que moins d'utilisateurs ouvrent leurs e-mails en raison du contenu ou de l'évolution de la taille de l'audience. 

### Comment les audiences des campagnes sont-elles évaluées ?

Par défaut, les campagnes vérifient les filtres d'audience au moment de la saisie. Pour les campagnes basées sur l'action avec un délai, il existe une option permettant de réévaluer les critères de segmentation au moment de l'envoi afin de s'assurer que les utilisateurs font toujours partie de l'audience cible au moment de l'envoi du message. 

### Pourquoi y a-t-il une différence entre le nombre de destinataires uniques et le nombre d'envois pour une campagne ou un canvas donné ?

Une explication possible pourrait être que la campagne ou Canvas a activé la rééligibilité, ce qui signifie que les utilisateurs qui se qualifient pour le segment et les paramètres de réception/distribution seront en mesure de recevoir le message plus d'une fois. Si la rééligibilité n'est pas activée, l'explication probable de la différence entre les envois et les destinataires uniques peut être due au fait que les utilisateurs ont plusieurs appareils, à travers les plateformes, associés à leurs profils. 

Par exemple, si vous avez un Canvas qui a des notifications push iOS et web, un utilisateur donné avec des appareils mobiles et de bureau pourrait recevoir plus d'un message.

### Pourquoi ma campagne a-t-elle une base d'utilisateurs atteignables plus petite que le segment que j'utilise pour la campagne ?

Si vous avez mis en place un [groupe de contrôle global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/), celui-ci empêchera un pourcentage de votre audience atteignable de recevoir des campagnes. Cela signifie que le nombre d'utilisateurs joignables pour votre segment peut parfois être plus important que le nombre d'utilisateurs joignables pour votre campagne, même si la campagne utilise ce même segment.

### Qu'offre la réception/distribution locale ?

La diffusion selon le fuseau horaire local vous permet d'envoyer des campagnes de messages à un segment en fonction du fuseau horaire de l'utilisateur. Sans réception/distribution locale, les campagnes seront planifiées en fonction des paramètres du fuseau horaire de votre entreprise dans Braze. 

Par exemple, une entreprise basée à Londres qui envoie une campagne à 12 heures atteindra les utilisateurs de la côte ouest de l'Amérique à 4 heures du matin. Si votre application n'est disponible que dans certains pays, vous ne courez peut-être aucun risque. Dans le cas contraire, nous vous recommandons vivement d'éviter d'envoyer des notifications push tôt le matin à votre base d'utilisateurs.

### Comment Braze reconnaît-il le fuseau horaire d'un utilisateur ?

Braze déterminera automatiquement le fuseau horaire d'un utilisateur à partir de son appareil. Cela garantit la précision du fuseau horaire et la couverture complète de vos utilisateurs. Les utilisateurs créés par le biais de l'API utilisateur ou autrement sans fuseau horaire auront le fuseau horaire de votre entreprise comme fuseau horaire par défaut jusqu'à ce qu'ils soient reconnus dans votre application par le SDK. 

Vous pouvez vérifier le fuseau horaire de votre entreprise dans les [paramètres de]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/) votre [entreprise]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/) sur le tableau de bord.

### Quand Braze évalue-t-il les utilisateurs pour la diffusion selon l'heure/distribution locale ?

Pour la diffusion selon l'heure/distribution locale, Braze évalue l'éligibilité des utilisateurs à l'entrée au cours de ces deux instances :

- A l'heure de Samoa (UTC+13) du jour planifié
- À l'heure locale du jour planifié

Pour qu'un utilisateur soit éligible à la participation, il doit être éligible aux deux contrôles. Par exemple, si le lancement d'un Canvas est planifié pour le 7 août 2021 à 14 heures, fuseau horaire local, le ciblage d'un utilisateur situé à New York nécessiterait les vérifications d'éligibilité suivantes :

- New York le 6 août 2021 à 21 heures
- New York le 7 août 2021 à 14 heures

Notez que l'utilisateur doit se trouver dans le segment pendant les 24 heures précédant le lancement. Si l'utilisateur n'est pas éligible lors de la première vérification, Braze ne tentera pas la deuxième vérification.

Par exemple, si une campagne est planifiée pour être diffusée à 19 heures UTC, nous commençons à mettre en file d'attente les envois de la campagne dès qu'un fuseau horaire est identifié (comme Samoa). Cela signifie que nous nous préparons à envoyer le message, et non à envoyer la campagne. Si les utilisateurs ne correspondent à aucun filtre lorsque nous vérifions leur éligibilité, ils ne feront pas partie de l'audience cible.

Prenons un autre exemple : vous souhaitez créer deux campagnes dont l'envoi est planifié le même jour, l'une le matin et l'autre le soir, et ajouter un filtre selon lequel les utilisateurs ne peuvent recevoir la deuxième campagne que s'ils ont déjà reçu la première. Selon l'heure/distribution locale, il se peut que certains utilisateurs ne reçoivent pas la deuxième campagne. En effet, nous vérifions l'éligibilité lorsque le fuseau horaire de l'utilisateur est identifié. Par conséquent, si l'heure planifiée n'a pas encore eu lieu dans son fuseau horaire, il n'a pas reçu la première campagne, ce qui signifie qu'il ne sera pas éligible pour la deuxième campagne.

### Comment puis-je planifier une campagne sur un fuseau horaire local ?

Lors de la planification d'une campagne, choisissez de l'envoyer à une heure donnée, puis sélectionnez **Envoyer la campagne aux utilisateurs dans leur fuseau horaire local**.

Braze recommande vivement que toutes les campagnes concernant les fuseaux horaires locaux soient planifiées 24 heures à l'avance. Étant donné qu'une telle campagne doit être envoyée sur une journée entière, la planifier 24 heures à l'avance permet de s'assurer que votre message atteindra l'ensemble de votre segmentation. Toutefois, vous pouvez planifier ces campagnes moins de 24 heures à l'avance si nécessaire. N'oubliez pas que Braze n'enverra pas de messages aux utilisateurs qui ont dépassé l'heure d'envoi de plus d'une heure. 

Par exemple, s'il est 13 heures et que vous planifiez une campagne pour un fuseau horaire local à 15 heures, la campagne sera immédiatement envoyée à tous les utilisateurs dont l'heure locale se situe entre 15 heures et 16 heures, mais pas à ceux dont l'heure locale est 17 heures. En outre, l'heure d'envoi que vous choisissez pour votre campagne ne doit pas encore avoir eu lieu dans le fuseau horaire de votre entreprise.

Modifier une campagne sur un fuseau horaire local programmée moins de 24 heures à l'avance ne modifiera pas la planification du message. Si vous décidez de modifier une campagne portant sur un fuseau horaire local pour l'envoyer à une heure plus tardive (par exemple, 19 heures au lieu de 18 heures), les utilisateurs qui faisaient partie du segment ciblé lorsque l'heure d'envoi initiale a été choisie recevront toujours le message à l'heure d'origine (18 heures). Si vous modifiez un fuseau horaire local pour que l'envoi se fasse plus tôt (par exemple, 16 heures au lieu de 17 heures), la campagne sera toujours envoyée à tous les membres du segment à l'heure d'origine (17 heures). 

{% alert note %}
Pour les composants Canvas, les utilisateurs n'ont pas besoin d'être dans le composant pendant 24 heures pour recevoir le composant suivant dans le parcours de l'utilisateur pour une réception/distribution selon l'heure locale.
{% endalert %}

Si vous avez autorisé les utilisateurs à redevenir éligibles pour la campagne, ils la recevront à nouveau à l'heure initiale (17 heures). Pour toutes les occurrences ultérieures de votre campagne, cependant, vos messages ne sont envoyés qu'à l'heure que vous avez mise à jour.

### Quand les changements apportés aux campagnes de fuseaux horaires locaux prennent-ils effet ?

Les segments cibles pour les campagnes sur les fuseaux horaires locaux doivent inclure une fenêtre d'au moins 48 heures pour tout filtre basé sur l'heure afin de garantir la réception/distribution à l'ensemble du segment. Prenons l'exemple d'un segment ciblant les utilisateurs au cours de leur deuxième jour, avec les filtres suivants :

- Première utilisation de l'application il y a plus d'un jour
- Première utilisation il y a moins de 2 jours

La diffusion selon l'heure/distribution locale peut manquer aux utilisateurs de ce segment en fonction de l'heure de livraison et du fuseau horaire local de l'utilisateur. En effet, un utilisateur peut quitter le segment au moment où son fuseau horaire déclenche la réception/distribution.

### Quelles modifications puis-je apporter aux campagnes planifiées avant leur lancement ?

Lorsque la campagne est planifiée, les modifications autres que la composition du message doivent être effectuées avant la mise en file d'attente des messages à envoyer. Comme pour toutes les campagnes, vous ne pouvez pas modifier les événements de conversion une fois qu'ils ont été lancés.

### J'ai mis à jour ma campagne planifiée. Pourquoi n'a-t-il pas été lancé ?

Cela peut se produire lorsqu'une campagne est planifiée pour être lancée à l'heure exacte où elle a été mise à jour. Par exemple, s'il est actuellement 15 h 10 et que vous avez modifié la campagne pour la lancer à 15 h 10 et sélectionné **Mettre à jour la campagne**, il est maintenant plus de 15 h 10, ce qui signifie que l'heure prévue pour le lancement est passée. Au lieu de planifier la campagne au même moment, sélectionnez **Envoyer dès le lancement de la campagne**.

### Quelle est la "zone de sécurité" avant que les messages d'une campagne de planification ne soient mis en file d'attente ?

Nous vous recommandons de modifier les messages dans les délais suivants :

- **Campagnes à planification unique :** Modifier jusqu'à l'heure d'envoi planifiée.
- **Campagnes planifiées récurrentes :** Modifier jusqu'à l'heure d'envoi planifiée.
- **Campagnes d'envoi local :** Modifiez jusqu'à 24 heures avant l'heure d'envoi planifiée.
- **Campagnes d'envoi optimales :** Modifiez jusqu'à 24 heures avant le jour où l'envoi de la campagne est planifié.

Si vous apportez des modifications à votre message en dehors de ces recommandations, il se peut que les mises à jour ne soient pas reflétées dans le message envoyé. Par exemple, si vous modifiez l'heure d'envoi trois heures avant une campagne dont l'envoi est planifié à 12 heures, heure locale, la situation suivante peut se produire :

- Braze n'enverra pas de messages aux utilisateurs qui ont dépassé l'heure d'envoi de plus d'une heure.
- Les messages pré-enregistrés peuvent toujours être envoyés à l'heure initialement prévue, plutôt qu'à l'heure Adjust.

Si vous devez apporter des modifications, nous vous recommandons d'arrêter la campagne en cours (ce qui annulera tous les messages en file d'attente). Vous pouvez ensuite dupliquer la campagne, apporter les modifications nécessaires et lancer la nouvelle campagne. Vous devrez peut-être exclure de cette campagne les utilisateurs qui ont déjà reçu la première campagne. Veillez à réajuster les heures de planification de la campagne pour tenir compte de l'envoi par fuseau horaire.

### Pourquoi le nombre d'utilisateurs entrant dans une campagne ne correspond-il pas au nombre attendu ?

Le nombre d'utilisateurs entrant dans une campagne peut être différent de celui que vous attendiez en raison de la manière dont les audiences et les déclencheurs sont évalués. Dans Braze, une audience est évaluée avant le déclencheur (à moins d'utiliser un déclencheur de [changement d'attribut]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value) ). Ainsi, les utilisateurs seront exclus de la campagne s'ils ne font pas initialement partie de votre audience sélectionnée avant que les actions déclencheurs ne soient évaluées.

{% alert tip %}
Pour obtenir de l'aide dans la résolution des problèmes liés aux campagnes, contactez le service d'assistance de Braze dans les 30 jours suivant l'apparition de votre problème, car nous ne disposons que des journaux de diagnostic des 30 derniers jours.
{% endalert %}

### Quelle est la différence entre les options CSV Export User Data et CSV Export Email Address sur la page d'analyse/analytique de ma campagne ?

En sélectionnant l'option **CSV Export Email Addresses**, vous ne téléchargerez que les données relatives aux utilisateurs disposant d'une adresse e-mail. Par exemple, si vous avez un segment de 100 000 utilisateurs, mais que seuls 50 000 d'entre eux ont une adresse e-mail, et que vous cliquez sur **CSV Exporter les adresses e-mail**, vous devez vous attendre à ne voir que 50 000 lignes de données dans le fichier CSV. En revanche, la sélection de l'option **CSV Export User Data (Exporter les données de l'utilisateur)** exportera toutes les données de l'utilisateur.

### Puis-je rechercher une campagne par son identifiant API ?

Oui, utilisez le filtre `api_id:YOUR_API_ID` sur la page **Campagnes** pour rechercher une campagne par son identifiant API. Pour en savoir plus, reportez-vous à la rubrique ["Recherche de campagnes"]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/).

### Quelle est la différence entre les campagnes API et les campagnes déclenchées par l'API ?

Les campagnes déclenchées par API vous permettent de gérer le texte de la campagne, les tests multivariés et les règles de rééligibilité dans le tableau de bord de Braze, tout en déclenchant la réception/distribution de ce contenu à partir de vos propres serveurs et systèmes. Ces messages peuvent également contenir des données supplémentaires à intégrer en temps réel dans les messages.

Les campagnes API sont utilisées pour suivre les messages envoyés à l'aide de l'API. Contrairement à la plupart des campagnes, vous ne spécifiez pas le message, les destinataires ou la planification, mais vous transmettez les identifiants dans vos appels API. 

### Quelle est la différence entre les campagnes basées sur des actions et les campagnes déclenchées par l'API ?

<style>
table th:nth-child(1) {
    width: 50%;
}
table th:nth-child(3) {
    width: 50%;
}
</style>

#### Basé sur l'action

Les campagnes de réception/distribution basées sur des actions ou des événements sont très efficaces pour les messages transactionnels ou basés sur des réalisations et vous permettent de déclencher leur envoi après qu'un utilisateur a accompli un certain événement. 

| Pour | Cons | 
| ---- | ---- |
| \- Visibilité des charges utiles JSON entrantes dans la plate-forme (si l'événement est déclenché par l'utilisateur test) via le **journal des activités déclenchées par les messages.**<br><br>\- Les éléments de personnalisation sont inclus dans les propriétés de l'événement personnalisé.<br><br>\- L'événement personnalisé peut être utilisé pour créer des segments d'utilisateurs éligibles pour le message. | \- Consomme des points de données |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Déclenché par l'API

Les campagnes déclenchées par l'API et par le serveur sont idéales pour traiter des transactions plus avancées, vous permettant de déclencher la réception/distribution du contenu de la campagne à partir de vos propres serveurs et systèmes. La demande d'API pour déclencher le message peut également inclure des données supplémentaires qui seront intégrées au message en temps réel.

| Avantages | Considérations | 
| ---- | ---- |
| \- N'enregistre pas de points de données<br><br>\- Les éléments de personnalisation sont inclus dans les propriétés de la charge utile JSON | \- Ne vous permet pas de créer un segment d'utilisateurs éligibles pour le message dans les propriétés de l'envoi JSON.<br><br>\- Impossible de voir les charges utiles JSON entrantes avec le **journal d'activité des messages**|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

