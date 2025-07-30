---
nav_title: Solução de problemas
article_title: Solução de problemas de push
page_order: 23
page_type: reference
description: "Esta página contém etapas de solução de problemas para vários problemas relacionados ao canal de envio de mensagens Push."
channel: push
---

# Solução de problemas de push

> Esta página o ajuda a solucionar vários problemas que podem ocorrer com o canal de envio de mensagens Push.

## Falta de notificações por push

Está enfrentando desafios de entrega com notificações por push? Há uma série de etapas que você pode seguir para solucionar esse problema, verificando o seguinte:

- [Status da inscrição por push](#push-subscription-status)
- [Segmento](#segment)
- [Limites de notificação por push](#push-notification-caps)
- [Limites de frequência](#rate-limits)
- [Status do grupo de controle](#control-group-status)
- [Token por push válido](#valid-push-token)
- [Tipo de notificação por push](#push-notification-type)
- [Aplicativo atual](#current-app)

#### Status da inscrição por push

Os pushs só podem ser enviados para usuários inscritos ou com aceitação. Verifique seu perfil de usuário na guia [Engajamento]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab), na seção **Perfil do usuário**, para confirmar se está ativamente registrado para push no espaço de trabalho que está testando. Se estiver registrado em vários apps, eles serão listados no campo **Push Registered For**:

![Push registrado para]({% image_buster /assets/img_archive/trouble1.png %})

Também é possível exportar os perfis de usuário usando os endpoints de exportação do Braze:
- [Usuários por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [Usuários por segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)

Qualquer um dos endpoints retornará um objeto de token por push que inclui informações de capacitação por push por dispositivo.

#### Segmento

Confira se você se enquadra no segmento que está direcionando (se essa for uma campanha ativa e não um teste). No **Perfil do usuário**, você verá uma lista dos segmentos em que o usuário se enquadra atualmente. Lembre-se de que essa é uma variável em constante mudança, pois a segmentação é atualizada em tempo real.

![Lista de segmentos]({% image_buster /assets/img_archive/trouble2.png %})

Você também pode confirmar que o usuário faz parte do segmento usando o **User Lookup** ao criar um segmento.

![Seção User Lookup com um campo de pesquisa.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

#### Limites de notificação por push

Verifique os limites de frequência global. É possível que você não tenha recebido a notificação por push porque seu espaço de trabalho tem um limite de frequência global em vigor e você já atingiu o limite de notificações por push para o período de tempo especificado.

Você pode fazer isso verificando [o limite de frequência global]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over) no dashboard. Se a campanha for definida para obedecer às regras de limite de frequência, haverá vários usuários afetados por essas configurações

![Detalhes da campanha]({% image_buster /assets/img_archive/trouble3.png %})

#### Limites de frequência

Se você tiver um limite de frequência definido para sua campanha ou Canva, pode estar deixando de receber envios de mensagens por exceder esse limite. Para saber mais, consulte [Limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting).

#### Status do grupo de controle

Se essa for uma campanha de canal único ou um Canva com um grupo de controle, é possível que você esteja se enquadrando no grupo de controle.

  1. Verifique a [distribuição de variantes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants) para ver se há um grupo de controle.
  2. Em caso afirmativo, crie uma filtragem de segmento para o [grupo de controle da campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter), [exporte o segmento]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/segment_data_to_csv/#exporting-to-csv) e verifique se o seu ID de usuário está nessa lista.

#### Token por push válido
Um token por push é um identificador que os remetentes usam para direcionar uma notificação por push a dispositivos específicos. Portanto, se o dispositivo não tiver um token por push válido, não haverá como enviar uma notificação por push para ele. 

#### Tipo de notificação por push

Verifique se está usando o tipo correto de notificação por push. Por exemplo, se quiser direcionar uma FireTV, você usaria uma notificação por push do Kindle, não uma campanha por push do Android. Da mesma forma, se você quiser direcionar um Android, use uma notificação por push para Android e não uma campanha por push para iOS. Dê uma olhada nos artigos a seguir para obter mais informações sobre como entender o fluxo de trabalho da Braze:
- [Notificações por push da Apple]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)
- [Firebase Cloud Messaging]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)

#### Aplicativo atual

Ao testar envios por push com usuários internos, certifique-se de que o usuário que deseja receber a notificação por push esteja atualmente registrado no app relevante. Isso pode fazer com que o usuário não receba um push ou receba um push para o qual você acredita que ele não está segmentado.

Ainda precisa de ajuda? Abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).

