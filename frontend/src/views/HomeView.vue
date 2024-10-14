<script setup lang="ts">
import { RouterLink } from 'vue-router';
</script>

<template>
  <main class="home">
    <!-- Hero Section -->
    <section class="hero">
      <h1 class="hero-title">Transform Your Outdoor Spaces</h1>
      <p class="hero-subtitle">
        Experience luxury landscaping tailored to fit your lifestyle.
      </p>
      <div class="cta-buttons">
        <RouterLink to="/quote" class="button primary">Get a Free Quote</RouterLink>
        <RouterLink to="/services" class="button secondary">View Services</RouterLink>
      </div>
    </section>

    <!-- Featured Services Section -->
    <section class="services">
      <h2>Our Services</h2>
      <div class="grid-3">
        <div class="grid-item">
          <h3>Lawn Care</h3>
          <p>Keep your lawn lush and healthy year-round.</p>
        </div>
        <div class="grid-item">
          <h3>Landscaping</h3>
          <p>Transform your outdoor areas into elegant spaces.</p>
        </div>
        <div class="grid-item">
          <h3>Fences & Gates</h3>
          <p>Secure and enhance your property with custom fences.</p>
        </div>
        <div class="grid-item">
          <h3>Raised Beds</h3>
          <p>Grow your own garden in style with our custom designs.</p>
        </div>
        <div class="grid-item">
          <h3>Roof & Gutters</h3>
          <p>Protect your home with quality roofing and gutter services.</p>
        </div>
      </div>
    </section>

    <!-- Testimonials Section -->
    <section class="testimonials">
      <h2>What Our Clients Say</h2>
      <div class="testimonial">
        <p>
          "The transformation of our backyard was incredible! The team brought
          our vision to life beyond our expectations."
        </p>
        <h4>– Sarah W.</h4>
      </div>
    </section>
  </main>
</template>

<style scoped>
/* Home View Styles */
.home {
  color: #e0e0e0; /* Text color for dark theme */
  background: #121212; /* Dark background */
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 3rem 1.5rem;
  font-family: 'Poppins', sans-serif; /* Modern, clean font */
}

/* Hero Section */
.hero {
  text-align: center;
  margin-bottom: 3rem;
  background: linear-gradient(to right, #1c1c1c, #2c2c2c);
  padding: 2rem;
  border-radius: 15px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
}

.hero-title {
  font-size: 3rem;
  margin-bottom: 0.5rem;
  color: #4caf50; /* Primary color for dark theme */
  animation: fadeIn 1.2s ease-in-out;
}

.hero-subtitle {
  font-size: 1.25rem;
  margin-bottom: 2rem;
  color: #b0b0b0;
  opacity: 0.85;
  animation: fadeIn 1.4s ease-in-out;
}

.cta-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
}

.button {
  padding: 0.75rem 1.5rem;
  border-radius: 30px;
  font-size: 1rem;
  text-decoration: none;
  transition: all 0.3s ease;
  cursor: pointer;
}

.primary {
  background-color: #4caf50; /* Bright primary button for dark theme */
  color: white;
}

.primary:hover {
  background-color: #81c784; /* Lighter hover effect */
}

.secondary {
  background-color: transparent;
  border: 2px solid #4caf50;
  color: #4caf50;
}

.secondary:hover {
  background-color: #4caf50;
  color: white;
}

/* Services Section */
.services {
  margin-top: 3rem;
  text-align: center;
}

.services h2 {
  font-size: 2rem;
  margin-bottom: 2rem;
  color: #e0e0e0; /* Text color for headings */
}

.grid-3 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}

.grid-item {
  background-color: #1c1c1c; /* Dark card background */
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
  transition: transform 0.3s, box-shadow 0.3s;
  text-align: center;
}

.grid-item:hover {
  transform: scale(1.05);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.5); /* More dramatic shadow on hover */
}

.grid-item h3 {
  color: #81c784; /* Accent color for headings */
}

.grid-item p {
  color: #b0b0b0; /* Lighter text for descriptions */
}

/* Testimonials Section */
.testimonials {
  margin-top: 3rem;
  text-align: center;
}

.testimonial {
  max-width: 600px;
  margin: 0 auto;
  background-color: #1c1c1c; /* Dark background for testimonials */
  padding: 1.5rem;
  border-radius: 10px;
  font-style: italic;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
}

.testimonial h4 {
  margin-top: 1rem;
  font-weight: bold;
  color: #4caf50; /* Primary color for emphasis */
}

/* Animations */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Responsive Design */
@media (max-width: 768px) {
  .hero-title {
    font-size: 2.25rem;
  }

  .grid-3 {
    grid-template-columns: 1fr;
  }

  .cta-buttons {
    flex-direction: column;
  }
}
</style>
