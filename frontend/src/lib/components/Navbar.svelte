<script lang="ts">
  import { page } from '$app/stores';
  import { onMount } from 'svelte';
  import GhostLogo from './GhostLogo.svelte';
  
  // Toggle mobile menu
  let isMenuOpen = false;
  let scrolled = false;
  
  function toggleMenu() {
    isMenuOpen = !isMenuOpen;
  }
  
  // Close menu when clicking on a link (mobile)
  function closeMenu() {
    isMenuOpen = false;
  }
  
  // Determine if a nav link is active
  $: isActive = (path: string) => {
    if (path === '/') {
      return $page.url.pathname === '/';
    }
    return $page.url.pathname.startsWith(path);
  };
  
  onMount(() => {
    const handleScroll = () => {
      scrolled = window.scrollY > 50;
    };
    
    window.addEventListener('scroll', handleScroll);
    
    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  });
</script>

<nav class:scrolled={scrolled}>
  <div class="container">
    <div class="navbar-content">
      <a href="/" class="logo" on:click={closeMenu} aria-label="Home">
        <GhostLogo size={45} />
      </a>
      
      <button class="menu-toggle" aria-label="Toggle menu" on:click={toggleMenu}>
        <span class="hamburger" class:open={isMenuOpen}></span>
      </button>
      
      <ul class="nav-links" class:open={isMenuOpen}>
        <li>
          <a 
            href="/" 
            class:active={isActive('/')} 
            on:click={closeMenu}
          >
            Home
          </a>
        </li>
        <li>
          <a 
            href="/projects" 
            class:active={isActive('/projects')} 
            on:click={closeMenu}
          >
            Projects
          </a>
        </li>
        <li>
          <a 
            href="/blog" 
            class:active={isActive('/blog')} 
            on:click={closeMenu}
          >
            Blog
          </a>
        </li>
        <li>
          <a 
            href="/#contact" 
            class="contact-link" 
            on:click={closeMenu}
          >
            Contact
          </a>
        </li>
      </ul>
    </div>
  </div>
</nav>

<style>
  nav {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 100;
    background-color: rgba(0, 0, 0, 0.8);
    backdrop-filter: blur(10px);
    box-shadow: 0 1px 3px rgba(0, 255, 0, 0.2);
    padding: 0.75rem 0;
    border-bottom: 1px solid rgba(0, 255, 0, 0.1);
    transition: all 0.3s ease;
  }
  
  nav.scrolled {
    background-color: rgba(0, 0, 0, 0.95);
    box-shadow: 0 2px 10px rgba(0, 255, 0, 0.2);
    padding: 0.5rem 0;
  }
  
  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1.5rem;
  }
  
  .navbar-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .logo {
    display: flex;
    align-items: center;
    text-decoration: none;
    transition: transform 0.3s ease;
  }
  
  .logo:hover {
    transform: scale(1.05);
  }
  
  .nav-links {
    display: flex;
    list-style: none;
    margin: 0;
    padding: 0;
    gap: 2rem;
  }
  
  .nav-links a {
    text-decoration: none;
    color: #cccccc;
    font-weight: 500;
    font-size: 1rem;
    transition: color 0.2s ease;
    position: relative;
    text-shadow: 0 0 5px rgba(0, 255, 0, 0.3);
  }
  
  .nav-links a:hover {
    color: #00ff00;
  }
  
  .nav-links a.active {
    color: #00ff00;
  }
  
  .nav-links a.active::after {
    content: '';
    position: absolute;
    bottom: -5px;
    left: 0;
    width: 100%;
    height: 2px;
    background-color: #00ff00;
    border-radius: 2px;
    box-shadow: 0 0 8px #00ff00;
  }
  
  .contact-link {
    background-color: rgba(0, 255, 0, 0.2);
    color: #00ff00 !important;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    transition: all 0.2s ease;
    border: 1px solid #00ff00;
  }
  
  .contact-link:hover {
    background-color: rgba(0, 255, 0, 0.3);
    box-shadow: 0 0 10px rgba(0, 255, 0, 0.5);
  }
  
  .menu-toggle {
    display: none;
    background: none;
    border: none;
    cursor: pointer;
    padding: 0.5rem;
  }
  
  .hamburger {
    display: block;
    position: relative;
    width: 24px;
    height: 2px;
    background-color: #00ff00;
    transition: all 0.3s ease-in-out;
  }
  
  .hamburger::before,
  .hamburger::after {
    content: '';
    position: absolute;
    width: 24px;
    height: 2px;
    background-color: #00ff00;
    transition: all 0.3s ease-in-out;
  }
  
  .hamburger::before {
    transform: translateY(-8px);
  }
  
  .hamburger::after {
    transform: translateY(8px);
  }
  
  .hamburger.open {
    background-color: transparent;
  }
  
  .hamburger.open::before {
    transform: rotate(45deg);
  }
  
  .hamburger.open::after {
    transform: rotate(-45deg);
  }
  
  @media (max-width: 768px) {
    .menu-toggle {
      display: block;
    }
    
    .nav-links {
      position: fixed;
      top: 70px;
      left: 0;
      right: 0;
      background-color: rgba(0, 0, 0, 0.95);
      flex-direction: column;
      align-items: center;
      padding: 2rem 0;
      gap: 1.5rem;
      box-shadow: 0 4px 6px rgba(0, 255, 0, 0.2);
      transform: translateY(-150%);
      opacity: 0;
      transition: transform 0.3s ease, opacity 0.3s ease;
      z-index: 99;
      border-bottom: 1px solid rgba(0, 255, 0, 0.1);
    }
    
    .nav-links.open {
      transform: translateY(0);
      opacity: 1;
    }
  }
</style> 