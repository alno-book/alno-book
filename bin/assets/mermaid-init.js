let used_theme = localStorage.getItem("mdbook-theme");

mermaid.initialize({
    startOnLoad: true,
    theme: used_theme === 'light' || used_theme === 'rust' ? 'neutral' : 'dark',
});
