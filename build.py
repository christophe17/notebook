#!/usr/bin/env python3
"""Build a static website from topic summaries and Jupyter notebooks."""

import re
import shutil
from pathlib import Path

import nbformat
from markdown import markdown
from nbconvert import HTMLExporter
from nbconvert.preprocessors import ExecutePreprocessor

SITE_DIR = Path("_site")
PROJECT_DIR = Path(__file__).parent

# Topic summary files (order determines display order on landing page)
TOPIC_FILES = ["topics/probabilistic-ml.md", "topics/jax.md"]

# ---------------------------------------------------------------------------
# Shared CSS
# ---------------------------------------------------------------------------
CSS = """\
:root {
  --bg: #ffffff; --fg: #1a1a2e; --muted: #64748b;
  --border: #e2e8f0; --accent: #4f46e5; --accent-hover: #4338ca;
  --code-bg: #f8fafc; --cell-bg: #f1f5f9;
  --font: "Inter", system-ui, -apple-system, sans-serif;
  --mono: "JetBrains Mono", "Fira Code", ui-monospace, monospace;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0f172a; --fg: #e2e8f0; --muted: #94a3b8;
    --border: #334155; --accent: #818cf8; --accent-hover: #a5b4fc;
    --code-bg: #1e293b; --cell-bg: #1e293b;
  }
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { font-size: 17px; }
body {
  font-family: var(--font); color: var(--fg); background: var(--bg);
  line-height: 1.7; max-width: 960px; margin: 0 auto;
  padding: 3rem 1.5rem 5rem;
}
h1, h2, h3 { line-height: 1.3; }
h1 { font-size: 2rem; margin-bottom: .3rem; }
h2 { font-size: 1.4rem; margin-top: 2.5rem; margin-bottom: 1rem; color: var(--accent); }
h3 { font-size: 1.15rem; margin-top: 1.5rem; margin-bottom: .5rem; }
a { color: var(--accent); text-decoration: none; }
a:hover { color: var(--accent-hover); text-decoration: underline; }
hr { border: none; border-top: 1px solid var(--border); margin: 2rem 0; }
p { margin-bottom: 1rem; }
code {
  font-family: var(--mono); font-size: .88em;
  background: var(--code-bg); padding: .15em .35em; border-radius: 4px;
}
pre { background: var(--code-bg); padding: 1rem; border-radius: 8px;
      overflow-x: auto; margin-bottom: 1rem; }
pre code { background: none; padding: 0; }

/* Tables (topic summaries) */
table { width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: .92rem; }
th, td { padding: .6rem .8rem; border: 1px solid var(--border); vertical-align: top; }
th { background: var(--cell-bg); font-weight: 600; }

/* Notebook output */
.jp-OutputArea-output img, .output img, .jp-RenderedImage img {
  max-width: 100%; height: auto;
}
.jp-InputArea, .input_area {
  background: var(--code-bg); border-radius: 8px; margin-bottom: .5rem;
  padding: .75rem 1rem;
}
.jp-OutputArea, .output_area { margin-bottom: 1rem; }

.back-link {
  display: inline-block; margin-bottom: 1.5rem;
  font-size: .9rem; color: var(--muted);
}
.back-link:hover { color: var(--accent); }
.subtitle { color: var(--muted); margin-bottom: 2rem; font-size: 1.05rem; }

/* Topic cards (landing page) */
.topic-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 1.5rem; margin-top: 2rem;
}
.topic-card {
  border: 1px solid var(--border); border-radius: 12px;
  padding: 2rem; transition: border-color .2s, box-shadow .2s;
  text-decoration: none; color: var(--fg); display: block;
}
.topic-card:hover {
  border-color: var(--accent); box-shadow: 0 4px 12px rgba(79, 70, 229, .1);
  text-decoration: none;
}
@media (prefers-color-scheme: dark) {
  .topic-card:hover { box-shadow: 0 4px 12px rgba(129, 140, 248, .15); }
}
.topic-card h2 { margin-top: 0; margin-bottom: .5rem; }
.topic-card p { color: var(--muted); margin: 0; font-size: .95rem; }

@media (max-width: 767px) {
  body { padding: 1rem 0.5rem 3rem; }
  .topic-grid { grid-template-columns: 1fr; }
}
"""

