---
page_order: 1
nav_title: Termes à connaître
article_title: Termes SMS à connaître
alias: /sms_terms_to_know/

layout: glossary_page
glossary_top_header: "Terms to Know"
glossary_top_text: "SMS–everyone has it and knows what it is. What they don't know is the nuance. Check out the following terms to learn more about SMS ecosystems, technologies, and processes."
page_type: glossary
description: "Ce glossaire définit divers termes relatifs aux SMS que vous devez connaître."
channel: SMS 

glossaries:
  - name: SMS (Short Message Service)
    description: "Un canal de communication créé en 1980 et l'une des plus anciennes technologies d'envoi de messages. Il s'agit également de l'un des canaux d'envoi de SMS les plus répandus et les plus fréquemment utilisés. Ce canal est un moyen plus direct d'atteindre vos utilisateurs et vos clients que la plupart des autres canaux d'envoi de messages, car il utilise leur numéro de téléphone personnel pour les joindre. En tant que tel, le SMS est soumis à davantage de règles et de réglementations que les autres canaux d'envoi de messages."
  - name: Code court
    description: "Il s'agit d'une séquence de 5 à 6 chiffres, courte et mémorable, qui permet aux expéditeurs d'envoyer davantage de messages à un rythme plus régulier que les numéros longs (un message par seconde).<br><br>Un code court ou un code long est nécessaire."
  - name: Code long
    description: "Il s'agit du numéro de téléphone standard à 10 chiffres (dans la plupart des pays) qui permet aux expéditeurs d'envoyer davantage de messages au rythme d'un message par seconde.<br><br>Un code court ou un code long est nécessaire."
  - name: Encodage
    description: La conversion de toute chose en une forme codée. Le contenu des SMS peut être codé en GSM-7 ou en UCS-2.
  - name: Encodage GSM-7 (Système mondial de communications mobiles)
    description: "GSM-7 est la norme d'encodage la plus répandue pour la plupart des envois de messages SMS. Il utilise la plupart des alphabets grec et anglais, ainsi que quelques caractères supplémentaires. Pour en savoir plus sur l'encodage GSM-7 et les jeux de caractères que vous pouvez utiliser, consultez l'<a href='https://en.wikipedia.org/wiki/GSM_03.38#GSM_7-bit_default_alphabet_and_extension_table_of_3GPP_TS_23.038_.2F_GSM_03.38' title=\"alphabet par défaut et la table d&apos;extension GSM 7 bitsWikipedia.\"></a> Les langues telles que le chinois, le coréen ou le japonais doivent être transférées en utilisant le codage de caractères UCS-2 sur 16 bits. <br> <br> Vous pouvez estimer que la limite de caractères par segment pour ce type d'encodage est de 128 caractères."
  - name: Codage UCS-2 (jeu de caractères codés universel)
    description: "L'encodage UCS-2 est une norme d'encodage de secours, notamment lorsqu'un message ne peut être encodé à l'aide du GSM-7 ou lorsqu'une langue nécessite un rendu de plus de 128 caractères. L'USC-2 se mesure mieux en <a href='https://en.wikipedia.org/wiki/Code_point'>points de code</a> qu'en \"caractères\". Quoi qu'il en soit, on peut estimer que la limite de caractères par segment pour ce type d'encodage est de 67 caractères."
  - name: "Groupes d'abonnement pour les SMS"
    description: "Les groupes d'abonnement sont un outil de Braze qui vous permet de cibler des niveaux d'abonnement spécifiques d'utilisateurs ou de clients. Les groupes d'abonnement pour les SMS sont construits en interne sur la base de votre service de messages et ne peuvent pas être partagés entre les espaces de travail."
  - name: Segments de messages
    description: "Un segment de message est un envoi de messages comprenant un nombre défini de caractères (160 pour le codage GSM-7 ; 67 pour le codage UCS-2) qui seront envoyés en une seule fois par SMS. Si vous envoyez un SMS de 161 caractères en utilisant le codage GSM-7, vous verrez qu'il y a deux (2) segments de message qui ont été envoyés. L'envoi de plusieurs segments de messages peut entraîner des frais supplémentaires."
  - name: Service des messages
    description: "Ensemble de codes longs, de codes courts et d'ID alphanumériques utilisés pour envoyer votre message SMS avec Braze."
  - name: Mot-clé
    description: "Mot court envoyé à un code court ou long pour interagir avec un programme SMS prédéfini ou pour demander l'ABSTENTION d'un programme spécifique ou de tous les programmes d'un code. Par exemple, <code>STOP</code>. Les mots-clés doivent <br> - être alphanumérique <br> - ne comportent pas d'espaces <br> - moins de 10 caractères. <br> <br> Une combinaison spécifique de mot-clé et de code court ne peut être utilisée que pour un seul programme actif à la fois. Si vous introduisez un mot-clé qui est déjà utilisé par un autre programme, une erreur de validation apparaîtra. <br> <br> Il existe deux catégories de mots-clés obligatoires auxquelles tous les fournisseurs de contenu SMS doivent se conformer : <code>STOP</code> et <code>HELP</code>."
  - name: Mot-clé obligatoire HELP
    description: "Pour chaque programme créé dans la plateforme du gestionnaire de campagnes SMS, le contenu de ce mot-clé doit être fourni et doit répondre aux meilleures pratiques et à la conformité de l'opérateur pour le pays ou la région dans lequel le trafic SMS est envoyé et reçu. Dans la plupart des cas, ce contenu doit contenir une brève explication du programme SMS et de la manière de s'y soustraire."
  - name: Mots clés Global STOP
    description: "Les variantes comprennent <code>STOP</code>, <code>END</code>, <code>QUIT</code>, <code>UNSUBSCRIBE</code>, <code>CANCEL</code>, <code>STOPALL</code>. C'est ce qu'on appelle les <code>mots-clés \"Global-Stop\"</code>. Si l'un de ces mots-clés est saisi dans un code court ou long, le numéro de téléphone mobile (le numéro de téléphone mobile d'origine) est exclu de tous les programmes SMS actifs sur le code auquel il est associé."
  - name: Code de la vanité
    description: "Un \"vanity short code\" est un numéro de téléphone de 5 à 6 chiffres spécifiquement choisi par une marque. Les codes courts de marque sont plus faciles à mémoriser pour les consommateurs."
  - name: Code court partagé
    description: "Lorsqu'on utilise un code court partagé, tous les messages textuels, quelle que soit l'entreprise ou l'organisation qui les envoie, arrivent sur l'appareil mobile du consommateur à partir du même numéro de téléphone 5-6. Bien que les codes courts partagés soient relativement peu coûteux et immédiatement disponibles, cela signifie que votre entreprise ne disposera pas d'un code court dédié et qu'elle sera soumise à l'obligation pour les autres entreprises de suivre le protocole correct avec votre code court partagé." 
  - name: "Alphanumérique ID de l'expéditeur"
    description: "L'ID d'expéditeur alphanumérique vous permet de définir le nom de votre entreprise ou de votre marque comme ID d'expéditeur en utilisant des caractères alphanumériques lors de l'envoi de messages unidirectionnels vers les pays pris en charge."
  - name: Numéro gratuit
    description: "Un numéro de téléphone gratuit ou numéro de libre appel est un numéro de téléphone qui est facturé pour tous les appels entrants au lieu d'être facturé à l'utilisateur du téléphone d'origine. Les numéros gratuits aux États-Unis et au Canada sont compatibles avec les SMS, c'est-à-dire que les abonnés sont facturés pour les textes entrants et sortants.<br><br>L'envoi de messages sans frais fonctionne mieux lorsque votre cas d'utilisation est de personne à personne, comme l'assistance à la clientèle ou les ventes, l'expéditeur et le destinataire ayant une conversation par texto."
  - name: Envoi de messages à sens unique
    description: "La messagerie unidirectionnelle vous permet de communiquer avec vos clients par l'envoi de messages textuels. L'envoi de messages unidirectionnels est utile si vous mettez en place un ID d'expéditeur alphanumérique sur des marchés où les codes longs et courts ne sont pas disponibles." 
  - name: Envoi de messages dans les deux sens
    description: "L'envoi de messages bidirectionnels vous permet de tenir une conversation en envoyant et en recevant des messages texte." 
---
