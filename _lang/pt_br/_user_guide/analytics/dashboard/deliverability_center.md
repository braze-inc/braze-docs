---
nav_title: Centro de entregabilidade
article_title: Centro de entregabilidade
page_order: 4
description: "Este artigo de referência cobre como configurar o Centro de Entregabilidade, um recurso que permite aos profissionais de marketing visualizar seus domínios de envio de e-mail e reputações de IP e entender sua entregabilidade de e-mail."
channel:
  - email

---

# Centro de entregabilidade

> O Centro de Entregabilidade fornece mais insight sobre a performance do seu e-mail, apoiando o uso de [Gmail Postmaster Tools](https://www.gmail.com/postmaster/) para rastrear dados sobre e-mails enviados e coletar dados sobre seu domínio de envio.

A entregabilidade de e-mail é o cerne do sucesso da campanha. Usando o Centro de Entregabilidade no dashboard do Braze, você pode visualizar seus domínios por **Reputação de IP** ou **Erros de Entrega** para descobrir e solucionar quaisquer problemas potenciais com a entregabilidade de e-mail. 

Para acessar o Centro de Entregabilidade, você precisará de [permissões de usuário]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) "Acessar Campanhas, Canvas, Cartões, Segmentos, Biblioteca de Mídia" e "Ver Dados de Uso".

## Configuração de sua conta do Google Postmaster

Antes de se conectar ao Centro de Entregabilidade, você precisará configurar uma conta no Google Postmaster Tools. Você pode usar uma conta do Gmail de trabalho ou pessoal para configurar seu Google Postmaster. 

