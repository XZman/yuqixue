# yuqixue.com

Personal academic website for Yuqi Xue, ECE Ph.D. candidate at UIUC.

Built with [HugoBlox](https://github.com/HugoBlox/kit) (Hugo Academic CV theme).

## Local development

```bash
# Install dependencies
pnpm install

# Run dev server
hugo server
```

Requires [Hugo Extended](https://gohugo.io/installation/) ≥ 0.161.0 and Node.js 22+.

## Editing

- Profile / bio / experience / awards: `data/authors/me.yaml`
- Site identity / theme: `config/_default/params.yaml`
- Homepage layout: `content/_index.md`
- Experience page layout: `content/experience.md`
- Publications: `content/publications/<slug>/index.md`
- Navigation: `config/_default/menus.yaml`
- CV PDF: `static/uploads/yuqixue_cv.pdf`
- Paper PDFs: `static/pdf/`
- Profile photo: `assets/media/authors/me.png`
