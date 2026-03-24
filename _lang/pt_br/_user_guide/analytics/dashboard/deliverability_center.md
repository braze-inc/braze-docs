---
nav_title: Centro de entregabilidade
article_title: Centro de entregabilidade
alias: "/deliverability_center/"
page_order: 4
description: "Este artigo de referência cobre como configurar o Centro de Entregabilidade, um recurso que permite aos profissionais de marketing visualizar seus domínios de envio de e-mail e reputações de IP e entender sua entregabilidade de e-mail."
channel:
  - email

---

# Centro de entregabilidade

> O Centro de Entregabilidade fornece mais insight sobre a performance do seu e-mail, apoiando o uso do [Gmail Postmaster Tools](https://www.gmail.com/postmaster/) para rastrear dados sobre e-mails enviados e coletar dados sobre seu domínio de envio.

A entregabilidade de e-mail é o cerne do sucesso da campanha. Usando o Centro de Entregabilidade no dashboard da Braze, você pode visualizar seus domínios por **Reputação de IP** ou **Erros de Entrega** para descobrir e solucionar quaisquer problemas potenciais com a entregabilidade de e-mail. 

Para acessar o Centro de Entregabilidade, você precisa das permissões "Acessar Campanhas, Canvas, Cartões, Segmentos, Biblioteca de Mídia" e "Ver Dados de Uso" [permissões de usuário legadas]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions) ou as [permissões granulares]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions) no seguinte menu suspenso para o seu espaço de trabalho.

{% details Permissões de usuário para o Centro de Entregabilidade %}

{% multi_lang_include deprecations/user_permissions.md %}

- Ver campanhas
- Editar campanhas
- Arquivar campanhas
- Ver canvas
- Editar canvas
- Arquivar canvas
- Ver regras de limite de frequência
- Editar regras de limite de frequência
- Ver priorização de mensagens
- Editar priorização de mensagens
- Ver blocos de conteúdo
- Ver Feature Flags
- Editar Feature Flags
- Arquivar Feature Flags
- Ver segmentos
- Editar segmentos
- Ver modelos de IAM
- Editar modelos de IAM
- Arquivar modelos de IAM
- Ver modelos de e-mail
- Editar modelos de e-mail
- Arquivar modelos de e-mail
- Ver modelos de webhook
- Editar modelos de webhook
- Arquivar modelos de webhook
- Ver modelos de links de e-mail
- Editar modelos de links de e-mail
- Ver ativos da biblioteca de mídia
- Editar ativos da biblioteca de mídia
- Excluir ativos da biblioteca de mídia
- Ver locais
- Editar locais
- Arquivar locais
- Ver códigos de promoção
- Editar códigos de promoção
- Exportar códigos de promoção
- Ver Centrais de Preferências
- Editar Centrais de Preferências
- Ver relatórios
- Editar relatórios
- Ver dados de uso

{% enddetails %}

## Configuração da sua conta do Google Postmaster

Antes de se conectar ao Centro de Entregabilidade, você precisará configurar uma conta no Google Postmaster Tools. Você pode usar uma conta do Gmail de trabalho ou pessoal para configurar seu Google Postmaster. 

