{% if include.content == "Differences" %}

Sie können [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/), [Berechtigungssätze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-permission-set) und [Nutzer:innen-Rollen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) verwenden, um den Zugriff von Dashboard-Benutzern und deren Verantwortlichkeiten innerhalb von Braze zu verwalten. Jede Funktion umfasst eine andere Sammlung von Berechtigungen und Zugriffskontrollen.

### Wesentliche Unterschiede

Auf einer hohen Ebene hat jede Funktion einen anderen Umfang:
- Berechtigungssätze steuern, was Dashboard-Benutzer in allen Arbeitsbereichen tun können.
- Rollen steuern, was Dashboard-Benutzer in bestimmten Arbeitsbereichen tun können.
- Teams kontrollieren die Zielgruppen, die Nutzer:innen des Dashboards mit ihren Nachrichten erreichen können.

| Feature | Was Sie tun können | Umfang des Zugriffs |
| - | - | - |
| [Berechtigungssätze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-permission-set) | Bündeln Sie Berechtigungen, die sich auf bestimmte Themenbereiche oder Aktionen beziehen (z.B. für "Entwickler:in" und "Marketer"), und wenden Sie diese dann auf Nutzer:innen des Dashboards an, die dieselben Berechtigungen in verschiedenen Workspaces benötigen. | Unternehmensweit |
| [Rollen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) | Bündeln Sie individuell angepasste Berechtigungen und Workspace-Zugriffskontrollen (z.B. "Marketer - Fashion Brands", bei dem der Nutzer:in seiner Rolle als Marketer bestimmte Berechtigungen hat und auf die Workspaces "Fashion Brands" beschränkt ist). Weisen Sie dann den Nutzer:innen des Dashboards eine Rolle zu, um ihnen direkt die zugehörigen Berechtigungen und den Zugriff auf den Workspace zu gewähren. <br><br>Nutzer:innen mit dieser Zugriffsebene sind in der Regel Manager:innen in stärker kontrollierten Einrichtungen mit vielen Marken oder regionalen Workspaces in einem Dashboard. | Spezifische Workspaces |
| [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/#creating-teams) | Schränken Sie den Zugriff der Nutzer:innen des Dashboards auf Ressourcen ein, die auf der Zielgruppe basieren (z.B. Standort der Nutzerbasis, Sprache und angepasste Attribute). <br><br>Nutzer:innen mit dieser Zugriffsstufe sind in der Regel für einen bestimmten Bereich innerhalb der Marke verantwortlich, an dem sie arbeiten, z. B. für die Erstellung sprachspezifischer Inhalte für eine mehrsprachige Marke. | Spezifisches Dashboard |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endif %}