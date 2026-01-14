---
article_title: FAQ
hidden: true
permalink: /onboarding_faq/
excerpt_separator: ""
page_type: glossary
layout: onboarding_faq
description: "Cette page contient une collection de questions fréquemment posées, classées par catégories."

---

{% multi_lang_include video.html id="keAZAlBR9zc" source="youtube" %}


<!--- Users --->

{% api %}

### Comment traiter les données anonymes des utilisateurs ?

{% apitags %}
Utilisateurs
{% endapitags %}

Au départ, lorsqu'un profil utilisateur est reconnu via le SDK, Braze crée un profil utilisateur anonyme auquel est associé `braze_id`: un identifiant utilisateur unique qui est défini par Braze.

Pour mieux suivre les utilisateurs anonymes, vous pouvez mettre en place des [alias d'utilisateurs]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-aliases) qui vous permettent d'étiqueter les utilisateurs anonymes à l'aide d'un identifiant. Ces utilisateurs peuvent ensuite être exportés à l'aide de leurs alias ou référencés par l'API.

Si un profil utilisateur anonyme doté d'un alias est reconnu ultérieurement par une adresse `external_id`, il sera traité comme un profil utilisateur identifié normal, mais conservera son alias existant et pourra toujours être référencé par cet alias.

Pour les utilisateurs alias que vous souhaitez fusionner avec des utilisateurs identifiés, vous pouvez fusionner tous les champs pertinents pour le profil réel que vous souhaitez conserver. Vous devrez exporter ces données avant de les supprimer du profil d'alias à l'aide de notre [point de terminaison Exporter le profil utilisateur par identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/). Vous pouvez ensuite utiliser notre [endpoint Suivi des utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour publier ces événements dans le profil que vous avez conservé. Cela permettra de préserver toutes les données que vous souhaitez conserver, telles que les attributs qui ont été enregistrés précédemment sur un profil, mais pas sur l'autre.

Pour une analyse complète des différentes méthodes de collecte des données des utilisateurs nouveaux et existants dans Braze, consultez les [meilleures pratiques en matière de collecte de données.]({{site.baseurl}}/user_guide/data/user_data_collection/best_practices/)

{% endapi %}
{% api %}

### Comment puis-je importer des utilisateurs que j'ai déjà collectés et identifiés en dehors de Braze ?

{% apitags %}
Utilisateurs
{% endapitags %}

Pour importer des utilisateurs précédemment identifiés, vous pouvez télécharger un fichier CSV vers Braze ou envoyer des données via l'API.

#### CSV

Vous pouvez télécharger et mettre à jour les profils utilisateurs via des fichiers CSV à partir de **Audience** > Importer des **utilisateurs.** Lors de l'importation des données de vos clients, vous devrez spécifier l'identifiant unique de chaque client, également connu sous le nom de `external_id`.

Avant de commencer votre importation CSV, il est important que votre équipe d'ingénieurs comprenne comment les utilisateurs seront identifiés dans Braze. Il s'agit généralement d'un ID de base de données utilisé en interne. Cela devrait s'aligner sur la manière dont les utilisateurs seront identifiés par le SDK de Braze sur les mobiles et le web, de sorte que chaque client disposera d'un profil utilisateur unique au sein de Braze sur l'ensemble de ses appareils. En savoir plus sur le [cycle de vie du profil utilisateur]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) Braze.

Lorsque vous fournissez un `external_id` dans votre importation, Braze met à jour tout utilisateur existant avec le même `external_id` ou crée un nouvel utilisateur identifié avec ce jeu de `external_id` s'il n'y en a pas.

Pour plus d'informations et pour télécharger des modèles d'importation CSV, reportez-vous à l'[importation d'utilisateurs.]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv)

#### API

Pour télécharger des utilisateurs via l'API, vous pouvez utiliser notre [endpoint Track users]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour les importer dans Braze.

Si vous n'êtes pas sûr que l'utilisateur existe déjà dans Braze, vous pouvez implémenter notre [endpoint Exporter le profil utilisateur par identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) pour vérifier. Si vous identifiez que l'utilisateur existe déjà dans Braze, vous pouvez utiliser notre endpoint `/users/track` pour poster les nouvelles données que vous souhaitez ajouter au profil utilisateur qui existe déjà dans Braze.

{% alert note %}
Gardez les nuances suivantes à l'esprit lorsque vous utilisez l'endpoint `/users/track`:

- Lors de la création d'alias d'utilisateurs via cet endpoint, vous devez explicitement attribuer la valeur false à l'indicateur `_update_existing_only`.
- La mise à jour de l'état de l'abonnement avec cet endpoint mettra à jour l'utilisateur spécifié par son ID externe (par exemple User1) et mettra à jour l'état de l'abonnement de tous les utilisateurs ayant le même e-mail que cet utilisateur (User1).
{% endalert %}

