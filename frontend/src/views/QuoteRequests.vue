<template>
  <div class="quote-page">
    <h1>Customer Quotes</h1>
    
    <!-- Display Quotes -->
    <div class="quotes-list">
      <div v-for="(quote, index) in quotes" :key="index" class="quote-item">
        <p><strong>Email:</strong> {{ quote.email_address }}</p>
        <p><strong>Project Description:</strong> {{ quote.description }}</p>
        <div class="services">
          <strong>Services:</strong>
          <div class="service-checkbox">
            <input type="checkbox" :checked="quote.fence_gates_service" disabled>
            <label>Fence & Gates</label>
          </div>
          <div class="service-checkbox">
            <input type="checkbox" :checked="quote.raised_beds_service" disabled>
            <label>Raised Beds</label>
          </div>
          <div class="service-checkbox">
            <input type="checkbox" :checked="quote.landscaping_service" disabled>
            <label>Landscaping</label>
          </div>
          <div class="service-checkbox">
            <input type="checkbox" :checked="quote.gutters_roofing_service" disabled>
            <label>Gutters & Roofing</label>
          </div>
        </div>
        <button @click="deleteQuote(quote.quote_id)" class="delete-btn">Delete Quote</button>
      </div>
    </div>
  </div>
</template>
  
<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';

interface Quote {
  quote_id: number;
  email_address: string;
  description: string;
  fence_gates_service: boolean;
  raised_beds_service: boolean;
  landscaping_service: boolean;
  gutters_roofing_service: boolean;
}

const quotes = ref<Quote[]>([]);

async function fetchQuotes() {
  try {
    const response = await axios.get<Quote[]>('http://localhost:5000/api/Quotes');
    quotes.value = response.data;
  } catch (error) {
    console.error('Error fetching quotes:', error);
  }
}

async function deleteQuote(quote_id: number) {
  try {
    await axios.delete('http://localhost:5000/api/Quotes/delete', {
      data: { quote_id: quote_id }
    });
    // Remove the deleted quote from the local list
    quotes.value = quotes.value.filter(quote => quote.quote_id !== quote_id);
  } catch (error) {
    console.error('Error deleting quote:', error);
  }
}

onMounted(fetchQuotes);
</script>
  
<style scoped>
.quote-page {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  background-color: #1e1e1e;
  border-radius: 8px;
  color: #ffffff;
}

h1 {
  color: #81c784;
  text-align: center;
  font-size: 2.5rem;
  margin-bottom: 2rem;
}

.quotes-list {
  margin-top: 2rem;
}

.quote-item {
  margin-bottom: 1.5rem;
  padding: 1.5rem;
  border: 1px solid #2c2c2c;
  border-radius: 8px;
  background-color: #2c2c2c;
  transition: all 0.3s ease;
}

.quote-item:hover {
  box-shadow: 0 0 15px rgba(29, 220, 77, 0.3);
}

.quote-item p {
  margin: 0.5rem 0;
  font-size: 1.1rem;
}

.quote-item strong {
  color: #81c784;
}

.services {
  margin-top: 1rem;
}

.service-checkbox {
  display: flex;
  align-items: center;
  margin-top: 0.5rem;
}

.service-checkbox input[type="checkbox"] {
  margin-right: 0.5rem;
}

.delete-btn {
  background-color: #ff4136;
  color: white;
  border: none;
  padding: 8px 15px;
  cursor: pointer;
  margin-top: 15px;
  border-radius: 4px;
  transition: background-color 0.3s ease;
  font-size: 1rem;
}

.delete-btn:hover {
  background-color: #d0342b;
}

@media (max-width: 768px) {
  .quote-page {
    padding: 1rem;
  }

  h1 {
    font-size: 2rem;
  }

  .quote-item {
    padding: 1rem;
  }
}

.services {
  margin-top: 1rem;
}

.service-checkbox {
  display: flex;
  align-items: center;
  margin-top: 0.8rem;
}

.service-checkbox input[type="checkbox"] {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  width: 20px;
  height: 20px;
  border: 2px solid #81c784;
  border-radius: 4px;
  outline: none;
  transition: all 0.3s ease;
  position: relative;
  cursor: pointer;
  margin-right: 0.8rem;
}

.service-checkbox input[type="checkbox"]:checked {
  background-color: #81c784;
}

.service-checkbox input[type="checkbox"]:checked::before {
  content: '\2714';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: #1e1e1e;
  font-size: 14px;
}

.service-checkbox label {
  color: #ffffff;
  font-size: 1.1rem;
  cursor: pointer;
}

.service-checkbox:hover input[type="checkbox"] {
  border-color: #a5d6a7;
}

.service-checkbox:hover label {
  color: #a5d6a7;
}
</style>