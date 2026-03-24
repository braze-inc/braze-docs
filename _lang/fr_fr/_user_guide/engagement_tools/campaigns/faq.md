---
nav_title: FAQ
article_title: FAQ sur les campagnes
page_order: 10
page_type: FAQ
description: "Le présent article fournit des réponses aux questions fréquemment posées sur les campagnes."
tool: Campaigns

---

# Foire aux questions

> Cet article fournit des réponses à des questions fréquemment posées sur les campagnes.

### Comment créer une campagne multicanal ?

Pour créer une campagne multicanale, sélectionnez **Messagerie** > **Campagnes**. Sélectionnez ensuite **Créer une campagne** > **Multicanal**. À partir de là, vous pouvez choisir parmi les canaux de communication suivants : Cartes de contenu, e-mail, LINE, notifications push, SMS/MMS/RCS, webhook ou WhatsApp.

### Puis-je ajouter un groupe de contrôle à ma campagne multicanal ?

Non, les groupes de contrôle dans les campagnes sont conçus pour les messages à canal unique, comme l'e-mail A par rapport à l'e-mail B. Comme alternative, essayez d'utiliser [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas) pour tester différents canaux, contenus de message et horaires de distribution. 

### Comment puis-je commencer à tester et optimiser les campagnes ?

Les campagnes multivariées et l'exécution de Canvas avec plusieurs variantes sont un excellent point de départ ! Par exemple, vous pouvez lancer une [campagne multivariée]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) pour tester un message avec différentes copies ou lignes d'objet. Les Canvas comportant plusieurs variantes permettent quant à eux de tester des flux de travail entiers.

### Pourquoi le taux d'ouverture de ma campagne a-t-il baissé ?

De faibles taux d'ouverture ne sont pas forcément liés à un problème technique. Il peut y avoir des problèmes liés à l'écrêtage d'un e-mail, entraînant la disparition d'un pixel de suivi. Il est cependant également possible que moins d'utilisateurs ouvrent leurs e-mails en raison de changements de contenu ou de taille d'audience. 

### Comment les audiences de la campagne sont-elles évaluées ?

Par défaut, les campagnes vérifient les filtres d'audience au moment de l'entrée. Pour les campagnes par événement disposant d'un délai, il existe une option pour réévaluer les critères de segmentation au moment de l'envoi, afin de s'assurer que les utilisateurs font toujours partie de l'audience cible lorsque le message est envoyé. 

### Pourquoi y a-t-il une différence entre le nombre de destinataires uniques et le nombre d'envois pour une campagne ou un Canvas donné ?

Une explication possible est que la campagne ou le Canvas a la rééligibilité activée, ce qui signifie que les utilisateurs qui remplissent les conditions du segment et les paramètres de distribution peuvent recevoir le message plus d'une fois. Si la rééligibilité n'est pas activée, la différence entre les envois et les destinataires uniques s'explique probablement par le fait que certains utilisateurs possèdent plusieurs appareils, sur différentes plateformes, associés à leurs profils. 

Par exemple, si vous avez un Canvas qui comporte à la fois des notifications push iOS et web, un utilisateur possédant à la fois un téléphone et un ordinateur de bureau peut recevoir plus d'un message.

### Pourquoi le nombre de conversions peut-il dépasser le nombre d'utilisateurs uniques pour les campagnes multicanales ?

Pour les campagnes multicanales, Braze comptabilise les conversions par canal et non par utilisateur. Lorsqu'un utilisateur effectue une seule action de conversion dans la fenêtre de conversion, Braze attribue cette conversion à chaque canal par lequel l'utilisateur a reçu un message. Cela signifie que si un utilisateur reçoit des messages sur plusieurs canaux (par exemple, à la fois par e-mail et par notification push) et effectue une conversion, Braze comptabilise plusieurs conversions, une pour chaque canal. Par conséquent, le nombre total de conversions peut dépasser le nombre d'utilisateurs uniques ayant effectué une conversion.