{% endapi %}
{% api %}

### Quelle est la différence entre les statuts de l'abonnement push ?

{% apitags %}
Utilisateurs
{% endapitags %}

Il existe trois options d'état de l'abonnement push : abonné, abonné et désabonné.

Par défaut, pour que votre utilisateur reçoive vos messages via push, son état d'abonnement à push doit être soit abonné, soit abonné avec option, et il doit être activé pour push. Vous pouvez remplacer ce paramètre si nécessaire lors de la rédaction d'un message.

|État d'abonnement|Description|
|---|---|
|Abonné| État de l'abonnement push par défaut lorsqu'un profil utilisateur est créé dans Braze. |
|Abonnement| Un utilisateur a explicitement exprimé sa préférence pour recevoir des notifications push. Braze fait automatiquement passer la demande d'abonnement d'un utilisateur à `Opted-In` s'il accepte une invitation à pousser au niveau du système d'exploitation.<br><br>Cela ne s'applique pas aux utilisateurs d'Android 12 ou d'une version inférieure.|
|Désabonné| Un utilisateur s'est explicitement désabonné de push via votre application ou d'autres méthodes proposées par votre marque. Par défaut, les campagnes de push de Braze ne ciblent que les utilisateurs qui sont `Subscribed` ou `Opted-in` pour le push.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
{% api %}

### Que faire si j'ai identifié des utilisateurs en double ?

{% apitags %}
Utilisateurs
{% endapitags %}

Si vous avez identifié des utilisateurs en double, vous devrez nettoyer ces profils utilisateurs. Vous pouvez le faire en suivant les étapes suivantes :

1. Exportez les profils utilisateurs à l'aide de notre endpoint `/users/export/ids`.
2. Identifier le profil utilisateur correct (en fin de compte, votre équipe devra décider des informations correctes) et soit :
    - Fusionnez tous les champs pertinents pour le profil que vous souhaitez conserver à l'aide de l'endpoint `/user/track`.
    - Supprimez le profil en double, non utile, sans fusionner aucune donnée à l'aide de l'endpoint utilisateurs/suppression. Une fois que vous avez supprimé un profil utilisateur, **il n'y a aucun moyen de récupérer les informations**.

{% alert important %}
Nous vous recommandons d'importer d'abord les nouveaux profils utilisateurs avec les `external_id` corrects et les événements et attributs personnalisés correspondants. Une fois les profils utilisateurs supprimés, ils ne peuvent plus être récupérés. La suppression doit donc être la toute dernière étape.
{% endalert %}

Quelques éléments supplémentaires à noter :

- Toutes les données d'engagement (telles que les campagnes ou les Canevas reçus) sur les profils utilisateurs dupliqués seront perdues. Le seul moyen de conserver l'historique du contexte d'engagement est de l'ajouter en tant qu'attribut personnalisé (tel qu'un attribut personnalisé de type tableau de toutes les campagnes ou toiles reçues).
- Lors de la migration des profils utilisateurs, c'est également à votre équipe de décider quel profil utilisateur des doublons sera conservé. Braze ne peut pas décider ou vous fournir une liste de profils à supprimer.  
- En fin de compte, il sera important pour votre équipe d'évaluer le processus d'inscription à partir de l'expérience de vos utilisateurs et de s'assurer que vous n'appelez la méthode `changeUser()` que lorsqu'un utilisateur s'identifie.

{% endapi %}
{% api %}

<!-- Segments -->

### Comment créer une segmentation lorsque j'importe un groupe d'utilisateurs via CSV ?

{% apitags %}
Segmentations
{% endapitags %}

Pour importer votre fichier CSV, accédez à la page **Importation d'utilisateurs** dans la section Utilisateurs. Le tableau des **importations récentes** répertorie jusqu'à vingt de vos importations les plus récentes, leur nom de fichier, le nombre de lignes dans le fichier, le nombre de lignes importées avec succès, le nombre total de lignes dans chaque fichier et l'état de chaque importation.

Le panneau " **Importer CSV** " contient des instructions pour l'importation et un bouton pour commencer l'importation. Cliquez sur **Select CSV File** et sélectionnez le fichier qui vous intéresse. Ensuite, avant de cliquer sur **Démarrer l'importation**, vous avez la possibilité d'indiquer à Braze ce qu'il doit faire de cette liste sous "Que voulez-vous que nous fassions avec les utilisateurs de ce CSV".

Sélectionnez **Importer des utilisateurs dans ce CSV et permettre également de recibler ce lot spécifique d'utilisateurs en tant que groupe**, puis sélectionnez **Générer automatiquement un segment à partir des utilisateurs qui sont importés à partir de ce CSV**. Après avoir cliqué sur **Démarrer l'importation**, Braze télécharge votre fichier, vérifie les en-têtes de colonne et les types de données de chaque colonne, et crée une segmentation.