# ---------------------------------------------------------------------------
# HTML wrappers
# ---------------------------------------------------------------------------
def page_html(title: str, body: str, extra_head: str = "") -> str:
    return f"""\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{CSS}</style>
{extra_head}
</head>
<body>
{body}
</body>
</html>"""


NOTEBOOK_EXTRA_CSS = """\
<style>
.cm-editor.cm-s-jupyter .highlight pre { padding: 10px !important; }
</style>"""

NOTEBOOK_DARK_CSS = """\
<style>
@media (prefers-color-scheme: dark) {
  :root {
    /* Grey palette — invert for dark */
    --md-grey-50: #212121; --md-grey-100: #303030; --md-grey-200: #424242;
    --md-grey-300: #616161; --md-grey-400: #757575; --md-grey-500: #9e9e9e;
    --md-grey-600: #bdbdbd; --md-grey-700: #e0e0e0; --md-grey-800: #eee;
    --md-grey-900: #fafafa;

    /* Backgrounds */
    --jp-layout-color0: #0f172a;
    --jp-layout-color1: #0f172a;
    --jp-layout-color2: #1e293b;
    --jp-layout-color3: #334155;
    --jp-layout-color4: #475569;

    /* Inverse backgrounds */
    --jp-inverse-layout-color0: #f8fafc;
    --jp-inverse-layout-color1: #e2e8f0;
    --jp-inverse-layout-color2: #cbd5e1;
    --jp-inverse-layout-color3: #94a3b8;
    --jp-inverse-layout-color4: #64748b;

    /* Text */
    --jp-content-font-color0: rgba(226, 232, 240, 1);
    --jp-content-font-color1: rgba(226, 232, 240, 0.87);
    --jp-content-font-color2: rgba(226, 232, 240, 0.6);
    --jp-content-font-color3: rgba(226, 232, 240, 0.4);
    --jp-ui-font-color0: rgba(226, 232, 240, 1);
    --jp-ui-font-color1: rgba(226, 232, 240, 0.87);
    --jp-ui-font-color2: rgba(226, 232, 240, 0.6);
    --jp-ui-font-color3: rgba(226, 232, 240, 0.4);

    /* Borders */
    --jp-border-color0: #334155;
    --jp-border-color1: #334155;
    --jp-border-color2: #1e293b;
    --jp-border-color3: #1e293b;

    /* Cells */
    --jp-cell-editor-background: #1e293b;
    --jp-cell-editor-active-background: #0f172a;
    --jp-cell-editor-border-color: #334155;

    /* Brand */
    --jp-brand-color0: #818cf8;
    --jp-brand-color1: #6366f1;
    --jp-brand-color2: #4f46e5;

    /* Syntax highlighting — VSCode Dark Modern base variables */
    --jp-mirror-editor-keyword-color: #569CD6;
    --jp-mirror-editor-number-color: #B5CEA8;
    --jp-mirror-editor-variable-color: #9CDCFE;
    --jp-mirror-editor-variable-2-color: #9CDCFE;
    --jp-mirror-editor-variable-3-color: #4EC9B0;
    --jp-mirror-editor-punctuation-color: #D4D4D4;
    --jp-mirror-editor-operator-color: #D4D4D4;
    --jp-mirror-editor-comment-color: #6A9955;
    --jp-mirror-editor-string-color: #CE9178;
    --jp-mirror-editor-string-2-color: #CE9178;
    --jp-mirror-editor-error-color: #F44747;

    /* Misc */
    --jp-rendermime-error-background: #450a0a;
    --jp-rendermime-table-row-background: #1e293b;
    --jp-input-background: #1e293b;
    --jp-toolbar-active-background: #334155;
  }

  /* VSCode Dark Modern — per-token overrides (Pygments classes) */
  /* Control-flow keywords: if, for, return, import, with, etc. */
  .highlight .kr,                          /* reserved */
  .highlight .kn { color: #C586C0; }      /* namespace (import/from) */
  /* Type names */
  .highlight .kt,                          /* keyword type */
  .highlight .nc,                          /* class name */
  .highlight .ne { color: #4EC9B0; }      /* exception */
  /* Function / decorator names */
  .highlight .nf,                          /* function name */
  .highlight .fm,                          /* magic function */
  .highlight .nb,                          /* builtin (print, len, …) */
  .highlight .nd { color: #DCDCAA; }      /* decorator */
  /* self / cls */
  .highlight .bp { color: #569CD6; }      /* builtin pseudo */
  /* Constants */
  .highlight .no { color: #4FC1FF; }      /* constant name */
  /* Escape chars in strings */
  .highlight .se { color: #D7BA7D; }      /* string escape */
  /* Word operators (and, or, not, in, is) */
  .highlight .ow { color: #569CD6; }
  /* Default text */
  .highlight .w { color: #D4D4D4; }

  /* Back link */
  .back-link { color: #94a3b8; }
  .back-link:hover { color: #818cf8; }
  /* DataFrame / table outputs */
  .dataframe, .rendered_html table { color: #e2e8f0; }
  .dataframe th, .rendered_html th { background: #1e293b !important; }
  .dataframe td, .rendered_html td { background: #0f172a !important; }
}
</style>"""

