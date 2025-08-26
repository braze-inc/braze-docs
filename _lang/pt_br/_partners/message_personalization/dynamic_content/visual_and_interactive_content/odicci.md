---
nav_title: Odicci
article_title: Odicci
description: "Guia passo a passo para integrar a Odicci ao Braze para campanhas de marketing personalizadas"
alias: /partners/odicci/
page_type: partner
search_tag: Partner
---

# Integração da Odicci com o Braze

> Saiba como integrar o Braze com a [Odicci](https://www.odicci.com/), uma plataforma que capacita as empresas a adquirir, engajar e reter clientes por meio de experiências omnicanal orientadas pela fidelidade.

{% alert tip %}
Consulte a [Central de Ajuda da Odicci](https://help.odicci.com) para obter recursos adicionais e perguntas frequentes.
{% endalert %}

## Casos de uso

Você pode conectar a plataforma Odicci com o Braze para um compartilhamento de dados e gerenciamento de campanhas perfeitos, que incluem:

- Envio automático dos dados do público coletados nas experiências da Odicci para o Braze.
- A disparar campanhas de marketing personalizadas com base nas interações do usuário.
- Mapeamento de campos entre a Odicci e o Braze para garantir a sincronização precisa dos dados.

## Exemplo

Um varejista usa as experiências gamificadas da Odicci para coletar endereços de e-mail para uma campanha de marketing.

1. Um cliente conclui um jogo na Odicci, fornecendo seu endereço de e-mail.
2. A Odicci sincroniza automaticamente esses dados com o Braze.
3. O Braze dispara um e-mail personalizado de agradecimento e inclui um código de desconto.

## Pré-requisitos

Antes de começar, você precisará do seguinte:

| Pré-requisito             | Descrição                                                               |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Um relato da Odicci            | É necessário ter uma conta na Odicci com acesso à seção **Integrações** para aproveitar essa parceria.|
| Chave da API REST do Braze        | Uma chave da API REST do Braze com as permissões `users.track` e 'campaigns.list'. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração da Odicci

### Etapa 1: Ativar a integração no Odicci

1. Faça o registro em sua conta Odicci.
2. Navegue até a seção **Configurações > Integrações**.
3. Encontre a integração **do Braze** e clique em **Connect (Conectar**).

   ![Integração do Connect Braze]({% image_buster /assets/img/odicci/braze_connect.png %})

4. Digite sua chave da API REST do Braze no campo fornecido.
5. Salve as configurações para ativar a integração no nível da conta.

### Etapa 2: Obter sua chave da API REST do Braze

1. Faça o registro em sua conta Braze.
2. Acesse **Console do desenvolvedor > Chaves da API REST.**
3. Crie uma nova chave de API ou copie uma existente com a permissão `users.track`.

### Etapa 3: Ativar a integração no nível da experiência

1. Crie ou abra uma **experiência** no Odicci Studio.
2. Navegue até **Studio > Configurações > Integrações**.
3. Localize a caixa de seleção **Braze** e marque-a para ativar a integração para a experiência.
4. Salve suas alterações.

### Etapa 4: Campos do mapa

1. Depois de ativar a integração, permaneça na seção **Studio > Configurações > Integrações**.
2. Mapeie os campos de sua experiência na Odicci (e.g., `Email`, `Name`) para seus campos correspondentes no Braze.
3. Salve sua configuração.

   ![Configuração de mapeamento de campo]({% image_buster /assets/img/odicci/braze_field_mapping.png %})

### Etapa 5: Teste a integração

1. Execute a experiência no Odicci para coletar dados de teste.
2. Verifique se os dados estão sincronizados corretamente com o Braze, verificando o dashboard do Braze ou os registros de dados.
3. Certifique-se de que os campos mapeados estejam preenchidos corretamente no Braze.

## Solução de problemas

Se você tiver problemas com a integração, considere as seguintes soluções. Para obter mais assistência, entre em contato com o [Suporte da Odicci](https://help.odicci.com).

### Chave de API não válida

Verifique novamente sua chave de API do Braze e certifique-se de que ela tenha as permissões necessárias. Em seguida, insira novamente a chave de API nas configurações de integração da Odicci.

### Os dados não estão sendo sincronizados

Verifique se os campos na seção **Mapeamento de campos** estão configurados corretamente. Em seguida, certifique-se de que a chave de API tenha permissões para importações de dados de usuários.

### Campanha não está sendo disparada

Verifique as configurações de campanha do Braze para garantir que o público ou as condições de disparo corretos estejam definidos.
