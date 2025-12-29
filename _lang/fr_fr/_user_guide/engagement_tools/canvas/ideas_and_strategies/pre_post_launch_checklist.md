---
nav_title: Liste de contrôle avant et après le lancement
article_title: Liste de contrôle avant et après le lancement
page_order: 2
description: "Cet article fournit des indications sur les points à vérifier avant et après le lancement d'un canvas."
tool: Canvas

---

# Liste de contrôle avant et après le lancement

> Cet article fournit des indications sur les points à vérifier avant et après le lancement d'un canvas.

## Les éléments à prendre en compte avant le lancement

Avant de lancer un Canvas, vous pouvez vérifier plusieurs détails pour vous assurer que vos messages et vos heures d'envoi correspondent aux préférences de votre audience. Les éléments à prendre en compte sont les variations des fuseaux horaires, les paramètres d'entrée, etc. En utilisant cette liste de contrôle comme guide, affinez ces domaines en fonction de votre cas d'utilisation pour contribuer à la réussite de votre Canvas. 

### Réviser les paramètres du fuseau horaire

Si vous saisissez les utilisateurs en fonction de leur fuseau horaire local à l'aide d'une planification de saisie, vous devez lancer votre Canvas au moins 24 heures avant la date à laquelle vous souhaitez que les utilisateurs entrent dans votre Canvas. Par exemple, voici une toile qui n'a pas laissé suffisamment de temps entre le lancement et l'heure d'entrée prévue. Dans ce scénario, il se peut que certains utilisateurs n'entrent pas dans votre Canvas car l'heure d'entrée planifiée est déjà passée dans certains fuseaux horaires. 

{% alert tip %}
Vous verrez une alerte si vous n'avez pas planifié un tampon suffisant. Une solution rapide consiste à ajuster l'heure d'envoi pour que les utilisateurs puissent rester dans le segmentage ciblé pendant 24 heures complètes.
{% endalert %}

!Une toile planifiée pour entrer en une seule fois chez les utilisateurs à partir de 10 heures le 30 avril 2025, à leur heure locale.]({% image_buster /assets/img_archive/canvas_checklist1.png %}){: style="max-width:75%;"}

### Pensez à utiliser des expressions régulières pour les filtres d'audience

Après avoir réglé les détails préliminaires concernant le moment où vos utilisateurs doivent entrer dans un Canvas, il est recommandé de vérifier maintenant vos segments ou vos filtres dans l'étape de l' **audience cible** de la création d'un Canvas. Au cours de cette étape, vous pouvez également consulter le résumé de la **population** cible pour voir comment votre audience a été définie. 

Ici, pensez à utiliser une expression régulière pour les segments ou les filtres dans les étapes Parcours d'audience, les paramètres de réception/distribution dans les étapes Message et Arbre décisionnel également. Une [expression régulière]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/) (également appelée "regex") est une chaîne de caractères, ce qui signifie qu'elle reconnaît des motifs et prend en compte les caractères, plutôt que des éléments tels que les majuscules. En d'autres termes, si vous utilisez "Égal / n'égal", vous risquez de limiter la taille de votre audience en raison de simples erreurs de syntaxe.

Si vous remarquez que votre audience cible est plus petite que prévu, essayez d'utiliser "Correspond à l'expression régulière" ou "Ne correspond pas à l'expression régulière" au lieu de "Est égal" ou "N'est pas égal". Cela peut permettre de prendre en compte les utilisateurs manquants et de cibler une audience plus large. 

### Identifier les paramètres d'entrée et les conditions de concurrence

Une condition de concurrence peut se produire lorsque vous avez utilisé les mêmes critères d'entrée dans vos paramètres de **planification d'entrée** et d' **audience cible**. 

Si vous utilisez une entrée basée sur l'action, vérifiez que vous n'avez pas utilisé ici la même action de déclenchement que dans votre audience cible. Une condition de concurrence peut se produire : l'utilisateur n'est pas dans l'audience au moment où il effectue l'événement déclencheur, ce qui signifie qu'il n'entrera pas dans le Canvas.

{% alert tip %}
Consultez les [meilleures pratiques]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/#scenario-3-matching-action-based-triggers-and-audience-filters) pour éviter cette condition de concurrence lors de la configuration d'un Canvas basé sur une action avec le même déclencheur que le filtre d'audience.
{% endalert %}

### Vérifier les propriétés d'entrée et les propriétés d'événement de Canvas

Bien que leur nom soit similaire, les [propriétés d'entrée et les propriétés d'événement de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) fonctionnent différemment dans vos flux de travail Canvas. Les propriétés d'entrée du canvas sont liées à vos paramètres d'entrée et peuvent être référencées dans n'importe quel composant de message de votre canevas. Les propriétés d'entrée dans le Canvas sont des propriétés de l'événement ou de l'appel API qui déclenche l'entrée d'un utilisateur dans un Canvas, à l'aide de paramètres d'entrée basés sur l'action ou déclenchés par l'API.

Les propriétés d'événement, en revanche, ne peuvent être référencées que dans la première étape de message suivant une étape de parcours d'action. Les propriétés d'événement sont des propriétés d'un événement personnalisé ou d'un événement d'achat que l'utilisateur a effectué pendant la fenêtre d'évaluation d'une étape des parcours d'action, et qui déclenche sa progression vers l'un des parcours d'action définis.

Vérifiez dans l'aperçu de votre message si des étapes du message font référence à des propriétés d'entrée dans le canvas ou à des propriétés d'événement.

### Examen des étapes du message pour l'avancement des utilisateurs

