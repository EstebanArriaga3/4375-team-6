<template>
  <section class="quote-container">
    <div class="quote-header">
      <h1>Get Your Free Quote</h1>
      <p>Let us know your needs, and we’ll craft the perfect solution tailored to you.</p>
    </div>

    <form class="quote-form">
      <div class="services-section">
        <h2>Select Services:</h2>
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
            <input type="checkbox" id="gutters-roofing" value="gutters-roofing" />
            <label for="gutters-roofing">Gutters & Roofing</label>
          </div>
        </div>
      </div>

      <div class="description-section">
        <label for="description">Project Description:</label>
        <textarea
          id="description"
          rows="4"
          placeholder="Describe the size, location, and specifics of your project..."
        ></textarea>

        <label for="email">Your Email Address:</label>
        <input type="email" id="email" placeholder="Enter your email" />
      </div>

      <div class="submit-section">
        <button type="submit" class="btn-submit">Get My Free Quote</button>
      </div>
    </form>
  </section>
</template>

<style scoped>
/* Container */
.quote-container {
  max-width: 900px;
  margin: 3rem auto;
  padding: 2.5rem;
  background-color: #1f1f1f; /* Dark background */
  border-radius: 16px;
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.6);
  animation: fadeIn 0.8s ease-in-out;
}

/* Animation for smooth fade-in effect */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Header */
.quote-header {
  text-align: center;
  margin-bottom: 2.5rem;
}

.quote-header h1 {
  font-size: 3rem;
  color: #ffffff;
  text-transform: uppercase;
  font-weight: bold;
  letter-spacing: 2px;
  border-bottom: 2px solid #28a745;
  display: inline-block;
  padding-bottom: 10px;
}

.quote-header p {
  font-size: 1.3rem;
  color: #d4d4d4;
  margin-top: 1rem;
}

/* Form Styling */
.quote-form {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

/* Services Section */
.services-section h2 {
  font-size: 1.6rem;
  color: #f0f0f0;
  margin-bottom: 1rem;
  text-transform: uppercase;
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
  accent-color: #28a745;
}

.checkbox label {
  color: #ffffff;
  font-size: 1.2rem;
}

/* Description Section */
.description-section label {
  font-size: 1.2rem;
  color: #ffffff;
  display: block;
  margin-bottom: 0.5rem;
}

.description-section textarea,
.description-section input {
  width: 100%;
  padding: 15px;
  margin-bottom: 1.5rem;
  border: 2px solid #444;
  border-radius: 10px;
  background-color: #2d2d2d;
  color: #f0f0f0;
  font-size: 1.1rem;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.description-section textarea:focus,
.description-section input:focus {
  border-color: #28a745;
  box-shadow: 0 4px 12px rgba(40, 167, 69, 0.3);
}

.description-section textarea::placeholder,
.description-section input::placeholder {
  color: #888;
  font-size: 1rem;
}

/* Submit Button */
.submit-section {
  text-align: center;
}

.btn-submit {
  padding: 15px 40px;
  background-color: #28a745;
  color: #ffffff;
  font-size: 1.3rem;
  font-weight: 600;
  text-transform: uppercase;
  border: none;
  border-radius: 50px;
  box-shadow: 0 8px 20px rgba(40, 167, 69, 0.6);
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.btn-submit:hover {
  background-color: #218838;
  transform: translateY(-5px);
}

/* Responsiveness */
@media (max-width: 768px) {
  .checkbox-group {
    grid-template-columns: 1fr;
  }

  .quote-container {
    padding: 1.5rem;
  }

  .quote-header h1 {
    font-size: 2.5rem;
  }

  .quote-header p {
    font-size: 1.1rem;
  }

  .btn-submit {
    font-size: 1.1rem;
    padding: 12px 30px;
  }
}
</style>
