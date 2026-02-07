# Upgrading the Chirpy Theme

This site uses the [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) gem. Upgrades can silently break JS-dependent features if custom overrides conflict with new theme files.

## When to Upgrade

| Reason | Urgency |
|--------|---------|
| Security fix in Jekyll or Chirpy | High |
| New Chirpy feature you want | Medium |
| Staying current (< 2 minor versions behind) | Low |

Check the [Chirpy changelog](https://github.com/cotes2020/jekyll-theme-chirpy/releases) before upgrading.

## Pre-Upgrade Checklist

1. **Review custom overrides** — see [Custom Overrides Inventory](#custom-overrides-inventory) below
2. **Read the changelog** — look for breaking changes, especially to files you override
3. **Commit or stash** any in-progress work so you can cleanly revert

## Upgrade Steps

```bash
# 1. Update the gem
bundle update jekyll-theme-chirpy

# 2. Build locally
bundle exec jekyll build

# 3. Run the CI smoke tests locally (same checks that run in GitHub Actions)
set -e
grep -q 'assets/js/dist/theme.min.js' _site/index.html
grep -q 'data-lqip' _site/posts/plane-collection/index.html
grep -q 'data-mode' _site/index.html
grep -q 'MathJax-script' _site/posts/ml_metrics/index.html
echo "All smoke tests passed"

# 4. Serve and manually verify
bundle exec jekyll serve
```

## What to Test

After upgrading, verify these JS-dependent features still work:

| Feature | How to verify | What breaks it |
|---------|--------------|----------------|
| Theme JS (search, sidebar, TOC) | Page loads without console errors, search works | Stale `_includes/head.html` override blocking theme scripts |
| MathJax | Open [ML Metrics](/posts/ml_metrics/) — equations render | Missing `mathjax.js` data file or broken head includes |
| LQIP placeholders | Images show blur-to-sharp transition, placeholders fill container width (not 16px) | Chirpy's `refactor-content.html` or `post.min.js` broken; `metadata-hook.html` missing `a.blur` width fix |
| Dark/light mode | Toggle works, persists on reload | `theme.min.js` not loaded, `data-mode` attribute missing |
| Clipboard (code blocks) | Click copy button on a code block | `commons.min.js` not loaded |
| Search | Type in search box, results appear | `simple-jekyll-search` CDN script missing |

## Custom Overrides Inventory

Chirpy supports two kinds of customization:

| Type | Location | Risk | Example |
|------|----------|------|---------|
| **Extension points** (safe) | `_includes/metadata-hook.html`, `_includes/custom-head.html` | Low — theme never overwrites these | Custom metadata, extra head tags |
| **Full-file overrides** (fragile) | Any `_includes/`, `_layouts/`, `_sass/` file that shadows the gem | High — theme updates won't apply | Copying `_includes/head.html` to add a script tag |

### Listing current overrides

To see which files you're overriding from the gem:

```bash
# Find the gem's installed path
THEME_PATH=$(bundle show jekyll-theme-chirpy)

# List your overrides and check if they exist in the gem
for dir in _includes _layouts _sass; do
  if [ -d "$dir" ]; then
    for file in "$dir"/*; do
      basename=$(basename "$file")
      if [ -f "$THEME_PATH/$dir/$basename" ]; then
        echo "OVERRIDE: $file (shadows $THEME_PATH/$dir/$basename)"
      else
        echo "EXTENSION: $file (no gem equivalent — safe)"
      fi
    done
  fi
done
```

Current overrides in this repo:

| File | Type | Purpose |
|------|------|---------|
| `_includes/metadata-hook.html` | Extension point | LQIP layout shift fix — forces `a.blur` and its image to `width: 100%` so 16px LQIP thumbnails fill the container instead of rendering at natural size |
| `_includes/embedded_plotly_graph.html` | Extension point | Plotly embed helper |

If you ever need to override a full file (like `head.html`), prefer using the extension points instead. If a full override is unavoidable, add it to this table and check it against the gem on every upgrade.

## Rollback

If the upgrade breaks something:

```bash
# Revert Gemfile.lock to the previous working version
git checkout HEAD~1 -- Gemfile.lock
bundle install

# Verify the rollback
bundle exec jekyll build
bundle exec jekyll serve
```
