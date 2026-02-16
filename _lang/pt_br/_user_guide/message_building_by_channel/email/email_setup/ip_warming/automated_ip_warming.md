---
nav_title: Aquecimento de IP automatizado
article_title: Aquecimento de IP automatizado
page_order: 1
page_type: reference
description: "Este artigo de referência aborda o aquecimento de IP automatizado e como monitorar seu aquecimento de IP."
channel: email
---

# Aquecimento de IP automatizado

> Use o aquecimento de IP automatizado para aumentar gradualmente o volume de e-mails a partir de um novo endereço IP para construir a reputação do remetente com os provedores de caixa de entrada.

{% include early_access_beta_alert.md feature='Automated IP warming' %}

## Como funciona?

Você pode usar o aquecimento de IP automatizado para aumentar gradualmente seu volume de envio diário, permitindo que os provedores de caixa de entrada aprendam e confiem em seus padrões de envio. Quando você adiciona um domínio ao seu espaço de trabalho, pode selecionar o bloco **Aquecimento de IP automatizado** na seção **Continuar de onde parou** do seu dashboard inicial, e esse bloco permanece aqui por 60 dias.

O Braze envia primeiro para seus assinantes mais engajados, o que permite que o volume diário cresça em um ritmo que corresponda às práticas recomendadas. Em seguida, o Braze rastreia os sinais de engajamento e entregabilidade. Se o Braze detectar algum problema, o sistema ajustará sua programação automaticamente.

{% alert note %}
Você pode realizar apenas um aquecimento de IP.
{% endalert %}

## Pré-requisitos

Para realizar o aquecimento de IP automatizado, você deve ter o seguinte:

- Subdomínio verificado e endereços IP ativos
- Permissões para visualizar e iniciar um aquecimento de IP
    - "View Usage Data" (Exibir dados de uso) para exibir a seção de aquecimento de IP
    - "View Email Templates" (Exibir modelos de e-mail) para visualizar e selecionar os modelos de e-mail para aquecimento de IP
    - "Manage Email Settings" (Gerenciar configurações de e-mail) para iniciar o aquecimento de IP
- "Campanhas de acesso" 
- "Aprovar e recusar campanhas" se o fluxo de trabalho de aprovação de campanhas estiver ativado 
    - A Braze aprova automaticamente as campanhas criadas a partir do aquecimento de IP automatizado em seu nome.

## Configure um plano de aquecimento de IP automatizado

### Etapa 1: Definir uma programação

1. Na seção **Informações de envio**, selecione o **endereço From (De)** para aquecer os endereços IP.
2. Insira o volume de envio diário atual e o volume de envio de direcionamento.
3. Selecione a data de início do aquecimento de IP automatizado. Essa data deve ser de pelo menos um dia após o lançamento do plano.
4. Digite o tempo de envio. Isso envia as mensagens no fuso horário da empresa.
5. Selecione **Next: Segmentos** para continuar a configuração.

![Exemplo de detalhes da programação.]({% image_buster /assets/img/automated_ip_warming_schedule.png %})

### Etapa 2: Selecionar e classificar segmentos

1. Em seguida, selecione os segmentos a serem direcionados. Durante o aquecimento de IP, o Braze começa a enviar para seus usuários com maior engajamento e aumenta gradualmente o volume de envio ao longo do tempo, acrescentando lentamente segmentos com menos engajamento. 
2. Em seguida, arraste e solte os segmentos para classificá-los de alto a baixo engajamento. O alto engajamento inclui destinatários que abrem e clicam consistentemente em seus e-mails. O baixo engajamento inclui destinatários que são inconsistentes no envolvimento com seus e-mails ou que não se envolvem com seus e-mails há muito tempo.
3. Selecione **Next: Mensagens** para continuar a configuração.

![Dois segmentos selecionados para direcionamento ao aquecimento de IP automatizado.]({% image_buster /assets/img/automated_ip_warming_segment.png %})

### Etapa 3: Selecione as mensagens a serem enviadas

