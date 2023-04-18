---
nav_title: FAQ
article_title: FAQ Campagnes
page_order: 10
page_type: FAQ
description: "Le présent article fournit des réponses aux questions fréquemment posées sur les campagnes."
tool: Campaigns

---

# FAQ Campagnes

> Cet article fournit des réponses à des questions fréquemment posées sur les campagnes.

### Comment créer une campagne multicanale ?

Les campagnes multicanal peuvent être créées en sélectionnant **Create Campaign (Créer une campagne)** puis **Multichannel Campaign (Campagne multicanal)** dans le tableau de bord. Une fois dans une campagne multicanal, sélectionnez **Add Messaging Channel (Ajouter un canal de communication)** au sein de l’onglet **Compose (Composer)** pour ajouter les canaux souhaités. En cliquant sur les icônes de canal qui apparaissent, vous pouvez basculer entre différents composeurs de messages lorsque vous créez le texte de votre campagne pour les différents canaux.

### Puis-je ajouter un groupe de contrôle à ma campagne multicanal ?

Non, les groupes de contrôle dans les campagnes sont prévus pour un envoi de messages omnicanal tel que e-mail A versus e-mail B. Vous pouvez essayer à la place d’utiliser [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas) pour tester plusieurs canaux, le contenu de communication et le timing de livraison. 

### Comment puis-je commencer à tester et optimiser les campagnes ?

Les campagnes multivariées et l’exécution de Canvas avec plusieurs variantes sont un excellent moyen de commencer ! Par exemple, vous pouvez exécuter une [campagne multivariée]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) pour tester un message comportant des textes ou des lignes Objet variés. Les Canvas avec plusieurs variantes sont utiles pour tester des flux de travail entiers.

### Pourquoi le taux d’ouverture de ma campagne a-t-il baissé ?

De faibles taux d’ouverture ne sont pas forcément liés à un problème technique. Il peut y avoir des problèmes liés à l’écrêtage d’un e-mail qui peut entraîner la disparition d’un pixel de suivi. Il est cependant également possible que moins d’utilisateurs ouvrent leurs e-mails en raison de changements de contenu ou de taille d’audience. 

### Comment les audiences de la campagne sont-elles évaluées ?

Par défaut, les campagnes vérifient les filtres d’audience lors de l’entrée. Pour les campagnes par événement disposant d’un délai, il existe une option pour réévaluer le critère de segmentation au moment de l’envoi pour vous assurer que les utilisateurs font toujours partie de l’audience cible lorsque le message est envoyé. 

### Pourquoi y a-t-il une différence entre le nombre de destinataires uniques et le nombre d’envois pour une campagne ou un Canvas donné ?

Une explication potentielle de cette différence peut venir de l’activation de la rééligibilité pour la campagne ou le Canvas. Pour ce faire, les utilisateurs qui remplissent les conditions requises pour les paramètres de segment et de livraison pourront recevoir le message plusieurs fois. Si la rééligibilité n’est pas activée, l’explication probable de la différence entre les envois et les destinataires uniques peut venir des utilisateurs ayant plusieurs appareils, sur plusieurs plates-formes, associés à leurs profils. 

Par exemple, si vous avez un Canvas qui dispose à la fois d’une notification push iOS et Web, un utilisateur donné possédant à la fois un téléphone et un ordinateur de bureau peut recevoir plus d’un message.

### Pourquoi ma campagne a-t-elle une plus petite base d’utilisateurs accessible que le segment que j’utilise pour cette campagne ?

Si vous avez configuré un [groupe de contrôle global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/), il empêchera un pourcentage de votre audience pouvant être atteinte de recevoir les campagnes. Cela signifie que le nombre d’utilisateurs accessibles à votre segment peut parfois être supérieur au nombre d’utilisateurs accessibles pour votre campagne, même si la campagne utilise ce même segment.

### Qu’est-ce que l’offre de livraison selon le fuseau horaire local ?

