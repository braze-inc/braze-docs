---
nav_title: Liste de contrôle avant et après lancement
article_title: Liste de contrôle avant et après lancement
page_order: 2
description: "Cet article fournit une directive sur les choses à vérifier avant et après avoir lancé un Canvas."
tool: Canvas

---

# Liste de contrôle avant et après lancement

## Choses à prendre en compte avant le lancement

Avant de lancer un Canvas, plusieurs détails vous permettent de vérifier que vos envois de messages et vos heures d’envoi correspondent aux préférences de votre public. Les choses à prendre en compte comprennent toutes les variations dans les fuseaux horaires, les paramètres d’entrée, etc. En utilisant cette liste de contrôle comme guide, finalisez ces domaines en fonction de votre cas d’utilisation pour contribuer à la réussite de votre Canvas. 

### Vérifier les paramètres de fuseau horaire

Si vous saisissez des utilisateurs en fonction de leur fuseau horaire local à l’aide d’un calendrier d’entrée planifié, vous devez lancer votre Canvas au moins 24 heures avant le moment où vous souhaitez que les utilisateurs accèdent à votre Canvas. Par exemple, voici un Canvas qui n’a pas laissé suffisamment de temps entre le lancement et l’heure d’entrée prévue. Dans ce scénario, certains utilisateurs n’accèderont pas à votre Canvas car l’heure d’entrée prévue a déjà été passée dans certaines fuseaux horaires. 

{% alert tip %} 
Vous verrez une alerte si vous n’avez pas assez planifié un tampon. Une solution rapide consiste à ajuster l’heure d’envoi pour garantir que les utilisateurs peuvent rester dans le segment ciblé pendant 24 heures.
{% endalert %}

![][1]

### Envisager d’utiliser des expressions régulières pour les filtres publics

Après avoir configuré les détails préliminaires lorsque vos utilisateurs doivent entrer un Canvas, il est recommandé de vérifier à présent vos segments ou filtres dans le **Public cible** de construire un Canvas. Dans cette étape, vous pouvez également examiner **Population cible** récapitulatif pour voir comment votre public cible a été configuré. 

Ici, envisagez d’utiliser une expression régulière pour les segments ou filtres dans les étapes des chemins de public, les paramètres de validation de livraison dans les étapes Message et Répartition de décision. A [expression régulière]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/) (également appelé regex) est une chaîne de caractères, ce qui signifie qu’il reconnaît les modèles et prend en compte les personnages, au lieu de choses comme la capitalisation. Cela signifie que si vous utilisez « Égal/Non égal », vous pouvez limiter la taille de votre public en raison d’erreurs de syntaxe simples.

Si vous remarquez que votre public cible est plus petit que prévu, essayez d’utiliser « Correspond à Regex » ou « Ne correspond pas à Regex » au lieu de « Égal » ou « Non égal ». Cela peut rendre compte des utilisateurs manquants et cibler un public plus important. 

### Identifier les paramètres d’entrée et les conditions de course

Une condition de course peut survenir lorsque vous avez utilisé les mêmes critères d’entrée dans votre **Calendrier des entrées** et **Public cible** paramètres. Si vous utilisez une entrée basée sur des actions, vérifiez que vous n’avez pas utilisé la même action de déclenchement ici que dans votre public cible. Une condition de concurrence peut se produire lorsque l’utilisateur ne figure pas dans l’audience au moment de l’événement déclencheur, ce qui signifie qu’il ne pourra pas accéder au Canvas.

### Vérifiez les propriétés d’entrée et propriétés de l’événement Canvas

Bien que leur nom soit similaire, [les propriétés d’entrée et les propriétés de l’événement Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) fonctionnent différemment dans vos flux de travail Canvas. Les propriétés d’entrée du Canvas sont liées à vos paramètres d’entrée et peuvent être référencées dans n’importe quel composant de message dans votre Canvas. Les propriétés d’entrée de Canvas sont des propriétés de l’événement ou de l’appel API qui déclenchent l’entrée d’un utilisateur dans un Canvas, en utilisant des paramètres d’entrée basés sur des actions ou des API.

Les propriétés de l'événement, d’autre part, ne peuvent être référencées que dans la première étape du message après une étape des chemins d’action. Les propriétés de l'événement sont des propriétés d’un événement personnalisé ou d’un événement d’achat que l’utilisateur a effectué pendant la fenêtre d’évaluation d’une étape des chemins d’action, et qui déclenche leur progression vers l’un des chemins d’action définis.

Vérifiez l’aperçu de votre message pour toutes les étapes de message référencées dans les propriétés de saisie de Canvas ou les propriétés de l'événement.

### Passer en revue les étapes du message pour l’avancement de l’utilisateur

Par défaut, les utilisateurs passeront par toutes les étapes du message, qu’ils aient reçu le message. Si vous souhaitez faire avancer les utilisateurs qui reçoivent un message particulier, vous pouvez le faire en ajoutant une étape de fractionnement des décisions directement après votre composant Message. Ajoutez le filtre « Message reçu du Canvas Step » comme filtre supplémentaire, puis sélectionnez l’étape Canvas et message.

