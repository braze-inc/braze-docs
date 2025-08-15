---
page_order: 1
nav_title: Termes à connaître
article_title: Conditions générales SMS
alias: /sms_terms_to_know/

layout: glossary_page
glossary_top_header: "Terms to Know"
glossary_top_text: "SMS–everyone has it and knows what it is. What they don't know is the nuance. Check out the following terms to learn more about SMS ecosystems, technologies, and processes."
page_type: glossary
description: "Ce glossaire définit les différentes conditions de SMS que vous devez connaître."
channel: SMS 

glossaries:
  - name: SMS (service de messages courts)
    description: "Un canal de communication créé en 1980 et l’une des technologies de SMS les plus anciennes. Il s’agit également d’une des voies de texte les plus répandues et les plus fréquemment utilisées. Ce canal est une façon plus directe d’atteindre vos utilisateurs et clients que la plupart des autres canaux de messagerie, car ils utilisent leur numéro de téléphone personnel pour les atteindre. Ainsi, le SMS a plus de règles et de réglementations que les autres canaux de messagerie."
  - name: Code court
    description: "Il s'agit d'une séquence courte et mémorable de 5 à 6 chiffres qui permet aux expéditeurs d'envoyer plus de messages à des débits plus constants que les numéros longs (un message par seconde).<br><br>Un code long ou court est requis."
  - name: Code long
    description: Il s’agit du numéro de téléphone standard à 10 chiffres (dans la plupart des pays) qui permet aux expéditeurs d’envoyer plus de messages au taux d’un message par seconde.<br><br>Un code long ou court est requis.
  - name: Encodage
    description: La conversion de tout dans un formulaire codé. Le contenu SMS peut être encodé dans GSM-7 ou UCS-2.
  - name: Codage GSM-7 (système mondial pour les communications mobiles)
    description: "GSM-7 est la norme de codage la plus visible pour la plupart des SMS. Il utilise la plupart des lettres grecques et anglaises, ainsi que des caractères supplémentaires. Pour en savoir plus sur le codage GSM-7 et sur les jeux de caractères que vous pouvez utiliser, consultez l'<a href='https://en.wikipedia.org/wiki/GSM_03.38#GSM_7-bit_default_alphabet_and_extension_table_of_3GPP_TS_23.038_.2F_GSM_03.38' title=\"alphabet par défaut et la table d&apos;extension GSM 7 bitsWikipedia.\"></a> Les langues telles que chinois, coréen ou japonais doivent être transférées à l’aide du codage de personnage UCS-2 de 16 bits. <br> <br> Vous pouvez estimer que la limite de caractères par segment pour ce type d’encodage est de 128 caractères."
  - name: Codage UCS-2 (jeu de caractères codé universel)
    description: "L’encodage UCS-2 est une norme d’encodage de secours, particulièrement lorsqu’un message ne peut pas être codé à l’aide de GSM-7 ou lorsqu’une langue nécessite plus de 128 caractères à rendre. L’USC-2 est mieux mesurée par <a href='https://en.wikipedia.org/wiki/Code_point'>points de code</a>, par opposition aux « caractères ». Quelle que soit la raison, vous pouvez estimer que la limite de caractères par segment pour ce type d’encodage est de 67 caractères."
  - name: Groupes d’abonnement pour SMS
    description: "Les groupes d'abonnement sont un outil de Braze qui vous permet de cibler des niveaux d'abonnement spécifiques d'utilisateurs ou de clients. Les groupes d'abonnement pour les SMS sont construits en interne sur la base de votre service de messages et ne peuvent pas être partagés entre les espaces de travail."
  - name: Segments de message
    description: "Un segment de message est un groupement allant jusqu’à un nombre défini de caractères (160 pour le codage GSM-7 ; 67 pour le codage UCS-2) qui sera envoyé dans une seule distribution par SMS. Si vous envoyez un SMS avec 161 caractères à l’aide du codage GSM-7, vous verrez qu’il y a deux (2) segments de messages envoyés. L’envoi de plusieurs segments de messages peut entraîner des frais supplémentaires."
  - name: Service de messagerie
    description: "Ensemble de codes longs, de codes courts et d'ID alphanumériques utilisés pour envoyer votre message SMS avec Braze."
  - name: Mot-clé
    description: "Un court mot envoyé à un code long ou court pour interagir avec un programme SMS prédéfini ou pour demander à OPT-OUT d’un programme spécifique ou de tous les programmes sur un code. Par exemple,  <code>STOP</code>. Les mots-clés devraient <br> - être alphanumériques <br> - ne pas avoir d’espaces <br> - contenir moins de 10 caractères. <br> <br> Un mot clé spécifique et une combinaison de codes courts ne peuvent être utilisés que sur un programme actif à la fois. Si un mot-clé est saisi déjà utilisé par un autre programme, une erreur de validation s’affiche. <br> <br> Il existe deux catégories de mots-clés obligatoires que tous les fournisseurs de contenu SMS doivent respecter : <code>STOP</code> et <code>HELP</code>."
  - name: Aide mot-clé obligatoire
    description: "Pour chaque programme créé dans la plate-forme de gestionnaire de campagne SMS, le contenu de ce mot clé doit être fourni et doit être conforme aux meilleures pratiques et à la conformité du transporteur par pays ou région dans laquelle le trafic SMS est envoyé et reçu. Dans la plupart des cas, ce contenu doit avoir une brève explication du programme SMS et comment vous DÉSINSCRIRE."
  - name: Mots clés STOP global
    description: "Les variations comprennent <code>STOP</code>, <code>END</code>, <code>QUIT</code>, <code>UNSUBSCRIBE</code>, <code>CANCEL</code>, <code>STOPALL</code>. On les appelle <code>Global-Stop-Keywords</code>. Si l’un de ces mots-clés est envoyé par SMS à un code long ou court, il se traduit par le numéro de téléphone portable (numéro de téléphone portable provenant du numéro de téléphone portable) choisi par chaque programme SMS actif sur le code auquel il est associé."
  - name: Code de comptoir
    description: Un code court à 5 à 6 chiffres est spécifiquement sélectionné par une marque. Les codes courts Vanity sont marqués et plus faciles à retenir pour les consommateurs.
  - name: Code court partagé
    description: "Avec un code court partagé, tous les messages texte, quelle que soit l’identité de l’entreprise ou de l’organisation, parviennent à l’appareil mobile d’un consommateur avec le même numéro de téléphone à 5 à 6 chiffres. Bien que les codes courts partagés soient relativement économiques et immédiatement disponibles, cela signifie que votre entreprise n’aura pas de code abrégé dédié et est soumise à d’autres entreprises suivant le protocole approprié avec votre code abrégé partagé." 
  - name: ID d’expéditeur alphanumérique
    description: L’ID d’expéditeur alphanumérique vous permet de définir le nom ou la marque de votre société comme identifiant de l’expéditeur à l’aide de caractères alphanumériques lorsque vous envoyez des messages unidirectionnels aux pays pris en charge.
  - name: Numéro gratuit
    description: "Un numéro de téléphone gratuit ou un numéro de téléphone gratuit est un numéro de téléphone facturé pour tous les appels d’arrivée au lieu d’engager des frais à l’abonné téléphonique d’origine. Les numéros gratuits aux États-Unis et au Canada sont activés par SMS, où les abonnés sont facturés pour les textes entrants et sortants.<br><br>Le message gratuit fonctionne mieux lorsque votre cas d’utilisation est une personne à personne, comme le support client ou les ventes, avec l’expéditeur et le destinataire ayant une conversation par SMS."
  - name: Messagerie unidirectionnelle
    description: La messagerie unidirectionnelle vous permet de communiquer avec vos clients en envoyant des messages texte. La messagerie unidirectionnelle est utile si vous implémentez un ID d’expéditeur alphanumérique sur les marchés où les codes longs et courts ne sont pas disponibles. 
  - name: Messagerie bidirectionnelle
    description: La messagerie bidirectionnelle vous permet de mener une conversation en envoyant et en recevant des messages texte. 
---
