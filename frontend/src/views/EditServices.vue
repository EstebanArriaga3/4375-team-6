<template>
  <div class="services">
    <!-- Page Title -->
    <h1>Our Premium Services</h1>

    <!-- Loading and Error Indicators -->
    <div v-if="isLoading" class="loading">Loading services...</div>
    <div v-if="errorMessage" class="error">{{ errorMessage }}</div>

    <!-- Add New Service Form -->
    <div class="new-service-form">
      <h2>Add a New Service</h2>
      <input v-model="newService.ServiceName" placeholder="Service Name" />
      <textarea v-model="newService.Description" placeholder="Description"></textarea>
      <input type="number" v-model="newService.Price" placeholder="Price" min="0" />
      <button @click="addService">Add Service</button>
    </div>

    <!-- Editable Service Cards Section for Admin -->
    <div v-if="!isLoading && !errorMessage" class="service-cards">
      <div v-for="service in services" :key="service.ServiceID" class="service-card">
        <input v-model="service.ServiceName" placeholder="Service Name" />
        <textarea v-model="service.Description" placeholder="Description"></textarea>
        <input type="number" v-model="service.Price" placeholder="Price" min="0" />

        <!-- Save and Delete buttons -->
        <button @click="updateService(service)">Save Changes</button>
        <button @click="deleteService(service.ServiceID)">Delete</button>
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

// New Service data model for form
const newService = ref({
  ServiceName: '',
  Description: '',
  Price: 0
})

// Fetch services from the backend
async function fetchServices() {
  try {
    const response = await axios.get('http://localhost:5000/api/Services')
    console.log("Fetched services data:", response.data) // Log the data to verify structure
    services.value = response.data                   // Set the fetched data to services
    errorMessage.value = null                        // Clear any existing error message
  } catch (error) {
    errorMessage.value = 'Failed to load services. Please try again later.'
    console.error('Error fetching services:', error) // Log error for debugging
  } finally {
    isLoading.value = false                          // End loading state
  }
}

// Update a service in the backend
async function updateService(service: Service) {
  try {
    await axios.put(`http://localhost:5000/api/Services/update`, {
      ServiceID: service.ServiceID,
      ServiceName: service.ServiceName,
      Description: service.Description,
      Price: service.Price
    })
    alert("Service updated successfully!")
  } catch (error) {
    console.error("Error updating service:", error)
    alert("Failed to update service. Please try again.")
  }
}

// Add a new service
async function addService() {
  if (!newService.value.ServiceName || !newService.value.Description) {
    alert("Please fill in all the fields.")
    return
  }

  try {
    const response = await axios.post('http://localhost:5000/api/Services/add', {
      ServiceName: newService.value.ServiceName,
      Description: newService.value.Description,
      Price: newService.value.Price
    })
    alert("Service added successfully!")
    // Clear the form after adding
    newService.value = { ServiceName: '', Description: '', Price: 0 }
    // Refresh the services list to include the new service
    fetchServices()
  } catch (error) {
    console.error("Error adding new service:", error)
    alert("Failed to add new service. Please try again.")
  }
}

// Delete a service
async function deleteService(serviceID: number) {
  const confirmation = confirm("Are you sure you want to delete this service?")
  if (!confirmation) return

  try {
    await axios.delete(`http://localhost:5000/api/Services/delete`, {
      data: { ServiceID: serviceID }
    })
    alert("Service deleted successfully!")
    // Refresh the services list after deletion
    fetchServices()
  } catch (error) {
    console.error("Error deleting service:", error)
    alert("Failed to delete service. Please try again.")
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

/* New Service Form */
.new-service-form {
  margin-bottom: 2rem;
  padding: 1rem;
  background-color: #1a1a1a;
  border-radius: 15px;
  width: 100%;
  max-width: 600px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
  text-align: center;
}

.new-service-form input,
.new-service-form textarea {
  width: 100%;
  padding: 0.5rem;
  margin: 0.5rem 0;
  border-radius: 5px;
  border: none;
  background-color: #333;
  color: #f0f0f0;
}

.new-service-form button {
  padding: 0.5rem 1rem;
  border: none;
  background-color: #4caf50;
  color: #fff;
  border-radius: 5px;
  cursor: pointer;
}

.new-service-form button:hover {
  background-color: #45a049;
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

.service-card input, .service-card textarea {
  width: 100%;
  margin-bottom: 0.5rem;
  padding: 0.5rem;
  font-size: 1rem;
  color: #f0f0f0;
  background-color: #2a2a2a;
  border: none;
  border-radius: 8px;
}

.service-card button {
  margin-top: 1rem;
  padding: 0.5rem 1rem;
  color: #f0f0f0;
  background-color: #4caf50;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}

.service-card button:hover {
  background-color: #388e3c;
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
</style>
