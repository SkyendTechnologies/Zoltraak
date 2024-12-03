/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'zol-dark-blue-1': '#081623',    // Глубокий тёмно-синий
        'zol-dark-blue-2': '#071522',    // Более тёмный синий
        'zol-dark-blue-3': '#081522',    // Ещё один тёмно-синий
        'zol-dark-blue-4': '#081521',    // Тёмно-синий с легкой разницей
        'zol-dark-blue-5': '#081724',    // Насытно тёмный синий
        'zol-dark-blue-6': '#081622',    // Глубокий синий оттенок
        'zol-dark-blue-7': '#051320',    // Почти чёрно-синий
        'zol-gray': '#cccfd2',           // Светло-серый
        'zol-cyan': '#3dcff2',           // Яркий циан
        'zol-blue-black': '#000d1b',     // Очень тёмно-синий/чёрный
      },
      fontFamily: {
        sans: ['-zol-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'Helvetica', 'Arial', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
