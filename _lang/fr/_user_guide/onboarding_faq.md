---
article_title: FAQ
hidden: true
permalink: /onboarding_faq/
excerpt_separator: ""
page_type: glossary
layout: onboarding_faq
description: "Cette page contient un ensemble de questions fréquemment posées, résumées par catégorie."

---

{% multi_lang_include video.html id="keAZAlBR9zc" source="youtube" %}


<!--- Users --->

{% api %}

### Comment puis-je traiter les données d’utilisateurs anonymes ?

{% apitags %}
Utilisateurs
{% endapitags %}

Initialement, lorsqu’un profil utilisateur est reconnu via le SDK, Braze crée un profil utilisateur anonyme avec un `braze_id` associé : un identifiant utilisateur unique défini par Braze.

Pour mieux suivre vos utilisateurs anonymes, vous pouvez implémenter les [alias utilisateurs]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-aliases) qui vous permettent d’étiqueter les utilisateurs anonymes avec un identifiant. Ces utilisateurs peuvent alors être exportés à l’aide de leurs alias ou référencés par l’API.

Si un profil utilisateur anonyme avec un alias est reconnu ultérieurement avec un `external_id`, il sera traité comme un profil utilisateur normal identifié, mais il conservera son alias existant et pourront toujours être référencés par cet alias.

Si vous désirez regrouper des alias utilisateurs avec des utilisateurs identifiés, vous pouvez regrouper tous les champs pertinents pour le profil que vous désirez conserver. Vous allez devoir exporter les données avant de le supprimer du profil utilisateur en utilisant notre endpoint [POST: Exportation de profil utilisateur par identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/). Vous pouvez alors utiliser notre endpoint [POST: Suivi d’utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour envoyer ces événements au profil que vous souhaitez conserver. Ceci vous permettra de préserver les données que vous souhaitez conserver, comme les attributs qui étaient enregistrés auparavant sur un profil et pas l’autre.

Consultez nos [meilleurs pratiques en matière d’obtention des données]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/) pour voir une description complète des méthodes permettant de recueillir les données des utilisateurs nouveaux ou existants dans Braze.

{% endapi %}
{% api %}

### Comment puis-je importer des utilisateurs recueillis et identifiés en dehors de Braze ?

{% apitags %}
Utilisateurs
{% endapitags %}

Pour importer des utilisateurs que vous avez déjà identifiés, vous pouvez charger un CSV dans Braze ou envoyer des données par l’API.

#### CSV

Vous pouvez charger et mettre à jour les profils d’utilisateur via des fichiers CSV sur la page **Importation d’utilisateurs**. Lors de l’importation des données client, vous devez spécifier l’identifiant unique de chaque client, également appelé `external_id`.

Avant de commencer votre importation CSV, il est important de voir avec votre équipe d’ingénierie comment les utilisateurs seront identifiés dans Braze. Ce sera généralement avec un ID d’une base données interne. Il devra être aligné sur la façon d’identifier les utilisateurs utilisée par le SDK Braze sur mobile et web, pour garantir que chaque client aura un seul profil utilisateur dans Braze pour tous ses appareils. En savoir plus sur le [cycle de vie du profil de l’utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/) dans Braze.

Lorsque vous indiquez un `external_id` dans votre importation, Braze mettra à jour un utilisateur existant avec le même `external_id`, ou créera un utilisateur nouvellement identifié avec ce `external_id` défini si Braze ne le trouve pas.

Consultez l’[importation d’utilisateurs]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv) pour obtenir plus d’informations et télécharger des modèles d’importation CSV.

#### API

