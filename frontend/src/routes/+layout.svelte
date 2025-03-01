<script lang="ts">
  import Navbar from '$lib/components/Navbar.svelte';
  import MatrixBackground from '$lib/components/MatrixBackground.svelte';
  import '../app.css';
</script>

<MatrixBackground opacity={0.2} speed={1.2} color="#00ff00" />

<Navbar />

<slot />

<footer class="footer">
  <div class="container">
    <div class="footer-content">
      <div class="footer-info">
        <h3>Tech Explorer</h3>
        <p>Discovering the digital frontier, one project at a time.</p>
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
    background-color: #000;
    color: #f0f0f0;
    position: relative;
    overflow-x: hidden;
  }
  
  :global(*) {
    box-sizing: border-box;
  }
  
  .footer {
    background-color: rgba(0, 0, 0, 0.9);
    color: #f9fafb;
    padding: 3rem 0 1.5rem;
    margin-top: 4rem;
    position: relative;
    z-index: 1;
    border-top: 1px solid rgba(0, 255, 0, 0.1);
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
    background: linear-gradient(90deg, #00ff00, #00aa00);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline-block;
  }
  
  .footer-info p {
    color: #a3a3a3;
    line-height: 1.6;
  }
  
  .footer-links h4, .footer-social h4 {
    font-size: 1.1rem;
    margin-bottom: 1rem;
    color: #f9fafb;
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
    color: #00ff00;
    text-shadow: 0 0 5px rgba(0, 255, 0, 0.5);
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