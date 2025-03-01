<script lang="ts">
  import Navbar from '$lib/components/Navbar.svelte';
  import '../app.css';
</script>

<Navbar />

<slot />

<footer class="footer">
  <div class="container">
    <div class="footer-content">
      <div class="footer-info">
        <h3>Portfolio</h3>
        <p>A showcase of my projects and blog posts.</p>
      </div>
      
      <div class="footer-links">
        <h4>Quick Links</h4>
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="/projects">Projects</a></li>
          <li><a href="/blog">Blog</a></li>
          <li><a href="/#contact">Contact</a></li>
        </ul>
      </div>
      
      <div class="footer-social">
        <h4>Connect</h4>
        <div class="social-links">
          <a href="https://github.com/yourusername" target="_blank" rel="noopener noreferrer" aria-label="GitHub">
            GitHub
          </a>
          <a href="https://linkedin.com/in/yourusername" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">
            LinkedIn
          </a>
          <a href="https://twitter.com/yourusername" target="_blank" rel="noopener noreferrer" aria-label="Twitter">
            Twitter
          </a>
        </div>
      </div>
    </div>
    
    <div class="footer-bottom">
      <p>&copy; {new Date().getFullYear()} Your Name. All rights reserved.</p>
    </div>
  </div>
</footer>

<style>
  :global(body) {
    margin: 0;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    background-color: #f9fafb;
    color: #333;
  }
  
  :global(*) {
    box-sizing: border-box;
  }
  
  .footer {
    background-color: #1a1a1a;
    color: #f9fafb;
    padding: 3rem 0 1.5rem;
    margin-top: 4rem;
  }
  
  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1.5rem;
  }
  
  .footer-content {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    margin-bottom: 2rem;
  }
  
  .footer-info h3 {
    font-size: 1.5rem;
    margin-bottom: 1rem;
  }
  
  .footer-info p {
    color: #a3a3a3;
    line-height: 1.6;
  }
  
  .footer-links h4, .footer-social h4 {
    font-size: 1.1rem;
    margin-bottom: 1rem;
  }
  
  .footer-links ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .footer-links li {
    margin-bottom: 0.75rem;
  }
  
  .footer-links a, .social-links a {
    color: #a3a3a3;
    text-decoration: none;
    transition: color 0.2s ease;
  }
  
  .footer-links a:hover, .social-links a:hover {
    color: #3b82f6;
  }
  
  .social-links {
    display: flex;
    gap: 1rem;
  }
  
  .footer-bottom {
    border-top: 1px solid #333;
    padding-top: 1.5rem;
    text-align: center;
    color: #a3a3a3;
    font-size: 0.9rem;
  }
  
  @media (max-width: 768px) {
    .footer-content {
      grid-template-columns: 1fr;
    }
    
    .social-links {
      flex-direction: column;
      gap: 0.75rem;
    }
  }
</style> 