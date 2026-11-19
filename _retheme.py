from pathlib import Path
import re

ROOT = Path(r"d:\dilipanafinal")
FILES = [
    "signin.html",
    "signup.html",
    "browser.html",
    "student-dashboard.html",
    "owner-dashboard.html",
    "admin-dashboard.html",
]

HEX = {
    "#1b2d47": "#1b4334",
    "#18283f": "#143328",
    "#132238": "#10281f",
    "#263c5d": "#9a3b1b",
    "#314c75": "#c4512c",
    "#2563eb": "#c4512c",
    "#2866c4": "#c4512c",
    "#1d4ed8": "#9a3b1b",
    "#3b82f6": "#c4512c",
    "#1e40af": "#9a3b1b",
    "#1e3a8a": "#9a3b1b",
    "#0369a1": "#1b4334",
    "#0891b2": "#1b4334",
    "#0f172a": "#1c1915",
    "#1a202c": "#1c1915",
    "#1e293b": "#1c1915",
    "#334155": "#3f3832",
    "#475569": "#5c534b",
    "#64748b": "#6f675e",
    "#94a3b8": "#a3988c",
    "#e2e8f0": "#e6dccb",
    "#cbd5e1": "#d9ccb8",
    "#f1f5f9": "#efe6d6",
    "#f8fafc": "#f6f1e8",
    "#f0f4f9": "#f6f1e8",
    "#fafcff": "#fffdf8",
    "#dbeafe": "#f6e4d6",
    "#bfdbfe": "#f0d3c2",
    "#eff6ff": "#fff6ee",
    "#e0f2fe": "#fff6ee",
}

RGBA = [
    ("rgba(49, 76, 117,", "rgba(196, 81, 44,"),
    ("rgba(49,76,117,", "rgba(196, 81, 44,"),
    ("rgba(37, 99, 235,", "rgba(196, 81, 44,"),
    ("rgba(37,99,235,", "rgba(196, 81, 44,"),
    ("rgba(27, 45, 71,", "rgba(27, 67, 52,"),
    ("rgba(27,45,71,", "rgba(27, 67, 52,"),
    ("rgba(24, 40, 63,", "rgba(27, 67, 52,"),
    ("rgba(15, 23, 42,", "rgba(28, 25, 21,"),
    ("rgba(15,23,42,", "rgba(28, 25, 21,"),
]

FONT_LINK = (
    "https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,620;1,9..144,560"
    "&family=Outfit:wght@400;500;600;700&display=swap"
)
THEME = '  <link rel="stylesheet" href="css/theme.css"/>\n'


def recolor(text: str, name: str) -> str:
    if name in ("signin.html", "signup.html"):
        text = text.replace("background-color: #314c75;", "background-color: #1b4334;", 1)
    for old, new in HEX.items():
        text = re.sub(re.escape(old), new, text, flags=re.I)
    for old, new in RGBA:
        text = text.replace(old, new)
    text = text.replace("Plus Jakarta Sans", "Outfit")
    text = re.sub(
        r"https://fonts\.googleapis\.com/css2\?family=Plus\+Jakarta\+Sans:[^\"']+",
        FONT_LINK,
        text,
    )
    # Some files already had the Plus Jakarta URL rewritten only in CSS family name.
    if "family=Outfit" not in text and "fonts.googleapis.com" in text:
        text = re.sub(
            r"https://fonts\.googleapis\.com/css2\?family=[^\"']+",
            FONT_LINK,
            text,
            count=1,
        )
    if "css/theme.css" not in text:
        text = text.replace("</head>", THEME + "</head>", 1)
    text = text.replace(
        '<span class="logo-text">DormFinder</span>',
        '<span class="logo-text">Dorm<span class="gold">Finder</span></span>',
    )
    text = text.replace(
        "      DormFinder\n",
        '      Dorm<span class="gold">Finder</span>\n',
    )
    return text


for name in FILES:
    path = ROOT / name
    original = path.read_text(encoding="utf-8")
    updated = recolor(original, name)
    path.write_text(updated, encoding="utf-8")
    leftover = len(re.findall(r"#(?:1b2d47|2563eb|314c75|2866c4|f8fafc)", updated, re.I))
    print(f"{name}: wrote, leftover brand colors {leftover}, theme {'css/theme.css' in updated}")
