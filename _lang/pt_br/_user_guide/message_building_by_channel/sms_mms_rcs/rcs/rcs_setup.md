---
nav_title: "Configuração do RCS"
article_title: Configuração do RCS
page_order: 1
alias: /rcs_setup/
description: "Este artigo de referência aborda os requisitos necessários para colocar o RCS em funcionamento."
page_type: reference
channel:
  - RCS
---

# Configuração do RCS

> Este artigo aborda os requisitos necessários para colocar seu canal RCS em funcionamento.

A configuração do RCS é tão simples quanto a configuração do SMS. Continue lendo para saber como você pode começar a enviar mensagens ricas e interativas.

## Etapa 1: Atender aos critérios de elegibilidade

Para se qualificar para o envio de RCS com o Braze, sua empresa deve atender a três critérios antecipadamente:

1. Seu contrato Braze atual deve incluir Créditos de Mensagens. 
2. Você deve enviar suas mensagens RCS para um dos seguintes países com suporte do Brasil:
- Estados Unidos
- Reino Unido
- Alemanha
- México
- Suécia
- Espanha
- Cingapura
- Brasil
- França
- Itália
- Colômbia
3. Você deve adquirir uma SKU(s) RCS de US$ 0 em seu contrato.

## Etapa 2: Registre um remetente verificado por RCS

Antes de poder enviar mensagens RCS, é necessário registrar um remetente verificado pelo RCS. Essa é a representação da sua marca que os usuários verão em seus dispositivos móveis, que inclui o nome da marca, o logotipo, um emblema de verificação e um slogan opcional. O remetente verificado pelo RCS reforça a confiança do cliente e confirma que suas mensagens vêm de uma fonte autenticada. 

\![Um exemplo de remetente verificado por RCS em uma mensagem RCS chamada "Cat Failz Cafe".]({% image_buster /assets/img/rcs/rcs_sender.png %}){: style="max-width:60%;"}

Depois de adicionar as SKUs RCS ao seu formulário de pedido, a Braze será notificada e entrará em contato com você com as informações de registro do remetente RCS. O formato dessas mensagens dependerá dos países para os quais você deseja enviar mensagens RCS. 

Depois de enviar os formulários preenchidos para a Braze, concluiremos o processo de registro em seu nome. 

### Etapa 2.1: Configurar fallbacks de SMS para grupos de assinatura RCS

Como a cobertura atual das operadoras varia de acordo com o país, e o suporte ao hardware e ao software do usuário varia de acordo com o indivíduo, o fallback de SMS é um componente essencial para ter um programa RCS bem-sucedido atualmente. Recomendamos configurar o fallback de SMS. Se uma operadora não for compatível com RCS ou se o dispositivo de um usuário não puder receber mensagens RCS, o fallback de SMS enviará sua mensagem independentemente disso, para que você nunca perca um momento importante com seus usuários.

É altamente recomendável analisar sua experiência atual de opt-in de SMS, grupos de assinatura e segmentação de público-alvo antes de implementar sua primeira campanha de RCS. Se necessário, o gerente de sucesso do cliente está sempre disponível para fornecer orientação e ajudá-lo a navegar pelo processo de configuração.

### Cronograma para aprovação da transportadora

O cronograma para aprovação da operadora varia de acordo com o país e também pode variar dentro de um mesmo país. Lembre-se de que o mercado de RCS ainda está engatinhando, portanto, os processos das operadoras e dos agregadores estão evoluindo rapidamente. Nos Estados Unidos, a Braze estima que o tempo de aprovação da operadora para um remetente verificado pelo RCS normalmente fica na faixa de 4 a 6 semanas, e um remetente de teste normalmente é aprovado em uma semana.

Quando seu remetente verificado por RCS for aprovado, nossa equipe de operações atualizará seus grupos de assinatura conforme necessário para confirmar que o remetente RCS está incluído neles. 

## Etapa 3: Configurar grupos de assinatura

Normalmente, o RCS é usado de duas maneiras: 
- Para atualizar o tráfego de SMS existente 
- Para permitir novos casos de uso que só são possíveis com a funcionalidade mais avançada fornecida pelo RCS

Dependendo da sua integração, o Braze pode adicionar remetentes verificados por RCS aos seus grupos de assinatura de SMS existentes ou configurar novos grupos de assinatura para você. Em ambos os casos, a equipe da Braze o orientará em uma atualização de tráfego SMS perfeita e em conformidade. Para obter mais informações, consulte [Grupos de assinatura de SMS e RCS]({{site.baseurl}}/sms_rcs_subscription_groups/).

Para novos casos de uso que não são possíveis com SMS, considere a possibilidade de configurar grupos de assinatura RCS dedicados para alinhar-se às metas do seu programa.