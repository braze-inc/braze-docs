---
nav_title: Depuração do SDK
article_title: Depuração do SDK do Braze 
description: "Saiba como usar o depurador do Braze SDK para solucionar problemas em seus canais com SDK, sem ativar manualmente o registro detalhado em seu app."
page_order: 13
---

# Depuração do SDK do Braze

> Saiba como usar o depurador integrado do Braze SDK para solucionar problemas em seus canais com SDK, sem precisar ativar o registro detalhado em seu app.

{% alert important %}
Atualmente, esse recurso está disponível apenas para aplicativos nativos para iOS e Android. Para ativar a depuração do Braze Web SDK, você pode [usar um parâmetro de URL]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#logging).
{% endalert %}

## Pré-requisitos

Para usar o depurador Braze SDK, certifique-se de que seus SDKs estejam atualizados com pelo menos essas versões mínimas:

{% sdk_min_versions swift:10.2.0 android:32.1.0 %}

## Depuração do SDK do Braze

### Etapa 1: Feche seu aplicativo

Antes de iniciar a sessão de depuração, feche o app que está apresentando problemas no momento. Você pode reiniciar o app no início de sua sessão.

### Etapa 2: Criar uma sessão de depuração

No Braze, acesse **Settings (Configurações)** e, em **Setup and Testing (Configuração e teste)**, selecione **SDK Debugger (Depurador SDK)**.

![A seção "Setup and Testing" (Configuração e teste) com "SDK Debugger" destacado.]({% image_buster /assets/img/sdk_debugger/select_sdk_debugger.png %})

Selecione **Criar sessão de depuração**.

![A página "SDK Debugger".]({% image_buster /assets/img/sdk_debugger/select_create_debugging_session.png %})

### Etapa 3: Selecione um usuário

Pesquise um usuário usando seu endereço de e-mail, `external_id`, alias de usuário ou token por push. Quando estiver pronto para iniciar a sessão, selecione **Select User (Selecionar usuário)**.

![A página de depuração do usuário selecionado.]({% image_buster /assets/img/sdk_debugger/search_and_select_user.png %}){: style="max-width:85%;"}

### Etapa 4: Reabra o app

Primeiro, inicie o app e confirme se o dispositivo está emparelhado. Se o emparelhamento for bem-sucedido, reinicie o aplicativo - isso garantirá que os registros de inicialização do app sejam totalmente capturados.

### Etapa 5: Conclua as etapas de reprodução

Depois de reiniciar o app, siga as etapas para reproduzir o erro.

{% alert tip %}
Quando estiver reproduzindo o erro, certifique-se de seguir as etapas de reprodução o mais fielmente possível, para que possa criar [registros de qualidade](#step-6-export-your-session-logs-optional).
{% endalert %}

### Etapa 6: Encerre sua sessão

Quando terminar as etapas de reprodução, selecione **Encerrar sessão** > **Fechar**.

![A sessão de depuração mostra o botão "End Session" (Finalizar sessão).]({% image_buster /assets/img/sdk_debugger/close_debugging_session.png %}){: style="max-width:85%;"}

{% alert note %}
Pode levar alguns minutos para gerar os registros, dependendo da duração da sessão e da conectividade da rede.
{% endalert %}

### Etapa 7: Compartilhe ou exporte sua sessão (opcional)

Após a sessão, é possível exportar os registros da sessão como um arquivo CSV. Além disso, outras pessoas podem usar seu **ID de sessão** para procurar sua sessão de depuração, portanto, não é necessário enviar seus registros diretamente.

![A página de depuração com "Exportar registros" e "Copiar ID da sessão" é mostrada após a sessão.]({% image_buster /assets/img/sdk_debugger/copy_id_and_export_logs.png %})
