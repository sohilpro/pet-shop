/** @type {import('tailwindcss').Config} */
module.exports = {
  // content: [
  //   "./components/**/*.{js,vue,ts}",
  //   "./layouts/**/*.vue",
  //   "./pages/**/*.vue",
  //   "./plugins/**/*.{js,ts}",
  //   "./nuxt.config.{js,ts}",
  //   "./node_modules/flowbite.{js,ts}"
  // ],
  content: [
    "node_modules/flowbite-vue/**/*.{js,jsx,ts,tsx}",
    "node_modules/flowbite/**/*.{js,jsx,ts,tsx}",
  ],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        custom: "rgb(41, 0, 75)",
      },
      backgroundImage: {
        'product-white': "url('/img/bg-products-pg-white.jpg')",
        'product-black': "url('/img/bg-products-pg-black.jpg')",
      },
    },
  },
  // plugins: [require("flowbite")],
  plugins: [require("flowbite/plugin")],
};
