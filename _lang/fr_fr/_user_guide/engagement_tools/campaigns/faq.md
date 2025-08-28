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

Pour créer une campagne multicanale, sélectionnez **Messagerie** > **Campagnes**. Sélectionnez ensuite **Créer une campagne** > **Multicanal**. À partir de là, vous pouvez sélectionner l'un des canaux de communication suivants : Cartes de contenu, e-mail, LINE, notifications push, SMS/MMS/RCS, webhook ou WhatsApp.

### Puis-je ajouter un groupe de contrôle à ma campagne multicanal ?

Non, les groupes de contrôle dans les campagnes sont destinés aux messages à canal unique, tels que l'Email A par rapport à l'Email B. Comme alternative, essayez d'utiliser [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas) pour tester différents canaux, contenus de message et horaires de livraison. 

### Comment puis-je commencer à tester et optimiser les campagnes ?

Les campagnes multivariées et l’exécution de Canvas avec plusieurs variantes sont un excellent moyen de commencer ! Par exemple, vous pouvez lancer une [campagne multivariée]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) pour tester un message qui a différentes copies ou lignes d'objet. Les toiles comportant plusieurs variantes peuvent permettre de tester des flux de travail entiers.

### Pourquoi le taux d’ouverture de ma campagne a-t-il baissé ?

De faibles taux d’ouverture ne sont pas forcément liés à un problème technique. Il peut y avoir des problèmes liés à l’écrêtage d’un e-mail qui peut entraîner la disparition d’un pixel de suivi. Il est cependant également possible que moins d’utilisateurs ouvrent leurs e-mails en raison de changements de contenu ou de taille d’audience. 

### Comment les audiences de la campagne sont-elles évaluées ?

Par défaut, les campagnes vérifient les filtres d’audience lors de l’entrée. Pour les campagnes par événement disposant d’un délai, il existe une option pour réévaluer le critère de segmentation au moment de l’envoi pour vous assurer que les utilisateurs font toujours partie de l’audience cible lorsque le message est envoyé. 

### Pourquoi y a-t-il une différence entre le nombre de destinataires uniques et le nombre d’envois pour une campagne ou un Canvas donné ?

Une explication possible pourrait être que la campagne ou Canvas a activé la rééligibilité, ce qui signifie que les utilisateurs qui se qualifient pour le segment et les paramètres de réception/distribution seront en mesure de recevoir le message plus d'une fois. Si la rééligibilité n’est pas activée, l’explication probable de la différence entre les envois et les destinataires uniques peut venir des utilisateurs ayant plusieurs appareils, sur plusieurs plates-formes, associés à leurs profils. 

Par exemple, si vous avez un Canvas qui dispose à la fois d’une notification push iOS et Web, un utilisateur donné possédant à la fois un téléphone et un ordinateur de bureau peut recevoir plus d’un message.

### Pourquoi ma campagne a-t-elle une plus petite base d’utilisateurs accessible que le segment que j’utilise pour cette campagne ?

Si vous avez un [Groupe de Contrôle Global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) configuré, cela empêchera un pourcentage de votre audience atteignable de recevoir des campagnes. Cela signifie que le nombre d’utilisateurs accessibles à votre segment peut parfois être supérieur au nombre d’utilisateurs accessibles pour votre campagne, même si la campagne utilise ce même segment.

### Qu’est-ce que l’offre de livraison selon le fuseau horaire local ?

La livraison selon le fuseau horaire local vous permet de livrer des campagnes de communication à un segment en fonction du fuseau horaire individuel d’un utilisateur. Sans la livraison selon le fuseau horaire local, les campagnes seront planifiées en fonction des paramètres de fuseau horaire de votre société dans Braze. 

Par exemple, une société basée à Londres qui envoie une campagne à midi atteindra les utilisateurs sur la côte ouest de l’Amérique à 4 h du matin. Si votre application n'est disponible que dans certains pays, vous ne courez peut-être aucun risque. Dans le cas contraire, nous vous recommandons vivement d'éviter d'envoyer des notifications push tôt le matin à votre base d'utilisateurs.

### Comment Braze connaît-t-il le fuseau horaire d’un utilisateur ?