Pour charger des utilisateurs par API, vous pouvez utiliser notre endpoint [POST: Suivi de l’utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour les importer dans Braze.

Si vous ne savez pas si l’utilisateur existe dans Braze, vous pouvez implémenter notre endpoint [POST: Exportation de profil utilisateur par identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) pour le vérifier. Si vous avez déterminé que l’utilisateur existe déjà dans Braze, vous pouvez utiliser notre endpoint POST: Suivi de l’utilisateur pour envoyer les nouvelles données que vous désirez ajouter au profil utilisateur existant déjà dans Braze.

{% alert note %}
Gardez les nuances suivantes à l’esprit lorsque vous utilisez l’endpoint `/users/track` :

- Lorsque vous créez des utilisateurs alias uniquement par le biais de cet endpoint, vous devez explicitement définir l’indicateur `_update_existing_only` comme faux.
- La mise à jour du statut d’abonnement avec cet endpoint mettra à jour l’utilisateur spécifié par son `external_id` (comme User1) et mettre à jour le statut de l’abonnement de tous les utilisateurs ayant le même e-mail que cet utilisateur (Utilisateur1).
{% endalert %}

{% endapi %}
{% api %}

### Qu’elle est la différence entre les statuts d’abonnement aux notifications push ?

{% apitags %}
Utilisateurs
{% endapitags %}

Il existe trois options d’état d’abonnement aux notifications push : abonné, inscrit et désabonné.

Par défaut, pour que votre utilisateur reçoive vos messages par le biais de notifications push, l’état de son abonnement doit être soit abonné soit inscrit, et il doit être « activé pour les notifications push ». Vous pouvez écraser ce paramétrage si nécessaire lors de la rédaction d’un message.

|État autorisé|Description|
|---|---|
|Abonné| État d’abonnement aux notifications push par défaut lorsqu’un profil utilisateur est créé dans Braze. |
|Autorisé| Un utilisateur a explicitement exprimé une préférence pour recevoir des notifications push. Braze déplace automatiquement l’état inscrit d’un utilisateur vers `Opted-In` si celui-ci accepte une invite de notification push au niveau du système d’exploitation.<br><br>Ceci ne s’applique pas aux utilisateurs sur Android 12 ou antérieur.|
|Désabonné| Un utilisateur s’est explicitement désabonné des notifications push par le biais de votre application ou d’autres méthodes fournies par votre marque. Par défaut, les campagnes de notification push de Braze ciblent uniquement les utilisateurs qui sont `Subscribed` ou `Opted-in` pour les notifications push.|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
{% api %}

### Que faire si j’ai identifié des utilisateurs en double ?

{% apitags %}
Utilisateurs
{% endapitags %}

Si vous avez identifié des utilisateurs en double, vous devrez nettoyer ces profils utilisateurs. Vous pouvez suivre les étapes suivantes :

1. Exportez les profils utilisateurs en utilisant notre endpoint d’API users/export/ids.
2. Identifiez le bon profil utilisateur (votre équipe devra, au final, déterminer l’information correcte) et soit :
    - Fusionnez tous les champs pertinents du profil utilisateur que vous désirez conserver en utilisant l’endpoint user/track.
    - Supprimez le doublon, le profil qui n’est pas utile, sans fusionner de données en utilisant l’endpoint users/delete. **Il est impossible de récupérer des informations** une fois que vous avez supprimé un profil utilisateur.

{% alert important %}
Nous vous recommandons d’importer tout d’abord les `external_id` corrects ainsi que les événements et attributs personnalisés correspondants vers les nouveaux profils utilisateurs. Une fois les profils utilisateurs supprimés, ils ne peuvent pas être récupérés. La suppression devrait donc être la toute dernière étape.
{% endalert %}

Quelques points supplémentaires à prendre en compte :

- Toutes les données d’engagement (telles que les campagnes ou les Canvas reçus) sur les profils utilisateurs en double seront perdues. La seule manière de conserver le contexte d’engagement d’origine se fait en ajoutant un attribut personnalisé (tel qu’un attribut personnalisé sous forme de tableau de toutes les campagnes et les Canvas reçus).
- Lorsque vous migrez des profils utilisateurs, votre équipe doit décider quel profil utilisateur en double conserver. Braze ne peut pas décider ou vous fournir une liste d’utilisateurs à supprimer.  
- Au final, il sera important pour votre équipe d’évaluer le profil d’enregistrement de l’expérience de votre utilisateur et de s’assurer que vous n’appelez que la méthode `changeUser()` quand un utilisateur est identifié.

{% endapi %}
{% api %}

<!-- Segments -->

### Comment puis-je créer un segment lorsque j’importe un groupe d’utilisateur par CSV ?

{% apitags %}
Segments
{% endapitags %}

Pour importer votre fichier CSV, allez sur la page **user Import** dans la section Utilisateurs. Le tableau **Importations récentes** répertorie vos importations les plus récentes (20 maximum), avec les noms des fichiers, le nombre de lignes dans le fichier, le nombre de lignes importées avec succès, le nombre de lignes totales dans chaque fichier et le statut de chaque importation.

Le panneau **Importer CSV**, affiche les instructions d’importation et a un bouton pour commencer votre importation. Cliquez sur **Sélectionner fichier CSV** et sélectionnez votre fichier. Ensuite, avant de cliquer sur **Débuter l’importation**, vous avez la possibilité de dire à Braze quoi faire de cette liste dans « Que vouliez-vous que nous fassions avec les utilisateurs de ce CSV ? ».

Sélectionnez **Importer les utilisateurs de se CSV et faire en sorte de pouvoir également recibler cet ensemble d’utilisateurs donnés en tant que groupe**, puis sélectionnez **Générer automatiquement un segment à partir des utilisateurs qui sont importés depuis ce CSV**. Une fois que vous cliquez sur **Débuter l’importation**, Braze chargera votre fichier, vérifiera les en-têtes de colonne et les types de données pour chacune et créera un segment.

Pour télécharger un modèle de CSV, consultez l’[importation d’utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv).

{% endapi %}
{% api %}

### Quels types de filtres puis-je utiliser lors de la création d’un segment ?

{% apitags %}
Segments
{% endapitags %}

Le SDK de Braze vous propose un vaste arsenal de filtres pour segmenter et cibler vos utilisateurs en fonction de fonctionnalités et d’attributs spécifiques. Vous pouvez utiliser le glossaire des [filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) pour rechercher et affiner ces filtres par catégorie (données personnalisées, activité de l’utilisateur, reciblage, activité marketing, attributs utilisateur, attribution d’installation, activité sociale, tests et autres).

{% endapi %}
{% api %}

### Comment puis-je paramétrer le ciblage de position pour pouvoir segmenter les utilisateurs en fonction de leur emplacement le plus récent et l’utiliser dans mes stratégies et mes campagnes basées sur la position ?

{% apitags %}
Segments
{% endapitags %}

Accédez à la page **Segments**, dans Engagement, pour afficher tous vos segments d’utilisateurs actuels. Sur cette page, vous pouvez créer et nommer de nouveaux segments. Pour commencer, cliquez sur **Create Segment (Créer un segment)** et nommez votre segment.

Après avoir créé votre segment, ajoutez un filtre `Most Recent Location` pour cibler les utilisateurs en fonction du dernier emplacement où ils ont utilisé votre application. Vous pouvez sélectionner des utilisateurs dans une région circulaire standard ou créer une région polygonale personnalisée.

- Avec les régions circulaires, vous pouvez déplacer l’origine et ajuster le rayon de votre segmentation.
- Avec les régions polygonales, vous pouvez désigner les zones que vous souhaitez inclure dans votre segment de manière plus précise.

{% alert tip %}
Vous souhaitez tirer parti du ciblage de localisation avec l’aide d’un partenaire Braze ? Découvrez les [partenaires de localisation contextuelle]({{site.baseurl}}/partners/message_personalization/location) de Braze.
{% endalert %}

{% endapi %}
{% api %}

### Comment puis-je cibler des listes précises d’utilisateurs sur la base de leurs événements personnalisés ou leur comportement d’achat sur les 365 derniers jours ?

{% apitags %}
Segments
{% endapitags %}

Vous pouvez utiliser les [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) ! Les Segment Extensions vous permettent de cibler une liste d’utilisateurs plus fine que vous ne pourriez le faire avec un segment habituel.

Vous pouvez créer jusqu’à 10 Segment Extensions par groupe d’apps. Une fois ces listes d’extension générées, elles peuvent être incluses ou exclues de vos segments sous forme de filtres. Lorsque vous créez une Segment Extension, vous pouvez également choisir que la liste soit renouvelée une fois toutes les 24 heures.

1. Dans **Engagements**, développez la liste **Segments et cliquez sur Segment Extension**.
2. Dans le tableau Segment Extension, cliquez sur **+ Créer une nouvelle extension**.
3. Nommez votre Segment Extension en décrivant le type d’utilisateur que vous souhaitez cibler. Cela vous permettra de retrouver facilement cette extension lorsque vous souhaiterez l’utiliser en tant que filtre dans votre segment.
4. Sélectionnez un critère d’achat ou d’événement personnalisé pour le ciblage.
5. Choisissez quel produit acheté ou événement personnalisé donné doit être ciblé pour votre liste d’utilisateur. 
6. Choisissez le nombre de fois (supérieur à, inférieur à ou égal à) que l’utilisateur devra avoir effectué l’événement et le nombre de jours que vous souhaitez analyser (365 jours maximum).

Pour améliorer la précision du ciblage, vous pouvez sélectionner **Ajouter des filtres de propriété** et segmenter en fonctions des propriétés spécifiques de votre achat ou événement personnalisé. Braze prend en charge la segmentation des propriétés de l’événement en fonction des objets de chaîne de caractères, numériques, booléens et temporels.

Nous prenons également en charge la segmentation basée sur les [Propriétés d’événement imbriqué]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#nested-objects).

Les Segment Extensions s’appuient sur le stockage à long terme des propriétés de l’événement et ne sont pas soumises à la limite de stockage des propriétés d’événement personnalisé de 30 jours. Cela signifie que vous pouvez analyser les propriétés de l’événement suivies au cours de l’année, et que le suivi ne doit pas attendre que l’extension ait été configurée en premier.

{% alert note %}
L’utilisation de propriétés d’événement dans des Segment Extensions n’affecte pas l’utilisation de vos points de données.
{% endalert %}

{% endapi %}
{% api %}

#### Maintenir les Segment Extensions à jour

{% apitags %}
Segments
{% endapitags %}

Vous pouvez indiquer si vous souhaitez que cette extension représente une instantanée à un moment T, ou si vous souhaitez que cette extension soit renouvelée quotidiennement. Votre extension sera toujours traitée après la sauvegarde initiale. Si vous souhaitez que l’extension soit renouvelée quotidiennement, sélectionnez **Renouveler quotidiennement l’extension** et l’extension sera régénérée chaque jour à partir de minuit selon le fuseau horaire de votre entreprise.

Lorsque vous avez fini, cliquez sur **Enregistrer**. Votre extension va commencer à être traitée. La durée nécessaire pour générer votre extension dépend du nombre d’utilisateurs que vous avez, du nombre d’événements personnalisés ou d’événements d’achat que vous collectez, et du nombre de jours que vous analysez dans l’historique.

Enfin, après avoir créé une extension, vous pouvez l’utiliser comme filtre lorsque vous créez un segment ou définissez une audience pour une campagne ou un Canvas. Commencez par choisir `Braze Segment Extension` dans la liste des filtres dans la section **Attributs utilisateur**. Dans la liste des filtres Braze Segment Extension, choisissez l’extension que vous souhaitez inclure ou exclure de ce segment. Pour afficher les critères d’extension, cliquez sur **Afficher les détails de l’extension**. Vous pouvez maintenant créer votre segment comme vous le faites habituellement.

{% endapi %}
{% api %}

<!-- Campagnes -->

### Comment créer une campagne multicanale ?

{% apitags %}
Campagnes
{% endapitags %}

Pour créer une campagne multicanale, rendez-vous sur la page **Campagnes**, sélectionnez **Créer une campagne** puis **Campagne multicanale**. Une fois dans une campagne multicanale, sélectionnez **Ajouter un canal de messagerie** depuis l’onglet « Composer » pour ajouter les canaux souhaités. Cliquez sur les icônes de canal qui apparaissent pour basculer entre différents composeurs de messages lorsque vous créez le texte de votre campagne pour les différents canaux.

{% endapi %}
{% api %}

### Comment puis-je commencer à tester et optimiser les campagnes ?

{% apitags %}
Campagnes
{% endapitags %}

La création de campagnes multivariées et l’exécution de Canvas avec plusieurs variantes sont un excellent moyen de commencer ! Par exemple, vous pouvez exécuter une [campagne multivariée]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) pour tester un message comportant des textes ou des lignes Objet variés. Les Canvas avec plusieurs variantes sont utiles pour tester des flux de travail entiers.

