## Configuração do rastreamento de desinstalação

### Etapa 1: ativar push em segundo plano

Em seu projeto Xcode, acesse **Capacidades** e verifique se **os Modos de segundo plano** estão ativados. Para saber mais, consulte [notificação por push silenciosa]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift).

### Etapa 2: Ignorar notificações por push internas

O SDK do Swift Braze usa notificações por push em segundo plano para coletar análises de dados de rastreamento de desinstalação. Para garantir que seu app não realize ações indesejadas quando elas forem enviadas, será necessário garantir que [as notificações por push internas sejam ignoradas]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications).

### Etapa 3: Enviar um push de teste (opcional)

Em seguida, envie a si mesmo uma notificação por push de teste no dashboard do Braze (não se preocupe - ela não atualizará seu perfil de usuário).

1. Acesse Campanha **de mensagens** > **Campanhas** e crie uma campanha de notificação por push usando a plataforma relevante.
2. Acesse **Settings** > **App Settings (Configurações > Configurações do app** ) e adicione a chave `appboy_uninstall_tracking` com o valor `true` relevante e, em seguida, marque **Add Content-Available Flag (Adicionar sinalizador de conteúdo disponível**).
3. Use a página **Prévia** para enviar a si mesmo um push de rastreamento de desinstalação de teste.
4. Verifique se o app não executa nenhuma ação automática indesejada quando recebe uma notificação por push.

{% alert note %}
Um número de crachá será enviado junto com a notificação por push de teste - no entanto, um push de rastreamento de desinstalação real não enviará nenhum número de crachá.
{% endalert %}

### Etapa 3: Ativar o rastreamento de desinstalação

Por fim, ative o rastreamento de desinstalação no Braze. Para obter um passo a passo completo, consulte [Ativar o rastreamento de desinstalação]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking).

{% alert important %}
O rastreamento de desinstalações pode ser impreciso. As métricas que você vê no Braze podem sofrer postergação ou ser imprecisas.
{% endalert %}