Par exemple, si une campagne multicanal envoie à la fois un e-mail et une notification push à un utilisateur, et que cet utilisateur effectue une action de conversion après avoir reçu les deux messages et dans la fenêtre de conversion, Braze compte cela comme deux conversions : l'une attribuée à l'e-mail et l'autre à la notification push, même s'il s'agit d'une seule action effectuée par le même utilisateur.

### Pourquoi ma campagne a-t-elle une base d'utilisateurs atteignable plus petite que le segment que j'utilise pour cette campagne ?

Si vous avez configuré un [groupe de contrôle global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/), un pourcentage de votre audience atteignable sera exclu de la réception des campagnes. Cela signifie que le nombre d'utilisateurs atteignables pour votre segment peut parfois être supérieur au nombre d'utilisateurs atteignables pour votre campagne, même si la campagne utilise ce même segment.

### Que propose la livraison selon le fuseau horaire local ?

La livraison selon le fuseau horaire local vous permet d'envoyer des campagnes de communication à un segment en fonction du fuseau horaire individuel de chaque utilisateur. Sans cette option, les campagnes seront planifiées en fonction des paramètres de fuseau horaire de votre société dans Braze. 

Par exemple, une société basée à Londres qui envoie une campagne à midi atteindra les utilisateurs sur la côte ouest de l'Amérique à 4 h du matin. Si votre application n'est disponible que dans certains pays, cela ne pose peut-être pas de problème. Dans le cas contraire, nous vous recommandons vivement d'éviter d'envoyer des notifications push tôt le matin à votre base d'utilisateurs.

### Comment Braze détermine-t-il le fuseau horaire d'un utilisateur ?

Braze détermine automatiquement le fuseau horaire d'un utilisateur à partir de son appareil. Cela garantit une précision de fuseau horaire et une couverture complète de vos utilisateurs. Les utilisateurs créés via l'API utilisateur ou n'ayant pas de fuseau horaire se verront attribuer celui de votre entreprise comme fuseau horaire par défaut, jusqu'à ce qu'ils soient identifiés dans votre application par le SDK. 