{% endapi %}
{% api %}

### Pourquoi y a-t-il une différence entre le nombre de destinataires uniques et le nombre d’envois pour une campagne ou un Canvas donné ?

{% apitags %}
Campagnes
{% endapitags %}

Une explication potentielle de cette différence peut venir de l’activation de la rééligibilité pour la campagne ou le Canvas. Pour ce faire, les utilisateurs qui remplissent les conditions requises pour les paramètres de segment et de livraison pourront recevoir le message plusieurs fois. Si la rééligibilité n’est pas activée, l’explication probable de la différence entre les envois et les destinataires uniques peut venir des utilisateurs ayant plusieurs appareils, sur plusieurs plateformes, associés à leurs profils.

Par exemple, si vous avez un Canvas qui dispose à la fois d’une notification push iOS et Web, un utilisateur donné possédant à la fois un téléphone et un ordinateur de bureau peut recevoir plus d’un message.

{% endapi %}
{% api %}

### Qu’est-ce que l’offre de livraison selon le fuseau horaire local ?

{% apitags %}
Campagnes
{% endapitags %}

La livraison selon le fuseau horaire local vous permet de livrer des campagnes de messagerie à un segment en fonction du fuseau horaire individuel d’un utilisateur. Sans la livraison selon le fuseau horaire local, les campagnes seront planifiées en fonction des paramètres de fuseau horaire de votre société dans Braze.

