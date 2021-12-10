---
nav_title: Foire aux questions
article_title: FAQ de la campagne
page_order: 10
page_type: Foire Aux Questions
description: "Cette page fournit des réponses aux questions les plus fréquemment posées sur les campagnes."
tool: Campagnes
---

# FAQ de la campagne

### Comment créer une campagne multicanal ?

Les campagnes multi-canaux peuvent être créées en sélectionnant __Créer une campagne__ puis __Campagne multicanal__ dans le tableau de bord. Une fois dans une campagne multi-canaux, sélectionnez __Ajouter un canal de messagerie__ dans l'onglet __composer__ pour ajouter vos canaux désirés. Cliquer sur les icônes des canaux qui apparaissent vous permettra de basculer à travers différents compositeurs de messagerie au fur et à mesure que vous construisez votre copie de campagne pour les différents canaux.

### Quelles sont les façons dont je peux commencer à tester et optimiser les campagnes ?

Des campagnes multivariées et des Canvases avec plusieurs variantes sont une excellente façon de commencer! Par exemple, vous pouvez exécuter une [campagne multivariée]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) pour tester un message qui a des copies ou des lignes de sujet différentes. Les toiles avec plusieurs variantes sont utiles pour tresser des flux de travail entiers.

### Pourquoi y a-t-il une différence entre le nombre de destinataires uniques et le nombre d’envois pour une campagne donnée ou Canvas?

Une explication potentielle de cette différence pourrait être due à la rééligibilité de la campagne ou de Canvas qui a été activée. En ayant ceci activé, les utilisateurs qui se qualifient pour le segment et les paramètres de livraison pourront recevoir le message plus d'une fois. Si la rééligibilité n'est pas activée, alors l'explication probable de la différence entre les envois et les destinataires uniques peut être due aux utilisateurs ayant plusieurs périphériques, à travers des plates-formes, associées à leurs profils.

Par exemple, si vous avez un Canvas qui a à la fois des notifications de push iOS et web, un utilisateur donné avec des appareils mobiles et de bureau pourrait recevoir plus d'un message.

### Pourquoi ma campagne a-t-elle une base d'utilisateurs plus petite que le segment que j'utilise pour la campagne ?

Si vous avez mis en place un [Groupe de contrôle global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) , cela empêchera un pourcentage de votre public accessible de recevoir des campagnes. Cela signifie que le nombre d'utilisateurs accessibles pour votre segment peut parfois être plus grand que le nombre d'utilisateurs accessibles pour votre campagne, même si la campagne utilise ce même segment.

### Que propose la livraison des fuseaux horaires locaux?

La livraison locale de fuseaux horaires vous permet de livrer des campagnes de messagerie à un segment basé sur le fuseau horaire individuel de l’utilisateur. Sans livraison locale du fuseau horaire, les campagnes seront planifiées en fonction des paramètres du fuseau horaire de votre entreprise au Brésil.

Par exemple, une société londonienne qui envoie une campagne à 12 heures atteindra les utilisateurs de la côte ouest de l'Amérique à 4 heures. Si votre application n'est disponible que dans certains pays, cela peut ne pas être un risque pour vous, sinon, Nous vous recommandons fortement d'éviter d'envoyer des notifications push tôt le matin à votre base d'utilisateurs !

### Comment Braze reconnaît-il le fuseau horaire d'un utilisateur ?

Braze déterminera automatiquement le fuseau horaire d'un utilisateur à partir de son appareil. Cela garantit la précision du fuseau horaire et la couverture complète de vos utilisateurs. Les utilisateurs créés via l'API utilisateur ou autrement sans fuseau horaire auront le fuseau horaire de votre entreprise comme fuseau horaire par défaut jusqu'à ce qu'ils soient reconnus dans votre application par le SDK.

Pour vérifier le fuseau horaire de votre entreprise, consultez vos [Paramètres de la société]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/company-wide_settings_management/) sur le tableau de bord. Cliquez sur votre nom dans la barre d'outils du haut, puis cliquez sur **Paramètres de la société**.

### Comment planifier une campagne locale de fuseau horaire?

Lorsque vous planifiez une campagne, vous devez choisir de l'envoyer à une heure désignée, puis cochez **Envoyer une campagne aux utilisateurs dans leur fuseau horaire local**.

Braze recommande vivement que toutes les campagnes locales de fuseau horaire soient planifiées 24 heures à l'avance. Étant donné qu'une telle campagne doit être envoyée au cours d'une journée entière, Les planifier 24 heures à l'avance garantit que votre message parviendra à tout votre segment. Cependant, vous pouvez planifier ces campagnes moins de 24 heures à l'avance si nécessaire. Gardez à l'esprit que Braze n'enverra pas de messages aux utilisateurs qui ont manqué le temps d'envoi de plus d'une heure.

Par exemple, s'il est 13h et que vous planifiez une campagne locale de fuseau horaire pour 15h, alors la campagne enverra immédiatement à tous les utilisateurs dont l'heure locale est de 3-16 heures, mais pas aux utilisateurs dont l'heure locale est de 17 heures. De plus, le temps d'envoi que vous avez choisi pour votre campagne doit ne pas avoir encore eu lieu dans le fuseau horaire de votre entreprise.

