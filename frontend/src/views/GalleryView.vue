<template>
  <div class="gallery-page">
    <h1 class="gallery-title">Our Work</h1>

    <!-- Category Navigation -->
    <div class="category-tabs">
      <div 
        v-for="tab in tabs" 
        :key="tab"
        @click="setActiveTab(tab)"
        :class="['tab', { active: activeTab === tab }]"
      >
        {{ tab }}
      </div>
    </div>

    <!-- Image Grid -->
    <div class="gallery-grid">
      <transition-group name="gallery-fade" mode="out-in">
        <div 
          v-for="image in filteredImages" 
          :key="image"
          class="gallery-item"
          @click="openModal(image)"
        >
          <img :src="image" :alt="getImageAlt(image)" />
        </div>
      </transition-group>
    </div>

    <!-- Modal -->
    <div v-if="showModal" class="modal" @click.self="closeModal">
      <div class="modal-content">
        <img :src="selectedImage" :alt="getImageAlt(selectedImage)" />
        <button class="modal-close" @click="closeModal">×</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeTab: 'All',
      showModal: false,
      selectedImage: null,
      tabs: ['All', 'Fence Work', 'Landscaping Projects', 'Lawn Maintenance', 'Raised Beds', 'Roof Gutters', 'Sodding'],
      imageData: {
        'Fence Work': Array.from({ length: 7 }, (_, i) => `/images/fence_work/fence${i + 1}.jpg`),
        'Landscaping Projects': Array.from({ length: 6 }, (_, i) => `/images/landscaping_projects/landscaping${i + 1}.jpg`),
        'Lawn Maintenance': Array.from({ length: 6 }, (_, i) => `/images/lawn_maintenance/lawn${i + 1}.jpg`),
        'Raised Beds': Array.from({ length: 7 }, (_, i) => `/images/raised_beds/raised_bed${i + 1}.jpg`),
        'Roof Gutters': Array.from({ length: 3 }, (_, i) => `/images/roof_gutters/roof_gutters${i + 1}.jpg`),
        'Sodding': [`/images/sodd/Sodding.jpg`]
      }
    }
  },

  computed: {
    filteredImages() {
      if (this.activeTab === 'All') {
      // Get all images and shuffle them
      const allImages = Object.values(this.imageData).flat()
      return this.shuffleArray([...allImages])
    }
    return this.imageData[this.activeTab] || []
  }
},

  methods: {
    setActiveTab(tab) {
      this.activeTab = tab
    },

    openModal(image) {
      this.selectedImage = image
      this.showModal = true
    },

    closeModal() {
      this.showModal = false
      this.selectedImage = null
    },

    getImageAlt(imagePath) {
      return imagePath.split('/').pop().split('.')[0]
    },

    shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array
}
  }
}
</script>

<style scoped>
.gallery-page {
  padding: 2rem;
  background-color: #f4f1ed;
  min-height: 100vh;
}

.gallery-title {
  text-align: center;
  color: #333;
  font-size: 2.5rem;
  margin-bottom: 2rem;
}

.category-tabs {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}

.tab {
  padding: 0.5rem 1rem;
  cursor: pointer;
  position: relative;
  color: #555;
  transition: color 0.3s;
}

.tab::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: #333;
  transform: scaleX(0);
  transition: transform 0.3s;
}

.tab:hover::after {
  transform: scaleX(0.5);
}

.tab.active {
  color: #000;
}

.tab.active::after {
  transform: scaleX(1);
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
  padding: 1rem;
}

.gallery-item {
  aspect-ratio: 4/3;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: transform 0.3s ease;
}

.gallery-item:hover {
  transform: translateY(-5px);
}

.gallery-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.gallery-item:hover img {
  transform: scale(1.05);
}

/* Modal styles */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.9);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  position: relative;
  max-width: 90vw;
  max-height: 90vh;
}

.modal-content img {
  max-width: 100%;
  max-height: 90vh;
  object-fit: contain;
  border-radius: 4px;
}

.modal-close {
  position: absolute;
  top: -40px;
  right: -40px;
  background: none;
  border: none;
  color: white;
  font-size: 2rem;
  cursor: pointer;
  padding: 1rem;
}

/* Transitions */
.gallery-fade-enter-active,
.gallery-fade-leave-active {
  transition: opacity 0.5s ease;
}

.gallery-fade-enter-from,
.gallery-fade-leave-to {
  opacity: 0;
}

@media (max-width: 768px) {
  .gallery-title {
    font-size: 2rem;
  }

  .tab {
    padding: 0.4rem 0.8rem;
    font-size: 0.9rem;
  }

  .gallery-grid {
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1rem;
    padding: 0.5rem;
  }

  .modal-close {
    top: 10px;
    right: 10px;
  }
}
</style>