Par exemple, une société basée à Londres qui envoie une campagne à midi atteindra les utilisateurs sur la côte ouest de l’Amérique à 4 h du matin. Si votre application n’est disponible que dans certains pays, cela peut ne pas représenter un risque pour vous, sinon nous vous recommandons vivement d’éviter d’envoyer des notifications push matinales à votre base d’utilisateurs !

{% endapi %}
{% api %}

### Comment Braze connaît-t-il le fuseau horaire d’un utilisateur ?

{% apitags %}
Campagnes
{% endapitags %}

Braze détermine automatiquement le fuseau horaire d’un utilisateur à partir de son appareil. Cela garantit une précision de fuseau horaire et une couverture complète de vos utilisateurs. Les utilisateurs créés via l’API utilisateur ou n’ayant pas de fuseau horaire prendront celui de votre entreprise comme fuseau horaire par défaut jusqu’à ce qu’ils soient identifiés dans votre application par le SDK.

Vous pouvez vérifier le fuseau horaire de votre entreprise dans vos [Paramètres de l’entreprise]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/company-wide_settings_management/).

{% endapi %}
{% api %}

### Comment planifier une campagne selon un fuseau horaire local ?

{% apitags %}
Campagnes
{% endapitags %}

Lors de la planification d’une campagne, vous devez choisir de l’envoyer à un moment donné, puis sélectionner **Envoyer une campagne aux utilisateurs selon leur fuseau horaire local**.