MATHJAX = """\
<script>
MathJax = {
  tex: { inlineMath: [['$','$'], ['\\\\(','\\\\)']], displayMath: [['$$','$$'], ['\\\\[','\\\\]']] },
  options: { skipHtmlTags: ['script','noscript','style','textarea','pre','code'] }
};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" async></script>"""


# ---------------------------------------------------------------------------
# Parse topic metadata from markdown files
# ---------------------------------------------------------------------------
def parse_topic(filepath: Path) -> dict:
    """Extract title, subtitle, and slug from a topic markdown file."""
    text = filepath.read_text(encoding="utf-8")
    slug = filepath.stem  # e.g. "probabilistic-ml"

    # Title = first H1
    m = re.search(r'^#\s+(.+)$', text, re.MULTILINE)
    title = m.group(1).strip() if m else slug

    # Subtitle = first paragraph after the H1 (non-heading, non-blank, non-rule)
    lines = text.split('\n')
    subtitle = ""
    past_title = False
    for line in lines:
        if not past_title:
            if line.startswith('# '):
                past_title = True
            continue
        stripped = line.strip()
        if not stripped or stripped.startswith('#') or stripped.startswith('---'):
            continue
        # Strip markdown bold/italic for plain text subtitle
        subtitle = re.sub(r'\*\*(.+?)\*\*', r'\1', stripped)
        subtitle = re.sub(r'\*(.+?)\*', r'\1', subtitle)
        break

    return {"slug": slug, "title": title, "subtitle": subtitle, "path": filepath}


# ---------------------------------------------------------------------------
# Build landing page (index.html) with topic cards
# ---------------------------------------------------------------------------
def build_landing(topics: list[dict]):
    cards = []
    for t in topics:
        cards.append(
            f'<a class="topic-card" href="{t["slug"]}.html">'
            f'<h2>{t["title"]}</h2>'
            f'<p>{t["subtitle"]}</p>'
            f'</a>'
        )

    body = (
        '<h1>Notebooks</h1>'
        '<p class="subtitle">Interactive notebooks for learning by doing.</p>'
        '<div class="topic-grid">'
        + '\n'.join(cards)
        + '</div>'
    )
    html = page_html("Notebooks", body)
    (SITE_DIR / "index.html").write_text(html, encoding="utf-8")
    print("  index.html")


