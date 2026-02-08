# scripts/main.py
"""
MkDocs Macros Plugin - Dynamic Content Injection
Permite inyectar datos en tiempo de compilación (GitHub stats, status, etc.)
"""
import os
import requests
from datetime import datetime


def define_env(env):
    """
    Hook principal para definir variables, macros y filtros.
    Se ejecuta durante el proceso 'mkdocs build'.
    """

    # =========================================================================
    # MACRO: GitHub Repository Stats
    # =========================================================================
    @env.macro
    def github_repo_stats(repo_path):
        """
        Obtiene estrellas y forks de un repositorio de GitHub.
        Maneja fallos de red silenciosamente para no romper el build.
        
        Uso en Markdown: {{ github_repo_stats('usuario/repo') }}
        """
        api_url = f"https://api.github.com/repos/{repo_path}"
        headers = {
            "Accept": "application/vnd.github.v3+json"
        }
        
        # Usar token en CI para evitar rate limits
        if "GITHUB_TOKEN" in os.environ:
            headers["Authorization"] = f"token {os.environ['GITHUB_TOKEN']}"
        
        try:
            response = requests.get(api_url, headers=headers, timeout=5)
            response.raise_for_status()
            data = response.json()
            stars = data.get('stargazers_count', 0)
            forks = data.get('forks_count', 0)
            return f'<span class="repo-stats">⭐ {stars} | 🍴 {forks}</span>'
        except Exception as e:
            print(f"⚠️ Error al obtener stats para {repo_path}: {e}")
            return '<span class="repo-stats-error">Stats no disponibles</span>'

    # =========================================================================
    # MACRO: Current Year (for footer)
    # =========================================================================
    @env.macro
    def current_year():
        """
        Devuelve el año actual.
        
        Uso en Markdown: {{ current_year() }}
        """
        return datetime.now().year

    # =========================================================================
    # MACRO: Skills Grid
    # =========================================================================
    @env.macro
    def skill_badge(name):
        """
        Genera un badge de skill.
        
        Uso en Markdown: {{ skill_badge('Kubernetes') }}
        """
        return f'<span class="skill-badge">{name}</span>'

    @env.macro
    def skills_grid(skills_list):
        """
        Genera un grid de skills.
        
        Uso: {{ skills_grid(['Kubernetes', 'Terraform', 'ArgoCD']) }}
        """
        badges = ''.join([f'<span class="skill-badge">{s}</span>' for s in skills_list])
        return f'<div class="skills-grid">{badges}</div>'

    # =========================================================================
    # MACRO: Last Build Time
    # =========================================================================
    @env.macro
    def build_time():
        """
        Devuelve la fecha y hora del último build.
        
        Uso: {{ build_time() }}
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M UTC")
