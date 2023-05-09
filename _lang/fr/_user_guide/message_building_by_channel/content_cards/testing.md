---
nav_title: Test
article_title: Tester des cartes de contenu
page_order: 3
description: "Le présent article de référence explique comment prévisualiser et tester les cartes de contenu, et décrit certaines des meilleures pratiques."
channel:
  - cartes de contenu
  
---

# Tester des cartes de contenu

> Il est extrêmement important de toujours tester vos cartes de contenu avant d’envoyer vos campagnes. Nos capacités de prévisualisation et de test offrent deux façons de vérifier vos cartes de contenu. Vous pouvez prévisualiser votre message pendant que vous le composer, et vous envoyer un message de test (ou un autre appareil spécifique). Nous vous recommandons d’utiliser les deux.

## Aperçu

Vous pouvez prévisualiser votre carte lorsque vous la composez. Cela devrait vous aider à visualiser à quoi ressemblera votre message final du point de vue de l’utilisateur.

Sur l’onglet **Preview (Aperçu)** de votre compositeur, la vue de votre message peut ne pas être identique à son rendu réel sur l’appareil de l’utilisateur. Nous vous recommandons d’envoyer toujours un message test à un appareil pour vérifier que votre support, votre texte, votre personnalisation et vos attributs personnalisés sont générés correctement.

## Test

Pour envoyer un test à [groupes]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou des utilisateurs individuels pour tester votre contenu, la notification push doit être activé sur vos appareils de test avant l’envoi. Pour les utilisateurs iOS, vous devez appuyer sur la notification push envoyée par Braze pour afficher la carte de contenu test. Ce comportement s’applique uniquement aux tests des cartes de contenu.

### Aperçu du message en tant qu’utilisateur

Sur l’onglet **Test**, vous pouvez également prévisualiser les messages comme si vous étiez un utilisateur. Vous pouvez sélectionner un utilisateur spécifique, un utilisateur aléatoire ou créer un utilisateur personnalisé.

![Custom_User_Preview][3]

### Liste de contrôle des tests

- Les images et les données s’affichent-elles et se comportent-elles comme prévu ?
- Le Liquid fonctionne-t-il comme prévu ? Avez-vous pris en compte une [valeur d’attribut par défaut]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) si Liquid ne renvoie aucune information ?
- Votre texte est-il clair, concis et correct ?
- Vos liens dirigent-ils l’utilisateur vers les bons endroits ?

## Débogage

Une fois que vos cartes de contenu sont envoyées, vous pouvez identifier ou déboguer les éventuels problèmes dans le [Journal d'événements utilisateurs]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/) sur la Console Développeur. 

C’est notamment utile pour comprendre pourquoi un utilisateur n’arrive pas à voir une carte de contenu spécifique. Dans ce cas, vous pouvez regarder dans le **Journal d'événements utilisateurs** les cartes de contenu livrées au SDK lors du démarrage de session, mais avant une impression, pour identifier la campagne spécifique en question :

1. Allez sur la **Developer Console** et sélectionnez l’onglet **Journal d'événements utilisateurs**.
2. Localisez et développez la demande SDK pour votre utilisateur test.
3. Cliquez sur **Raw Data (Données brutes)**.
4. Trouvez le `id` pour votre session. Voici un échantillon d’exemple :

    ```json
    [
      {
        "session_id": "D1B051E6-469B-47E2-B830-5A728D1D4AC5",
        "data": {
          "ids": [
            "NjE4NTAwNWE5ZDliZWU3OTM4N2NjZTQzXyRfY2M9YzNiMjU3NDAtZjExMy1jMDQ3LTRiMWQtZDI5NmYyODBhZjRmJm12PTYxODUwMDViOWQ5YmVlNzkzODdjY2U0NSZwaT1jbXA="
          ]
        },
        "name": "cci",
        "time": 1636106490.155
      }
    ]
    ```

5. Utiliser un outil de décodage comme [l’encodeur/décodeur Base64](https://www.base64decode.org/) pour décoder le `id` au format Base64 et trouver la `campaign_id` associée. Dans notre exemple, cela donne les résultats suivants :

    ```
    6185005a9d9bee79387cce43_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    Où `6185005a9d9bee79387cce43` est le `campaign_id`.<br><br>

6. Allez sur la page **Campaigns (Campagnes)** et recherchez `campaign_id`.

![Rechercher campaign_id sur la page Campaigns (Campagnes)][1]

Ensuite, vous pouvez examiner les paramètres et le contenu de vos messages pour déterminer pourquoi un utilisateur ne voit pas une carte de contenu particulière.

[1]: {% image_buster /assets/img_archive/cc_debug.png %}
[3]: {% image_buster /assets/img/cc-user-preview.png %}