Vous pouvez vérifier le fuseau horaire de votre entreprise dans vos [paramètres de l'entreprise]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/) sur le tableau de bord.

### Quand Braze évalue-t-il les utilisateurs pour la livraison selon un fuseau horaire local ?

Braze évalue l'éligibilité des utilisateurs à l'entrée aux moments suivants :

- Heure des Samoa (UTC+13) ou UTC+14 pendant l'heure d'été
- L'heure locale du jour de la planification

Pour qu'un utilisateur soit éligible à l'entrée, il doit remplir les conditions lors des deux vérifications. Par exemple, si un Canvas est prévu pour être lancé le 7 août 2021 à 14 h en fuseau horaire local, cibler un utilisateur situé à New York nécessite les vérifications d'éligibilité suivantes :

- New York, le 6 août 2021 à 21 h
- New York, le 7 août 2021 à 14 h

L'utilisateur doit être dans le segment pendant 24 heures avant le lancement. Si l'utilisateur n'est pas éligible lors de la première vérification, Braze ne procède pas à la deuxième.

Par exemple, si une campagne est planifiée pour une distribution à 19 h UTC, nous commençons à placer les envois de la campagne en file d'attente dès qu'un fuseau horaire est identifié (par exemple, les Samoa). Cela signifie que nous nous préparons à envoyer le message, pas que nous l'envoyons effectivement. Si les utilisateurs ne correspondent à aucun filtre au moment de la vérification d'éligibilité, ils ne feront pas partie de l'audience cible.

Autre exemple : imaginons que vous souhaitiez créer deux campagnes planifiées pour le même jour, une le matin et une le soir, avec un filtre stipulant que les utilisateurs ne peuvent recevoir la deuxième campagne que s'ils ont déjà reçu la première. Avec la livraison selon le fuseau horaire local, certains utilisateurs pourraient ne pas recevoir la seconde campagne. En effet, l'éligibilité est vérifiée lorsque le fuseau horaire de l'utilisateur est identifié. Si l'heure planifiée n'a pas encore eu lieu dans son fuseau horaire, il n'a pas reçu la première campagne et ne sera donc pas éligible pour la deuxième.

### Comment planifier une campagne selon un fuseau horaire local ?

Lors de la planification d'une campagne, choisissez de l'envoyer à une heure donnée, puis sélectionnez **Envoyer la campagne aux utilisateurs dans leur fuseau horaire local**.

Braze recommande vivement de planifier toutes les campagnes en fuseau horaire local 24 heures à l'avance. Étant donné qu'une telle campagne doit être envoyée sur une journée entière, la planifier 24 heures à l'avance permet de s'assurer que votre message atteindra l'ensemble de votre segment. Cependant, vous pouvez planifier ces campagnes moins de 24 heures à l'avance si nécessaire. N'oubliez pas que Braze n'enverra pas de messages aux utilisateurs qui ont dépassé l'heure d'envoi de plus d'une heure. 

Par exemple, s'il est 13 h et que vous planifiez une campagne en fuseau horaire local pour 15 h, la campagne sera envoyée immédiatement à tous les utilisateurs dont l'heure locale est comprise entre 15 h et 16 h, mais pas aux utilisateurs dont l'heure locale est 17 h. De plus, l'heure d'envoi que vous choisissez pour votre campagne ne doit pas encore être dépassée dans le fuseau horaire de votre société.

La modification d'une campagne en fuseau horaire local programmée moins de 24 heures à l'avance ne modifiera pas la planification du message. Si vous décidez de modifier une campagne en fuseau horaire local pour qu'elle soit envoyée plus tard (par exemple, à 19 h au lieu de 18 h), les utilisateurs qui se trouvaient dans le segment ciblé lorsque l'heure d'envoi initiale a été choisie recevront toujours le message à l'heure d'origine (18 h). Si vous modifiez l'heure d'envoi pour qu'elle soit plus tôt (par exemple, à 16 h au lieu de 17 h), la campagne sera tout de même envoyée à tous les membres du segment à l'heure d'origine (17 h). 

{% alert note %}
Pour les composants Canvas, les utilisateurs n'ont pas besoin d'être dans le composant pendant 24 heures pour recevoir le composant suivant de leur parcours utilisateur lors de la livraison selon un fuseau horaire local.
{% endalert %}

Si vous avez permis aux utilisateurs de devenir rééligibles pour la campagne, ils la recevront une nouvelle fois à l'heure d'origine (17 h). Pour toutes les occurrences ultérieures de votre campagne, cependant, vos messages ne sont envoyés qu'à l'heure mise à jour.

### Quand les changements apportés aux campagnes en fuseau horaire local prennent-ils effet ?

Les segments cibles pour les campagnes en fuseau horaire local doivent inclure une fenêtre d'au moins 48 heures pour les filtres temporels, afin de garantir la distribution au segment tout entier. Par exemple, imaginez un segment ciblant les utilisateurs lors de leur deuxième jour avec les filtres suivants :

- Première utilisation de l'application il y a plus d'un jour
- Première utilisation de l'application il y a moins de 2 jours

La livraison selon un fuseau horaire local peut manquer certains utilisateurs de ce segment en fonction de l'heure de distribution et de leur fuseau horaire local. Cela est dû au fait qu'un utilisateur peut quitter le segment avant que son fuseau horaire ne déclenche la distribution.

### Quels changements puis-je apporter aux campagnes planifiées avant le lancement ?

Une fois la campagne planifiée, il est nécessaire de modifier tout élément autre que la composition du message avant que les messages ne soient mis en file d'attente pour l'envoi. Comme pour toutes les campagnes, il n'est pas possible de modifier les événements de conversion après le lancement.

### J'ai mis à jour ma campagne programmée. Pourquoi n'a-t-elle pas été lancée ?

Cela peut se produire lorsqu'une campagne est programmée pour être lancée à l'heure exacte où elle a été mise à jour. Par exemple, s'il est actuellement 15 h 10 et que vous avez modifié la campagne pour la lancer à 15 h 10 et sélectionné **Mettre à jour la campagne**, il est maintenant plus de 15 h 10, ce qui signifie que l'heure prévue pour le lancement est passée. Au lieu de programmer la campagne pour la même heure, sélectionnez **Envoyer dès le lancement de la campagne**.

### Quelle est la « zone sécurisée » avant que les messages d'une campagne programmée soient placés en file d'attente ?

Nous vous recommandons de modifier les messages dans les délais suivants :

- **Campagnes à planification unique :** Modifier jusqu'à l'heure d'envoi planifiée.
- **Campagnes planifiées récurrentes :** Modifier jusqu'à l'heure d'envoi planifiée.
- **Campagnes en heure locale :** Modifier jusqu'à 24 heures avant l'heure d'envoi planifiée.
- **Campagnes à heure d'envoi optimale :** Modifier jusqu'à 24 heures avant le jour où l'envoi de la campagne est planifié.

Si vous apportez des modifications en dehors de ces recommandations, il se peut que les mises à jour ne soient pas reflétées dans le message envoyé. Par exemple, si vous modifiez l'heure d'envoi trois heures avant une campagne dont l'envoi est planifié à 12 h, heure locale, la situation suivante peut se produire :

- Braze n'envoie pas de messages aux utilisateurs qui ont dépassé l'heure d'envoi de plus d'une heure.
- Les messages déjà en file d'attente peuvent être envoyés à l'heure initialement prévue, plutôt qu'à l'heure ajustée.

Si vous devez apporter des modifications, nous vous recommandons d'interrompre la campagne en cours (ceci annule tous les messages en attente). Vous pouvez ensuite dupliquer la campagne, apporter les modifications nécessaires et lancer la nouvelle campagne. Vous devrez peut-être exclure de cette campagne les utilisateurs qui ont déjà reçu la première. Assurez-vous de réajuster les heures de planification de la campagne pour permettre l'envoi selon le fuseau horaire.

### Pourquoi aucun utilisateur n'est-il entré dans ma campagne quotidienne planifiée le jour du passage à l'heure d'été ?

Lors des jours de transition à l'heure d'été, les campagnes quotidiennes planifiées peuvent être diffusées jusqu'à une heure plus tôt ou plus tard que d'habitude, selon que les horloges avancent ou reculent. Si votre segment repose sur des attributs personnalisés ou des événements dont les horodatages se situent dans l'heure précédant l'heure planifiée de l'envoi, ces utilisateurs pourraient ne pas encore être éligibles lorsque la campagne évalue l'éligibilité le jour du passage à l'heure d'été.

Par exemple, supposons que les utilisateurs reçoivent généralement une mise à jour d'attribut personnalisé à 15 h UTC et que votre campagne soit diffusée quotidiennement à 10 h 30 à New York (heure de l'Est). Lorsque New York est à l'heure standard (UTC-5), 10 h 30 ET correspond à 15 h 30 UTC : la campagne est donc diffusée après l'enregistrement de l'attribut. Lorsque New York passe à l'heure d'été (UTC-4), 10 h 30 ET correspond à 14 h 30 UTC. Ainsi, le jour du passage à l'heure d'été, la campagne peut être diffusée avant la mise à jour de l'attribut à 15 h UTC. Étant donné que l'attribut de qualification n'existe pas encore, ces utilisateurs sont exclus. Si la rééligibilité est désactivée, les utilisateurs qui sont entrés les jours précédents ne peuvent pas entrer à nouveau, ce qui entraîne zéro entrée pour ce jour-là.

