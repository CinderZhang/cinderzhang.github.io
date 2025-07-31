import { defineConfig } from 'vite'

export default defineConfig({
  server: {
    fs: {
      // Allow serving files from Monaco Editor
      allow: [
        '..',
        '../../node_modules'
      ]
    }
  }
})