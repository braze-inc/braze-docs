{% if include.release == "General availability" %}

<span style="display: inline-flex; align-items: center; background: #00bf7d; color: rgba(0, 0, 0, .87); padding: 6px 17px; border-radius: 16px; font-size: 14px; height: 32px; margin: 3px; transition: all .3s ease; border: 1px solid transparent; font-weight: bold;">
    Disponibilidad general
</span>

{% elsif include.release == "Early access" %}

<span style="display: inline-flex; align-items: center; background: #ff9349; color: rgba(0, 0, 0, .87); padding: 6px 17px; border-radius: 16px; font-size: 14px; height: 32px; margin: 3px; transition: all .3s ease; border: 1px solid transparent; font-weight: bold;">
    Acceso anticipado
</span>


{% elsif include.release == "Beta" %}

<span style="display: inline-flex; align-items: center; background: #50c5d4; color: rgba(0, 0, 0, .87); padding: 6px 17px; border-radius: 16px; font-size: 14px; height: 32px; margin: 3px; transition: all .3s ease; border: 1px solid transparent; font-weight: bold;">
    Beta
</span>

{% endif %}