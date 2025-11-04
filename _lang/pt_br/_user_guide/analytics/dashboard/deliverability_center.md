---
nav_title: Centro de entregabilidade
article_title: Centro de entregabilidade
page_order: 4
description: "Este artigo de referência aborda como configurar o Deliverability Center, um recurso que permite que os profissionais de marketing visualizem seus domínios de envio de e-mail e reputações de IP e entendam sua capacidade de entrega de e-mail."
channel:
  - email

---

# Centro de entregabilidade

> O Deliverability Center fornece mais informações sobre o desempenho de seu e-mail, apoiando o uso do [Gmail Postmaster Tools](https://www.gmail.com/postmaster/) para rastrear dados sobre e-mails enviados e coletar dados sobre seu domínio de envio.

A capacidade de entrega de e-mails é o núcleo do sucesso da campanha. Usando o Deliverability Center no painel de controle do Braze, você pode visualizar seus domínios por **Reputação de IP** ou **Erros de Entrega** para descobrir e solucionar quaisquer problemas potenciais com a capacidade de entrega de e-mail. 

Para acessar o Deliverability Center, você precisará das [permissões de usuário]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)"Access Campaigns, Canvases, Cards, Segments, Media Library" e "View Usage Data".

## Configuração de sua conta do Google Postmaster

Antes de se conectar ao Deliverability Center, você precisará configurar uma conta do Google Postmaster Tools. Você pode usar uma conta de trabalho ou pessoal do Gmail para configurar seu Google Postmaster. 

