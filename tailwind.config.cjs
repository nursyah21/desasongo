/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}"
  ],
  theme: {
    extend: {
      colors:{
        'pale-gray':'#F3F4F6',
      },
      backgroundImage:{
        'banner': "url('/assets/banner.jpeg')"
      },
    },
  },
  plugins: [
    require('@tailwindcss/line-clamp'),
  ],
}
