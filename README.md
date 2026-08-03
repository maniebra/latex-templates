# latex-templates

LaTeX templates I use, each in an English and a Persian version.

```
en/  fa/
├── notebook-template        book class, for long notes
├── slide-template           beamer, for lectures
├── assignment-template-1    article, for homework handouts
└── student-solution         article, for answering one of those
                             (notebook typography, monochrome)
```

## Build

```sh
cd en/notebook-template
latexmk -xelatex -shell-escape main.tex
```

- `-shell-escape` is for the notebook and solution templates, which use minted.
- The `fa/` ones need XeLaTeX. There is no LuaLaTeX build for them.
- Run twice. Some backgrounds are placed with `remember picture`.

## Layout

Same in every template:

```
main.tex        packages and inputs
vars/meta.tex   title, author, date
vars/colors.tex the palette
styles/         one file per concern
sections/       the writing
fonts/          loaded by path, nothing to install
```

The files in `sections/` are demos. Delete them and write your own.

## Persian

- `\lr{...}` for Latin inside Persian, `\rl{...}` for Persian inside an LTR
  box such as a TikZ node.
- Numbers like 4.1 flip in RTL. Use `\nbnum` (notebook), `\hwnum`
  (assignment), or `\solnum` (solution), and `\SepMark{-}` so the number doesn't read as a decimal.
- Don't add microtype. Its protrusion breaks Persian letter joining.

## Licence

MIT, see [LICENSE](LICENSE). The bundled fonts are not mine and have their own
terms.