Braze détermine automatiquement le fuseau horaire d’un utilisateur à partir de son appareil. Cela garantit une précision de fuseau horaire et une couverture complète de vos utilisateurs. Les utilisateurs créés via l’API utilisateur ou n’ayant pas de fuseau horaire prendront celui de votre entreprise comme fuseau horaire par défaut jusqu’à ce qu’ils soient identifiés dans votre application par le SDK. 

Vous pouvez vérifier le fuseau horaire de votre entreprise dans vos [paramètres de l'entreprise]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/) sur le tableau de bord.

### Quand Braze évalue-t-il les utilisateurs pour la livraison selon un fuseau horaire local ?

Pour la livraison selon un fuseau horaire local, Braze évalue les utilisateurs pour leur éligibilité à l’entrée à deux moments :

- À l’heure des Samoa (UTC + 13) du jour planifié
- À l’heure locale du jour planifié

Pour que l’utilisateur puisse être admissible à l’entrée, il doit être admissible pour les deux vérifications. Par exemple, si un Canvas est prévu pour être lancé le 7 août 2021 à 14 h du fuseau horaire local, cibler un utilisateur situé à New York nécessite les vérifications d’admissibilité suivantes :

- New York, le 6 août 2021 à 21 h
- New York, le 7 août 2021 à 14 h

Notez que l’utilisateur doit être dans le segment pendant 24 heures avant le lancement. Si l’utilisateur n’est pas admissible à la première vérification, alors Braze n’essaiera pas de faire la deuxième.

Par exemple, si une campagne est planifiée pour une livraison à 19 h UTC, nous commencerons à placer les envois de la campagne en file d’attente dès qu’un fuseau horaire est identifié (tpar exemple, les Samoa). Cela signifie que nous nous préparons à envoyer le message, et non à envoyer la campagne. Si les utilisateurs ne correspondent à aucun filtre lorsque nous vérifions leur éligibilité, ils ne feront pas partie de l'audience cible.

Un autre exemple serait que vous désirez créer deux campagnes planifiées pour s’envoyer le même jour, une le matin et une le soir, et ajouter un filtre disant que les utilisateurs ne peuvent recevoir la deuxième campagne que s’ils ont déjà reçu la première. Avec la livraison selon le fuseau horaire local, certains utilisateurs pourraient ne pas recevoir la seconde campagne. En effet, nous vérifions l'éligibilité lorsque le fuseau horaire de l'utilisateur est identifié. Par conséquent, si l'heure planifiée n'a pas encore eu lieu dans son fuseau horaire, il n'a pas reçu la première campagne, ce qui signifie qu'il ne sera pas éligible pour la deuxième campagne.

### Comment planifier une campagne selon un fuseau horaire local ?

Lors de la planification d'une campagne, choisissez de l'envoyer à une heure donnée, puis sélectionnez **Envoyer la campagne aux utilisateurs dans leur fuseau horaire local**.

Braze recommande vivement que toutes les campagnes concernant les fuseaux horaires locaux soient planifiées 24 heures à l'avance. Étant donné qu'une telle campagne doit être envoyée sur une journée entière, la planifier 24 heures à l'avance permet de s'assurer que votre message atteindra l'ensemble de votre segmentation. Cependant, vous pouvez planifier ces campagnes moins de 24 heures à l’avance si nécessaire. N'oubliez pas que Braze n'enverra pas de messages aux utilisateurs qui ont dépassé l'heure d'envoi de plus d'une heure. 

Par exemple, s’il est 13 h et que vous planifiez une campagne selon un fuseau horaire local pour 15 h, la campagne sera envoyée immédiatement à tous les utilisateurs dont l’heure locale est comprise entre 15 h et 16 h, mais pas aux utilisateurs dont l’heure locale est 17 h. De plus, l’heure d’envoi que vous choisissez pour votre campagne ne doit pas encore être dépassée dans le fuseau horaire de votre société.

La modification d’une campagne selon un fuseau horaire local qui est programmée moins de 24 heures à l’avance ne modifiera pas la planification du message. Si vous décidez de modifier une campagne selon un fuseau horaire local pour qu’elle soit envoyée ultérieurement (par exemple, à 19 h au lieu de 18 h), les utilisateurs qui se trouvaient dans le segment ciblé lorsque l’heure d’envoi initiale a été choisie recevront toujours le message à l’heure d’origine (18 h). Si vous modifiez un fuseau horaire local pour que l’envoi se fasse plus tôt (par exemple, à 16 h au lieu de 17 h), la campagne sera toujours envoyée à tous les membres du segment à l’heure d’origine (17 h). 

{% alert note %}
Pour les composants Canvas, les utilisateurs n’ont pas besoin d’être dans le composant pendant 24 heures pour recevoir le composant suivant de leur parcours utilisateur lors de la livraison selon un fuseau horaire local.
{% endalert %}

Si vous avez permis aux utilisateurs de devenir rééligibles pour la campagne, ils la recevront une nouvelle fois à l’heure d’origine (17 h). Pour toutes les occurrences ultérieures de votre campagne, cependant, vos messages ne sont envoyés qu'à l'heure que vous avez mise à jour.

### Quand les changements apportés aux campagnes selon un fuseau horaire local prennent-ils effet ?

Les segments cibles pour les campagnes selon un fuseau horaire local doivent inclure une fenêtre de 48 heures au moins pour que les filtres temporels garantissent la livraison au segment tout entier. Par exemple, imaginez un segment ciblant les utilisateurs lors de leur deuxième jour avec les filtres suivants :

- Première utilisation de l’application il y a plus d’un jour
- Première utilisation de l’application il y a moins de 2 jours

La livraison selon un fuseau horaire local peut manquer les utilisateurs de ce segment en fonction du temps de livraison et de leur fuseau horaire local. Ceci est dû à la possibilité que l’utilisateur quitte le segment avant que son fuseau horaire ne déclenche la livraison.

### Quels changements puis-je apporter aux campagnes planifiées avant le lancement ?

Lorsque la campagne est planifiée, les modifications touchant autre chose que la composition du message doivent être effectuées avant qu’il ne soit placé dans la file d’attente d’envois. Comme pour toutes les campagnes, vous ne pouvez pas modifier les événements de conversion après son lancement.

### J'ai mis à jour ma campagne programmée. Pourquoi n’a-t-elle pas été lancée ?

Cela peut se produire lorsqu'une campagne est programmée pour être lancée à l'heure exacte où elle a été mise à jour. Par exemple, s'il est actuellement 15 h 10 et que vous avez modifié la campagne pour la lancer à 15 h 10 et sélectionné **Mettre à jour la campagne**, il est maintenant plus de 15 h 10, ce qui signifie que l'heure prévue pour le lancement est passée. Au lieu de programmer la campagne pour la même heure, sélectionnez **Envoyer dès le lancement de la campagne**.

### Quelle est la « zone sécurisée » avant que les messages d’une campagne programmée soient placés en file d’attente ?

Nous vous recommandons de modifier les messages dans les délais suivants :

- **Campagnes à planification unique :** Modifier jusqu'à l'heure d'envoi planifiée.
- **Campagnes planifiées récurrentes :** Modifier jusqu'à l'heure d'envoi planifiée.
- **Campagnes d'envoi local :** Modifiez jusqu'à 24 heures avant l'heure d'envoi planifiée.
- **Campagnes d'envoi optimales :** Modifiez jusqu'à 24 heures avant le jour où l'envoi de la campagne est planifié.

Si vous apportez des modifications à votre message en dehors de ces recommandations, il se peut que les mises à jour ne soient pas reflétées dans le message envoyé. Par exemple, si vous modifiez l'heure d'envoi trois heures avant une campagne dont l'envoi est planifié à 12 heures, heure locale, la situation suivante peut se produire :

- Braze n’enverra pas de messages aux utilisateurs qui ont manqué l’heure d’envoi de plus d’une heure.
- Les messages pré-enregistrés peuvent toujours être envoyés à l'heure initialement prévue, plutôt qu'à l'heure Adjust.

Si vous devez apporter des modifications, nous vous recommandons d'arrêter la campagne en cours (ce qui annulera tous les messages en file d'attente). Vous pouvez ensuite dupliquer la campagne, apporter les modifications nécessaires et lancer la nouvelle campagne. Vous devrez peut-être exclure les utilisateurs de cette campagne qui ont déjà reçu la première. Assurez-vous de réajuster les heures de planification de la campagne pour permettre l’envoi selon un fuseau horaire.