Braze recommande vivement que toutes les campagnes selon le fuseau horaire local soient planifiées 24 heures à l’avance. Puisque cette campagne doit être envoyée au cours d’une journée entière, les planifier 24 heures à l’avance garantit que votre message atteindra votre segment tout entier. Cependant, vous pouvez planifier ces campagnes moins de 24 heures à l’avance si nécessaire. N’oubliez pas que Braze n’enverra pas de messages aux utilisateurs qui ont manqué l’heure d’envoi de plus d’une heure.

Par exemple, s’il est 13 h et que vous planifiez une campagne selon un fuseau horaire local pour 15 h, la campagne sera envoyée immédiatement à tous les utilisateurs dont l’heure locale est de 15 h à 16 h, mais pas aux utilisateurs dont l’heure locale est 17 h. De plus, l’heure d’envoi que vous choisissez pour votre campagne ne doit pas encore être dépassée dans le fuseau horaire de votre société.

La modification d’une campagne selon un fuseau horaire local qui est programmée moins de 24 heures à l’avance ne modifiera pas la planification du message. Si vous décidez de modifier une campagne selon un fuseau horaire local pour qu’elle soit envoyée ultérieurement (par exemple, à 19 h au lieu de 18 h), les utilisateurs qui se trouvaient dans le segment ciblé lorsque l’heure d’envoi initiale a été choisie recevront toujours le message à l’heure d’origine (18 h). Si vous modifiez un fuseau horaire local pour que l’envoi se fasse plus tôt (par exemple, à 16 h au lieu de 17 h), la campagne sera toujours envoyée à tous les membres du segment à l’heure d’origine (17 h).

{% alert note %}
Pour les Canvas Step, les utilisateurs n’ont pas besoin d’être dans l’étape pendant 24 heures pour recevoir l’étape suivante lors de la livraison selon un fuseau horaires local.
{% endalert %}

Si vous avez permis aux utilisateurs de devenir rééligibles pour la campagne, ils la recevront une nouvelle fois à l’heure d’origine (17 h). Cependant, pour toutes les occurrences ultérieures de votre campagne, vos messages ne seront envoyés que lors de votre mise à jour.

{% endapi %}
{% api %}

### Quand les changements apportés aux campagnes selon un fuseau horaire local prennent-ils effet ?

{% apitags %}
Campagnes
{% endapitags %}

Les segments cibles pour les campagnes selon un fuseau horaire local doivent inclure une fenêtre de 48 heures au moins pour que les filtres temporels garantissent la livraison au segment tout entier. Par exemple, imaginez un segment ciblant les utilisateurs lors de leur deuxième jour avec les filtres suivants :

- Première utilisation de l’application il y a plus d’un jour
- Première utilisation de l’application il y a moins de 2 jours

La livraison selon un fuseau horaire local peut manquer les utilisateurs de ce segment en fonction du temps de livraison et de leur fuseau horaire local. Ceci est dû à la possibilité que l’utilisateur quitte le segment avant que son fuseau horaire ne déclenche la livraison.

{% endapi %}
{% api %}

### Quels changements puis-je apporter aux campagnes planifiées avant le lancement ?

{% apitags %}
Campagnes
{% endapitags %}

Lorsque la campagne est planifiée, les modifications touchant autre chose que la composition du message doivent être effectuées avant qu’il ne soit placé dans la file d’attente d’envoi. Comme pour toutes les campagnes, vous ne pouvez pas modifier les événements de conversion après le lancement de la campagne.

{% endapi %}
{% api %}

### Quelle est la « zone sécurisée » avant que les messages d’une campagne programmée soient placés en file d’attente ?

{% apitags %}
Campagnes
{% endapitags %}

- Les campagnes planifiées ponctuelles peuvent être modifiées jusqu’à l’heure d’envoi prévue.
- Les campagnes planifiées récurrentes peuvent être modifiées jusqu’à l’heure d’envoi prévue.
- Les campagnes à heure d’envoi locale peuvent être modifiées jusqu’à 24 heures avant l’heure d’envoi prévue.
- Les campagnes à heure d’envoi optimale peuvent être modifiées jusqu’à 24 heures avant le jour où la campagne est planifiée pour l’envoi.