Pour télécharger un modèle CSV, reportez-vous à l'[importation d'utilisateurs]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv).

{% endapi %}
{% api %}

### Quels types de filtres puis-je utiliser lors de la création d'un segment ?

{% apitags %}
Segmentations
{% endapitags %}

Le SDK de Braze met à votre disposition un puissant arsenal de filtres pour segmenter et cibler vos utilisateurs en fonction de fonctionnalités et d'attributs spécifiques. Vous pouvez utiliser le glossaire des [filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) pour rechercher ou restreindre ces filtres par catégorie de filtre (données personnalisées, activité de l'utilisateur, reciblage, activité marketing, attributs de l'utilisateur, attribution de l'installation, activité sociale, test, autre).

{% endapi %}
{% api %}

### Comment puis-je configurer le ciblage par emplacement afin de segmenter les utilisateurs en fonction de leur emplacement le plus récent et de l'utiliser dans mes campagnes et stratégies basées sur l'emplacement ?

{% apitags %}
Segmentations
{% endapitags %}

Naviguez jusqu'à la page **Segments**, sous Engagement, pour afficher tous vos segments d'utilisateurs actuels. Sur cette page, vous pouvez créer et nommer de nouvelles segmentations. Pour commencer, cliquez sur **Créer un segment** et donnez un nom à votre segment.

Une fois que vous avez créé votre segmentation, ajoutez un filtre `Most Recent Location` pour cibler les utilisateurs en fonction du dernier endroit où ils ont utilisé votre appli. Vous pouvez soit mettre en évidence les utilisateurs dans une région circulaire standard, soit créer une région polygonale personnalisée.

- Pour les emplacements circulaires, vous pouvez déplacer l'origine et ajuster le rayon d'emplacement/localisation de votre segmentation.
- Pour les régions polygonales, vous pouvez désigner plus précisément les zones que vous souhaitez inclure dans votre segment.

{% alert tip %}
Vous souhaitez tirer parti du ciblage des emplacements/localisations avec l'aide d'un partenaire de Braze ? Consultez nos [partenaires d'emplacement/localisation contextuelle]({{site.baseurl}}/partners/message_personalization/) Braze disponibles.
{% endalert %}

{% endapi %}
{% api %}

### Comment puis-je cibler des listes précises d'utilisateurs en fonction de leurs événements personnalisés et de leur comportement d'achat au cours des 365 derniers jours ?

{% apitags %}
Segmentations
{% endapitags %}

Vous pouvez utiliser les [extensions de segments]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)! Les extensions de segments vous permettent de cibler une liste d'utilisateurs plus précise qu'avec un segment classique.

Vous pouvez créer jusqu'à 10 extensions de segments par espace de travail. Une fois ces listes d'extensions générées, elles peuvent être incluses ou exclues en tant que filtre dans vos segmentations. Lors de la création d'une extension de segmentation, vous pouvez également spécifier que la liste doit être régénérée toutes les 24 heures.

1. Sous Engagements, développez **Segments** et cliquez sur **Extension de segment.**
2. Dans le tableau Extensions de segments, cliquez sur **\+ Créer une nouvelle extension.**
3. Nommez votre extension de segments en décrivant le type d'utilisateurs que vous souhaitez filtrer. Cela permettra de découvrir facilement et précisément cette extension lorsque vous l'appliquerez comme filtre dans votre segmentation.
4. Sélectionnez un critère d'achat ou d'événement personnalisé pour le ciblage.
5. Choisissez l'article acheté ou l'événement personnalisé spécifique que vous souhaitez cibler pour votre liste d'utilisateurs. 
6. Choisissez le nombre de fois (supérieur, inférieur ou égal) que l'utilisateur devrait avoir effectué l'événement, et le nombre de jours à prendre en compte, jusqu'à 365 jours.

Pour accroître la précision du ciblage, vous pouvez sélectionner **Ajouter des filtres de propriétés** et segmenter en fonction des propriétés spécifiques de votre achat ou de votre événement personnalisé. Braze prend en charge la segmentation des propriétés d'événement sur la base d'objets de type chaîne de caractères, numérique, booléen et temporel.

