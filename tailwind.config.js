module.exports = {
  content: [
    "./codershq/static/**/*.js",
    "./codershq/templates/**/*.html",
    "./codershq/templates/*.html",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('tailwindcss'),
    require('autoprefixer')
  ],
}
