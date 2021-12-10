---
page_order: 2
nav_title: Termes à connaître
article_title: Conditions d'utilisation du SMS
layout: glossary_page
glossary_top_header: "Conditions d'utilisation du SMS"
glossary_top_text: "SMS - tout le monde l'a et sait ce qu'il est. Ce qu'ils ne savent pas, c'est la nuance. Consultez les termes ci-dessous pour en savoir plus sur les écosystèmes, les technologies et les processus SMS."
page_type: glossary
description: "Ce glossaire définit différents termes SMS que vous devriez connaître."
channel: SMS
glossaries:
  - 
    name: SMS (Service de messagerie court)
    description: Un canal de messagerie créé en 1980 et l'une des plus anciennes technologies de texte. Il se trouve aussi être l'un des canaux les plus répandus et les plus fréquemment utilisés, de tous les canaux de texte. Ce canal est un moyen plus direct d'atteindre vos utilisateurs et vos clients que la plupart des autres canaux de messagerie, car il utilise leur numéro de téléphone personnel pour les atteindre. Ainsi, les SMS ont plus de règles et de règlements autour de lui que les autres canaux de messagerie.
  - 
    name: Code court
    description: Ceci est court, une séquence mémorable de 5 à 6 chiffres qui permet aux expéditeurs d'envoyer plus de messages à des tarifs plus cohérents que les nombres longs (un message par seconde).<br><br>Un code court ou long est requis.
  - 
    name: Code Long
    description: Il s'agit du numéro de téléphone standard à 10 chiffres (dans la plupart des pays) qui permet aux expéditeurs d'envoyer plus de messages au rythme d'un message par seconde.<br><br>Un code court ou long est requis.
  - 
    name: Encodage
    description: La conversion de tout ce qui est en une forme codée. Le contenu des SMS peut être encodé en GSM-7 ou UCS-2.
  - 
    name: Encodage GSM-7 (Global System for Mobile Communications)
    description: 'GSM-7 est la norme d''encodage la plus connue pour la plupart des messages SMS. Il utilise la plupart des alphabets grecs et anglais ainsi que quelques caractères supplémentaires. Vous pouvez <a href=''https://en.wikipedia.org/wiki/GSM_03.38#GSM_7-bit_default_alphabet_and_extension_table_of_3GPP_TS_23.038_.2F_GSM_03.38''>en savoir plus sur l''encodage GSM-7 et les jeux de caractères que vous pouvez utiliser ici</a>. Les langues telles que le chinois, le coréen ou le japonais doivent être transférées en utilisant l''encodage de caractères UCS-2 16 bits. <br> <br> Vous pouvez estimer que la borne de caractères par segment pour ce type d''encodage est 128 caractères.'
  - 
    name: Encodage UCS-2 (jeu de caractères universel)
    description: L'encodage UCS-2 est un standard d'encodage par défaut surtout quand un message ne peut pas être encodé en utilisant le GSM-7 ou quand un langage a besoin de plus de 128 caractères pour être affiché. USC-2 est mieux mesuré par <a href='https://en.wikipedia.org/wiki/Code_point'>"points de code"</a>, par opposition aux "caractères". Quoi qu'il en soit, vous pouvez estimer que la limite de caractères par segment pour ce type d'encodage est de 67 caractères.
  - 
    name: Groupes d'abonnement pour SMS
    description: Les groupes d'abonnement sont un outil Braze qui vous permet de cibler des niveaux d'abonnement spécifiques d'utilisateurs ou de clients. Les groupes d'abonnement pour SMS sont construits en interne en fonction de votre service de messagerie et ne peuvent pas être partagés entre les groupes d'applications.
  - 
    name: Segments de message
    description: Un segment de message est un regroupement de jusqu'à un nombre défini de caractères (160 pour l'encodage GSM-7 ; 67 pour l'encodage UCS-2) qui sera envoyé en un seul envoi de SMS. Si vous envoyez un SMS avec 161 caractères en utilisant l'encodage GSM-7, vous verrez qu'il y a deux (2) segments de messages qui ont été envoyés. L'envoi de plusieurs segments de messages peut entraîner des frais supplémentaires.
  - 
    name: Service de messages
    description: Une collection de codes longs, de codes courts et d'identifiants alphanumériques utilisés pour envoyer votre message SMS avec Braze.
  - 
    name: Keyword
    description: "Un mot court qui est envoyé à un code court ou long pour interagir avec un programme SMS prédéfini ou pour demander à OPT-OUT d'un programme spécifique ou tous les programmes sur un code. Par exemple, <code>STOP</code>. Les mots-clés doivent <br> - être alphanumériques <br> - n'ont pas d'espaces <br> - être de moins de 10 caractères. <br> <br> Une combinaison de mot clé et de code court spécifiques ne peut être utilisée que sur un programme actif à la fois. Si un mot clé est entré qui est déjà utilisé par un autre programme, une erreur de validation apparaît. <br> <br> Il y a deux catégories de mots-clés obligatoires que tous les fournisseurs de contenu de SMS doivent respecter : <code>STOP</code> et <code>AIDE</code>."
  - 
    name: Mandatory Keyword HELP
    description: Pour chaque programme qui est créé sur la plateforme SMS Campaign Manager, le contenu de ce mot clé doit être fourni et doit respecter les meilleures pratiques et la conformité des transporteurs par pays ou région où le trafic de SMS est envoyé et reçu. Dans la plupart des cas, ce contenu devrait avoir une brève explication du programme SMS et comment OPT-OUT.
  - 
    name: Mots-clés Globaux Arrêt
    description: Les variantes incluent <code>STOP</code>, <code>END</code>, <code>QUIT</code>, <code>Désabonner</code>, <code>ANNULER</code>, <code>STOPALL</code>. On appelle ces mots clés <code>Global-Stop-Keywords</code>. Si l'un de ces mots-clés est écrit en un code court ou long, il en résulte que le numéro de portable (le numéro de téléphone portable originaire) est exclu de chaque programme SMS actif sur le code auquel il est associé.
  - 
    name: Code Vanity
    description: Un code court de vanité est un numéro de téléphone de 5 à 6 chiffres qui est spécifiquement sélectionné par une marque. Les codes abrégés Vanity sont de marque et plus faciles à retenir pour les consommateurs.
  - 
    name: Code court partagé
    description: Lorsque vous utilisez un code court partagé, tous les messages textuels, peu importe ce que l'entreprise ou l'organisation les envoie, arrive sur l'appareil mobile d'un consommateur à partir du même numéro de téléphone 5-6. Bien que les codes courts partagés soient relativement peu coûteux et immédiatement disponibles, cela signifie que votre entreprise n'aura pas de code court dédié. et sont soumis à d'autres entreprises suivant le protocole correct avec votre code court partagé.
  - 
    name: ID de l'expéditeur alphanumérique
    description: Alphanumeric Sender ID vous permet de définir le nom ou la marque de votre entreprise en tant que Sender ID en utilisant des caractères alphanumériques lors de l'envoi de messages à sens unique vers les pays pris en charge.
  - 
    name: Numéro sans frais
    description: Un numéro sans frais ou un numéro de téléphone gratuit est un numéro de téléphone qui est facturé pour tous les appels qui arrivent plutôt que de percevoir des frais à l'abonné du téléphone originaire. Les numéros sans frais aux États-Unis et au Canada sont activés par SMS, où les abonnés sont facturés pour les textes entrants et sortants.<br><br>La messagerie sans frais fonctionne mieux lorsque votre cas d'utilisation est de personne à personne, comme l'assistance à la clientèle ou les ventes, avec à la fois l'expéditeur et le destinataire ayant une conversation par texte.
  - 
    name: Messagerie à sens unique
    description: La messagerie unique vous permet de communiquer avec vos clients en envoyant des SMS. La messagerie unique est utile si vous implémentez un identifiant alphanumérique de l'expéditeur dans les marchés où les codes longs et courts ne sont pas disponibles.
  - 
    name: Messagerie à deux voies
    description: La messagerie bidirectionnelle vous permet de poursuivre une conversation en envoyant et en recevant des SMS.
---

