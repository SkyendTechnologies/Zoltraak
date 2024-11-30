

module.exports = {
    content: [
        "./index.html",
        "./src/**/*.{vue,js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                'skyend-cyan': '#26DDF3',       // Яркий голубой (Bright Cyan)
                'skyend-dark-indigo': '#141D5C',// Тёмный индиго (Dark Indigo)
                'skyend-light-blue': '#3FACE6', // Светло-голубой (Light Blue)
                'skyend-light-cyan': '#2882D8', // Светло-циан (Light Cyan)
                'skyend-very-light-cyan': '#92E9F2', // Очень светлый циан (Very Light Cyan)
                'skyend-very-dark-blue': '#080C49', // Очень тёмно-синий (Very Dark Blue)
                'skyend-medium-blue': '#2060D5', // Средний синий (Medium Blue)
                'skyend-dark-cyan': '#1384D3',   // Тёмный циан (Dark Cyan)
                'skyend-light-cyan-2': '#40A2D8', // Светло-циан 2 (Light Cyan 2)
                'skyend-gray': {
                    100: '#F2F2F7',  // Светло-серый (Light Gray)
                    200: '#E5E5EA',  // Светло-серый 2 (Light Gray 2)
                    300: '#D1D1D6',  // Светло-серый 3 (Light Gray 3)
                    400: '#C7C7CC',  // Светло-серый 4 (Light Gray 4)
                    500: '#AEAEB2',  // Средний серый (Medium Gray)
                    600: '#8E8E93',  // Средний серый 2 (Medium Gray 2)
                    700: '#636366',  // Тёмно-серый (Dark Gray)
                    800: '#48484A',  // Тёмно-серый 2 (Dark Gray 2)
                    900: '#3A3A3C',  // Тёмно-серый 3 (Dark Gray 3)
                },
                'skyend-black': '#000000',     // Чёрный (Black)
                'skyend-white': '#FFFFFF',     // Белый (White)
                'skyend-light-gray': '#F2F2F7', // Светло-серый (Light Gray)
            },
            fontFamily: {
                sans: ['-skyend-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'Helvetica', 'Arial', 'sans-serif'],
            },
        },
    },
    plugins: [],
}
