<template>
  <section class="quote-container">
    <div class="quote-header">
      <h1>Customer Quotes</h1>
      <p>Review and manage incoming quote requests</p>
    </div>
    
    <div class="quotes-list">
      <div v-for="quote in quotes" :key="quote.quote_id" class="quote-item">
        <div class="quote-content">
          <div class="quote-info">
            <h3>Contact Information</h3>
            <p class="email">{{ quote.email_address }}</p>
          </div>

          <div class="quote-description">
            <h3>Project Description</h3>
            <p>{{ quote.description }}</p>
          </div>
          
          <div class="services-section">
            <h3>Requested Services</h3>
            <div class="checkbox-group">
              <div v-for="service in servicesList" :key="service.key" class="checkbox">
                <input 
                  type="checkbox" 
                  :checked="quote[service.key]" 
                  disabled 
                  :id="'service-' + quote.quote_id + '-' + service.key"
                />
                <label :for="'service-' + quote.quote_id + '-' + service.key">
                  {{ service.label }}
                </label>
              </div>
            </div>
          </div>

          <div class="action-section">
            <button @click="confirmDeleteQuote(quote.quote_id)" class="btn-delete">
              Delete Quote
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
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
  [key: string]: any;
}

const servicesList = [
  { key: 'fence_gates_service', label: 'Fences and Gates' },
  { key: 'raised_beds_service', label: 'Raised Beds' },
  { key: 'landscaping_service', label: 'Landscaping' },
  { key: 'gutters_roofing_service', label: 'Gutters & Roofing' },
];

const quotes = ref<Quote[]>([]);

async function fetchQuotes() {
  try {
    const response = await axios.get<Quote[]>('http://localhost:5000/api/Quotes');
    quotes.value = response.data;
  } catch (error) {
    console.error('Error fetching quotes:', error);
    alert('Failed to load quotes. Please try again later.');
  }
}

function confirmDeleteQuote(quote_id: number) {
  if (confirm("Are you sure you want to delete this quote?")) {
    deleteQuote(quote_id);
  }
}

async function deleteQuote(quote_id: number) {
  try {
    await axios.delete('http://localhost:5000/api/Quotes/delete', {
      data: { quote_id: quote_id },
    });
    quotes.value = quotes.value.filter(quote => quote.quote_id !== quote_id);
    alert('Quote deleted successfully!');
  } catch (error) {
    console.error('Error deleting quote:', error);
    alert('Failed to delete quote. Please try again.');
  }
}

onMounted(fetchQuotes);
</script>

<style scoped>
.quote-container {
  max-width: 900px;
  margin: 3rem auto;
  padding: 2.5rem;
  background-color: var(--color-background-soft);
  border-radius: 16px;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.6);
  animation: fadeIn 0.8s ease-in-out;
}

.quote-header {
  text-align: center;
  margin-bottom: 2.5rem;
}

.quote-header h1 {
  font-size: 3rem;
  color: var(--color-primary);
  text-transform: uppercase;
  font-weight: bold;
  letter-spacing: 2px;
  border-bottom: 2px solid var(--color-primary-light);
  display: inline-block;
  padding-bottom: 10px;
}

.quote-header p {
  font-size: 1.3rem;
  color: var(--color-text-soft);
  margin-top: 1rem;
}

.quotes-list {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.quote-item {
  background-color: var(--color-background);
  border: 2px solid var(--color-primary-light);
  border-radius: 10px;
  padding: 2rem;
  transition: all 0.3s ease;
}

.quote-item:hover {
  box-shadow: 0 4px 12px rgba(var(--color-primary-rgb), 0.3);
}

.quote-content {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.quote-info h3,
.quote-description h3,
.services-section h3 {
  font-size: 1.6rem;
  color: var(--color-text);
  margin-bottom: 1rem;
  text-transform: uppercase;
}

.email {
  color: var(--color-primary);
  font-size: 1.2rem;
}

.quote-description p {
  color: var(--color-text);
  font-size: 1.1rem;
  line-height: 1.6;
}

.services-section {
  margin-top: 1rem;
}

.checkbox-group {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
}

.checkbox {
  display: flex;
  align-items: center;
}

.checkbox input {
  margin-right: 0.8rem;
  accent-color: var(--color-secondary);
}

.checkbox label {
  color: var(--color-text);
  font-size: 1.2rem;
}

.action-section {
  display: flex;
  justify-content: flex-end;
  margin-top: 1rem;
}

.btn-delete {
  padding: 12px 30px;
  background-color: #ff4136;
  color: var(--color-background);
  font-size: 1.1rem;
  font-weight: 600;
  text-transform: uppercase;
  border: none;
  border-radius: 50px;
  box-shadow: 0 4px 12px rgba(255, 65, 54, 0.4);
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-delete:hover {
  background-color: #d0342b;
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .quote-container {
    padding: 1.5rem;
    margin: 1.5rem;
  }

  .quote-header h1 {
    font-size: 2.5rem;
  }

  .checkbox-group {
    grid-template-columns: 1fr;
  }

  .quote-item {
    padding: 1.5rem;
  }
}
</style>