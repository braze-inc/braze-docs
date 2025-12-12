{% if include.section == "Differing audience size" %}

O tamanho do público-alvo exibido em uma campanha ou Canvas pode ser diferente do [tamanho do público alcançável para um segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size#segment-membership-calculation), mesmo que você esteja adicionando diretamente esse segmento à sua campanha ou Canvas sem filtros adicionais.
Isso pode ocorrer por vários motivos:

- Quando um Grupo de Controle Global se aplica a uma campanha ou Canva, os usuários desse Grupo de Controle Global são excluídos da contagem de usuários acessíveis.
- O tamanho do público-alvo de uma campanha ou Canva exclui os usuários que não podem ser contatados por meio de vários canais de envio de mensagens; o comportamento difere de canal para canal. Por exemplo, o público-alvo de uma campanha ou Canva exclui os usuários que cancelaram a inscrição, foram marcados como spam (para e-mails) ou sofreram soft bounce (para e-mails). O segmento em si, no entanto, exclui apenas as aceitações ao mostrar o número estimado de usuários alcançáveis por e-mail. 
- O Braze só envia mensagens SMS para usuários dentro do grupo de inscrições selecionado, portanto, o público-alvo de SMS para uma campanha ou Canva também excluirá todos os usuários que não fizerem parte do grupo de inscrições selecionado.

{% endif %}

{% if include.section == "Refresh settings" %}

Se não precisar que sua extensão seja atualizada regularmente, você poderá salvá-la sem usar as configurações de atualização, e o Braze gerará sua extensão de segmento com base na associação do usuário naquele momento. Use o comportamento padrão se quiser gerar o público apenas uma vez e depois direcioná-lo com uma campanha única.

Seu segmento sempre começará a ser processado após o salvamento inicial. Sempre que seu segmento for atualizado, o Braze executará novamente o segmento e atualizará a associação do segmento para refletir os usuários em seu segmento no momento da atualização. Isso pode ajudar suas campanhas recorrentes a alcançar os usuários mais relevantes.

#### Configuração de uma atualização recorrente

Para definir uma agenda recorrente designando configurações de atualização, selecione **Ativar atualização**. A opção de designar configurações de atualização está disponível para todos os tipos de extensões de segmento, incluindo segmentos SQL, extensões de segmento CDI e extensões de segmento simples baseadas em formulário.

{% alert important %}
Para otimizar seu gerenciamento de dados, as configurações de atualização são automaticamente desativadas para extensões de segmento não utilizadas. As extensões de segmento são consideradas não utilizadas quando são:

- Não usado em nenhuma campanha, tela ou segmento ativo ou inativo (rascunho, interrompido, arquivado); ou
- Sem modificação há mais de 7 dias

O Braze notificará o contato da empresa e o criador da extensão se essa configuração estiver desativada. A opção de regenerar extensões diariamente pode ser ativada novamente a qualquer momento.
{% endalert %}

#### Seleção de suas configurações de atualização

![Configurações de intervalo de atualização com uma frequência de atualização semanal, horário de início às 10h e segunda-feira selecionada como dia.]({% image_buster /assets/img/segment/segment_interval_settings.png %}){: style="max-width:50%;"}

No painel **Refresh Interval Settings (Configurações de intervalo de atualização** ), você pode selecionar a frequência de atualização dessa extensão de segmento: por hora, diariamente, semanalmente ou mensalmente. Também será necessário selecionar o horário específico (que está no fuso horário da sua empresa) em que a atualização ocorrerá, como, por exemplo:

- Se você tiver uma campanha de envio de e-mail que é enviada todas as segundas-feiras às 11 horas, horário da empresa, e quiser garantir que seu segmento seja atualizado logo antes do envio, deverá escolher uma agenda de atualização semanal às 10 horas das segundas-feiras.
- Se quiser que seu segmento seja atualizado todos os dias, selecione a frequência de atualização diária e, em seguida, escolha a hora do dia para atualizar.

{% alert note %}
A capacidade de definir um cronograma de atualização por hora não está disponível para extensões de segmento baseadas em formulário (mas você pode definir cronogramas diários, semanais ou mensais).
{% endalert %}

#### Consumo de crédito e custos adicionais

Como as atualizações executam novamente a consulta do seu segmento, cada atualização para segmentos SQL consumirá créditos de segmento SQL e cada atualização para extensões de segmento CDI incorrerá em um custo em seu data warehouse de terceiros.

{% alert note %}
Os segmentos podem levar até 60 minutos para serem atualizados devido ao tempo de processamento dos dados. Os segmentos que estão atualmente em processo de atualização terão o status "Processing" (Processando) na lista de extensões de segmento. Isso tem algumas implicações:

- Para concluir o processamento de seu segmento antes de um horário específico, escolha um horário de atualização que seja 60 minutos antes. 
- Somente uma atualização pode ocorrer de cada vez em uma extensão de segmento específica. Se houver um conflito em que uma nova atualização seja iniciada quando uma atualização existente já tiver começado a ser processada, o Braze cancelará a nova solicitação de atualização e continuará o processamento em andamento.
{% endalert %}

#### Critérios para desativar automaticamente extensões obsoletas

As atualizações programadas são automaticamente desativadas quando uma extensão de segmento se torna obsoleta. Uma extensão de segmento estará obsoleta se atender aos seguintes critérios:

- Não usado em nenhuma campanha ou tela ativa
- Não usado em nenhum segmento que esteja em uma campanha ativa ou canva
- Não usado em nenhum segmento que tenha [o rastreamento de dados]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking#segment-analytics-tracking) ativado
- Não é modificado há mais de sete dias
- Não foi adicionado a uma campanha ou Canva (incluindo rascunhos) ou segmento há mais de sete dias

Se a atualização programada estiver desativada para uma extensão de segmento, essa extensão terá uma notificação informando isso.

![Uma notificação informando que "As atualizações programadas foram desativadas para essa extensão porque ela não é usada em nenhuma campanha, canvas ou segmento ativo. A extensão do segmento foi desativada em 23 de fevereiro de 2025 às 12:00 AM."]({% image_buster /assets/img/segment/segment_extension_disabled.png %})

Quando estiver pronto para usar uma extensão de segmento desatualizada, revise as configurações de atualização, selecione a programação de atualização que corresponda ao seu caso de uso e salve as modificações.

{% endif %}