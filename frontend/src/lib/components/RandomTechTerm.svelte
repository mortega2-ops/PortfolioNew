<script lang="ts">
  import { onMount } from 'svelte';
  import { getRandomTerm, generateSearchUrl } from '../utils/techTerms.js';
  
  // Add a prop to determine if this should be a link or just text
  export let asLink = true;
  
  let randomTerm = { term: '', category: '' };
  let isLoaded = false;
  let tooltipVisible = false;
  
  // Generate a new random term
  function refreshTerm() {
    randomTerm = getRandomTerm();
  }
  
  // Show tooltip
  function showTooltip() {
    tooltipVisible = true;
  }
  
  // Hide tooltip
  function hideTooltip() {
    tooltipVisible = false;
  }
  
  // Initialize on component mount
  onMount(() => {
    refreshTerm();
    isLoaded = true;
  });
</script>

<div class="random-term-container">
  {#if asLink}
    <a 
      href={generateSearchUrl(randomTerm.term)} 
      target="_blank" 
      rel="noopener noreferrer"
      class="random-term"
      class:loaded={isLoaded}
      on:click={() => refreshTerm()}
      on:mouseenter={showTooltip}
      on:mouseleave={hideTooltip}
      aria-label={`Search for ${randomTerm.term}`}
    >
      {randomTerm.term}
      <span class="term-highlight"></span>
    </a>
  {:else}
    <span
      class="random-term"
      class:loaded={isLoaded}
      on:mouseenter={showTooltip}
      on:mouseleave={hideTooltip}
      role="button"
      tabindex="0"
    >
      {randomTerm.term}
      <span class="term-highlight"></span>
    </span>
  {/if}
  
  {#if tooltipVisible}
    <div class="tooltip" class:visible={tooltipVisible}>
      <span class="category">{randomTerm.category.replace(/([A-Z])/g, ' $1').trim()}</span>
      <span class="info">Click to search • Refreshes on each visit</span>
    </div>
  {/if}
</div>

<style>
  .random-term-container {
    position: relative;
    display: inline-block;
  }
  
  .random-term {
    position: relative;
    font-size: 1.5rem;
    font-weight: 700;
    color: #1a1a1a;
    text-decoration: none;
    cursor: pointer;
    transition: color 0.3s ease;
    overflow: hidden;
    display: inline-block;
    opacity: 0;
    transform: translateY(10px);
  }
  
  .random-term.loaded {
    opacity: 1;
    transform: translateY(0);
    transition: opacity 0.5s ease, transform 0.5s ease;
  }
  
  .random-term:hover {
    color: #3b82f6;
  }
  
  .term-highlight {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 2px;
    background-color: #3b82f6;
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.3s ease;
  }
  
  .random-term:hover .term-highlight {
    transform: scaleX(1);
  }
  
  .tooltip {
    position: absolute;
    top: calc(100% + 10px);
    left: 50%;
    transform: translateX(-50%) translateY(-10px);
    background-color: #1a1a1a;
    color: white;
    padding: 0.75rem 1rem;
    border-radius: 6px;
    font-size: 0.875rem;
    white-space: nowrap;
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.2s ease, transform 0.2s ease;
    z-index: 100;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .tooltip::before {
    content: '';
    position: absolute;
    top: -6px;
    left: 50%;
    transform: translateX(-50%);
    border-width: 0 6px 6px 6px;
    border-style: solid;
    border-color: transparent transparent #1a1a1a transparent;
  }
  
  .tooltip.visible {
    opacity: 1;
    transform: translateX(-50%) translateY(0);
  }
  
  .category {
    font-weight: 600;
    color: #3b82f6;
    margin-bottom: 0.25rem;
    text-transform: capitalize;
  }
  
  .info {
    font-size: 0.75rem;
    color: #a3a3a3;
  }
  
  @media (max-width: 768px) {
    .tooltip {
      display: none;
    }
  }
</style> 