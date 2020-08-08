# Lovelace Soft UI light theme 
{% if installed %}
**Thanks for installing!**
{% else %}
**Install? I worked pretty hard on this...**
{% endif %}
{% if version_available != version_installed %}
## Please update your version! It's important, as I've added stuff in version {{version_available}}
{% endif %}
Home Assistant light theme, built on from @JuanMTech, using style boilerplates from @thomasloven and @N-L1.  
This theme depends on [`card-mod`](https://github.com/thomasloven/lovelace-card-mod) for the soft-ui styling.  
Looking for the [dark theme instead?](https://github.com/KTibow/lovelace-dark-soft-ui-theme/)  
## Screenshot
[![Screenshot of it](https://raw.githubusercontent.com/KTibow/lovelace-light-soft-ui-theme/main/lighttheme.png)](#)
## Features
This theme can
- Apply soft-ui to an auto-generated dashboard, and keep it auto-generated.
- Help you to only use the necessary style in your handmade dashboard, and keep it simple.
- Work in most places over HA, not just Lovelace.
- Apply a compact header to Lovelace, without installing an addon.
## More details
This will clamp your columns to 1 column wide. [More info.](https://github.com/KTibow/lovelace-light-soft-ui-theme/issues/6#issuecomment-669204209)
Go see more [over on GitHub](https://github.com/KTibow/lovelace-light-soft-ui-theme/).
