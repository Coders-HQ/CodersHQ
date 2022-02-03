module.exports = {
  darkMode: 'class',
  content: [
    "./codershq/templates/**/*.html",
    "./codershq/templates/*.html",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('tailwindcss'),
    require('autoprefixer')
  ]
}
