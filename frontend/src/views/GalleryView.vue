<template>
  <div class="gallery-wrapper">
    <h2 class="gallery-heading">Explore Our Creations</h2>

    <!-- Categories Section -->
    <div class="categories">
      <div
        class="category-box"
        v-for="(category, index) in categories"
        :key="index"
        @click="openCarousel(index)"
      >
        <img :src="category.thumbnail" :alt="category.label" class="category-thumbnail" />
        <div class="category-label">{{ category.label }}</div>
      </div>
    </div>

    <!-- Image Carousel Modal -->
    <div v-if="showCarousel" class="carousel-modal" @click.self="closeCarousel">
      <div class="carousel">
        <button class="close-btn" @click="closeCarousel">✖</button>

        <div class="carousel-wrapper">
          <div
            v-for="(image, imgIndex) in categories[currentCategoryIndex].images"
            :key="imgIndex"
            class="carousel-item"
            :class="{ active: currentIndex === imgIndex }"
          >
            <img :src="image.src" :alt="image.alt" class="carousel-image"/>
          </div>
        </div>

        <!-- Carousel Controls -->
        <div class="carousel-controls">
          <button class="prev-btn" @click="prevSlide">❮</button>
          <button class="next-btn" @click="nextSlide">❯</button>
        </div>

        <!-- Slide Indicators -->
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
          thumbnail: "/images/thumbnail/lawn_thumb.jpg",
          images: [
            { src: "/images/lawn1.jpg", alt: "Lawn 1" },
            { src: "/images/lawn2.jpg", alt: "Lawn 2" },
            { src: "/images/lawn3.jpg", alt: "Lawn 3" },
          ],
        },
        {
          label: "Landscaping",
          thumbnail: "/images/thumbnail/landscaping_thumb.jpg",
          images: [
            { src: "/images/landscaping1.jpg", alt: "Landscaping 1" },
            { src: "/images/landscaping2.jpg", alt: "Landscaping 2" },
            { src: "/images/landscaping3.jpg", alt: "Landscaping 3" },
          ],
        },
        {
          label: "Fences & Gates",
          thumbnail: "/images/thumbnail/fences_thumb.jpg",
          images: [
            { src: "/images/fence1.jpg", alt: "Fence 1" },
            { src: "/images/fence2.jpg", alt: "Fence 2" },
            { src: "/images/fence3.jpg", alt: "Fence 3" },
          ],
        },
        {
          label: "Raised Beds",
          thumbnail: "/images/thumbnail/raised_bed_thumb.jpg",
          images: [
            { src: "/images/raised_bed1.jpg", alt: "Raised Bed 1" },
            { src: "/images/raised_bed2.jpg", alt: "Raised Bed 2" },
            { src: "/images/raised_bed3.jpg", alt: "Raised Bed 3" },
          ],
        },
        {
          label: "Roof & Gutters",
          thumbnail: "/images/thumbnail/roof_gutter_thumb.jpg",
          images: [
            { src: "/images/roof_gutters1.jpg", alt: "Roof & Gutter 1" },
          ],
        },
      ],
    };
  },
  methods: {
    openCarousel(categoryIndex) {
      this.currentCategoryIndex = categoryIndex;
      this.showCarousel = true;
      this.currentIndex = 0; // Reset slide index when opening a new carousel
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
/* Main Wrapper */
.gallery-wrapper {
  padding: 3rem 1rem;
  text-align: center;
  background-color: #1e1e1e; /* Dark background */
  animation: fadeIn 1s ease-in-out;
}

/* Animation for smooth fade-in effect */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Heading */
.gallery-heading {
  font-size: 3rem;
  font-weight: bold;
  margin-bottom: 3rem;
  color: #f5f5f5;
  text-transform: uppercase;
  letter-spacing: 2px;
  border-bottom: 3px solid #28a745;
  display: inline-block;
  padding-bottom: 10px;
}

/* Categories Section */
.categories {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 40px;
}

.category-box {
  position: relative;
  width: 320px;
  height: 220px;
  border-radius: 20px;
  overflow: hidden;
  cursor: pointer;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.4);
  transition: transform 0.4s ease, box-shadow 0.4s ease;
}

.category-box:hover {
  transform: scale(1.08);
  box-shadow: 0 12px 25px rgba(0, 0, 0, 0.5);
}

.category-thumbnail {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.category-label {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 10px;
  background: rgba(0, 0, 0, 0.7);
  color: white;
  font-weight: bold;
  font-size: 1.4rem;
  text-transform: uppercase;
  text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.6);
}

/* Modal for Carousel */
.carousel-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background: rgba(0, 0, 0, 0.85);
  z-index: 1000;
  padding: 1rem;
  overflow: auto;
}

/* Carousel */
.carousel {
  position: relative;
  width: 90%;
  max-width: 1000px;
  background: #2c2c2c;
  padding: 20px;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8);
}

.carousel-wrapper {
  display: flex;
  justify-content: center;
  transition: transform 0.5s ease-in-out;
}

.carousel-item {
  display: none;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.5s ease-in-out;
}

.carousel-item.active {
  display: block;
  opacity: 1;
}

.carousel img {
  width: 100%;
  max-height: 80vh; /* Auto-scaling for smaller devices */
  object-fit: contain; /* Maintain aspect ratio without cropping */
  border-radius: 15px;
}

/* Close Button */
.close-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  background: rgba(255, 0, 0, 0.8);
  color: white;
  border: none;
  font-size: 1.8rem;
  cursor: pointer;
  padding: 10px;
  border-radius: 50%;
  z-index: 10;
}

/* Controls */
.carousel-controls {
  display: flex;
  justify-content: space-between;
  position: absolute;
  width: 100%;
  top: 50%;
  left: 0;
  transform: translateY(-50%);
  pointer-events: none;
}

.prev-btn,
.next-btn {
  background-color: rgba(0, 0, 0, 0.7);
  color: white;
  border: none;
  padding: 15px;
  cursor: pointer;
  font-size: 1.8rem;
  pointer-events: all;
  border-radius: 50%;
  transition: background-color 0.3s ease;
}

.prev-btn:hover,
.next-btn:hover {
  background-color: rgba(40, 167, 69, 0.8);
}

/* Indicators */
.carousel-indicators {
  display: flex;
  justify-content: center;
  margin-top: 15px;
}

.carousel-indicators span {
  width: 14px;
  height: 14px;
  margin: 0 6px;
  background-color: rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  cursor: pointer;
}

.carousel-indicators span.active {
  background-color: rgba(255, 255, 255, 1);
}

/* Responsive Styles */
@media (max-width: 768px) {
  .category-box {
    width: 100%;
  }

  .carousel {
    width: 95%;
    padding: 10px;
  }

  .close-btn {
    font-size: 1.5rem;
    padding: 8px;
  }
}
</style>
