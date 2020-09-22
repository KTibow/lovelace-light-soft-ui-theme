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
    ["Mint", 155],
    ["Cyan", 190],
    ["", 214],
    ["Violet", 270],
    ["Rose", 315],
]:
    primary_color = colorsys.hsv_to_rgb(color_hue / 360.0, 0.59, 0.92)
    primary_color = convert_color(primary_color)
    accent_color = colorsys.hsv_to_rgb(((color_hue - 15) % 360) / 360.0, 0.59, 0.92)
    accent_color = convert_color(accent_color)
    background_color = colorsys.hsv_to_rgb(color_hue / 360.0, 0.025, 0.97)
    background_color = convert_color(background_color)
    more_info_background_color = background_color.replace('"', "") + "b2"
    if color_name != "":
        color_name = " " + color_name
    file_color_name = color_name.lower().replace(" ", "-")
    with open(rf"themes\light-soft-ui{file_color_name}.yaml", "w") as theme_file:
        theme_file.write(
            theme.replace("{color_name}", color_name)
            .replace("{primary_color}", primary_color)
            .replace("{accent_color}", accent_color)
            .replace("{background_color}", background_color)
            .replace("{more_info_background_color}", more_info_background_color)
        )
