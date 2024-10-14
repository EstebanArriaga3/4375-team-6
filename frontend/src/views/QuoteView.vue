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

      <div class="description-section">
        <label for="contact">Email Address:</label>
        <textarea
          id="email"
          rows="1"
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
  max-width: 800px;
  margin: 2rem auto;
  padding: 2rem;
  background-color: var(--color-background-soft); /* Dark theme consistency */
  border-radius: 12px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.4); /* Enhanced shadow for a more appealing look */
}

.quote-header h1 {
  font-size: 2rem;
  margin-bottom: 0.5rem;
  color: var(--color-text);
  text-align: center;
}

.quote-header p {
  color: var(--color-text-soft);
  text-align: center;
  margin-bottom: 1.5rem;
}

.quote-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.services-section label {
  font-size: 1.2rem;
  font-weight: 500;
  color: var(--color-text-soft); /* Softer text for the label */
  margin-bottom: 0.5rem;
}

.checkbox-group {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.checkbox {
  display: flex;
  align-items: center;
}

.checkbox input {
  margin-right: 0.5rem;
}

.checkbox label {
  color: var(--color-text);
}

.description-section label {
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
  color: var(--color-text-soft);
}

.description-section textarea {
  width: 100%;
  padding: 0.8rem;
  border-radius: 8px;
  border: 1px solid #444; /* Darker border for consistency with the dark theme */
  background-color: var(--color-background);
  color: var(--color-text);
  resize: none;
}

.submit-section {
  text-align: center;
}

.btn-submit {
  background-color: var(--color-primary);
  color: var(--color-background);
  border: none;
  padding: 0.8rem 2rem;
  font-size: 1rem;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.btn-submit:hover {
  background-color: var(--color-primary-light);
  transform: translateY(-2px); /* Added lift effect on hover */
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