Nous prenons également en charge la segmentation basée sur les [propriétés d'événements imbriqués]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

Les extensions de segments reposent sur le stockage à long terme des propriétés d'événement et ne sont pas soumises à la limite de 30 jours de stockage des propriétés d'événement personnalisé. Cela signifie que vous pouvez consulter les propriétés d'événement suivies au cours de l'année écoulée, et que le suivi n'attend pas que l'extension ait été configurée au préalable.

{% alert note %}
L'utilisation des propriétés d'événement dans les extensions de segments n'a pas d'incidence sur l'utilisation des points de données.
{% endalert %}

{% endapi %}
{% api %}

#### Maintenir les extensions de segments à jour

{% apitags %}
Segmentations
{% endapitags %}

Vous pouvez préciser si vous souhaitez que cette extension représente un instantané unique dans le temps ou si vous souhaitez qu'elle se régénère quotidiennement. Votre extension commencera toujours à être traitée après l'enregistrement initial. Si vous souhaitez que l'extension soit régénérée quotidiennement, sélectionnez **Régénérer l'extension quotidiennement** et la régénération commencera chaque jour vers minuit dans le fuseau horaire de votre entreprise.

Lorsque vous avez terminé, cliquez sur **Enregistrer.** Le traitement de votre demande d'extension va commencer. Le temps nécessaire pour générer votre extension dépend du nombre d'utilisateurs, du nombre d'événements personnalisés ou d'événements d'achat que vous saisissez et du nombre de jours de l'historique.

Enfin, après avoir créé une extension, vous pouvez l'utiliser comme filtre lors de la création d'un segment ou de la définition d'une audience pour une campagne ou un Canvas. Commencez par choisir `Braze Segment Extension` dans la liste des filtres de la section **Attributs de l'utilisateur**. Dans la liste de filtres Extension du segment Braze, choisissez l'extension que vous souhaitez inclure ou exclure dans ce segment. Pour afficher les critères d'extension, cliquez sur **Afficher les détails de l'extension.** Vous pouvez maintenant procéder comme d'habitude à la création de votre segmentation.

{% endapi %}
{% api %}

<!-- Campaigns -->

### Comment créer une campagne multicanal ?

{% apitags %}
Campagnes
{% endapitags %}

Pour créer une campagne multicanal, accédez à la page **Campagnes**, sélectionnez **Créer une campagne**, puis sélectionnez **Campagne multicanal**. Dans une campagne multicanale, sélectionnez **Ajouter un canal de messages** dans l'onglet de composition pour ajouter les canaux souhaités. Cliquez sur les icônes de canaux qui apparaissent pour basculer entre les différents compositeurs d'envois de messages à mesure que vous créez le texte de votre campagne pour les différents canaux.

{% endapi %}
{% api %}

### Comment puis-je commencer à tester et à optimiser mes campagnes ?

{% apitags %}
Campagnes
{% endapitags %}

La création de campagnes multivariées et l'exécution de Canvas avec plusieurs variantes sont une excellente façon de commencer ! Par exemple, vous pouvez lancer une [campagne multivariée]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) pour tester un message avec différentes copies ou lignes d'objet. Les toiles comportant plusieurs variantes sont utiles pour tester des flux de travail entiers.

{% endapi %}
{% api %}

### Pourquoi y a-t-il une différence entre le nombre de destinataires uniques et le nombre d'envois pour une campagne ou un canvas donné ?

{% apitags %}
Campagnes
{% endapitags %}

Cette différence pourrait s'expliquer par le fait que la rééligibilité a été activée pour la campagne ou pour Canvas. En activant cette option, les utilisateurs qui remplissent les conditions requises pour le segment et les paramètres de réception/distribution pourront recevoir le message plus d'une fois. Si la rééligibilité n'est pas activée, l'explication probable de la différence entre les envois et les destinataires uniques peut être due au fait que les utilisateurs ont plusieurs appareils à travers les plateformes associées à leurs profils.

Par exemple, si vous avez un Canvas qui a des notifications push iOS et web, un utilisateur donné avec des appareils mobiles et de bureau pourrait recevoir plus d'un message.

{% endapi %}
{% api %}

### Qu'offre la réception/distribution locale ?

{% apitags %}
Campagnes
{% endapitags %}

La diffusion selon le fuseau horaire local vous permet d'envoyer des campagnes de messages à un segment en fonction du fuseau horaire de l'utilisateur. Sans réception/distribution locale, les campagnes seront planifiées en fonction des paramètres du fuseau horaire de votre entreprise dans Braze.

Par exemple, une entreprise basée à Londres qui envoie une campagne à 12 heures atteindra les utilisateurs de la côte ouest de l'Amérique à 4 heures du matin. Si votre application n'est disponible que dans certains pays, cela peut ne pas être un risque pour vous, sinon, nous vous recommandons vivement d'éviter d'envoyer des notifications push tôt le matin à votre base d'utilisateurs !

{% endapi %}
{% api %}

### Comment Braze reconnaît-il le fuseau horaire d'un utilisateur ?

{% apitags %}
Campagnes
{% endapitags %}

Braze déterminera automatiquement le fuseau horaire d'un utilisateur à partir de son appareil. Il est conçu pour assurer la précision des fuseaux horaires et la couverture complète de vos utilisateurs. Les utilisateurs créés par le biais de l'API utilisateur ou autrement sans fuseau horaire auront le fuseau horaire de votre entreprise comme fuseau horaire par défaut jusqu'à ce qu'ils soient reconnus dans votre application par le SDK.

Vous pouvez vérifier le fuseau horaire de votre entreprise dans les [paramètres de]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/) votre [entreprise]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/).

