/// <reference types="vite/client" />

// Declare any environment variables your project needs, prefixed with `VITE_`
interface ImportMetaEnv {
    readonly VITE_APP_BASE_URL: string; // Base URL for your API or backend server
    readonly VITE_APP_TITLE?: string; // Title of the app (optional)
    readonly VITE_API_KEY?: string; // API Key for external services (optional)
    readonly VITE_ENVIRONMENT?: string; // Environment type (e.g., development, production)
    // Add more variables as needed and be sure to prefix them with VITE_
  }
  
  interface ImportMeta {
    readonly env: ImportMetaEnv;
  }
  