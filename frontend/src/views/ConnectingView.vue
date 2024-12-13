<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="bg-white shadow-lg rounded-lg p-8 w-full max-w-md">
      <h1 class="text-2xl font-bold text-center text-gray-800 mb-4">
        TON Wallet Authentication
      </h1>
      <p class="text-center text-gray-600 mb-6">
        {{ walletAddress
        ? `Logged in as: ${walletAddress}`
        : "Connect your TON wallet to access the system." }}
      </p>

      <button
        @click="connectTonWallet"
        :disabled="isConnecting"
        class="w-full bg-blue-500 hover:bg-blue-600 text-white font-medium py-2 px-4 rounded-md transition disabled:bg-gray-400 disabled:cursor-not-allowed"
      >
        {{ isConnecting ? "Connecting..." : "Login with TON Wallet" }}
      </button>

      <p v-if="error" class="mt-4 text-center text-red-500">
        {{ error }}
      </p>
      <p v-if="backendMessage" class="mt-4 text-center text-green-500">
        {{ backendMessage }}
      </p>
    </div>
  </div>
</template>

<script lang="ts">
import { reactive } from "vue";
import axios from "axios";

export default {
  setup() {
    const state = reactive({
      walletAddress: "",
      isConnecting: false,
      error: null,
      backendMessage: null,
    });

    const connectTonWallet = async () => {
      state.isConnecting = true;
      state.error = null;
      state.backendMessage = null;

      try {
        // Проверяем наличие TON Wallet
        if (!window.ton) {
          throw new Error("TON Wallet not detected. Please install a TON wallet.");
        }

        // Запрашиваем аккаунты TON
        const accounts = await window.ton.send("ton_requestAccounts");
        if (!accounts || accounts.length === 0) {
          throw new Error("No wallet accounts found.");
        }

        // Отправляем запрос на сервер для проверки или сохранения
        const response = await axios.post("http://localhost:3000/connect", {
          walletAddress: accounts[0],
        });

        state.walletAddress = accounts[0];
        state.backendMessage = response.data.message || "Authentication successful!";
      } catch (error) {
        state.error = error.response?.data?.error || error.message || "Error occurred.";
      } finally {
        state.isConnecting = false;
      }
    };

    return {
      ...state,
      connectTonWallet,
    };
  },
};
</script>

<style>
/* Tailwind CSS используется для оформления */
</style>