{% endapi %}
{% api %}

### Comment puis-je planifier une campagne sur un fuseau horaire local ?

{% apitags %}
Campagnes
{% endapitags %}

Lors de la planification d'une campagne, vous devez choisir de l'envoyer à une heure donnée, puis sélectionner **Envoyer la campagne aux utilisateurs dans leur fuseau horaire local**.

Braze recommande vivement de planifier toutes les campagnes dans les fuseaux horaires locaux 24 heures à l'avance. Étant donné qu'une telle campagne doit être envoyée au cours d'une journée entière, le fait de les planifier 24 heures à l'avance permet à votre message d'atteindre l'ensemble de votre segmentation. Toutefois, vous pouvez planifier ces campagnes moins de 24 heures à l'avance si nécessaire. N'oubliez pas que Braze n'enverra pas de messages aux utilisateurs qui ont dépassé l'heure d'envoi de plus d'une heure.

Par exemple, s'il est 13 heures et que vous planifiez une campagne pour un fuseau horaire local à 15 heures, la campagne sera immédiatement envoyée à tous les utilisateurs dont l'heure locale est de 15 à 16 heures, mais pas à ceux dont l'heure locale est de 17 heures. En outre, l'heure d'envoi que vous choisissez pour votre campagne ne doit pas encore avoir eu lieu dans le fuseau horaire de votre entreprise.

Modifier une campagne sur un fuseau horaire local programmée moins de 24 heures à l'avance ne modifiera pas la planification du message. Si vous décidez de modifier une campagne portant sur un fuseau horaire local pour l'envoyer à une heure plus tardive (par exemple, 19 heures au lieu de 18 heures), les utilisateurs qui faisaient partie du segment ciblé lorsque l'heure d'envoi initiale a été choisie recevront toujours le message à l'heure d'origine (18 heures). Si vous modifiez un fuseau horaire local pour que l'envoi se fasse plus tôt (par exemple, 16 heures au lieu de 17 heures), la campagne sera toujours envoyée à tous les membres du segment à l'heure d'origine (17 heures).

{% alert note %}
Pour les étapes du canvas, les utilisateurs n'ont pas besoin d'être dans l'étape pendant 24 heures pour recevoir l'étape suivante selon la réception/distribution locale.
{% endalert %}

Si vous avez autorisé les utilisateurs à redevenir éligibles pour la campagne, ils la recevront à nouveau à l'heure initiale (17 heures). Pour toutes les occurrences ultérieures de votre campagne, cependant, vos messages ne sont envoyés qu'à l'heure que vous avez mise à jour.

{% endapi %}
{% api %}

### Quand les changements apportés aux campagnes de fuseaux horaires locaux prennent-ils effet ?

{% apitags %}
Campagnes
{% endapitags %}

Les segments cibles pour les campagnes sur les fuseaux horaires locaux doivent inclure une fenêtre d'au moins 48 heures pour tout filtre basé sur l'heure afin de garantir la réception/distribution à l'ensemble du segment. Prenons l'exemple d'un segment ciblant les utilisateurs au cours de leur deuxième jour, avec les filtres suivants :

- Première utilisation de l'application il y a plus d'un jour
- Première utilisation il y a moins de 2 jours

La diffusion selon l'heure/distribution locale peut manquer aux utilisateurs de ce segment en fonction de l'heure de livraison et du fuseau horaire local de l'utilisateur. En effet, un utilisateur peut quitter le segment au moment où son fuseau horaire déclenche la réception/distribution.

{% endapi %}
{% api %}

### Quelles modifications puis-je apporter aux campagnes planifiées avant leur lancement ?

{% apitags %}
Campagnes
{% endapitags %}

Lorsque la campagne est planifiée, il faut modifier tout ce qui n'est pas la composition du message avant de mettre les messages en file d'attente pour l'envoi. Comme pour toutes les campagnes, vous ne pouvez pas modifier les événements de conversion une fois la campagne lancée.

{% endapi %}
{% api %}

### Quelle est la "zone de sécurité" avant que les messages d'une campagne planification ne soient mis en file d'attente ?

{% apitags %}
Campagnes
{% endapitags %}

- Les campagnes à planification unique peuvent être modifiées jusqu'à l'heure d'envoi prévue.
- Les campagnes à planification récurrente peuvent être modifiées jusqu'à l'heure d'envoi prévue.
- Les campagnes d'envoi local peuvent être modifiées jusqu'à 24 heures avant l'heure d'envoi planifiée.
- Les campagnes à heure d'envoi optimale peuvent être modifiées jusqu'à 24 heures avant le jour prévu pour l'envoi de la campagne.

