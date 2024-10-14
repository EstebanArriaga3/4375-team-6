<template>
  <section class="quote-container">
    <div class="quote-header">
      <h1>Get Your Free Quote</h1>
      <p>Tell us about your needs, and we'll provide the perfect solution.</p>
    </div>

    <form class="quote-form">
      <div class="services-section">
        <label>Select Services:</label>
        <div class="checkbox-group">
          <div class="checkbox">
            <input type="checkbox" id="fences-gates" value="fences-gates" />
            <label for="fences-gates">Fences and Gates</label>
          </div>
          <div class="checkbox">
            <input type="checkbox" id="raised-beds" value="raised-beds" />
            <label for="raised-beds">Raised Beds</label>
          </div>
          <div class="checkbox">
            <input type="checkbox" id="landscaping" value="landscaping" />
            <label for="landscaping">Landscaping</label>
          </div>
          <div class="checkbox">
            <input type="checkbox" id="gutters-roofing" value="Gutters&Roofing" />
            <label for="gutters-roofing">Gutters & Roofing</label>
          </div>
        </div>
      </div>

      <div class="description-section">
        <label for="description">Description:</label>
        <textarea
          id="description"
          rows="5"
          placeholder="Provide size, details, and requirements..."
        ></textarea>
      </div>

      <div class="submit-section">
        <button type="submit" class="btn-submit">Submit</button>
      </div>
    </form>
  </section>
</template>

<style scoped>
.quote-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh - var(--header-height) - 60px); /* Adjust for header and footer height */
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  background-color: #f8f9fa;
  border-radius: 12px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}

.quote-header h1 {
  font-size: 2rem;
  margin-bottom: 0.5rem;
  color: #333;
  text-align: center;
}

.quote-header p {
  color: #555;
  text-align: center;
  margin-bottom: 1.5rem;
}

.quote-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  width: 100%;
}

.services-section label {
  font-size: 1.2rem;
  font-weight: 500;
  margin-bottom: 0.5rem;
}

.checkbox-group {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.checkbox input {
  margin-right: 0.5rem;
}

.description-section label {
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
}

.description-section textarea {
  width: 100%;
  padding: 0.8rem;
  border-radius: 8px;
  border: 1px solid #ddd;
  resize: none;
}

.submit-section {
  text-align: center;
}

.btn-submit {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 0.8rem 2rem;
  font-size: 1rem;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn-submit:hover {
  background-color: #0056b3;
}

@media (max-width: 768px) {
  .checkbox-group {
    grid-template-columns: 1fr;
  }

  .quote-container {
    padding: 1rem;
  }
}
</style>
