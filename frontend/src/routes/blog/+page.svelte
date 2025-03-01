<script lang="ts">
  import { onMount } from 'svelte';
  
  // Define the BlogPost type
  interface BlogPost {
    id: number;
    title: string;
    slug: string;
    summary: string;
    image: string | null;
    created_at: string;
    updated_at: string;
    published: boolean;
  }
  
  let posts: BlogPost[] = [];
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
      // Replace with your actual API URL
      const response = await fetch('http://localhost:8000/api/blog/posts/');
      if (!response.ok) {
        throw new Error('Failed to fetch blog posts');
      }
      posts = await response.json();
      loading = false;
    } catch (err) {
      console.error('Error fetching blog posts:', err);
      error = true;
      loading = false;
    }
  });
</script>

<svelte:head>
  <title>Blog | Portfolio</title>
</svelte:head>

<main>
  <section class="blog-header">
    <div class="container">
      <h1>Blog</h1>
      <p>Thoughts, ideas, and insights about technology and software development</p>
    </div>
  </section>
  
  <section class="blog-posts">
    <div class="container">
      {#if loading}
        <div class="loading">
          <p>Loading blog posts...</p>
        </div>
      {:else if error}
        <div class="error">
          <p>Failed to load blog posts. Please try again later.</p>
        </div>
      {:else if posts.length === 0}
        <div class="no-posts">
          <p>No blog posts available yet. Check back soon!</p>
        </div>
      {:else}
        <div class="posts-grid">
          {#each posts as post}
            <article class="post-card">
              {#if post.image}
                <div class="post-image">
                  <img src={post.image} alt={post.title} />
                </div>
              {/if}
              <div class="post-content">
                <h2><a href={`/blog/${post.slug}`}>{post.title}</a></h2>
                <div class="post-meta">
                  <span class="post-date">{formatDate(post.created_at)}</span>
                </div>
                <p class="post-summary">{post.summary}</p>
                <a href={`/blog/${post.slug}`} class="read-more">Read more</a>
              </div>
            </article>
          {/each}
        </div>
      {/if}
    </div>
  </section>
</main>

<style>
  main {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    color: #333;
    line-height: 1.6;
  }
  
  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1.5rem;
  }
  
  .blog-header {
    background-color: #f8f9fa;
    text-align: center;
    padding: 4rem 0;
  }
  
  .blog-header h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
    color: #1a1a1a;
  }
  
  .blog-header p {
    font-size: 1.2rem;
    max-width: 700px;
    margin: 0 auto;
    color: #555;
  }
  
  .blog-posts {
    padding: 4rem 0;
  }
  
  .loading, .error, .no-posts {
    text-align: center;
    padding: 3rem 0;
    font-size: 1.2rem;
    color: #555;
  }
  
  .error {
    color: #e53e3e;
  }
  
  .posts-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
  }
  
  .post-card {
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    background-color: white;
  }
  
  .post-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
  }
  
  .post-image {
    height: 200px;
    overflow: hidden;
  }
  
  .post-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s ease;
  }
  
  .post-card:hover .post-image img {
    transform: scale(1.05);
  }
  
  .post-content {
    padding: 1.5rem;
  }
  
  .post-content h2 {
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
  }
  
  .post-content h2 a {
    color: #1a1a1a;
    text-decoration: none;
  }
  
  .post-content h2 a:hover {
    color: #3b82f6;
  }
  
  .post-meta {
    font-size: 0.9rem;
    color: #666;
    margin-bottom: 1rem;
  }
  
  .post-summary {
    margin-bottom: 1.5rem;
    color: #555;
  }
  
  .read-more {
    display: inline-block;
    color: #3b82f6;
    font-weight: 600;
    text-decoration: none;
  }
  
  .read-more:hover {
    text-decoration: underline;
  }
  
  @media (max-width: 768px) {
    .posts-grid {
      grid-template-columns: 1fr;
    }
    
    .blog-header h1 {
      font-size: 2.5rem;
    }
  }
</style> 