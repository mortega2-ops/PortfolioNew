<script lang="ts">
  import { onMount, onDestroy } from 'svelte';
  
  // Props for customization
  export let opacity = 0.15;  // Increased opacity for better visibility
  export let speed = 0.8;     // Reduced speed for slower animation
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
    // Keep track of characters for each column
    let columnChars: string[][] = [];
    
    // Animation loop
    function animate() {
      // Completely black background with no transparency
      ctx.fillStyle = 'rgba(0, 0, 0, 1)';
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      
      // Draw characters
      for (let i = 0; i < columns.length; i++) {
        if (columns[i] === undefined) continue;
        
        // Initialize character array for this column if needed
        if (!columnChars[i]) {
          columnChars[i] = [];
          // Fill with initial characters
          for (let j = 0; j < 20; j++) {
            columnChars[i].push(matrixChars[Math.floor(Math.random() * matrixChars.length)]);
          }
        }
        
        // Occasionally change a character but not every frame (reduced frequency)
        if (Math.random() > 0.95) {
          // Update the first character (head of the column)
          columnChars[i][0] = matrixChars[Math.floor(Math.random() * matrixChars.length)];
        }
        
        // Calculate y position
        const y = columns[i];
        
        // Draw each character in the column
        for (let j = 0; j < columnChars[i].length; j++) {
          // Calculate position for this character
          const charY = y - (j * fontSize);
          
          // Only draw if on screen
          if (charY < -fontSize || charY > canvas.height) continue;
          
          // Calculate x position
          const x = i * fontSize;
          
          // Get the character
          const char = columnChars[i][j];
          
          // Vary the color brightness based on position in the column
          const colorValues = hexToRgb(color);
          if (!colorValues) continue;
          
          // Reset shadow
          ctx.shadowBlur = 0;
          
          // First character (head of the column)
          if (j === 0) {
            // Bright white for the head with subtle glow
            ctx.fillStyle = '#ffffff';
            ctx.shadowColor = color;
            ctx.shadowBlur = 3; // Reduced glow
          } else {
            // Fade out based on position in the column - more gradual fade
            const fadeRatio = Math.min(1, j / 20); // 0 to 1 (extended range)
            const brightness = 1 - (fadeRatio * 0.8); // 1.0 to 0.2
            
            // More stable opacity that doesn't flash
            const opacity = Math.max(0.1, 1 - (fadeRatio * 0.9));
            
            ctx.fillStyle = `rgba(${colorValues.r * brightness}, ${colorValues.g * brightness}, ${colorValues.b * brightness}, ${opacity})`;
          }
          
          ctx.font = `${fontSize}px monospace`;
          
          // Draw the character
          ctx.fillText(char, x, charY);
        }
        
        // Move the column down at a very consistent speed
        columns[i] += fontSize * speed * 0.25; // Reduced and more consistent speed
        
        // Reset if off screen
        if (y > canvas.height + (fontSize * 20)) {
          columns[i] = 0;
          // Generate new characters
          columnChars[i] = [];
          for (let j = 0; j < 20; j++) {
            columnChars[i].push(matrixChars[Math.floor(Math.random() * matrixChars.length)]);
          }
        }
        
        // Randomly reset some columns for varied effect (extremely rarely)
        if (Math.random() > 0.999) {
          columns[i] = 0;
          columnChars[i] = [];
        }
      }
      
      // Continue animation
      animationId = requestAnimationFrame(animate);
    }
    
    // Start the animation loop
    animate();
  }
  
  // Helper function to convert hex color to RGB
  function hexToRgb(hex: string) {
    const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? {
      r: parseInt(result[1], 16),
      g: parseInt(result[2], 16),
      b: parseInt(result[3], 16)
    } : null;
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