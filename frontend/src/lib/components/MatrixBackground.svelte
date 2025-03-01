<script lang="ts">
  import { onMount, onDestroy } from 'svelte';
  
  // Props for customization
  export let opacity = 0.15;  // Increased opacity for better visibility
  export let speed = 1.5;     // Animation speed multiplier
  export let density = 1.0;   // Character density (0-1)
  export let color = '#00ff00'; // Classic Matrix green
  
  let canvas: HTMLCanvasElement;
  let ctx: CanvasRenderingContext2D;
  let animationId: number;
  let columns: number[] = [];
  let fontSize = 14;
  
  // Matrix characters (mix of letters, numbers, and symbols)
  const matrixChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789<>[]{}|/\\+=_-!@#$%^&*()~`';
  
  // Initialize the canvas and start animation
  onMount(() => {
    if (!canvas) return;
    
    ctx = canvas.getContext('2d')!;
    
    // Set canvas to full window size
    const resizeCanvas = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
      
      // Calculate columns based on font size
      const columnCount = Math.floor(canvas.width / fontSize);
      columns = [];
      
      // Initialize drop positions for each column
      for (let i = 0; i < columnCount; i++) {
        // Only create a column based on density
        if (Math.random() < density) {
          columns[i] = Math.random() * -canvas.height;
        }
      }
    };
    
    // Handle window resize
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();
    
    // Start the animation
    startMatrixAnimation();
    
    return () => {
      window.removeEventListener('resize', resizeCanvas);
      if (animationId) {
        cancelAnimationFrame(animationId);
      }
    };
  });
  
  onDestroy(() => {
    if (animationId) {
      cancelAnimationFrame(animationId);
    }
  });
  
  // Matrix animation function
  function startMatrixAnimation() {
    // Animation loop
    function animate() {
      // Black background with slight transparency for trail effect
      ctx.fillStyle = `rgba(0, 0, 0, ${0.1 / speed})`;
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      
      // Draw characters
      for (let i = 0; i < columns.length; i++) {
        if (columns[i] === undefined) continue;
        
        // Get random character
        const char = matrixChars[Math.floor(Math.random() * matrixChars.length)];
        
        // Calculate x position
        const x = i * fontSize;
        
        // Calculate y position
        const y = columns[i];
        
        // Vary the color brightness for a more dynamic effect
        // First character is brighter (white-ish) for the "head" of each column
        if (y > 0 && y < fontSize) {
          ctx.fillStyle = '#ffffff';
        } else {
          // Random brightness variation for the green color
          const brightness = Math.random() * 0.5 + 0.5; // 0.5 to 1.0
          ctx.fillStyle = `rgba(0, ${Math.floor(255 * brightness)}, 0, 0.8)`;
        }
        
        ctx.font = `${fontSize}px monospace`;
        
        // Draw the character
        ctx.fillText(char, x, y);
        
        // Move the character down
        columns[i] += fontSize * speed * (0.5 + Math.random() * 0.5);
        
        // Reset if off screen or randomly
        if (y > canvas.height && Math.random() > 0.975) {
          columns[i] = 0;
        } else if (y > canvas.height + 10000) {
          // Hard reset if it's way off screen (safety)
          columns[i] = 0;
        }
        
        // Randomly reset some columns for varied effect
        if (Math.random() > 0.995) {
          columns[i] = 0;
        }
      }
      
      // Continue animation
      animationId = requestAnimationFrame(animate);
    }
    
    // Start the animation loop
    animate();
  }
</script>

<canvas 
  bind:this={canvas} 
  class="matrix-background"
  style="opacity: {opacity};"
></canvas>

<style>
  .matrix-background {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    pointer-events: none;
    background-color: #000;
  }
</style> 