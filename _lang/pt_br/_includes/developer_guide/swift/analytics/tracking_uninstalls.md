## Configurando o rastreamento de desinstalação

### Etapa 1: ativar push em segundo plano

Em seu projeto Xcode, acesse **Capacidades** e verifique se **os Modos de segundo plano** estão ativados. Para saber mais, consulte [notificação por push silenciosa]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift).

### Etapa 2: Ignorar notificações por push internas

O SDK Braze Swift usa notificações por push em segundo plano para coletar análises de rastreamento de desinstalação. Para garantir que seu app não execute ações indesejadas quando estas forem enviadas, você precisará garantir que [as notificações por push internas sejam ignoradas]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications).

### Etapa 3: Envie um push de teste (opcional)

Em seguida, envie uma notificação por push de teste para você mesmo a partir do dashboard do Braze (não se preocupe—não atualizará seu perfil de usuário).

1. Acesse **Envio de Mensagens** > **Campanhas** e crie uma campanha de notificação por push usando a plataforma relevante.
2. Acesse **Configurações** > **Configurações do App** e adicione a chave `appboy_uninstall_tracking` com o valor `true` relevante, depois verifique **Adicionar Flag de Conteúdo-Disponível**.
3. Use a página **Prévia** para enviar a si mesmo um push de rastreamento de desinstalação de teste.
4. Verifique se seu app não realiza nenhuma ação automática indesejada ao receber uma notificação por push.

{% alert note %}
Um número de badge será enviado junto com a notificação por push de teste—no entanto, um push de rastreamento de desinstalação real não enviará nenhum número de badge.
{% endalert %}

### Etapa 3: Ativar o rastreamento de desinstalação

Por fim, ative o rastreamento de desinstalação no Braze. Para um guia completo, veja [Ativar rastreamento de desinstalação]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking).

{% alert important %}
O rastreamento de desinstalações pode ser impreciso. As métricas que você vê no Braze podem sofrer postergação ou ser imprecisas.
{% endalert %}
