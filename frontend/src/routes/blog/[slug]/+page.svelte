<script lang="ts">
  import { onMount } from 'svelte';
  import { page } from '$app/stores';
  
  // Define the BlogPost type
  interface BlogPost {
    id: number;
    title: string;
    slug: string;
    content: string;
    image: string | null;
    created_at: string;
    updated_at: string;
    published: boolean;
  }
  
  let post: BlogPost | null = null;
  let loading = true;
  let error = false;
  
  // Format date to a more readable format
  function formatDate(dateString: string): string {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  }
  
  onMount(async () => {
    try {
      const slug = $page.params.slug;
      // Replace with your actual API URL
      const response = await fetch(`http://localhost:8000/api/blog/posts/${slug}/`);
      if (!response.ok) {
        throw new Error('Failed to fetch blog post');
      }
      post = await response.json();
      loading = false;
    } catch (err) {
      console.error('Error fetching blog post:', err);
      error = true;
      loading = false;
    }
  });
</script>

<svelte:head>
  {#if post}
    <title>{post.title} | Blog</title>
  {:else}
    <title>Blog Post | Portfolio</title>
  {/if}
</svelte:head>

<main>
  {#if loading}
    <div class="container">
      <div class="loading">
        <p>Loading blog post...</p>
      </div>
    </div>
  {:else if error}
    <div class="container">
      <div class="error">
        <h1>Post Not Found</h1>
        <p>Sorry, the blog post you're looking for doesn't exist or has been removed.</p>
        <a href="/blog" class="back-link">Back to Blog</a>
      </div>
    </div>
  {:else if post}
    <article class="blog-post">
      {#if post.image}
        <div class="post-header-image">
          <img src={post.image} alt={post.title} />
        </div>
      {/if}
      
      <div class="container">
        <header class="post-header">
          <h1>{post.title}</h1>
          <div class="post-meta">
            <span class="post-date">Published on {formatDate(post.created_at)}</span>
            {#if post.updated_at !== post.created_at}
              <span class="post-updated">Updated on {formatDate(post.updated_at)}</span>
            {/if}
          </div>
        </header>
        
        <div class="post-content">
          <!-- Using {@html} to render HTML content from the backend -->
          {@html post.content}
        </div>
        
        <div class="post-footer">
          <a href="/blog" class="back-link">Back to Blog</a>
        </div>
      </div>
    </article>
  {/if}
</main>

<style>
  main {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    color: #333;
    line-height: 1.6;
  }
  
  .container {
    max-width: 800px;
    margin: 0 auto;
    padding: 0 1.5rem;
  }
  
  .loading, .error {
    text-align: center;
    padding: 5rem 0;
    font-size: 1.2rem;
    color: #555;
  }
  
  .error h1 {
    color: #e53e3e;
    margin-bottom: 1rem;
  }
  
  .post-header-image {
    width: 100%;
    height: 400px;
    overflow: hidden;
    margin-bottom: 2rem;
  }
  
  .post-header-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  
  .post-header {
    margin-bottom: 2rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid #eaeaea;
  }
  
  .post-header h1 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    color: #1a1a1a;
  }
  
  .post-meta {
    font-size: 0.9rem;
    color: #666;
  }
  
  .post-updated {
    margin-left: 1rem;
    font-style: italic;
  }
  
  .post-content {
    font-size: 1.1rem;
    line-height: 1.8;
  }
  
  .post-content p {
    margin-bottom: 1.5rem;
  }
  
  .post-content h2 {
    font-size: 1.8rem;
    margin: 2rem 0 1rem;
    color: #1a1a1a;
  }
  
  .post-content h3 {
    font-size: 1.5rem;
    margin: 1.8rem 0 1rem;
    color: #1a1a1a;
  }
  
  .post-content img {
    max-width: 100%;
    height: auto;
    border-radius: 4px;
    margin: 1.5rem 0;
  }
  
  .post-content a {
    color: #3b82f6;
    text-decoration: none;
  }
  
  .post-content a:hover {
    text-decoration: underline;
  }
  
  .post-content ul, .post-content ol {
    margin: 1.5rem 0;
    padding-left: 2rem;
  }
  
  .post-content li {
    margin-bottom: 0.5rem;
  }
  
  .post-content blockquote {
    border-left: 4px solid #3b82f6;
    padding-left: 1.5rem;
    margin: 1.5rem 0;
    font-style: italic;
    color: #555;
  }
  
  .post-content pre {
    background-color: #f8f9fa;
    padding: 1.5rem;
    border-radius: 4px;
    overflow-x: auto;
    margin: 1.5rem 0;
  }
  
  .post-content code {
    font-family: 'Fira Code', monospace;
    background-color: #f8f9fa;
    padding: 0.2rem 0.4rem;
    border-radius: 3px;
    font-size: 0.9em;
  }
  
  .post-footer {
    margin-top: 3rem;
    padding-top: 1.5rem;
    border-top: 1px solid #eaeaea;
  }
  
  .back-link {
    display: inline-block;
    color: #3b82f6;
    font-weight: 600;
    text-decoration: none;
  }
  
  .back-link:hover {
    text-decoration: underline;
  }
  
  @media (max-width: 768px) {
    .post-header h1 {
      font-size: 2rem;
    }
    
    .post-header-image {
      height: 250px;
    }
  }
</style> 