Par défaut, les utilisateurs passeront par toutes les étapes du message, qu'ils aient ou non reçu le message. Si vous souhaitez faire avancer les utilisateurs qui reçoivent un message particulier, vous pouvez le faire en ajoutant une étape de l'arbre décisionnel directement après votre composant Message. Ajoutez le filtre "Received Message from Canvas Step" comme filtre supplémentaire, puis sélectionnez l'étape Canvas et Message.

Pour les étapes de message avec envoi de messages in-app, vous pouvez utiliser un composant Parcours d'action au lieu du composant Fractionnement de la décision. Vous pourrez ainsi faire avancer les utilisateurs en fonction de la consultation ou non de votre message in-app. Définissez un groupe d'applications en ajoutant le filtre "Interagir avec l'étape" et sélectionnez **Afficher dans le message in-app**. Ensuite, définissez la fenêtre d'évaluation de l'étape sur la fenêtre d'expiration du message in-app.

Pour un composant de message dans l'envoi de messages multicanaux, nous recommandons ce qui suit :
* Intégrez une étape Délai entre les étapes Message et Arbre décisionnel, et fixez un délai d'au moins cinq secondes.
* Si le composant inclut le timing intelligent, réglez le délai sur 24 heures
* Si le composant comporte une limite de débit, divisez vos messages en plusieurs étapes de messages à canal unique et reliez-les entre elles. Ensuite, connectez l'étape de l'arbre décisionnel directement après la dernière étape du message pour vérifier si un utilisateur a reçu l'un des messages. Vous pouvez également utiliser cette méthode comme alternative pour un envoi de messages multicanal avec le timing intelligent.

## Ce qu'il faut prendre en compte après le lancement

Vous avez lancé votre Canvas ! Et maintenant, quoi ? Utilisez cette liste de contrôle pour voir comment vous pouvez revoir et ajuster vos Canvas en cas de divergences après le lancement, sur la base de ces scénarios.

### Beaucoup d'entrées, mais peu d'envois

Par exemple, disons que vous avez remarqué une disparité entre le nombre de messages envoyés et le nombre total d'entrées. Vous pouvez identifier et découvrir les domaines dans lesquels vous pouvez ajuster votre Canvas en vérifiant ces domaines clés.

#### Audience d'entrée

Si vous utilisez une campagne d'envoi planifiée, vérifiez à nouveau votre audience cible en passant en revue votre population cible. Comment se présentent les chiffres sur l'ensemble des canaux, et quel est le lien avec les canaux que vous avez utilisés dans votre Canvas ? Si les chiffres les plus bas correspondent aux canaux que vous avez utilisés dans votre Canvas, vous avez peut-être trouvé le problème.

#### Premier élément du canvas

Passez en revue les filtres d'audience, les déclencheurs d'action ou les segments utilisés dans les premiers éléments de votre Canvas. Y a-t-il des fautes d'orthographe ou des conditions trop strictes qui empêchent votre toile de démarrer correctement ? Utilisez-vous "Equals" alors que vous devriez utiliser "Matches Regex" ?

#### Groupe de contrôle canvas 

Examinez la répartition des utilisateurs entre vos variantes et votre groupe de contrôle. Le groupe de contrôle est-il plus important que prévu ? Si c'est le cas, vous pouvez modifier ce paramètre. Si vous avez activé la **sélection intelligente** et que le groupe de contrôle gagne, envisagez d'arrêter votre Canvas et d'essayer une nouvelle approche.

### Une audience totale vide

Si vous ne voyez pas de données d'entrée pour votre Canvas, la raison pour laquelle les utilisateurs n'entrent pas dans votre Canvas peut être due à des conditions de concurrence et à des filtres de segmentation d'audience restrictifs.

Si vous utilisez la saisie par action dans votre planification de saisie, vérifiez que vous n'avez pas utilisé ici la même action de déclenchement que dans votre **audience cible.** Une condition de concurrence peut se produire : l'utilisateur n'est pas dans l'audience au moment où il effectue l'événement déclencheur, ce qui signifie qu'il n'entrera pas dans le Canvas.

En outre, vérifiez que le segment sélectionné contient des utilisateurs en consultant le tableau **Population cible** dans les paramètres de l'**audience cible.**  Si ce chiffre est faible, voyez comment vous pouvez ajuster vos paramètres de saisie ou examinez les segments ou les filtres que vous avez sélectionnés pour y déceler d'éventuelles erreurs.

### Descente inattendue entre les marches

Un autre moyen apparent d'identifier les domaines d'ajustement de votre Canvas peut se produire lorsqu'il y a un grand décalage d'une étape du Canvas à l'autre. Dans ce cas, vérifiez que vos filtres d'audience et événements d'exception ne comportent pas de fautes d'orthographe ou de majuscules. Et comme toujours, vérifiez que vos filtres d'audience ne sont pas trop stricts au point d'exclure une majorité de vos utilisateurs de l'accès au Canvas. 

Ensuite, il est important d'identifier ces paramètres qui peuvent affecter quand et si les messages sont envoyés à vos utilisateurs :
- [Le timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/)
- Heures calmes
- Validations de réception/distribution

En général, choisissez soit le timing intelligent, soit les heures calmes pour votre Canvas, mais pas les deux. La même suggestion s'applique pour utiliser soit le timing intelligent, soit la [limite de débit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/), mais pas les deux. Pour plus d'informations sur la meilleure façon d'utiliser l'Intelligence Suite, lisez nos [cas d'utilisation de l'Intelligence Suite.]({{site.baseurl}}/user_guide/brazeai/intelligence/#use-cases)

### Volumes d'envois suspects entre les chemins

Lorsque le volume d'envois entre deux ou plusieurs parcours (soit les parcours d'audience, soit les parcours d'action) n'est pas celui auquel vous vous attendiez, cela peut être l'occasion de vérifier vos segments, vos filtres ou vos actions déclencheurs. Veillez également à identifier et à supprimer les filtres qui se chevauchent.