1. Acesse o [dashboard do Google Postmaster Tools](https://postmaster.google.com/managedomains?pli=1).
2. No canto inferior direito, selecione o ícone de <i class="fas fa-plus-circle"></i> mais.
3. Digite seu domínio raiz (pai) para autenticar seu e-mail. Certifique-se de que o registro TXT esteja vinculado a esse domínio raiz (pai), **não** ao subdomínio que você está usando pela Braze. Verificar o domínio raiz (pai) permite que você adicione subdomínios posteriormente no Postmaster Tools sem criar registros TXT adicionais. Por exemplo, ao verificar `braze.com`, você pode adicionar `demo.braze.com` como um subdomínio separado no Postmaster Tools para ver métricas no nível do subdomínio.
4. O Google gera um registro TXT que pode ser adicionado diretamente ao DNS do seu domínio. Isso geralmente é gerenciado por quem administra seu DNS. Para obter informações e orientações sobre como atualizar seu DNS específico, confira [Verificar seu domínio (etapas específicas do host)](https://support.google.com/a/topic/1409901).
5. Selecione **Próximo**. <br>![Um domínio de exemplo "demo.braze.com" para autenticar um e-mail.]({% image_buster /assets/img_archive/domain_authentication.png %})
6. Depois que o registro TXT for adicionado ao DNS, volte para o dashboard do Google Postmaster Tools e selecione **Verificar**. Essa etapa confirma que você possui o domínio, para que você possa acessar as métricas de entregabilidade do Gmail na sua conta do Postmaster. <br> ![Um aviso para verificar a propriedade do domínio "demo.braze.com".]({% image_buster /assets/img_archive/domain_verification.png %})

{% alert note %}
Se seus subdomínios não estiverem incluídos no Centro de Entregabilidade do Google Postmaster, isso pode ser resultado de ter adicionado apenas o domínio raiz (pai) ao Google Postmaster. Depois que os domínios raiz forem verificados no Google Postmaster, você pode adicionar seus subdomínios, que são verificados automaticamente. Esse processo permite que o Google reporte métricas no nível do subdomínio, que podem então ser importadas para o Centro de Entregabilidade da Braze.
{% endalert %}

## Integração do Google Postmaster

Antes de configurar seu Centro de Entregabilidade, verifique se seus domínios foram [adicionados ao Gmail Postmaster Tools](https://support.google.com/mail/answer/9981691?hl=en).

Siga estas etapas para integrar com o Google Postmaster e configurar seu Centro de Entregabilidade:

1. Acesse **Análise de dados** > **Performance de e-mail**.
2. Selecione a guia **Centro de Entregabilidade**. <br>![Um Centro de Entregabilidade com Google Postmaster desconectado.]({% image_buster /assets/img_archive/deliverability_center1.png %})
3. Selecione **Conectar com o Google Postmaster**. 
4. Selecione sua Conta do Google e, em seguida, selecione **Permitir** para permitir que a Braze visualize as métricas de tráfego de e-mail para os domínios registrados no Postmaster Tools. 

Seus domínios verificados são exibidos no Centro de Entregabilidade. 

![Dois domínios verificados para Google Postmaster com reputação média e baixa.]({% image_buster /assets/img_archive/deliverability_center2.png %})

Você também pode acessar o Google Postmaster no dashboard da Braze acessando **Integrações com Parceiros** > **Parceiros de Tecnologia** > **Google Postmaster**. Após a integração, a Braze coleta dados de reputação e erros dos últimos 30 dias. Os dados podem não estar imediatamente disponíveis e podem levar vários minutos para serem preenchidos.

### Métricas e definições

As seguintes métricas e definições se aplicam ao Google Postmaster Tools.

#### Reputação de IP 

Para ajudar a entender as classificações de reputação de IP, consulte esta tabela:

| Classificação de reputação | Definição |
| ----- | ---------- |
| Alta | Tem um bom histórico de gerar poucas reclamações de spam (como usuários clicando no botão "spam"). |
| Média/Regular | Conhecido por gerar engajamento positivo, mas ocasionalmente recebe reclamações de spam. A maioria dos e-mails deste domínio é enviada para a caixa de entrada, exceto quando as reclamações de spam aumentam. |
| Baixa | Conhecido por receber taxas elevadas de reclamações de spam regularmente. E-mails deste remetente provavelmente serão filtrados para a pasta de spam. |
| Ruim | Tem um histórico de receber taxas elevadas de reclamações de spam. E-mails deste domínio quase sempre são rejeitados no momento da conexão ou filtrados para a pasta de spam. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Reputação de domínio 

Use a tabela a seguir para ajudar a monitorar e entender suas classificações de reputação de domínio e evitar ser filtrado para a pasta de spam.

| Classificação de reputação | Definição |
| ----- | ---------- |
| Alta | Tem um bom histórico de muito poucas reclamações de spam. Está em conformidade com as diretrizes de remetente do Gmail. E-mails raramente são filtrados para a pasta de spam. Tem um bom histórico de uma taxa de spam muito baixa. Está em conformidade com [as diretrizes de remetente do Gmail](https://developers.google.com/gmail/markup/registering-with-google). |
| Média/Regular | Conhecido por gerar engajamento positivo, mas ocasionalmente recebeu um baixo volume de reclamações de spam. A maioria dos e-mails deste domínio chega à caixa de entrada (exceto quando há um aumento notável nos níveis de spam). |
| Baixa | Conhecido por receber reclamações de spam regularmente. E-mails deste remetente provavelmente serão filtrados para a pasta de spam. |
| Ruim | Tem um histórico de receber taxas elevadas de reclamações de spam. E-mails deste domínio quase sempre são rejeitados no momento da conexão ou filtrados para a pasta de spam. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Autenticação

Use o dashboard de autenticação para analisar a porcentagem de e-mails que foram aprovados no Sender Policy Framework (SPF), no DomainKeys Identified Mail (DKIM) e no Domain-based Message Authentication, Reporting and Conformance (DMARC).

| Tipo de gráfico | Definição |
| ----- | ---------- |
| SPF | Mostra a porcentagem de e-mails que passaram no SPF em relação a todos os e-mails do domínio que tentaram o SPF. Isso exclui qualquer e-mail falsificado. |
| DKIM | Mostra a porcentagem de e-mails que passaram no DKIM em relação a todos os e-mails do domínio que tentaram o DKIM. |
| DMARC | Mostra a porcentagem de e-mails que passaram no alinhamento DMARC em relação a todos os e-mails recebidos do domínio que passaram no SPF ou DKIM. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Criptografia

Consulte esta tabela para entender qual porcentagem do seu tráfego de entrada e saída está criptografado.

| Termo | Definição |
| ----- | ---------- |
| TLS Inbound | Mostra a porcentagem de e-mails recebidos (para o Gmail) que passaram pelo TLS em comparação com todos os e-mails recebidos desse domínio. |
| TLS Outbound | Mostra a porcentagem de e-mails enviados (do Gmail) aceitos via TLS em comparação com todos os e-mails enviados para esse domínio. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para mais ideias sobre como melhorar a entregabilidade, leia [Armadilhas de entregabilidade e armadilhas de spam]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/deliverability_pitfalls_and_spam_traps/#deliverability-pitfalls-and-spam-traps). Não deixe de consultar nossas [Melhores práticas de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/) para conferir o que você deve verificar antes de enviar uma campanha de e-mail.

## Configuração do Microsoft Smart Network Data Services (SNDS)

Se a Microsoft for seu principal provedor de caixa de e-mail, você pode usar esta integração para acessar e visualizar seus dados de reputação da Microsoft. Dessa forma, você pode monitorar a integridade dos seus IPs para ajudar a determinar como seus e-mails estão sendo recebidos.

{% alert important %}
Se você não vir seus dados no Centro de Entregabilidade, entre em contato com o [Suporte]({{site.baseurl}}/user_guide/administrative/access_braze/support/) com uma lista dos seus endereços IP.
{% endalert %}

![Um exemplo de resultados do Microsoft SNDS, incluindo IPs de amostra, destinatários, comandos RCPT, comandos DATA, resultado do filtro, taxa de reclamação, período de início e fim da mensagem de armadilha e acertos de armadilha de spam.]({% image_buster /assets/img_archive/deliverability_center_msnds.png %})

### Métricas e definições

As seguintes métricas se aplicam ao Microsoft SNDS.

#### Destinatários

Esta métrica refere-se ao número de destinatários em mensagens transmitidas pelo IP.

#### Comandos DATA

Esta métrica rastreia o número de comandos DATA enviados pelo IP. Os comandos DATA fazem parte do protocolo SMTP usado para enviar e-mails.

#### Resultados do filtro

Consulte esta tabela para entender os resultados do filtro: 

| Resultado | Definição |
| ----- | ---------- |
| Verde | Julgado como spam pelo filtro de spam da Microsoft em até 10% do período de tempo fornecido. |
| Amarelo | Julgado como spam pelo filtro de spam da Microsoft entre 10% e 90% do período de tempo dado. |
| Vermelho | Julgado como spam pelo filtro de spam da Microsoft em mais de 90% do período de tempo dado.| 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Taxa de reclamação

É a fração do tempo em que uma mensagem recebida do IP recebe uma reclamação de um usuário do Hotmail ou do Windows Live durante o período de atividade. Os usuários têm a opção de relatar quase todas as mensagens como lixo pela interface web. 

Para calcular a taxa de reclamações, divida o número de reclamações pelo número de destinatários da mensagem.  

| Resultado | Definição |
| ----- | ---------- |
| Menos de 0,3% | A taxa de reclamação ideal. |
| Mais de 0,3% | Revise seu processo de inscrição e certifique-se de que seu link de cancelamento de inscrição está funcionando. Além disso, considere se o e-mail poderia ser melhor personalizado para o seu público. |
| Mais de 100% | Observe que o SNDS exibe reclamações para o dia em que foram relatadas, não retroativamente contra o dia em que o e-mail reclamado foi entregue. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Acertos de armadilha de spam

Os acertos de armadilha de spam são o número de mensagens enviadas para "contas de armadilha", que são contas mantidas pelo Outlook.com que não solicitam nenhum e-mail. É provável que quaisquer mensagens enviadas para essas contas de armadilha sejam consideradas spam, então é importante monitorar essa métrica para garantir que esteja baixa. Poucos acertos de armadilha de spam significam que as mensagens não estão sendo enviadas para essas contas e estão sendo enviadas para contas reais.

{% alert tip %}
Se você está procurando registros relacionados a um dos seus domínios verificados na Braze, note que o Centro de Entregabilidade lista seus dados do Google Postmaster ou Microsoft SNDS, o que significa que é provável que nenhuma das plataformas tenha dados para compartilhar com a Braze. Como alternativa, sugerimos manter a entrega consistente de e-mails, pois isso pode levar a uma reputação mais alta. 
{% endalert %}