# ---------------------------------------------------------------------------
# Build topic summary pages
# ---------------------------------------------------------------------------
def build_topics(topics: list[dict]):
    for t in topics:
        text = t["path"].read_text(encoding="utf-8")
        # Rewrite .ipynb links to .html
        text = re.sub(r'\(\.\./notebooks/(.+?)\.ipynb\)', r'(notebooks/\1.html)', text)
        body = markdown(text, extensions=["tables", "fenced_code"])
        # Add back-link to landing page
        back_link = '<a class="back-link" href="index.html">&larr; All topics</a>'
        body = back_link + body
        html = page_html(t["title"], body, extra_head=MATHJAX)
        (SITE_DIR / f'{t["slug"]}.html').write_text(html, encoding="utf-8")
        print(f'  {t["slug"]}.html')


# ---------------------------------------------------------------------------
# Build notebook HTML files
# ---------------------------------------------------------------------------
def build_notebooks(slug_to_topic: dict[str, dict]):
    exporter = HTMLExporter()
    exporter.template_name = "classic"
    exporter.exclude_input_prompt = True
    exporter.exclude_output_prompt = True

    ep = ExecutePreprocessor(timeout=600, kernel_name="python3")

    notebooks = sorted(PROJECT_DIR.glob("notebooks/**/*.ipynb"))
    for nb_path in notebooks:
        rel = nb_path.relative_to(PROJECT_DIR)
        out_path = SITE_DIR / rel.with_suffix(".html")
        out_path.parent.mkdir(parents=True, exist_ok=True)

        # Topic slug is the first folder under notebooks/
        # e.g. notebooks/probabilistic-ml/3-multivariate-models/file.ipynb → "probabilistic-ml"
        topic_slug = rel.parts[1]
        topic = slug_to_topic.get(topic_slug)

        # Compute relative path back to topic summary
        depth = len(rel.parts) - 1
        prefix = "/".join([".."] * depth)
        if topic:
            back_href = f'{prefix}/{topic["slug"]}.html'
            back_text = f'&larr; {topic["title"]}'
        else:
            back_href = f'{prefix}/index.html'
            back_text = '&larr; Back to index'

        # Execute notebook to produce outputs, then convert to HTML
        nb = nbformat.read(str(nb_path), as_version=4)
        try:
            ep.preprocess(nb, {"metadata": {"path": str(nb_path.parent)}})
        except Exception as e:
            print(f"  WARNING: execution failed for {rel}: {e}")
        body_raw, _ = exporter.from_notebook_node(nb)

        # Inject back-link right after <body...>
        back_link = f'<a class="back-link" href="{back_href}">{back_text}</a>'
        body_raw = re.sub(r'(<body[^>]*>)', rf'\1{back_link}', body_raw, count=1)

        # Add MathJax (some notebook templates already include it, but this ensures it)
        if "mathjax" not in body_raw.lower():
            body_raw = body_raw.replace("</head>", f"{MATHJAX}\n</head>", 1)

        # Inject extra notebook CSS + dark mode CSS
        body_raw = body_raw.replace("</head>", f"{NOTEBOOK_EXTRA_CSS}\n{NOTEBOOK_DARK_CSS}\n</head>", 1)

        out_path.write_text(body_raw, encoding="utf-8")
        print(f"  {rel.with_suffix('.html')}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    SITE_DIR.mkdir()

    # Parse all topic files
    topics = []
    for fname in TOPIC_FILES:
        path = PROJECT_DIR / fname
        if path.exists():
            topics.append(parse_topic(path))

    # Build slug → topic mapping
    slug_to_topic = {t["slug"]: t for t in topics}

    print("Building landing page...")
    build_landing(topics)

    print("Building topic pages...")
    build_topics(topics)

    print("Building notebooks...")
    build_notebooks(slug_to_topic)

    print(f"\nDone! Site generated in {SITE_DIR}/")
    print(f"Serve locally with:  python -m http.server -d {SITE_DIR}")


if __name__ == "__main__":
    main()
