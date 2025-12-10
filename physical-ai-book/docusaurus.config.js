// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

import { themes as prismThemes } from 'prism-react-renderer';

const config = {
  // --- Site Metadata (Required Fields) ---
  title: 'Physical AI & Humanoid Robotics: The VLA Stack', // Book Title
  tagline: 'Mastering ROS 2, NVIDIA Isaac, and GPT Integration for Embodied Intelligence.',
  url: 'https://localhost:3000', // Changed for local testing
  baseUrl: '/', // Site is deployed to the root of the domain

  // --- Deployment Configuration (Used later for T-012) ---
  projectName: 'physical-ai-book', // Usually your repo name.
  organizationName: 'your-organization', // Usually your GitHub org/username.

  // --- Build Settings ---
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',

  // --- Localization ---
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  // --- Presets (Using the Classic preset) ---
  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          // Set a basic 'edit this page' link to encourage contributions
          editUrl: 'https://localhost:3000/tree/main/', // Changed for local testing
          routeBasePath: '/', // Serve the docs at the site's root
          sidebarCollapsed: false,
        },
        blog: false, // Disable the blog feature, as it's not needed for the book
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  // --- Theme Configuration (Styling and Navbar) ---
  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card image
      image: 'img/social-card.png', 
      navbar: {
        title: 'Physical AI Book',
        logo: {
          alt: 'Physical AI Book Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Modules (1-4)',
          },
          {
            href: 'https://github.com/your-username/physical-ai-book',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        copyright: `Copyright © ${new Date().getFullYear()} Physical AI Book Project. Built with Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
        // Add all relevant languages for robotics and AI
        additionalLanguages: ['python', 'bash', 'json', 'yaml', 'cpp'],
      },
      // --- Placeholder for the RAG Chatbot Search (T-019) ---
      // We will add the actual client-side search plugin later if needed, 
      // but for now, we leave the standard search bar.
    }),
};

export default config;
