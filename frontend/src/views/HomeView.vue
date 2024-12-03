<script setup="ts">
import { onMounted } from 'vue';
import { gsap } from 'gsap';

// Анимация GSAP
onMounted(() => {
  gsap.from(".hero-heading", {
    opacity: 0,
    y: -50,
    duration: 1,
    ease: "power2.out",
  });

  gsap.from(".hero-subtitle", {
    opacity: 0,
    y: 50,
    duration: 1.2,
    ease: "power2.out",
    delay: 0.2,
  });

  gsap.from(".cta-button", {
    opacity: 0,
    scale: 0.8,
    duration: 1.5,
    ease: "elastic.out(1, 0.4)",
    delay: 0.5,
  });
});
</script>

<template>
  <div class="min-h-screen bg-zol-dark-blue-1 text-zol-gray flex flex-col items-center justify-center glass-effect">
    <!-- Hero Section -->
    <div class="text-center">
      <h1 class="hero-heading text-5xl md:text-7xl font-bold text-zol-cyan mb-4">
        Zoltraak
      </h1>
      <p class="hero-subtitle text-xl md:text-2xl text-zol-gray max-w-2xl mx-auto">
        Empowering secure blockchain-based file sharing with ZOL and advanced AetherShield encryption.
      </p>
      <div class="mt-8">
        <button class="cta-button px-6 py-3 bg-zol-cyan text-zol-blue-black rounded-full text-lg font-semibold hover:bg-zol-light-cyan transition duration-300">
          Get Started
        </button>
      </div>
    </div>

    <!-- Features Section -->
    <div class="mt-20 max-w-4xl px-6">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="p-6 bg-zol-dark-blue-2 rounded-lg shadow-lg">
          <h3 class="text-lg font-bold text-zol-cyan">Advanced Encryption</h3>
          <p class="text-zol-gray mt-2">
            Experience state-of-the-art data protection with AetherShield integration.
          </p>
        </div>
        <div class="p-6 bg-zol-dark-blue-2 rounded-lg shadow-lg">
          <h3 class="text-lg font-bold text-zol-cyan">Decentralized Storage</h3>
          <p class="text-zol-gray mt-2">
            Secure your files with the power of decentralized technology and TON nodes.
          </p>
        </div>
        <div class="p-6 bg-zol-dark-blue-2 rounded-lg shadow-lg">
          <h3 class="text-lg font-bold text-zol-cyan">ZOL Token Ecosystem</h3>
          <p class="text-zol-gray mt-2">
            Seamlessly transact and manage digital assets within the ZOL ecosystem.
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Добавляем анимацию для секций */
.hero-heading {
  transition: transform 0.3s ease, opacity 0.3s ease;
}

.hero-heading:hover {
  transform: translateY(-5px);
  opacity: 0.9;
}

.hero-subtitle {
  transition: color 0.3s ease;
}

.hero-subtitle:hover {
  color: #3dcff2; /* Яркий циан для взаимодействия */
}
</style>