{% endapi %}
{% api %}

### Que faire si je fais une modification dans la « zone sécurisée » ?

{% apitags %}
Campagnes
{% endapitags %}

Changer l’heure d’envoi sur les campagnes à ce moment-là peut entraîner un comportement indésirable, par exemple :

- Braze n’enverra pas de messages aux utilisateurs qui ont manqué l’heure d’envoi de plus d’une heure.
- Les messages placés en file d’attente à l’avance peuvent toujours être envoyés à l’heure initialement prévue, plutôt qu’à l’heure modifiée.

{% endapi %}
{% api %}

### Que dois-je faire si la « zone sécurisée » est déjà passée ?

{% apitags %}
Campagnes
{% endapitags %}

Afin de garantir que les campagnes fonctionnent comme souhaité, nous vous recommandons d’arrêter la campagne actuelle (ceci annulera tous les messages qui ont été placés en file d’attente). Vous pouvez ensuite dupliquer la campagne, apporter les modifications nécessaires et lancer la nouvelle campagne. Vous devrez peut-être exclure les utilisateurs de cette campagne qui ont déjà reçu la première.

Assurez-vous de réajuster les heures de planification de la campagne pour permettre l’envoi selon un fuseau horaire.

{% endapi %}
{% api %}

### Quand Braze évalue-t-il les utilisateurs pour la livraison selon un fuseau horaire local ?

{% apitags %}
Campagnes
{% endapitags %}

Pour la livraison selon un fuseau horaire local, Braze évalue les utilisateurs pour leur éligibilité à l’entrée à deux moments :

- À l’heure des Samoa (UTC + 13) du jour planifié
- À l’heure locale du jour planifié

Pour que l’utilisateur puisse être admissible à l’entrée, il doit être admissible pour les deux vérifications. Par exemple, si un Canvas est prévu pour être lancé le 7 août 2021 à 14 h du fuseau horaire local, cibler un utilisateur situé à New York nécessite les vérifications d’admissibilité suivantes :

- New York, le 6 août 2021 à 21 h
- New York, le 7 août 2021 à 14 h

L’utilisateur doit être dans le segment pendant 24 heures avant le lancement. Si l’utilisateur n’est pas admissible à la première vérification, alors Braze n’essaiera pas de faire la deuxième.

{% endapi %}
{% api %}

### Pourquoi le nombre d’utilisateurs qui accèdent à une campagne ne correspond pas au nombre prévu ?

{% apitags %}
Campagnes
{% endapitags %}

Le nombre d’utilisateurs accédant à une campagne peut être différent du nombre prévu selon le mode d’évaluation des audiences et des déclencheurs. Dans Braze, une audience est évaluée avant le déclencheur (sauf si un déclencheur [modification d’attribut]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers#change-custom-attribute-value) est utilisé). Les utilisateurs seront alors exclus de la campagne s’ils ne font pas partie de l’audience que vous avez sélectionnée au départ, avant l’évaluation des actions de déclenchement.

{% endapi %}
{% api %}

<!-- Canvas -->

### Que se passe-t-il si l’audience et l’heure d’envoi sont identiques pour un Canvas qui a une variante, mais plusieurs branches ?

{% apitags %}
Canvas
{% endapitags %}

Nous mettons en file d’attente un travail pour chaque étape, ils sont exécutés à peu près simultanément et l’un d’entre eux « gagne ». En pratique ce processus peut être quelque peu uniforme, mais il y a parfois une légère distorsion par rapport à l’étape créée en premier.

De plus, nous ne pouvons pas garantir avec précision ce à quoi ressemblera cette répartition. Si vous voulez garantir un fractionnement uniforme, ajoutez un filtre [numéro de compartiment aléatoire]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/ab_testing_with_random_buckets/).

{% endapi %}
{% api %}

### Que se passe-t-il lorsque vous arrêtez un Canvas ?

{% apitags %}
Canvas
{% endapitags %}

Lorsque vous arrêtez un Canvas, les éléments suivants s’appliquent :

- L’accès au Canvas sera bloqué pour les utilisateurs.
- Plus aucun message ne sera envoyé, quel que soit le niveau auquel se situe un utilisateur dans le flux.
    - **Exception :** Les Canvas e-mail ne seront pas automatiquement arrêtés. Une fois que les requêtes sont transmises à SendGrid, nous ne pouvons rien faire pour arrêter la livraison à l’utilisateur.

{% alert note %}
Arrêter un Canvas ne fera pas sortir les utilisateurs qui attendent dans une étape. Si vous réactivez le Canvas et que les utilisateurs attendent toujours, ils finiront l’étape et passeront au composant suivant. Cependant, si le délai durant lequel l’utilisateur aurait dû passer au composant suivant est dépassé, il quittera le Canvas.
{% endalert %}

