<template>
    <div class="categories-wrapper">
    <div class="categories">
      <div
        class="category-box"
        v-for="(category, index) in categories"
        :key="index"
        @click="openCarousel(index)"
      >
        {{ category.label }}
      </div>
    </div>

    <div v-if="showCarousel" class="carousel-modal">
      <div class="carousel">
        <!-- Move close button here -->
        <button class="close-btn" @click="closeCarousel">X</button>
        <div class="carousel-wrapper">
          <div
            v-for="(image, imgIndex) in categories[currentCategoryIndex].images"
            :key="imgIndex"
            class="carousel-item"
            :class="{ active: currentIndex === imgIndex }"
          >
            <img :src="image.src" :alt="image.alt" />
          </div>
        </div>
        <div class="carousel-controls">
          <button class="prev-btn" @click="prevSlide">❮</button>
          <button class="next-btn" @click="nextSlide">❯</button>
        </div>
        <div class="carousel-indicators">
          <span
            v-for="(image, imgIndex) in categories[currentCategoryIndex].images"
            :key="imgIndex"
            @click="goToSlide(imgIndex)"
            :class="{ active: currentIndex === imgIndex }"
          ></span>
        </div>
      </div>
    </div>
  </div>
  </template>

<script>
export default {
  data() {
    return {
      currentIndex: 0,
      showCarousel: false,
      currentCategoryIndex: null,
      categories: [
        {
          label: "Lawns",
          images: [
            { src: "/images/lawn1.jpg", alt: "/images/lawn1.jpg" },
            { src: "/images/lawn2.jpg", alt: "/images/lawn2.jpg" },
            { src: "/images/lawn3.jpg", alt: "/images/lawn3.jpg" },
          ],
        },
        {
          label: "Landscaping",
          images: [
            { src: "/images/landscaping1.jpg", alt: "/images/landscaping1.jpg" },
            { src: "/images/landscaping2.jpg", alt: "/images/landscaping2.jpg" },
            { src: "/images/landscaping3.jpg", alt: "/images/landscaping3.jpg" },
          ],
        },
        {
          label: "Fences & Gates",
          images: [
            { src: "/images/fence&gate1.jpg", alt: "/images/fence&gate1.jpg" },
            { src: "/images/fence&gate2.jpg", alt: "/images/fence&gate2.jpg" },
            { src: "/images/fence&gate3.jpg", alt: "/images/fence&gate3.jpg" },
          ],
        },
        {
          label: "Raised Beds",
          images: [
            { src: "/images/raised_bed1.jpg", alt: "/images/raised_bed1.jpg" },
            { src: "/images/raised_bed2.jpg", alt: "/images/raised_bed2.jpg" },
            { src: "/images/raised_bed3.jpg", alt: "/images/raised_bed3.jpg" },
          ],
        },
        {
          label: "Roof & Gutters",
          images: [
          { src: "/images/roof&gutters1.jpg", alt: "/images/roof&gutters1.jpg" },
          ],
        },
      ],
    };
  },
  methods: {
    openCarousel(categoryIndex) {
      this.currentCategoryIndex = categoryIndex;
      this.showCarousel = true;
      this.currentIndex = 0; // Reset the slide index when opening a new carousel
    },
    closeCarousel() {
      this.showCarousel = false;
    },
    nextSlide() {
      const images = this.categories[this.currentCategoryIndex].images;
      this.currentIndex = (this.currentIndex + 1) % images.length;
    },
    prevSlide() {
      const images = this.categories[this.currentCategoryIndex].images;
      this.currentIndex = (this.currentIndex - 1 + images.length) % images.length;
    },
    goToSlide(index) {
      this.currentIndex = index;
    },
  },
};
</script>
  
  <style scoped>
  @media (min-width: 1024px) {
    .about {
      min-height: 100vh;
      display: flex;
      align-items: center;
    }
  }

  .categories-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}

.categories {
  display: flex;
  justify-content: center; /* Center content within the container */
  gap: 20px; /* Spacing between boxes */
  margin-top: 0px; /* Space from the top */
  margin-left: 10px;
  padding: 1px;
  
}

.category-box {
  width: 250px; /* Set a fixed width for the boxes */
  height: 250px; /* Set a fixed height for the boxes */
  display: flex;
  justify-content: center; /* Center content inside the box */
  align-items: center; /* Center content inside the box */
  background-color: #ccc;
  cursor: pointer;
  text-align: center;
  padding: 20px;
  font-weight: bold;
  border-radius: 10px;
  flex-shrink: 0; /* Prevent boxes from shrinking */
  font-family: 'Copperplate', serif; /* Set font to Copperplate */
  font-size: large;
  color: red; /* Change text color to red */
}

/* Exit button (close carousel) in the top-right corner */
.close-btn {
  position: absolute;
  bottom: 10px; /* Position at the bottom */
  right: 10px; /* Position at the right */
  background-color: rgba(255, 255, 255, 0.8);
  border: none;
  font-size: 24px;
  cursor: pointer;
  color: black;
  padding: 5px 10px;
  border-radius: 50%;
  z-index: 3; /* Ensure it appears on top of all content */
}

.carousel-modal {
  position: fixed;
  top: 60px; /* Adjust this value based on your actual header height */
  left: 0;
  width: 100%;
  height: calc(100% - 60px); /* Make sure the modal covers the rest of the screen, accounting for the header */
  display: flex;
  justify-content: center;
  align-items: center;
  background: rgba(0, 0, 0, 0.7);
  z-index: 2; /* Ensure the modal is behind the header if the header is fixed or sticky */
}

.carousel {
  background-color: #fff;
  padding: 20px;
  position: relative;
  width: 80%;
  max-width: 800px;
  margin: auto; /* Center carousel */
}

.carousel-wrapper {
  display: flex;
  transition: transform 0.5s ease-in-out;
  width: 100%; /* Ensure the wrapper takes up full width */
  justify-content: center; /* Center the content inside */
}

.carousel-item {
  min-width: 100%;
  display: none; /* Initially hide all items */
  justify-content: center; /* Center the image inside the item */
  opacity: 0;
  transition: opacity 0.5s ease-in-out;
}

.carousel-item.active {
  display: flex; /* Show the active item */
  opacity: 1;
}

.carousel img {
  width: 100%;
  height: auto;
  object-fit: contain; /* Ensure the image fits within the container */
}

/* Adjusting previous and next button positions to avoid covering the image */
.carousel-controls {
  display: flex;
  justify-content: space-between;
  position: absolute;
  width: 100%;
  top: 50%;
  left: 0;
  right: 0;
  transform: translateY(-50%);
  pointer-events: none; /* Prevent buttons from interfering with images */
}

.prev-btn, .next-btn {
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  font-size: 24px;
  pointer-events: all; /* Enable clicks only on buttons */
  z-index: 1;
}

.prev-btn {
  left: -60px;
  position: relative;
}

.next-btn {
  right: -60px;
  position: relative;
}

.carousel-indicators {
  display: flex;
  justify-content: center;
  margin-top: 10px;
}

.carousel-indicators span {
  width: 10px;
  height: 10px;
  margin: 0 5px;
  background-color: rgba(0, 0, 0, 0.3);
  border-radius: 50%;
  cursor: pointer;
}

.carousel-indicators span.active {
  background-color: rgba(0, 0, 0, 1);
}
  </style>
