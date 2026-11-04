# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: SavingsGoal
def money(v):
    return f"{v:,.2f}"

def c(code, text):
    reset = "\033[0m"
    return f"\033[{code}m{text}{reset}" if code else text

def cgreen(t):  return c("32", t)
def cblue(t):   return c("34", t)
def cyellow(t): return c("33", t)
def cgray(t):   return c("90", t)
def cwhite(t):  return c("37", t)

def colorize_row(label, value, accent="32"):
    return c(accent, f"{label}: ") + cwhite(money(value))

def colorized_summary(goal):
    lines = []
    lines.append(cwhite("=" * 40))
    lines.append(c("1;36", f"{goal.name}"))
    lines.append(c("90", f"Target: {money(goal.target)}"))
    lines.append(c("90", f"Saved:   {money(goal.saved)}"))
    lines.append(c("90", f"Remaining: {money(goal.target - goal.saved)}"))
    lines.append(cwhite("=" * 40))
    return lines

def colorized_projection(goal):
    lines = []
    lines.append(cwhite("Projection:"))
    lines.append(c("90", f"{'Year':<6}{'Balance':>12}{'Progress':>10}"))
    for y in range(1, 6):
        bal = goal.projected(y)
        pct = min(100, round(bal / goal.target * 100))
        bar = "#" * (pct // 10) + "-" * (10 - pct // 10)
        lines.append(cblue(f"{y:<6}") + cwhite(f"{money(bal):>12}") + cgreen(f"[{bar}] {pct:>2}%"))
    return lines