{% endapi %}
{% api %}

### À quel moment un événement d’exception est-il déclenché ?

{% apitags %}
Canvas
{% endapitags %}

[Les événements d’exception]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events/) sont uniquement déclenchés alors qu’un utilisateur attend de recevoir le composant de l’étape Canvas associée. Si un utilisateur effectue une action à l’avance, l’événement d’exception ne sera pas déclenché.

Si vous souhaitez créer une exception pour des utilisateurs ayant effectué un événement spécifique en avance, utilisez plutôt [filtres]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).

{% endapi %}
{% api %}

### En quoi la modification d’un Canvas affecte-t-elle des utilisateurs déjà présents dans les Canvas ?

{% apitags %}
Canvas
{% endapitags %}

Si vous modifiez certaines étapes d’un Canvas à plusieurs étapes, les utilisateurs qui étaient déjà dans l’audience, mais n’ayant pas encore reçu les étapes, recevront la version mise à jour du message. Notez que ce cas se produit uniquement s’ils n’ont pas encore été évalués pour l’étape.

Pour plus d’informations sur ce que vous pouvez modifier ou pas après le lancement, consultez [Modification de votre Canvas après le lancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/change_your_canvas_after_launch/).

{% endapi %}
{% api %}

### Comment le suivi des conversions utilisateur est-il effectué dans Canvas ?

{% apitags %}
Canvas
{% endapitags %}

Un utilisateur peut uniquement effectuer une conversion par entrée Canvas.

Les conversions sont affectées au message le plus récent reçu par l’utilisateur pour cette entrée. Le blocage de synthèse au début d’un Canvas illustre toutes les conversions effectuées par les utilisateurs dans ce parcours, qu’ils aient reçu un message ou pas. Chaque message suivant affichera uniquement les conversions effectuées lorsque l’utilisateur a reçu l’étape la plus récente.

{% details Exemples %}

#### Exemple 1

Il existe un chemin Canvas avec 10 notifications push et l’événement de conversion est « lancement de session » (« Ouvre l’application ») :

- L’utilisateur A ouvre l’application après l’accès, mais avant la réception du premier message.
- L’utilisateur B ouvre l’application après chaque notification push.

**Résultat :**
La synthèse affichera deux conversions alors que chaque étape affichera une conversion pour la première étape et aucune conversion pour toutes les étapes suivantes.

{% alert note %}
Si des heures calmes sont actives lorsque l’événement de conversion se produit, les mêmes règles s’appliquent.
{% endalert %}

#### Exemple 2

Il existe un Canvas avec des heures calmes :

1. L’utilisateur accède au Canvas.
2. La première étape ne présente pas de retard, mais se situe dans les heures calmes, le message est donc supprimé.
3. L’utilisateur effectue l’événement de conversion.

**Résultat :**
La conversion de l’utilisateur sera prise en compte dans l’ensemble de Canvas Variant, mais pas l’étape, faute d’avoir été reçue.

{% enddetails %}

{% endapi %}
{% api %}

### Lorsqu’on examine le nombre d’utilisateurs uniques, l’analyse Canvas est-elle plus précise que la segmentation ?

{% apitags %}
Canvas
{% endapitags %}

La segmentation est une statistique plus précise pour les données de l’utilisateur unique par rapport aux statistiques de Canvas ou de la campagne. Cela est dû au fait que les statistiques Canvas et des campagnes sont des nombres incrémentés par Braze en fonction des opérations effectuées. En d’autres termes, des variables peuvent entraîner cette différence de nombre par rapport à l’outil de segmentation. Par exemple, des utilisateurs peuvent effectuer plus de conversions pour un Canvas ou une campagne.  

{% endapi %}
{% api %}

### Pourquoi le nombre d’utilisateurs qui accèdent à un Canvas ne correspond pas au nombre prévu ?

{% apitags %}
Canvas
{% endapitags %}

Le nombre d’utilisateurs accédant à un Canvas peut être différent du nombre prévu selon le mode d’évaluation des audiences et des déclencheurs. Dans Braze, une audience est évaluée avant le déclencheur (sauf si un déclencheur [modification d’attribut]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value) est utilisé). Les utilisateurs seront alors exclus du Canvas s’ils ne font pas partie de l’audience que vous avez sélectionnée, avant l’évaluation des actions de déclenchement.

{% endapi %}
{% api %}

<!-- Analytique -->

### Quels sont les indicateurs mesurés par Braze ?

{% apitags %}
Analytique
{% endapitags %}

Selon le canal, Braze mesure plusieurs indicateurs pour vous permettre de déterminer la réussite d’une campagne et renseigner les campagnes futures. Vous pouvez en trouver une liste détaillée dans notre [glossaire d’indicateurs rapportés]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics).

