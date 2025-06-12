import {
  defineConfig,
  presetAttributify,
  presetIcons,
  // presetTypography,
  // presetWebFonts,
  presetWind3,
  transformerDirectives,
  // transformerVariantGroup
} from 'unocss'

export default defineConfig({
  presets: [
    presetWind3(),
    presetAttributify(),
    presetIcons(),
    // presetTypography(),
  //   presetWebFonts({
  //     fonts: {
  //       // ...
  //     },
  //   }),
  ],
  transformers: [
    transformerDirectives(),
  //   transformerVariantGroup(),
  ],
});
