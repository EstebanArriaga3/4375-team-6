<template>
  <div class="services">
    <h1>Our Premium Services</h1>

    <!-- New Service Form -->
    <div class="new-service-form">
      <h2>Add a New Service</h2>
      <input v-model="newService.ServiceName" placeholder="Service Title" />
      <textarea v-model="newService.Description" placeholder="Service Description"></textarea>
      <input v-model.number="newService.Price" placeholder="Price" type="number" />
      <button @click="addService">Add Service</button>
    </div>

    <!-- Service Cards Section -->
    <div class="service-cards">
      <div v-for="(service, index) in services" :key="service.ServiceID" class="service-card">
        <div v-if="editIndex === index">
          <input v-model="editableService.ServiceName" placeholder="Service Title" />
          <textarea v-model="editableService.Description" placeholder="Service Description"></textarea>
          <input v-model.number="editableService.Price" placeholder="Price" type="number" />
          <button @click="saveEdit(service.ServiceID)">Save</button>
          <button @click="cancelEdit">Cancel</button>
        </div>
        <div v-else>
          <h2>{{ service.ServiceName }}</h2>
          <p>{{ service.Description }}</p>
          <button @click="editService(index)">Edit</button>
          <button @click="deleteService(service.ServiceID)">Delete</button>
        </div>
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
import { ref, onMounted } from 'vue'
import axios from 'axios'

// Define the TypeScript interface for a service
interface Service {
  ServiceID: number
  ServiceName: string
  Description: string
  Price: number
}

// State for the services and editing
const services = ref<Service[]>([]) // Array to store services fetched from the backend
const editIndex = ref<number | null>(null) // Index of the service being edited
const editableService = ref<Service>({ ServiceID: 0, ServiceName: '', Description: '', Price: 0 }) // Service being edited
const newService = ref<Omit<Service, 'ServiceID'>>({ ServiceName: '', Description: '', Price: 0 }) // Data for a new service

// Fetch services from the backend when component is mounted
onMounted(async () => {
  await fetchServices()
})

// Function to fetch services from backend
async function fetchServices() {
  try {
    const response = await axios.get('/api/Services')
    services.value = response.data // Populate the services array with data from the API
  } catch (error) {
    console.error('Error fetching services:', error)
  }
}

// Enter edit mode for a specific service
function editService(index: number) {
  editIndex.value = index
  editableService.value = { ...services.value[index] }
}

// Save the edited service
async function saveEdit(serviceId: number) {
  try {
    await axios.put('/api/Services/update', {
      ServiceID: serviceId,
      ServiceName: editableService.value.ServiceName,
      Description: editableService.value.Description,
      Price: editableService.value.Price,
    })
    await fetchServices() // Refresh services after the edit
    editIndex.value = null // Exit edit mode
  } catch (error) {
    console.error('Error saving service:', error)
  }
}

// Cancel editing mode
function cancelEdit() {
  editIndex.value = null
}

// Delete a service
async function deleteService(serviceId: number) {
  try {
    await axios.delete('/api/Services/delete', { data: { ServiceID: serviceId } })
    await fetchServices() // Refresh services after deletion
  } catch (error) {
    console.error('Error deleting service:', error)
  }
}

// Add a new service
async function addService() {
  if (newService.value.ServiceName && newService.value.Description && newService.value.Price) {
    try {
      await axios.post('/api/Services/add', {
        ServiceName: newService.value.ServiceName,
        Description: newService.value.Description,
        Price: newService.value.Price,
      })
      await fetchServices() // Refresh services after adding a new one
      newService.value = { ServiceName: '', Description: '', Price: 0 } // Reset form fields
    } catch (error) {
      console.error('Error adding service:', error)
    }
  } else {
    alert('Please provide a title, description, and price for the new service.')
  }
}
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

.new-service-form h2 {
  color: #4caf50;
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