### Pourquoi le nombre d’utilisateurs qui accèdent à une campagne ne correspond pas au nombre prévu ?

Le nombre d’utilisateurs accédant à une campagne peut être différent du nombre prévu selon le mode d’évaluation des audiences et des déclencheurs. Dans Braze, une audience est évaluée avant le déclencheur (sauf si un déclencheur [modification d'attribut]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value) est utilisé). Ainsi, les utilisateurs seront exclus de la campagne s'ils ne font pas initialement partie de votre audience sélectionnée avant que les actions déclencheurs ne soient évaluées.

{% alert tip %}
Pour obtenir de l'aide dans la résolution des problèmes liés aux campagnes, contactez le service d'assistance de Braze dans les 30 jours suivant l'apparition de votre problème, car nous ne disposons que des journaux de diagnostic des 30 derniers jours.
{% endalert %}

### Quelle est la différence entre les options Exportation CSV des données utilisateurs et Exportation CSV des adresses e-mail sur ma page des analyses de campagne ?

Sélectionner l'option **Adresses e-mail d'exportation CSV** ne téléchargera que les données des utilisateurs avec des adresses e-mail. Par exemple, si vous avez un segment de 100 000 utilisateurs, mais que seulement 50 000 de ces utilisateurs ont des adresses e-mail, et que vous cliquez sur **Exportation CSV des adresses e-mail**, alors vous devriez vous attendre à voir seulement 50 000 lignes de données dans le fichier CSV. En comparaison, l’option **Exporter les données utilisateur en CSV** exportera toutes les données utilisateur.

### Puis-je rechercher une campagne en utilisant son identifiant API ?

Oui, utilisez le filtre `api_id:YOUR_API_ID` sur la page **Campagnes** pour rechercher une campagne par son identifiant API. Pour en savoir plus, reportez-vous à [Rechercher des campagnes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/).

### Quelle est la différence entre les campagnes API et les campagnes déclenchées par l'API ?

Les campagnes déclenchées par API vous permettent de gérer le texte de la campagne, les tests multivariés et les règles de rééligibilité dans le tableau de bord de Braze, tout en déclenchant la réception/distribution de ce contenu à partir de vos propres serveurs et systèmes. Ces messages peuvent également contenir des données supplémentaires à intégrer en temps réel dans les messages.

Les campagnes API sont utilisées pour suivre les messages envoyés à l'aide de l'API. Contrairement à la plupart des campagnes, vous ne spécifiez pas le message, les destinataires ou la planification, mais vous transmettez les identifiants dans vos appels API. 

### Quelle est la différence entre les campagnes par événement et les campagnes déclenchées par API ?

<style>
table th:nth-child(1) {
    width: 50%;
}
table th:nth-child(3) {
    width: 50%;
}
</style>

#### Par événement

Les campagnes de livraison par événement ou les campagnes déclenchées par événement sont très efficaces pour les messages transactionnels ou basés sur la réussite et vous permettent de les déclencher après qu’un utilisateur a terminé un événement donné. 

| Avantages | Inconvénients | 
| ---- | ---- |
| • Visibilité des charges utiles JSON entrantes dans la plateforme (si l'événement est déclenché par un utilisateur de test) via le **Journal d'activité des messages**<br><br>• Les éléments de personnalisation sont inclus dans les propriétés d’événement personnalisé<br><br>• Les événements personnalisés peuvent être utilisés pour créer des segments d’utilisateurs éligibles pour le message | • Utilise des points de données |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Déclenchement par API

Les campagnes déclenchées par l'API et par le serveur sont idéales pour traiter des transactions plus avancées, vous permettant de déclencher la réception/distribution du contenu de la campagne à partir de vos propres serveurs et systèmes. La demande d'API pour déclencher le message peut également inclure des données supplémentaires qui seront intégrées au message en temps réel.

| Avantages | Considérations | 
| ---- | ---- |
| • N’utilise pas de points de données<br><br>• Les éléments de personnalisation sont compris dans les propriétés de l’événement | • Ne vous permet pas de créer un segment d’utilisateurs éligibles au message dans les propriétés de la charge utile JSON<br><br>\- Impossible de voir les charges utiles JSON entrantes avec le **journal d'activité des messages**|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