Pour les étapes du message avec la messagerie dans l’application, vous pouvez utiliser un composant d’action paths plutôt que le composant Decision de séparation. Cela vous permettra d’avancer les utilisateurs selon qu’ils ont affiché votre message In-App. Définissez un groupe d’actions en ajoutant le filtre « Interagir avec l’étape » et sélectionnez **View in app message (Afficher dans le message d’application)**. Ensuite, définissez la fenêtre d’évaluation de l’étape dans la fenêtre d’expiration du message In-App.

Pour un composant Message dans un envoi de messages multicanal, nous recommandons ce qui suit :
* Incluez une étape de retard entre vos étapes de communication de message et de décision, et réglez le délai sur au moins cinq secondes
* Si le composant inclut un timing intelligent, réglez le délai sur 24 heures
* Si le composant inclut la limitation du taux, divisez vos messages en plusieurs étapes du message canal unique et reliez-les ensemble. Ensuite, connectez l’étape de fractionnement des décisions directement après la dernière étape du message pour vérifier si un utilisateur a reçu l’un des messages. Vous pouvez également utiliser cette méthode comme alternative pour une étape de message multicanal avec Timing Intelligent.

## Choses à prendre en compte après le lancement

Vous avez lancé votre Canvas ! Et maintenant ? Utilisez cette liste de contrôle pour voir comment vous pouvez revoir et ajuster votre Canvas en cas de divergences après le lancement sur la base de ces scénarios.

### Beaucoup d’entrées, mais peu d’envois

Par exemple, disons que vous avez remarqué une disparité entre votre nombre de messages envoyés par rapport aux entrées totales. Vous pouvez identifier et découvrir les zones pour ajuster votre Canvas en vérifiant ces zones clés.

#### Public entrant

Si vous utilisez une campagne d’envoi programmée, vérifiez deux fois votre public cible en examinant votre population cible. Comment les chiffres examinent-ils les canaux et comment cela se rapporte aux canaux que vous avez utilisés dans votre Canvas ? Si les nombres les plus bas correspondent aux canaux que vous avez utilisés dans votre Canvas, vous avez peut-être trouvé le problème.

#### Premier composant du Canvas

Examinez les filtres publics, les déclencheurs d’action ou les segments utilisés dans les composants initiaux de votre Canvas. Y a-t-il des fautes d’orthographe ou des conditions trop strictes qui empêchent votre Canvas de commencer à s’éteindre ? Utilisez-vous « Égal » lorsque vous devez utiliser « Correspondances Regex » ?

#### Dans le groupe de contrôle de Canvas 

Examinez la distribution des utilisateurs entre vos variantes et votre groupe de contrôle. Le groupe de contrôle est-il plus grand que vous ne l’avez souhaité ? Si tel est le cas, vous pouvez modifier ce paramètre. Si vous avez **Sélection intelligente** activé, et le groupe de contrôle est gagnant, pensez à arrêter votre Canvas et à essayer une nouvelle approche.

### Un public total vide

Si vous remarquez que les messages ont été envoyés, mais que vous ne voyez pas de données d’entrée pour votre Canvas, la principale raison pour laquelle les utilisateurs peuvent ne pas entrer dans votre Canvas peut être dû à des conditions de course et à des filtres de segmentation de public restrictifs. 

Si vous utilisez une entrée basée sur des actions dans votre calendrier d’entrée, vérifiez que vous n’avez pas utilisé la même action de déclenchement que dans votre **Public cible**. Une condition de concurrence peut se produire lorsque l’utilisateur ne figure pas dans l’audience au moment de l’événement déclencheur, ce qui signifie qu’il ne pourra pas accéder au Canvas.

De plus, vérifiez que le segment sélectionné a des utilisateurs en examinant le **Population cible** tableau dans le **Public cible** paramètres. Si ce nombre est faible, voir comment ajuster vos paramètres d’entrée ou revoir les segments ou filtres sélectionnés pour détecter toute erreur.

### Abandon inattendu entre les étapes

Une autre façon apparente d’identifier les zones d’ajustement pour votre Canvas peut se produire lorsqu’une grande goutte de Canvas est déplacée d’une Canvas step à la suivante. Dans ce cas, vérifiez que vos filtres publics et les événements d’exception n’ont pas d’erreurs de fautes ou d’erreurs de capitalisation. Et comme toujours, vérifiez que vos filtres publics ne sont pas si stricts pour omettre une majorité de vos utilisateurs de pénétrer dans le Canvas. 

Ensuite, il est important d’identifier ces paramètres qui peuvent affecter quand et si les messages sont envoyés à vos utilisateurs :
- [Timing Intelligent]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/)
-Heures calmes
-Validations de livraison

En général, choisissez le Timing intelligent ou les Heures calmes pour votre Canvas, pas les deux. La même suggestion s’applique à l’utilisation du timing intelligent ou [limitation du taux]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/), pas les deux. Pour plus d’informations sur la meilleure utilisation de Intelligence Suite, lisez notre [FAQ sur les renseignements]({{site.baseurl}}/user_guide/intelligence/faqs/).

### Volumes d’envoi suspects entre chemins

Lorsque le volume d’envois entre deux chemins ou plus (chemins publics ou chemins d’action) n’est pas ce que vous attendez, cela peut être l’occasion de vérifier vos segments, filtres ou actions déclencheurs. Assurez-vous également d’identifier et de retirer les filtres qui se chevauchent.

[1]: {% image_buster /assets/img_archive/canvas_checklist1.png %}
