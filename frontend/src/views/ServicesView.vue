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
  padding: 3rem 1rem;
  background-color: #f5f5f5; /* Light gray background */
  color: #333; /* Dark text for better contrast on light background */
  font-family: 'Poppins', sans-serif;
  animation: fadeIn 1s ease-in-out;
}

/* Smooth Fade-in Animation */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Page Title Styling */
h1 {
  font-size: 2.8rem;
  color: #004175; /* Navy blue for headings */
  margin-bottom: 2rem;
  text-transform: uppercase;
  letter-spacing: 1px;
  border-bottom: 4px solid #ff7f50; /* Coral accent under heading */
  padding-bottom: 0.5rem;
}

/* Loading and Error States */
.loading, .error {
  font-size: 1.5rem;
  margin-top: 2rem;
  text-align: center;
}

.error {
  color: #e57373; /* Red tone for errors */
}

/* Service Cards Grid Layout */
.service-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  width: 100%;
  max-width: 1200px;
}

/* Individual Service Card */
.service-card {
  background-color: #ffffff; /* White background for each card */
  border-radius: 10px;
  padding: 2rem;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  text-align: left; /* Align text to the left for better readability */
}

.service-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
}

/* Service Title and Description */
.service-card h2 {
  font-size: 1.8rem;
  color: #004175; /* Navy blue for service titles */
  margin-bottom: 0.8rem;
}

.service-card p {
  font-size: 1.1rem;
  color: #555; /* Darker text for descriptions */
}

/* Price Tag Styling */
.service-card .price {
  font-size: 1.3rem;
  color: #ff7f50; /* Coral for price highlight */
  font-weight: bold;
}

/* Footer Styling - Contact Information */
footer.contact-info {
  margin-top: 3rem;
  text-align: center;
  padding: 2rem;
  background-color: #eeeeee; /* Light background for footer */
  border-radius: 10px;
  width: 100%;
  max-width: 900px;
}

/* Contact Details */
.contact-details p {
  font-size: 1.1rem;
  color: #666; /* Darker grey for readability */
}

.contact-details a {
  color: #004175; /* Navy blue for links */
  text-decoration: none;
}

.contact-details a:hover {
  text-decoration: underline; /* Underline on hover for links */
}

/* Responsive Adjustments */
@media (max-width: 768px) {
  .service-cards {
    grid-template-columns: 1fr; /* Single column layout on smaller screens */
  }
  
  h1 {
    font-size: 2.5rem; /* Smaller font size for mobile */
  }
}
</style>