1. Selecione **Selecionar modelos de e-mail**.
2. Escolha os modelos de e-mail para as mensagens a serem enviadas. O conteúdo que você envia durante o aquecimento de IP deve incentivar aberturas e cliques. Recomendamos escolher conteúdo que tenha tido boa recepção no passado. Por exemplo, você pode usar ofertas promocionais para incentivar o engajamento e as compras imediatas.
3. Selecione **Selecionar modelos**. O Braze calcula o número de modelos necessários antes que você possa iniciar. Recomendamos fornecer mais modelos do que o mínimo necessário para permitir que o sistema se ajuste aos problemas de entregabilidade sem parar.
4. Depois de adicionar o número necessário de modelos, selecione **Next: Resumo**.

{% alert important %}
As alterações feitas nas campanhas criadas a partir da ferramenta de aquecimento de IP (como alterar a data programada, o segmento, o volume) não serão refletidas na página **Resumo do** aquecimento de IP.
{% endalert %}

### Etapa 4: Revisão e lançamento

Revise os detalhes de seu plano de aquecimento de IP. Em seguida, selecione **Launch**.

## Durante o aquecimento de IP ativo

As campanhas de aquecimento de IP são criadas com 1 a 2 dias de antecedência, a menos que você esteja lançando um aquecimento de IP no dia seguinte. Essas campanhas são nomeadas automaticamente com o seguinte formato: `IP Warming Day [X] - [Date] - [Template Name]`.

Quando a meta de envio diário direcionada é atingida, o sistema interrompe o envio naquele dia para proteger sua reputação. 

O sistema monitora sua integridade com base nos seguintes padrões de referência do setor: 

- A taxa de entrega cai para menos ou igual a 90%
- Taxa de abertura inferior a 10%
- Bounces superiores a 5%
- Taxas de reclamação de spam superiores a 0,1%

Se as estatísticas estiverem abaixo de nossos padrões de referência, o sistema retém o volume no dia seguinte, em vez de aumentá-lo, para reduzir o risco à reputação de seu remetente.

## Interromper um plano de aquecimento de IP

O Braze permite que você interrompa o aquecimento de IP e a criação de campanhas futuras, mas se uma campanha já estiver ativa ou programada para as próximas 24 a 48 horas, talvez seja necessário interromper a campanha específica manualmente. A interrupção de um plano de aquecimento de IP também interrompe todas as campanhas associadas.

No entanto, quando interrompido, o aquecimento do IP não pode ser retomado. Em vez disso, você deve definir um novo plano para continuar de onde parou:

- Baixe os dados existentes do seu plano de parada para mantê-los em seu registro, pois assim que iniciar um novo aquecimento de IP, o rastreador anterior será removido
- **Atualizando** o **volume de envio diário atual** para o volume mais recente
- Adicionar um filtro a um segmento se você planeja usar o mesmo segmento do último aquecimento de IP, excluindo usuários que já receberam campanhas anteriores

## Quando um aquecimento de IP é concluído

O aquecimento de IP é marcado como concluído quando o último dia de aquecimento de IP termina à meia-noite no fuso horário de sua empresa. Por exemplo, se a última campanha enviada no plano de aquecimento de IP for enviada às 20 horas, o plano será marcado como concluído após quatro horas.

O rastreador permanece na página inicial por 90 dias após o término do plano. Após 90 dias, o rastreador é removido. O download dos dados inclui essas métricas padrão de e-mail:

- _Envios_	
- _Entregue_	
- _Bounces_	
- _Relatórios de spam_	
- _Total de aberturas_	
- _Aberturas exclusivas_	
- _Clicado_	
- _Cancelou inscrição_

Se um dia incluir várias campanhas usadas para atender aos requisitos de volume, elas serão agregadas na exibição diária.

![Rastreador de aquecimento de IP com volume de envio para a semana de 16 de janeiro.]({% image_buster /assets/img/automated_ip_warming_example.png %})