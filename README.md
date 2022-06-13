# Soft UI light theme
## This is an old theme. Some stuff might be broken.
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/hacs/integration)  
Home Assistant light theme, built on from @JuanMTech, using style boilerplates from @thomasloven and @N-L1.  
This theme depends on [`card-mod`](https://github.com/thomasloven/lovelace-card-mod) for the soft-ui styling.  
Looking for the [dark theme instead?](https://github.com/KTibow/lovelace-dark-soft-ui-theme/)  
This theme is pretty powerful. It can:
- Apply soft-ui to an auto-generated dashboard, and keep it auto-generated.
- Help you to only use the necessary style in your handmade dashboard, and keep it simple.
- Work in most places over HA, not just Lovelace.
- Apply a compact header to Lovelace, without installing an addon.
## Screenshot
[![Screenshot of it](lighttheme.png)](#)
*Custom dashboard made with [soft ui](https://github.com/N-l1/lovelace-soft-ui)*
## Notes
- You can use your own colors by just copy/pasting the card-mod part.
- This will clamp your columns to 1 column wide. [More info.](https://github.com/KTibow/lovelace-light-soft-ui-theme/issues/6#issuecomment-669204209)
- [These things are supported.](https://github.com/KTibow/lovelace-light-soft-ui-theme/issues/3)
- This theme was based off of the [Google Light Theme](https://github.com/JuanMTech/Home_Assistant_files/blob/b2ffbf2a3ffc05638b02f06d63e45618740ae281/themes/google_light_theme.yaml).
## Fonts
Some fonts that you should probably download and install that I think match Soft UI, or just load as a CSS resource:
- Quicksand: [Google Fonts page](https://fonts.google.com/specimen/Quicksand), [download](https://fonts.google.com/download?family=Quicksand), [Google Fonts css](https://fonts.googleapis.com/css?family=Quicksand&display=swap).
- Cascadia Code PL: [download](https://github.com/microsoft/cascadia-code/releases/latest) (click on the top asset, download, unzip, find `CascadiaCodePL.woff2`).
  
<details><summary>Tutorial on how to load any font into your browser</summary>

Upload the `woff2` into `/config/www`, and then make a file called `/config/www/fonts.js` which contains this:
```js
function loadcss() {
    let css = '/local/fonts.css?v=0.001';
    
    let link = document.createElement('link');
    let head = document.getElementsByTagName('head')[0];
    let tmp;
    link.rel = 'stylesheet';
    link.type = 'text/css';

    tmp = link.cloneNode(true);
    tmp.href = css;
    head.appendChild(tmp);
    console.info('%c Loaded font CSS at ' + css, 'color: white; background: #000; font-weight: 700;');
}
loadcss();
```
Then make a file called `/config/www/fonts.css` which contains this:
```css
@font-face {
  font-family: 'Cascadia Code PL';
  font-style: normal;
  font-weight: 400;
  src: url(/local/CascadiaCodePL.woff2) format('woff2');
}
```
(For each font, create the same thing in the file, but changing the source and name of font.)  
Then finally add `/local/fonts.js` to your list of lovelace resources. (Maybe?) Restart Home Assistant. Press Ctrl+Shift+R. Done!  
Credit to https://community.home-assistant.io/t/use-ttf-in-lovelace/143495.
</details>