Modifier une campagne locale de fuseau horaire qui est programmée moins de 24 heures à l’avance ne modifiera pas le calendrier du message. Si vous décidez de modifier une campagne locale de fuseau horaire à envoyer plus tard (par exemple, 19h au lieu de 18h), les utilisateurs qui se trouvaient dans le segment ciblé lorsque l'heure d'envoi originale a été choisie, recevront toujours le message à l'heure d'origine (6hm). Si vous modifiez un fuseau horaire local à envoyer à une heure antérieure (par exemple, 16h au lieu de 17h), alors la campagne sera toujours envoyée à tous les membres du segment à l'heure initiale (5h).

{% alert note %}
Pour les étapes de Canvas , les utilisateurs n'ont pas besoin d'être à l'étape pendant 24 heures pour recevoir l'étape suivante de la livraison locale du fuseau horaire.
{% endalert %}

Si vous avez autorisé les utilisateurs à redevenir éligibles pour la campagne, ils le recevront à nouveau à la date initiale (5h). Cependant, pour tous les événements subséquents de votre campagne, vos messages ne vous sont envoyés qu'à l'heure à laquelle vous avez été mis à jour.

### Quand les changements de fuseau horaire local entrent-ils en vigueur?

Les segments cibles pour les campagnes locales de fuseau horaire devraient inclure au moins une fenêtre de 48 heures pour tous les filtres basés sur le temps afin de garantir la livraison à l'ensemble du segment. Par exemple, envisagez un segment ciblant les utilisateurs sur leur deuxième jour avec les filtres suivants :

- Première application utilisée il y a plus d'un jour
- Première application utilisée il y a moins de 2 jours

La livraison locale du fuseau horaire peut manquer les utilisateurs de ce segment en fonction de l'heure de livraison et du fuseau horaire local des utilisateurs. Ceci est dû au fait qu'un utilisateur peut laisser le segment avant que son fuseau horaire ne déclenche la livraison.

### Quels changements puis-je apporter aux campagnes planifiées avant le lancement ?

Lorsque la campagne est programmée, les modifications à autre chose que la composition du message doivent être faites avant de faire la file d'attente des messages à envoyer. Comme pour toutes les campagnes, vous ne pouvez pas modifier les événements de conversion après son lancement.

Pour les entrées Canvas reportez-vous à la section ci-dessus. Pour les étapes de Canvas reportez-vous aux éléments suivants :

- Les modifications planifiées ne s'appliqueront qu'aux utilisateurs qui n'attendent pas déjà de recevoir l'étape.
- L'audience change par défaut pour s'appliquer à tout le monde à moins que vous n'ayez sélectionné **Évaluer au moment de la file d'attente**, auquel cas c'est un comportement similaire à celui ci-dessus.

### Qu'est-ce que la « zone de sécurité » avant que les messages sur une campagne planifiée ne soient mis en file d'attente ?

- **Des campagnes ponctuelles planifiées**- peuvent être modifiées jusqu'à l'heure d'envoi prévue.
- **Campagnes planifiées récurrentes**- peuvent être modifiées jusqu'à l'heure d'envoi planifiée.
- **Campagnes locales d'envoi**- peut être modifié jusqu'à 24 heures avant l'heure d'envoi prévue.
- **Campagnes optimales pour l'envoi du temps**- peut être modifié jusqu'à 24 heures avant le jour où la campagne est programmée à envoyer.

### Que faire si je fais un montage dans la "zone sûre"?

Changer le temps d'envoi des campagnes dans ce délai peut conduire à un comportement indésirable, par exemple :

- Braze n'enverra pas de messages aux utilisateurs qui ont manqué le temps d'envoi de plus d'une heure.
- Les messages préalablement mis en file d'attente peuvent toujours être envoyés au moment de la mise en file d'attente initiale, plutôt que dans le délai ajusté.

### Que dois-je faire si la "zone sûre" est déjà passée?

Pour s'assurer que les campagnes fonctionnent comme vous le souhaitez, nous vous recommandons d'arrêter la campagne actuelle (cela annulera tous les messages mis en attente). Vous pouvez ensuite dupliquer la campagne, faire les changements si nécessaire et lancer la nouvelle campagne. Vous devrez peut-être exclure les utilisateurs de cette campagne qui ont déjà reçu la première campagne.

Veuillez vous assurer de réajuster les horaires de la campagne pour permettre l'envoi du fuseau horaire.

### Quand Braze évalue-t-il les utilisateurs pour la livraison des fuseaux horaires locaux?

Pour la livraison locale du fuseau horaire, Braze évalue les utilisateurs pour l'éligibilité de leur entrée dans ces deux instances :
- A l'heure Samoa (UTC+13) du jour programmé
- À l'heure locale du jour programmé

Pour qu'un utilisateur puisse être éligible à l'inscription, il doit être admissible aux deux vérifications. Par exemple, si une Canvas est prévue pour le lancement le 7 août 2021 à 14h, fuseau horaire local, alors cibler un utilisateur situé à New York nécessiterait les vérifications suivantes pour son éligibilité :
- New York le 6 août 2021 à 21h
- New York le 7 août 2021 à 14h

Notez que l'utilisateur doit être dans le segment pendant 24 heures avant le lancement. Si l'utilisateur n'est pas éligible lors de la première vérification, alors Braze ne tentera pas la deuxième vérification.
