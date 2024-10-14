<template>
  <div class="services">
    <h1>Our Premium Services</h1>
    <div class="service-cards">
      <div v-for="service in services" :key="service.title" class="service-card">
        <h2>{{ service.title }}</h2>
        <p>{{ service.description }}</p>
      </div>
    </div>
    <footer class="contact-info">
      <h3>Contact Us</h3>
      <div class="contact-details">
        <p><strong>Owner:</strong> Steven Acrocco</p>
        <p><strong>Email:</strong> <a href="mailto:TLLG24@Yahoo.com">TLLG24@Yahoo.com</a></p>
        <p><strong>Phone:</strong> <a href="tel:+17134463057">(713) 446-3057</a></p>
        <p><strong>Location:</strong> Brazos Valley & Houston, Texas</p>
        <p><em>Proudly Aggie owned and operated.</em></p>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
const services = [
  { title: 'Free Estimates', description: 'Get a free estimate for your landscaping needs.' },
  { title: 'Lawn & Landscaping Maintenance', description: 'Keep your lawn healthy and beautiful year-round.' },
  { title: 'Raised Bed Installation', description: 'Install elegant raised beds to enhance your garden.' },
  { title: 'Roof/Gutter Clean-up', description: 'Ensure your roof and gutters stay clear and functional.' },
  { title: 'Hedge Trimming', description: 'Precise trimming to keep your hedges in shape.' },
  { title: 'Mulching', description: 'Improve soil health and enhance aesthetics with professional mulching.' },
  { title: 'Fertilizing', description: 'Optimize lawn growth with our fertilizing services.' },
  { title: 'Sodding', description: 'Install fresh sod for instant results.' },
  { title: 'Debris & Weed Removal', description: 'Keep your landscape clean and weed-free.' },
  { title: 'Firepit Creation', description: 'Add a cozy firepit for outdoor enjoyment.' },
  { title: 'Fence Installation & Repair', description: 'Install or repair fences to secure your property.' },
  { title: 'Herbicide Application', description: 'Professional herbicide application for weed control.' },
  { title: 'Painting', description: 'Quality painting for fences, walls, and exteriors.' },
  { title: 'Handyman Work', description: 'General handyman services for all your needs.' },
  { title: 'Advertising', description: 'Promote your business with our advertising services.' },
];
</script>

<style scoped>
.services {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
  background-color: #0d0d0d;
  color: #f0f0f0;
  font-family: 'Poppins', sans-serif;
}

h1 {
  font-size: 2.5rem;
  margin-bottom: 2rem;
  color: #4caf50;
}

.service-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  width: 100%;
  max-width: 1200px;
}

.service-card {
  background-color: #1a1a1a;
  border-radius: 10px;
  padding: 1.5rem;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
  transition: transform 0.3s, box-shadow 0.3s;
}

.service-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.5);
}

.service-card h2 {
  margin-bottom: 0.5rem;
  color: #81c784;
}

footer.contact-info {
  margin-top: 3rem;
  text-align: center;
  padding: 2rem;
  background-color: #1a1a1a;
  border-radius: 10px;
}

.contact-details a {
  color: #58a6ff;
  text-decoration: none;
}

.contact-details a:hover {
  text-decoration: underline;
}
</style>
