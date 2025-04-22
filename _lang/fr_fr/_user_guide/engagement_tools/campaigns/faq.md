---
nav_title: FAQ
article_title: ""
page_order: 10
page_type: FAQ
description: "Le présent article fournit des réponses aux questions fréquemment posées sur les campagnes."
tool: Campaigns

---

# 

> Cet article fournit des réponses à des questions fréquemment posées sur les campagnes.

### 

   

### Puis-je ajouter un groupe de contrôle à ma campagne multicanal ?

Non, les groupes de contrôle dans les campagnes sont destinés aux messages à canal unique, tels que l'Email A par rapport à l'Email B. Comme alternative, essayez d'utiliser [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas) pour tester différents canaux, contenus de message et horaires de livraison. 

### Comment puis-je commencer à tester et optimiser les campagnes ?

Les campagnes multivariées et l’exécution de Canvas avec plusieurs variantes sont un excellent moyen de commencer ! Par exemple, vous pouvez lancer une [campagne multivariée]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) pour tester un message qui a différentes copies ou lignes d'objet. 

### Pourquoi le taux d’ouverture de ma campagne a-t-il baissé ?

De faibles taux d’ouverture ne sont pas forcément liés à un problème technique. Il peut y avoir des problèmes liés à l’écrêtage d’un e-mail qui peut entraîner la disparition d’un pixel de suivi. Il est cependant également possible que moins d’utilisateurs ouvrent leurs e-mails en raison de changements de contenu ou de taille d’audience. 

### Comment les audiences de la campagne sont-elles évaluées ?

Par défaut, les campagnes vérifient les filtres d’audience lors de l’entrée. Pour les campagnes par événement disposant d’un délai, il existe une option pour réévaluer le critère de segmentation au moment de l’envoi pour vous assurer que les utilisateurs font toujours partie de l’audience cible lorsque le message est envoyé. 

### Pourquoi y a-t-il une différence entre le nombre de destinataires uniques et le nombre d’envois pour une campagne ou un Canvas donné ?

Une explication potentielle de cette différence peut venir de l’activation de la rééligibilité pour la campagne ou le Canvas. Pour ce faire, les utilisateurs qui remplissent les conditions requises pour les paramètres de segment et de livraison pourront recevoir le message plusieurs fois. Si la rééligibilité n’est pas activée, l’explication probable de la différence entre les envois et les destinataires uniques peut venir des utilisateurs ayant plusieurs appareils, sur plusieurs plates-formes, associés à leurs profils. 

Par exemple, si vous avez un Canvas qui dispose à la fois d’une notification push iOS et Web, un utilisateur donné possédant à la fois un téléphone et un ordinateur de bureau peut recevoir plus d’un message.

### Pourquoi ma campagne a-t-elle une plus petite base d’utilisateurs accessible que le segment que j’utilise pour cette campagne ?

Si vous avez un [Groupe de Contrôle Global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) configuré, cela empêchera un pourcentage de votre audience atteignable de recevoir des campagnes. Cela signifie que le nombre d’utilisateurs accessibles à votre segment peut parfois être supérieur au nombre d’utilisateurs accessibles pour votre campagne, même si la campagne utilise ce même segment.

### Qu’est-ce que l’offre de livraison selon le fuseau horaire local ?

La livraison selon le fuseau horaire local vous permet de livrer des campagnes de communication à un segment en fonction du fuseau horaire individuel d’un utilisateur. Sans la livraison selon le fuseau horaire local, les campagnes seront planifiées en fonction des paramètres de fuseau horaire de votre société dans Braze. 

Par exemple, une société basée à Londres qui envoie une campagne à midi atteindra les utilisateurs sur la côte ouest de l’Amérique à 4 h du matin. Si votre application n’est disponible que dans certains pays, cela peut ne pas représenter un risque pour vous, sinon nous vous recommandons vivement d’éviter d’envoyer des notifications push matinales à votre base d’utilisateurs !

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

Par exemple, si une campagne est planifiée pour une livraison à 19 h UTC, nous commencerons à placer les envois de la campagne en file d’attente dès qu’un fuseau horaire est identifié (tpar exemple, les Samoa).  

Un autre exemple serait que vous désirez créer deux campagnes planifiées pour s’envoyer le même jour, une le matin et une le soir, et ajouter un filtre disant que les utilisateurs ne peuvent recevoir la deuxième campagne que s’ils ont déjà reçu la première. Avec la livraison selon le fuseau horaire local, certains utilisateurs pourraient ne pas recevoir la seconde campagne. 

### Comment planifier une campagne selon un fuseau horaire local ?



Braze recommande vivement que toutes les campagnes selon le fuseau horaire local soient planifiées 24 heures à l’avance.  Cependant, vous pouvez planifier ces campagnes moins de 24 heures à l’avance si nécessaire. N’oubliez pas que Braze n’enverra pas de messages aux utilisateurs qui ont manqué l’heure d’envoi de plus d’une heure. 

 De plus, l’heure d’envoi que vous choisissez pour votre campagne ne doit pas encore être dépassée dans le fuseau horaire de votre société.

La modification d’une campagne selon un fuseau horaire local qui est programmée moins de 24 heures à l’avance ne modifiera pas la planification du message. Si vous décidez de modifier une campagne selon un fuseau horaire local pour qu’elle soit envoyée ultérieurement (par exemple, à 19 h au lieu de 18 h), les utilisateurs qui se trouvaient dans le segment ciblé lorsque l’heure d’envoi initiale a été choisie recevront toujours le message à l’heure d’origine (18 h). Si vous modifiez un fuseau horaire local pour que l’envoi se fasse plus tôt (par exemple, à 16 h au lieu de 17 h), la campagne sera toujours envoyée à tous les membres du segment à l’heure d’origine (17 h). 

