<template>
  <div class="services">
    <!-- Page Title -->
    <h1>Our Premium Services</h1>

    <!-- Loading and Error Indicators -->
    <div v-if="isLoading" class="loading">Loading services...</div>
    <div v-if="errorMessage" class="error">{{ errorMessage }}</div>

    <!-- Service Cards Section -->
    <div v-if="!isLoading && !errorMessage" class="service-cards">
      <div v-for="service in services" :key="service.ServiceID" class="service-card">
        <h2>{{ service.ServiceName }}</h2>
        <p>{{ service.Description }}</p>
        <!-- Optionally show price if needed -->
        <p v-if="service.Price > 0" class="price">Starting at: ${{ service.Price }}</p>
      </div>
    </div>

    <!-- Contact Information -->
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
import { ref, onMounted } from 'vue'
import axios from 'axios'

// Define TypeScript interface for a Service
interface Service {
  ServiceID: number
  ServiceName: string
  Description: string
  Price: number
}

// Reactive state variables
const services = ref<Service[]>([])      // Holds the list of services
const isLoading = ref(true)              // Loading state indicator
const errorMessage = ref<string | null>(null)  // Error message

// Fetch services from the backend
async function fetchServices() {
  try {
    const response = await axios.get('http://localhost:5000/api/Services'); // Use 'localhost' to match frontend
    services.value = response.data;
    errorMessage.value = null;
  } catch (error) {
    errorMessage.value = 'Failed to load services. Please try again later.';
    console.error('Error fetching services:', error);
  } finally {
    isLoading.value = false;
  }
}


// On component mount, fetch services from the backend
onMounted(() => {
  fetchServices()
})
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

/* Page Title */
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

/* Loading and Error States */
.loading, .error {
  font-size: 1.5rem;
  margin-top: 2rem;
  color: #81c784;
  text-align: center;
}

.error {
  color: #e57373;
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

/* Price Information */
.service-card .price {
  font-size: 1.2rem;
  color: #ffd700;
  font-weight: bold;
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