La livraison selon le fuseau horaire local vous permet de livrer des campagnes de communication à un segment en fonction du fuseau horaire individuel d’un utilisateur. Sans la livraison selon le fuseau horaire local, les campagnes seront planifiées en fonction des paramètres de fuseau horaire de votre société dans Braze. 

Par exemple, une société basée à Londres qui envoie une campagne à midi atteindra les utilisateurs sur la côte ouest de l’Amérique à 4 h du matin. Si votre application n’est disponible que dans certains pays, cela peut ne pas représenter un risque pour vous, sinon nous vous recommandons vivement d’éviter d’envoyer des notifications push matinales à votre base d’utilisateurs !

### Comment Braze connaît-t-il le fuseau horaire d’un utilisateur ?

Braze détermine automatiquement le fuseau horaire d’un utilisateur à partir de son appareil. Cela garantit une précision de fuseau horaire et une couverture complète de vos utilisateurs. Les utilisateurs créés via l’API utilisateur ou n’ayant pas de fuseau horaire prendront celui de votre entreprise comme fuseau horaire par défaut jusqu’à ce qu’ils soient identifiés dans votre application par le SDK. 

Vous pouvez vérifier le fuseau horaire de votre entreprise dans vos [Company settings]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/company-wide_settings_management/) (Paramètres de la société) sur le tableau de bord.

### Quand Braze évalue-t-il les utilisateurs pour la livraison selon un fuseau horaire local ?

Pour la livraison selon un fuseau horaire local, Braze évalue les utilisateurs pour leur éligibilité à l’entrée à deux moments :

- À l’heure des Samoa (UTC + 13) du jour planifié
- À l’heure locale du jour planifié

Pour que l’utilisateur puisse être admissible à l’entrée, il doit être admissible pour les deux vérifications. Par exemple, si un Canvas est prévu pour être lancé le 7 août 2021 à 14 h du fuseau horaire local, cibler un utilisateur situé à New York nécessite les vérifications d’admissibilité suivantes :

- New York, le 6 août 2021 à 21 h
- New York, le 7 août 2021 à 14 h

Notez que l’utilisateur doit être dans le segment pendant 24 heures avant le lancement. Si l’utilisateur n’est pas admissible à la première vérification, alors Braze n’essaiera pas de faire la deuxième.

Par exemple, si une campagne est planifiée pour une livraison à 19 h UTC, nous commencerons à placer les envois de la campagne en file d’attente dès qu’un fuseau horaire est identifié (tel que les Samoa). Ceci signifie que nous nous préparons à envoyer le message, pas que la campagne est envoyée. Si les utilisateurs ne correspondent à aucun filtre lorsque nous vérifions l’éligibilité, ils ne feront pas partie de l’audience cible.

Un autre exemple serait que vous désirez créer deux campagnes planifiées pour s’envoyer le même jour, une le matin et une le soir, et ajouter un filtre disant que les utilisateurs ne peuvent recevoir la deuxième campagne que s’ils ont déjà reçu la première. Avec la livraison selon le fuseau horaire local, certains utilisateurs pourraient ne pas recevoir la seconde campagne. La raison en est que nous vérifions l’éligibilité lorsque le fuseau horaire de l’utilisateur est identifié, de sorte que si l’heure planifiée n’est pas encore passée dans leur fuseau horaire, ils n’ont pas reçu la première campagne. Ils ne seront donc pas éligibles à la seconde campagne.

### Comment planifier une campagne selon un fuseau horaire local ?

Lors de la planification d’une campagne, vous devez choisir de l’envoyer à un moment donné, puis cocher **Send campaign to users in their local time zone** (Envoyer une campagne aux utilisateurs selon leur fuseau horaire local).

Braze recommande vivement que toutes les campagnes selon le fuseau horaire local soient planifiées 24 heures à l’avance. Puisque cette campagne doit être envoyée au cours d’une journée entière, les planifier 24 heures à l’avance garantit que votre message atteindra votre segment tout entier. Cependant, vous pouvez planifier ces campagnes moins de 24 heures à l’avance si nécessaire. N’oubliez pas que Braze n’enverra pas de messages aux utilisateurs qui ont manqué l’heure d’envoi de plus d’une heure. 