{% endapi %}
{% api %}

### Que se passe-t-il si j'effectue une modification dans la "zone de sécurité" ?

{% apitags %}
Campagnes
{% endapitags %}

Modifier l'heure d'envoi des campagnes dans ce laps de temps peut entraîner un comportement indésirable, par exemple :

- Braze n'enverra pas de messages aux utilisateurs qui ont dépassé l'heure d'envoi de plus d'une heure.
- Les messages qui étaient déjà en file d'attente peuvent encore être envoyés à l'heure initialement prévue, plutôt qu'à l'heure ajustée.

{% endapi %}
{% api %}

### Que dois-je faire si la "zone de sécurité" est déjà dépassée ?

{% apitags %}
Campagnes
{% endapitags %}

Pour vous assurer que les campagnes fonctionnent comme vous le souhaitez, nous vous recommandons d'arrêter la campagne en cours (ce qui aura pour effet d'arrêter tous les messages en file d'attente). Vous pouvez ensuite dupliquer la campagne, en y apportant les modifications nécessaires, et lancer la nouvelle campagne. Vous devrez peut-être exclure de cette campagne les utilisateurs qui ont déjà reçu la première campagne.

Veillez à réajuster les heures de planification de la campagne pour tenir compte de l'envoi par fuseau horaire.

{% endapi %}
{% api %}

### Quand Braze évalue-t-il les utilisateurs pour la diffusion selon l'heure/distribution locale ?

{% apitags %}
Campagnes
{% endapitags %}

Pour la diffusion selon l'heure/distribution locale, Braze évalue l'éligibilité des utilisateurs à l'entrée au cours de ces deux instances :

- A l'heure de Samoa (UTC+13) du jour planifié
- À l'heure locale du jour planifié

Pour qu'un utilisateur soit éligible à la participation, il doit être éligible aux deux contrôles. Par exemple, si le lancement d'un Canvas est planifié pour le 7 août 2021 à 14 heures, fuseau horaire local, le ciblage d'un utilisateur situé à New York nécessiterait les vérifications d'éligibilité suivantes :

- New York le 6 août 2021 à 21 heures
- New York le 7 août 2021 à 14 heures

L'utilisateur doit se trouver dans le segment pendant les 24 heures précédant le lancement. Si l'utilisateur n'est pas éligible lors de la première vérification, Braze ne tentera pas la deuxième vérification.

{% endapi %}
{% api %}

### Pourquoi le nombre d'utilisateurs entrant dans une campagne ne correspond-il pas au nombre attendu ?

{% apitags %}
Campagnes
{% endapitags %}

Le nombre d'utilisateurs entrant dans une campagne peut être différent de celui que vous attendiez en raison de la manière dont les audiences et les déclencheurs sont évalués. Dans Braze, une audience est évaluée avant le déclencheur (à moins d'utiliser un [déclencheur de changement d'attribut]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Ainsi, les utilisateurs seront exclus de la campagne s'ils ne font pas initialement partie de votre audience sélectionnée avant que les actions déclencheurs ne soient évaluées.

{% endapi %}
{% api %}

<!-- Canvases -->

### Que se passe-t-il si l'audience et l'heure d'envoi sont identiques pour une toile qui a une variante, mais plusieurs branches ?

{% apitags %}
Toiles
{% endapitags %}

Nous mettons en file d'attente une tâche pour chaque étape - elles s'exécutent à peu près en même temps, et l'une d'entre elles "gagne". Dans la pratique, le tri peut être assez uniforme, mais il est probable qu'il y ait au moins un léger biais en faveur de l'étape qui a été créée en premier.

En outre, nous ne pouvons donner aucune garantie quant à la forme exacte que prendra cette distribution. Si vous souhaitez garantir un partage égal, ajoutez un filtre de [numéro de compartiment aléatoire]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/).

{% endapi %}
{% api %}

### Que se passe-t-il lorsque vous arrêtez une toile ?

{% apitags %}
Toiles
{% endapitags %}

Lorsque vous arrêtez une toile, les règles suivantes s'appliquent :

- Les utilisateurs ne pourront pas entrer dans la toile.
- Aucun autre message ne sera envoyé, quelle que soit la position de l'utilisateur dans le flux.
    - **Exception :** Email Canvases ne s'arrête pas immédiatement. Une fois que les demandes d'envoi sont envoyées à Sendgrid, nous ne pouvons rien faire pour les empêcher d'être transmises à l'utilisateur.