{% alert note %}
Pour les composants Canvas, les utilisateurs n’ont pas besoin d’être dans le composant pendant 24 heures pour recevoir le composant suivant de leur parcours utilisateur lors de la livraison selon un fuseau horaire local.
{% endalert %}

Si vous avez permis aux utilisateurs de devenir rééligibles pour la campagne, ils la recevront une nouvelle fois à l’heure d’origine (17 h). 

### Quand les changements apportés aux campagnes selon un fuseau horaire local prennent-ils effet ?

Les segments cibles pour les campagnes selon un fuseau horaire local doivent inclure une fenêtre de 48 heures au moins pour que les filtres temporels garantissent la livraison au segment tout entier. Par exemple, imaginez un segment ciblant les utilisateurs lors de leur deuxième jour avec les filtres suivants :

- Première utilisation de l’application il y a plus d’un jour
- Première utilisation de l’application il y a moins de 2 jours

La livraison selon un fuseau horaire local peut manquer les utilisateurs de ce segment en fonction du temps de livraison et de leur fuseau horaire local. Ceci est dû à la possibilité que l’utilisateur quitte le segment avant que son fuseau horaire ne déclenche la livraison.

### Quels changements puis-je apporter aux campagnes planifiées avant le lancement ?

Lorsque la campagne est planifiée, les modifications touchant autre chose que la composition du message doivent être effectuées avant qu’il ne soit placé dans la file d’attente d’envois. Comme pour toutes les campagnes, vous ne pouvez pas modifier les événements de conversion après son lancement.

### J'ai mis à jour ma campagne programmée. Pourquoi n’a-t-elle pas été lancée ?

Cela peut se produire lorsqu'une campagne est programmée pour être lancée à l'heure exacte où elle a été mise à jour.  Au lieu de programmer la campagne pour la même heure, sélectionnez **Envoyer dès le lancement de la campagne**.

### Quelle est la « zone sécurisée » avant que les messages d’une campagne programmée soient placés en file d’attente ?

Vous pouvez modifier en toute sécurité les messages dans les zones sûres suivantes :

- Les **campagnes planifiées ponctuelles** peuvent être modifiées jusqu'à l'heure d'envoi prévue.
- Les **campagnes planifiées récurrentes** peuvent être modifiées jusqu'à l'heure d'envoi prévue.
- 
- 

### Que se passe-t-il si je modifie l'heure d'envoi dans la "zone de sécurité" ?

Changer l’heure d’envoi sur les campagnes à ce moment-là peut entraîner un comportement indésirable, par exemple :

- Braze n’enverra pas de messages aux utilisateurs qui ont manqué l’heure d’envoi de plus d’une heure.
- Les messages placés en file d’attente à l’avance peuvent toujours être envoyés à l’heure initialement prévue, plutôt qu’à l’heure modifiée.

### Que dois-je faire si la « zone sécurisée » est déjà passée ?

Pour garantir que les campagnes fonctionnent comme souhaité, nous recommandons d'arrêter la campagne actuelle (cela annulera tous les messages en file d'attente).  Vous devrez peut-être exclure les utilisateurs de cette campagne qui ont déjà reçu la première.

Assurez-vous de réajuster les heures de planification de la campagne pour permettre l’envoi selon un fuseau horaire.

### Pourquoi le nombre d’utilisateurs qui accèdent à une campagne ne correspond pas au nombre prévu ?

Le nombre d’utilisateurs accédant à une campagne peut être différent du nombre prévu selon le mode d’évaluation des audiences et des déclencheurs. Dans Braze, une audience est évaluée avant le déclencheur (sauf si un déclencheur [modification d'attribut]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value) est utilisé). 

{% alert tip %}

{% endalert %}

### Quelle est la différence entre les options Exportation CSV des données utilisateurs et Exportation CSV des adresses e-mail sur ma page des analyses de campagne ?

Sélectionner l'option **Adresses e-mail d'exportation CSV** ne téléchargera que les données des utilisateurs avec des adresses e-mail. Par exemple, si vous avez un segment de 100 000 utilisateurs, mais que seulement 50 000 de ces utilisateurs ont des adresses e-mail, et que vous cliquez sur **Exportation CSV des adresses e-mail**, alors vous devriez vous attendre à voir seulement 50 000 lignes de données dans le fichier CSV. En comparaison, l’option **Exporter les données utilisateur en CSV** exportera toutes les données utilisateur.

### Puis-je rechercher une campagne en utilisant son identifiant API ?

Oui, utilisez le filtre `api_id:YOUR_API_ID` sur la page **Campagnes** pour rechercher une campagne par son identifiant API. Pour en savoir plus, reportez-vous à [Rechercher des campagnes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/).

### 

 

Les campagnes API sont utilisées pour suivre les messages que vous envoyez en utilisant l’API.  

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

 

| Avantages | Inconvénients | 
| ---- | ---- |
| • N’utilise pas de points de données<br><br>• Les éléments de personnalisation sont compris dans les propriétés de l’événement | • Ne vous permet pas de créer un segment d’utilisateurs éligibles au message dans les propriétés de la charge utile JSON<br><br>|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

