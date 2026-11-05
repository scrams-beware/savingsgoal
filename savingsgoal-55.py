# === Stage 55: Add a setting to disable colorized output ===
# Project: SavingsGoal
COLOR_ENABLED = not os.environ.get("SAVINGS_COLOR", "").lower() in ("0", "false", "no", "off")


def colorize(text, color):
    if COLOR_ENABLED and color in COLORS:
        return "\033[{}m{}\033[0m".format(COLORS[color], text)
    return text


def money(text, positive=True):
    return colorize(text, "green" if positive else "red")


def header(text):
    return colorize(text, "bold")


def section(text):
    return colorize(text, "cyan")


def dim(text):
    return colorize(text, "dim")


def enable_color():
    global COLOR_ENABLED
    COLOR_ENABLED = True


def disable_color():
    global COLOR_ENABLED
    COLOR_ENABLED = False


def set_color_enabled(value):
    global COLOR_ENABLED
    COLOR_ENABLED = value in (True, 1, "yes", "true", "on")


if __name__ == "__main__":
    print(header("SavingsGoal Color Setting"))
    print("Colorized output is currently enabled: {}".format(COLOR_ENABLED))
    print("Tip: set SAVINGS_COLOR=0 to disable colorized output.")
    print("Example colored text: {}".format(colorize("Hello", "bold")))
