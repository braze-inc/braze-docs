---
nav_title: Solução de problemas
article_title: Segmentos de solução de problemas
page_order: 12
page_type: reference
tool: 
  - Segments
description: "Este artigo de referência aborda as etapas de solução de problemas e as considerações que devem ser levadas em conta ao usar segmentos."
---

# Segmentos de solução de problemas

## Comportamento do usuário

### O usuário não está mais em um segmento

Se um usuário não estiver disponível durante a criação de um segmento, os dados de usuários que determinam a elegibilidade do segmento poderão ter sido alterados como resultado de sua própria atividade ou de outras campanhas e Canvases com os quais ele interagiu anteriormente. Se a reelegibilidade estiver ativada, o perfil do usuário mostrará os dados mais recentes da campanha recebida.

### As informações são exibidas para usuários de outros aplicativos quando eu filtro para um aplicativo específico

Os usuários podem ter vários aplicativos, portanto, a seleção de um aplicativo específico na seção **Aplicativos usados** da página de segmentação produzirá resultados para os usuários que têm pelo menos esse aplicativo. O filtro não produz resultados para os usuários que têm exclusivamente esse app.

## Análise de dados e relatórios

### *A mensagem enviada* ou *os destinatários únicos* na análise de dados da campanha não correspondem à contagem do segmento 

Se a contagem da análise de *dados* da sua campanha de *Mensagens enviadas* ou *Destinatários únicos* não corresponder ao número de usuários no filtro de segmento `Has received message from campaign X`, pode haver dois motivos possíveis para isso:

1. **Os usuários podem ter sido arquivados, tornados órfãos ou excluídos desde o lançamento da campanha**<br><br>Por exemplo, digamos que 1.000 usuários recebam uma campanha e você faça uma exportação CSV no mesmo dia. Você verá 1.000 usuários relatados. No mês seguinte, 50 desses 1.000 usuários são excluídos (por exemplo, pelo endpoint `users/delete`). Quando fizer outra exportação CSV, verá 950 usuários relatados, enquanto a contagem de *Unique Recipient (destinatário único* ) no **Campaign Analytics** ainda é de 1.000.<br><br>Em outras palavras, a métrica *Unique Recipients* é uma contagem incrementada, enquanto o segmentador e a exportação CSV fornecem uma contagem de usuários existentes no momento.<br><br>

2. **A campanha tem a reelegibilidade definida, de modo que os usuários podem entrar novamente na campanha várias vezes**<br><br>Por exemplo, digamos que uma campanha de e-mail tenha a reelegibilidade definida como zero minutos (os usuários podem entrar novamente na campanha desde que atendam aos requisitos do segmento de público) e a campanha esteja em execução há mais de um mês. O número de *mensagens enviadas* no **Campaign Analytics** não corresponderia ao número no segmento porque esse campo incluiria mensagens enviadas a usuários duplicados.<br><br>Isso ocorre porque o Braze conta os usuários únicos como *Unique Daily Recipients*, ou o número de usuários que receberam uma determinada mensagem em um dia. Isso significa que os usuários reelegíveis serão contados mais de uma vez como um destinatário único, porque a janela "única" dura apenas um dia. Isso pode fazer com que o número de *destinatários diários exclusivos* seja maior do que o número de perfis de usuário na exportação CSV. Os perfis de usuário no arquivo CSV serão realmente exclusivos.