---
page_order: 1.3
nav_title: Depuração
article_title: Depuração do SDK da Braze 
description: "Saiba como usar o depurador do SDK da Braze para solucionar problemas em seus canais com SDK, sem ativar manualmente o registro detalhado em seu app."
---

# Depuração do SDK da Braze

> Saiba como usar o depurador integrado do SDK da Braze para solucionar problemas em seus canais com SDK, sem precisar ativar o registro detalhado em seu app.

{% alert tip %}
Para uma investigação mais aprofundada, você também pode [ativar o registro detalhado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging) para capturar a saída detalhada do SDK e [aprender a ler logs detalhados]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs) para canais específicos.
{% endalert %}

## Pré-requisitos

Para usar o depurador do SDK da Braze, você precisará das permissões granulares "Ver IPI" e "Ver Perfis de Usuários (IPI Ocultada)" (ou das permissões legadas "Ver Perfis de Usuários em Conformidade com IPI"). Para baixar os registros da sua sessão de depuração, você também precisará da permissão "Exportar dados de usuários". Além disso, seu SDK da Braze precisa atender ou apontar para as seguintes versões mínimas: 

{% sdk_min_versions swift:10.2.0 android:32.1.0 %}

## Depuração do SDK da Braze

{% alert tip %}
Para ativar a depuração do Braze Web SDK, você pode [usar um parâmetro de URL]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#logging).
{% endalert %}

### Etapa 1: Feche seu app

Antes de iniciar a sessão de depuração, feche o app que está apresentando problemas no momento. Você pode reabrir o app no início da sua sessão.

### Etapa 2: Crie uma sessão de depuração

Na Braze, acesse **Settings** e, em **Setup and Testing**, selecione **SDK Debugger**.

![A seção "Setup and Testing" com "SDK Debugger" destacado.]({% image_buster /assets/img/sdk_debugger/select_sdk_debugger.png %})

Selecione **Create debugging session**.

![A página "SDK Debugger".]({% image_buster /assets/img/sdk_debugger/select_create_debugging_session.png %})

### Etapa 3: Selecione um usuário

Pesquise um usuário usando seu endereço de e-mail, `external_id`, alias de usuário ou token por push. Quando estiver pronto para iniciar a sessão, selecione **Select User**.

![A página de depuração para o usuário selecionado.]({% image_buster /assets/img/sdk_debugger/search_and_select_user.png %}){: style="max-width:85%;"}

### Etapa 4: Reabra o app

Primeiro, abra o app e confirme se o dispositivo está emparelhado. Se o emparelhamento for bem-sucedido, reinicie o app — isso garantirá que os registros de inicialização do app sejam totalmente capturados.

### Etapa 5: Reproduza o erro

Depois de reiniciar o app, siga as etapas para reproduzir o erro.

{% alert tip %}
Quando estiver reproduzindo o erro, certifique-se de seguir as etapas de reprodução o mais fielmente possível, para que possa criar [registros de qualidade](#step-6-export-your-session-logs-optional).
{% endalert %}

### Etapa 6: Encerre sua sessão

Quando terminar as etapas de reprodução, selecione **End Session** > **Close**.

![A sessão de depuração mostrando o botão "End Session".]({% image_buster /assets/img/sdk_debugger/close_debugging_session.png %}){: style="max-width:85%;"}

{% alert note %}
Pode levar alguns minutos para gerar os registros, dependendo da duração da sessão e da conectividade da rede.
{% endalert %}

### Etapa 7: Compartilhe ou exporte sua sessão (opcional)

Após a sessão, é possível exportar os registros da sessão como um arquivo CSV. Além disso, outras pessoas podem usar seu **Session ID** para procurar sua sessão de depuração, então não é necessário enviar seus registros diretamente.

![A página de depuração com "Export Logs" e "Copy Session ID" mostrados após a sessão.]({% image_buster /assets/img/sdk_debugger/copy_id_and_export_logs.png %})