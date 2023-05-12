// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  runtimeConfig: {
    public: {
      apiBase: "https://petshop.iran.liara.run",
    },
  },
  modules: [
    "@nuxtjs/tailwindcss",
    "nuxt-swiper",
    "@vueuse/nuxt",
    "@pinia/nuxt",
    "@nuxtjs/color-mode",
    "@pinia-plugin-persistedstate/nuxt",
  ],
  app: {
    head: {
      script: [
        {
          src: "https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.5/lodash.min.js",
        },
      ],
      link: [
        {
          rel: "icon",
          href: "/img/man.png",
          type: "image/png",
        },
      ],
    },
  },
  css: ["~/assets/css/logReg.css","~/assets/css/navMobile.css"],
  colorMode: {
    classSuffix: "",
    preference: "light",
  },
  build: {
    transpile: ["vue-toastification"],
  },
});