Pour éviter cela, assurez-vous que vos mises à jour d'attributs personnalisés ou d'événements personnalisés ont lieu plus d'une heure avant l'heure planifiée de l'envoi de la campagne.

### Pourquoi le nombre d'utilisateurs entrant dans une campagne ne correspond-il pas au nombre prévu ?

Le nombre d'utilisateurs entrant dans une campagne peut différer du nombre prévu en raison de la manière dont les audiences et les déclencheurs sont évalués. Dans Braze, une audience est évaluée avant le déclencheur (sauf en cas d'utilisation d'un déclencheur de [modification d'attribut]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value)). Les utilisateurs seront donc exclus de la campagne s'ils ne font pas initialement partie de votre audience sélectionnée avant que les actions de déclenchement ne soient évaluées.

{% alert tip %}
Pour obtenir de l'aide dans la résolution des problèmes liés aux campagnes, contactez l'assistance Braze dans les 30 jours suivant l'apparition de votre problème, car nous ne disposons que des journaux de diagnostic des 30 derniers jours.
{% endalert %}

### Quelle est la différence entre les options « Exportation CSV des données utilisateur » et « Exportation CSV des adresses e-mail » sur la page d'analyse de ma campagne ?

L'option **Exporter les adresses e-mail au format CSV** ne télécharge que les données des utilisateurs disposant d'une adresse e-mail. Par exemple, si vous disposez d'un segment de 100 000 utilisateurs, mais que seuls 50 000 d'entre eux possèdent une adresse e-mail, et que vous cliquez sur **Exporter les adresses e-mail au format CSV**, l'exportation ne contiendra que 50 000 lignes de données. En comparaison, l'option **Exporter les données utilisateur au format CSV** exporte toutes les données utilisateur.

