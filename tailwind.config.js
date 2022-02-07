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
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('tailwindcss'),
    require('autoprefixer')
  ]
}
