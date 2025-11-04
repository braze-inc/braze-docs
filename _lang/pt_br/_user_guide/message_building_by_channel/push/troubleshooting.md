---
nav_title: Solução de problemas
article_title: Solução de problemas Push
page_order: 23
page_type: reference
description: "Esta página contém etapas de solução de problemas para vários problemas relacionados ao canal de mensagens Push."
channel: push
---

# Solução de problemas Push

> Esta página o ajuda a solucionar vários problemas que podem ocorrer com o canal de mensagens Push.

## Falta de notificações push

Está enfrentando desafios de entrega com notificações por push? Há várias etapas que podem ser seguidas para solucionar esse problema, verificando o seguinte:

- [Status da assinatura push](#push-subscription-status)
- [Segmento](#segment)
- [Tampas de notificação por push](#push-notification-caps)
- [Limites de taxas](#rate-limits)
- [Status do grupo de controle](#control-group-status)
- [Token de envio válido](#valid-push-token)
- [Tipo de notificação push](#push-notification-type)
- [Aplicativo atual](#current-app)

#### Status da assinatura push

Os pushs só podem ser enviados para usuários inscritos ou opt-in. Verifique o seu perfil de usuário na guia [Envolvimento]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab), na seção **Perfil do usuário**, para confirmar se você está ativamente registrado para o push do espaço de trabalho que está testando. Se você estiver registrado em vários aplicativos, eles serão listados no campo **Push Registered For**:

\![Push Registered For]({% image_buster /assets/img_archive/trouble1.png %})

Você também pode exportar os perfis de usuário usando os endpoints de exportação do Braze:
- [Usuários por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [Usuários por segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)

Qualquer um dos pontos de extremidade retornará um objeto de token de envio que inclui informações de ativação de envio por dispositivo.

#### Segmento

Verifique se você se enquadra no segmento que está segmentando (se essa for uma campanha ativa e não um teste). No **Perfil do usuário**, você verá uma lista dos segmentos em que o usuário se enquadra atualmente. Lembre-se de que essa é uma variável em constante mudança, pois a segmentação é atualizada em tempo real.

\![Lista de segmentos]({% image_buster /assets/img_archive/trouble2.png %})

Você também pode confirmar que o usuário faz parte do segmento usando o **User Lookup** ao criar um segmento.

\![Seção User Lookup com um campo de pesquisa.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

#### Tampas de notificação por push

Verifique os limites de frequência global. É possível que você não tenha recebido a notificação por push porque seu espaço de trabalho tem um limite de frequência global em vigor e você já atingiu o limite de notificações por push para o período de tempo especificado.

Você pode fazer isso verificando [o limite de frequência global]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over) no painel. Se a campanha for definida para obedecer às regras de limite de frequência, haverá vários usuários afetados por essas configurações

\![Detalhes da campanha]({% image_buster /assets/img_archive/trouble3.png %})

#### Limites de taxas

Se você tiver um limite de taxa definido para sua campanha ou Canvas, poderá deixar de receber mensagens por exceder esse limite. Para obter mais informações, consulte [Limitação de taxa]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting).

#### Status do grupo de controle

Se essa for uma campanha de canal único ou um Canvas com um grupo de controle, é possível que você esteja se enquadrando no grupo de controle.

  1. Verifique a [distribuição de variantes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants) para ver se há um grupo de controle.
  2. Se for o caso, crie um filtro de segmento para o [grupo de controle de campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter), [exporte o segmento]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/segment_data_to_csv/#exporting-to-csv) e verifique se o seu ID de usuário está nessa lista.

#### Token de envio válido
Um token push é um identificador que os remetentes usam para direcionar dispositivos específicos com uma notificação push. Portanto, se o dispositivo não tiver um token push válido, não haverá como enviar uma notificação push para ele. 

#### Tipo de notificação push

Verifique se você está usando o tipo correto de notificação por push. Por exemplo, se você quiser segmentar uma FireTV, usará uma notificação por push do Kindle, não uma campanha por push do Android. Da mesma forma, se você quiser segmentar um Android, use uma notificação push para Android e não uma campanha push para iOS. Confira os artigos a seguir para obter mais informações sobre como entender o fluxo de trabalho do Braze:
- [Notificação por push da Apple]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)
- [Mensagens na nuvem do Firebase]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)

#### Aplicativo atual

Ao testar os envios por push com usuários internos, certifique-se de que o usuário que deseja receber a notificação por push esteja conectado no momento ao aplicativo relevante. Isso pode fazer com que o usuário não receba um push ou receba um push para o qual você acredita que ele não está segmentado.

## Cliques push inesperadamente abertos no aplicativo

Se estiver tendo problemas com links em notificações por push que abrem inesperadamente no seu aplicativo em vez de no navegador da Web, pode haver um problema com a configuração da sua campanha ou com a implementação do SDK. Consulte estas etapas para obter ajuda.

### Verificar o comportamento ao clicar

Na etapa da campanha ou do Canvas, verifique se a opção **Abrir URL da Web dentro do aplicativo móvel** não está selecionada. Se for o caso, limpe a seleção e reinicie. 

Campo "["Comportamento ao clicar"] da configuração de um push definido como "Abrir URL da Web" com "Abrir URL da Web dentro do aplicativo móvel" desmarcado.]({% image_buster /assets/img/push_on_click.png %})

A interação padrão para o comportamento ao clicar "Abrir URL da Web" difere de acordo com a versão do SDK. Para as versões do SDK iOS 2.29.0 e Android 2.0.0 e superiores, essa opção é selecionada por padrão e os URLs da Web serão abertos em uma visualização da Web dentro do aplicativo. Antes dessas versões, essa opção é desmarcada por padrão e os URLs da Web são abertos no navegador da Web padrão do dispositivo.

Se esse não for o problema, pode haver um problema com sua implementação do push. 

### Verifique novamente a integração por push

Se os links em suas notificações push estiverem abrindo no aplicativo inesperadamente, isso pode ser devido a problemas com a integração da notificação push ou com as configurações de personalização. Siga estas etapas para solucionar o problema:

1. **Revise a implementação do delegado push:** Certifique-se de que o delegado push do Braze esteja implementado corretamente. Para obter instruções detalhadas, consulte o guia de integração para notificações por push de sua [plataforma]({{site.baseurl}}/developer_guide/home/).
2. **Inspecionar o tratamento de links personalizados:** Verifique se o aplicativo inclui tratamento personalizado para todos os links `https://`. As configurações personalizadas podem substituir os comportamentos padrão. Colabore com sua equipe de desenvolvimento para revisar e ajustar essas configurações, se necessário.
3. **Verifique o registro de push do iOS:** Para iOS, reveja a etapa 1 do guia de integração por push sobre o [registro de notificações por push com APNs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-register-for-push-notifications-with-apns). Certifique-se de que seu objeto delegado seja atribuído de forma síncrona antes que o aplicativo termine de ser iniciado. Essa etapa deve ser concluída no método `application:didFinishLaunchingWithOptions:`.
4. **Teste sua integração:** Depois de fazer os ajustes, teste o comportamento da notificação por push nos dispositivos iOS e Android para confirmar que o problema foi resolvido.

## As notificações Web Push não estão se comportando como esperado

Se estiver tendo problemas com as notificações por push no navegador, talvez seja necessário redefinir as permissões de notificação do site e limpar o armazenamento do site. Consulte estas etapas para obter ajuda.

{% tabs %}
{% tab Chrome %}

### Redefinir o Chrome no desktop

1. Ao lado do seu URL no navegador Chrome, selecione o ícone do controle deslizante **Exibir informações do site**.
2. Em **Notifications (Notificações**), selecione **Reset permission (Redefinir permissão**).
3. Abra o Chrome DevTools. Veja a seguir os atalhos relevantes por sistema operacional.

<style> 
table {
    max-width: 50%;
}
</style>

| SO      | Atalhos de teclado                                                  |
| ------- | ------------------------------------------------------------------- |
| Mac      | `Fn` + `F12`<br>`Ctrl` + `Shift` + `I` |
| Windows | `F12`<br>`Ctrl` + `Shift` + `I` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="4"}
4\. No DevTools, navegue até a guia **Application (Aplicativo** ).
5\. Na barra lateral, selecione **Armazenamento**.
6\. Selecione **Limpar dados do site**.
7\. O Chrome solicitará que você recarregue a página para aplicar as configurações atualizadas. Selecione **Recarregar**.

Suas permissões de envio agora foram redefinidas. Abra uma nova guia em seu site e experimente.

### Redefinir o Chrome no Android

Se você tiver uma notificação do seu site visível na gaveta de notificações do Android:

1. Na notificação por push, toque em <i class="fas fa-cog" title="Configurações"></i> e selecione **Configurações do site**.
2. Nas **configurações do site**, toque em **Clear & Reset**.

Se você não tiver uma notificação de seu site aberta:

1. Abra o Chrome no Android.
2. Toque no menu <i class="fas fa-ellipsis-vertical"></i>.
3. Vá para **Configurações** > **Configurações do site** > **Notificações**.
4. Verifique se as notificações estão definidas como **Perguntar antes de enviar (recomendado)**.
5. Encontre seu site na lista.
6. Selecione a entrada e toque em **Limpar e redefinir**.

Suas permissões de envio agora foram redefinidas. Abra uma nova guia em seu site e experimente.

{% endtab %}
{% tab Firefox %}

### Redefinir o Firefox na área de trabalho

1. Ao lado do URL do seu site, selecione <i class="fa-solid fa-circle-info" alt="info icon"></i> ou <i class="fas fa-lock" alt="lock icon"></i>.
2. Em **Permissões**, ao lado de **Receber notificações**, selecione <i class="fa-solid fa-circle-xmark" title="Limpar essa permissão e perguntar novamente"></i> para limpar as permissões de notificação.
3. No mesmo menu, selecione **Limpar cookies e dados do site**.
4. Na caixa de diálogo para confirmar sua escolha, selecione **OK**.

Suas permissões de envio agora foram redefinidas. Abra uma nova guia em seu site e experimente.

### Redefinir o Firefox no Android

Para redefinir as permissões de envio no Android, consulte este [artigo de suporte da Mozilla](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser).

{% endtab %}
{% tab Safari %}

### Redefinir o Safari no macOS

{% alert note %}
Essas etapas são apenas para o macOS, pois a Apple não oferece suporte ao Web Push para o Safari no Windows.
{% endalert %}

1. Abra o Safari.
2. Na [barra de menus do Mac](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac), vá para **Safari** > **Configurações** > **Sites** > **Notificações**.
3. Selecione seu site na lista.
4. Selecione **Remover** para excluir as permissões de notificação do site.
5. Em seguida, vá para **Privacy** > **Manage Website Data (** **Privacidade** > **Gerenciar dados do site**).
6. Selecione seu site na lista.
7. Selecione **Remove (Remover**) ou, para remover todos os dados do site, selecione **Remove All (Remover tudo**).
8. Selecione **Concluído**.

Suas permissões de envio agora foram redefinidas. Abra uma nova guia em seu site e experimente.

{% endtab %}
{% endtabs %}

Ainda precisa de ajuda? Abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).