Par exemple, s’il est 13 h et que vous planifiez une campagne selon un fuseau horaire local pour 15 h, la campagne sera envoyée immédiatement à tous les utilisateurs dont l’heure locale est comprise entre 15 h et 16 h, mais pas aux utilisateurs dont l’heure locale est 17 h. De plus, l’heure d’envoi que vous choisissez pour votre campagne ne doit pas encore être dépassée dans le fuseau horaire de votre société.

La modification d’une campagne selon un fuseau horaire local qui est programmée moins de 24 heures à l’avance ne modifiera pas la planification du message. Si vous décidez de modifier une campagne selon un fuseau horaire local pour qu’elle soit envoyée ultérieurement (par exemple, à 19 h au lieu de 18 h), les utilisateurs qui se trouvaient dans le segment ciblé lorsque l’heure d’envoi initiale a été choisie recevront toujours le message à l’heure d’origine (18 h). Si vous modifiez un fuseau horaire local pour que l’envoi se fasse plus tôt (par exemple, à 16 h au lieu de 17 h), la campagne sera toujours envoyée à tous les membres du segment à l’heure d’origine (17 h). 

{% alert note %}
Pour les composants Canvas, les utilisateurs n’ont pas besoin d’être dans le composant pendant 24 heures pour recevoir le composant suivant de leur parcours utilisateur lors de la livraison selon un fuseau horaire local. 
{% endalert %}

Si vous avez permis aux utilisateurs de devenir rééligibles pour la campagne, ils la recevront une nouvelle fois à l’heure d’origine (17 h). Cependant, pour toutes les occurrences ultérieures de votre campagne, vos messages ne seront envoyés que lors de votre mise à jour.

### Quand les changements apportés aux campagnes selon un fuseau horaire local prennent-ils effet ?

Les segments cibles pour les campagnes selon un fuseau horaire local doivent inclure une fenêtre de 48 heures au moins pour que les filtres temporels garantissent la livraison au segment tout entier. Par exemple, imaginez un segment ciblant les utilisateurs lors de leur deuxième jour avec les filtres suivants :

- Première utilisation de l’application il y a plus d’un jour
- Première utilisation de l’application il y a moins de 2 jours

La livraison selon un fuseau horaire local peut manquer les utilisateurs de ce segment en fonction du temps de livraison et de leur fuseau horaire local. Ceci est dû à la possibilité que l’utilisateur quitte le segment avant que son fuseau horaire ne déclenche la livraison.

### Quels changements puis-je apporter aux campagnes planifiées avant le lancement ?

Lorsque la campagne est planifiée, les modifications touchant autre chose que la composition du message doivent être effectuées avant qu’il ne soit placé dans la file d’attente d’envois. Comme pour toutes les campagnes, vous ne pouvez pas modifier les événements de conversion après son lancement.

### Quelle est la « zone sécurisée » avant que les messages d’une campagne programmée soient placés en file d’attente ?

- Les **campagnes planifiées ponctuelles** peuvent être modifiées jusqu’à l’heure d’envoi prévue.
- Les **campagnes planifiées récurrentes** peuvent être modifiées jusqu’à l’heure d’envoi prévue.
- Les **campagnes à heure d’envoi locale** peuvent être modifiées jusqu’à 24 heures avant l’heure d’envoi prévue.
- Les **campagnes à heure d’envoi optimale** peuvent être modifiées jusqu’à 24 heures avant le jour où la campagne est planifiée pour l’envoi.

### Que faire si je fais une modification dans la « zone sécurisée » ?

Changer l’heure d’envoi sur les campagnes à ce moment-là peut entraîner un comportement indésirable, par exemple :

- Braze n’enverra pas de messages aux utilisateurs qui ont manqué l’heure d’envoi de plus d’une heure.
- Les messages placés en file d’attente à l’avance peuvent toujours être envoyés à l’heure initialement prévue, plutôt qu’à l’heure modifiée.

### Que dois-je faire si la « zone sécurisée » est déjà passée ?