{% endapi %}
{% api %}

### Comment sont calculés les revenus dans Braze ?

{% apitags %}
Analytique
{% endapitags %}

Sur la page **Revenus**, vous pouvez afficher les données sur les revenus ou les achats pour des périodes spécifiques, pour un produit spécifique, ou voir le chiffre d’affaires total ou les achats totaux pour votre application. Ces valeurs de revenus sont générées à partir des achats réalisés par les destinataires des campagnes durant une période de conversion donnée.

Ceci dit, il est important de prendre en compte le fait que Braze est un outil de marketing et non de gestion des revenus. Notre [objet d’achat]({{site.baseurl}}/api/objects_filters/purchase_object/) ne prend pas en charge les remboursements ou les annulations et vous pourrez donc constater des écarts en comparant les données avec d’autres outils.

{% endapi %}
{% api %}

### Quelles autres capacités de reporting permet Currents ?

{% apitags %}
Analytique
{% endapitags %}

Currents diffuse continuellement des données d’engagement de messagerie et de comportement des clients à l’un de nos nombreux partenaires de données, vous permettant d’utiliser les données uniques et précieuses que Braze crée pour alimenter vos efforts d’aide à la décision et d’analyse avec d’autres partenaires de premier ordre.

Ces données vont au-delà des simples indicateurs d’engagement des envois de message, mais peuvent aussi comprendre des valeurs plus complexes comme les attributs personnalisés et la performance de l’événement. Pour plus de détails, consultez notre [glossaire des événements Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events).

{% endapi %}
{% api %}

### Comment puis-je planifier un rapport d’engagement récurrent ?

{% apitags %}
Analytique
{% endapitags %}

Pour planifier un rapport d’engagement récurrent, faites ce qui suit :

1. Dans votre compte de tableau de bord, naviguez jusqu’à **Rapports d’engagement**, sous **Données**.
2. Cliquez sur **+ Créer un nouveau rapport**.
3. Ajoutez les [messages des campagnes et du Canvas]({{site.baseurl}}//user_guide/data_and_analytics/reporting/engagement_reports/#manually-select-campaigns-or-canvases) (individuellement ou [par balise]({{site.baseurl}}//user_guide/data_and_analytics/reporting/engagement_reports/#automatically-select-campaigns-or-canvases)) que vous souhaitez compiler dans votre rapport.
4. [Ajouter des statistiques]({{site.baseurl}}//user_guide/data_and_analytics/reporting/engagement_reports/#add-statistics-to-your-report) à votre rapport.
5. Sélectionnez la compression et le délimiteur pour votre rapport.
6. Entrez les adresses e-mail des utilisateurs de Braze qui recevront ce rapport.
7. Sélectionnez la [période]({{site.baseurl}}//user_guide/data_and_analytics/reporting/engagement_reports/#time-frame) pour les données qui seront affichées dans votre rapport.
8. Sélectionnez les [intervalles (quotidien, hebdomadaire, etc.)]({{site.baseurl}}//user_guide/data_and_analytics/reporting/engagement_reports/#data-display) pour la ventilation de vos données.
9. Indiquez si le rapport doit être [envoyé immédiatement]({{site.baseurl}}//user_guide/data_and_analytics/reporting/engagement_reports/#send-immediately) ou à une [date future spécifiée]({{site.baseurl}}//user_guide/data_and_analytics/reporting/engagement_reports/#send-at-designated-time).
10. Exécutez le rapport, puis ouvrez-le dans votre e-mail quand il arrive !

{% endapi %}
{% api %}

### Quelle est la différence entre les Rapports d’engagement et le créateur de rapports ?

{% apitags %}
Analytique
{% endapitags %}

Les Rapports d’engagement vous fournissent des CSV des statistiques d’engagement pour des messages donnés envoyés depuis des campagnes ou des Canvas à l’aide d’e-mails déclenchés. Certaines données sont agrégées au niveau de la campagne ou du Canvas et non pas au niveau de la variante ou de l’étape spécifique. Les rapports ne sont pas enregistrés dans le tableau de bord. Relancer le rapport peut fournir des statistiques actualisées.

Le Créateur de rapports vous permet de comparer les résultats de plusieurs campagnes ou de plusieurs Canvas dans une vue unique pour déterminer rapidement quelles stratégies d’engagement ont le plus impacté vos indicateurs clés. Pour les campagnes et les Canvas, vous pouvez exporter vos données et enregistrer votre rapport pour une utilisation future.

Consultez l’[aperçu des rapports]({{site.baseurl}}/user_guide/data_and_analytics/reporting/reports_overview/) pour obtenir plus d’informations sur l’utilisation des rapports et des analytiques dans Braze.

{% endapi %}