{% alert note %}
L'arrêt d'un canvas n'entraîne pas la sortie des utilisateurs en attente dans une étape. Si vous réactivez le Canvas et que les utilisateurs attendent toujours, ils termineront l'étape et passeront au composant suivant. Cependant, si le temps que l'utilisateur aurait dû passer au composant suivant s'est écoulé, il quittera le canvas.
{% endalert %}

{% endapi %}
{% api %}

### Quand un événement d'exception se déclenche-t-il ?

{% apitags %}
Toiles
{% endapitags %}

Les événements d'exception ne se déclenchent que lorsque l'utilisateur attend de recevoir le composant Canvas auquel il est associé. Si un utilisateur effectue une action à l'avancement, l'événement d'exception ne se déclenchera pas.

Si vous souhaitez exclure les utilisateurs qui ont effectué un certain événement à l'avance, utilisez plutôt des [filtres]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).

{% endapi %}
{% api %}

### Comment la modification d'un Canvas affecte-t-elle les utilisateurs déjà présents dans le Canvas ?

{% apitags %}
Toiles
{% endapitags %}

Si vous modifiez certaines des étapes d'un Canvas à plusieurs étapes, les utilisateurs qui faisaient déjà partie de l'audience mais qui n'ont pas reçu les étapes recevront la version mise à jour du message. Notez que cela ne se produira que s'ils n'ont pas encore été évalués pour l'étape en question.

Pour plus d'informations sur ce que vous pouvez ou ne pouvez pas modifier après le lancement, consultez la rubrique [Modifier votre canvas après le lancement]({{site.baseurl}}/post-launch_edits/).

{% endapi %}
{% api %}

### Comment les conversions des utilisateurs sont-elles suivies dans un canvas ?

{% apitags %}
Toiles
{% endapitags %}

Un utilisateur ne peut effectuer qu'une seule conversion par entrée dans le canvas.

Les conversions sont attribuées au message le plus récent reçu par l'utilisateur pour cette entrée. Le bloc de résumé au début d'un canvas reflète toutes les conversions effectuées par les utilisateurs à l'intérieur de ce canvas, qu'ils aient reçu un message ou non. Chaque étape suivante n'affichera que les conversions qui se sont produites pendant l'étape la plus récente que l'utilisateur a reçue.

{% details Use cases %}

#### Cas d'utilisation 1

Il y a un parcours Canvas avec 10 notifications push et l'événement de conversion est " début de session " (" ouvre l'appli ") :

- L'utilisateur A ouvre l'appli après être entré mais avant d'avoir reçu le premier message.
- L'utilisateur B ouvre l'application après chaque notification push.

**Résultat :**
Le résumé indiquera une conversion de deux, tandis que les étapes individuelles indiqueront une conversion de un pour la première étape et de zéro pour toutes les étapes suivantes.

{% alert note %}
Si les heures calmes sont actives au moment de l'événement de conversion, les mêmes règles s'appliquent.
{% endalert %}

#### Cas d'utilisation 2

Il existe une étape du canvas avec les heures calmes :

1. L'utilisateur entre dans le Canvas.
2. La première étape n'a pas de délai, mais se situe dans les heures calmes, de sorte que le message est supprimé.
3. L'utilisateur effectue l'événement de conversion.

**Résultat :**
L'utilisateur sera comptabilisé comme converti dans la variante globale du canvas, mais pas l'étape puisqu'il n'a pas reçu l'étape.

{% enddetails %}

{% endapi %}
{% api %}

### Si l'on considère le nombre d'utilisateurs uniques, l'analyse/analytique de Canvas ou la segmentation est-elle plus précise ?

{% apitags %}
Toiles
{% endapitags %}

Le segmenteur est une statistique plus précise pour les données d'utilisateurs uniques par rapport aux statistiques de Canvas ou de campagne. En effet, les statistiques de Canvas et de campagne sont des nombres que Braze incrémente lorsque quelque chose se produit, ce qui signifie qu'il existe des variables qui pourraient faire en sorte que ce nombre soit différent de celui de la segmentation. Par exemple, les utilisateurs peuvent se convertir plusieurs fois pour un canvas ou une campagne.  

{% endapi %}
{% api %}

### Pourquoi le nombre d'utilisateurs entrant dans un canvas ne correspond-il pas au nombre attendu ?

{% apitags %}
Toiles
{% endapitags %}