### Puis-je rechercher une campagne par son identifiant API ?

Oui, utilisez le filtre `api_id:YOUR_API_ID` sur la page **Campagnes** pour rechercher une campagne par son identifiant API. Pour en savoir plus, consultez [Rechercher des campagnes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/).

### Pourquoi les espaces blancs apparaissent-ils différemment dans les champs de saisie et dans le texte affiché ?

Le traitement des espaces blancs diffère entre les champs de saisie et les composants de texte affichés en raison du style CSS. Dans les composants de texte utilisant le CSS par défaut `white-space: normal`, plusieurs espaces consécutifs sont réduits à un seul espace lors de l'affichage. Il s'agit du comportement HTML standard pour le texte rendu. 

Les champs de saisie conservent les espaces multiples exactement tels que vous les avez saisis, car il est nécessaire de voir et de modifier l'espacement exact pour une saisie précise des données. Cela signifie qu'un texte comportant plusieurs espaces peut apparaître différemment dans un champ de saisie (où tous les espaces sont conservés) et dans d'autres parties du tableau de bord (où le CSS peut réduire plusieurs espaces). 

Par exemple, si vous saisissez un nom de campagne ou un paramètre UTM comportant plusieurs espaces dans un champ de saisie, tous les espaces sont conservés. Cependant, lorsque ce même texte apparaît dans les résultats de recherche, les listes de campagnes ou d'autres composants textuels, plusieurs espaces peuvent apparaître comme un seul espace en raison du traitement CSS des espaces blancs. 

### Quelle est la différence entre les campagnes API et les campagnes déclenchées par l'API ?

Les campagnes déclenchées par API vous permettent de gérer le texte de la campagne, les tests multivariés et les règles de rééligibilité dans le tableau de bord de Braze, tout en déclenchant la distribution de ce contenu à partir de vos propres serveurs et systèmes. Ces messages peuvent également contenir des données supplémentaires à intégrer en temps réel dans les messages.

Les campagnes API sont utilisées pour suivre les messages envoyés via l'API. Contrairement à la plupart des campagnes, vous ne spécifiez pas le message, les destinataires ou la planification, mais vous transmettez les identifiants dans vos appels API. 

### Quelle est la différence entre les campagnes par événement et les campagnes déclenchées par API ?

<style>
table th:nth-child(1) {
    width: 50%;
}
table th:nth-child(3) {
    width: 50%;
}
</style>

#### Par événement

Les campagnes de livraison par événement ou les campagnes déclenchées par événement sont très efficaces pour les messages transactionnels ou basés sur la réussite, et vous permettent de les déclencher après qu'un utilisateur a effectué un événement donné. 