1. Acesse o [painel de controle do Google Postmaster Tools](https://postmaster.google.com/managedomains?pli=1).
2. No canto inferior direito, selecione o ícone de adição <i class="fas fa-plus-circle"></i>.
3. Digite seu domínio raiz ou subdomínio para autenticar seu e-mail. Se você estiver adicionando e verificando o domínio raiz, isso permitirá que a verificação seja aplicada posteriormente aos subdomínios. Por exemplo, ao verificar `braze.com`, você pode adicionar posteriormente `demo.braze.com` e outros subdomínios sem precisar verificá-los individualmente.
4. O Google gerará um registro TXT que pode ser adicionado diretamente ao DNS do seu domínio. Geralmente, ele pertence a quem gerencia seu DNS. Para obter informações e orientações sobre como atualizar seu DNS específico, consulte [Verificar seu domínio (etapas específicas do host)](https://support.google.com/a/topic/1409901).
5. Selecione **Next**. <br>\![Um exemplo de domínio "demo.braze.com" para autenticar um e-mail.]({% image_buster /assets/img_archive/domain_authentication.png %})
6. Depois que o registro TXT for adicionado ao DNS, retorne ao painel do Google Postmaster Tools e selecione **Verificar**. Essa etapa confirma que você é o proprietário do domínio e, portanto, poderá acessar as métricas de capacidade de entrega do Gmail na sua conta Postmaster. <br> \![Um prompt para verificar a propriedade do domínio "demo.braze.com".]({% image_buster /assets/img_archive/domain_verification.png %})

{% alert tip %}
Certifique-se de que o registro TXT esteja vinculado ao domínio principal, e não ao subdomínio que você está usando por meio do Braze.
{% endalert %}

{% alert note %}
Se os seus subdomínios não estiverem incluídos no Deliverability Center do Google Postmaster, isso pode ser resultado da adição apenas do domínio principal ao Google Postmaster. Depois que os domínios principais forem verificados no Google Postmaster, você poderá adicionar seus subdomínios, que serão verificados automaticamente. Esse processo permite que o Google informe sobre as métricas no nível do subdomínio, que podem então ser inseridas no Braze Deliverability Center.
{% endalert %}

## Integração do Google Postmaster

Antes de configurar o Deliverability Center, verifique se seus domínios foram [adicionados ao Gmail Postmaster Tools](https://support.google.com/mail/answer/9981691?hl=en).

Siga estas etapas para fazer a integração com o Google Postmaster e configurar seu Deliverability Center:

1. Vá para **Analytics** > **Email Performance**.
2. Selecione a guia **Deliverability Center**. <br>\![Um Centro de entregabilidade com o Google Postmaster não conectado.]({% image_buster /assets/img_archive/deliverability_center1.png %})
3. Selecione **Conectar com o Google Postmaster**. 
4. Selecione sua conta do Google e, em seguida, selecione **Allow (Permitir** ) para permitir que o Braze visualize as métricas de tráfego de e-mail dos domínios registrados nas Postmaster Tools. 

Seus domínios verificados serão exibidos no Deliverability Center. 

\![Dois domínios verificados para o Google Postmaster com reputação média e baixa.]({% image_buster /assets/img_archive/deliverability_center2.png %})

Você também pode acessar o Google Postmaster no painel do Braze, indo para **Partner Integrations** > **Technology Partners** > **Google Postmaster**. Após a integração, o Braze extrai dados de reputação e erros dos últimos 30 dias. Os dados podem não estar disponíveis imediatamente e podem levar vários minutos para serem preenchidos.

### Métricas e definições

As métricas e definições a seguir se aplicam ao Google Postmaster Tools.

#### Reputação de IP 

Para ajudar a entender as classificações de reputação de IP, consulte esta tabela:

| Classificação da reputação | Definição |
| ----- | ---------- |
| Alta | Tem um bom histórico de geração de poucas reclamações de spam (como usuários que clicam no botão "spam"). |
| Médio/Fraco | Conhecido por gerar engajamento positivo, mas ocasionalmente recebe reclamações de spam. A maioria dos e-mails desse domínio será enviada para a caixa de entrada, exceto quando as reclamações de spam aumentarem. |
| Baixa | Conhecido por receber regularmente taxas elevadas de reclamações de spam. Os e-mails desse remetente provavelmente serão filtrados para a pasta de spam. |
| Ruim | Tem um histórico de receber taxas elevadas de reclamações de spam. Os e-mails desse domínio quase sempre serão rejeitados no momento da conexão ou filtrados para a pasta de spam. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Reputação do domínio 

Use a tabela a seguir para ajudar a monitorar e entender as classificações de reputação do seu domínio e evitar que ele seja filtrado em uma pasta de spam.

| Classificação da reputação | Definição |
| ----- | ---------- |
| Alta | Tem um bom registro de reclamações de spam muito baixas. Está em conformidade com as diretrizes de remetente do Gmail. Os e-mails raramente são filtrados para a pasta de spam. Tem um bom histórico de uma taxa de spam muito baixa. Está em conformidade com as [diretrizes de remetente do Gmail](https://developers.google.com/gmail/markup/registering-with-google). |
| Médio/Fraco | Conhecido por gerar engajamento positivo, mas ocasionalmente recebeu um baixo volume de reclamações de spam. A maioria dos e-mails desse domínio chegará à caixa de entrada (exceto quando houver um aumento notável nos níveis de spam). |
| Baixa | Conhecido por receber reclamações de spam regularmente. Os e-mails desse remetente provavelmente serão filtrados para a pasta de spam. |
| Ruim | Tem um histórico de receber taxas elevadas de reclamações de spam. Os e-mails desse domínio quase sempre serão rejeitados no momento da conexão ou filtrados para a pasta de spam. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Autenticação

Use o painel de autenticação para analisar a porcentagem de e-mails que foram aprovados no Sender Policy Framework (SPF), no DomainKeys Identified Mail (DKIM) e no Domain-based Message Authentication, Reporting and Conformance (DMARC).

| Tipo de gráfico | Definição |
| ----- | ---------- |
| FPS | Mostra a porcentagem de e-mails que foram aprovados no SPF em relação a todos os e-mails do domínio que tentaram o SPF. Isso exclui qualquer e-mail falsificado. |
| DKIM | Mostra a porcentagem de e-mails que foram aprovados no DKIM em relação a todos os e-mails do domínio que tentaram o DKIM. |
| DMARC | Mostra a porcentagem de e-mails que passaram no alinhamento DMARC em relação a todos os e-mails recebidos do domínio que passaram no SPF ou no DKIM. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Criptografia

Consulte esta tabela para saber qual porcentagem do seu tráfego de entrada e saída é criptografada.

| Prazo | Definição |
| ----- | ---------- |
| Entrada de TLS | Mostra a porcentagem de e-mails recebidos (para o Gmail) que passaram pelo TLS em relação a todos os e-mails recebidos desse domínio. |
| TLS de saída | Mostra a porcentagem de e-mails enviados (do Gmail) aceitos por TLS em relação a todos os e-mails enviados para esse domínio. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para obter mais ideias sobre como melhorar a capacidade de entrega, leia [Armadilhas da capacidade de entrega e armadilhas de spam]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/deliverability_pitfalls_and_spam_traps/#deliverability-pitfalls-and-spam-traps). Não deixe de consultar nossas [práticas recomendadas de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/) para saber o que você deve verificar antes de enviar uma campanha de e-mail.

## Configuração do Microsoft Smart Network Data Services (SNDS)

Se a Microsoft for seu principal provedor de caixa de correio, você poderá usar essa integração para acessar e visualizar seus dados de reputação da Microsoft. Dessa forma, você pode monitorar a integridade de seus IPs para ajudar a determinar como seus e-mails estão sendo recebidos.

{% alert important %}
Se não vir seus dados no Deliverability Center, entre em contato com [o Suporte]({{site.baseurl}}/user_guide/administrative/access_braze/support/) com uma lista dos seus endereços IP.
{% endalert %}

\![Um exemplo de resultados do Microsoft SNDS, incluindo IPs de amostra, destinatários, comandos RCPT, comandos de dados, resultado de filtro, taxa de reclamação, início e fim do período de mensagem de interceptação e ocorrências de interceptação de spam.]({% image_buster /assets/img_archive/deliverability_center_msnds.png %})

### Métricas e definições

As métricas a seguir se aplicam ao Microsoft SNDS.

#### Beneficiários

Essa métrica refere-se ao número de destinatários das mensagens transmitidas pelo IP.

#### Comandos DATA

Essa métrica rastreia o número de comandos DATA enviados pelo IP. Os comandos DATA fazem parte do protocolo SMTP usado para enviar e-mails.

#### Filtrar resultados

Consulte esta tabela para entender os resultados do filtro 

| Resultado | Definição |
| ----- | ---------- |
| Verde | Considerado spam pelo filtro de spam da Microsoft em até 10% do período de tempo determinado. |
| Amarelo | Julgado como spam pelo filtro de spam da Microsoft entre 10% e 90% do período de tempo determinado. |
| Vermelho | Considerado spam pelo filtro de spam da Microsoft em até mais de 90% do período de tempo determinado.| 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Taxa de reclamação

Essa é a fração do tempo em que uma mensagem recebida do IP é reclamada por um usuário do Hotmail ou do Windows Live durante o período de atividade. Os usuários têm a opção de denunciar quase todas as mensagens como lixo eletrônico por meio da interface de usuário da Web. 

Para calcular a taxa de reclamações, divida o número de reclamações pelo número de destinatários da mensagem.  

| Resultado | Definição |
| ----- | ---------- |
| Menos de 0,3% | A taxa de reclamação ideal. |
| Mais de 0,3% | Revise seu processo de inscrição e verifique se o link de cancelamento de inscrição está funcionando. Além disso, considere se a correspondência poderia ser mais bem personalizada para seu público. |
| Mais de 100% | Observe que o SNDS exibe as reclamações para o dia em que foram relatadas, e não retroativamente em relação ao dia em que a correspondência reclamada foi entregue. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### A armadilha de spam atinge

As ocorrências de spam trap são o número de mensagens enviadas para "contas trap", que são contas mantidas por Outlook.com que não solicitam nenhum e-mail. É provável que todas as mensagens enviadas para essas contas de interceptação sejam consideradas spam, portanto, é importante monitorar essa métrica para garantir que ela seja baixa. O baixo número de ocorrências de armadilhas de spam significa que as mensagens não são enviadas para essas contas e, em vez disso, estão sendo enviadas para contas reais.

{% alert tip %}
Se você estiver procurando registros relacionados a um dos seus domínios verificados no Braze, observe que o Deliverability Center lista seus dados do Google Postmaster ou do Microsoft SNDS, o que significa que é provável que nenhuma das plataformas tenha dados para compartilhar com o Braze. Como alternativa, sugerimos manter uma entrega consistente de e-mails, pois isso pode levar a uma reputação mais alta.
{% endalert %}