1. Acessar o [dashboard do Google Postmaster Tools](https://postmaster.google.com/managedomains?pli=1).
2. No canto inferior direito, selecione o ícone de <i class="fas fa-plus-circle"></i> mais.
3. Digite seu domínio raiz ou subdomínio para autenticar seu e-mail. Se você estiver adicionando e verificando o domínio raiz, isso permitirá que a verificação seja aplicada a jusante aos subdomínios. Por exemplo, ao verificar `braze.com`, você pode adicionar posteriormente `demo.braze.com` e outros subdomínios sem precisar verificá-los individualmente.
4. O Google gerará um registro TXT que pode ser adicionado diretamente ao DNS do seu domínio. Isso é geralmente de propriedade de quem gerencia seu DNS. Para obter informações e orientações sobre como atualizar seu DNS específico, confira [Verificar seu domínio (etapas específicas do host)](https://support.google.com/a/topic/1409901).
5. Selecione **Próximo**. <br>![Um domínio de exemplo "demo.braze.com" para autenticar um e-mail.]({% image_buster /assets/img_archive/domain_authentication.png %})
6. Depois que o registro TXT for adicionado ao DNS, volte para o dashboard do Google Postmaster Tools e selecione **Verificar**. Esta etapa confirma que você possui o domínio, para que você possa acessar as métricas de entregabilidade do Gmail na sua conta do Postmaster. <br> ![Um prompt para verificar a propriedade do domínio "demo.braze.com".]({% image_buster /assets/img_archive/domain_verification.png %})

{% alert tip %}
Certifique-se de que o registro TXT esteja vinculado ao domínio pai, não ao subdomínio que você está usando através do Braze.
{% endalert %}

{% alert note %}
Se seus subdomínios não estiverem incluídos no Centro de Entregabilidade do Google Postmaster, isso pode ser resultado de adicionar apenas o domínio pai ao Google Postmaster. Depois que os domínios principais forem verificados no Google Postmaster, você poderá adicionar seus subdomínios, que serão verificados automaticamente. Esse processo permite que o Google reporte métricas no nível do subdomínio, que podem então ser puxadas para o Centro de Entregabilidade da Braze.
{% endalert %}

## Integração do Google Postmaster

Antes de configurar seu Centro de Entregabilidade, verifique se seus domínios foram [adicionados às Ferramentas do Postmaster do Gmail](https://support.google.com/mail/answer/9981691?hl=en).

Siga estas etapas para integrar com o Google Postmaster e configurar seu Centro de Entregabilidade:

1. Acessar **análise de dados** > **performance de e-mail**.
2. Selecione a guia **Centro de Entregabilidade**. <br>![Um Centro de Entregabilidade com o Google Postmaster desconectado.]({% image_buster /assets/img_archive/deliverability_center1.png %})
3. Selecione **Conectar com o Google Postmaster**. 
4. Selecione sua Conta do Google e, em seguida, selecione **Permitir** para permitir que o Braze visualize as métricas de tráfego de e-mail para os domínios registrados nas Ferramentas do Google Postmaster. 

Seus domínios verificados serão exibidos no Centro de entregabilidade. 

![Dois domínios verificados para o Google Postmaster com uma reputação média e baixa.]({% image_buster /assets/img_archive/deliverability_center2.png %})

Você também pode acessar o Google Postmaster no dashboard do Braze acessando **Partner Integrations** > **Technology Partners** > **Google Postmaster**. Após a integração, a Braze coleta dados de reputação e erros dos últimos 30 dias. Os dados podem não estar imediatamente disponíveis e podem levar vários minutos para serem preenchidos.

### Métricas e definições

As seguintes métricas e definições se aplicam às Ferramentas do Google Postmaster.

#### Reputação de IP 

Para ajudar a entender as classificações de reputação de IP, consulte esta tabela:

| Classificação de Reputação | Definição |
| ----- | ---------- |
| Alta | Tem um bom histórico de gerar poucas reclamações de spam (como usuários clicando no botão "spam"). |
| Médio/Justo | Conhecido por gerar engajamento positivo, mas ocasionalmente recebe reclamações de spam. A maioria dos e-mails deste domínio será enviada para a caixa de entrada, exceto quando as reclamações de spam aumentarem. |
| Baixa | Conhecido por receber taxas elevadas de reclamações de spam regularmente. Emails deste remetente provavelmente serão filtrados para a pasta de spam. |
| Ruim | Tem um histórico de receber taxas elevadas de reclamações de spam. Emails deste domínio quase sempre serão rejeitados no momento da conexão ou filtrados para a pasta de spam. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Reputação de domínio 

Use a tabela a seguir para ajudar a monitorar e entender suas classificações de reputação de domínio para evitar ser filtrado em uma pasta de spam.

| Classificação de Reputação | Definição |
| ----- | ---------- |
| Alta | Tem um bom histórico de muito poucas reclamações de spam. Está em conformidade com as diretrizes do remetente do Gmail. Emails raramente são filtrados para a pasta de spam. Tem um bom histórico de uma taxa de spam muito baixa. Está em conformidade com [as diretrizes de remetente do Gmail](https://developers.google.com/gmail/markup/registering-with-google). |
| Médio/Justo | Conhecido por gerar {engajamento} positivo, mas ocasionalmente recebeu um baixo volume de reclamações de spam. A maioria dos e-mails deste domínio chegará à caixa de entrada (exceto quando houver um aumento notável nos níveis de spam). |
| Baixa | Conhecido por receber reclamações de spam regularmente. Emails deste remetente provavelmente serão filtrados para a pasta de spam. |
| Ruim | Tem um histórico de receber taxas elevadas de reclamações de spam. Emails deste domínio quase sempre serão rejeitados no momento da conexão ou filtrados para a pasta de spam. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Autenticação

Use o dashboard de autenticação para analisar a porcentagem de e-mails que foram aprovados no Sender Policy Framework (SPF), no DomainKeys Identified Mail (DKIM) e no Domain-based Message Authentication, Reporting and Conformance (DMARC).

| Tipo de Gráfico | Definição |
| ----- | ---------- |
| FPS | Mostra a porcentagem de e-mails que passaram no SPF em relação a todos os e-mails do domínio que tentaram o SPF. Isso exclui qualquer e-mail falsificado. |
| DKIM | Mostra a porcentagem de e-mails que passaram no DKIM em relação a todos os e-mails do domínio que tentaram o DKIM. |
| DMARC | Mostra a porcentagem de e-mails que passaram no alinhamento DMARC em relação a todos os e-mails recebidos do domínio que passaram no SPF ou DKIM. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Criptografia

Consulte esta tabela para entender qual porcentagem do seu tráfego de entrada e saída está criptografado.

| Prazo | Definição |
| ----- | ---------- |
| TLS Inbound | Mostra a porcentagem de e-mails recebidos (para o Gmail) que passaram pelo TLS em comparação com todos os e-mails recebidos desse domínio. |
| TLS Saída | Mostra a porcentagem de e-mails enviados (do Gmail) aceitos via TLS em comparação com todos os e-mails enviados para esse domínio. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para mais ideias sobre como melhorar a entregabilidade, leia [armadilhas de entregabilidade e armadilhas de spam]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/deliverability_pitfalls_and_spam_traps/#deliverability-pitfalls-and-spam-traps). Certifique-se de consultar nossas [Melhores práticas de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/) para coisas que você deve verificar antes de enviar uma campanha de e-mail.

## Configuração do Microsoft Smart Network Data Services (SNDS)

Se a Microsoft for seu principal provedor de caixa de e-mail, você pode usar esta integração para acessar e visualizar seus dados de reputação da Microsoft. Dessa forma, você pode monitorar a integridade de seus IPs para ajudar a determinar como seus e-mails estão sendo recebidos.

{% alert important %}
Se você não vir seus dados no Centro de Entregabilidade, entre em contato com [Suporte]({{site.baseurl}}/user_guide/administrative/access_braze/support/) com uma lista de seus endereços IP.
{% endalert %}

![Um exemplo de resultados do Microsoft SNDS, incluindo IPs de amostra, destinatários, comandos RCPT, comandos de dados, resultado do filtro, taxa de reclamação, período de início e fim da mensagem de armadilha e hits de armadilha de spam.]({% image_buster /assets/img_archive/deliverability_center_msnds.png %})

### Métricas e definições

As seguintes métricas se aplicam ao Microsoft SNDS.

#### Destinatários

Esta métrica refere-se ao número de destinatários em mensagens transmitidas pelo IP.

#### comandos de DADOS

Esta métrica rastreia o número de comandos DATA enviados pelo IP. Os comandos DATA fazem parte do protocolo SMTP usado para enviar e-mails.

#### Filtrar resultados

Consulte esta tabela para entender os resultados do filtro 

| Resultado | Definição |
| ----- | ---------- |
| Verde | Julgado como spam pelo filtro de spam da Microsoft em até 10% do período de tempo fornecido. |
| Amarelo | Julgado como spam pelo filtro de spam da Microsoft entre 10% e 90% do período de tempo dado. |
| Vermelho | Julgado como spam pelo filtro de spam da Microsoft em mais de 90% do período de tempo dado.| 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Taxa de reclamação

A fração do tempo que leva para uma mensagem recebida deste IP receber uma reclamação de um usuário do Hotmail ou do Windows Live durante o período de atividade. Os usuários têm a opção de relatar quase todas as mensagens como lixo através da interface web do usuário. 

Para calcular a taxa de reclamações, divida o número de reclamações pelo número de destinatários da mensagem.  

| Resultado | Definição |
| ----- | ---------- |
| Menos de 0,3% | A taxa de reclamação ideal. |
| Mais de 0,3% | Revise seu processo de inscrição e certifique-se de que seu link de cancelamento de inscrição está funcionando. Além disso, considere se o correio poderia ser melhor personalizado para seu público. |
| Mais de 100% | Observe que o SNDS exibe reclamações para o dia em que foram relatadas, não retroativamente contra o dia em que o e-mail reclamado foi entregue. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Hits de spam trap

Os acertos de armadilhas de spam são o número de mensagens enviadas para "contas de armadilha", que são contas mantidas por Outlook.com que não solicitam nenhum e-mail. É provável que quaisquer mensagens enviadas para essas contas de armadilha sejam consideradas spam, portanto, é importante monitorar essa métrica para garantir que esteja baixa. Baixos hits de armadilha de spam significam que as mensagens não estão sendo enviadas para essas contas e estão sendo enviadas para contas reais em vez disso.

{% alert tip %}
Se você está procurando por registros relacionados a um dos seus domínios verificados no Braze, note que o Centro de Entregabilidade lista seus dados do Google Postmaster ou Microsoft SNDS, o que significa que é provável que qualquer uma das plataformas não tenha dados para compartilhar com o Braze. Alternativamente, sugerimos manter a entrega consistente de e-mails, pois isso pode levar a uma reputação mais alta.
{% endalert %}


