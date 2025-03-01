<script lang="ts">
  import { onMount } from 'svelte';
  
  // Set document title
  onMount(() => {
    document.title = "Mark Ortega | Portfolio";
  });
  
  // Your information
  const name = "Mark Ortega";
  const title = "Software Developer";
  
  // Form handling
  let formData = {
    name: '',
    email: '',
    message: ''
  };
  
  let formSubmitted = false;
  let formError = false;
  
  function handleSubmit() {
    // In a real application, you would send this data to your backend
    console.log('Form submitted:', formData);
    
    // Simulate form submission
    if (formData.name && formData.email && formData.message) {
      formSubmitted = true;
      formError = false;
      
      // Reset form
      formData = {
        name: '',
        email: '',
        message: ''
      };
    } else {
      formError = true;
    }
  }
</script>

<main>
  <!-- Hero Section -->
  <section class="hero">
    <div class="container">
      <div class="hero-content">
        <h1 class="hero-title">Hi, I'm {name}</h1>
        <h2 class="gradient-text">{title}</h2>
        <div class="hero-description">
          I build modern web applications with cutting-edge technologies.
          Interested in <span class="highlight-text">digital innovation</span>? Let's connect!
        </div>
        <div class="cta-buttons">
          <a href="/projects" class="btn btn-primary">View Projects</a>
          <a href="/blog" class="btn btn-outline">Read Blog</a>
        </div>
      </div>
    </div>
  </section>
  
  <!-- About Me Section -->
  <section class="about" id="about">
    <div class="container">
      <h2 class="section-title">About Me</h2>
      <div class="about-content">
        <div class="about-text">
          <p>
            I'm a passionate software developer with expertise in building web applications
            using modern technologies. With a strong foundation in both frontend and backend
            development, I create seamless, user-friendly experiences across multiple platforms and languages.
          </p>
          <p>
            My technical toolkit includes JavaScript/TypeScript, Python, C++, and Java, along with 
            experience in cloud services like AWS and deploying resources via CDK. I've worked on 
            projects ranging from small business websites to complex web applications and enterprise-level systems.
          </p>
          <p>
            My current focus is on Artificial Intelligence and its practical applications in production environments. 
            I'm particularly interested in finding innovative ways to integrate AI into large-scale codebases and databases, 
            making intelligent systems more accessible and useful for real-world applications.
          </p>
          <p>
            As an avid learner, I've been experimenting with building simple LLMs that can run locally on ARM devices 
            like the Jetson Orin for robotics applications. This blend of software development and AI exploration 
            allows me to stay at the cutting edge of technology while creating practical solutions.
          </p>
        </div>
      </div>
    </div>
  </section>
  
  <!-- Skills Section -->
  <section class="skills">
    <div class="container">
      <h2 class="section-title">Skills</h2>
      <div class="skills-content">
        <div class="skill-category">
          <h3>Languages</h3>
          <ul class="skill-list">
            <li>JavaScript/TypeScript</li>
            <li>Python</li>
            <li>C++</li>
            <li>Java</li>
            <li>HTML/CSS</li>
            <li>SQL</li>
          </ul>
        </div>
        
        <div class="skill-category">
          <h3>Frameworks</h3>
          <ul class="skill-list">
            <li>React</li>
            <li>Svelte/SvelteKit</li>
            <li>Django</li>
            <li>Express.js</li>
          </ul>
        </div>
        
        <div class="skill-category">
          <h3>Tools & Platforms</h3>
          <ul class="skill-list">
            <li>AWS Cloud Services</li>
            <li>AWS CDK</li>
            <li>Git</li>
            <li>Docker</li>
            <li>VS Code</li>
          </ul>
        </div>

        <div class="skill-category">
          <h3>AI & ML</h3>
          <ul class="skill-list">
            <li>LLM Development</li>
            <li>AI Integration</li>
            <li>Robotics (Jetson)</li>
            <li>Data Processing</li>
          </ul>
        </div>
      </div>
    </div>
  </section>
  
  <!-- Current Interests Section -->
  <section class="interests">
    <div class="container">
      <h2 class="section-title">Current Interests</h2>
      <p class="interests-intro">
        These are the technologies and concepts I'm currently exploring, ranked by my level of focus.
      </p>
      
      <div class="interests-content">
        <div class="interest-item">
          <div class="interest-rank">#1</div>
          <div class="interest-details">
            <h3>AI Integration in Production</h3>
            <div class="interest-bar">
              <div class="interest-progress" style="width: 95%;"></div>
            </div>
            <p>Developing strategies and tools to integrate AI into large-scale production systems</p>
          </div>
        </div>
        
        <div class="interest-item">
          <div class="interest-rank">#2</div>
          <div class="interest-details">
            <h3>Edge AI & Robotics</h3>
            <div class="interest-bar">
              <div class="interest-progress" style="width: 85%;"></div>
            </div>
            <p>Building lightweight LLMs for ARM devices like Jetson Orin for robotics applications</p>
          </div>
        </div>
        
        <div class="interest-item">
          <div class="interest-rank">#3</div>
          <div class="interest-details">
            <h3>Cloud Infrastructure</h3>
            <div class="interest-bar">
              <div class="interest-progress" style="width: 75%;"></div>
            </div>
            <p>Advanced AWS architectures and infrastructure as code with CDK</p>
          </div>
        </div>
        
        <div class="interest-item">
          <div class="interest-rank">#4</div>
          <div class="interest-details">
            <h3>Modern Web Development</h3>
            <div class="interest-bar">
              <div class="interest-progress" style="width: 70%;"></div>
            </div>
            <p>Exploring new frameworks and techniques for building responsive, performant web applications</p>
          </div>
        </div>
        
        <div class="interest-item">
          <div class="interest-rank">#5</div>
          <div class="interest-details">
            <h3>Low-Level Programming</h3>
            <div class="interest-bar">
              <div class="interest-progress" style="width: 65%;"></div>
            </div>
            <p>Optimizing C++ and exploring systems programming for performance-critical applications</p>
          </div>
        </div>
      </div>
    </div>
  </section>
  
  <!-- Contact Section -->
  <section class="contact" id="contact">
    <div class="container">
      <h2 class="section-title">Get In Touch</h2>
      <p class="contact-intro">
        Have a project in mind or want to chat? Feel free to reach out!
      </p>
      
      <div class="contact-content">
        <div class="contact-info">
          <div class="contact-item">
            <h3>Email</h3>
            <p><a href="mailto:your.email@example.com">your.email@example.com</a></p>
          </div>
          
          <div class="contact-item">
            <h3>Location</h3>
            <p>City, Country</p>
          </div>
          
          <div class="contact-item">
            <h3>Social</h3>
            <div class="social-links">
              <a href="https://github.com/mortega2-ops" target="_blank" rel="noopener noreferrer">GitHub</a>
              <a href="https://linkedin.com/in/yourusername" target="_blank" rel="noopener noreferrer">LinkedIn</a>
            </div>
          </div>
        </div>
        
        <div class="contact-form">
          {#if formSubmitted}
            <div class="form-success">
              <h3>Thank you for your message!</h3>
              <p>I'll get back to you as soon as possible.</p>
            </div>
          {:else}
            <form on:submit|preventDefault={handleSubmit}>
              {#if formError}
                <div class="form-error">
                  <p>Please fill out all fields.</p>
                </div>
              {/if}
              
              <div class="form-group">
                <label for="name">Name</label>
                <input 
                  type="text" 
                  id="name" 
                  bind:value={formData.name} 
                  required
                />
              </div>
              
              <div class="form-group">
                <label for="email">Email</label>
                <input 
                  type="email" 
                  id="email" 
                  bind:value={formData.email} 
                  required
                />
              </div>
              
              <div class="form-group">
                <label for="message">Message</label>
                <textarea 
                  id="message" 
                  rows="5" 
                  bind:value={formData.message} 
                  required
                ></textarea>
              </div>
              
              <button type="submit" class="btn btn-primary">Send Message</button>
            </form>
          {/if}
        </div>
      </div>
    </div>
  </section>
</main>

<style>
  main {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    color: #f0f0f0;
    line-height: 1.6;
    position: relative;
    z-index: 1;
  }
  
  section {
    padding: 5rem 0;
    position: relative;
    background-color: rgba(0, 0, 0, 0.7);
    margin: 2rem 0;
    border-radius: 8px;
    box-shadow: 0 4px 20px rgba(0, 255, 0, 0.1);
  }
  
  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1.5rem;
  }
  
  .section-title {
    font-size: 2.5rem;
    margin-bottom: 2rem;
    text-align: center;
    color: #f0f0f0;
    position: relative;
    display: inline-block;
    left: 50%;
    transform: translateX(-50%);
  }
  
  .section-title::after {
    content: '';
    position: absolute;
    bottom: -10px;
    left: 0;
    width: 100%;
    height: 3px;
    background: linear-gradient(90deg, #00ff00, #00aa00);
    border-radius: 3px;
  }
  
  /* Hero Section */
  .hero {
    background-color: rgba(0, 0, 0, 0.8);
    padding: 8rem 0;
    backdrop-filter: blur(5px);
    position: relative;
    overflow: hidden;
    border-radius: 0;
    margin-top: 0;
  }
  
  .hero::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: radial-gradient(circle at center, rgba(0, 255, 0, 0.1) 0%, rgba(0, 0, 0, 0) 70%);
    pointer-events: none;
  }
  
  .hero-content {
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
    position: relative;
    z-index: 2;
  }
  
  /* Hero title - replaced glitch effect with clean style */
  .hero-title {
    font-size: 3.5rem;
    font-weight: 800;
    color: #f0f0f0;
    margin: 0 0 0.5rem 0;
    text-shadow: 0 0 10px rgba(0, 255, 0, 0.3);
  }
  
  .gradient-text {
    font-size: 1.5rem;
    margin-bottom: 1.5rem;
    font-weight: 600;
    background: linear-gradient(90deg, #ff0000, #cc0000);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline-block;
  }
  
  .hero .hero-description {
    font-size: 1.2rem;
    margin-bottom: 2rem;
    color: #cccccc;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
  }
  
  .cta-buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
  }
  
  .btn {
    display: inline-block;
    padding: 0.75rem 1.5rem;
    border-radius: 4px;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.3s ease;
    cursor: pointer;
    border: none;
    font-size: 1rem;
  }
  
  .btn-primary {
    background: linear-gradient(90deg, #0066ff, #0044cc);
    color: white;
    box-shadow: 0 4px 6px rgba(0, 102, 255, 0.25);
  }
  
  .btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 7px 10px rgba(0, 102, 255, 0.3);
  }
  
  .btn-outline {
    background: transparent;
    color: #0066ff;
    border: 2px solid #0066ff;
  }
  
  .btn-outline:hover {
    background-color: rgba(0, 102, 255, 0.1);
    transform: translateY(-2px);
  }
  
  /* About Section */
  .about {
    background-color: rgba(0, 0, 0, 0.7);
    backdrop-filter: blur(5px);
  }
  
  .about-content {
    display: flex;
    gap: 3rem;
    align-items: center;
    max-width: 900px;
    margin: 0 auto;
  }
  
  .about-text p {
    margin-bottom: 1.5rem;
    font-size: 1.1rem;
    color: #cccccc;
  }
  
  /* Skills Section */
  .skills {
    background-color: rgba(0, 0, 0, 0.7);
    backdrop-filter: blur(5px);
  }
  
  .skills-content {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    max-width: 900px;
    margin: 0 auto;
  }
  
  .skill-category {
    background-color: rgba(0, 0, 0, 0.8);
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 255, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    backdrop-filter: blur(5px);
    border: 1px solid rgba(0, 255, 0, 0.1);
  }
  
  .skill-category:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 15px rgba(0, 255, 0, 0.2);
    border-color: rgba(0, 255, 0, 0.3);
  }
  
  .skill-category h3 {
    font-size: 1.5rem;
    margin-bottom: 1.5rem;
    color: #00ff00;
    text-align: center;
  }
  
  .skill-list {
    list-style-type: none;
    padding: 0;
  }
  
  .skill-list li {
    padding: 0.75rem 0;
    border-bottom: 1px solid rgba(0, 255, 0, 0.1);
    font-size: 1.1rem;
    color: #cccccc;
    position: relative;
    padding-left: 1.5rem;
  }
  
  .skill-list li:last-child {
    border-bottom: none;
  }
  
  .skill-list li::before {
    content: '>';
    position: absolute;
    left: 0;
    color: #00ff00;
    font-weight: bold;
  }
  
  /* Current Interests Section */
  .interests {
    background-color: rgba(0, 0, 0, 0.7);
    backdrop-filter: blur(5px);
  }
  
  .interests-intro {
    text-align: center;
    max-width: 700px;
    margin: 0 auto 3rem;
    font-size: 1.2rem;
    color: #cccccc;
  }
  
  .interests-content {
    max-width: 900px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
  }
  
  .interest-item {
    background-color: rgba(0, 0, 0, 0.8);
    border-radius: 8px;
    padding: 1.5rem;
    display: flex;
    gap: 1.5rem;
    align-items: center;
    box-shadow: 0 4px 6px rgba(0, 255, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border: 1px solid rgba(0, 255, 0, 0.1);
  }
  
  .interest-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 15px rgba(0, 255, 0, 0.2);
    border-color: rgba(0, 255, 0, 0.3);
  }
  
  .interest-rank {
    font-size: 2rem;
    font-weight: 800;
    color: #00ff00;
    text-shadow: 0 0 10px rgba(0, 255, 0, 0.3);
    min-width: 60px;
    text-align: center;
  }
  
  .interest-details {
    flex: 1;
  }
  
  .interest-details h3 {
    font-size: 1.3rem;
    margin-bottom: 0.75rem;
    color: #f0f0f0;
  }
  
  .interest-bar {
    height: 8px;
    background-color: rgba(255, 255, 255, 0.1);
    border-radius: 4px;
    margin-bottom: 1rem;
    overflow: hidden;
  }
  
  .interest-progress {
    height: 100%;
    background: linear-gradient(90deg, #00ff00, #00aa00);
    border-radius: 4px;
    box-shadow: 0 0 10px rgba(0, 255, 0, 0.5);
  }
  
  .interest-details p {
    color: #cccccc;
    font-size: 1rem;
  }
  
  @media (max-width: 768px) {
    section {
      padding: 4rem 0;
    }
    
    .hero {
      padding: 6rem 0;
    }
    
    .hero-title {
      font-size: 2.5rem;
    }
    
    .contact-content {
      grid-template-columns: 1fr;
    }
    
    .cta-buttons {
      flex-direction: column;
      gap: 1rem;
    }
    
    .cta-buttons .btn {
      width: 100%;
    }
    
    .interest-item {
      flex-direction: column;
      align-items: flex-start;
      gap: 1rem;
    }
    
    .interest-rank {
      min-width: auto;
      text-align: left;
    }
  }
  
  .highlight-text {
    color: #00ff00;
    font-weight: 600;
    text-shadow: 0 0 5px rgba(0, 255, 0, 0.5);
    position: relative;
    display: inline-block;
  }
  
  .highlight-text::after {
    content: '';
    position: absolute;
    bottom: -2px;
    left: 0;
    width: 100%;
    height: 1px;
    background-color: #00ff00;
    box-shadow: 0 0 5px rgba(0, 255, 0, 0.5);
  }

  /* Contact Section */
  .contact {
    background-color: rgba(0, 0, 0, 0.7);
    backdrop-filter: blur(5px);
  }

  .contact-intro {
    text-align: center;
    max-width: 600px;
    margin: 0 auto 3rem;
    font-size: 1.2rem;
    color: #cccccc;
  }

  .contact-content {
    display: grid;
    grid-template-columns: 1fr 1.5fr;
    gap: 3rem;
    max-width: 1000px;
    margin: 0 auto;
  }

  .contact-item {
    margin-bottom: 2rem;
  }

  .contact-item h3 {
    font-size: 1.3rem;
    margin-bottom: 0.75rem;
    color: #00ff00;
  }

  .contact-item p {
    font-size: 1.1rem;
    color: #cccccc;
  }

  .social-links {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
  }

  .social-links a {
    color: #cccccc;
    text-decoration: none;
    transition: color 0.2s ease;
  }

  .social-links a:hover {
    color: #00ff00;
  }

  .contact-form {
    background-color: rgba(0, 0, 0, 0.8);
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 255, 0, 0.1);
    backdrop-filter: blur(5px);
    border: 1px solid rgba(0, 255, 0, 0.1);
  }

  .form-group {
    margin-bottom: 1.5rem;
  }

  .form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 500;
    color: #cccccc;
  }

  .form-group input,
  .form-group textarea {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #333;
    border-radius: 4px;
    font-size: 1rem;
    font-family: inherit;
    background-color: rgba(0, 0, 0, 0.6);
    color: #f0f0f0;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
    backdrop-filter: blur(5px);
  }

  .form-group input:focus,
  .form-group textarea:focus {
    outline: none;
    border-color: #00ff00;
    box-shadow: 0 0 0 3px rgba(0, 255, 0, 0.1);
  }

  .form-success {
    text-align: center;
    padding: 2rem;
  }

  .form-success h3 {
    color: #00ff00;
    margin-bottom: 1rem;
  }

  .form-error {
    background-color: rgba(255, 0, 0, 0.2);
    color: #ff6666;
    padding: 0.75rem;
    border-radius: 4px;
    margin-bottom: 1.5rem;
    backdrop-filter: blur(5px);
  }
</style>
