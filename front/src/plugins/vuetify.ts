import Vue from 'vue'
import Vuetify from 'vuetify/lib'
import fr from 'vuetify/src/locale/fr'

Vue.use(Vuetify)

export default new Vuetify({
  theme: {
    dark: true,
    options: {
      customProperties: true,
    },
    themes: {
      dark: {
        primary: '#617be2',
        secondary: '#ffde6c',
        accent: '#ff6473',
        error: '#ff6473',
        info: '#a7baff',
        success: '#3fcc98',
        warning: '#ffde6c',
      },
    },
  },
  lang: {
    locales: { fr },
    current: 'fr',
  },
  icons: {
    iconfont: 'mdi',
  },
})