Afin de garantir que les campagnes fonctionnent comme souhaité, nous vous recommandons d’arrêter la campagne actuelle (ceci annulera tous les messages qui ont été placés en file d’attente). Vous pouvez ensuite dupliquer la campagne, apporter les modifications nécessaires et lancer la nouvelle campagne. Vous devrez peut-être exclure les utilisateurs de cette campagne qui ont déjà reçu la première.

Assurez-vous de réajuster les heures de planification de la campagne pour permettre l’envoi selon un fuseau horaire.

### Pourquoi le nombre d’utilisateurs qui accèdent à une campagne ne correspond pas au nombre prévu ?

Le nombre d’utilisateurs accédant à une campagne peut être différent du nombre prévu selon le mode d’évaluation des audiences et des déclencheurs. Dans Braze, une audience est évaluée avant le déclencheur (sauf si un déclencheur [modification d’attribut]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value) est utilisé). Les utilisateurs seront alors exclus de la campagne s’ils ne font pas partie de l’audience que vous avez sélectionnée au départ, avant l’évaluation des actions de déclenchement.

### Quelle est la différence entre les options Exportation CSV des données utilisateurs et Exportation CSV des adresses e-mail sur ma page d’analytiques de campagne ?

Sélectionner l’option **Exportation CSV des adresses e-mail** téléchargera uniquement les données des utilisateurs ayant des adresses e-mail. Par exemple, si vous disposez d’un segment de 100 000 utilisateurs, mais que seulement 50 000 de ces utilisateurs ont des adresses e-mail, puis que vous cliquez sur **Exportation CSV des adresses e-mail**, alors vous devez vous attendre à ne voir que 50 000 lignes de données dans le fichier CSV. Comparativement, sélectionner **Exportation CSV des données utilisateurs** exportera toutes les données utilisateur.

### Puis-je rechercher une campagne en utilisant son identifiant API ?

Oui, utilisez le filtre `api_id:YOUR_API_ID` sur la page **Campaigns** pour rechercher une campagne par son identifiant API. Consultez [Rechercher des campagnes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/) pour en savoir plus.

### Quelle est la différence entre les campagnes API et les campagnes déclenchées par API ?

Les campagnes déclenchées par API vous permettent de gérer les copies de campagne, les tests multivariés et les règles de rééligibilité dans le tableau de bord de Braze tout en déclenchant la livraison de ce contenu à partir de vos propres serveurs et systèmes. Ces messages peuvent également inclure des données supplémentaires à modéliser dans les messages en temps réel.

Les campagnes API sont utilisées pour suivre les messages que vous envoyez en utilisant l’API. Contrairement à la majorité des campagnes, vous ne spécifiez ni le message, ni les destinataires, ni la planification, mais vous transmettez à la place les identifiants dans vos appels API. 

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
| • Visibilité des charges utiles JSON à venir sur la plate-forme (si l’événement est déclenché par l’utilisateur de test) via la **Journalisation d’activité des messages**<br><br>• Les éléments de personnalisation sont compris dans les propriétés de l’événement personnalisées<br><br>• Les événements personnalisés peuvent être utilisés pour créer des segments d’utilisateurs éligibles pour le message | • Utilise des points de données |
{: .reset-td-br-1 .reset-td-br-2}

#### Déclenchée par API

Les campagnes déclenchées par API ou par le serveur sont idéales pour les cas d’utilisation transactionnels plus avancés et vous permettent de déclencher la livraison du contenu de la campagne depuis vos propres serveurs et systèmes. La demande API pour déclencher le message peut également inclure des données supplémentaires à modéliser dans le message en temps réel.

| Avantages | Inconvénients | 
| ---- | ---- |
| • N’utilise pas de points de données<br><br>• Les éléments de personnalisation sont compris dans les propriétés de l’événement | • Ne vous permet pas de créer un segment d’utilisateurs éligibles au message dans les propriétés de la charge utile JSON<br><br>• Il n’est pas possible de voir les charges utiles JSON à venir à l’aide de la **Journalisation d’activité des messages**|
{: .reset-td-br-1 .reset-td-br-2}

