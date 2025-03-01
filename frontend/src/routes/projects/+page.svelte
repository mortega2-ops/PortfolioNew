<script lang="ts">
  import { onMount } from 'svelte';
  
  // Define the Project type
  interface Project {
    id: number;
    title: string;
    description: string;
    image: string;
    technologies: string[];
    github_url: string | null;
    live_url: string | null;
  }
  
  // Sample projects data (in a real app, this would come from an API)
  let projects: Project[] = [
    {
      id: 1,
      title: "Portfolio Website",
      description: "A personal portfolio website built with Django and SvelteKit to showcase my projects and blog posts.",
      image: "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80",
      technologies: ["Django", "SvelteKit", "TypeScript", "SQLite"],
      github_url: "https://github.com/yourusername/portfolio",
      live_url: "https://yourportfolio.com"
    },
    {
      id: 2,
      title: "E-commerce Platform",
      description: "A full-featured e-commerce platform with product catalog, shopping cart, and payment processing.",
      image: "https://images.unsplash.com/photo-1563013544-824ae1b704d3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80",
      technologies: ["React", "Node.js", "Express", "MongoDB"],
      github_url: "https://github.com/yourusername/ecommerce",
      live_url: null
    },
    {
      id: 3,
      title: "Weather App",
      description: "A weather application that provides real-time weather data and forecasts for locations worldwide.",
      image: "https://images.unsplash.com/photo-1592210454359-9043f067919b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80",
      technologies: ["JavaScript", "OpenWeather API", "HTML", "CSS"],
      github_url: "https://github.com/yourusername/weather-app",
      live_url: "https://yourweatherapp.com"
    }
  ];
  
  let loading = true;
  
  onMount(() => {
    // Simulate loading data from an API
    setTimeout(() => {
      loading = false;
    }, 500);
    
    // In a real application, you would fetch projects from your API:
    // async function fetchProjects() {
    //   try {
    //     const response = await fetch('http://localhost:8000/api/projects/');
    //     if (!response.ok) {
    //       throw new Error('Failed to fetch projects');
    //     }
    //     projects = await response.json();
    //   } catch (err) {
    //     console.error('Error fetching projects:', err);
    //   } finally {
    //     loading = false;
    //   }
    // }
    // fetchProjects();
  });
</script>

<svelte:head>
  <title>Projects | Portfolio</title>
</svelte:head>

<main>
  <div class="container">
    <header class="projects-header">
      <h1>My Projects</h1>
      <p>Here are some of the projects I've worked on. Each project represents a unique challenge and learning experience.</p>
    </header>
    
    {#if loading}
      <div class="loading">
        <p>Loading projects...</p>
      </div>
    {:else}
      <div class="projects-grid">
        {#each projects as project (project.id)}
          <div class="project-card">
            <div class="project-image">
              <img src={project.image} alt={project.title} />
            </div>
            <div class="project-content">
              <h2>{project.title}</h2>
              <p class="project-description">{project.description}</p>
              <div class="project-tech">
                {#each project.technologies as tech}
                  <span class="tech-tag">{tech}</span>
                {/each}
              </div>
              <div class="project-links">
                {#if project.github_url}
                  <a href={project.github_url} target="_blank" rel="noopener noreferrer" class="project-link github">
                    GitHub
                  </a>
                {/if}
                {#if project.live_url}
                  <a href={project.live_url} target="_blank" rel="noopener noreferrer" class="project-link live">
                    Live Demo
                  </a>
                {/if}
              </div>
            </div>
          </div>
        {/each}
      </div>
    {/if}
  </div>
</main>

<style>
  main {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    color: #333;
    line-height: 1.6;
    padding: 2rem 0;
  }
  
  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1.5rem;
  }
  
  .projects-header {
    text-align: center;
    margin-bottom: 3rem;
  }
  
  .projects-header h1 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    color: #1a1a1a;
  }
  
  .projects-header p {
    font-size: 1.1rem;
    color: #555;
    max-width: 700px;
    margin: 0 auto;
  }
  
  .loading {
    text-align: center;
    padding: 5rem 0;
    font-size: 1.2rem;
    color: #555;
  }
  
  .projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 2rem;
  }
  
  .project-card {
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    background-color: #fff;
  }
  
  .project-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
  }
  
  .project-image {
    height: 200px;
    overflow: hidden;
  }
  
  .project-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
  }
  
  .project-card:hover .project-image img {
    transform: scale(1.05);
  }
  
  .project-content {
    padding: 1.5rem;
  }
  
  .project-content h2 {
    font-size: 1.5rem;
    margin-bottom: 0.75rem;
    color: #1a1a1a;
  }
  
  .project-description {
    color: #555;
    margin-bottom: 1rem;
    line-height: 1.5;
  }
  
  .project-tech {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
  }
  
  .tech-tag {
    background-color: #f0f4f8;
    color: #0066ff;
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 500;
  }
  
  .project-links {
    display: flex;
    gap: 1rem;
  }
  
  .project-link {
    display: inline-block;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    font-weight: 600;
    text-decoration: none;
    transition: background-color 0.2s ease;
  }
  
  .project-link.github {
    background-color: #24292e;
    color: #fff;
  }
  
  .project-link.github:hover {
    background-color: #1b1f23;
  }
  
  .project-link.live {
    background-color: #0066ff;
    color: #fff;
  }
  
  .project-link.live:hover {
    background-color: #0044cc;
  }
  
  @media (max-width: 768px) {
    .projects-grid {
      grid-template-columns: 1fr;
    }
    
    .projects-header h1 {
      font-size: 2rem;
    }
  }
</style> 