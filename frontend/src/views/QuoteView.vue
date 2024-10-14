<template>
  <div class="about">
    <h1>Fill out the form below to receive a free quote</h1>
    <form class="quote-form">
      <div>
        <label>Select services: </label>
        
        <div class="checkbox-group">
          <div>
            <input type="checkbox" id="fences-gates" name="service" value="fences-gates">
            <label for="fences-gates">Fences and Gates</label>
          </div>
          <div>
            <input type="checkbox" id="raised-beds" name="service" value="raised-beds">
            <label for="raised-beds">Raised Beds</label>
          </div>
          <div>
            <input type="checkbox" id="landscaping" name="service" value="landscaping">
            <label for="landscaping">Landscaping</label>
          </div>
          <div>
            <input type="checkbox" id="Gutters&Roofing" name="service" value="Gutters&Roofing">
            <label for="Gutters&Roofing">Gutters & Roofing</label>
          </div>
        </div>
      </div>
      <div>
        <label for="description">Description:</label>
        <textarea id="description" name="description" rows="4" cols="50" placeholder="Provide information like the size of the lawn or work area and details about the requested services."></textarea>
      </div>
      <div>
        <button type="submit">Submit</button>
      </div>
    </form>
  </div>
</template>

<style>
  @media (min-width: 1024px) {
    .about {
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
    }

    h1 {
      margin-bottom: 2rem;
    }

    .quote-form {
      display: flex;
      flex-direction: column;
      width: 500px;
      height: 500px;
      text-align: left;
      
    }

    .quote-form div {
      margin: auto;
      width: 100%;
      
    }

    .checkbox-group {
      display: flex;
      flex-direction: column;
      align-items: flex-start; /* Aligns checkboxes to the left */
    }

    .checkbox-group div {
      margin-bottom: 0.5rem;
    }

    .quote-form label {
      font-size: 1.2rem;
      margin-bottom: 0.5rem;
    }

    .quote-form textarea, .quote-form input[type="checkbox"], .quote-form button {
      font-size: 1rem;
    }

    .quote-form textarea {
      width: 100%;
      padding: 0.5rem;
    }

    .quote-form button {
      background-color: #4CAF50;
      color: white;
      border: none;
      padding: 0.7rem;
      cursor: pointer;
      width: 100%;
    }

    .quote-form button:hover {
      background-color: #45a049;
    }
  }
</style>
