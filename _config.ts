import lume from "lume/mod.ts";
import robots from "lume/plugins/robots.ts";

import code_highlight from "lume/plugins/code_highlight.ts";
import google_fonts from "lume/plugins/google_fonts.ts";
import toc from "https://deno.land/x/lume_markdown_plugins@v0.8.0/toc.ts";
// import { imgLazyload } from "npm:@mdit/plugin-img-lazyload";
import headerSections from 'npm:markdown-it-header-sections'

import unocss from "lume/plugins/unocss.ts";
import unoConfig from "./uno.config.ts";
import minifyHTML from "lume/plugins/minify_html.ts";
import lightningCss from "lume/plugins/lightningcss.ts";
// import terser from "lume/plugins/terser.ts";
// Does not work on GitHub Pages
// import brotli from "lume/plugins/brotli.ts";

const markdown = {
  plugins: [
    /*imgLazyload,*/
    headerSections
  ],
};
const site = lume(
  { src: "./src" },
  { markdown }
);
site.add("img");
// site.add("js");

site.use(robots({
    allow: [],
    disallow: "*"
}));

site.use(code_highlight({
  theme: {
    name: "grayscale",
    cssFile: "/highlightjs.css",
  },
}));

/*
site.use(terser(
  // {
  //   options: {
  //     module: true,
  //   },
  // }
));
*/

site.use(google_fonts({
  subsets: ["latin"],
  fonts:
    "https://fonts.google.com/share?selection.family=Figtree:ital,wght@0,300..900;1,300..900|Geist+Mono:wght@100..900|Inter+Tight:ital,wght@0,100..900;1,100..900"
}));

site.use(toc({
  slugify: {
    separator: "_",
    lowercase: true,
  },
}));

site.use(unocss({
  reset: "tailwind",
  cssFile: "./uno.css",
  // @ts-ignore invalid type
  options: unoConfig
}));

site.use(minifyHTML());
site.use(lightningCss());
// site.use(brotli());

export default site;
