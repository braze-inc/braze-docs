{% if include.content == "Differences" %}

Você pode usar [Equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/), [conjuntos de permissões]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-permission-set) e [papéis de usuário]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) para gerenciar o acesso e as responsabilidades dos usuários da empresa dentro do Braze. Cada recurso engloba um conjunto diferente de permissões e controles de acesso.

### Principais diferenças

Em um nível elevado, cada recurso tem um escopo diferente:
- Os conjuntos de permissões controlam o que os usuários da empresa podem fazer em todos os espaços de trabalho.
- Os papéis controlam o que os usuários da empresa podem fazer em espaços de trabalho específicos.
- As equipes controlam os públicos que os usuários da empresa podem alcançar com suas mensagens.

| Recurso | O que você pode fazer | Escopo de acesso |
| - | - | - |
| [Conjuntos de permissão]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-permission-set) | Agrupe permissões relacionadas a áreas de assunto ou ações específicas (como para "Desenvolvedores" e "Profissionais de Marketing"), e aplique-as aos usuários da empresa que precisam das mesmas permissões em diferentes espaços de trabalho. | Em toda a empresa |
| [Funções]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) | Agrupe permissões personalizadas individuais e controles de acesso a espaços de trabalho (como "Profissional de Marketing - Marcas de Moda", onde o usuário tem certas permissões associadas ao seu papel como profissional de marketing e está limitado aos espaços de trabalho "Marcas de Moda"). Em seguida, atribua um papel aos usuários da empresa para conceder diretamente as permissões e o acesso ao espaço de trabalho associados. <br><br>Usuários com esse nível de acesso são tipicamente gerentes em configurações mais controladas com muitas marcas ou espaços de trabalho regionais em um dashboard. | Espaços de trabalho específicos |
| [Equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/#creating-teams) | Limite o acesso dos usuários da empresa a recursos com base no público (como localização da base de clientes, idioma e atributos personalizados). <br><br>Usuários com esse nível de acesso geralmente são responsáveis por um escopo específico dentro da marca em que estão trabalhando, como criar conteúdo específico para idiomas para uma marca multilíngue. | Dashboard específico |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endif %}