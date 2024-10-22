<template>
  <div class="gallery-wrapper">
    <h2 class="gallery-heading">Explore Our Work</h2>
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

    <div v-if="showCarousel" class="carousel-modal">
      <div class="carousel">
        <button class="close-btn" @click="closeCarousel">✖</button>
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
.gallery-wrapper {
  padding: 2rem;
  text-align: center;
}

.gallery-heading {
  font-size: 2.5rem;
  font-weight: bold;
  margin-bottom: 2rem;
  color: #dddddd;
}

.categories {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 30px;
}

.category-box {
  position: relative;
  width: 300px;
  height: 200px;
  border-radius: 15px;
  overflow: hidden;
  cursor: pointer;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.category-box:hover {
  transform: scale(1.05);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
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
  font-size: 1.2rem;
}

.carousel-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background: rgba(0, 0, 0, 0.8);
  z-index: 1000;
}

.carousel {
  position: relative;
  width: 80%;
  max-width: 900px;
  background: white;
  padding: 20px;
  border-radius: 15px;
}

.carousel-wrapper {
  display: flex;
  transition: transform 0.5s ease-in-out;
  width: 100%;
  justify-content: center;
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
  height: auto;
  border-radius: 10px;
  object-fit: contain;
}

.close-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  background: rgba(0, 0, 0, 0.8);
  color: white;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  padding: 5px 10px;
  border-radius: 50%;
  z-index: 10;
}

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
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
  border: none;
  padding: 10px;
  cursor: pointer;
  font-size: 1.5rem;
  pointer-events: all;
  z-index: 1;
}

.carousel-indicators {
  display: flex;
  justify-content: center;
  margin-top: 10px;
}

.carousel-indicators span {
  width: 12px;
  height: 12px;
  margin: 0 5px;
  background-color: rgba(0, 0, 0, 0.3);
  border-radius: 50%;
  cursor: pointer;
}

.carousel-indicators span.active {
  background-color: rgba(0, 0, 0, 1);
}
</style>