Le nombre d'utilisateurs entrant dans un Canvas peut différer de votre nombre attendu en raison de la façon dont les audiences et les déclencheurs sont évalués. Dans Braze, une audience est évaluée avant le déclencheur (à moins d'utiliser un déclencheur de [changement d'attribut]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value) ). Les utilisateurs qui ne font pas partie de l'audience sélectionnée seront exclus de la toile avant que les actions déclencheurs ne soient évaluées.

{% endapi %}
{% api %}

<!-- Analytics -->

### Quels sont les indicateurs mesurés par Braze ?

{% apitags %}
Analyse/analytique (si utilisé comme adjectif)
{% endapitags %}

En fonction du canal, Braze mesure une variété d'indicateurs pour vous permettre de déterminer le succès d'une campagne et d'informer les campagnes futures. Vous trouverez une liste complète dans notre [glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data/report_metrics/).

{% endapi %}
{% api %}

### Comment le chiffre d'affaires est-il calculé dans Braze ?

{% apitags %}
Analyse/analytique (si utilisé comme adjectif)
{% endapitags %}

Sur la page **Revenus**, vous pouvez consulter des données sur les revenus ou les achats sur des périodes spécifiques, pour un produit spécifique, ou le total des revenus ou des achats de votre appli. Ces chiffres d'affaires sont générés par les achats effectués par les destinataires de la campagne au cours d'une certaine période de conversion.

Ceci étant dit, il est important de noter que Braze est un outil de marketeur et non un outil de chiffre d'affaires. Notre [objet d'achat]({{site.baseurl}}/api/objects_filters/purchase_object/) ne prend pas en charge les remboursements et les annulations, il se peut donc que vous constatiez des écarts lorsque vous comparez les données avec d'autres outils.

{% endapi %}
{% api %}

### Quelles sont les capacités de reporting offertes par Currents ?

{% apitags %}
Analyse/analytique (si utilisé comme adjectif)
{% endapitags %}

Notre outil Currents transmet en continu les données d'engagement des messages et de comportement des clients à l'un de nos nombreux partenaires de données, ce qui vous permet d'utiliser les données uniques et précieuses créées par Braze pour alimenter vos efforts d'aide à la décision et d'analyse des clients chez d'autres partenaires de premier plan.

Ces données vont au-delà des indicateurs d'engagement des messages et peuvent également inclure des chiffres plus complexes tels que les attributs personnalisés et les performances des événements. Pour plus de détails, consultez notre [glossaire des événements en cours.]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/)

{% endapi %}
{% api %}

### Comment puis-je planifier un rapport d'engagement récurrent ?

{% apitags %}
Analyse/analytique (si utilisé comme adjectif)
{% endapitags %}

Pour planifier un rapport d'engagement récurrent, procédez comme suit :

1. Dans votre compte tableau de bord, accédez à **Rapports d'engagement**, sous **Données**.
2. Cliquez sur **\+ Créer un nouveau rapport**.
3. Ajoutez les [campagnes et les messages Canvas]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#manually-select-campaigns-or-canvases) (individuellement ou [par étiquette]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#automatically-select-campaigns-or-canvases)) que vous souhaitez compiler dans votre rapport.
4. [Ajoutez des statistiques]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#add-statistics-to-your-report) à votre rapport.
5. Sélectionnez la compression et l'élimination pour votre rapport.
6. Saisissez les adresses e-mail des utilisateurs de Braze qui doivent recevoir ce rapport.
7. Sélectionnez la [période]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#time-frame) à partir de laquelle vous souhaitez que votre rapport exécute des données.
8. Sélectionnez les [intervalles (quotidiens, hebdomadaires, etc.)]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#data-display) auxquels vous souhaitez voir la ventilation de vos données.
9. Planifiez l'[envoi de]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#send-immediately) votre rapport [immédiatement]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#send-immediately) ou à une [date ultérieure spécifiée]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#send-at-designated-time).
10. Exécutez le/un rapport, puis ouvrez-le dans votre e-mail dès son arrivée !

{% endapi %}
{% api %}

### Quelle est la différence entre les rapports d'engagement et le générateur de rapports ?

{% apitags %}
Analyse/analytique (si utilisé comme adjectif)
{% endapitags %}

Les rapports d'engagement vous fournissent des CSV de statistiques d'engagement pour des messages spécifiques des campagnes et des Canevas via un message déclenché. Certaines données sont agrégées au niveau de la campagne ou du Canvas plutôt qu'au niveau de la variante individuelle ou de l'étape canvas. Les rapports ne sont pas enregistrés dans le tableau de bord et le fait d'exécuter à nouveau le rapport peut permettre d'obtenir des statistiques actualisées.

Le générateur de rapports vous permet de comparer les résultats de plusieurs campagnes ou Canvas dans une seule vue afin que vous puissiez facilement déterminer quelles stratégies d'engagement ont eu le plus d'impact sur vos indicateurs clés. Pour les campagnes comme pour les toiles, vous pouvez exporter vos données et enregistrer votre rapport pour le consulter ultérieurement.

Pour plus d'informations sur l'utilisation des rapports et des analyses/analytiques dans Braze, reportez-vous à l'[aperçu des rapports.]({{site.baseurl}}/user_guide/analytics/reporting/reports_overview/)

{% endapi %}
