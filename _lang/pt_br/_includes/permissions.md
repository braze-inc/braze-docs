{% if include.content == "Differences" %}

Você pode usar [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/), [conjuntos de permissões]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-permission-set) e [funções de usuário]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) para gerenciar o acesso e as responsabilidades do usuário do dashboard no Braze. Cada recurso engloba um conjunto diferente de permissões e controles de acesso.

### Principais diferenças

Em um nível elevado, cada recurso tem um escopo diferente:
- Os conjuntos de permissões controlam o que os usuários do dashboard podem fazer em todos os espaços de trabalho.
- As funções controlam o que os usuários do dashboard podem fazer em espaços de trabalho específicos.
- As equipes controlam os públicos que os usuários do dashboard podem alcançar com suas mensagens.

| Recurso | O que você pode fazer | Escopo de acesso |
| - | - | - |
| [Conjuntos de permissão]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-permission-set) | Agrupe as permissões relacionadas a áreas temáticas ou ações específicas (como para "Desenvolvedores" e "Profissionais de marketing") e, em seguida, aplique-as aos usuários do dashboard que precisam das mesmas permissões em diferentes espaços de trabalho. | Toda a empresa |
| [Funções]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) | Agrupe permissões personalizadas individuais e controles de acesso ao espaço de trabalho (como "Profissional de marketing - Marcas de moda", em que o usuário tem determinadas permissões associadas à sua função de profissional de marketing e está limitado aos espaços de trabalho "Marcas de moda"). Em seguida, atribua uma função aos usuários do dashboard para conceder-lhes diretamente as permissões associadas e o acesso ao espaço de trabalho. <br><br>Os usuários com esse nível de acesso geralmente são gerentes em configurações mais rigidamente controladas, com muitas marcas ou espaços de trabalho regionais em um dashboard. | Espaços de trabalho específicos |
| [Equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/#creating-teams) | Limite o acesso do usuário do dashboard a recursos com base no público (como local da base de clientes, idioma e atributos personalizados). <br><br>Os usuários com esse nível de acesso geralmente são responsáveis por um escopo específico dentro da marca em que estão trabalhando, como a criação de conteúdo específico de um idioma para uma marca multilíngue. | Painel de controle específico |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endif %}