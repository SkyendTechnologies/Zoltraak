<script setup lang="ts">
import { ref, onMounted } from "vue";
import { gsap } from "gsap";

import Zlogo from "@/components/logo/Zlogo.vue";

const introSection = ref(null);

onMounted(() => {
  gsap.fromTo(
    introSection.value,
    { opacity: 0, y: 50 },
    { opacity: 1, y: 0, duration: 1, ease: "power4.out" }
  );

  // Animation for cards
  gsap.fromTo(
    ".card",
    { opacity: 0, y: 50, rotateY: 20 },
    { opacity: 1, y: 0, rotateY: 0, duration: 1, stagger: 0.2, ease: "power4.out" }
  );
});
</script>

<template>
  <div class="relative min-h-screen bg-zol-dark-blue-1 text-white overflow-hidden">
    <!-- Hero Section -->
    <section
      ref="introSection"
      class="flex flex-col justify-center items-center h-screen text-center p-4"
    >
      <Zlogo class="animate-fade-in" @animate-logo="animateLogo" :height="520" :width="520" />
      <h1 class="text-5xl lg:text-7xl font-bold tracking-tight animate-fade-in">
        Welcome to <span class="text-zol-cyan">Zoltraak</span>
      </h1>
      <p class="mt-4 text-lg lg:text-xl text-zol-gray">
        Secure file sharing powered by the TON blockchain.
      </p>
      <button
        class="mt-8 px-6 py-3 text-lg bg-zol-cyan hover:bg-zol-dark-cyan transition-transform transform hover:scale-105 rounded-md shadow-lg font-medium"
      >
        Get Started
      </button>
    </section>

    <!-- "Table" Effect with Cards -->
    <section class="flex justify-center items-center py-20 bg-gradient-to-b from-zol-dark-blue-2 to-zol-dark-blue-1">
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          class="card relative bg-zol-dark-blue-6 rounded-xl p-6 shadow-lg hover:shadow-xl transition-all transform hover:-translate-y-2"
        >
          <h3 class="text-xl font-semibold text-zol-cyan">Encryption</h3>
          <p class="mt-2 text-sm text-zol-gray">
            Multi-layered encryption with AetherShield.
          </p>
        </div>
        <div
          class="card relative bg-zol-dark-blue-6 rounded-xl p-6 shadow-lg hover:shadow-xl transition-all transform hover:-translate-y-2"
        >
          <h3 class="text-xl font-semibold text-zol-cyan">Decentralization</h3>
          <p class="mt-2 text-sm text-zol-gray">
            Powered by TON blockchain for unparalleled security.
          </p>
        </div>
        <div
          class="card relative bg-zol-dark-blue-6 rounded-xl p-6 shadow-lg hover:shadow-xl transition-all transform hover:-translate-y-2"
        >
          <h3 class="text-xl font-semibold text-zol-cyan">Speed</h3>
          <p class="mt-2 text-sm text-zol-gray">
            Ultra-fast file sharing with advanced tech.
          </p>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* Animation classes */
.animate-fade-in {
  animation: fadeIn 1.2s ease-in-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