| Avantages | Inconvénients | 
| ---- | ---- |
| • Visibilité des charges utiles JSON entrantes dans la plateforme (si l'événement est déclenché par un utilisateur test) via le **Journal d'activité des messages**<br><br>• Les éléments de personnalisation sont inclus dans les propriétés d'événement personnalisé<br><br>• Les événements personnalisés peuvent être utilisés pour créer des segments d'utilisateurs éligibles pour le message | • Consomme des points de données |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Déclenchement par API

Les campagnes déclenchées par l'API et par le serveur sont idéales pour traiter des transactions plus avancées, vous permettant de déclencher la distribution du contenu de la campagne à partir de vos propres serveurs et systèmes. La requête API pour déclencher le message peut également inclure des données supplémentaires qui seront intégrées au message en temps réel.

| Avantages | Considérations | 
| ---- | ---- |
| • N'enregistre pas de points de données<br><br>• Les éléments de personnalisation sont inclus dans les propriétés de la charge utile JSON | • Ne permet pas de créer un segment d'utilisateurs éligibles au message dans les propriétés de la charge utile JSON<br><br>• Impossible de voir les charges utiles JSON entrantes avec le **Journal d'activité des messages**|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Que dois-je inclure lorsque je soumets un ticket d'assistance pour une erreur « Request Timed Out » ?

Si vous rencontrez une erreur « Request Timed Out » lors de la création ou de la modification d'une campagne ou d'un Canvas et que vous devez contacter l'[assistance Braze]({{site.baseurl}}/braze_support/), incluez les informations suivantes pour accélérer la résolution :

- **Enregistrement d'écran :** Un enregistrement des étapes que vous avez suivies avant de voir l'erreur, y compris les transitions de page.
- **Horodatage et fuseau horaire :** L'heure exacte à laquelle l'erreur s'est produite et votre fuseau horaire.
- **Navigateur et version :** Le navigateur que vous utilisez (par exemple, Chrome 120, Safari 17) et si vous avez essayé de reproduire l'erreur dans un autre navigateur.
- **Étapes de reproduction :** Une description claire des actions qui déclenchent l'erreur, y compris les paramètres spécifiques de la campagne ou du Canvas concernés.
- **Journaux réseau (facultatif) :** Ouvrez les outils de développement de votre navigateur (onglet **Réseau**), reproduisez l'erreur et exportez le journal réseau sous forme de fichier HAR (HTTP Archive). Cela aide l'équipe d'assistance à identifier quel appel API est en dépassement de délai.

### Pourquoi mes analyses d'envoi ne correspondent-elles pas à la limite maximale de destinataires que j'ai définie ?

Si vous ajoutez ou modifiez une limite maximale de destinataires sur une campagne active, il se peut que cette limite ne soit pas reflétée dans vos analyses d'envoi pour les raisons suivantes :

- **Limite ajoutée après le lancement :** Si la limite maximale de destinataires n'est pas définie au moment du lancement de la campagne, les messages déjà en file d'attente avant l'application de la limite sont tout de même envoyés. La limite ne prend effet que pour les envois mis en file d'attente après l'enregistrement de la modification.
- **Interaction avec la limite de débit :** Si une campagne est également soumise à une limite de débit, les messages peuvent être distribués sur une fenêtre de temps plus longue. La limite maximale de destinataires est évaluée lorsque les messages sont mis en file d'attente, et non lorsqu'ils sont livrés. Si la limite est modifiée alors que des messages sont déjà dans la file d'attente, la limite d'origine s'applique à ces messages.
- **Campagnes récurrentes :** Pour les campagnes récurrentes, chaque envoi planifié évalue la limite maximale de destinataires de manière indépendante. Modifier la limite entre deux envois ne réajuste pas rétroactivement les comptages des envois précédents.

Pour éviter tout décalage, définissez la limite maximale de destinataires avant de lancer la campagne et évitez de la modifier pendant que des envois sont en cours.