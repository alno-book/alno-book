let used_theme_pseudocode = localStorage.getItem("mdbook-theme");
if (
    used_theme_pseudocode === 'navy'
    || used_theme_pseudocode === 'ayu'
    || used_theme_pseudocode == 'coal') {
    $('.pseudocode').pseudocode({
        keywords: {
            // green
            'max': '#008200',
            'min': '#008200',
            'true': '#008200',
            'false': '#008200',
            // yellow
            'for': '#e5c07b',
            'in': '#e5c07b',
            'return': '#e5c07b',
            'if': '#e5c07b',
            'then': '#e5c07b',
            'else': '#e5c07b',
            'elif': '#e5c07b',
            'var': '#e5c07b',
            'while': '#e5c07b',
            'foreach': '#e5c07b',
            'not': '#e5c07b',
            'do': '#e5c07b',
            // light blue
            'function': '#52adf2',
            // light red
            'structure': '#e25b51',
            'attributes:': '#e25b51',
            'methods:': '#e25b51',
            'this': '#e25b51',
        }
    });
} else {
    $('.pseudocode').pseudocode({
        keywords: {
            // red
            'max': '#b8212f',
            'min': '#b8212f',
            'true': '#b8212f',
            'false': '#b8212f',
            // purple
            'for': '#a42fa2',
            'in': '#a42fa2',
            'return': '#a42fa2',
            'if': '#a42fa2',
            'then': '#a42fa2',
            'else': '#a42fa2',
            'elif': '#a42fa2',
            'var': '#a42fa2',
            'while': '#a42fa2',
            'foreach': '#a42fa2',
            'not': '#a42fa2',
            'do': '#a42fa2',
            // light blue
            'function': '#1485ba',
            'this': '#1485ba',
            'structure': '#1485ba',
            'attributes:': '#1485ba',
            'methods:': '#1485ba',
        }
    });
}
