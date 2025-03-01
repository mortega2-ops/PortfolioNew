import { defineConfig } from 'vitest/config';
import { svelte } from '@sveltejs/vite-plugin-svelte';

export default defineConfig({
  plugins: [svelte({ hot: !process.env.VITEST })],
  test: {
    globals: true,
    environment: 'jsdom',
    include: ['src/**/*.{test,spec}.{js,ts,svelte}'],
    coverage: {
      reporter: ['text', 'json', 'html'],
      exclude: ['**/*.d.ts', '**/*.spec.ts', '**/*.test.ts']
    }
  }
}); 