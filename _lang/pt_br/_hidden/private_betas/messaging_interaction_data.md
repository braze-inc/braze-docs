---
nav_title: "Dados de interação de envio de mensagens"
article_title: "Dados de interação de envio de mensagens"
permalink: "/messaging_interaction_data/"
hidden: true
---

# Sobre a disponibilidade de dados de interação de envio de mensagens

> Este artigo aborda informações sobre dados de interação da campanha e do Canva e sua disponibilidade.

### O que são dados de interação de envio de mensagens?

Os dados de interação de mensagens referem-se a como um usuário interage com uma campanha ou com a variante de campanha que recebeu (por exemplo, quando um usuário abre a campanha A ou recebe a variante A). Esses dados são usados para redirecionamento.

{% alert important %}
A partir do início de 2024, os dados de interação de envio de mensagens estarão disponíveis de acordo com o processo descrito aqui.
{% endalert %}

### Quando os dados de interação de envio de mensagens estarão disponíveis?

Os dados de interação estão sempre disponíveis. Para campanhas ativas e Canvas, os dados de interação estão sempre disponíveis em tempo real. 

Para campanhas interrompidas e Canvas, seus dados de interação expiram após três meses, a menos que sejam usados em filtros de redirecionamento por campanhas ativas ou Canvas. Os dados de interação expirados são movidos para o armazenamento de longo prazo e não estão disponíveis para uso, a menos que sejam restaurados usando o processo descrito abaixo.

Os dados de interação expirados nunca são excluídos e podem ser restaurados a qualquer momento.

#### Recursos que usam dados de interação

Os seguintes recursos usam dados de interação de envio de mensagens:

- Filtros que redirecionam em uma campanha ou canva específico
    - Alias clicado na campanha
    - Alias clicado na etapa do canva
    - Campanha clicada/aberta
    - Clicou/abriu uma etapa
    - Convertidos de uma campanha
    - Convertidos de um canva
    - Entrou na variação do canva
    - No grupo de controle da campanha
    - No grupo de controle do canva
    - Última mensagem recebida de uma campanha específica
    - Última mensagem recebida de uma etapa de canva específica
    - Recebeu variante de campanha
    - Recebeu mensagem de campanha
    - Recebeu mensagem de uma etapa de um canva
- Filtros que redirecionam em campanhas ou canvas de uma determinada tag
    - Recebeu mensagem de campanha ou canva com tag
    - Campanhas ou canvas clicados/abertos com tag
    - Recebeu mensagem de campanha ou canva com tag pela última vez
- Listas de **campanhas recebidas** e **envios de mensagens do Canva recebidas** no perfil do usuário
- Endpoint `/users/export`
- Exportações de CSV de **dados de usuários** nas páginas de resumo da campanha e do Canva

Esses recursos não incluirão dados de interação expirados em seus resultados. Para incluir dados de interação expirados nos resultados desses recursos, restaure a campanha ou o Canva com dados expirados.

#### Recursos que não usam dados de interação

Os recursos a seguir **não** usam dados de interação de mensagens, o que significa que não são afetados pela expiração dos dados de interação de mensagens:

- Configuração da campanha e do Canva
- Análise de dados da campanha e do Canva
- Relatórios de análise de dados (como o Criador de relatórios, o Criador de consultas e os Relatórios de engajamento)
- Currents
- Compartilhamento de dados do Snowflake
- Extensões de segmento
- Pontos de dados
- Os seguintes filtros de redirecionamento:
    - Alias clicado em qualquer etapa da campanha ou do canva
    - Feature Flags
    - Hard bounce
    - Marcou sua mensagem como spam
    - Nunca recebeu mensagem de campanha ou etapa do canva
    - Número de telefone inválido
    - Última interação com mensagem
    - Ultima inscrição em qualquer grupo de controle
    - Última impressão da mensagem no app
    - Último recebimento de qualquer mensagem
    - Último recebimento de e-mail 
    - Último push recebido
    - Último SMS recebido
    - Último webhook recebido
    - Último recebimento por WhatsApp
    - Última categoria de palavra-chave de SMS de inbound específica enviada
    - Última visualização do feed de notícias
    - Contagem de visualizações do feed de notícias

### Como faço para restaurar os dados de interação de envio de mensagens?

Para restaurar seus dados de interação, siga estas etapas:

1. Acesse a campanha expirada ou o Canva.
2. Na parte superior da campanha ou da landing page do Canva, clique em **Restaurar dados de interação** no banner.

![][1]

Você também pode restaurar os dados de interação de várias campanhas na página Campanhas, selecionando as campanhas e clicando no botão Restaurar dados de interação.

O tempo de restauração dos dados de interação varia, mas, na maioria dos casos, esse processo pode variar de 5 a 15 minutos. Você receberá um e-mail após a conclusão da restauração.

#### Restauração por tag

Você também pode restaurar os dados de interação de campanhas expiradas ou Canvas com uma determinada tag.

1. Acesse a página **Campanhas** ou **Canvas** e pesquise pela tag relevante.
2. Selecione suas campanhas ou telas.
3. Selecione **Restaurar dados de interação** para restaurar os dados dessas campanhas ou Canvas.

Após mais três meses de inatividade, essas campanhas ou Canvas expirarão novamente.

#### Redirecionamento por tag

As campanhas que usam filtros de redirecionamento que estão redirecionando por tag não estão isentas da expiração. Os filtros de redirecionamento que estão redirecionando por tag incluem:

- Recebeu mensagem de campanha ou canva com tag
- Campanhas ou canvas clicados/abertos com tag
- Recebeu mensagem de campanha ou canva com tag pela última vez

### Quando os dados de interação de envio de mensagens estavam disponíveis no passado?

Anteriormente, os dados de interação de mensagens eram excluídos quando uma campanha ou o canva:
- Não havia enviado mensagens em 25 meses corridos, E
- Não foi usado para redirecionamento em nenhuma campanha ativa, Canvas ou cartões de conteúdo.

Campanhas e Canvas com dados de interação de envio de mensagens excluídos anteriormente não podem ser usados em filtros de redirecionamento para campanhas, Canvases e segmentos.

[1]: {% image_buster /assets/img/restore_interaction_data.png %}
