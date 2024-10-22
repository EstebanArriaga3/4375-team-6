<template>
  <div class="services">
    <h1>Our Premium Services</h1>

    <!-- Service Cards Section -->
    <div class="service-cards">
      <div v-for="service in services" :key="service.title" class="service-card">
        <h2>{{ service.title }}</h2>
        <p>{{ service.description }}</p>
      </div>
    </div>

    <!-- Contact Info Section -->
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
/* Main Container */
.services {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 3rem 2rem;
  background-color: #0d0d0d;
  color: #f0f0f0;
  font-family: 'Poppins', sans-serif;
  animation: fadeIn 1s ease-in-out;
}

/* Fade-in animation for smooth entry */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Heading */
h1 {
  font-size: 3rem;
  margin-bottom: 2.5rem;
  color: #4caf50;
  text-transform: uppercase;
  letter-spacing: 1px;
  border-bottom: 3px solid #4caf50;
  display: inline-block;
  padding-bottom: 10px;
}

/* Service Cards Section */
.service-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  width: 100%;
  max-width: 1200px;
}

/* Individual Service Card */
.service-card {
  background-color: #1a1a1a;
  border-radius: 15px;
  padding: 2rem;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.4);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  text-align: center;
  cursor: pointer;
}

.service-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.5);
}

/* Service Card Title */
.service-card h2 {
  margin-bottom: 1rem;
  font-size: 1.8rem;
  color: #81c784;
  text-transform: uppercase;
  letter-spacing: 1px;
}

/* Service Card Description */
.service-card p {
  font-size: 1.1rem;
  color: #ccc;
  line-height: 1.6;
  margin: 0 auto;
}

/* Footer (Contact Section) */
footer.contact-info {
  margin-top: 4rem;
  text-align: center;
  padding: 2.5rem;
  background-color: #1a1a1a;
  border-radius: 15px;
  width: 100%;
  max-width: 900px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
}

/* Contact Details */
.contact-details p {
  margin: 0.5rem 0;
  font-size: 1.1rem;
  color: #ccc;
}

.contact-details a {
  color: #58a6ff;
  text-decoration: none;
}

.contact-details a:hover {
  text-decoration: underline;
}

/* Responsive Design */
@media (max-width: 768px) {
  .service-cards {
    grid-template-columns: 1fr;
  }

  h1 {
    font-size: 2.5rem;
  }

  .service-card h2 {
    font-size: 1.6rem;
  }

  footer.contact-info {
    padding: 2rem;
  }
}
</style>
