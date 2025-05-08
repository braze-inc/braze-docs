---
nav_title: Falta de notificações por push
article_title: Falta de notificações por push
page_order: 3

page_type: solution
description: "Este artigo de ajuda o orienta nas etapas de solução de problemas que podem ser executadas se os usuários não estiverem recebendo suas notificações por push."
channel: push
---
# Falta de notificações por push

Está enfrentando desafios de entrega com notificações por push? Há uma série de etapas que você pode seguir para solucionar esse problema, verificando o seguinte:

* [Status da inscrição por push](#push-subscription-status)
* [Segmento](#segment)
* [Limites de notificação por push](#push-notification-caps)
* [Limites de frequência](#rate-limits)
* [Status do grupo de controle](#control-group-status)

### Status da inscrição por push

Verifique seu perfil de usuário na guia [Engajamento][1], na seção **Perfil do usuário**, para ver se está ativamente registrado para push no espaço de trabalho que está testando. Se estiver registrado em vários apps, você os verá listados no campo **Push Registered For**:

![Push registrado para][2]

Também é possível exportar os perfis de usuário usando os endpoints de exportação do Braze:
- [Usuários por identificador][12]
- [Usuários por segmento][13]

Qualquer um dos endpoints retornará um objeto de token por push que inclui informações de capacitação por push por dispositivo.

### Segmento

Confira se você se enquadra no segmento que está direcionando (se essa for uma campanha ativa e não um teste). No **Perfil do usuário**, você verá uma lista dos segmentos em que o usuário se enquadra atualmente. Lembre-se de que essa é uma variável em constante mudança, pois a segmentação é atualizada em tempo real.

![Lista de segmentos][3]

### Limites de notificação por push

Verifique os limites de frequência global. É possível que você não tenha recebido a notificação por push porque seu espaço de trabalho tem um limite de frequência global em vigor e você já atingiu o limite de notificações por push para o período de tempo especificado.

Você pode fazer isso verificando [global frequency capping][4] no dashboard. Se a campanha for definida para obedecer às regras de limite de frequência, haverá vários usuários afetados por essas configurações

![Detalhes da campanha][5]

### Limites de frequência

Se você tiver um limite de frequência definido para sua campanha ou Canva, pode estar deixando de receber envios de mensagens por exceder esse limite. Para saber mais, consulte [Limite de frequência][9].

### Status do grupo de controle

Se essa for uma campanha de canal único ou um Canva com um grupo de controle, é possível que você esteja se enquadrando no grupo de controle.

  1. Verifique a [distribuição de variantes][6] para ver se há um grupo de controle.
  2. Em caso afirmativo, crie uma filtragem de segmento para [no grupo de controle de campanha][7] e, em seguida, [exporte o segmento][8] e verifique se o seu ID de usuário está nessa lista.

### Token por push válido
Um token por push é um identificador que os remetentes usam para direcionar uma notificação por push a dispositivos específicos. Portanto, se o dispositivo não tiver um token por push válido, não haverá como enviar uma notificação por push para ele. 

### Tipo de notificação por push

Verifique se está usando o tipo correto de notificação por push. Por exemplo, se quiser direcionar uma FireTV, você usaria uma notificação por push do Kindle, não uma campanha por push do Android. Dê uma olhada nos artigos a seguir para obter mais informações sobre como entender o fluxo de trabalho da Braze:
- [Notificações por push da Apple][10]
- [Envio de mensagens do Firebase Cloud][11]

Ainda precisa de ajuda? Abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).

_Última atualização em 21 de janeiro de 2021_

[1]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab
[2]: {% image_buster /assets/img_archive/trouble1.png %}
[3]: {% image_buster /assets/img_archive/trouble2.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over
[5]: {% image_buster /assets/img_archive/trouble3.png %}
[6]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants
[7]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter
[8]: {{site.baseurl}}/user_guide/data_e_analytics/export_braze_data/segment_data_to_csv/#exporting-to-csv
[9]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/troubleshooting/
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/troubleshooting
[12]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier
[13]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment