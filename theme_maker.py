import colorsys


def convert_color(color):
    color = [round(comp * 255.0) for comp in color]
    color = "".join([format(comp, "x") for comp in color])
    color = color.zfill(6)
    return f'"#{color}"'


theme = open("theme.yaml").read()
for color_name, color_hue in [
    ["Red", 0],
    ["Fire", 18],
    ["Orange", 36],
    ["Yellow", 54],
    ["Lime", 90],
    ["Green", 129],
    ["Mint Green", 155],
    ["Mint", 180],
    ["Cyan", 200],
    ["", 214],
    ["Indigo", 260],
    ["Purple", 275],
    ["Pink", 300],
]:
    primary_color = colorsys.hsv_to_rgb(color_hue / 360.0, 0.59, 0.92)
    primary_color = convert_color(primary_color)
    accent_color = colorsys.hsv_to_rgb(((color_hue - 25) % 360) / 360.0, 0.59, 0.92)
    accent_color = convert_color(accent_color)
    background_color = colorsys.hsv_to_rgb(color_hue / 360.0, 0.03, 0.97)
    # background_color = colorsys.hsv_to_rgb(color_hue / 360.0, 0.13, 0.22)
    background_color = convert_color(background_color)
    with open(
        rf"themes\soft-ui-{color_name.lower().replace(' ', '-')}.yaml", "w"
    ) as theme_file:
        theme_file.write(
            theme.replace("{color_name}", color_name)
            .replace("{primary_color}", primary_color)
            .replace("{accent_color}", accent_color)
            .replace("{background_color}", background_color)
        )
